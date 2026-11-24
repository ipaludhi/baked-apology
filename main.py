"""Baked apology — one-line entry for Make the Judge Smile.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The sentence: this morning Mrs. Sari knocked with warm bread — an alarm
complaint turned into a baked apology. Warmth is the kindness itself,
surprise is the twist (complaint -> edible apology), concreteness is the
name + warm bread + knock, fresh wording is "best apology I've ever
eaten". No greeting-card phrasing, no cliche.

Revision: entry sentence written once, unchanged since first draft.
"""

import os
from pathlib import Path

TEXT = (
    "This morning Mrs. Sari knocked, handed me warm bread, and said, "
    "'your alarm woke me, so I baked you an apology' \u2014 best apology "
    "I've ever eaten."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
