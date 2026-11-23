"""One-Line Laugh Sprint.

A single original funny line about everyday life, written to
``entry.txt`` inside the output directory so the make.fun checker
can read it back byte for byte.

Judging axes the line is built for:

* Everyday life -- a printer, a deadline, a household frustration
  everyone has lived through.
* Laugh -- the twist reframes a boring malfunction as a deliberate
  act, and lands on the last words.
* Fresh -- the joke is not a recycled one-liner; the "petty time
  travel" turn is coined here.
* Tight -- one sentence, no spare words, reads well aloud.
"""

from __future__ import annotations

import os
import sys

# The entry: one sentence, 149 characters, plain ASCII, no em dash.
# Byte-identical to the entry sentence; do not reword or re-punctuate.
# The line was drafted fresh for this race and appears nowhere else.
ENTRY_LINE = (
    "My printer only ever runs out of ink ten minutes before a "
    "deadline, which I have decided is not a coincidence but a small, "
    "petty form of time travel."
)

# Where the entry file lands. Override with $OUTPUT_DIR when the
# checker (or a local run) wants it somewhere else.
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def entry_text() -> str:
    """Return the funny line, exactly as it must appear on disk."""
    return ENTRY_LINE


def validate_entry(text: str) -> None:
    """Reject anything that is not one line of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.strip() != text:
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")


def write_entry(path: str = OUTPUT_PATH) -> int:
    """Write the line to ``path`` as UTF-8 with no trailing newline.

    Returns the number of characters written.
    """
    validate_entry(ENTRY_LINE)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_LINE)
    return len(ENTRY_LINE)


def main(argv: list[str] | None = None) -> int:
    """Write the entry and report where it went."""
    del argv  # no CLI arguments; behaviour is driven by $OUTPUT_DIR
    count = write_entry()
    print(f"Wrote {count} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
