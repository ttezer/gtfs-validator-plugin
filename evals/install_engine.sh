#!/bin/bash
# Pre-installs the pinned engine into the venv path SKILL.md uses on the user's computer.
# Runs as a scaffold (outside the eval sandbox), because the sandbox cannot reach PyPI over TLS.
set -euo pipefail
venv="$HOME/.cache/gtfs-validator/venv"
python3 -m venv "$venv"
"$venv/bin/pip" install --quiet --disable-pip-version-check gtfs-analyzer==0.16.0
