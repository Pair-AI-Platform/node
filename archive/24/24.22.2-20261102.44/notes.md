## `ghcr.io/pair-ai-platform/node:24.22.2-20261102.44`

Node.js 24.22.2 (runtime). Index digest `sha256:dbcf70d466b8aa88a482cd5cf65a2653742f5c185ecaa864ff09f29b0f4cbe66`.
Tags: `24.22.2-20261102.44`, `24`, `24.22`, `24.22.2`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `glibc-2.44` | 2.44-r11 | 2.44-r12 |
| `glibc-2.44-locale-posix` | 2.44-r11 | 2.44-r12 |
| `ld-linux-2.44` | 2.44-r11 | 2.44-r12 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 21 | 53.7 MB | 142.5 MB |
| aarch64 | 21 | 51.1 MB | 137.0 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r12`, `libicu79 79.1-r1`, `libstdc++ 16.2.0-r2`, `libuv 1.53.0-r0`, `nodejs-24 24.22.2-r0`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`.
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
cosign verify ghcr.io/pair-ai-platform/node:24.22.2-20261102.44 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/node/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/node:24.22.2-20261102.44 --repo Pair-AI-Platform/node
```
