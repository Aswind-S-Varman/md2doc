import argparse
from pathlib import Path

import pandoc_backend


def parse_args():
    parser = argparse.ArgumentParser(
        prog="md2doc",
        description="Convert Markdown to DOCX and PDF with structure preserved.",
    )
    parser.add_argument("input", help="Path to the Markdown file")
    parser.add_argument("-o", "--output", help="Output directory (default: alongside input)")
    return parser.parse_args()


def main():
    args = parse_args()
    source = Path(args.input)

    if not source.exists():
        raise SystemExit(f"File not found: {source}")

    if not pandoc_backend.is_available():
        raise SystemExit("Pandoc is not installed or not on PATH.")

    output_dir = Path(args.output) if args.output else source.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"{source.stem}.docx"

    pandoc_backend.convert(source, target)
    print(f"Created: {target}")


if __name__ == "__main__":
    main()


