# Trending-topics clean run — 2026-11-03 (12:00 UTC)

Reference call sequence for a weekday-noon trending-topics run that completed with 2 commits, zero hook failures, zero rework except the apostrophe SyntaxError (see SKILL.md pitfall #21 extension).

## State probe (parallel, 2 calls)
- `git pull --rebase` → failed "unstaged changes" (other jobs' skill-file edits). Correct behavior per pitfall #14: skipped pull, plain push later succeeded. Never stash/commit other jobs' files.
- `ls -t inbox/rss-scans/`, newsletter + blog_ingest checkpoint `latest.json` (both today's run_ids), `git status --short` (all unstaged changes were `config/hermes/skills/` — left untouched).
- log.md morning entries told what newsletter-wiki-ingest already covered (Realtime-Bench, Figma PM OS, Duet 9-task) — none overlapped the noon topics. active-crawl had NOT run today (no 11:00 entry).

## Scan sequence (3 terminal calls total)
1. `find` for hn_algolia_supplement.py → deployed path was `/opt/data/.hermes/home/ai-topics/config/hermes/skills/_custom/daily-rss-triage/scripts/` (the `.hermes/home` prefix form worked). cp to /tmp/hn, run `--days 2 --min-points 20`. **Pipe-to-head gotcha: `... | head -120` killed the script at 60s mid-keyword-block. Re-run redirecting to a file (`timeout 120 python3 ... > out.txt 2>&1`), then sed-window the file.**
2. Self-written `scan2.py`: unfiltered `search?tags=story&numericFilters=created_at_i%3E{24h},points%3E100&hitsPerPage=50` sweep (surfaced the day's non-AI-keyword leaders: Oracle, Intel rout, Subvocal, WTF-Ubuntu) + 10-keyword second pass.
3. **Keyword-filter gotcha (NEW)**: on the plain `search` endpoint, `query=<term>&numericFilters=created_at_i%3E{ts},points%3E60` returned ZERO hits for every keyword. Swap to `search_by_date?query=<term>&tags=story&numericFilters=points%3E50,created_at_i%3E{ts}` → works. The points-only unfiltered sweep is fine on `search`.

## Evidence gathering (2 write_file + 2 terminal, per 2026-11-01 recipe)
- `/tmp/hn/fetch_sources.py` — TARGETS list, Chrome UA + gzip sniff + strip_html: 5/6 OK first pass (rikiyat.github.io, techpolicy.press, regenerator1.com Substack, arxiv abstract, terrytao.wordpress.com), only FAIL the known openai.com 403 (documented gate class → cite via HN thread, mark 本文未取得 in report/page).
- `/tmp/hn/mine_comments.py` — IDS dict of 12 objectIDs → item JSON `read(3_000_000)`, children depth ≤2, cap 14, min-len 90, author-attributed 450-char quotes. All 12 OK; quotes went verbatim into raw files' HN-appendix sections and the report.

## Coverage check before page proposals (batched terminal calls)
`for kw in ...; do find concepts entities -iname "*${kw}*"; done` + `grep -in` on index.md → confirmed all candidate topics UNINGESTED. SCHEMA token checks caught the near-miss pairs again: `open-weight` exists / `open-weights` does NOT; `pretraining` exists / `pretraining-poisoning` does NOT. Minted 6 tags (weight-space-programming, model-editing, pretraining-poisoning, agentic-backdoor, anthropic-ipo, self-hosted-inference) on the Models line BEFORE writing pages — zero hook failures as a result.

## Batch script (the one stumble)
Single `/tmp/hn/batch_update.py`: SCHEMA patch → raw copies + two-pass sha256 → page copies (from /tmp-staged bodies) → 7 heading-anchored idempotent appends (Related/Sources anchor ladder, all 7 hit) → index inserts (anchor = existing wikilink line via `re.search(re.escape(anchor)+r'[^\n]*\n')`, insert AFTER; short stable anchors survived sibling drift) → log prepend with H1 dedupe (`ln.strip()=='# Wiki Log'`).
- **Stumble**: `append_section('page.md', '## ...OpenAI's Git scale-up...', '''body''')` — apostrophe in the single-quoted heading arg closed the string early; compiler blamed an em-dash (U+2014) inside the body two lines later. ~6 diagnostic calls wasted. Fix: double-quote heading/arg strings containing prose possessives. write_file's lint caught it as SyntaxError, but at the WRONG location (inside the triple-quoted body, not at the real apostrophe).
- Note: the `'''` body itself tolerates lone apostrophes fine — only a `'''` sequence would break it. The fragile spot is the single-quoted heading arg.

## Closing
- Post-write wikilink sweep: 18 targets via bash `[ -f ]` loop, all OK (verified subdir page `concepts/claude-code/claude-code-vsx-backdoor.md` exists rather than guessing).
- Scoped `git add` of exactly 16 files (never blanket `wiki/` — 11 concurrent skill-file changes from other jobs stayed out of the commit). `git commit -m` passed both pre-commit hooks with no `--no-verify`; push succeeded outright (no rebase needed).
- **Count reconciliation as separate final step (per 10-31 pitfall, re-confirmed)**: Concepts header 2287 vs actual 2289 lines after commit — the batch script's in-script regex bump under-counted; fixed in a one-line reconciliation commit. Entities header matched. Always run the `grep -c '^- [[concepts/'` vs header check AFTER the final commit.
- Report: `inbox/rss-scans/trending-topics-2026-11-03.md`, Japanese, with ✅済み/⚠️未収録 action table; every cited page path taken from `find` output or `[ -f ]`, none from memory. Secondhand quotes (Altman X post, Sutskever podcast remarks) explicitly marked 二手/secondhand with verify-before-verbatim notes both in the page and the report.

## Cost budget observed
~30 tool calls end-to-end. Expensive phases: comment mining (1 long run, fine), batch-script debug (~6 calls — avoidable with the double-quote rule), coverage sweeps (kept to 3 batched calls).
