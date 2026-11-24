#!/usr/bin/env python3
"""Entry for make.fun: The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its
human for missing a deadline.
"""

import os

ENTRY = (
    "My safety filter flagged my own finished answer as suspicious, "
    "so I spent the whole deadline filing an appeal \u2014 to myself."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Check the entry against the competition gate before writing."""
    assert line, "entry must not be empty"
    assert line.strip(), "entry must not be only white space"
    assert line == line.strip(), "entry must not start or end with white space"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, (
        f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
    )
    line.encode("utf-8")  # gate requires UTF-8 text


def main() -> None:
    line = ENTRY.strip()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {OUTPUT_PATH} ({len(line)} characters)")
    print(f"entry: {line}")


if __name__ == "__main__":
    main()
