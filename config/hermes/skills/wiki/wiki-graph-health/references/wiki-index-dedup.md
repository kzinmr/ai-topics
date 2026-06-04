# Index Deduplication

Pattern for detecting and removing duplicate entries from `wiki/index.md`. See also the **False-Positive Trap** in `llm-wiki` skill — inline cross-references in description text are NOT duplicates.

## Pre-check: Primary vs All Wikilinks

When a report claims N duplicate index entries, filter by **line-starting (primary) wikilinks** first:

```python
# Primary (line-starting) — correct for dedup
m = re.match(r'^- \[\[(entities|concepts|comparisons|queries|events)/([^|\]]+)', line)
key = f"{m.group(1)}/{m.group(2)}"

# ALL wikilinks — inflated by inline cross-refs (wrong for dedup)
all_links = re.findall(r'\[\[(entities|concepts|comparisons|queries|events)/([^|\]]+)\]\]', content)
```

Observed: 48 of 67 reported "duplicates" were inline cross-references. Only act on primary-link duplicates.

## Cluster Detection for Contiguous Duplicate Blocks

When N primary duplicates survive filtering, check if they form a **contiguous block** (consecutive lines at positions L+1..L+N that mirror L-N-1..L-1 with identical text). If yes, it's a single bulk-duplication incident, not N independent issues:

```python
import re
with open('wiki/index.md') as f:
    lines = f.readlines()

prev_slug, cluster_start = None, None
for i, line in enumerate(lines):
    m = re.match(r'^- \[\[(entities|concepts|comparisons|queries|events)/([^|\]]+)', line.strip())
    if m:
        slug = f"{m.group(1)}/{m.group(2)}"
        if slug == prev_slug and cluster_start is None:
            cluster_start = i - 1
        elif slug != prev_slug:
            cluster_start = None
        prev_slug = slug
```

**Fix**: Remove the entire duplicate block in one operation (not N individual pair removals). Verify by re-running the primary-link count.

## Detection

```bash
grep -n '^- \[' wiki/index.md | cut -d' ' -f2 | sort | uniq -c | sort -rn | head -20
```

## Skeleton-vs-Rich from build_x_wiki.py

When a skeleton entry (`**X/Twitter**`, `**Name**`, `**Blog**`) duplicates an existing rich entry: keep the rich entry, remove the skeleton.

## Adjacent Duplicate Blocks (Consecutive Lines)

When two entries for the same slug appear back-to-back, remove BOTH in a SINGLE `patch` operation covering all adjacent lines plus one surrounding line each side.

## Safety Checks After Dedup

```bash
python3 scripts/validate_index.py
grep -n '[[entities/<slug>]]' wiki/index.md  # count == 1 for primary, >1 is inline cross-refs
```

## Automated Script

For bulk dedup:

```python
from collections import defaultdict
import re

with open("wiki/index.md") as f:
    lines = f.readlines()

entries = defaultdict(list)
for i, line in enumerate(lines):
    m = re.match(r'- \[\[(.*?)(?:\||\])', line.strip())
    if m and not m.group(1).endswith('/_index'):
        entries[m.group(1)].append(i)

lines_to_remove = set()
for key, indices in entries.items():
    if len(indices) > 1:
        todo = [i for i in indices if '**TODO**' in lines[i] or 'Enrich this page' in lines[i]]
        rich = [i for i in indices if i not in todo]
        if rich:
            lines_to_remove.update(rich[1:])
        lines_to_remove.update(todo)

for idx in sorted(lines_to_remove, reverse=True):
    lines.pop(idx)
```

## Rules
- `[[entities/foo]]` and `[[concepts/foo]]` are NOT duplicates if both files exist
- `_index` entries are legitimate — never remove
- Remove bottom-up to preserve line numbers
- Verify against `os.path.exists()` after dedup
