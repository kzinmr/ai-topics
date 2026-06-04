# Entity Consolidation During Ingest

When ingesting articles, you may discover that the target person/org already has **multiple entity pages** created by different pipelines or naming conventions. This reference documents the mid-ingest consolidation workflow.

## Trigger: When to Consolidate

Consolidate **immediately during ingest** when you encounter any of these signals:

1. **Index.md has multiple entries for the same person** — e.g., `[[entities/dialloibu]]` AND `[[entities/idiallo-com]]` AND your planned `[[entities/ibrahim-diallo]]`. Grep the index before creating a new page.
2. **`search_files` returns 0 but `os.path.exists()` returns True** — the slug you planned (`ibrahim-diallo.md`) doesn't exist, but the person does under a different slug (`dialloibu.md`).
3. **Same name normalized slug** — the hyphen-stripped lowercase version of your planned slug matches an existing file (e.g., `dialloibu` → `dialloibu`, `ibrahim-diallo` → `ibrahimdiallo`, `idiallo-com` → `idiallocom` — three different inputs normalizing to near-identical identifiers).

## Detection Sequence

```python
import os, re

wiki = "/opt/data/ai-topics/wiki"
target_name = "ibrahim diallo"  # The entity you're about to create

# 1. Scan index.md first
with open(f"{wiki}/index.md") as f:
    for line in f:
        if target_name.lower() in line.lower():
            print(f"Index match: {line.strip()}")

# 2. Check filesystem with normalized lookup
normalized = target_name.lower().replace(' ', '').replace('-', '').replace('_', '')
for fname in os.listdir(f"{wiki}/entities"):
    if fname.endswith('.md'):
        fnorm = fname.replace('.md', '').lower().replace('-', '').replace('_', '')
        if normalized in fnorm or fnorm in normalized:
            print(f"Filesystem match: {fname}")

# 3. Read found pages to confirm identity (slug alone is ambiguous)
for slug in ["dialloibu", "idiallo-com"]:
    path = f"{wiki}/entities/{slug}.md"
    if os.path.exists(path):
        with open(path) as f:
            first_5_lines = ''.join(f.readlines()[:5])
            if target_name.split()[0].lower() in first_5_lines.lower():
                print(f"Confirmed: {slug}.md is about {target_name}")
```

## Consolidation Workflow

### Step 1: Read All Files
Read the complete content of all candidate files. Identify what each contains:
- **dialloibu.md** → Comprehensive bio (bio, "The Machine Fired Me" essay, philosophy, 100 Principle)
- **idiallo-com.md** → LLM-assisted writing focus, pragmatic AI stance
- (your planned page) → The new article content to be added

### Step 2: Pick the Canonical Slug
- Prefer the **full name** hyphenated-form slug: `ibrahim-diallo` over `dialloibu` (username)
- Prefer the **directory convention**: `ibrahim-diallo` aligns with other entity pages by full name
- The canonical slug should be the one a future agent would search for

### Step 3: Create the Merged Page
Write a single canonical page that includes ALL content from all sources. In the frontmatter:
- Set `created` to the oldest creation date across all source pages
- Set `updated` to today
- Add all source filenames to `sources`
- Collect all unique tags from all source pages (verify against SCHEMA.md)

### Step 4: Delete the Non-Canonical Files
```python
# Git-aware deletion — git will detect this as a delete + rename
os.remove(f"{wiki}/entities/dialloibu.md")
os.remove(f"{wiki}/entities/idiallo-com.md")
```

Git's rename detection may automatically pair deletions with new files of similar content (`git status` shows `renamed: dialloibu.md → ibrahim-diallo.md`). This is fine and preserves some history.

### Step 5: Update index.md

Remove the old index entries and add the canonical one:

```python
# Using patch — remove old entries
patch(
    old_string="- [[entities/dialloibu]] — old description...\n- [[entities/dimitris-papailiopoulos]]",
    new_string="- [[entities/dimitris-papailiopoulos]]",
    path="~/wiki/index.md"
)

# Replace remaining entry with canonical
patch(
    old_string="- [[entities/idiallo-com]] — old description...",
    new_string="- [[entities/ibrahim-diallo]] — new description...",
    path="~/wiki/index.md"
)
```

**Alphabetical placement**: The canonical slug's alphabetical position may differ from the old entries. Verify the insertion point is correct — `ibrahim-diallo` goes between `ian-nuttall` and `iii-platform` (the `ib` section), NOT at the old position of `idiallo-com` (the `id` section). If the old entry was at the wrong alphabetical position, removing it and inserting at the correct position is part of the consolidation — don't keep it at the wrong place.

**Header counts**: If the old entries are removed, decrement `Indexed entries:` by 1 for each unique entry removed minus entries added. Since you're replacing N entries with 1, the net change is `-(N-1)`.

### Step 6: Update log.md
Log the consolidation under the relevant ingest or lint entry:
```
### Files Deleted (merged into <canonical-slug>.md)
- entities/dialloibu.md
- entities/idiallo-com.md
```

### Step 7: Verify and Commit
```bash
cd ~/ai-topics
git add wiki/
git commit -m "wiki: consolidate entities <old1> + <old2> → <canonical>"
git push
```

The pre-commit hook should pass cleanly because only canonical entries remain.

## When NOT to Consolidate Mid-Ingest

Defer consolidation to a lint pass when:
- The duplicate pages have **divergent content** that requires human judgment to merge (e.g., two different people with similar names)
- There are **3+ inbound wikilinks** pointing to each non-canonical page — fixing those is a separate task best done as a batch
- The consolidation would touch **10+ index entries** (e.g., a major slug rename of a well-linked entity)
- The non-canonical pages have **substantial external inbound references** (e.g., listed in a published paper or external site)

## Example: Ibrahim Diallo Consolidation (May 2026)

**Files discovered mid-ingest:**
- `entities/dialloibu.md` — Full bio, "Machine Fired Me" essay, philosophy (136 lines)
- `entities/idiallo-com.md` — LLM-assisted writing, pragmatic AI stance (81 lines)

**Planned file:** `entities/ibrahim-diallo.md` (new, token-burn critique)

**Resolution:** Consolidate all 3 into `entities/ibrahim-diallo.md` (canonical slug = full name). Deleted old files. Updated index (removed `dialloibu` + `idiallo-com` entries, added `ibrahim-diallo` at correct alphabetical position between `ian-nuttall` and `iii-platform`). Git detected rename: `dialloibu.md → ibrahim-diallo.md` (58% similarity).

**Key signal that triggered consolidation:** grep of `index.md` for "ibrahim diallo" returned 2 existing entries, indicating the entity was duplicated across pipelines.
