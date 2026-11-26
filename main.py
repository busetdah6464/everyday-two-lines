#!/usr/bin/env python3
"""Write the two-line entry to /output/entry.txt.

Deterministic, standard library only, no network.
Line 1 explains a traffic jam to a 10-year-old through one vivid analogy.
Line 2 says in one sentence what that analogy maps and what it leaves out.
"""

import os

LINES = [
    "A traffic jam is a herd of elephants all trying to squeeze through one garden gate at once, so the whole herd shuffles forward one tiny step at a time.",
    "It works because the elephants show a crowd of big, slow things stuck at one narrow opening, but it leaves out that cars are driven by people making choices, not animals following a herd.",
]


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(LINES) + "\n")


if __name__ == "__main__":
    main()
