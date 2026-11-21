# Dreaming-GROUP stage (18:10 cron): triage-only, no content edits — validated 2026-11-19

## Scope rule

The `dreaming-group` job (the one that receives the pre-run checkpoint JSON injected into its prompt) is **triage-only**:

1. Build/overwrite `triage_latest.json` at `${HERMES_HOME}/cron/data/dreaming/triage_latest.json`
2. Run `python3 scripts/archive_triage.py dreaming --keep-reference`
3. Prepend a `## [YYYY-MM-DD] dreaming group | ...` log entry
4. Commit + push (staged: `wiki/log.md` + dated archive JSON + `archive_index.json` only)
5. Deliver the report

It does **NOT** create or enrich entity/concept pages. That is downstream `dreaming-wiki-ingest` (18:20), which independently runs the Deep Sleep verification gate on every take. The group stage's `candidate_wiki_path` values are **proposals** for downstream — `find`-verify them before assigning, but never touch the page files yourself. A group run that edits `wiki/entities/` or `wiki/concepts/` has crossed its lane and risks duplicating the downstream enrichment.

## Clean-run recipe (2026-11-19, commit daa0d249, both hooks green first try)

Checkpoint state that triggered Pattern E: `total_articles: 0`, `recent_raw_articles: 280`, `articles: []` — the classic saturation shape. The cron-injected script output was trusted for shape but the on-disk probe was the triage input.

### Steps

1. **State probe** (one batch of terminal calls):
   - `git log --oneline -8` + `grep "$(date +%F)" wiki/log.md | head -20` — same-day sibling saturation check (this run: trending-topics `a8b6462f` Gemini 4 Neon / NGINX RCE / MAI Ignite, active-crawl `3c3a674e` EBR / FrontierHarness / LLM-assisted RE / TrnRT — all excluded from triage).
   - `ls -la ${HERMES_HOME}/cron/data/dreaming/` — `triage_latest.json` mtime; `grep -i dreaming wiki/log.md | head -5` — confirm prior triage consumed (11-17 entry existed → safe overwrite).
   - `python3 config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py` — decisive never-archived list (this run: 134 recent, 3,279 indexed URLs). This is the ground-truth untriaged pool per the 2026-08-27 rule.

2. **Coverage sweep in ONE batched grep loop** over candidate keywords against `concepts/ entities/` (18 keywords in one terminal call), plus `head -c 500` on ~10 top raw files to satisfy the BODY-READING MANDATE. Cheap pre-filter that separates takes (zero coverage) from references (page exists, verify specific claims) from batch-skips (marketing/non-AI/opinion).

3. **Build triage JSON via write_file → /tmp/ → terminal python3** (cron-mode, execute_code blocked). Use a `make()`-style helper with `stars` as an int (never None), `None` not `null`, no star glyphs inside the script (ASCII asterisks built at runtime with `"*" * stars`), Japanese reasons without ASCII double quotes. Gate with the lint pass — `write_file` lints .py automatically. 15 decisions this run: 4 takes / 7 references / 4 batch-skip entries (batch skips collapse ~45 raws into 3-4 entries, one pipe-joined excerpt each — the large-batch compaction pattern).

4. **Verify JSON parseable** with hardcoded-path `python3 -c` (no pipes).

5. **Archive EARLY**: `python3 scripts/archive_triage.py dreaming --keep-reference`. This run printed a misleading container-home `archive_path` (`/opt/data/.hermes/home/...` — symlink, ignore) and the first invocation's output was truncated by `tail -5` mid-JSON, so a second invocation was run just to grep the counters (idempotent — safe). 11 archived, total_archive_urls 3,287.

6. **Log prepend via entry-file + insert script** (both `write_file`, run via terminal) — NOT patch, NOT heredoc:
   - Entry file `/tmp/dreaming_group_entry_<date>.md` starts with a leading blank line; contains the full mixed JP/EN log entry. (CJK in a log entry is FINE — log.md is an already-Japanese file, the language hook only blocks NEW JP in previously-clean files.)
   - Insert script asserts `len([l for l in lines if l.startswith('# Wiki Log')]) == 1` (line-START, not substring), anchors on the italic `_Log of all wiki changes..._` line, inserts after it with one blank separator, idempotency guard on `## [date] dreaming group`, re-verifies header count and single-entry after write.
   - The post-insert `print(open(log).read().split('\n')[:8])` self-check confirmed header at line 1 — this cheap head-8 eyeball is what catches burial/dup before commit.

7. **Selective staging + commit**: `git add wiki/log.md wiki/raw/archived/triage/dreaming/<date>_<runid>.json wiki/raw/archived/triage/archive_index.json` — never `git add wiki/` (dirty sibling tree). Plain `git commit -m` — tag hook passes on log.md + archive JSON. Plain `git push` (no pull --rebase; sibling tree blocks it and the local branch is ahead anyway).

## Classification heuristics that worked

- **Take signal**: keyword grep returns zero concept/entity coverage AND the raw has first-party data/experiments (protein-sequence prediction tests, vendor's own latency benchmarks, site-owner traffic series, CVE disclosure follow-up).
- **Reference signal**: a same-topic page exists (created same week by another pipeline) — assign reference with the exact page path and let downstream verify specific claims.
- **Batch-skip entry construction**: one decision with empty `url`/`raw_path`, title "X batch (reason) xN", pipe-joined member titles in `body_excerpt`. Three buckets worked well: company-blog marketing, non-AI/personal blogs, opinion/quote-post items. Archive tolerates URL-less decisions (they land in the dated JSON but not the URL index — expected).
- **Today's-sibling-saturation exclusion**: any topic appearing in today's trending-topics/active-crawl commit messages is a skip even if its raw file is absent from the archive index — the commit is a stronger coverage signal than the archive index for same-day stories.

## Numerical expectations (2026-11-19 data point)

- Saturation-day group run: ~30-40 terminal/tool calls, 1 commit, 0 content-page edits.
- Archive yield on a fresh Pattern E pool after a 2-day gap: ~10-15 newly archived out of 11-20 candidates.
- Report table format: Takes as a table (candidate | NJ stars | target path), References as a comma list, batch skips as counts per bucket.
