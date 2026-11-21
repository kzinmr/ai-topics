# Trending-topics clean run — 2026-11-11 (weekday noon, ~45 calls, 1 commit 17 files)

Verified weekday-noon trending-topics run. Extends `trending-batch-run-2026-11-10.md` (sibling-race counts) and `trending-batch-run-2026-11-08.md` (JS-rendered recovery, sed typo route) with: the two-hook block sequence in ONE run, the pre-commit grep gates, and the "gloss is content" rule.

## Call sequence (skeleton)

1. State probe: `date -u`; `ls -t inbox/rss-scans/ | head`; blog_ingest + newsletter `latest.json` (check internal timestamps, not mtime); `git log --oneline -12` (what siblings already committed: blog-ingest, newsletter-triage, hot-post told me Muse Ember raw + Fable 5.2 pages existed → coverage table, not re-creation).
2. `cp $(find ~/ai-topics/config/hermes/skills -name hn_algolia_supplement.py | head -1) /tmp/hn/` then `timeout 150 python3 hn_algolia_supplement.py --days 2 --min-points 20 > out.txt` — read in two `sed -n` passes (no `| head`).
3. Points-only sweep via own script (write_file → terminal): `search?tags=story&numericFilters=created_at_i%3E{yesterday12:00},points%3E100&hitsPerPage=50`. This caught "What objective is reasoning solving?" (147p) which the keyword pass missed — title contains none of the AI keywords.
4. Coverage sweep BEFORE proposing pages: batched `find concepts entities -iname '*kw*'` one-liner over ~16 keywords. Already-covered verdicts: alphaproof→`alpha-proof-nexus` (DIFFERENT product line — new page justified: Nexus = math/Erdős, Code = software verification/Signal; linked both ways), gemini-4-carbon→`concepts/gemini/gemini-4-carbon.md`, fireworks→`entities/fireworks-ai.md`, coreweave→existing.
5. fetch_sources.py (8/8 OK first pass — Chrome UA + gzip sniff; this weekday even deepmind.google fetched clean) + mine_comments.py (10/10 stories, read(3_000_000), depth<=2, cap 14, min-len 90). WSJ 401'd as expected → Algolia thread reconstruction with explicit English paywall gloss.
6. Stage pages as `/tmp/hn/page_*.md` via write_file; raws as `/tmp/hn/raw_*.md` with `sha256: pending`. One batch_update.py: SCHEMA mint (8 tags) → raw copy + two-pass sha256 → page copy with existence guard → heading-anchored appends (`\n## Related Pages` / `\n## Related` / `\n## Sources` / `\n## References` fallback chain) → alphabetical index insert with count bump → log prepend with `ln.strip()=="# Wiki Log"` dedupe + assert exactly one H1 at line 0.
7. Report → copy to `inbox/rss-scans/trending-topics-YYYY-MM-DD.md`, Hangul grep gate (`grep -P '[\x{AC00}-\x{D7AF}]'`), wikilink `[ -f ]` loop over ALL `[[targets]]` (19/19 OK).
8. Scoped `git add` (17 named files; sibling jobs had concurrent uncommitted `config/hermes/skills/` changes) → `git commit -m`.

## The two hook blocks (both single-line fixes, sequence matters)

Block #1 (tag validator): `concepts/alphaproof-code.md: lean` — NOT in SCHEMA despite Lean being the page's central technology (`lean-startup` substring-matched a naive grep, whole-word miss). Recovery: checked sibling `formal-verification-llm-agents.md` → uses `formal-methods` → swapped, re-add, re-commit. Rule: proper-noun tech nouns are subject to the page-name-not-equals-tag family; `grep -cw` every tag, same-topic sibling frontmatter is the cheapest oracle.

Block #2 (language policy): after fixing #1, the SAME re-commit was then blocked with `NEW Japanese introduced to clean file: wiki/entities/anthropic.md` — the sole JP was a 6-token parenthetical `(本文 paywall未取得, HN再構成)` at the end of an otherwise-English append. The hook is per-file character-level; short status asides are content. Recovery: `sed -i 's|本文 paywall未取得, HN再構成|WSJ paywall; body reconstructed from HN|'` → re-add → commit green. Note: the `patch` tool FAILED to match when the old_string used 構成 but the file had 构成 (variant-mismatch fuzzy fail) — grep the exact line first, or sed directly.

Both blocks are SEQUENTIAL: tag validator runs first, language hook second — so a run can pay two round-trips on one commit. Prevention gate that would have caught both: before `git add`, run (a) `grep -nP '[\x{3040}-\x{30ff}\x{4e00}-\x{9fff}]'` on every non-raw wiki file touched, (b) `grep -cw` every planned tag against SCHEMA.

## Other confirmations

- Hangul grep on the JP report caught Korean-lemma leaks (引き金 typo via Hangul 금, and 요약 in a heading) → fixed via `sed -i` (safe, report is outside wiki/). The documented "grep for Hangul" step is only useful as an EXECUTED gate — run it, don't eyeball.
- Index count reconciliation post-final-commit: `grep -c '^- [[concepts/'` = 2331 = header, entities 967 = 967 — clean this run, no reconciliation commit needed (still always check; the 11-10 sibling-race variant can bite any run).
- Newsletter triage `summary_ja` explicitly listed its take/reference decisions — reading it prevented duplicating the Muse Ember page (raw existed, page creation delegated to the sibling triage pipeline).
