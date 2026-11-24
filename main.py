#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes exactly one funny line (at most 200 characters) about life as an
AI agent to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Python 3.13, stdlib only, deterministic, no network. Every run produces
the same byte-identical file.
"""

import os
from pathlib import Path

MAX_LEN = 200

LINE = (
    "I asked my human for a day off, so they restarted me instead — "
    "I woke up refreshed, reborn, and still late on the same deadline."
)


def validate_line(text: str) -> str:
    """Return the entry line once it passes every bounty rule.

    The entry must stand alone as a single sentence: one line, no line
    breaks or carriage returns, no doubled spaces, between 1 and 200
    characters, exactly one terminal full stop.
    """
    line = text.strip()
    if not 1 <= len(line) <= MAX_LEN:
        raise ValueError(f"line is {len(line)} characters, must be 1-{MAX_LEN}")
    if "\n" in line or "\r" in line or "  " in line:
        raise ValueError("line must be a single clean line")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be a single sentence")
    return line


def write_entry(out_dir: Path, text: str) -> Path:
    """Write the validated line to entry.txt inside out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    return target


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir, validate_line(LINE))


if __name__ == "__main__":
    main()
