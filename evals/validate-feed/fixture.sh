#!/bin/bash
set -euo pipefail
bash "$(dirname "$0")/../make_feed.sh"
bash "$(dirname "$0")/../install_engine.sh"
