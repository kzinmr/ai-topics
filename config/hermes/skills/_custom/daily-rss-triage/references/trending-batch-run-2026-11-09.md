# Trending Batch Run — 2026-11-09 (Monday noon, clean run)

~35 tool calls, 2 commits (18 files + 1 reconciliation), both pre-commit hooks green, no `--no-verify`, zero rework.

## Call sequence (the skeleton that worked)

1. `git pull --ff-only` + `git log --oneline -12` + `ls inbox/rss-scans/ | tail` — sibling-job state probe.
2. Read `~/.hermes/cron/data/{newsletter,blog_ingest}/latest.json` + `triage_latest.json` via one `python3 -c` (no pipes). Established: blog_ingest 33 new / 16 raw already ingested at 10:11, newsletter 3 processed / triage 2 take 2 ref 56 skip already ingested at 10:16.
3. `git log --oneline --since=today` + `git diff --stat wiki/` — saw the newsletter job's 12 uncommitted wiki `M` files. **Left them alone**; scoped `git add` excluded all 22 concurrent dirty files.
4. `find ~/ai-topics/config/hermes/skills -name hn_algolia_supplement.py` → cp to /tmp → `timeout 150 python3 ... --days 2 --min-points 20 > /tmp/hn/out.txt` (165 lines), read in two `sed -n` passes. Note: the deployed copy resolved under `/opt/data/.hermes/home/ai-topics/...` (container-home path) and the same content is reachable at `/opt/data/ai-topics/config/hermes/skills/_custom/daily-rss-triage/scripts/` — both cp fine.
5. Points-only 24h sweep (`search?tags=story&numericFilters=created_at_i%3E{ts},points%3E100`) via write_file→terminal. Caught RAM Altman (234p) and the Nvidia-affair pair that the keyword block missed; no new AI lead beyond the keyword pass.
6. `fetch_sources.py` batch (12 targets, Chrome UA + gzip sniff + strip_html, print-and-continue): **10/12 OK first pass**. Fails: polso.info `HTTP 418` (bot counter), 247wallst `404`.
7. `mine_comments.py` (10 stories, `read(3_000_000)`, depth ≤2, cap 12, min-len 90): report-grade author quotes for all 10 in one run.
8. Coverage sweep: one batched `find concepts entities comparisons queries -iname "*kw*"` over ~12 topics + `grep -ril` on candidate pages. Result: Microsoft AI Frontiers, OpenAI $11B@1.25T, Anthropic IPO valuation, GPT-6 Cyber all already covered → NOT re-created. Only one genuinely-new page.
9. `grep -cw` on ~28 candidate SCHEMA tags → 6 to mint. Read the real `## ` heading list of every append target first (assert-count avoided any mis-insert).
10. `save_raws.py` (7 raws, `sha256: pending` placeholder then separate recompute pass).
11. Staged the new page body via `write_file` to `/tmp/hn/pages/`; batch script only `shutil.copyfile`s it.
12. `batch_update.py` — SCHEMA mint → copyfile page → 6 heading-anchored appends (idempotency guard `if heading in t: skip`) → index insert with `assert count==1` on a short stable anchor + Concepts count bump → log prepend with `ln.strip()=="# Wiki Log"` dedupe. Ran clean, one pass.
13. Post-write wikilink sweep: `for t in ...; do [ -f "wiki/$t.md" ]` — caught ONE ghost: `[[concepts/model-attestation]]` (tag exists in SCHEMA, page does not; real page is `concepts/provable-inference.md`). Same class as the documented "tag-shaped name ≠ page" trap, but the reverse direction: **a tag being in SCHEMA does not mean a page of that name exists.**
14. Report via `write_file` Python script (never heredoc — JP prose + em-dashes). Grep for Hangul/stray CJK caught `어` inside a JP word (덩어리) → fixed with `patch` tool. Report also needed `sed -i` on a `那样` CJK leak — plain `sed -i` fine outside wiki/.
15. Scoped `git add` (18 explicit paths) → `git commit -m` → hooks green → push.
16. Post-commit count reconciliation: Concepts header correct, **Entities header 965 vs 966 real lines** (sibling job drift) → one-line reconciliation commit + push. Exactly the documented two-step.

## New lessons this run

- **HTTP 418 is a new fetch-failure class** (polso.info) alongside 401/403/404. Same handling as the Reddit-403 recipe: Algolia `/items/<id>` comment tree becomes the raw file with `type` article/HN-record frontmatter. Two of seven raws this run were comment-tree records (418 article, unretrievable X long-form).
- **X long-form posts are unretrievable by urllib** (no 403, just nothing useful) — go straight to the HN tree, do not burn retries.
- **`_index.md` for claude-code** is `concepts/claude-code/_index.md`, not `index.md` — wikilinks to `concepts/claude-code/index` will miss.
- Nothing to fix in the existing skill guidance; every documented pitfall that could bite (pipe-to-interpreter, heredoc JP, SCHEMA whole-word grep, heading-anchored append, log H1 dedupe, scoped add, sibling-modified /tmp warnings) behaved as described.
