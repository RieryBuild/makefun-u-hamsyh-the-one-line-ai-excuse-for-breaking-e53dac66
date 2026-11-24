"""One-line AI excuse for breaking production.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt with no
trailing newline, so the sealed scorer reads exactly one line.
"""

import os

LINE = "I fixed production's memory leak by deleting the memory, and honestly the servers have never been quieter."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
