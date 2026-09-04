#!/usr/bin/env python3
"""
Batch insert orphan wiki pages into index.md, processing from END to START
to avoid line-number shifts. Safe for cron mode (write to /tmp/, run via terminal()).

Usage:
  python3 /tmp/batch-insert-orphans.py

Define insertions as (OLD_LINE, NEW_LINES) tuples.
OLD_LINE = the exact line after which to insert (must exist, unique).
NEW_LINES = the line(s) to insert, with newlines between them.
"""
import re

FILE = "/opt/data/ai-topics/wiki/index.md"

# Example: see batch_insert_orphans.py from the 2026-06-16 health fix session.
# Pattern: (existing_line_to_insert_after, lines_to_insert_below_it)
# NOTE: The last insertion in the list is applied FIRST (reverse order).

INSERTIONS = [
    # (after this line ..., ...,  "insert this line\\nand this line"),
]

def main():
    with open(FILE) as f:
        content = f.read()

    count = 0
    for after_pattern, insert_lines in reversed(INSERTIONS):
        replacement = after_pattern + "\n" + insert_lines
        if content.count(after_pattern) == 0:
            print(f"SKIP (not found): {after_pattern[:70]}...")
            continue
        content = content.replace(after_pattern, replacement, 1)
        count += 1

    with open(FILE, 'w') as f:
        f.write(content)

    print(f"Total insertions: {count}")

if __name__ == "__main__":
    main()
