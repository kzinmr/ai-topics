# Log Header Burial — Re-confirmed 2026-09-14 (NOT a false positive)

**Symptom**: `wiki_health.py --json` reports `frontmatter_syntax` issue on `wiki/log.md`: "File does not start with --- or # ".

**Truth**: This is a REAL issue, not an "append-only format" false positive. The canonical `wiki/log.md` starts with:

```
# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete, watchdog
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.
```

A prepend that writes `new_entry + content` after a previous strip leaves the file starting directly with the newest `## [YYYY-MM-DD]` entry — header block gone.

**Prior wrong reasoning to avoid**: dismissing it as "log.md is append-only and starts with `## [` entries — expected" or "425 entries < 500 so no rotation needed" (rotation threshold is unrelated to this check).

**Fix**: `python3 ~/ai-topics/scripts/fix_log_header_burial.py --dry-run` then without `--dry-run` (only if action needed). Script is idempotent (refuses when header present), verifies exactly one `# Wiki Log` after write, and separately reports when file starts with `---` (frontmatter corruption — needs manual inspection).

**Session 2026-09-14 (watchdog)**: header was buried (diff showed exactly the 6 header lines missing). Restored (commit ba8e84d1), logged, pushed (07d9029d). The nightly wiki-health-fix job (17:50, after watchdog at 17:35) never fixed it across multiple prior runs — do not rely on upstream repair for this issue.
