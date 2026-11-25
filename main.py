"""Laugh Track: The Crypto Trading Joke Contest.

Writes one joke about crypto and trading life to /output/entry.txt.
Pure Python standard library. The gate: UTF-8 text, 1-200 characters,
not only whitespace, a single line.
"""

import os

JOKE = (
    "My trading strategy is simple: buy high, panic-sell low, "
    "then buy it back higher and call it dollar-cost averaging."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Validation gate: re-read the file and assert the sealed gate's rules.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        text = f.read()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    print(f"OK: {len(text)} chars, one line")


if __name__ == "__main__":
    main()
