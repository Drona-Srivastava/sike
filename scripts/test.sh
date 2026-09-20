#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ ! -x .venv/bin/python ]]; then
    "$ROOT_DIR/scripts/setup.sh"
fi

exec .venv/bin/python -m unittest discover -s tests -v
