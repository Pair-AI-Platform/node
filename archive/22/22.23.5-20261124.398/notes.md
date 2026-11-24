## `ghcr.io/pair-ai-platform/node:22.23.5-20261124.398`

Node.js 22.23.5 (runtime). Index digest `sha256:a8699804488f276df8a54eca083f5d1126f5fc4717a7e5a9a333e3052e584d38`.
Tags: `22.23.5-20261124.398`, `22`, `22.23`, `22.23.5`.

### What changed

No package changed; the image metadata did.

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 15 | 61.6 MB | 191.7 MB |
| aarch64 | 15 | 60.6 MB | 189.0 MB |

Main components: `ca-certificates-bundle 20261020-r1`, `glibc-2.44 2.44-r25`, `libstdc++ 16.2.0-r5`, `nodejs-22-upstream 22.23.5-r0`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 0 / 0 / 3 / 1 |
| aarch64 | 85 / 91 (93.4%) | 107 | 0 / 0 / 3 / 1 |

### Vulnerabilities

| ID | Severity | Package | Installed | Comes from | Fixed upstream in | Architectures |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CVE-2026-115819](https://nvd.nist.gov/vuln/detail/CVE-2026-115819) | Medium | `glibc-2.44` | 2.44-r25 | `glibc-2.44 2.44-r25` | no fix yet | x86_64, aarch64 |
| [CVE-2026-121758](https://nvd.nist.gov/vuln/detail/CVE-2026-121758) | Medium | `glibc-2.44` | 2.44-r25 | `glibc-2.44 2.44-r25` | no fix yet | x86_64, aarch64 |
| [CVE-2026-124024](https://nvd.nist.gov/vuln/detail/CVE-2026-124024) | Medium | `glibc-2.44` | 2.44-r25 | `glibc-2.44 2.44-r25` | no fix yet | x86_64, aarch64 |
| [CVE-2026-100290](https://nvd.nist.gov/vuln/detail/CVE-2026-100290) | Low | `glibc-2.44` | 2.44-r25 | `glibc-2.44 2.44-r25` | no fix yet | x86_64, aarch64 |

*Comes from* is the Wolfi package that brings the affected code into the image; a library bundled inside npm, for example, comes from the npm package. *Fixed upstream in* is the version of the affected code that fixes it; the image gets the fix when the package it comes from ships that version, and the next build after that publishes it.

Hardening-profile rules not passed (x86_64):

- `SV-203649r971535_rule`: The operating system must use mechanisms meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.
- `SV-203739r987791_rule`: The operating system must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.
- `SV-203750r958912_rule`: The operating system must maintain the confidentiality and integrity of information during preparation for transmission.
- `SV-203751r958914_rule`: The operating system must maintain the confidentiality and integrity of information during reception.
- `SV-203776r959006_rule`: The operating system must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.
- `SV-263659r982563_rule`: The operating system must include only approved trust anchors in trust stores or certificate stores managed by the organization.

### Verify

```sh
cosign verify ghcr.io/pair-ai-platform/node:22.23.5-20261124.398 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/node/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/node:22.23.5-20261124.398 --repo Pair-AI-Platform/node
```
