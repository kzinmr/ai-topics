# Batch Reference Update After File Relocation

> Moving source files between wiki directories and updating all references. Covers both intra-raw relocations and top-level reorganizations (e.g., `raw/transcripts/` → `transcripts/`).

## When This Applies

- YouTube transcripts misclassified as articles → move to appropriate directory
- Papers misclassified → move to `raw/papers/`
- Newsletter digests reorganized → move between `raw/newsletters/` and `raw/inbox/`
- Any `git mv` of a source file that's referenced in wiki page frontmatter or body
- **Top-level reorganization**: Moving files out of `raw/` to a new wiki-level directory (e.g., `raw/transcripts/` → `transcripts/`)

## Step-by-Step

### 1. Classify files to move

When moving YouTube-related files, distinguish by `type:` field in frontmatter:
- `type: transcript` → raw speech-to-text, move to transcripts dir
- `type: talk` / `type: podcast` / `type: panel` → structured summaries, keep in `raw/articles/`

### 2. Discover all references

Search the entire wiki for every file path that will change:

```bash
# For a path prefix change (e.g., raw/transcripts/ → transcripts/):
grep -rl 'raw/transcripts/' --include='*.md' ~/wiki/
```

Also search for files by stem (without `.md`) to catch wikilinks without extension:
```bash
grep -rl 'raw/articles/2024-12-13_ilyasutskever-transcript' --include='*.md' ~/wiki/
```

Check both `[[raw/transcripts/foo]]` wikilink syntax and `raw/transcripts/foo.md` bare path syntax.

### 3. Move files with git mv

```bash
cd ~/ai-topics
mkdir -p wiki/<target-dir>
git mv wiki/<source-dir>/<file>.md wiki/<target-dir>/
```

### 4. Update internal references within moved files

Check the moved files themselves for references to other moved files or to their old location:
```bash
grep -n 'raw/transcripts/\|raw/articles/' ~/wiki/transcripts/*.md
```

### 5. Bulk-update external references with sed

For path prefix changes across many files:
```bash
cd ~/ai-topics/wiki
grep -rl 'raw/transcripts/' --include='*.md' . | while read f; do
  sed -i 's|raw/transcripts/|transcripts/|g' "$f"
done
```

For individual file renames, use `patch` with `replace_all=true`.

### 6. Update structural files

When moving to a **new top-level directory**:
- **AGENTS.md**: Add directory to tree, update Layer table, update immutability rule
- **index.md**: Add/update section header with correct page count, add entries for all moved files
- **log.md**: Append operation log entry (don't modify historical entries)
- **SCHEMA.md**: Add any missing tags from moved files' frontmatter (pre-commit blocks on unknown tags)

### 7. Handle pre-commit tag taxonomy violations

Files in `raw/` may have tags that weren't previously validated. After moving to a tracked directory, the pre-commit hook checks them:

```bash
git commit -m "..." 2>&1 | grep "TAGS NOT IN SCHEMA"
```

Add missing tags to SCHEMA.md under the appropriate category:
- Person names → People/Orgs
- Architecture concepts → Models or Techniques
- Event names → Meta (e.g., `neurips-2024`)
- Domain concepts → Domain Concepts (e.g., `scaling-hypothesis`, `superintelligence`)

### 8. Stage only relevant files

```bash
cd ~/ai-topics
git reset HEAD
git add wiki/<target-dir>/ wiki/<source-dir>/ wiki/index.md wiki/log.md wiki/SCHEMA.md AGENTS.md
git add wiki/<all-files-with-updated-references>
git commit -m "wiki: move <description>" && git push
```

### 9. Verify cleanup

```bash
ls wiki/<source-dir>/ 2>/dev/null  # Should be empty/gone
grep -r 'old/path/prefix' --include='*.md' ~/wiki/  # Should find nothing
```

## Pitfalls

- **Don't update historical logs**: `log.md` and `log-2026-*.md` are append-only. Old entries referencing the old path are historical records — leave them.
- **Pre-commit blocks on unknown tags**: Files in `raw/` may have tags that weren't validated. After moving, the pre-commit hook checks them. Add missing tags to SCHEMA.md before committing.
- **Internal references in moved files**: Don't forget to check references *within* the moved files — e.g., a transcript referencing a companion VTT file or other transcripts by their old path.
- **Stage only changed files**: If other agents have pending changes in the repo, use explicit `git add` paths instead of `git add wiki/` to avoid staging unrelated changes.
- **index.md section headers**: Update the section header page count (e.g., `## Raw Transcripts (3 pages)` → `## Transcripts (13 pages)`).

## Real Examples

### Intra-raw move (2026-05)
Moved 5 Vanishing Gradients YouTube transcripts from `raw/articles/` to `raw/transcripts/`:
- 4 SUAYS episodes (Ep.1-4) + 1 standalone transcript (Ep.68)
- Updated 22 wiki pages
- Result: `28 files changed, 32 insertions(+), 32 deletions(-)`

### Top-level reorganization (2026-06-05)
Moved 13 YouTube transcripts from `raw/` to `wiki/transcripts/`:
- 11 from `raw/transcripts/` + 2 from `raw/articles/` (`type: transcript`)
- 20 files in `raw/articles/` with `source: YouTube` but `type: talk/podcast/panel` were **kept in place**
- Updated 35 external files + 2 internal references
- Added 9 missing tags to SCHEMA.md (pre-commit blocker)
- Updated AGENTS.md (directory tree, Layer 1 table, immutability rule)
- Expanded index.md section from 3 to 13 entries
- Result: `52 files changed, 413 insertions(+), 77 deletions(-)`
