# md2doc

Convert Markdown to Word documents with structure preserved — tables, headings, and lists intact.

![tests](https://github.com/Aswind-S-Varman/md2doc/actions/workflows/tests.yml/badge.svg)

## The problem

Markdown is easy to produce. Scripts generate it, AI tools output it, and docs-as-code
workflows keep it in version control. Word is what stakeholders actually want to receive.

Bridging the two by hand — especially tables — is repetitive work that gets done over and
over. `md2doc` automates that step.

## What it does

- Converts Markdown to `.docx` with headings, tables, and bullet lists preserved
- Uses Pandoc when available, falls back to a pure-Python converter when it isn't
- Lets you force a specific backend for predictable output
- Reports which backend produced the file

## Quick start

```bash
pip install -e .
md2doc samples/input.md
```

```
Created: samples/input.docx (backend: pandoc)
```

Options:

```bash
md2doc input.md -o output/          # choose output directory
md2doc input.md --backend python    # force the fallback converter
md2doc --help
```

See [samples/input.md](samples/input.md) for the input and `samples/input.docx` for the result.

## How it works

```
cli.py          argument parsing and error handling
  └─ converter.py    picks a backend, returns which one ran
       ├─ pandoc_backend.py   shells out to pandoc
       └─ python_backend.py   line-based parser using python-docx
```

## Design decisions

**Two backends, not one.** Pandoc is the better converter and I didn't try to
out-engineer it — it's the default whenever it's installed. But Pandoc is a separate
binary, and on locked-down corporate machines or minimal CI containers you often can't
install it. Rather than fail, the tool degrades to a pure-Python converter that handles
the common cases.

**The fallback is deliberately limited.** It handles headings, paragraphs, bullet lists,
and tables. It does not handle nested lists, inline bold/italic, code blocks, or images.
Pandoc also applies proper Word table styling, while the fallback uses a plain grid.
Supporting everything would mean writing a full Markdown parser, which is what Pandoc
already is. The fallback exists to keep the tool usable, not to replace Pandoc.

**Backend selection is visible and overridable.** The output states which backend ran, and
`--backend` forces a choice. Silent fallback would mean inconsistent output with no
explanation — worse than a clear failure.

**Availability is checked before use.** `is_available()` looks for pandoc on PATH and the
tool reports a clear message instead of surfacing a raw traceback.

## Tests

```bash
pip install -e ".[dev]"
pytest -v
```

Tests cover the parts most likely to break: excluding Markdown's `|---|---|` alignment row
from table data, applying the correct bullet style, and selecting the right backend.

## License

MIT


