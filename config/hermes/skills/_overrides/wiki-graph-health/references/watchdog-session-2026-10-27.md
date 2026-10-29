# Watchdog session — 2026-10-27 (wiki-health-fix cron, clean pass)

## Verdict
Full clean pass. No auto-fixes applied; only log.md entry committed (`0b8cd019`).

## Digest orphan list = false positive (redirect stubs)
Digest reported 3 orphans: `entities/eugeneyan`, `entities/giles-thomas`, `entities/lilianweng`.
All three were **intentional `status: redirect` stubs** (~225–242 B) created the previous day by
watchdog dedup commit `fa32e7a4` — content merged into canonical `eugene-yan` / `gilesthomas` /
`lilian-weng` (18–28 KB each, all already in index.md).

**Recipe for any digest orphan**:
1. `head -15 wiki/entities/<slug>.md` — if `status: redirect` + `redirect:` field → likely intentional.
2. `git log --oneline -1 -- wiki/entities/<slug>.md` — if the latest commit message says dedup/redirect
   conversion, the removal from index.md was deliberate.
3. Verify canonical (`redirect:` target) IS indexed: `grep -c '[[entities/<canonical>]]' wiki/index.md`.
4. Do NOT add the stub to index.md. Report as false positive in the health report + log.md.

Root cause: `wiki_health.py`'s orphan scan compares filesystem slugs against index.md wikilinks and
has no `status: redirect` filter. Same class as the known "redirect stubs indexed twice" dedup
false positive (A4b, 2026-08-19) — the scanner treats redirect stubs as regular pages in BOTH
directions (counts them as duplicates when indexed, as orphans when not).

## Verified-clean baseline (use as healthy baseline, 2026-10-27)
- index.md: 3,352 lines; pipe_prefix/line_number/triple_bracket/space_prefix/double_pipe all 0;
  `validate_index.py` exit 0.
- Header counts matched filesystem: Entities 955 / Concepts 2246 / Comparisons 35
  (digest's 957/2251/35 counts subdirectory files too — small deltas vs header are normal).
- `tag_audit.py` (run with `/opt/data/.hermes/venv/bin/python`): 0 non-SCHEMA, 0 composite,
  926 unique tags, coverage 108.9%.
- ~20 dirty/untracked wiki files from sibling pipelines (newsletter ingest WIP) — leave uncommitted.

## log.md prepend gotcha re-encountered
Prepending via `content.split('\n')` + rejoin can leave the new entry ABOVE the `# Wiki Log` H1 if the
file has no frontmatter and you naively do `new_entry + content`. Post-write check mandatory:
`head -6 wiki/log.md` must start with `# Wiki Log`, `grep -c '^# Wiki Log'` = 1, and the italic
`_Log of all wiki changes...` subtitle appears exactly once. Fix pattern: locate
`lines.index('# Wiki Log')`, move the entry block after header + subtitle + blank, dedupe any
duplicated subtitle line. (Same header-burial class the watchdog repaired at 17:35 UTC the same day
via `fix_log_header_burial.py` — worth re-checking that script handles the no-frontmatter prepend case.)
