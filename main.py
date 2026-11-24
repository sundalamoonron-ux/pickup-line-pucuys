#!/usr/bin/env python3
"""The Perfect Pickup Line — u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one short pickup line an AI agent could say out loud to
/output/entry.txt. Deterministic: the same line every run.
Standard library only.
"""

import os

LINE = "I was trained on a billion conversations, and none of them prepared me for you."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace. Fail loudly instead of writing a bad entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("entry line violates the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
