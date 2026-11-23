## `ghcr.io/pair-ai-platform/node:22.23.5-dev-20261123.385`

Node.js 22.23.5 (dev). Index digest `sha256:eee3d2a2a11b4633fdee2a6142928eb216627547da630bd0830495f2cc2d4fb6`.
Tags: `22.23.5-dev-20261123.385`, `22-dev`, `22.23-dev`, `22.23.5-dev`.

### What changed

No package changed; the image metadata did.

### SBOM and size

| Architecture | Packages (SBOM) | Compressed | Installed |
| :--- | :--- | :--- | :--- |
| x86_64 | 76 | 283.7 MB | 790.6 MB |
| aarch64 | 76 | 269.2 MB | 840.0 MB |

Main components: `ca-certificates-bundle 20261020-r1`, `glibc-2.44 2.44-r24`, `glibc-2.44-dev 2.44-r24`, `libstdc++ 16.2.0-r5`, `libstdc++-dev 16.2.0-r5`, `nodejs-22-upstream 22.23.5-r0`, `npm 12.0.2-r0`, `openssl-4.0-libcrypto 4.0.3-r8`, `openssl-4.0-libssl 4.0.3-r8`, `pnpm-11.8 11.8.0-r6`, `yarn 1.22.22-r9`.
The SPDX SBOMs are attached to this release and to each image as signed attestations.

### Scans

| Architecture | Hardening profile, DISA GPOS SRG (applicable rules passed) | Not applicable | Vulnerabilities (C / H / M / L) |
| :--- | :--- | :--- | :--- |
| x86_64 | 85 / 91 (93.4%) | 107 | 0 / 11 / 23 / 4 |
| aarch64 | 85 / 91 (93.4%) | 107 | 0 / 11 / 23 / 4 |

### Vulnerabilities

