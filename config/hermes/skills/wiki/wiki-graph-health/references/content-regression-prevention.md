# Content Regression Prevention — Cross-Cutting Concern

This reference applies to ALL wiki modification operations: enrichment, health remediation, ingestion pipelines, and manual edits.

## The Problem

Batch wiki operations (health remediation, article ingestion, enrichment) have repeatedly overwritten rich curated pages with skeletons or stubs. **58 documented regression events** across 9 destructive commits:

| Commit | Pages | Context |
|--------|-------|---------|
| `7b69b67d` | 15 | "Show Us Your Agent Skills" article ingestion |
| `383eff68` | 14 | "comprehensive health remediation" |
| `284a567c` | 3 | "Prime Intellect people" addition |
| `34932bb2` | 4 | "Cognition/Devin Philosophy" section |
| `8dea159` | 1 | Thariq Shihipar (triggered this investigation) |

## Prevention Stack (3 layers)

### Layer 1: Pre-write verification (agent-level)
Before ANY `write_file` to `wiki/entities/` or `wiki/concepts/`:
1. `read_file` the existing page
2. If >40 lines → use `patch`, NOT `write_file`
3. Check `git log` for richer historical versions

### Layer 2: Pre-commit hook (commit-level)
`.githooks/pre-commit-content-regression.py` blocks commits that shrink entity/concept pages by >50 lines AND >50%.

### Layer 3: Cron prompt enforcement (pipeline-level)
All ingestion cron jobs must include anti-overwrite warnings in their prompt preamble.

## Recovery: Git History Enrichment Pattern

When a page has been damaged:

```bash
# Step 1: Find the richest historical version
for commit in $(git log --format=%H -- 'wiki/entities/<slug>.md' | head -10); do
    lines=$(git show "$commit:wiki/entities/<slug>.md" 2>/dev/null | wc -l)
    echo "$commit $lines lines"
done | sort -rn -k2 | head -3

# Step 2: Restore the richest version
git show <RICHEST_COMMIT>:wiki/entities/<slug>.md > wiki/entities/<slug>.md

# Step 3: Check for genuinely new sections in the damaged version
# (compare section headers between restored and damaged versions)

# Step 4: Merge new sections into restored base, then enrich with patch
```

## Scanning Script

`references/content-regression-scanner.sh` — scans all commits for regression events:
```bash
bash references/content-regression-scanner.sh
```
Output format: `REGRESSION|path|old_lines|new_lines|drop|ratio%|commit_message`
