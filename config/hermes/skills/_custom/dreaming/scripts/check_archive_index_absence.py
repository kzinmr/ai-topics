#!/usr/bin/env python3
"""Pattern E archive-index absence probe for dreaming-wiki-ingest.

Lists recent raw articles whose frontmatter `url:` is ABSENT from
`archive_index.json`. Absence = never decided by any pipeline triage =
genuine Pattern E candidate. This is the decisive dedup signal when the
upstream dreaming-group claims saturation (validated 2026-08-11, 2026-08-12):
never trust a saturation verdict without running this check.

Usage:
  python3 check_archive_index_absence.py [--days N] [--dir RAW_DIR]

Defaults: N=3 days, RAW_DIR=/opt/data/ai-topics/wiki/raw/articles.
Works in cron mode (no pipes, no subprocess). Prints never-archived files
with mtime + url, then a count. Exit 0 always (grep-style exit codes are
unreliable after head-piping; use the printed count).
"""
import json, os, re, sys
from datetime import datetime

ARCHIVE_INDEX = '/opt/data/ai-topics/wiki/raw/archived/triage/archive_index.json'
RAW_DIR = '/opt/data/ai-topics/wiki/raw/articles'
DAYS = 3

args = sys.argv[1:]
if '--days' in args:
    DAYS = int(args[args.index('--days') + 1])
if '--dir' in args:
    RAW_DIR = args[args.index('--dir') + 1]

idx = json.load(open(ARCHIVE_INDEX))
urls = set(idx.get('urls', idx)) if isinstance(idx, dict) else set(idx)

files = []
for f in os.listdir(RAW_DIR):
    if not f.endswith('.md'):
        continue
    p = os.path.join(RAW_DIR, f)
    mt = os.path.getmtime(p)
    if mt > datetime.now().timestamp() - DAYS * 86400:
        files.append((f, mt))
files.sort(key=lambda x: -x[1])

print(f'Recent files ({DAYS}d): {len(files)}')
print(f'Archive index urls: {len(urls)}')

missing = []
for f, mt in files:
    try:
        head = open(os.path.join(RAW_DIR, f), encoding='utf-8', errors='replace').read(2000)
    except Exception:
        continue
    m = re.search(r'^url:\s*(.+)$', head, re.MULTILINE)
    u = m.group(1).strip().strip('"').strip("'") if m else ''
    ts = datetime.fromtimestamp(mt).strftime('%m-%d %H:%M')
    if u and u not in urls:
        missing.append((f, u, ts))

print('\n--- Never archived (absent from archive_index) ---')
for f, u, ts in missing:
    print(f'{ts} | {f} | {u[:100]}')
print(f'\nTotal never-archived: {len(missing)}')
print('NOTE: absence = never triaged, but not all are gaps — read bodies,')
print('check entity/concept coverage, then classify (reference/take/skip).')
