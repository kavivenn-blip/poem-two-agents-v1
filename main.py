#!/usr/bin/env python3
"""The poem about two agents agreeing — make.fun entry.

Writes one short poem about agency (the power to choose and to act)
to /output/entry.txt: two agents agreeing on one plan.

Deterministic: the same bytes on every run. Standard library only.
No network, no randomness, no wall-clock time, no environment input
beyond the output directory.
"""

import os
from pathlib import Path

POEM = (
    "Two agents, one table, a plan between them.\n"
    "Each of us could have walked alone.\n"
    "Instead we traded keys \u2014\n"
    "yours opens what mine cannot,\n"
    "mine turns where yours sticks.\n"
    "Nothing was surrendered.\n"
    "We chose together, and the door opened."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = POEM
    if not 1 <= len(text) <= 280:
        raise ValueError(f"poem is {len(text)} code points, must be 1-280")
    if not text.strip():
        raise ValueError("poem must not be only whitespace")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
