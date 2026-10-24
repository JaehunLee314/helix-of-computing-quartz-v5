#!/usr/bin/env python3
"""Put every display-math block ($$...$$) on its own lines.

    text $$x^2$$ more text

becomes

    text

    $$
    x^2
    $$

    more text

Code fences (```) are left untouched. Each file is rewritten in place,
and the original is kept as <file>.bak.

Usage: python fix_display_math.py note1.md note2.md ...
"""
import re
import shutil
import sys

FENCE = re.compile(r"(^```.*?^```[^\n]*$)", re.S | re.M)
DISPLAY = re.compile(r"[ \t]*\$\$(.+?)\$\$[ \t]*", re.S)


def to_block(match: re.Match) -> str:
    body = match.group(1).strip()
    return f"\n\n$$\n{body}\n$$\n\n"


def fix(text: str) -> str:
    parts = FENCE.split(text)
    for i in range(0, len(parts), 2):  # even indices are outside code fences
        s = DISPLAY.sub(to_block, parts[i])
        parts[i] = re.sub(r"\n{3,}", "\n\n", s)
    return "".join(parts).lstrip("\n")


def main(paths):
    for path in paths:
        with open(path, encoding="utf-8") as f:
            original = f.read()
        fixed = fix(original)
        if fixed == original:
            print(f"unchanged: {path}")
            continue
        shutil.copyfile(path, path + ".bak")
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"fixed:     {path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
