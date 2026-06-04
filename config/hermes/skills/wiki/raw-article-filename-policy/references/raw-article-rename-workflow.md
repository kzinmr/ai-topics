# Raw Article Rename Workflow

When a raw article filename needs correction (wrong date, typo, series mismatch), renaming it breaks all wikilink references across the wiki. This reference captures the full repair pattern.

## Pre-flight: Find All References

```bash
# Search the entire wiki for the old filename stem
search_files(pattern="OLD_FILENAME_STEM", target="content", path="wiki/")
```

Typical reference locations:
- `wiki/index.md` — main index entries
- `wiki/log.md` — historical log entries
- `wiki/entities/*.md` — entity page cross-references
- `wiki/concepts/*.md` — concept page sources/references
- `wiki/raw/transcripts/*.md` — transcript companion links
- `wiki/raw/archived/triage/**/*.json` — **leave as-is** (historical snapshots)

## Step-by-Step

### 1. Rename the file
```bash
terminal("mv ~/wiki/raw/articles/OLD_NAME.md ~/wiki/raw/articles/NEW_NAME.md")
```

### 2. Update frontmatter
```python
patch(mode="replace", path="wiki/raw/articles/NEW_NAME.md",
      old_string="date: OLD_DATE", new_string="date: NEW_DATE")
```

### 3. Batch-update all references
Use `patch(mode="patch")` with multiple `*** Update File` blocks to update all references in one call. The old filename stem is the search key.

**Files to update:**
- `wiki/index.md` (usually 1-2 entries)
- `wiki/log.md` (historical entries — update for link consistency)
- `wiki/entities/*.md` (entity cross-references)
- `wiki/concepts/*.md` (concept sources and references)
- `wiki/raw/transcripts/*.md` (companion links)

**Files to SKIP:**
- `wiki/raw/archived/triage/**/*.json` — these are point-in-time triage snapshots. The old filename is historically accurate for when the triage ran.

### 4. Add a log entry
Prepend a new section to `wiki/log.md` documenting the rename:
```markdown
## [YYYY-MM-DD] Rename | <brief description>

- **Renamed**: `raw/articles/OLD_NAME` → `raw/articles/NEW_NAME` — <reason>
- **Updated frontmatter**: `field: new_value`
- **Updated references**: list of files updated
```

### 5. Commit + push
```bash
terminal("cd ~/ai-topics && git add wiki/ && git commit -m 'wiki: rename ...' && git push")
```

## Edge Cases

- **AGENTS.md "raw/ immutable" rule**: The convention is that `raw/` files are source material and should not be edited. However, filename corrections and date fixes are legitimate exceptions when the user explicitly requests them. The immutability rule is about preserving content integrity, not preventing metadata corrections.
- **Multiple references in one file**: `index.md` often has 2+ references (raw articles section + transcripts section). Make sure to catch all of them.
- **Log.md historical entries**: These are append-only in principle, but when they reference a file that no longer exists at that path, updating the reference is justified for consistency.
