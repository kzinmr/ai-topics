# Dreaming-GROUP (triage-only) clean-run recipe — validated 2026-11-20

The 18:10 UTC `dreaming-group` job is **triage-only**: build `triage_latest.json` + run
`archive_triage.py` + one `log.md` entry + staged commit. ALL entity/concept content edits
belong to the downstream `dreaming-wiki-ingest` (18:20). Do NOT edit `entities/`/`concepts/`
in this job — write takes/references into the JSON for downstream.

## Clean call sequence (this run: ~15 calls, 1 commit, hooks green, no --no-verify)

0. Probe checkpoint shape: `python3 -c "import json;p=json.load(open('/opt/data/.hermes/cron/data/dreaming/latest.json'))['payload'];print({k:(type(v).__name__,len(v) if isinstance(v,(list,dict,str)) else v) for k,v in p.items()})"`.
   `payload.articles: 0` + `recent_raw_articles: 286` = Pattern E trigger. Trust the checkpoint, not the injected summary.
1. Read prior `triage_latest.json` (yesterday's) — but **re-verify each prior `take` against the actual page body**, do NOT blanket-skip prior takes as "consumed".
2. Run `python3 config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py` (full skill-dir path — NOT repo-root `scripts/`). Decisive never-triaged pool.
3. Batch coverage grep: `[grep -il keyword entities/<x>.md concepts/*.md]` per candidate; `find wiki -path ./raw -prune -o -iname '*kw*' -print`.
4. Read top AI candidates (DeepMind essays, OpenAI posts, benchmark pages, HN reconstructions).
5. Build `triage_latest.json` via `write_file`→`/tmp/build.py`→`terminal python3` (CJK in `reason_ja` is fine via write_file, NOT heredoc). source field = `"dreaming"`.
6. `python3 scripts/archive_triage.py dreaming --keep-reference`.
7. `write_file` the log entry to `/tmp/dreaming_log_<pipeline>_<date>_<hhmm>.md`, then `python3 config/hermes/skills/_custom/dreaming/scripts/repair_log_md_header.py wiki/log.md <entry>`. Verify header count==1, your entry unique.
8. Stage explicitly: `git add wiki/log.md wiki/raw/archived/triage/dreaming/<date>_<runid>.json wiki/raw/archived/triage/archive_index.json`. Commit, plain `git push`.

## NEW technique 1 — "log says consumed ≠ body has the content" verify on PRIOR takes

The strongest genuine reference gap this run came from a **prior day's `take` that a sibling
job claimed to consume but never wrote**. The `dreaming group` 11-19 log entry listed a take
"Claude was trained on protein sequences at scale → `entities/anthropic.md`", but
`grep -c protein entities/anthropic.md` returned **0** (only `concepts/esmfold2.md` mentioned
it). The log CLAIM ≠ body CONTENT. Contrast: sibling takes (blink, Java4Shell, All About
Berlin) WERE present in their target pages → correctly skipped.

**Rule:** when carrying forward / re-screening a prior triage's `take`s, do not infer
"already consumed" from the prior log line or the page's mere existence. Per prior take:
`grep -i "<the article's SPECIFIC claim/keyword>" <candidate_wiki_path>` and read the body
section. Zero body hits while the log says "take → that page" = genuine uncaptured gap →
re-queue as `reference` (or `take`) for THIS cycle. This is the take-side mirror of the
existing "log.md coverage claim ≠ applied content" gate.

## NEW technique 2 — "primary-source saved to raw/ by trending-topics ≠ concept page has the synthesis"

When a same-day sibling (trending-topics 12:30, active-crawl 11:00) lists a raw article in
its commit (`git show --stat` shows `wiki/raw/articles/<x>.md`) AND names a target concept
page, the article can be **fully consumed** — verify by grepping the SPECIFIC data points
into the body, not the page title. This run: OpenAI "Advancing chip design" raw was saved by
trending-topics `52f7d456`, and `concepts/openai-jalapeno-inference-chip.md` lines 97-108
already carried AMD 14% PPA / GPT-Synopsys / RISC-V 9,881-runs / GPT-6.2 Astra → correct
**skip**, not a re-triage candidate. The complementary trap (documented elsewhere) is the
raw saved + hot-post mentioned but NO concept-page synthesis → that IS a take. Decide via
`grep -il "<topic>" concepts/<subdir>/*.md` + grep the specific numbers, never the page name.

## Staging variant confirmed (Takes>0, group-stage = content untouched)

When Takes>0 but this job edits NO content files (group stage), the only wiki delta is
`log.md` + the dated archive JSON + `archive_index.json`. Stage those three explicitly —
never `git add wiki/` (the sibling tree carries ~70 concurrent skill/raw files). Commit
`43a231d2` passed tag-validation (3 files) + index-validator, plain push, zero `--no-verify`.

## Archive double-run

First `archive_triage.py dreaming --keep-reference` writes the dated file (+6 URLs,
`archive_index 3295→3301`, `dedup_skipped: 2`). A second run prints
`"message":"All items already archived (dedup)","archived":0` — idempotent, expected. The
printed `archive_path` shows `/opt/data/.hermes/home/ai-topics/...`; `readlink -f` confirms
it symlinks to `/opt/data/ai-topics/...` (same file). Don't move it.
