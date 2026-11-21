# Log-prepend: dynamic entry-header scan (2026-11-10)

## Problem with the 2026-10-28 recipe

`blog-ingest-session-notes-2026-10-28.md` hardcodes the header block as `lines[:4]` and asserts `startswith("# Wiki Log\n\n_Log of all wiki changes")`. That assumed log.md opens with:

```
# Wiki Log
(blank)
_Log of all wiki changes. Newest entries at top._
(blank)
## [entry] ...
```

**Actual repo state (verified 2026-11-10):** the italic subtitle is NOT present. Line 2 is blank, line 3 is already `## [2026-11-09] ingest | x-accounts-scan: ...`. The hardcoded slice inserts the new entry in the wrong place, and the post-write `startswith(...)` assert aborts the script — had to `git checkout HEAD -- wiki/log.md` and retry.

## Robust replacement

Do NOT hardcode the header block size. Scan for the first `## [` or `## 2026-` line instead:

```python
log_path = "/opt/data/ai-topics/wiki/log.md"
with open(log_path) as f:
    c = f.read()
lines = c.split("\n")
assert lines[0] == "# Wiki Log", repr(lines[0])

insert_at = None
for i in range(1, min(20, len(lines))):
    if lines[i].startswith("## [") or lines[i].startswith("## 2026-"):
        insert_at = i
        break
assert insert_at is not None, "no prior entry found"

new_entry = """## [2026-11-10] ingest | blog-ingest (cron): <short title>

- bullet 1
- bullet 2

"""
out = "\n".join(lines[:insert_at]) + "\n" + new_entry + "\n".join(lines[insert_at:])
with open(log_path, "w") as f:
    f.write(out)

# Post-write assert only invariants that are ALWAYS true.
with open(log_path) as f:
    c2 = f.read()
assert c2.startswith("# Wiki Log\n")            # NOT the italic subtitle
assert "<unique-substring-of-new-entry>" in c2
```

If the assert fails, `git checkout HEAD -- wiki/log.md` before retrying — never edit in place after a partial write.

## Even simpler: patch-anchored prepend (validated 2026-11-11)

No python needed. Use the `patch` tool with `old_string` = `# Wiki Log\n\n` + the first line of the current top entry (`## [YYYY-MM-DD] ...`, copy verbatim from `head -4 wiki/log.md`), `new_string` = header + new entry + that same line. The tool's fuzzy matching handles whitespace. Post-check with `head -4` in the same commit command chain.

Notes:
- If patch returns a `_warning` that a sibling subagent modified log.md since you read it, that's usually your own earlier read being stale — `head -4` before committing to confirm your entry landed exactly once.
- Do NOT use `execute_code` in cron sessions — it's BLOCKED unless `approvals.cron_mode: approve`. Terminal + patch are the correct tools here.

## Entry-header convention

Use `## [YYYY-MM-DD] <stage> | <short title>`:
- Bracketed ISO date
- Stage keyword (`ingest`, `dreaming`, `hot-post`, `skeleton-enrich-daily`, ...) matching sibling entries in the same file
- Pipe separator `|`
- Short descriptive title

This matches x-accounts-scan / dreaming / skeleton-enrich-daily entries already in the log, so `grep "^## \["` finds every entry regardless of stage.

## Sweeping sibling backlog

`git add wiki/raw/articles/` sweeps untracked raw files from OTHER pipelines (newsletter-ingest, x-bookmarks-ingest, etc.) whose earlier runs didn't commit. That's desirable — commit them together, but call it out in the log entry so the commit size (`+N files, +M lines`) doesn't look like a bug. Typical split this run: 20 blog-ingest + 9 sibling backlog files.

## Checkpoint sanity gate (unchanged from 2026-10-28)

`scan.total_new` counts ALL new DB articles; `articles.total` is the per-run fetch-cap subset. `blogs_scanned=0` with nonzero `total_new` is the known cosmetic stdout-parse bug — verify via direct DB query:

```sql
SELECT b.name, COUNT(*) c FROM articles a JOIN blogs b ON a.blog_id=b.id
WHERE DATE(a.discovered_date)='<run date>' GROUP BY b.name ORDER BY c DESC;
```

If DB sum matches `total_new`, do NOT re-scan.
