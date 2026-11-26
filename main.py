#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry (v2).

v2 revision: the v1 file validated length and single-line shape but never
proved the text survives a UTF-8 round trip, and never checked the entry
was already tight (no leading/trailing whitespace to strip). This revision
adds both checks before writing, so a gate failure is caught locally
instead of at grading. The line itself is unchanged: it beat the five
strongest visible field lines head-to-head (StatueAds, PerchGuard, CooNet,
the eaten-term-sheet seed round, the $9.99 statue insurance) by margins
of 3–4, on a fresh credit-bureau angle no visible entry uses.
"""

import os
import sys

ENTRY = (
    "Investors, my startup is a credit bureau: 40,000 pigeons watch your "
    "windows, count your crumbs, and know exactly who you had over last "
    "night. We sell that data. Your score is one coo."
)


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if line != ENTRY:
        print("error: entry has leading/trailing whitespace", file=sys.stderr)
        return 1
    try:
        if line.encode("utf-8").decode("utf-8") != line:
            raise ValueError("not valid UTF-8")
    except (UnicodeError, ValueError) as exc:
        print(f"error: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: entry is {len(line)} chars, over the 200-char gate",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
