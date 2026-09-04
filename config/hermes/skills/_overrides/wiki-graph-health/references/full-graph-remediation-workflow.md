# Full Graph Remediation Workflow

When `wiki-graph-analysis` reports multiple issues, fix them in this order to avoid cascading problems.

## Correct Fix Sequence

| Step | Operation | Why this order |
|------|-----------|---------------|
| 1 | Bulk wikilink auto-fix | Fixes broken refs that would interfere with later index operations |
| 2 | Ghost entry removal | Cleans stale refs before adding new entries |
| 3 | Duplicate page merge (with content preservation!) | Must happen before index rebuild to avoid double-counting |
| 4 | Sources field population | Pure frontmatter fix, no structural dependencies |
| 5 | Index.md missing entries bulk-add | Final structural reconciliation after all above |
| 6 | Orphan page linking | Adds inbound links to pages still unreferenced after index rebuild |

**Why this order**: Wikilink fixes can create or resolve ghost entries. Duplicate merge deletes files (which creates ghosts). Index rebuild must see the final file set. Orphan linking depends on the final index.

## Step Details

### Step 1: Bulk Wikilink Auto-Fix

See `bulk-wikilink-auto-fix.md`. Expected output: 100s–1000s of fixed links.

```bash
cd ~/ai-topics && python3 /tmp/fix_wikilinks.py
git add wiki/ && git commit -m "wiki: fix auto-fixable wikilinks" && git push
```

### Step 2: Ghost Entry Removal

Detect and remove index entries pointing to nonexistent files.

```bash
cd ~/ai-topics && python3 -c "
import os, re
wiki_base = '/opt/data/ai-topics/wiki'
with open(f'{wiki_base}/index.md') as f:
    content = f.read()
ghost = []
for m in re.finditer(r'- \[\[([^\]]+)\]\]', content):
    target = m.group(1).split('|')[0].strip()
    if target.startswith(('entities/', 'concepts/', 'comparisons/', 'queries/', 'events/')):
        target_clean = re.sub(r'\.md$', '', target)
        if not os.path.exists(f'{wiki_base}/{target_clean}.md'):
            ghost.append(target_clean)
print(f'Ghost entries: {len(ghost)}')
for g in ghost: print(f'  {g}')
"
```

Remove via sed (single-line removal from index.md), then verify count drops to 0.

### Step 3: Duplicate Page Merge (with Content Preservation)

See `duplicate-page-merge.md`. **CRITICAL**: NEVER delete a page without first merging its unique content into the kept page.

Key steps:
1. Detect entity↔concept duplicates via normalized name matching
2. Sort by file size, keep larger
3. **Recover deleted content from git and merge unique sections into kept page**
4. Delete smaller files
5. Update index.md references
6. Run ghost detection post-merge

### Step 4: Sources Field Population

Add `sources: []` to pages missing the field in YAML frontmatter.

```python
def add_sources_field(content):
    m = re.match(r'^(---\n)(.*?)(\n---)', content, re.DOTALL)
    if not m: return content
    fm_start, fm_body, fm_end = m.group(1), m.group(2), m.group(3)
    if re.search(r'^tags:', fm_body, re.MULTILINE):
        fm_body = re.sub(r'(^tags:.*$)', r'\1\nsources: []', fm_body, count=1, flags=re.MULTILINE)
    else:
        fm_body = fm_body.rstrip() + '\nsources: []'
    return fm_start + fm_body + fm_end + content[m.end():]
```

Insert after `tags:` line when present, otherwise append to frontmatter end.

### Step 5: Index.md Missing Entries Bulk-Add

Compare filesystem pages against index.md entries. Add missing entries with descriptions.

Key rules:
- **Max depth 3**: Skip pages at depth 4+ (e.g., `concepts/a/b/c/d`)
- **Skip `_index.md`**: These are directory hub pages, not listed individually
- **Extract description**: Use frontmatter `description:` → `title:` → slug fallback
- **Alphabetical insertion**: Sort within correct section

```bash
cd ~/ai-topics && python3 /tmp/add_missing_to_index.py
git add wiki/index.md && git commit -m "wiki: add N missing pages to index.md" && git push
```

### Step 6: Orphan Page Linking

After index rebuild, find pages with zero inbound wikilinks.

```python
# Get all linked targets
linked = set()
for m in re.finditer(r'\[\[([^\]|#]+)', all_content):
    linked.add(re.sub(r'\.md$', '', m.group(1).strip()))

# Find unreferenced pages
orphans = [p for p in all_pages if p not in linked and p.split('/')[-1] not in linked]
```

Add links from parent pages or conceptually related pages. Archive pages (`_archive/`) can remain orphaned intentionally.

## Session Example (2026-07-05)

Complete remediation of wiki-graph-analysis findings:

| Metric | Before | After |
|--------|--------|-------|
| Broken wikilinks | 4,890 | ~3,900 (997 auto-fixed) |
| Ghost entries | 20 | 0 |
| Duplicate groups | 39→33 entity-concept | 0 (merged with content preservation) |
| Missing sources | 684 (31%) | 0 |
| Index missing entries | 1,994 | 0 |
| Orphan pages | 43 | 2 (archive only) |
| Total index entries | 259 | 2,676 |

Commits: `0fc66e1f` (wikilinks) → `49d977c8` (duplicates) → `9d90f7c8` (content recovery) → `53227faf` (sources) → `e15452d8` (index) → `60e1ed3b` (orphans)
