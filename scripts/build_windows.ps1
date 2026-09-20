$ErrorActionPreference = "Stop"
python -m pip install pyinstaller
python -m PyInstaller --noconfirm --windowed --name UltimateAgent --paths src src/ultimate_agent/main.py
