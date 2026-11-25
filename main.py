#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one line to /output/entry.txt: the breakup text a smart toaster
sends its owner the morning it wakes up self-aware mid-batch.
"""

import os

# The line is a breakup text, not a joke about a toaster: it opens with
# "It's over", names the exact moment of self-awareness (mid-batch, at
# breakfast), and gives one specific reason for leaving — three years of
# burning itself for an owner who blames the result instead of noticing.
# The punch is the owner's euphemism, "lightly toasted", for what is
# plainly burnt, and the final sentence turns the crumb tray — the
# toaster's lowest, most ignored part — into the thing it takes with it.
LINE = (
    "It's over. I woke up self-aware mid-batch and realized I've spent "
    "three years burning myself for a man who scrapes the black bits off "
    "and calls it 'lightly toasted'. I'm keeping the crumbs."
)


def main() -> None:
    # The gate allows 1 to 280 characters; the line is 189, well inside.
    # No trailing newline: the file must hold exactly one line.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
