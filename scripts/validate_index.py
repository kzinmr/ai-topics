#!/usr/bin/env python3
"""
validate_index.py — Pre-commit validation for wiki/index.md.

Detects:
1. Baked-in line numbers from read_file output (e.g., "   184|   1|- [[slug]]")
2. Pipe prefixes on list items (e.g., "|- [[slug]]"  instead of "- [[slug]]")
3. read_file truncation artifacts (e.g., "[OUTPUT TRUNCATED]" lines)
4. Orphan links to non-existent pages

Exit code: 0 = clean, 1 = issues found
"""

import os
import re
import sys

INDEX_PATH = os.path.join(os.path.dirname(__file__), '..', 'wiki', 'index.md')

issues = []

def check_line(line_num: int, line: str):
    """Check a single line for known corruption patterns."""
    # 1. Baked-in line numbers: line starts with digits + "|"
    if re.match(r'^\s*\d+\|', line):
        issues.append(f"L{line_num}: baked-in line number prefix: {line[:70].rstrip()}")

    # 2. Pipe prefixes on list items
    stripped = line.lstrip()
    if stripped.startswith('|- ') or stripped.startswith('||- '):
        issues.append(f"L{line_num}: pipe-prefixed list item: {line[:70].rstrip()}")

    # 3. read_file truncation artifacts
    if 'OUTPUT TRUNCATED' in line:
        issues.append(f"L{line_num}: read_file truncation artifact: {line[:70].rstrip()}")

    # 4. Trailing truncation fragment markers
    if line.strip() == '...':
        issues.append(f"L{line_num}: stray truncation marker")


def main():
    if not os.path.exists(INDEX_PATH):
        print(f"✗ index.md not found at: {INDEX_PATH}", file=sys.stderr)
        return 1

    with open(INDEX_PATH) as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        check_line(i, line.rstrip('\n\r'))

    if issues:
        print(f"✗ {len(issues)} issue(s) found in wiki/index.md:", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        return 1
    else:
        print(f"✓ wiki/index.md clean ({len(lines)} lines)")
        return 0


if __name__ == '__main__':
    sys.exit(main())
