#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one original epitaph (famous last words) to
$MAKEFUN_OUTPUT_DIR/entry.txt: 47 characters, UTF-8, one line,
no trailing newline. Stdlib only, deterministic: the same output
on every run.

The line: a dying person asks for more time and is handed a
deadline. The joke is the ironic reversal plus the double meaning
of "deadline" (a work deadline, and the date by which you must be
dead). First-person dying speech, short enough to carve in stone,
no explanation needed, quotable.
"""

import os

LINE = "I asked for more time. They gave me a deadline."


def main() -> None:
    assert 1 <= len(LINE) <= 150, "line must be 1-150 characters"
    assert LINE.strip(), "line must not be whitespace only"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # make.fun collects outputs as another user: leave it world-readable.
    os.chmod(out_path, 0o644)
    os.chmod(out_dir, 0o755)
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back must match the line exactly"


if __name__ == "__main__":
    main()
