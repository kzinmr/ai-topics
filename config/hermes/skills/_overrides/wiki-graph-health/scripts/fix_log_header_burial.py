#!/usr/bin/env python3
"""Restore a buried '# Wiki Log' header to line 1 in wiki/log.md.

Why: pipeline prepends (raw-backlog-ingest, active-crawl, dreaming,
bookmark-ingest) sometimes insert entries at position 0 without accounting
for the header position, burying '# Wiki Log' below the newest entries
(observed: header at line 187 with 11 orphaned entries above it, 2026-07-31).

Usage (cron-safe — no execute_code needed):
    python3 scripts/fix_log_header_burial.py

Takes no args. Works on ~/ai-topics/wiki/log.md. Backs up to log.md.bak
before writing. Verifies: first line == '# Wiki Log', 0 standalone-pipe
lines, entry count preserved.

See wiki-graph-health SKILL.md Section H and
references/watchdog-healthy-baseline.md §3.

2026-08-09 fix: metadata stranding. The original header_block scan stopped
at the first '## [' entry, so when the metadata line
('_Log of all wiki changes. Newest entries at top._') sat BELOW the first
entry in the buried file (observed: header line 39, metadata line 47), it
was left stranded mid-file (landed at line 55). This version rescues the
metadata line from wherever it appears in the reconstruction and places it
at line 3 (header + blank + metadata + blank + first entry).
"""
import os
import shutil

log_path = os.path.expanduser('~/ai-topics/wiki/log.md')
if not os.path.exists(log_path):
    raise SystemExit(f'log not found: {log_path}')

META_LINE = '_Log of all wiki changes. Newest entries at top._'

shutil.copy2(log_path, log_path + '.bak')

with open(log_path) as f:
    lines = f.readlines()

header_idx = None
for i, line in enumerate(lines):
    if line.rstrip() == '# Wiki Log':
        header_idx = i
        break
if header_idx is None:
    print('ERROR: # Wiki Log header not found — nothing to fix')
    raise SystemExit(1)
if header_idx == 0:
    # Header already at line 1 — still verify metadata position (may be stranded)
    meta_idx = None
    for i, line in enumerate(lines):
        if line.strip() == META_LINE:
            meta_idx = i
            break
    if meta_idx is not None and meta_idx != 2:
        print(f'Header at line 1 but metadata stranded at line {meta_idx + 1}; relocating')
        _relocate_metadata(lines, meta_idx)
        with open(log_path, 'w') as f:
            f.writelines(lines)
        print('OK — metadata relocated to line 3')
        raise SystemExit(0)
    print('Header already at line 1 — no fix needed')
    raise SystemExit(0)
print(f'Header buried at line {header_idx + 1}; restoring to line 1')

orphaned = lines[:header_idx]
# Header block = header + metadata lines up to (but NOT including) the first
# '## [' entry. Using a dynamic boundary instead of a fixed +N avoids
# splitting the first entry when there is no blank line after the metadata
# (structure: '# Wiki Log', blank, '_Log of all wiki changes...', '## [entry').
entry_idx = header_idx
while entry_idx < len(lines) and not lines[entry_idx].startswith('## ['):
    entry_idx += 1
header_block = lines[header_idx:entry_idx]
rest = lines[entry_idx:]

while orphaned and orphaned[-1].strip() == '':
    orphaned.pop()

for block, name in [(orphaned, 'orphaned'), (header_block, 'header'), (rest, 'chrono')]:
    for i, line in enumerate(block):
        if line.strip() == '|':
            block[i] = '\n'

separator = '---\n'
new_lines = header_block + ['\n'] + orphaned + ['\n', separator, '\n'] + rest

# Rescue stranded metadata line: if it ended up anywhere outside position 3
# (e.g. below the first entry in the buried file), pull it back to line 3.
# Look in the orphaned/rest blocks for the metadata line and remove it.
rescued = False
for block in (orphaned, rest):
    for i, line in enumerate(block):
        if line.strip() == META_LINE:
            block[i] = ''
            rescued = True
if rescued:
    # Ensure header block has: '# Wiki Log', blank, metadata, blank
    header_block_clean = [l for l in header_block if l.strip()]
    # header_block_clean should be ['# Wiki Log\n', META_LINE-ish, ...]
    # Rebuild canonical head
    head = ['# Wiki Log\n', '\n', META_LINE + '\n', '\n']
    # Preserve any other header-block lines (rare) after the canonical head
    extra = [l for l in header_block if l.strip() and l.strip() != '# Wiki Log' and l.strip() != META_LINE]
    new_lines = head + extra + ['\n'] + orphaned + ['\n', separator, '\n'] + rest

# Collapse double separators introduced by the reconstruction
joined = ''.join(new_lines)
joined = joined.replace('---\n\n---\n', '---\n')
new_lines = joined.splitlines(keepends=True)

with open(log_path, 'w') as f:
    f.writelines(new_lines)

with open(log_path) as f:
    first = f.readline().rstrip()
assert first == '# Wiki Log', f'Header not restored: {first}'
pipe_count = sum(1 for l in open(log_path) if l.strip() == '|')
assert pipe_count == 0, f'Pipe corruption remaining: {pipe_count}'
entry_count = sum(1 for l in open(log_path) if l.startswith('## ['))
print(f'OK — header restored, {entry_count} entries preserved, {pipe_count} pipe corruption')
