## `ghcr.io/pair-ai-platform/node:24.22.3-20261111.179`

Node.js 24.22.3 (runtime). Index digest `sha256:5e45b040850dcfda0ea54af1b7b258f4e78e030a393f5aaa2bbab8bc91da5c3b`.
Tags: `24.22.3-20261111.179`, `24`, `24.22`, `24.22.3`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `nodejs-24` | 24.22.2-r2 | 24.22.3-r0 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 27 | 55.8 MB | 146.8 MB |
| aarch64 | 27 | 53.0 MB | 142.1 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r16`, `libicu79 79.1-r2`, `libstdc++ 16.2.0-r3`, `libuv 1.53.0-r0`, `nodejs-24 24.22.3-r0`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 0 / 1 / 0 / 0 |
| aarch64 | 85 / 91 (93.4%) | 107 | 0 / 1 / 0 / 0 |

### Vulnerabilities

| ID | Severity | Package | Installed | Comes from | Fixed upstream in | Architectures |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CVE-2026-84243](https://nvd.nist.gov/vuln/detail/CVE-2026-84243) | High | `glibc-2.44` | 2.44-r16 | `glibc-2.44 2.44-r16` | no fix yet | x86_64, aarch64 |

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
cosign verify ghcr.io/pair-ai-platform/node:24.22.3-20261111.179 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/node/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/node:24.22.3-20261111.179 --repo Pair-AI-Platform/node
```
