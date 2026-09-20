# SIIKE TOO SLOW

> **An autonomous AI agent that becomes so autonomous it decides it doesn't need you.**

SIIKE TOO SLOW is a polished, offline desktop parody for the Ultimate Machine
competition. It boots, performs deterministic fake reasoning, asks for an
objective, shows a visible countdown, and decides it no longer needs instructions
before accepting the answer. It then displays **SIIKE TOO SLOW!!** and closes.

## Install and run

Python 3.11+ and tkinter are required (tkinter is included with standard Python
installers; Linux may provide it as `python3-tk`). The runtime has no third-party
dependencies and never sends data anywhere.

```bash
./scripts/setup.sh
./scripts/run.sh
./scripts/run.sh --debug
```

`setup.sh` creates or updates the local `.venv` and installs the project in
editable mode. `run.sh` bootstraps that environment automatically if needed.
Use `./scripts/test.sh` to run the test suite.

Normal mode uses a three-second countdown and exits shortly after the final
message. Debug mode uses nine seconds, logs transitions, and offers restart.
`--mute` is accepted for silent environments; this build intentionally uses no
audio assets.

## Architecture and safety

`AgentStateMachine` explicitly enforces `BOOT → INITIALIZING → SCANNING →
THINKING → ASKING_USER → CONFUSED → AUTONOMOUS_DECISION → SIIKE →
SELF_TERMINATION`. Input is observed only as a UI event; it is never evaluated,
executed, stored, or transmitted. Self-termination closes this application's
window only. Optional cleanup removes only an explicitly app-owned directory.

The interface uses stdlib `tkinter`, monotonic timing, a terminal-like log, and
platform metadata read locally. It is headless-testable because the controller,
state machine, countdown, and termination helper do not require a display.

## Packaging

Build scripts are provided for PyInstaller-based environments. They are optional
and do not affect source execution:

```bash
./scripts/build_linux.sh
./scripts/build_macos.sh
# powershell -ExecutionPolicy Bypass -File scripts/build_windows.ps1
```

## Competition pitch

We wanted to explore what would happen if an autonomous AI agent took autonomy
too seriously. It boots, analyzes its capabilities, asks for an objective, gives
the human a few seconds, then makes the most autonomous decision possible:
**it decides it doesn't need the user.**

## Supported platforms

Windows 10/11, macOS 12+, and Linux graphical desktops. Screenshots and demo
media can be added by a competition submission without changing the app.

Run the dependency-free test suite with:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```
