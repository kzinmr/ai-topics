# Stale blog-triage JSON → premature archive run

`scripts/archive_triage.py blog` reads whatever `triage_latest.json` currently holds, with no
freshness check. If you run it BEFORE building today's triage JSON, it archives the PREVIOUS
day's checkpoint items and names the output file after the STALE run id:

```
# observed 2026-11-15
python3 scripts/archive_triage.py blog --keep-reference
{"blog": {"candidates": 10, "new_archived": 1, "dedup_skipped": 9,
          "archive_path": ".../triage/blog/2026-11-15_20261113T100036Z.json", ...}}
```

The `20261113T100036Z` in the filename is yesterday's run id leaking into a today-dated file.
Harmless (dedup absorbs it) but misleading, and it commits a junk archive file.

## Rule

1. Build and save today's triage JSON FIRST (`triage_timestamp` + `checkpoint_run_id` = current run).
2. Only THEN run `archive_triage.py {pipeline} --keep-reference`.
   Correct output: one file named `YYYY-MM-DD_{current_run_id}.json`,
   `new_archived` == skip+reference count, `dedup_skipped` == 0.
3. Before trusting `triage_latest.json` as evidence that a batch was already triaged, compare its
   `checkpoint_run_id` with the current run id (Priority list item 0 in SKILL.md). Different => the
   batch is FRESH and must be triaged, even if a same-day
   `wiki: daily RSS scan 2026-11-15 (17 articles saved)` commit exists — that commit is raw SAVING
   only, never triage consumption. Verify with `git show --stat <sha>` when in doubt.

## Also blocked in cron mode

- `python3 scripts/archive_triage.py ... | python3 -c "..."` → `tirith:pipe_to_interpreter`.
  Redirect to a file instead: `... > /tmp/archive_out.json 2>&1; tail -c 600 /tmp/archive_out.json`.
