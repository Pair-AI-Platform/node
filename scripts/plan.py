#!/usr/bin/env python3
"""Lists the images to build, one entry per apko/nodejs-<major>[-dev].apko.yaml.

    scripts/plan.py <image-repository>        # e.g. ghcr.io/pair-ai-platform/node

Prints a JSON list for a GitHub Actions matrix. Each entry has the config path, the family (the
floating tag, e.g. "22" or "22-dev"), the flavor and the Node.js major version.
"""
import json
import pathlib
import re
import sys

# The runtime and dev images of this major also get `latest` and `latest-dev`
LATEST_MAJOR = "24"

image = sys.argv[1]
entries = []
for config in sorted(pathlib.Path("apko").glob("nodejs-*.apko.yaml")):
    m = re.fullmatch(r"nodejs-(\d+)(-dev)?\.apko\.yaml", config.name)
    if not m:
        sys.exit(f"unexpected config name: {config.name}")
    major, dev = m.group(1), bool(m.group(2))
    family = f"{major}-dev" if dev else major
    entries.append({
        "config": str(config),
        "image": image,
        "family": family,
        "flavor": "dev" if dev else "runtime",
        "major": major,
        "latest": major == LATEST_MAJOR,
    })
print(json.dumps(entries))
