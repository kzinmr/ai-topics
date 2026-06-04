# Orphan Page Categorization Pattern

When wiki health detects 500+ orphan L2 pages (files on disk not in index.md),
batch-registering them all at once risks inserting stubs, date-prefixed news articles
accidentally placed in concepts/, and utility redirect pages.

**Use this 4-step categorization before any batch registration.**

## Step 1: Full Enumeration

```python
import os, re

wiki = '/opt/data/ai-topics/wiki'
with open(os.path.join(wiki, 'index.md')) as f:
    idx_content = f.read()

# Extract ALL indexed slugs
index_entries = set()
for line in idx_content.split('\n'):
    m = re.match(r'^- \[\[(entities|concepts|comparisons|events|queries)/([^|\]]+)', line.strip())
    if m:
        index_entries.add(f'{m.group(1)}/{m.group(2).strip()}')

# All files on disk (recursive)
all_files = set()
for cat in ['entities', 'concepts', 'comparisons', 'events', 'queries']:
    d = os.path.join(wiki, cat)
    if not os.path.isdir(d):
        continue
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith('.md'):
                rel_dir = os.path.relpath(root, wiki)
                slug = f.replace('.md', '')
                all_files.add(f'{rel_dir}/{slug}')

orphans = sorted(all_files - index_entries)
```

## Step 2: Categorize by Type

```python
date_prefix = [o for o in orphans if '/' in o and o.split('/')[-1].startswith(('2026-', '2025-'))]
underscore_prefix = [o for o in orphans if '/_index' in o]
at_prefix = [o for o in orphans if '/' in o and o.split('/')[-1].startswith('@')]
subdir_files = [o for o in orphans if o.count('/') > 1 and '/_index' not in o]
flat_files = [o for o in orphans if o.count('/') == 1 and o not in date_prefix and o not in underscore_prefix and o not in at_prefix]
```

| Category | Action | Reason |
|----------|--------|--------|
| Date-prefixed (2026-04-13-style) | **Skip** | News articles accidentally placed in concepts/ (raw/ error) |
| `_index.md` | **Skip** | Valid synthesis hubs, linked via subdirectory structure |
| `@-prefixed` | **Skip** | Utility/redirect pages, not real knowledge content |
| Subdirectory files (`fine-tuning/axolotl`) | **Skip** | Children of `_index` hubs, discoverable through parent |
| Flat orphans | **Candidate** | Real concept/entity pages that lack index entries |

## Step 3: Filter Stubs from Content

Among flat orphans, separate stubs (frontmatter-only, <500 bytes) from substantive content:

```python
candidates = []
for cat_slug in flat_orphans:
    cat, slug = cat_slug.split('/', 1)
    path = os.path.join(wiki, cat, slug + '.md')
    size = os.path.getsize(path)
    with open(path) as f:
        content = f.read()
    heading_count = content.count('\n## ')
    
    if size >= 500:
        candidates.append((cat_slug, size, heading_count))
    # else: skip stub
```

**Thresholds from 2026-05-25 session** (1,449 concept pages):
- <500B → typical stub (frontmatter + 1-2 lines)
- 500-2000B → thin page (has some content but may be sparse)
- 2000B+ → substantive page (3+ headings, meaningful prose)
- 5000B+ → deep page (10+ headings, thorough coverage)

Distribution observed: 461 stubs / 45 medium / 223 rich out of 729 flat concept orphans.

## Step 4: Batch Registration

Register in batches of 20 (per `_auto_apply_filter.max_auto_orphan_index: 20`).
Use the `scripts/batch_register_orphans.py` script for efficient batch insertion.

### Verification After Registration

```bash
# Count increased correctly
grep -c '^- \[\[concepts/' ~/ai-topics/wiki/index.md
grep -c '^- \[\[entities/' ~/ai-topics/wiki/index.md

# Spot-check specific entries
grep 'expected-slug' ~/ai-topics/wiki/index.md

# Structural validation
python3 scripts/validate_index.py

# Header counts consistent
grep 'Total pages:' ~/ai-topics/wiki/index.md
grep 'Not in index:' ~/ai-topics/wiki/index.md
```
