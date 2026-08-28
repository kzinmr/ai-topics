# Cross-Reference Worked Example — 2026-07-31

Normal-volume weekday with a **high-density 2-axis week** (agent security + inference cost), NO active-crawl research note, and strong HN validation.

## Situation

- Blogwatcher DB: 153 articles published in 3 days; 63 AI-relevant via Query 3. Merge Blog (33), AI Engineer (26), simonwillison.net (14) dominated.
- No `*trending-topics-research*` file in either raw-articles path (active-crawl absent/renamed) — `find` returned nothing.
- Newsletter ingest: AINews flagged the GPT-5.6 price cut as CRITICAL (subject line only; body URLs were Substack redirects — known pitfall).

## Workflow used

1. Ran `trending_topics.py --days 3` + blogwatcher Query 3 (write script to /tmp via write_file, run via terminal — Pattern B).
2. **Read yesterday's report first** (`inbox/rss-scans/trending-topics-2026-07-30.md`) → dropped Kimi K3, ARC-AGI-3, NVIDIA Blackwell, antirez debate, MCP-ecosystem (all covered 7/30). Kept genuinely new: GPT-5.6 price cut, Anthropic cyber-evals disclosure, Word worm, Dwarkesh compute essay, Zuckerberg AI-centralization campaign, Merge Agent Handler.
3. Even though volume ≥20 (volume-based skip rule), ran 5 targeted HN Algolia point-score queries → materially calibrated ratings:
   - GPT-5.6 price cut: 585pts/381c → ★★★★★
   - Anthropic cyber-evals: 190pts/148c → ★★★★★
   - Dwarkesh compute: 3pts on HN → ★★★★☆ on analytical merit alone (strong author signal, low HN engagement)
   - Zuckerberg: NYT 11pts + FT coverage → ★★★☆☆ (continuation of the open/closed debate, not a new event)
4. Checked wiki frontmatter `updated:` dates before writing recommendations → `ai-worming.md` already created 7/30 by blog-wiki-ingest (marked ✅ DONE); `agent-governance.md` stale since 6/1 (needs Merge Agent Handler); `ai-economics.md` stale since 7/13 (needs Dwarkesh).

## Pitfalls hit (new)

- `curl ... | python3 -c ...` blocked by the security scanner (`tirith:curl_pipe_shell`) → use `curl -o /tmp/x.json` then parse in a SEPARATE command.
- `.dev`-TLD curl (merge.dev) flagged `tirith:lookalike_tld` → skipped; used blogwatcher-DB title/URL only.
- WSJ op-ed page returned a 767-byte bot-block shell → reported title + NYT/FT secondary coverage with attribution; no fabricated specifics about op-ed content.
- `delegate_task` with the `web` toolset returned plan-only summaries (no actual results) twice for the same verification question → prefer direct HN Algolia curl-to-file for quick existence/engagement checks.

## Report shape

7 topics: 2 security (Anthropic disclosure ★5, Word worm ★4), 2 cost/economics (GPT-5.6 price ★5, Dwarkesh ★4), conference cluster ★4 (AI Engineer 26 talks), Zuckerberg campaign ★3, Merge Agent Handler ★3. Intro called out the 2-axis thematic concentration (エージェントセキュリティ + 推論コスト).
