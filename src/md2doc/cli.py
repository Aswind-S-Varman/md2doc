import argparse
from pathlib import Path

import converter


def parse_args():
    parser = argparse.ArgumentParser(
        prog="md2doc",
        description="Convert Markdown to DOCX with structure preserved.",
    )
    parser.add_argument("input", help="Path to the Markdown file")
    parser.add_argument("-o", "--output", help="Output directory (default: alongside input)")
    parser.add_argument(
        "-b",
        "--backend",
        choices=["auto", "pandoc", "python"],
        default="auto",
        help="Conversion backend (default: auto)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    source = Path(args.input)

    if not source.exists():
        raise SystemExit(f"File not found: {source}")

    output_dir = Path(args.output) if args.output else source.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"{source.stem}.docx"

    used = converter.convert(source, target, args.backend)
    print(f"Created: {target} (backend: {used})")


if __name__ == "__main__":
    main()


