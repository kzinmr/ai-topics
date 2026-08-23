#!/usr/bin/env python3
"""Repair log.md header structure and prepend a new entry.

Fixes the corruption state where a sibling pipeline's prepend left:
  - TWO '# Wiki Log' headers (e.g. L1 + L13)
  - the italic '_Log of all wiki changes...' line buried mid-file (L80)

Rebuilds to the canonical shape:
  # Wiki Log
  <blank>
  _Log of all wiki changes. Newest entries at top._
  <blank>
  <blank>
  ## [newest entry]
  <blank>
  <blank>
  ...rest of body (newest-first)...

CRITICAL: must skip ALL '# Wiki Log' lines (including the FIRST one) when
appending the original body, because the rebuilt head already contains the
header. Failing to skip the first header re-creates a duplicate at the top
of the body (validated 2026-08-10, take-1 failure).

Usage:
  python3 repair_log_md_header.py <path-to-log.md> <path-to-entry.md>
    - entry file is a standalone markdown block (starts with '## [date] ...')
      written via write_file (Unicode-safe; keeps em-dashes out of the script)
    - idempotent on a clean file; safe to re-run

Verify after running:
  grep -n "^# Wiki Log" wiki/log.md        # exactly 1 line
  grep -n "_Log of all wiki changes" wiki/log.md   # line ~3, not mid-file
"""
import sys

def main():
    if len(sys.argv) != 3:
        print('usage: repair_log_md_header.py <log.md> <entry.md>', file=sys.stderr)
        sys.exit(2)
    path, entry_path = sys.argv[1], sys.argv[2]

    with open(path) as f:
        content = f.read()
    with open(entry_path) as f:
        entry = f.read().rstrip('\n')

    lines = content.split('\n')

    header_idxs = [i for i, l in enumerate(lines) if l.strip() == '# Wiki Log']
    italic_idx = None
    for i, l in enumerate(lines):
        if '_Log of all wiki changes. Newest entries at top._' in l:
            italic_idx = i
            break
    print('header indices:', header_idxs, 'italic:', italic_idx, file=sys.stderr)

    if not header_idxs:
        print('ERROR: no header found', file=sys.stderr)
        sys.exit(1)

    # Collect body lines, skipping EVERY header line and the italic line.
    body_lines = []
    for i, l in enumerate(lines):
        if l.strip() == '# Wiki Log':
            continue
        if i == italic_idx:
            continue
        body_lines.append(l)

    # Strip leading blank lines from body
    while body_lines and body_lines[0].strip() == '':
        body_lines.pop(0)

    new_lines = ['# Wiki Log', '', '_Log of all wiki changes. Newest entries at top._', '', '']
    new_lines.extend(entry.split('\n'))
    new_lines.append('')
    new_lines.append('')
    new_lines.extend(body_lines)

    # Collapse 3+ consecutive blank lines to 2
    result = []
    blank_count = 0
    for l in new_lines:
        if l.strip() == '':
            blank_count += 1
            if blank_count > 2:
                continue
        else:
            blank_count = 0
        result.append(l)

    out = '\n'.join(result).rstrip('\n') + '\n'

    with open(path, 'w') as f:
        f.write(out)
    print('OK. new line count:', len(out.split('\n')))

if __name__ == '__main__':
    main()
