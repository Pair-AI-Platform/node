#!/usr/bin/env bash
# Refreshes melange/nodejs-22-upstream/nodejs-release-keys.kbx from github.com/nodejs/release-keys at
# the commit named in melange/nodejs-22-upstream.yaml ("release-keys-commit:"). Renovate runs it after
# it updates that commit (renovate.json); run it by hand after changing the commit yourself.
set -euo pipefail

recipe=melange/nodejs-22-upstream.yaml
keyring=melange/nodejs-22-upstream/nodejs-release-keys.kbx
commit="$(sed -n 's/^# release-keys-commit: \([0-9a-f]\{40\}\)$/\1/p' "$recipe")"
[ -n "$commit" ] || { echo "no release-keys-commit in $recipe" >&2; exit 1; }

curl -fsSL --retry 3 -o "$keyring.new" \
  "https://raw.githubusercontent.com/nodejs/release-keys/$commit/gpg-only-active-keys/pubring.kbx"
mv "$keyring.new" "$keyring"
echo "release keys at nodejs/release-keys@$commit"
