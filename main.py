#!/usr/bin/env python3
"""One Star, Five Stars for the Food entry for make.fun.

Writes one original one-star review of Earth by an alien tourist,
with a sincere compliment about the food, to entry.txt.
Deterministic, standard library only: the same bytes every run.
"""

import os

TEXT = (
    "One star: the locals spend their lives staring at glowing rectangles "
    "and breathing exhaust, yet the tacos are so good I almost applied for "
    "planetary residency."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read back and verify the written bytes match exactly, and the
    # entry stays one sentence within the 200-character gate.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == TEXT, "entry.txt bytes differ from TEXT"
    assert 1 <= len(written) <= 200, "entry.txt outside 1-200 characters"
    assert written.strip() == written, "entry.txt has stray whitespace"


if __name__ == "__main__":
    main()
