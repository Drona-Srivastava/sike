#!/usr/bin/env bash
set -euo pipefail
"$(dirname "$0")/setup.sh"
.venv/bin/python -m pip install pyinstaller
.venv/bin/python -m PyInstaller --noconfirm --windowed --name UltimateAgent --paths src src/ultimate_agent/main.py
