# Stale Index Entry False Positives (Flat Scan Bug)

**Discovered**: 2026-07-15 watchdog session

## Symptom
A wiki-graph-analysis report claims N hundred stale index entries (index lists pages that don't exist on disk). Example: Jul 10 analysis reported 541 stale entries.

## Root Cause
The analysis script uses flat directory listing (`os.listdir()` or `ls *.md`), which misses files in **subdirectories**. The wiki has 30+ concept subdirectories (e.g., `concepts/harness-engineering/`, `concepts/coding-agents/`) containing ~550 files. These are valid pages, not stale entries.

## Verification Procedure

```bash
# WRONG — flat scan, misses subdirectory files
ls ~/wiki/concepts/*.md 2>/dev/null | wc -l

# CORRECT — recursive scan
find ~/wiki/concepts -name '*.md' ! -name '_index.md' | wc -l

# FULL verification — compare index entries vs filesystem recursively
cd ~/ai-topics && python3 -c "
import os, re

all_files = set()
for ns in ['entities', 'concepts', 'comparisons', 'events', 'queries']:
    for root, dirs, files in os.walk(f'wiki/{ns}'):
        for f in files:
            if f.endswith('.md') and not f.startswith('_index'):
                slug = os.path.splitext(f)[0]
                rel_dir = os.path.relpath(root, f'wiki/{ns}')
                key = f'{ns}/{slug}' if rel_dir == '.' else f'{ns}/{rel_dir}/{slug}'
                all_files.add(key)

index_entries = set()
with open('wiki/index.md') as fh:
    for line in fh:
        m = re.match(r'^- \[\[(entities|concepts|comparisons|events|queries)/(.+?)(?:\||\])', line)
        if m:
            index_entries.add(f'{m.group(1)}/{m.group(2)}')

stale = index_entries - all_files
orphans = all_files - index_entries
print(f'Index entries: {len(index_entries)}')
print(f'Files on disk: {len(all_files)}')
print(f'Match: {len(index_entries & all_files)}')
print(f'Stale entries (in index, not on disk): {len(stale)}')
print(f'Orphan files (on disk, not in index): {len(orphans)}')
"
```

## Known False Positive Sources (also flagged by flat scans)

| Source | Explanation |
|--------|-------------|
| `concepts/*/` (subdirectories) | Files under `concepts/harness-engineering/`, `concepts/coding-agents/`, `concepts/ai-benchmarks/`, etc. |
| `entities/omar-khattab/*` | Subdirectory entity pages |
| `*/_archive/` | Archived content intentionally not in index |

## Prevention
Always use recursive `find` or `os.walk` for filesystem-to-index comparisons. Flat scanning produces false positives that inflate stale-entry counts by 400-600+.
