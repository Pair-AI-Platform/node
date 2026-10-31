#!/usr/bin/env python3
"""Release records, notes and status badges for published images.

    scripts/release.py record <old-packages.txt> <new-packages.txt> <results-dir>
        Prints the record of one published image as JSON. The package files have one
        "<name> <version>" per line; <results-dir> holds results-<family>-<arch>/ from the test
        job. Reads FAMILY, FLAVOR, IMAGE, INDEX, RELEASE and FLOATING from the environment.

    scripts/release.py notes <record.json>
        Prints the release notes of one image as Markdown.

    scripts/release.py pages <record.json> <site-dir>
        Writes the status of one image into the GitHub Pages site: status/<family>.json and the
        shields.io endpoint badges badges/<family>-{stig,vulns,sbom,size,release}.json.
"""
import json
import os
import pathlib
import sys

ARCHES = ["x86_64", "aarch64"]
# Shown in the release notes as the main components of each image (name prefixes, since Wolfi
# names some packages after their version: glibc-2.44, libicu78, openssl-3.6-libssl, ...)
KEY_PREFIXES = ("nodejs-", "glibc-", "libicu", "openssl-", "ca-certificates", "libstdc++", "libuv",
                "npm", "yarn", "pnpm")
SEVERITIES = ["Critical", "High", "Medium", "Low", "Negligible", "Unknown"]


def read_packages(path):
    packages = {}
    for line in pathlib.Path(path).read_text().splitlines():
        if line.strip():
            name, version = line.split(" ", 1)
            packages[name] = version
    return packages


def record(old_path, new_path, results):
    old, new = read_packages(old_path), read_packages(new_path)
    family = os.environ["FAMILY"]
    scans = {}
    node = None
    for arch in ARCHES:
        base = pathlib.Path(results) / f"results-{family}-{arch}"
        image = json.loads((base / "image.json").read_text())
        node = node or image["node"]
        scans[arch] = {
            "digest": image["digest"],
            "sbom": {"packages": image["packages"], "spdx_packages": image["sbom_spdx_packages"]},
            "size": image["size"],
            "stig": json.loads((base / "stig" / "summary.json").read_text()),
            "vulnerabilities": json.loads((base / "vuln" / "summary.json").read_text()),
        }
    return {
        "family": family,
        "flavor": os.environ["FLAVOR"],
        "image": os.environ["IMAGE"],
        "release": os.environ["RELEASE"],
        "floating": os.environ["FLOATING"].split(),
        "digest": os.environ["INDEX"],
        "node": node,
        "first_release": not old,
        "key_packages": [
            f"{n} {new[n]}" for n in sorted(new)
            if n.startswith(KEY_PREFIXES) and not n.endswith(("-locale-posix", "-legacy-allowed"))
        ],
        "packages": {
            "added": sorted(f"{n} {v}" for n, v in new.items() if n not in old),
            "removed": sorted(f"{n} {v}" for n, v in old.items() if n not in new),
            "updated": sorted(
                [n, old[n], new[n]] for n in new if n in old and old[n] != new[n]
            ),
        },
        "scans": scans,
    }


