## `ghcr.io/pair-ai-platform/node:26.13.0-20261102.38`

Node.js 26.13.0 (runtime). Index digest `sha256:f2871402ba18062f8f3b731238380cd41cdfc8c657eb79bbec59a46cc73b6ec7`.
Tags: `26.13.0-20261102.38`, `26`, `26.13`, `26.13.0`, `latest`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `nodejs-26` | 26.12.1-r2 | 26.13.0-r0 |
| `icu79-data-full` | (new) | 79.1-r1 |
| `libicu79` | (new) | 79.1-r1 |
| `icu78-data-full` | 78.3-r4 | (removed) |
| `libicu78` | 78.3-r4 | (removed) |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 21 | 57.4 MB | 152.2 MB |
| aarch64 | 21 | 54.9 MB | 149.2 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r11`, `libicu79 79.1-r1`, `libstdc++ 16.2.0-r2`, `libuv 1.53.0-r0`, `nodejs-26 26.13.0-r0`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`.
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
cosign verify ghcr.io/pair-ai-platform/node:26.13.0-20261102.38 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/node/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/node:26.13.0-20261102.38 --repo Pair-AI-Platform/node
```
