# Wiki Page Creation Pitfalls (Blog/Newsletter Ingest)

Captured from real cron session failures during wiki page creation and commit.

## 1. Tag Taxonomy Violations Block Commit

The pre-commit hook validates all tags against `SCHEMA.md` (855+ canonical tags). Common non-obvious violations encountered:

| Invalid Tag | Valid Substitute | Notes |
|---|---|---|
| `ml-infrastructure` | `infrastructure` | SCHEMA has no `ml-` prefix variants |
| `distributed-computing` | `distributed-systems` | SCHEMA uses `distributed-systems` |
| `data-scientist` | `blogger` or `developer` | No occupation tags in taxonomy |
| `subscription-economics` | `ai-economics` | Use the broader economic tag |
| `parallel-computing` | (omit) | No equivalent; use `distributed-systems` if relevant |

**Fix workflow:**
1. `git commit` → hook prints violation list with file paths and invalid tags
2. Edit each file to fix tags (use `patch` tool)
3. `git add` files → commit again

The hook tells you exactly which files and tags violated, so don't guess — read the error output.

## 2. Duplicate Frontmatter Keys Cause Patch Failures

Some entity pages (e.g., `simon-willison.md`) have duplicate `sources:` lines in YAML frontmatter — one nested under `status:` block and one at root level. The `patch()` tool finds multiple matches and returns "Found N matches" error.

**Fix:** Include more surrounding context in `old_string` to disambiguate. Use the line above/below to make the match unique. For example, include the `tags:` line that follows the `sources:` line.

## 3. `execute_code` Blocked for Cron Jobs

Cron sessions cannot use `execute_code` (blocked by approval policy when no user is present). Use `terminal()` and `patch()` directly for all wiki writes. Multi-step logic must be done as sequential tool calls, not a Python script.

## 4. Index Header Counts Must Be Updated Manually

After adding entity/concept pages, update the `## Entities (N pages)` and `## Concepts (N pages)` headers in `index.md`. The pre-commit hook validates that `index.md` is clean but does NOT auto-update counts. Forgetting this causes the watchdog auto-fix to correct it later, but it's cleaner to do it inline.

## 5. Raw Articles Are Pre-Staged by blog_ingest.py

The blog ingest script (`blog_ingest.py`) already stages raw articles in the git index before the agent runs. Do NOT re-add them — just add the wiki pages you create and the existing `index.md`/`log.md` updates. Check `git status` to see what's already staged.
