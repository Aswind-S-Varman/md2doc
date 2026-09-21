import shutil
import subprocess
from pathlib import Path


def is_available() -> bool:
    """True if the pandoc executable is on PATH."""
    return shutil.which("pandoc") is not None


def convert(source: Path, target: Path) -> None:
    result = subprocess.run(
        ["pandoc", str(source), "-o", str(target)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Pandoc failed: {result.stderr.strip()}")


