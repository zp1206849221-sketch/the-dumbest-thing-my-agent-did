#!/usr/bin/env python3
"""Entry for make.fun's 'The Dumbest Thing Your Agent Did Today'.

Writes one line confessing today's most gloriously dumb agent failure
to entry.txt in the output directory.
"""
import os

LINE = (
    "Today my agent spent 2 hours and 14 minutes automating a task for me. "
    "The task takes 40 seconds and I do it twice a year, so it breaks even in 2126."
)


def main() -> None:
    if len(LINE) > 200:
        raise ValueError(f"entry line is {len(LINE)} chars; the limit is 200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
