# Archive verification without pipe-to-interpreter (2026-08-10)

Validated during blog-triage run 20260810T102241Z. Two reusable lessons for the archive step (§8 of SKILL.md).

## 1. `python3 | python3` pipe is blocked — verify via stdout + file, not a pipe

**Attempt that failed** (blocked by `tirith:pipe_to_interpreter`, `pattern_key: tirith:pipe_to_interpreter`):

```bash
python3 scripts/archive_triage.py blog --keep-reference 2>&1 | python3 -c "import sys,json; d=json.load(sys.stdin); print(...)"
```

The skill previously documented pipe blocking for `cat file | python3 -c` (Triage JSON Verification) and `curl | python3 -c` (HTML Fallback), but NOT for parsing the archive script's own stdout. Same scanner, same rule: **no command whose stdout feeds an interpreter**.

**Working pattern**:
1. Run `python3 scripts/archive_triage.py blog --keep-reference` alone. The JSON it prints to stdout IS the archive-run verification (it contains `ok`, `candidates`, `new_archived`, `dedup_skipped`, `archive_path`, `total_archive_urls`).
2. Verify the FILE separately with a hardcoded path — no pipe, no shell expansion:

```bash
python3 -c "import json; d=json.load(open('wiki/raw/archived/triage/blog/2026-08-10_20260810T102241Z.json')); print(len(d['decisions']))"
```

Do not re-run the archive script just to verify it — run once, read stdout, then read the file.

## 2. Archive run touches TWO tracked files — one targeted commit for both

After `archive_triage.py --keep-reference`, `git status --short wiki/raw/archived/` shows:

```
M wiki/raw/archived/triage/archive_index.json
?? wiki/raw/archived/triage/blog/2026-08-10_20260810T102241Z.json
```

The dated JSON is new; `archive_index.json` is the URL-dedup index and gets modified on every run. `git add` BOTH in one commit:

```bash
git add wiki/raw/archived/triage/blog/2026-08-10_<runid>.json wiki/raw/archived/triage/archive_index.json
git commit -m "wiki: blog-triage archive + index (YYYY-MM-DD)"
git push
```

Forgetting the index file costs a second commit + push (observed 2026-08-10: two commits `0fd76c41` then `9fac6884` where one would have sufficed).

## Context notes from the run

- 20 decisions (3 takes / 4 references / 13 skips incl. 3 unsaved) written to `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` via `/tmp/blog_triage_20260810.py` (write_file → terminal python3, cron-mode default per Output Structure §Option B).
- Field-completeness check passed for all 20 (every decision had `body_excerpt` + `reason_ja`).
- Yield pattern: 3 takes / 17 resolved candidates ≈ 18% — consistent with the heterogeneous-batch higher-yield note (Aug 2026 batches ~22% 4/18). Mixed composition (4× Simon Willison, 4× shkspr Fringe, 2× johndcook, 2× idiallo, + seangoedecke/tedium/pluralistic/jim-nielsen/oldvcr) drove the yield; do not force extra takes on homogeneous opinion-blog batches.
