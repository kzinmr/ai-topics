# Dreaming-Group Quickrun — all-skip Pattern E variant (validated 2026-11-21)

Clean 8-call run of the 18:10 dreaming-GROUP cron job when the checkpoint has `total_articles: 0` and the prior day's triage was already consumed. No wiki content edits, no delegation — pure triage + archive + log + commit. Produced commit `79be01b2`, hooks green, zero round-trips.

## Call sequence

1. **State probe (one terminal call)**: `git log --oneline -15` + `grep "$(date +%F)" wiki/log.md | head -20` + `ls /opt/data/.hermes/cron/data/dreaming/`. Confirms what today's sibling jobs (trending-topics, newsletter-wiki-ingest, blog-ingest) already committed — these become explicit skip reasons with commit SHAs in `reason_ja`.
2. **Prior-triage consumption check**: read `triage_latest.json` via `python3 -c "import json; d=json.load(open(...))"` (no pipe). If its `checkpoint_run_id` is YESTERDAY's and `git log` shows a `dreaming: group triage <yesterday>` / downstream ingest commit after it, the prior triage is consumed — its takes become `dreaming-batch-prior-takes` skips (verify the take pages exist on disk with `find`).
3. **Recent-raw listing**: `ls -lt wiki/raw/articles/ | head -40`. The 06:00 sitemap batch + 10:00 blog batch are the untriaged pool.
4. **Never-archived probe (decisive)**: extract `url:` OR `source:` from each candidate's frontmatter — **sitemap raws use `source:`, blog-domain raws use `url:`, and some company-blog raws have `source: "Cartesia Blog"` (a name, not a URL)**. Membership-test normalized URLs against the umbrella `wiki/raw/archived/triage/archive_index.json` `{"urls":[...]}` list in one `python3 -c`. All-absent = never triaged → real Pattern-E material.
5. **Coverage grep**: `grep -il "<topic>" wiki/concepts/*.md wiki/entities/*.md` for each surviving cluster to split already-covered-skip vs reference.
6. **Builder via write_file → terminal** (cron mode, CJK reasons): `/tmp/dreaming_group_<date>.py` with a `make(item_id, title, url, raw, action, stars, reason, cpath, excerpt)` helper — star count as INT (`"*" * stars`), no `None`, no ASCII quotes inside Japanese literals, no `'''` bodies. Gate with `python3 -c "import ast;ast.parse(...)"` before running. Save to `/opt/data/.hermes/cron/data/dreaming/triage_latest.json` with hardcoded path (never `expanduser`).
7. **Archive + log + commit (3 calls)**:
   - `python3 scripts/archive_triage.py dreaming --keep-reference` — expect most-newly-archived on a fresh batch (this run: 20 candidates, 18 new, 2 dedup, index 3310→3325).
   - `write_file` the log entry to `/tmp/dreaming_log_entry_<date>_<hhmm>.md` (starts with `## [`, Unicode-safe), then `python3 config/hermes/skills/_custom/dreaming/scripts/repair_log_md_header.py wiki/log.md <entry>` — the DEFAULT log action (handles buried-header state; do not hand-roll a prepend). Verify `head -8` + `grep -c "^# Wiki Log"` == 1.
   - Selective staging ONLY: `git add wiki/log.md wiki/raw/archived/triage/dreaming/<date>_<runid>.json wiki/raw/archived/triage/archive_index.json` → `git commit -m "dreaming: group triage ..."` → `git push`. Sibling-dirty tree (skills/, AGENTS.md) never staged. Plain push worked; no pull --rebase needed.

## Decision-composition notes that paid off

- 20 decisions total: 5 references, 15 skips — batched marketing (Cartesia ×10) and non-AI rolling (9 sources) each into ONE batch-skip entry with `|`-joined excerpt.
- Same-event multi-source (Guardian + Gary Marcus + Zitron on one selloff) = one cluster, all skips with the covering commit SHAs cited in `reason_ja`.
- RSS-fallback stubs (~600-700B, `openai.com--*`) whose topic was already taken by blog-ingest today → skip citing the ingest commit, not reference.
- References got real `candidate_wiki_path` + 4-star reasons phrased as verification instructions for downstream ("verify paper-specific method details landed") — the group job decides targets but does not edit pages.
- A prior-day article that trending-topics covered SAME-DAY (weight self-rewriting arXiv) stays a reference: page exists, but the raw paper was never archived and body-level capture is unverified — the Deep Sleep gate downstream re-checks.

## Report shape

English report was fine for Discord delivery here; sections: Duplicate Check Summary → Theme Clusters → never-triaged verification (URL-absence counts) → Actions taken → `COST_REPORT:` line.
