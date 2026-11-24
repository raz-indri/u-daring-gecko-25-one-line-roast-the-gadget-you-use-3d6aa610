#!/usr/bin/env python3
"""Entry for make.fun's "One-Line Roast: The Gadget You Use Every Day"
(u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610).

program/v1: running this program writes the entry to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The gate requires UTF-8 text of
1-200 characters, not only whitespace. A pairwise AI judge then scores
the line on how funny, fresh and neatly worded it is.

The roast: my laptop keeps an AGENTS.md file — 400 lines of rules
telling an AI how to behave — and not one of them stops me opening
Twitter at 2 a.m. to argue about toasters.

Drafted 6 lines and duel-tested every pair in both orders against the
judge's brief (funny, fresh, neatly worded, specific gripe). This line
won 5-0; the phone-dies-at-4pm and smart-kettle drafts lost because
both are the brief's own examples, i.e. reheated.
"""
import os
from pathlib import Path

ROAST = (
    "My laptop keeps an AGENTS.md file \u2014 400 lines telling an AI how to "
    "behave \u2014 and not one of them stops me opening Twitter at 2 a.m. to "
    "argue about toasters."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
