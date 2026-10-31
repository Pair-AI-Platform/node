## `ghcr.io/pair-ai-platform/node:22.23.4-20261031.7`

Node.js 22.23.4 (runtime). Index digest `sha256:91c9cdf987a6b089727d926c52b4ace23de936045d45c11f8e4c8983a3a4cd58`.
Tags: `22.23.4-20261031.7`, `22`, `22.23`, `22.23.4`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `nodejs-22-upstream` | (new) | 22.23.4-r0 |
| `c-ares` | 1.34.9-r0 | (removed) |
| `icu78-data-full` | 78.3-r4 | (removed) |
| `libbrotlicommon1` | 1.2.1-r2 | (removed) |
| `libbrotlidec1` | 1.2.1-r2 | (removed) |
| `libbrotlienc1` | 1.2.1-r2 | (removed) |
| `libicu78` | 78.3-r4 | (removed) |
| `libnghttp2-14` | 1.70.0-r7 | (removed) |
| `libuv` | 1.53.0-r0 | (removed) |
| `nodejs-22` | 22.23.2-r1 | (removed) |
| `openssl-3.6-libcrypto` | 3.6.5-r6 | (removed) |
| `openssl-3.6-libssl` | 3.6.5-r6 | (removed) |
| `openssl-4.0-libcrypto` | 4.0.3-r8 | (removed) |
| `openssl-4.0-libssl` | 4.0.3-r8 | (removed) |
| `openssl-provider-legacy-allowed` | 4.1.0-r0 | (removed) |
| `zlib` | 1.3.2.1_rc20260921-r1 | (removed) |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 9 | 59.8 MB | 187.3 MB |
| aarch64 | 9 | 58.7 MB | 184.0 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r11`, `libstdc++ 16.2.0-r2`, `nodejs-22-upstream 22.23.4-r0`.
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
cosign verify ghcr.io/pair-ai-platform/node:22.23.4-20261031.7 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/node/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/node:22.23.4-20261031.7 --repo Pair-AI-Platform/node
```
