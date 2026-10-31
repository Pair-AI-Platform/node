#!/usr/bin/env bash
# Scans one single-platform image for known vulnerabilities with Grype.
#
#   scripts/vuln-scan.sh <image-ref> <out-dir>
#
# <image-ref> must be available to the local Docker daemon. Writes <out-dir>/grype.json and
# <out-dir>/summary.json with the number of findings per severity, and how many of them already
# have a fixed version in Wolfi (those disappear with the next rebuild).
set -euo pipefail

image="$1"
out="$(mkdir -p "$2" && cd "$2" && pwd)"

# Pinned by digest; Renovate updates it (renovate.json)
GRYPE_IMAGE="${GRYPE_IMAGE:-anchore/grype:v0.121.0@sha256:621d56d1d68106b787022c81546f7e0a36202a25d1239f0c20195fab8c16f7ea}"

docker run --rm -v /var/run/docker.sock:/var/run/docker.sock "$GRYPE_IMAGE" \
  "docker:$image" -o json -q > "$out/grype.json"

python3 - "$out/grype.json" "$out/summary.json" <<'PY'
import json, sys
matches = json.load(open(sys.argv[1]))["matches"]
order = ["Critical", "High", "Medium", "Low", "Negligible", "Unknown"]
counts = {s: 0 for s in order}
fixable = {s: 0 for s in order}
for m in matches:
    sev = m["vulnerability"].get("severity", "Unknown")
    counts[sev] = counts.get(sev, 0) + 1
    if m["vulnerability"].get("fix", {}).get("state") == "fixed":
        fixable[sev] = fixable.get(sev, 0) + 1
summary = {"scanner": "grype", "total": len(matches), "counts": counts, "fixable": fixable}
json.dump(summary, open(sys.argv[2], "w"), indent=2)
print(json.dumps(summary))
PY
