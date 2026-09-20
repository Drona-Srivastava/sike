"""Safe process termination helpers; never touch other processes or system files."""
from __future__ import annotations

import os
from pathlib import Path
import shutil


def cleanup_owned_cache(cache_dir: Path) -> None:
    """Remove only a directory explicitly supplied as app-owned cache."""
    if cache_dir.exists():
        shutil.rmtree(cache_dir)


def terminate(exit_func=os._exit, code: int = 0) -> None:
    """Terminate this process through an injectable function for testing."""
    exit_func(code)
