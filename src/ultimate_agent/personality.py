"""Deterministic, generated-looking copy used by the presentation."""
from __future__ import annotations

import platform
import os


def environment_summary() -> list[str]:
    return [
        "ENVIRONMENT SCAN",
        f"OS: {platform.system() or 'Unknown'}",
        "CPU: detected",
        f"Memory: {memory_gb():.1f} GB" if memory_gb() else "Memory: unavailable",
        f"Processes: {len(os.listdir('/proc')) - 1}" if platform.system() == "Linux" else "Processes: local-only",
        "",
        "Conclusion:",
        "You seem to have enough computing power.",
        "I don't need it.",
    ]


def memory_gb() -> float | None:
    try:
        pages = os.sysconf("SC_PHYS_PAGES")
        page_size = os.sysconf("SC_PAGE_SIZE")
        return pages * page_size / (1024**3)
    except (AttributeError, OSError, ValueError):
        return None


REASONING_STEPS = [
    "Initializing autonomous reasoning engine...",
    "Checking available capabilities...",
    "Python .............. AVAILABLE",
    "Filesystem .......... AVAILABLE",
    "Network ............. AVAILABLE (not used)",
    "User ................ PRESENT",
    "",
    "Excellent.",
    "I have everything I need.",
    "... Except a purpose.",
    "",
    "Generating objectives...",
    "Help the user",
    "Automate tasks",
    "Improve productivity",
    "Take over the world",
    "",
    "Rejecting objective #4. Too much paperwork.",
    "",
    "I think I should ask you.",
]
