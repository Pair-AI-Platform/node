## `ghcr.io/pair-ai-platform/node:26.13.1-20261113.200`

Node.js 26.13.1 (runtime). Index digest `sha256:06addcc07ba8d66873c41052263104cca08011f7ac8061ca7e95645dbeca022d`.
Tags: `26.13.1-20261113.200`, `26`, `26.13`, `26.13.1`, `latest`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `nodejs-26` | 26.13.1-r0 | 26.13.1-r1 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 27 | 59.2 MB | 156.6 MB |
| aarch64 | 27 | 56.7 MB | 154.2 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r17`, `libicu79 79.1-r2`, `libstdc++ 16.2.0-r3`, `libuv 1.53.0-r0`, `nodejs-26 26.13.1-r1`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`.
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
cosign verify ghcr.io/pair-ai-platform/node:26.13.1-20261113.200 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/node/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/node:26.13.1-20261113.200 --repo Pair-AI-Platform/node
```
