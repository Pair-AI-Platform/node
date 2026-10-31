# Where Node.js comes from

| Image | Node.js package | Source | OpenSSL used by Node.js |
| :--- | :--- | :--- | :--- |
| `node:26`, `node:26-dev` | `nodejs-26` | Wolfi (`packages.wolfi.dev`) | Wolfi's system OpenSSL 4.0 (`libssl.so.4`) |
| `node:24`, `node:24-dev` | `nodejs-24` | Wolfi (`packages.wolfi.dev`) | Wolfi's system OpenSSL 4.0 (`libssl.so.4`) |
| `node:22`, `node:22-dev` | `nodejs-22-upstream` | Official binaries from [nodejs.org](https://nodejs.org/dist/), packaged here by melange | The OpenSSL built into the official binary (3.5.x) |

## Why Node.js 22 comes from nodejs.org

On 14 August 2026 Wolfi moved `nodejs-22` to Chainguard's commercial repository
([wolfi-dev/os#231401](https://github.com/wolfi-dev/os/pull/231401), "Move non-latest nodejs 22
from os to enterprise"). Since then the public Wolfi package has stayed at 22.23.2 and gets no
fixes; for example 22.23.4, a security release, never reached it. Chainguard's commercial packages
need a subscription and are not used here.

The Node.js project itself publishes every release of every supported line, for `linux-x64` and
`linux-arm64`, on the day it is released. Node.js 22 is supported until 30 April 2027.

## How the package is built and verified

[`melange/nodejs-22-upstream.yaml`](../melange/nodejs-22-upstream.yaml), natively on x86_64 and
aarch64, for every build:

1. Downloads `SHASUMS256.txt.asc` and `node-v<version>-linux-<arch>.tar.xz` from
   `https://nodejs.org/dist/v<version>/`.
2. Verifies `SHASUMS256.txt.asc` with `gpgv` against the Node.js release keys
   ([`nodejs-release-keys.kbx`](../melange/nodejs-22-upstream/nodejs-release-keys.kbx), from
   [nodejs/release-keys](https://github.com/nodejs/release-keys), `gpg-only-active-keys`, at the
   commit recorded in the recipe). The build stops on a bad or unknown signature.
3. Checks the tarball against the checksum in the **signed** content; no checksum is written by
   hand or by Renovate.
4. Packages `bin/node`, the C headers (`include/node`, for node-gyp) and the license. npm, yarn and
   pnpm in the development image come from Wolfi.
5. Tests that the packaged binary runs and reports the expected version.

The package is signed with the repository's APK key (`keys/node-packages.rsa.pub`, private half in
the `MELANGE_SIGNING_KEY` secret). The build is reproducible: the same version gives the same
package, so an image changes only when Node.js or another package in it changes.

## How it is kept current

[Renovate](../renovate.json) tracks two things in the recipe and opens a pull request for each:

| What | Renovate source | Rule |
| :--- | :--- | :--- |
| Node.js version | `node-version` datasource (the release list of nodejs.org) | Newest `22.x` only (`allowedVersions: <23`); automerged once all images build, test and scan |
| Release keys | `git-refs` on `github.com/nodejs/release-keys` | When the Node.js project adds or removes a releaser; `scripts/update-node-release-keys.sh` refreshes the keyring in the same pull request |

The merge starts the release workflow, which publishes the new `node:22` and `node:22-dev` images
with their release notes, scans and evidence.

## What is different from the Wolfi images

- **OpenSSL:** the official binary carries its own OpenSSL (3.5.x) and does not load the system
  OpenSSL configuration the same way. It also does not offer the post-quantum TLS key exchange
  that Node.js 24 and 26 use by default (see below). A cryptography profile from
  [khatm](https://github.com/Pair-AI-Platform/khatm), such as FIPS 140-3, therefore does not apply
  to `node:22`; it applies to the images that use Wolfi's Node.js (24, 26). Choose 24 or 26 when a
  contract needs such a profile.
- **Vulnerability scans** still work: Grype identifies the Node.js version in the binary.

## OpenSSL and post-quantum key exchange

| Image | OpenSSL | Default TLS 1.3 key exchange | ML-KEM / ML-DSA in `crypto` |
| :--- | :--- | :--- | :--- |
| `node:24`, `node:26` | 4.0 (Wolfi) | `X25519MLKEM768` (hybrid post-quantum) | Yes |
| `node:22` | 3.5.x (bundled) | Classical | No |

Every release checks the first column: `scripts/test-image.sh` opens a TLS 1.3 connection between two
Node.js processes and fails the release if Node.js 24 or later does not negotiate `X25519MLKEM768`.

With a [khatm](https://github.com/Pair-AI-Platform/khatm) FIPS profile installed, Node.js 24 and 26
run in FIPS mode (`crypto.getFips()` returns 1, MD5 is refused) and lose ML-KEM and ML-DSA, since the
FIPS module (CMVP #4985) does not contain them. FIPS 140-3 and post-quantum key exchange cannot be
had together until a FIPS module with ML-KEM is validated.

## If Wolfi moves another line

`nodejs-24` and `nodejs-26` are in public Wolfi today. If either leaves, the same recipe works for
it: copy `melange/nodejs-22-upstream.yaml` to `nodejs-<major>-upstream.yaml`, change the version
and the `allowedVersions` rule, and switch the image definitions to the new package.
