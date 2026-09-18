import argparse
from pathlib import Path


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

    output_dir = Path(args.output) if args.output else source.parent
    print(f"Would convert: {source}")
    print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    main()