def notes(rec):
    image, release = rec["image"], rec["release"]
    out = [f"## `{image}:{release}`", ""]
    out.append(f"Node.js {rec['node']} ({rec['flavor']}). Index digest `{rec['digest']}`.")
    out.append("Tags: " + ", ".join(f"`{t}`" for t in [release] + rec["floating"]) + ".")
    out += ["", "### What changed", ""]
    pk = rec["packages"]
    if rec["first_release"]:
        out.append("First release of this image.")
    elif not (pk["added"] or pk["removed"] or pk["updated"]):
        out.append("No package changed; the image metadata did.")
    else:
        out += ["| Package | From | To |", "| :--- | :--- | :--- |"]
        out += [f"| `{n}` | {a} | {b} |" for n, a, b in pk["updated"]]
        out += [f"| `{p.split()[0]}` | (new) | {p.split()[1]} |" for p in pk["added"]]
        out += [f"| `{p.split()[0]}` | {p.split()[1]} | (removed) |" for p in pk["removed"]]
    out += ["", "### SBOM and size", "",
            "| Architecture | Packages (SBOM) | Compressed | Installed |",
            "| :--- | :--- | :--- | :--- |"]
    for arch in ARCHES:
        scan = rec["scans"][arch]
        out.append(f"| {arch} | {scan['sbom']['packages']} | {mb(scan['size']['compressed'])} | {mb(scan['size']['installed'])} |")
    out += ["", "Main components: " + ", ".join(f"`{p}`" for p in rec["key_packages"]) + ".",
            "The SPDX SBOMs are attached to this release and to each image as signed attestations."]
    out += ["", "### Scans", "",
            "| Architecture | STIG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |",
            "| :--- | :--- | :--- | :--- |"]
    for arch in ARCHES:
        stig = rec["scans"][arch]["stig"]
        vuln = rec["scans"][arch]["vulnerabilities"]["counts"]
        out.append(
            f"| {arch} | {stig['counts'].get('pass', 0)} / {stig['applicable']} ({stig['score']}%) "
            f"| {stig['counts'].get('notapplicable', 0)} "
            f"| {vuln['Critical']} / {vuln['High']} / {vuln['Medium']} / {vuln['Low']} |"
        )
    failed = rec["scans"]["x86_64"]["stig"]["failed"]
    if failed:
        out += ["", "STIG rules not passed (x86_64):", ""]
        out += [f"- `{f['rule']}`: {f['title']}" for f in failed]
    out += [
        "",
        "### Verify",
        "",
        "```sh",
        f"cosign verify {image}:{release} \\",
        f"  --certificate-identity-regexp '^https://github.com/{os.environ.get('GITHUB_REPOSITORY', '<repo>')}/.github/workflows/build.yml@' \\",
        "  --certificate-oidc-issuer https://token.actions.githubusercontent.com",
        f"gh attestation verify oci://{image}:{release} --repo {os.environ.get('GITHUB_REPOSITORY', '<repo>')}",
        "```",
    ]
    return "\n".join(out) + "\n"


def mb(size):
    return f"{size / 1048576:.1f} MB"


def badge(label, message, color):
    return {"schemaVersion": 1, "label": label, "message": message, "color": color}


def pages(rec, site):
    site = pathlib.Path(site)
    family = rec["family"]
    for d in ("status", "badges"):
        (site / d).mkdir(parents=True, exist_ok=True)
    stig = rec["scans"]["x86_64"]["stig"]
    vulns = {
        s: max(rec["scans"][a]["vulnerabilities"]["counts"].get(s, 0) for a in ARCHES)
        for s in SEVERITIES
    }
    status = {
        "family": family,
        "release": rec["release"],
        "node": rec["node"],
        "digest": rec["digest"],
        "stig": {a: {k: rec["scans"][a]["stig"][k] for k in ("counts", "applicable", "score")} for a in ARCHES},
        "vulnerabilities": {a: rec["scans"][a]["vulnerabilities"]["counts"] for a in ARCHES},
        "sbom": {a: rec["scans"][a]["sbom"] for a in ARCHES},
        "size": {a: rec["scans"][a]["size"] for a in ARCHES},
        "key_packages": rec["key_packages"],
    }
    (site / "status" / f"{family}.json").write_text(json.dumps(status, indent=2) + "\n")
    score = stig["score"]
    color = "brightgreen" if score >= 90 else "yellow" if score >= 75 else "red"
    (site / "badges" / f"{family}-stig.json").write_text(json.dumps(badge(
        "STIG", f"{stig['counts'].get('pass', 0)}/{stig['applicable']} ({score}%)", color)))
    serious = vulns["Critical"] + vulns["High"]
    color = "brightgreen" if serious == 0 and vulns["Medium"] == 0 else "yellow" if serious == 0 else "red"
    (site / "badges" / f"{family}-vulns.json").write_text(json.dumps(badge(
        "CVEs", f"C{vulns['Critical']} H{vulns['High']} M{vulns['Medium']} L{vulns['Low']}", color)))
    x86 = rec["scans"]["x86_64"]
    (site / "badges" / f"{family}-sbom.json").write_text(json.dumps(badge(
        "SBOM", f"{x86['sbom']['packages']} packages", "blue")))
    (site / "badges" / f"{family}-size.json").write_text(json.dumps(badge(
        "size", mb(x86["size"]["compressed"]), "blue")))
    (site / "badges" / f"{family}-release.json").write_text(json.dumps(badge(
        "release", rec["release"], "blue")))


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "record":
        print(json.dumps(record(*sys.argv[2:5]), indent=2))
    elif command == "notes":
        print(notes(json.loads(pathlib.Path(sys.argv[2]).read_text())), end="")
    elif command == "pages":
        pages(json.loads(pathlib.Path(sys.argv[2]).read_text()), sys.argv[3])
    else:
        sys.exit(f"unknown command {command}")
