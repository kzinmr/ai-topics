# Batch Directory Reorganization Pitfalls

Real-world lessons from reorganizing `concepts/fine-tuning/` → `concepts/post-training/` (47 files, ~100 cross-reference updates, 2026-06-12).

## Pitfall 1: Symlink + git add Trap

When wiki files are modified through the `~/wiki` symlink (which resolves to `~/ai-topics/wiki`), `git add wiki/` from the repo root may not stage all changes. Git sometimes tracks the real path vs the symlink path differently.

**Symptom**: `git show --stat HEAD` shows fewer files than expected (e.g., 2 instead of 100+).

**Fix**:
```bash
cd ~/ai-topics
git status --short wiki/  # Check what git sees
# If changes are missing:
git add -A wiki/           # Force-add all changes
# Or stage explicitly:
git add wiki/concepts/post-training/ wiki/concepts/fine-tuning.md wiki/index.md
```

**Verification**: Always check `git show --stat HEAD` after committing to confirm the expected file count.

## Pitfall 2: Double-Nesting in Bulk sed

When building sed expressions for bulk reference updates, if the replacement string contains the search pattern, you get double-nesting.

**Example**: Moving `concepts/post-training.md` to `concepts/post-training/post-training.md` while also replacing `concepts/post-training` → `concepts/post-training/post-training` in references creates `concepts/post-training/post-training/post-training`.

**Root cause**: The moved pages list includes `post-training`, and the sed expression `s|concepts/post-training|concepts/post-training/post-training|g` matches its own output.

**Fix**:
1. After bulk sed, immediately run: `grep -rli "double-pattern/" wiki/concepts/ wiki/entities/`
2. If found, run a cleanup sed: `s|concepts/post-training/post-training/|concepts/post-training/|g`
3. Better approach: exclude the directory prefix page from the sed replacement list, or use word-boundary matching

## Pitfall 3: Pre-Commit Tag Validation

The pre-commit hook validates tags against `SCHEMA.md` taxonomy. Unknown tags block the commit.

**Common misses**: `exploration`, `interview`, `llm-training`, `llm-infrastructure`, `load-balancing`, `rl` (should be `reinforcement-learning`).

**Fix workflow**:
1. Before committing, check tags: `grep "tags:" wiki/concepts/new-page.md`
2. Verify each tag exists: `grep -o "tagname" wiki/SCHEMA.md`
3. If missing: either add to SCHEMA.md or replace with existing canonical tag
4. Emergency override: `git commit --no-verify` (not recommended)

## Pitfall 4: Pre-Commit Language Enforcement

Non-raw wiki pages must be in English. Japanese content in `concepts/`, `entities/`, `comparisons/` blocks the commit.

**Fix**: Translate all Japanese content to English before committing. The hook checks new files and modified files.

## Pitfall 5: Reference Update Scope Estimation

For a directory with N pages, expect ~2-3x N files to need reference updates (pages referencing the moved pages).

**Efficient approach**:
```bash
# 1. Build the sed expression for all moved pages
PAGES="page1 page2 page3 ..."
SED_EXPR=""
for p in $PAGES; do
  SED_EXPR="${SED_EXPR}s|concepts/${p}]]|concepts/post-training/${p}]]|g;"
done

# 2. Find all files that reference ANY moved page
find wiki/concepts/ wiki/entities/ wiki/comparisons/ -name '*.md' \
  -exec grep -l 'concepts/page1\|concepts/page2\|concepts/page3' {} \; | \
  while read f; do sed -i "$SED_EXPR" "$f"; done

# 3. Also update index.md separately
sed -i "$SED_EXPR" wiki/index.md
```

**Key**: Use `find ... -exec grep -l` to identify affected files FIRST, then apply sed. Don't try to grep + sed in one pass per page (too slow for 40+ pages).

## Pitfall 6: index.md Not Updated by Subagents

`delegate_task` subagents may create pages and add entries to index.md, but if the parent session also modifies index.md, the subagent's changes may be lost (or create conflicts).

**Fix**: After all subagents complete, verify index.md has all expected entries. Add missing entries yourself before committing.

## Checklist for Batch Directory Reorganization

1. [ ] Create target directory
2. [ ] Move files (shell `mv` or `git mv`)
3. [ ] Create/update `_index.md` in target directory
4. [ ] Create redirect page at old location (if user-facing)
5. [ ] Build sed expression for all moved pages
6. [ ] Find + update all referencing files (~2-3x moved page count)
7. [ ] Update index.md (separate sed pass)
8. [ ] Verify no double-nesting: `grep -rli "double-pattern"`
9. [ ] Verify no remaining old refs: `grep -rli "old-path]]"`
10. [ ] Verify tags in SCHEMA.md taxonomy
11. [ ] Verify no Japanese in non-raw pages
12. [ ] `git add -A wiki/` (not just `git add wiki/`)
13. [ ] `git show --stat HEAD` — verify file count matches expectation
14. [ ] Update log.md
15. [ ] Push
