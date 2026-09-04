# Wiki Directory Reorganization (Mass Page Moves)

When restructuring wiki pages into subdirectories (e.g., `concepts/gpt-models.md` → `concepts/gpt/index.md`), this workflow handles git moves, wikilink updates, and deduplication.

## Workflow

### 1. Plan Moves

Define the complete mapping before executing:

```python
MOVES = [
    ("wiki/concepts/old-name.md", "wiki/concepts/subdir/new-name.md"),
    # ...
]
# Also define entity→concept merges (when an entity page should be absorbed)
ENTITY_MERGES = {
    "wiki/entities/old-entity.md": "wiki/concepts/subdir/target.md",
}
```

### 2. Execute git mv

```bash
for old, new in MOVES; do
    git mv "$old" "$new"
done
```

### 3. Build and Apply Wikilink Replacements

Scan ALL .md files in wiki/ (excluding raw/, transcripts/, _archive/) and replace old paths with new:

```python
# Build replacement pairs from the move mapping
for old_path, new_path in MOVES:
    old_no_ext = old_path.replace("wiki/", "").replace(".md", "")
    new_no_ext = new_path.replace("wiki/", "").replace(".md", "")
    # Replace [[old_no_ext → [[new_no_ext
    # Also handle sources: old_no_ext.md → new_no_ext.md
```

Apply with string replacement across all .md files. Report per-file replacement counts.

### 4. Handle Entity Merges

When an entity page is being merged into a concept page:
- Append entity body content to the target concept page (skip frontmatter)
- Add a separator note: `*Merged from entities/X.md*`
- `git rm` the entity file
- Change frontmatter `type: entity` → `type: concept` in the target

### 5. Remove Duplicate Index Entries

After moves, index.md may have entries at both old and new alphabetical positions. Scan for duplicates and remove the less-descriptive one.

### 6. Commit

Stage only the reorganization files (avoid including unrelated changes from sibling subagents):

```bash
git add wiki/concepts/subdir/ wiki/index.md wiki/log.md
git add wiki/concepts/modified-page1.md wiki/concepts/modified-page2.md  # link-updated files
git commit -m "wiki: reorganize X pages into concepts/subdir/"
```

## Pitfalls

- **git reset after git mv**: If `git reset HEAD` is called after git mv, the index changes are unstaged but files remain moved on disk. Re-stage with `git add wiki/concepts/subdir/` — git will detect the renames.
- **SCHEMA.md tag persistence**: Tags added to SCHEMA.md can be overwritten by concurrent sibling subagent operations. Always verify tags exist before committing: `grep "tag-name" wiki/SCHEMA.md`.
- **Pre-commit hook — Japanese content**: The hook blocks commits with CJK characters in non-raw/ files. If SCHEMA.md examples contain Japanese (as bad-name examples), translate them to English before committing.
- **Pre-commit hook — tag violations**: New pages must use tags from SCHEMA.md. Add new tags to SCHEMA.md first, then stage SCHEMA.md before committing.
- **Stale index entries**: After mass moves, manually verify index.md doesn't have entries pointing to old paths. The wikilink replacement handles content links but index entries need separate verification.
- **Platform vs model split**: When separating platform/API pages from model pages into different directories (e.g., gpt/ vs openai/), remove redundant prefixes from the destination (e.g., `gpt-responses-api.md` in openai/ becomes `responses-api.md`).
