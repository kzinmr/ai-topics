# Pre-Write Verification Protocol

## CRITICAL: Never Overwrite Existing Wiki Pages

The user maintains **100-200+ line comprehensive entity pages** representing hours of curation. Using `write_file` on an existing page irreversibly destroys this work.

### Mandatory Pre-Creation Checklist

Before ANY `write_file` to `wiki/entities/` or `wiki/concepts/`:

```bash
# 1. search_files for the expected slug
search_files(path="/opt/data/wiki/entities", pattern="<slug>")
search_files(path="/opt/data/wiki/concepts", pattern="<slug>")

# 2. Also check index.md for entries under different filenames
grep -i "<topic>" /opt/data/wiki/index.md

# 3. Check for partial name matches (will-brown vs william-brown)
search_files(path="/opt/data/wiki/entities", pattern="<partial-slug>")
```

### Decision Tree

| Finding | Action |
|---------|--------|
| No existing page | `write_file` is SAFE |
| Existing entity page | Use `patch` for targeted updates ONLY |
| Existing concept page (wrong type) | Consider merging into entity, then delete concept |
| `status: skeleton` stub | Enrich with `patch`, don't replace |
| Page under different filename | Use the EXISTING filename, add aliases |

### Recovery from Accidental Overwrite

If you overwrote an existing page:

```bash
# Find the last commit before your change
git log --oneline -3
# Restore from git
git show <PREVIOUS_COMMIT>:wiki/entities/<file>.md > /tmp/orig.md
# Read it to understand what was lost, then rewrite with content merged
```

### Real Failure Cases (2026-05-13)

- **Will Brown**: 203-line comprehensive page overwritten with 70-line stub. Had to `git show dd724453:wiki/entities/will-brown.md` to restore.
- **Florian Brand**: 183-line page overwritten with 43-line stub. Same recovery needed.
- **Elie Bakouch**: 140-line page overwritten with 45-line stub. Same recovery.
- **Grad**: Created `entities/grad62304977.md` (33 lines) when `entities/grad.md` (200 lines) already existed. Had to delete duplicate and cross-reference the existing page.
- **Thariq Shihipar** (2026-06-03): 282-line comprehensive page overwritten with 36-line skeleton by raw-backlog-ingest pipeline processing his dynamic-workflows article. Enrichment job restored to 173 lines, but ~109 lines of curated content (writing philosophy, blog table, Lenny's Podcast appearance, graph structure) were lost. Recovery needed only from git history (commit before 8dea159).

## SCHEMA Tag Validation (Pre-Commit Gate)

> **⚠️ CRITICAL**: The repo's pre-commit hook (`pre-commit-tag-validator.py`) blocks commits where ANY tag in ANY staged page is missing from `wiki/SCHEMA.md` taxonomy. This validates ALL staged files, not just yours.

### Before Writing Page Tags

```bash
# 1. Read SCHEMA.md tag taxonomy to know what's valid
# Check the tag categories in wiki/SCHEMA.md lines 31-40

# 2. For each tag you plan to use, verify it appears in SCHEMA.md
# If a tag is missing, either:
#   a) Find an existing canonical tag that covers the same concept
#   b) Add the new tag to the appropriate category in SCHEMA.md
```

### Common Tag Pitfalls

| Problem | Example | Fix |
|---------|---------|-----|
| Technology-specific tag not in schema | `sqlite`, `postgres`, `redis` | Add to Infrastructure category |
| Product-specific tag not in schema | `datasette`, `notion` | Add to Products category |
| Pattern/paradigm tag not in schema | `plugins`, `middleware` | Add to Engineering category |
| Pre-existing violations in staged files | Other people's pages also fail | Fix ALL violations, not just yours |

### Recovery from Tag Violations

When the pre-commit hook blocks you:
1. Read the error output — it lists every violating tag and file
2. For your own pages: either use existing canonical tags or add new ones to SCHEMA.md
3. For pre-existing violations in other staged files: **you must fix these too** — add their missing tags to SCHEMA.md
4. The hook validates the ENTIRE staging area, not just your changes
5. `git commit --no-verify` exists but should only be used in true emergencies

### Real Failure Case (2026-05-22)

Blog-ingest pipeline created 3 new pages with tags `sqlite`, `datasette`, `plugins`. Pre-commit hook blocked the commit. Additionally, pre-existing staged files (aaron-levie.md, box-com.md, context-engineering.md) had violations for `enterprise-agents`, `agent-identity`, `agent-governance`, `ceo`, `enterprise-saas`, `file-storage`, `cloud-infrastructure`. Required adding 10+ tags to SCHEMA.md across 5 taxonomy categories before commit succeeded.
