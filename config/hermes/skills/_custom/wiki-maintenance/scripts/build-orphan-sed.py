#!/usr/bin/env python3
"""
Build a sed script to insert orphan index entries after a specific line number.

Usage:
    python3 references/build-orphan-sed.py wiki/index.md 1406 [--dry-run]

Or call from Python, passing a list of entries and the target line number.

The sed script format is correct (text lines do NOT end with \):
    LINE_NUMa\
    - [[concepts/path/name]] -- description
    LINE_NUMa\
    - [[concepts/path/name2]] -- description 2

Pitfall avoided: text lines after `a\` must NOT have trailing backslash,
or sed will swallow the next `a\` command as continuation text.
"""

import argparse
import sys
import tempfile
import subprocess


def build_sed_script(entries, line_num, output_path):
    """
    Build a sed script that inserts `entries` after `line_num`.

    Args:
        entries: list of str, each a complete '- [[...]] -- desc' line
        line_num: int, the line number to append after
        output_path: str, path to write the sed script
    """
    with open(output_path, 'w') as f:
        for e in entries:
            # Escape forward slashes for sed
            text = e.replace('/', '\\/')
            f.write(f'{line_num}a\\\n')
            f.write(text + '\n')


def verify_ordering(entries):
    """Verify entries are in forward alphabetical order."""
    sorted_entries = sorted(entries)
    if entries != sorted_entries:
        print("WARNING: Entries are NOT in alphabetical order!", file=sys.stderr)
        for i, (a, b) in enumerate(zip(entries, sorted_entries)):
            if a != b:
                print(f"  Position {i}: has '{a[:60]}...' should be '{b[:60]}...'",
                      file=sys.stderr)
                break
        return False
    return True


def get_index_entry_count(index_path):
    """Count total - [[...]] lines in index.md for summary line updates."""
    import re
    count = 0
    with open(index_path) as f:
        for line in f:
            if re.match(r'^- \[\[', line.strip()):
                count += 1
    return count


def main():
    parser = argparse.ArgumentParser(
        description='Build sed script for orphan index entry insertion')
    parser.add_argument('index_path', nargs='?', help='Path to wiki/index.md')
    parser.add_argument('line_num', nargs='?', type=int,
                        help='Line number to append after')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print sed script to stdout instead of writing')
    parser.add_argument('--entries', nargs='+', default=None,
                        help='Entries to insert (one per arg)')
    args = parser.parse_args()

    if args.entries:
        entries = args.entries
    else:
        # Example entries — replace with actual data
        entries = [
            '- [[concepts/harness-engineering/agentic-workflows/how-agents-work]] -- How Coding Agents Work',
            '- [[concepts/harness-engineering/agentic-workflows/interactive-explanations]] -- Interactive Explanations',
            '- [[concepts/harness-engineering/system-architecture/building-effective-agents]] -- Building Effective Agents',
        ]

    verify_ordering(entries)

    if args.dry_run or not args.index_path:
        for e in entries:
            text = e.replace('/', '\\/')
            print(f'{args.line_num or 0}a\\')
            print(text)
    else:
        output = '/tmp/fix_orphans.sed'
        build_sed_script(entries, args.line_num, output)
        print(f'Sed script written to {output} ({len(entries)} entries)')

        # Count before/after entries
        before = get_index_entry_count(args.index_path)
        print(f'Current index entries: {before}')
        print(f'After insertion: {before + len(entries)}')
        print(f'\nTo apply: sed -i -f {output} {args.index_path}')
        print(f'To revert: git checkout -- {args.index_path}')


if __name__ == '__main__':
    main()
