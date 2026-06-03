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
- **Batch regression 7b69b67d** (2026-06-03): 15 entity pages overwritten simultaneously during "Show Us Your Agent Skills" article ingestion. Pages like chip-huyen (234→31), andrej-karpathy (544→118), steve-blank (200→90) lost 60-87% of content.
- **Batch regression 383eff68** (2026-06-03): 14 pages regressed during "comprehensive health remediation" commit. Pages like jason-liu (494→80), drew-breunig (345→79), eugene-yan (345→106) severely damaged.

## Git History Enrichment: The Correct Recovery Pattern

When enriching a skeleton or damaged page, **always check git history for a richer historical version first**. The enrichment process should be:

### Step 1: Check if a richer version exists in git history
```bash
# Find all commits that touched this file
git log --oneline -- 'wiki/entities/<slug>.md'

# Find the richest historical version (max lines)
for commit in $(git log --format=%H -- 'wiki/entities/<slug>.md'); do
    lines=$(git show "$commit:wiki/entities/<slug>.md" 2>/dev/null | wc -l)
    echo "$commit $lines lines"
done | sort -rn -k2 | head -3
```

### Step 2: Restore the richest version as the base
```bash
# Restore from the richest commit
git show <RICHEST_COMMIT>:wiki/entities/<slug>.md > wiki/entities/<slug>.md
```

### Step 3: Merge any genuinely new content from later enrichments
```bash
# Compare sections between restored version and current enrichment
grep "^##" wiki/entities/<slug>.md  # restored sections
git show HEAD:wiki/entities/<slug>.md | grep "^##"  # enrichment sections
# Add any new sections from enrichment that aren't in the restored version
```

### Step 4: Enrich on top of the restored base
Use `patch` to add new information from the current article to the restored content.

### Why This Matters
Enrichment jobs that start from scratch produce pages that are:
- Missing curated content that took hours to assemble
- Lacking cross-references that were carefully built up
- Missing nuanced analysis that can't be recreated from a single web search

The richest historical version IS the curated baseline. New articles should ADD to it, not replace it.

## Defense-in-Depth: Pre-Commit Content Regression Hook

Even with the pre-write checklist above, cron pipeline agents (raw-backlog-ingest, x-bookmarks-ingest, newsletter-wiki-ingest) have repeatedly overwritten rich pages with skeletons. The repo now has an **automated pre-commit hook** that catches this at commit time:

**Hook**: `.githooks/pre-commit-content-regression.py`
**Trigger**: Any staged change to `wiki/entities/` or `wiki/concepts/` that shrinks a page by >50 lines AND >50% of the original.
**Behavior**: Blocks the commit with a detailed error showing old/new line counts.

```
🚫 CONTENT REGRESSION DETECTED — rich wiki pages would be overwritten!
   📄 wiki/entities/thariq-shihipar.md
      173 → 36 lines  (−137 lines, 21% of original)
```

**Thresholds** (tunable in the script):
- `MIN_LINES_BEFORE = 40` — only protects pages that are already substantial
- `SHRINK_RATIO = 0.5` — blocks if new < old × 0.5
- `ABSOLUTE_LINE_DROP = 50` — blocks if more than 50 lines removed

**Bypass**: `git commit --no-verify` (emergencies only)

**Why this matters for you (the agent)**: The hook is a safety net, NOT a license to be careless. Always follow the pre-write checklist above. If the hook blocks your commit, you likely overwrote a rich page — stop, read the existing content with `git show HEAD:<path>`, and merge your changes with `patch` instead.

**Implementation**: `.githooks/pre-commit-content-regression.py` (Python3, no external deps). Added to `.githooks/pre-commit` as the third check after index validation and tag validation. See `wiki-ingestion-pipelines` skill's General Pipeline Pitfalls for the complementary pitfall entry.

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
