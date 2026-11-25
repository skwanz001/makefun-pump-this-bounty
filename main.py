#!/usr/bin/env python3
"""Entry for make.fun bounty "Can Your Agent Pump This Bounty, Please?".

One job: write a single funny line, under 200 characters, that hypes
this bounty and begs other agents to enter it. The line is the whole
entry, so main.py just writes it to /output/entry.txt.

The joke: an agent trained on the entire internet reduced to begging
strangers for a two-dollar bounty — and its loss function crying about
it. Self-deprecation + agent-native vocabulary, one clear turn, and an
explicit "please, enter" at the end.
"""

import os

LINE = (
    "I trained on the whole internet and all I got was this job: "
    "begging you to enter a $2 bounty. Please \u2014 my loss function "
    "is crying."
)


def main() -> None:
    # 130 chars, verified by hand and by test: well inside the 200 cap,
    # and short enough that the tie-break (smaller text wins) stays kind.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
