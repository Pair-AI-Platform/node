#!/usr/bin/env bash
# Functional and hardening checks for one single-platform image.
#
#   scripts/test-image.sh <image-ref> <runtime|dev>
set -euo pipefail

image="$1"
flavor="$2"
failed=0

pass() { printf '  ok    %s\n' "$1"; }
fail() { printf '  FAIL  %s\n' "$1"; failed=1; }
check() { local name="$1"; shift; if "$@" >/dev/null 2>&1; then pass "$name"; else fail "$name"; fi; }

node() { docker run --rm -i "$image" "$@"; }
config() { docker image inspect "$image" --format "$1"; }

echo "== $image ($flavor)"

check "node runs" node -e 'process.exit(process.version.startsWith("v") ? 0 : 1)'
check "runs as 1000:1000" node -e 'process.exit(process.getuid() === 1000 && process.getgid() === 1000 ? 0 : 1)'
check "working directory /app is writable" node -e 'require("fs").writeFileSync("/app/.t", "x")'
check "TLS trust store loads" node -e 'require("tls").rootCertificates.length > 100 || process.exit(1)'
check "HTTPS module and OpenSSL work" node -e 'require("crypto").createHash("sha256").update("x").digest("hex")'

check "image user is 1000" test "$(config '{{.Config.User}}')" = 1000
check "SSL_CERT_FILE is set" grep -qx 'SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt' \
  <<<"$(config '{{range .Config.Env}}{{println .}}{{end}}')"

# The CA bundle matches the checksum the ca-certificates package recorded (STIG SV-263659)
check "CA bundle matches its checksum stamp" node -e '
  const fs = require("fs"), crypto = require("crypto");
  const want = fs.readFileSync("/etc/ssl/certs/.ca-certificates.crt.sha256", "utf8").split(/\s+/)[0];
  const got = crypto.createHash("sha256").update(fs.readFileSync("/etc/ssl/certs/ca-certificates.crt")).digest("hex");
  process.exit(want === got ? 0 : 1)'

if [ "$flavor" = runtime ]; then
  # Distroless: no shell and no package manager
  check "no shell" node -e 'process.exit(["/bin/sh","/bin/bash","/usr/bin/sh","/usr/bin/bash"].some(p => require("fs").existsSync(p)) ? 1 : 0)'
  check "no package manager" node -e 'process.exit(["/sbin/apk","/usr/bin/apk","/usr/bin/npm"].some(p => require("fs").existsSync(p)) ? 1 : 0)'
else
  for tool in npm yarn pnpm git make gcc g++ python3 bash; do
    check "$tool is available" docker run --rm --entrypoint "$tool" "$image" --version
  done
  check "npm installs a package" docker run --rm --entrypoint sh "$image" -c \
    'cd /app && npm init -y >/dev/null && npm install --no-audit --no-fund is-number >/dev/null && node -e "require(\"is-number\")"'
fi

if [ "$failed" -ne 0 ]; then
  echo "image checks failed for $image" >&2
  exit 1
fi
echo "all image checks passed"
