# Node.js Images on Wolfi

[![SLSA Build L3](https://img.shields.io/badge/SLSA-Build%20L3-orange?style=for-the-badge)](#slsa-build-level-3)
[![Signed with Sigstore](https://img.shields.io/badge/signed-Sigstore%20keyless-purple?style=for-the-badge)](#verify)

Minimal, non-root Node.js container images for `linux/amd64` and `linux/arm64`, built with
[apko](https://github.com/chainguard-dev/apko) from [Wolfi](https://github.com/wolfi-dev) packages.
Every image is rebuilt daily and published again only when its content changed. Every version is:

- **tested** on both architectures;
- **scanned** with OpenSCAP against a hardening profile derived from the DISA General Purpose
  Operating System SRG, and for known vulnerabilities with Grype;
- **signed** keyless with Sigstore;
- **attested** with its SBOM, its scan results and SLSA Build Level 3 provenance.

These images ship Node.js and nothing more. The cryptography profile (for example FIPS 140-3) is
chosen per application and per contract, and is provided separately: see [Cryptography](#cryptography).

## Alignment at a glance

| Area | Aligned with | Evidence in every release |
| :--- | :--- | :--- |
| **Hardening** | OpenSCAP profile derived from the DISA General Purpose Operating System SRG (not an official DISA STIG for containers) | Rules passed out of the applicable ones (about 93% on `node:22`), the full report, a signed attestation; see [Security scans](#security-scans) |
| **🇸🇦 Saudi Arabia** | NCA ECC-2:2024 1-6-2-2, 1-6-3-2, 1-6-3-5, 2-1, 2-2-3-3, 2-10-3 · NCA CCC-2:2024 2-3-P-1-3, 2-3-P-1-7, 2-9-T-1-1, 4-1-P-1-2 · NCA CSCC-1:2019 2-3-1-1, 2-3-1-7 · SAMA CSF 3.3.8, 3.3.17 | Minimal non-root baseline, STIG and vulnerability results, SBOM, signatures, provenance |
| **🇰🇼 Kuwait** | CBK CORF 5.3.1.2–5.3.1.5 (hardening against recognized benchmarks), 5.8.1.3 (SBOM), 5.13 (vulnerability and patch management) · NCSC NBCC PR-1, ID-2 | Same, plus daily rebuilds |
| **🇦🇪 UAE** | UAE IA Regulation T3.2.1, T5.5.4, T7.5.1, T7.7.1, T7.8.1 | Same; the scans use the SCAP formats (XCCDF, OVAL, CVE, CVSS) T7.7 names |
| **🇧🇭 Bahrain · 🇴🇲 Oman** | CBB OM-5.5.18, OM-5.5.25, OM-5.5.27, Appendix C · ITA Basic Security Controls 5.5, 5.6, 5.8 | Same |
| **🔐 Cryptography** | FIPS 140-3, CMVP #4985 (security policy §11.1) · 🇸🇦 NCA NCS-1:2020 MODERATE §2.1.2, §2.2, §2.3, §3.1–§3.3, §3.6.2, §3.8, §4.2, §5.1 · NCA ECC-2:2024 2-8-3 · NCA DCC-1:2022 2-5-1-2 · SAMA CSF 3.3.9 · 🇰🇼 CBK CORF 5.3.1.3(i), 5.7.1.3, 8.1.4.5 · 🇶🇦 Qatar National Cryptographic Standard v1.0 Tables 1, 2, 4, 5, 7, 10 · 🇦🇪 UAE IA Regulation T7.4.1 · 🇧🇭 CBB OM Appendix C (Data Security 1–2) | Provided by **[khatm](https://github.com/Pair-AI-Platform/khatm)** when the application or contract requires it, with its clause-by-clause mapping and the tests behind each setting |

The images give the technical controls and the evidence for them; running them, the scanning
cadence, change approval, key management and hardware key storage stay with the operator. The
clause-by-clause table, with links to every document, is in
[Gulf cybersecurity rules at the container level](#gulf-cybersecurity-rules-at-the-container-level).

## Images

`ghcr.io/pair-ai-platform/node:<tag>`. The numbers come from the newest release of each image
and update with every release; click a badge for the details on the image's page:

- **Hardening profile:** rules passed out of the applicable ones, with the full OpenSCAP report.
- **Vulnerabilities:** counts by severity (Critical / High / Medium / Low); the page lists every
  CVE with the affected package and the version that fixes it.
- **SBOM:** packages on amd64 / arm64; the page lists every package with its version and license,
  and links each architecture's SPDX file.
- **Size:** compressed. Each image's [GitHub releases](../../releases) have the same numbers for both
architectures, plus what changed.

| Image | Node.js line | Hardening profile (x86_64) | Vulnerabilities | SBOM | Size | Newest release |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `node:26` · `latest` | Active LTS, until April 2029 | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-stig.json)](https://pair-ai-platform.github.io/node/images/26.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-vulns.json)](https://pair-ai-platform.github.io/node/images/26.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-sbom.json)](https://pair-ai-platform.github.io/node/images/26.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-release.json)](https://pair-ai-platform.github.io/node/images/26.html) |
| `node:26-dev` · `latest-dev` | Active LTS, until April 2029 | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-dev-stig.json)](https://pair-ai-platform.github.io/node/images/26-dev.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-dev-vulns.json)](https://pair-ai-platform.github.io/node/images/26-dev.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-dev-sbom.json)](https://pair-ai-platform.github.io/node/images/26-dev.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-dev-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/26-dev-release.json)](https://pair-ai-platform.github.io/node/images/26-dev.html) |
| `node:24` | Maintenance LTS, until April 2028 | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-stig.json)](https://pair-ai-platform.github.io/node/images/24.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-vulns.json)](https://pair-ai-platform.github.io/node/images/24.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-sbom.json)](https://pair-ai-platform.github.io/node/images/24.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-release.json)](https://pair-ai-platform.github.io/node/images/24.html) |
| `node:24-dev` | Maintenance LTS, until April 2028 | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-dev-stig.json)](https://pair-ai-platform.github.io/node/images/24-dev.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-dev-vulns.json)](https://pair-ai-platform.github.io/node/images/24-dev.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-dev-sbom.json)](https://pair-ai-platform.github.io/node/images/24-dev.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-dev-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/24-dev-release.json)](https://pair-ai-platform.github.io/node/images/24-dev.html) |
| `node:22` | Maintenance LTS, until April 2027 | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-stig.json)](https://pair-ai-platform.github.io/node/images/22.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-vulns.json)](https://pair-ai-platform.github.io/node/images/22.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-sbom.json)](https://pair-ai-platform.github.io/node/images/22.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-release.json)](https://pair-ai-platform.github.io/node/images/22.html) |
| `node:22-dev` | Maintenance LTS, until April 2027 | [![GPOS SRG profile](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-dev-stig.json)](https://pair-ai-platform.github.io/node/images/22-dev.html#stig) | [![CVEs](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-dev-vulns.json)](https://pair-ai-platform.github.io/node/images/22-dev.html#vulnerabilities) | [![SBOM](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-dev-sbom.json)](https://pair-ai-platform.github.io/node/images/22-dev.html#sbom) | ![size](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-dev-size.json) | [![release](https://img.shields.io/endpoint?url=https://pair-ai-platform.github.io/node/badges/22-dev-release.json)](https://pair-ai-platform.github.io/node/images/22-dev.html) |

Support dates are from the [Node.js release schedule](https://github.com/nodejs/Release). Only
supported lines are built; when a line reaches its end of life, its images stop being published.

Node.js 24 and 26 are Wolfi packages. Node.js 22 comes from the official nodejs.org binaries,
signature-verified and packaged here, because Wolfi stopped updating its Node.js 22 package in
August 2026; see [Where Node.js comes from](docs/NODE-SOURCES.md).

| Flavor | Contents |
| :--- | :--- |
| runtime (`node:22`) | Node.js, CA certificates and time zones. No shell, no package manager, no npm. Runs as `node` (1000:1000) in `/app`. |
| development (`node:22-dev`) | The runtime plus `bash`, busybox, npm, yarn, pnpm, git, the C/C++ toolchain and Python for native modules (node-gyp). For building, not for running. |

```dockerfile
FROM ghcr.io/pair-ai-platform/node:22-dev AS build
COPY --chown=node:node package*.json ./
RUN npm ci --omit=dev
COPY --chown=node:node . .

FROM ghcr.io/pair-ai-platform/node:22
COPY --from=build /app /app
CMD ["server.js"]
```

The entrypoint is `/usr/bin/node`, so `CMD` names the script. Pin the image by digest in
production (`node:22@sha256:…`).

---

## Tags and versions

| Tag | Example | Moves? |
| :--- | :--- | :--- |
| Release | `22.23.2-20261031.57`, `22.23.2-dev-20261031.57` | Never. One per published version, with its own [GitHub release](../../releases) |
| Patch | `22.23.2`, `22.23.2-dev` | To the newest release of that Node.js version |
| Minor and major | `22.23`, `22`, `22-dev` | To the newest release of that line |
| `latest`, `latest-dev` | | To the newest release of the Active LTS line (26) |

Every run takes each image through these steps; a version exists for users only after the last one:

| Step | What happens | If it fails |
| :--- | :--- | :--- |
| 1. Build and test | apko builds the image natively on x86_64 and aarch64; image tests, hardening-profile and vulnerability scans run on each | Nothing is published |
| 2. Compare | Both architectures are built together; each must be byte for byte the image tested in step 1. If the result equals the image under the floating tag (`22`), nothing changed and the run stops here for that image | Nothing is published |
| 3. Publish by digest | The image is pushed to GHCR without any tag | Untagged, invisible to users; the cleanup deletes it |
| 4. Sign, attest, verify | Sigstore signatures; SBOM, hardening-profile, vulnerability and SLSA provenance attestations; all verified | Still untagged |
| 5. Tag | The release tag (`22.23.2-20261031.57`) and the floating tags move to the new digest | A re-run of the failed job tags it |
| 6. Release | A GitHub release with the changes, the scan results, the SBOMs and the OpenSCAP report, created only if the tag exists on that digest; the badges are updated | A re-run of the failed job creates it |
| 7. Keep five | The five newest versions of each image stay, in GHCR and as GitHub releases | Never fails a release; runs again next time |

- **Only changed images are published.** The builds are reproducible: the same packages give the
  same digest. The daily rebuild publishes an image only when Wolfi shipped a new version of
  something inside it, or the image definition changed.
- **Release tags never move and never point to an image without its evidence.** Floating tags
  always point to a kept, signed version.
- **Retention: five versions per image.** GHCR and the GitHub releases keep the five newest versions
  of each image (`22`, `22-dev`, `24`, …). A new version is published only when the content
  changed, not on every daily build, so five versions cover several weeks.
- **The evidence outlives the image.** For every version ever published, these stay available after
  the image itself is deleted:
  - `https://pair-ai-platform.github.io/node/archive/<image>/<release>/` (for example
    `archive/22/22.23.2-20261031.2/`) keeps the release record (digest, packages, changes), both SBOMs, the OpenSCAP reports, the
    vulnerability findings and the notes;
  - the Sigstore transparency log (Rekor) permanently records every signature and attestation.

  Together they show what any image digest contained on any date. To keep the images themselves
  longer, mirror them into your own registry with their referrers (`oras cp -r`).
- **Every release says what changed**: the packages added, removed or updated since the previous
  version, with the SBOM package count, the size, the main components and the scan results on both
  architectures.

---

## Security scans

### Hardening profile (OpenSCAP, DISA GPOS SRG)

This is not an official DISA STIG for containers: DISA publishes none. Each image is scanned on both
architectures with OpenSCAP against the content that Wolfi
publishes in the `chainguard-security-guide` package (Apache-2.0): the `xccdf_basic_profile_.check`
profile of `ssg-chainguard-gpos-ds.xml`, which is based on the DISA General Purpose Operating System
SRG. The scanner is built from the Wolfi packages `openscap` and `chainguard-security-guide`. Results:

- The badges above show the newest release.
- Every GitHub release has the counts for both architectures and the full HTML report.
- Each image carries its results as a signed attestation.

The score is *rules passed ÷ rules applicable*. Rules that cannot apply to a container (no kernel,
boot loader, SSH, login or audit daemon, about 107 of 198) are reported as *not applicable* and
counted on neither side.

A typical run on `node:22` passes 85 of 91 applicable rules (93.4%). The rules that do not pass,
and why:

| Rule | Why it does not pass | Where it is handled |
| :--- | :--- | :--- |
| SV-203649, SV-203739, SV-203750, SV-203751, SV-203776 | They require FIPS-validated cryptography. These images use Wolfi's standard OpenSSL | A cryptography profile, when the contract requires one: see [Cryptography](#cryptography) |
| SV-263659 (approved trust anchors) | The rule also reads `SSL_CERT_FILE` from the running processes, and a scan of an image has no processes | The image sets `SSL_CERT_FILE`, and the image tests check that the CA bundle matches its checksum stamp, which is the rest of this rule |

### Vulnerabilities (Grype)

Each image is scanned with [Grype](https://github.com/anchore/grype) on both architectures, and
the counts per severity are in the badges, the GitHub releases and a signed attestation. Most
findings in Wolfi images already have a fix in Wolfi: the next daily rebuild picks it up and
publishes a new version.

### Image tests

On both architectures, before anything is published:

- **Both flavors:**
  - Node.js runs as 1000:1000 in a writable `/app`.
  - `SSL_CERT_FILE` is set, and the CA bundle loads and matches its checksum stamp.
- **Runtime images:** have no shell and no package manager.
- **Development images:** npm, yarn, pnpm, git, gcc, g++, Python and bash work, and `npm install`
  installs a package.

---

## Verify

| Evidence | Attached to | Verify with |
| :--- | :--- | :--- |
| Sigstore signature (keyless, logged in Rekor) | the index and each platform image | `cosign verify` |
| SPDX SBOM | each platform image | `cosign verify-attestation --type spdxjson` |
| Hardening-profile results (OpenSCAP) | each platform image | `cosign verify-attestation --type https://github.com/Pair-AI-Platform/node/attestations/stig/v1` |
| Vulnerability scan | each platform image | `cosign verify-attestation --type https://github.com/Pair-AI-Platform/node/attestations/vulnerabilities/v1` |
| SLSA v1 build provenance | the index | `gh attestation verify` |

```sh
IMAGE=ghcr.io/pair-ai-platform/node:22
WORKFLOW=Pair-AI-Platform/node/.github/workflows/build.yml

cosign verify "$IMAGE" \
  --certificate-identity-regexp "^https://github.com/$WORKFLOW@" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com

gh attestation verify "oci://$IMAGE" --repo Pair-AI-Platform/node --signer-workflow "$WORKFLOW"

# Hardening-profile results of the arm64 image
cosign verify-attestation "$IMAGE" --platform linux/arm64 \
  --type https://github.com/Pair-AI-Platform/node/attestations/stig/v1 \
  --certificate-identity-regexp "^https://github.com/$WORKFLOW@" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  | jq '.payload | @base64d | fromjson | .predicate | {counts, applicable, score}'

oras discover --format tree "$IMAGE"
```

---

## SLSA Build Level 3

| Requirement | How it is met |
| :--- | :--- |
| Provenance exists and is complete | `actions/attest-build-provenance` records the source commit, workflow, inputs and runner for every published image |
| Provenance is authentic | Signed through Sigstore with the build workflow's OIDC identity and logged in Rekor; checked again before the image is tagged |
| Hosted, ephemeral build platform | GitHub-hosted runners: `ubuntu-24.04` (x86_64) and `ubuntu-24.04-arm` (aarch64), with no emulation |
| Isolated build, provenance not forgeable by it | Building, signing and attesting run inside the reusable workflow `.github/workflows/build.yml`, whose identity signs the provenance; callers can only pass `publish: true/false` |

---

## Cryptography

The Node.js 24 and 26 images use the OpenSSL that Wolfi ships, with its default settings; Node.js 22
uses the OpenSSL built into the official binary ([details](docs/NODE-SOURCES.md)). Which
cryptography profile an application needs depends on the software and on the contract: none, or
FIPS 140-3 with a profile aligned with a national standard. That profile is not built into these
images. It comes from **[khatm](https://github.com/Pair-AI-Platform/khatm)**, which provides:

- the OpenSSL FIPS Provider 3.1.2 (FIPS 140-3, CMVP #4985);
- `fipshardened`, a compatible TLS policy;
- `fips-strict`, the NCA NCS-1:2020 MODERATE TLS policy;
- a clause-by-clause mapping to the Gulf cryptography rules (NCA NCS-1, Qatar QNCS, CBK CORF).

---

## Gulf cybersecurity rules at the container level

*Checked on 31 October 2026 against the primary text, unless a row says **secondary**. This is
technical information, not legal advice.*

None of these documents mentions containers, container images, STIG or SCAP by name. Their
requirements on hardening, vulnerability management, software inventory and supply chain apply to
the systems that run the images. What these images give is the **evidence** for those controls:

- a minimal, hardened, non-root baseline;
- per-release hardening-profile (DISA GPOS SRG) and vulnerability results;
- an SBOM;
- signatures and provenance.

Running the images, keeping the scanning cadence and approving changes stay with the operator. The
closest references are in two documents:

- **Kuwait CBK CORF 5.3.1.2** names the CIS benchmarks.
- **The UAE IA Regulation (T7.7)** names the SCAP formats (XCCDF, OVAL, CVE, CVSS) that OpenSCAP
  and Grype produce.

### Saudi Arabia 🇸🇦

| Document | Clause | Requirement | What the images provide | Stays with the operator |
| :--- | :--- | :--- | :--- | :--- |
| [NCA ECC-2:2024](https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf) | 1-6-2-2, 1-6-3-5 | "Reviewing secure configuration and hardening and updates packages before launching" | OpenSCAP results and package changes in every release | The review before go-live |
| | 1-6-3-2 | "Using trusted and licensed sources for software development tools and libraries" | Wolfi packages, signatures, SLSA provenance | Verifying signatures on admission |
| | 2-1 | Accurate and updated inventory of assets | SPDX SBOM per architecture | Loading SBOMs into the inventory |
| | 2-2-3-3 | Least privilege | Non-root (1000:1000), no shell in runtime images | Pod security context, RBAC |
| | 2-3-3-3, 2-10-3 | Patch management; periodic vulnerability assessment, classification by severity, tested patches | Daily rebuilds, Grype results per release | Classification, remediation targets, testing, redeploying |
| [NCA CCC-2:2024](https://cdn.nca.gov.sa/api/files/public/upload/6d5408a3-d8e6-4e96-963b-2c7198e5b7c2_CCC-2-2024-EN-.pdf) | 2-3-P-1-3 | "technical system configurations adhering to the minimum functionality principle" | Distroless runtime with minimal packages | The provider's configuration standard |
| | 2-3-P-1-7 | "Detection and prevention of unauthorized changes to software programs" | Signatures and digests | Admission policy, read-only root filesystem |
| | 2-9-P-1-1, 2-9-T-1-1 | Vulnerability assessments (monthly or quarterly) | Results per release | Scanning running workloads on that schedule |
| | 4-1-P-1-2 | Security documentation for supplied equipment and services | SBOM, provenance, scan reports | Keeping them |
| [NCA CSCC-1:2019](https://cdn.nca.gov.sa/api/files/public/upload/f15af01c-dc59-4281-95e2-03a770655937_Critical-Systems-Cybersecurity-Controls.pdf) | 2-3-1-1 | Whitelisting of software allowed to execute | Minimal file set, no shell or package manager | Admission allowlist of digests |
| | 2-3-1-6, 2-3-1-7 | Review hardening every six months; remove default passwords | OpenSCAP report every release; no accounts with passwords | The six-monthly review |
| | 2-9-1-3 | "Immediately remediating for critical vulnerabilities" | Daily rebuilds | Emergency redeploys |
| [SAMA Cyber Security Framework](https://rulebook.sama.gov.sa/sites/default/files/en_net_file_store/SAMA_EN_3837_VER1.pdf) | 3.3.8 (6)(a),(d),(f),(g) | Configuration parameters, approved software, application whitelisting, vulnerability and patch management | Minimal, signed images | The infrastructure standard |
| | 3.3.17 (3)(b),(d),(f) | Scan frequency, mitigation timelines, patch deployment | Results per release | The timelines (SAMA sets none) |

### Kuwait 🇰🇼

| Document | Clause | Requirement | What the images provide | Stays with the operator |
| :--- | :--- | :--- | :--- | :--- |
| [CBK CORF v1.0](https://www.cbk.gov.kw/en/images/corf-170113_v10_tcm10-170113.pdf) | 5.3.1.2 | Configuration standards "based on global best practices (such as NIST, Center for Internet Security (CIS) benchmarks)" | OpenSCAP results against the DISA GPOS SRG-derived profile; CIS is not run | Choosing and justifying the benchmark |
| | 5.3.1.3 (a,b,c,e,f) | Only supported software, minimum components, up-to-date updates, no unnecessary services, no unneeded accounts | Distroless, minimal, rebuilt daily, non-root | Approving versions, network policy |
| | 5.3.1.4, 5.3.1.5 | Quarterly checks against configuration standards; testing before go-live | OpenSCAP results per release | Quarterly checks of running systems |
| | 5.8.1.3 | "all software … accompanied by an up-to-date Software Bill of Materials (SBOM)" | SPDX SBOM per architecture, signed | SBOMs for the application layers added on top |
| | 5.13.1.2, 5.13.2.2–5.13.2.4 | Assessments for missing updates and baselines; risk-based patching; emergency patches immediately | Daily rebuilds, results per release | Patching schedule, exception register |
| [NCSC NBCC](https://github.com/SiteQ8/Kuwait-NBCC) (Decision 2/2026, **secondary**) | PR-1, PR-1.2, ID-2 | Hardened baselines, monthly or quarterly scans, monthly patches, list of authorized software | Hardened images, scans, SBOM | Cadence and the authorized-software list |

### United Arab Emirates 🇦🇪

| Document | Clause | Requirement | What the images provide | Stays with the operator |
| :--- | :--- | :--- | :--- | :--- |
| [UAE IA Regulation v1.1](https://web.archive.org/web/2025/https://u.ae/-/media/guidelines/Guidelines-2020/UAE-IA-Regulation-v11-1.pdf) (TDRA) | T3.2.1 | "define minimum security configurations"; guidance: build standard images and watch for deviations | Standard hardened images with OpenSCAP results | Drift monitoring |
| | T5.2.2, T5.5.4 | Restrict privileges and utility programs | Non-root; no shell or package manager in runtime images | Runtime privileges |
| | T7.5.1 | "operational systems should only hold approved executable code, and not development code or compilers" | Separate runtime and development images | Deploying only runtime images |
| | T7.7.1 | Identify vulnerabilities before production, with tools based on CVE, CCE, OVAL, CPE, CVSS, XCCDF | Grype (CVE, CVSS) and OpenSCAP (XCCDF, OVAL) on every build | Remediation plan and timeline |
| | T7.8.1 | Check every delivered product's compliance with security requirements | Signatures, provenance and attestations make this checkable | Verifying on receipt |

### Bahrain 🇧🇭 and Oman 🇴🇲

| Document | Clause | Requirement | What the images provide | Stays with the operator |
| :--- | :--- | :--- | :--- | :--- |
| [CBB Rulebook Vol. 1, OM](https://cbben.thomsonreuters.com/sites/default/files/net_file_store/Vol_1_OM_April_2023.pdf) | OM-5.5.18 (d),(h) | Security testing at development and after deployment; list of whitelisted applications and components | Build-time scans; SBOM as component list | Post-deployment testing |
| | OM-5.5.25, OM-5.5.27 | Monthly (internal) or weekly (external) assessments; patches in risk-based timeframes | Results per release; daily rebuilds | Cadence and timeframes |
| | Appendix C | Integrity checking of software; baseline configuration with least functionality; quarterly scans | Signatures; minimal baseline; scans | Change control |
| [ITA Basic Security Controls v1.0](https://www.moheri.gov.om/userupload/Policy/Basic%20Security%20Controls%20Guidelines.pdf) (Oman, 2017) | 5.5, CM.2–CM.8, 5.6, 5.8 | Baseline configurations, least functionality, component inventory, scheduled scanning, patch management | Hardened baseline, SBOM, scans, rebuilds | Schedules and change management |

**Not verified in primary text:**
- **Kuwait:** the official NBCC annex.
- **UAE:** Dubai DESC ISR and the CBUAE rules (no public text).
- **Qatar:** the NIA Policy and Standard (the sites were unreachable).
- **Saudi:** NCA's software-supply-chain guidance, if it exists.

---

## How updates reach the images

| What | How |
| :--- | :--- |
| Packages inside the images (Node.js, OpenSSL, glibc, …) | Not pinned. The daily build takes the current Wolfi packages and publishes each image whose content changed |
| apko, OpenSCAP and Grype images, oras, cosign, GitHub Actions | Pinned by digest or version. [Renovate](renovate.json) opens a pull request, which is automerged once the builds, tests and scans pass |
| Node.js 22 (official nodejs.org binaries) | Renovate tracks the nodejs.org releases and the Node.js release keys; the pull request is automerged once the images pass ([details](docs/NODE-SOURCES.md)) |
| A new Node.js line | Add `apko/nodejs-<major>.apko.yaml` and `-dev.apko.yaml` |

## Build locally

Needs Docker, curl and cosign. The tools come from their GitHub releases, verified, and the OpenSCAP
scanner is built from Wolfi packages; no other container registry is involved.

```sh
scripts/install-tools.sh ./bin apko
./bin/apko build scanner/stig-scanner.apko.yaml stig-scanner:local scanner.tar --arch x86_64
docker load -i scanner.tar                      # stig-scanner:local-amd64

./bin/apko build apko/nodejs-22.apko.yaml node:22 node-22.tar --arch x86_64
docker load -i node-22.tar                      # node:22-amd64
scripts/test-image.sh node:22-amd64 runtime
OPENSCAP_IMAGE=stig-scanner:local-amd64 scripts/stig-scan.sh node:22-amd64 out/stig
scripts/vuln-scan.sh node:22-amd64 out/vuln
```

## Layout

```
apko/nodejs-<major>[-dev].apko.yaml   image definitions
melange/nodejs-22-upstream.yaml       Node.js 22 from nodejs.org, signature and checksum verified
keys/node-packages.rsa.pub            public key of the packages built here
docs/NODE-SOURCES.md                  where each Node.js line comes from, and why
scanner/stig-scanner.apko.yaml        the OpenSCAP scanner (Wolfi: openscap, chainguard-security-guide)
scripts/install-tools.sh              apko from its GitHub release, signature and checksum verified
scripts/plan.py                       list of images for the build matrix
scripts/test-image.sh                 image tests
scripts/stig-scan.sh                  OpenSCAP scan against the DISA GPOS SRG-derived profile
scripts/vuln-scan.sh                  Grype scan
scripts/release.py                    release records, notes and status badges
.github/workflows/build.yml           reusable: build, test, scan, publish, sign, attest (SLSA L3)
.github/workflows/pr.yml              checks for every pull request
.github/workflows/release.yml         daily and on merge: publish, releases, badges, keep five
.github/workflows/renovate.yml        self-hosted Renovate for this repository
MAINTAINING.md                        repository settings
```

## License

The code in this repository (image definitions, workflows, scripts and documentation) is licensed
under the [Apache License 2.0](LICENSE). The software inside the images keeps its own license
(Node.js: MIT); the SBOM of every image lists the license of each package. [NOTICE](NOTICE) lists
the third-party software, where to get the source of the GPL and LGPL packages, the tools used in
the pipeline, and the trademarks.