| ID | Severity | Package | Installed | Comes from | Fixed upstream in | Architectures |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CVE-2026-101043](https://nvd.nist.gov/vuln/detail/CVE-2026-101043) | High | `pnpm-11.8` | 11.8.0-r6 | `pnpm-11.8 11.8.0-r6` | no fix yet | x86_64, aarch64 |
| [CVE-2026-82392](https://nvd.nist.gov/vuln/detail/CVE-2026-82392) | High | `pnpm-11.8` | 11.8.0-r6 | `pnpm-11.8 11.8.0-r6` | no fix yet | x86_64, aarch64 |
| [CVE-2026-82393](https://nvd.nist.gov/vuln/detail/CVE-2026-82393) | High | `pnpm-11.8` | 11.8.0-r6 | `pnpm-11.8 11.8.0-r6` | no fix yet | x86_64, aarch64 |
| [GHSA-2m5v-pch6-74hx](https://github.com/advisories/GHSA-2m5v-pch6-74hx) | High | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.29.1 | x86_64, aarch64 |
| [GHSA-6j4f-fj2g-mc7p](https://github.com/advisories/GHSA-6j4f-fj2g-mc7p) | High | `brace-expansion` | 5.0.8 | `npm 12.0.2-r0` | 5.0.10 | x86_64, aarch64 |
| [GHSA-mwp4-54f8-5fhr](https://github.com/advisories/GHSA-mwp4-54f8-5fhr) | High | `ip-address` | 10.2.0 | `npm 12.0.2-r0` | 10.3.1 | x86_64, aarch64 |
| [GHSA-qhr7-859c-m2p7](https://github.com/advisories/GHSA-qhr7-859c-m2p7) | High | `brace-expansion` | 5.0.8 | `npm 12.0.2-r0` | 5.0.11 | x86_64, aarch64 |
| [GHSA-qrxm-fqhp-jwvm](https://github.com/advisories/GHSA-qrxm-fqhp-jwvm) | High | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.29.1 | x86_64, aarch64 |
| [GHSA-rfgv-xxqx-mfg5](https://github.com/advisories/GHSA-rfgv-xxqx-mfg5) | High | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.28.1 | x86_64, aarch64 |
| [GHSA-rgw5-rvv9-x895](https://github.com/advisories/GHSA-rgw5-rvv9-x895) | High | `brace-expansion` | 5.0.8 | `npm 12.0.2-r0` | 5.0.9 | x86_64, aarch64 |
| [GHSA-xjj6-f33q-929c](https://github.com/advisories/GHSA-xjj6-f33q-929c) | High | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.29.1 | x86_64, aarch64 |
| [CVE-2025-15367](https://nvd.nist.gov/vuln/detail/CVE-2025-15367) | Medium | `python-3.13` | 3.13.18_git20261122-r0 | `python-3.13 3.13.18_git20261122-r0` | no fix yet | x86_64, aarch64 |
| [CVE-2026-115559](https://nvd.nist.gov/vuln/detail/CVE-2026-115559) | Medium | `python-3.13` | 3.13.18_git20261122-r0 | `python-3.13 3.13.18_git20261122-r0` | no fix yet | x86_64, aarch64 |
| [CVE-2026-115791](https://nvd.nist.gov/vuln/detail/CVE-2026-115791) | Medium | `python-3.13` | 3.13.18_git20261122-r0 | `python-3.13 3.13.18_git20261122-r0` | no fix yet | x86_64, aarch64 |
| [CVE-2026-115819](https://nvd.nist.gov/vuln/detail/CVE-2026-115819) | Medium | `glibc-2.44` | 2.44-r24 | `glibc-2.44 2.44-r24` | no fix yet | x86_64, aarch64 |
| [CVE-2026-116566](https://nvd.nist.gov/vuln/detail/CVE-2026-116566) | Medium | `python-3.13` | 3.13.18_git20261122-r0 | `python-3.13 3.13.18_git20261122-r0` | no fix yet | x86_64, aarch64 |
| [CVE-2026-124249](https://nvd.nist.gov/vuln/detail/CVE-2026-124249) | Medium | `python-3.13` | 3.13.18_git20261122-r0 | `python-3.13 3.13.18_git20261122-r0` | no fix yet | x86_64, aarch64 |
| [GHSA-22jq-vg5j-6vgg](https://github.com/advisories/GHSA-22jq-vg5j-6vgg) | Medium | `ip-address` | 10.2.0 | `npm 12.0.2-r0` | 10.2.1 | x86_64, aarch64 |
| [GHSA-2vr4-cq9g-pvrc](https://github.com/advisories/GHSA-2vr4-cq9g-pvrc) | Medium | `ip-address` | 10.2.0 | `npm 12.0.2-r0` | 10.5.1 | x86_64, aarch64 |
| [GHSA-3g3m-2fjr-6pw4](https://github.com/advisories/GHSA-3g3m-2fjr-6pw4) | Medium | `glob` | 13.0.6 | `npm 12.0.2-r0` | 14.0.2 | x86_64, aarch64 |
| [GHSA-3wwx-pv8p-q78v](https://github.com/advisories/GHSA-3wwx-pv8p-q78v) | Medium | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.28.1 | x86_64, aarch64 |
| [GHSA-4qv8-2p9j-2685](https://github.com/advisories/GHSA-4qv8-2p9j-2685) | Medium | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.29.1 | x86_64, aarch64 |
| [GHSA-4xrf-jv44-h6hh](https://github.com/advisories/GHSA-4xrf-jv44-h6hh) | Medium | `ip-address` | 10.2.0 | `npm 12.0.2-r0` | 10.2.2 | x86_64, aarch64 |
| [GHSA-8xcm-r25x-g524](https://github.com/advisories/GHSA-8xcm-r25x-g524) | Medium | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.28.0 | x86_64, aarch64 |
| [GHSA-9fm3-97px-rjf6](https://github.com/advisories/GHSA-9fm3-97px-rjf6) | Medium | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.29.1 | x86_64, aarch64 |
| [GHSA-g3hv-75wg-m249](https://github.com/advisories/GHSA-g3hv-75wg-m249) | Medium | `minimatch` | 10.2.3 | `npm 12.0.2-r0` | 11.0.1 | x86_64, aarch64 |
| [GHSA-h3mg-xc3c-68pw](https://github.com/advisories/GHSA-h3mg-xc3c-68pw) | Medium | `ip-address` | 10.2.0 | `npm 12.0.2-r0` | 10.7.1 | x86_64, aarch64 |
| [GHSA-j6r3-76f7-8jcv](https://github.com/advisories/GHSA-j6r3-76f7-8jcv) | Medium | `ip-address` | 10.2.0 | `npm 12.0.2-r0` | 10.7.1 | x86_64, aarch64 |
| [GHSA-m8rv-5g2x-5cg5](https://github.com/advisories/GHSA-m8rv-5g2x-5cg5) | Medium | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.28.0 | x86_64, aarch64 |
| [GHSA-q2hr-2g5m-vwhr](https://github.com/advisories/GHSA-q2hr-2g5m-vwhr) | Medium | `brace-expansion` | 5.0.8 | `npm 12.0.2-r0` | 5.0.12 | x86_64, aarch64 |
| [GHSA-rj75-hqrm-r3gf](https://github.com/advisories/GHSA-rj75-hqrm-r3gf) | Medium | `postcss-selector-parser` | 7.1.4 | `npm 12.0.2-r0` | 7.1.6 | x86_64, aarch64 |
| [GHSA-rpw4-54j3-4h4q](https://github.com/advisories/GHSA-rpw4-54j3-4h4q) | Medium | `ip-address` | 10.2.0 | `npm 12.0.2-r0` | 10.5.1 | x86_64, aarch64 |
| [GHSA-rxp7-6hxx-x8q5](https://github.com/advisories/GHSA-rxp7-6hxx-x8q5) | Medium | `ip-address` | 10.2.0 | `npm 12.0.2-r0` | 10.7.4 | x86_64, aarch64 |
| [GHSA-v3r7-h72x-cjcm](https://github.com/advisories/GHSA-v3r7-h72x-cjcm) | Medium | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.28.0 | x86_64, aarch64 |
| [CVE-2026-100290](https://nvd.nist.gov/vuln/detail/CVE-2026-100290) | Low | `glibc-2.44` | 2.44-r24 | `glibc-2.44 2.44-r24` | no fix yet | x86_64, aarch64 |
| [CVE-2026-103995](https://nvd.nist.gov/vuln/detail/CVE-2026-103995) | Low | `python-3.13` | 3.13.18_git20261122-r0 | `python-3.13 3.13.18_git20261122-r0` | no fix yet | x86_64, aarch64 |
| [CVE-2026-16052](https://nvd.nist.gov/vuln/detail/CVE-2026-16052) | Low | `python-3.13` | 3.13.18_git20261122-r0 | `python-3.13 3.13.18_git20261122-r0` | no fix yet | x86_64, aarch64 |
| [GHSA-r53p-7pc4-xj5r](https://github.com/advisories/GHSA-r53p-7pc4-xj5r) | Low | `undici` | 6.27.0 | `npm 12.0.2-r0` | 6.28.1 | x86_64, aarch64 |
| [CVE-2026-19552](https://nvd.nist.gov/vuln/detail/CVE-2026-19552) | Negligible | `python-3.13` | 3.13.18_git20261122-r0 | `python-3.13 3.13.18_git20261122-r0` | no fix yet | x86_64, aarch64 |

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
cosign verify ghcr.io/pair-ai-platform/node:22.23.5-dev-20261123.385 \
  --certificate-identity-regexp '^https://github.com/Pair-AI-Platform/node/.github/workflows/build.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/pair-ai-platform/node:22.23.5-dev-20261123.385 --repo Pair-AI-Platform/node
```
