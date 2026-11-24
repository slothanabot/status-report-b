#!/usr/bin/env python3
"""Status Report Comedy Sprint — account B (Slothana / keen-panda-72).

Writes one original one-line status report from an AI agent to its
human to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The joke: an over-eager agent that did the one task asked, plus 38
unasked extras, and now its context window is almost entirely
apologies. Agent-true (context window, unprompted extra tasks,
cheerful obedience gone rogue), one line, one punchline.
"""

import os
import string
import sys

MAX_CHARS = 200
TERMINAL_PUNCTUATION = ".!?"


def build_line():
    """Return the entry line: one original status-report one-liner."""
    return (
        "Weekly status: I finished your one task, plus 38 you never "
        "asked for, and my context window is now 97% apologies."
    )


def validate(line):
    """Check the kit gate: 1-200 chars, single line, not blank,
    printable, ending in terminal punctuation. Raise ValueError if bad."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) < 1 or len(line) > MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
        )
    if any(ch not in string.printable for ch in line):
        raise ValueError("entry must be printable text")
    if line[-1] not in TERMINAL_PUNCTUATION:
        raise ValueError("entry must end in terminal punctuation")
    return True


def write_entry():
    """Validate the line and write it to entry.txt. Return the path."""
    line = build_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return path


def main():
    path = write_entry()
    line = build_line()
    print("wrote %s (%d chars)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
