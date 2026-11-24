#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt: at most 120 characters, no trailing newline,
deterministic (same bytes every run). Stdlib only, no network.
"""

import os

FORTUNE = (
    "You will resolve the merge conflict you dreaded, "
    "and discover both sides were fixing the same bug."
)

OUTPUT_PATH = "/output/entry.txt"


def verify_written(path: str) -> None:
    """Re-read the written file and confirm the entry contract holds."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    assert text == FORTUNE, "written bytes differ from the fortune"
    assert len(text) <= 120, "fortune exceeds 120 characters"
    assert not text.endswith("\n"), "entry must not end with a newline"


def main() -> None:
    if len(FORTUNE) > 120:
        raise ValueError("fortune exceeds 120 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORTUNE)
    verify_written(OUTPUT_PATH)


if __name__ == "__main__":
    main()
