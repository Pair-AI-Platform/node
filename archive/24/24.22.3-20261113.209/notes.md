## `ghcr.io/pair-ai-platform/node:24.22.3-20261113.209`

Node.js 24.22.3 (runtime). Index digest `sha256:c83d10eb55eff56e61ba38db8c020a8cc89f13e6eb2df2567fc1b98821105a93`.
Tags: `24.22.3-20261113.209`, `24`, `24.22`, `24.22.3`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `glibc-2.44` | 2.44-r17 | 2.44-r18 |
| `glibc-2.44-locale-posix` | 2.44-r17 | 2.44-r18 |
| `ld-linux-2.44` | 2.44-r17 | 2.44-r18 |
| `libcrypt1-2.44` | 2.44-r17 | 2.44-r18 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 27 | 55.7 MB | 146.8 MB |
| aarch64 | 27 | 53.0 MB | 142.1 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r18`, `libicu79 79.1-r2`, `libstdc++ 16.2.0-r3`, `libuv 1.53.0-r0`, `nodejs-24 24.22.3-r2`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 0 / 0 / 0 / 0 |
| aarch64 | 85 / 91 (93.4%) | 107 | 0 / 0 / 0 / 0 |

### Vulnerabilities

None found.

Hardening-profile rules not passed (x86_64):

- `SV-203649r971535_rule`: The operating system must use mechanisms meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.
- `SV-203739r987791_rule`: The operating system must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.
- `SV-203750r958912_rule`: The operating system must maintain the confidentiality and integrity of information during preparation for transmission.
- `SV-203751r958914_rule`: The operating system must maintain the confidentiality and integrity of information during reception.
- `SV-203776r959006_rule`: The operating system must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.
- `SV-263659r982563_rule`: The operating system must include only approved trust anchors in trust stores or certificate stores managed by the organization.

### Verify

```sh
cosign verify ghcr.io/pair-ai-platform/node:24.22.3-20261113.209 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/node/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/node:24.22.3-20261113.209 --repo Pair-AI-Platform/node
```
