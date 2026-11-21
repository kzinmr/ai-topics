# Trending-topics clean run — 2026-11-08 (Sunday noon UTC)

~30 tool calls, 1 commit (19 files), both pre-commit hooks green, no rework. Follows the 11-02/11-03/11-07 skeletons.

## Call sequence (canonical order)

1. `git pull` + `git log --oneline -12` + `date -u` — sibling-job state probe (active-crawl 11:00, hot-post, blog/newsletter ingest commits visible in log tell you what's already covered).
2. Read checkpoints: `~/.hermes/cron/data/blog_ingest/latest.json` (date/run_id/scan.total_new/saved_articles) + `newsletter/latest.json` (processed_count). Timestamps fresh (today's run_id) → trust them.
3. Copy `hn_algolia_supplement.py` from `_custom/daily-rss-triage/scripts/` to /tmp, run `timeout 150 python3 ... --days 2 --min-points 20 > out.txt 2>&1`, read in two `sed` passes.
4. Points-only sweep script: `search?tags=story&numericFilters=created_at_i%3E{yesterday12:00},points%3E110&hitsPerPage=50`. On this Sunday the sweep added nothing new beyond the keyword block (Apple grey-list, Turbo Pascal), but on 10-31/11-07 it was the only source of lead stories — keep running both.
5. Coverage sweep: one `find concepts entities -iname '*kw*'` batch over ALL candidate topic keywords + `grep -i <topic> index.md`. Mark rows ✅ 済み with verified real paths.
6. Batched `fetch_sources_1108.py` (Chrome UA + gzip sniff + strip_html, print-and-continue): 11/13 OK; expected gate class = perplexity.ai 403, science.org 403.
7. Batched `mine_comments_1108.py` (per-story IDS dict, `read(3_000_000)`, depth ≤2, cap 14, min-len 90): 12/12 stories produced report-grade quotes in one run.
8. save_raws script: frontmatter with `sha256: pending` placeholder, body = article + `## HN discussion highlights (item <id>, <pts>pts)` appendix from mined comments. Hash fixed in batch_update two-pass.
9. One idempotent batch_update script: SCHEMA tag adds → staged page copy from /tmp → heading-anchored appends (try `\n## Related\n`, `## Related Pages`, `## Related Concepts`, `## See Also`, `## Sources`) → sha256 recompute → index insert after verified anchor + Concepts count bump → log prepend with `ln.strip()=="# Wiki Log"` dedupe.
10. Wikilink sweep: bash `[ -f ]` loop over every `[[target]]` + `grep -o "\[\[[^]|]*"` extraction. All OK.
11. Report via write_file'd Python script (JP text), scoped `git add` of exactly my 19 files, `git commit -m` (hooks green), push, post-commit count reconciliation (concepts 2318/2318, entities 966/966 — matched, no fixup commit needed).

## New this run

### Vendor React/JS-rendered blog pages → Algolia comment tree IS the content
Apiiro's post returned 3.9k/4.2k chars of pure page chrome (config comments, SEO boilerplate) on BOTH trailing-slash variants — retrying URL variants was wasted effort. The client-side-rendered body never appears in raw HTML. Recovery that worked: the vendor's own author comments in the HN thread (shmulc) answered the top technical objections verbatim and carried the full fact chain; saved the comment tree as the raw file (no article body) with the HN URL as `source:`. Rule: when a fetch returns THIN (<5000 chars) AND the stripped text is config/meta boilerplate, skip further fetch retries — mine the HN item tree and cite it as HN-thread-derived. (Same class as the paywalled-lead-source recipe, extended to JS-rendered vendor blogs.)

### Report typo fix: `sed -i` on a report file beats python heredoc + patch
Post-write, the report contained one stray Korean word (typo). Fixed in one call: `sed -i 's/OpenRouter 호출/OpenRouter 呼び出し/' inbox/rss-scans/<file>`. The report is OUTSIDE wiki/ (language-policy hook exempt) and the sed command string contained zero CJK outside the search/replacement tokens themselves — no `tirith:confusable_text` fire, unlike the documented Python-heredoc block for JP-heavy files. For a 1-2 token typo in a non-wiki report file, plain sed is cheapest; keep the patch-tool rule for wiki pages with dense JP prose.

### Mixed-Hangul/CJK typo class
Beware non-Japanese CJK leaking into JP report prose (here 호출 = Korean "call"). The report is JP-only by policy — a quick eyeball or `grep -P '[\p{Hangul}]'` before delivery catches it; the wiki language hook does NOT guard inbox/ reports.

## Positive confirmations (no action needed)
- All 8 minted SCHEMA tags (`maxxbench`, `benchmark-integrity`, `memory-standards`, `interoperability`, `microsoft-research`, `ai-frontiers`, `john-langford`, `on-device-ai`) were caught as absent by whole-word `grep -cw` pre-check; patched category lines BEFORE page creation → zero hook fires.
- `anthropic-ipo` already existed in Models line (added 11-07) — checking sibling/frontmatter orphans from yesterday's runs first saved a duplicate mint.
- Heading-anchored append pattern worked on 4 heterogeneous pages (entity with `## See Also`, concept _index with `## Related Pages`, concept with `## Related Pages`+`## Values & Positions`, benchmark page with `## Related Concepts`) — zero mis-inserts, per the 10-31 verification.
- Log prepend dedupe (`ln.strip() == "# Wiki Log"`, keep first) produced exactly 1 header in one shot.
- Post-commit count reconciliation matched with no sibling drift today — still run it, cheap.
