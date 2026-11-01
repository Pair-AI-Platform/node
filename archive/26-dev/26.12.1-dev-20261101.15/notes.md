## `ghcr.io/pair-ai-platform/node:26.12.1-dev-20261101.15`

Node.js 26.12.1 (dev). Index digest `sha256:5ad74d865afd0a8be49920a38ac3787906e007cbd9e94ec3fc2bc062f3d2d293`.
Tags: `26.12.1-dev-20261101.15`, `26-dev`, `26.12-dev`, `26.12.1-dev`, `latest-dev`.

### What changed

| Package | From | To |
| :--- | :--- | :--- |
| `libcurl-openssl4` | 8.23.0-r2 | 8.23.0-r3 |
| `ncurses` | 6.6.20261024-r0 | 6.6.20261031-r0 |
| `ncurses-terminfo-base` | 6.6.20261024-r0 | 6.6.20261031-r0 |

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 79 | 277.1 MB | 744.7 MB |
| aarch64 | 79 | 261.4 MB | 794.9 MB |

Main components: `ca-certificates-bundle 20261020-r0`, `glibc-2.44 2.44-r11`, `glibc-2.44-dev 2.44-r11`, `libicu78 78.3-r4`, `libstdc++ 16.2.0-r2`, `libstdc++-dev 16.2.0-r2`, `libuv 1.53.0-r0`, `nodejs-26 26.12.1-r2`, `npm-12 12.2.1-r1`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`, `pnpm-11.8 11.8.0-r5`, `yarn 1.22.22-r8`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 0 / 3 / 3 / 1 |
| aarch64 | 85 / 91 (93.4%) | 107 | 0 / 3 / 3 / 1 |

### Vulnerabilities

| ID | Severity | Package | Installed | Comes from | Fixed upstream in | Architectures |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CVE-2026-101043](https://nvd.nist.gov/vuln/detail/CVE-2026-101043) | High | `pnpm-11.8` | 11.8.0-r5 | `pnpm-11.8 11.8.0-r5` | no fix yet | x86_64, aarch64 |
| [CVE-2026-82392](https://nvd.nist.gov/vuln/detail/CVE-2026-82392) | High | `pnpm-11.8` | 11.8.0-r5 | `pnpm-11.8 11.8.0-r5` | no fix yet | x86_64, aarch64 |
| [CVE-2026-82393](https://nvd.nist.gov/vuln/detail/CVE-2026-82393) | High | `pnpm-11.8` | 11.8.0-r5 | `pnpm-11.8 11.8.0-r5` | no fix yet | x86_64, aarch64 |
| [CVE-2025-15367](https://nvd.nist.gov/vuln/detail/CVE-2025-15367) | Medium | `python-3.13` | 3.13.18_git20261030-r0 | `python-3.13 3.13.18_git20261030-r0` | no fix yet | x86_64, aarch64 |
| [GHSA-3g3m-2fjr-6pw4](https://github.com/advisories/GHSA-3g3m-2fjr-6pw4) | Medium | `glob` | 13.0.6 | `npm-12 12.2.1-r1` | 14.0.2 | x86_64, aarch64 |
| [GHSA-g3hv-75wg-m249](https://github.com/advisories/GHSA-g3hv-75wg-m249) | Medium | `minimatch` | 10.2.3 | `npm-12 12.2.1-r1` | 11.0.1 | x86_64, aarch64 |
| [CVE-2026-103995](https://nvd.nist.gov/vuln/detail/CVE-2026-103995) | Low | `python-3.13` | 3.13.18_git20261030-r0 | `python-3.13 3.13.18_git20261030-r0` | no fix yet | x86_64, aarch64 |

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
cosign verify ghcr.io/pair-ai-platform/node:26.12.1-dev-20261101.15 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/node/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/node:26.12.1-dev-20261101.15 --repo Pair-AI-Platform/node
```
