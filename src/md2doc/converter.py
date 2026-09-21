from pathlib import Path

from . import pandoc_backend, python_backend


def convert(source: Path, target: Path, backend: str = "auto") -> str:
    """Convert source to target. Returns the backend actually used."""
    if backend == "auto":
        backend = "pandoc" if pandoc_backend.is_available() else "python"

    if backend == "pandoc":
        if not pandoc_backend.is_available():
            raise SystemExit("Pandoc backend requested but pandoc is not installed.")
        pandoc_backend.convert(source, target)
    else:
        python_backend.convert(source, target)

    return backend


