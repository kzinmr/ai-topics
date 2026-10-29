# Model-Release Impact Investigation (time-boxed sources)

Recipe validated 2026-10-17 investigating DeepSeek-V4.1-Flash-1017 (~4h after announcement). Use when the user shares an X announcement URL and asks for "impact" research with a constraint like "sources must satisfy the time window" (i.e., only info published after the announcement).

## Steps

1. **Announcement metadata + full text** (per main SKILL.md): `xurl "/2/tweets/<ID>?tweet.fields=note_tweet,created_at,author_id,public_metrics&expansions=author_id&user.fields=..."`. `created_at` defines the time-window lower bound; `public_metrics` (impressions/likes/quotes) is itself impact evidence.
2. **Recover the whole thread** via the author timeline if the tweet is `1/N` (see pitfall in SKILL.md). Announcement threads usually contain: benchmarks teaser, demo cases, pricing/API news, weight-download links.
3. **Expand t.co links** per tweet with `tweet.fields=entities` → `entities.urls[].expanded_url`. Usually yields HF model card, docs page, product page — the primary sources.
4. **Scrape primary sources via Jina Reader** (`curl -sL "https://r.jina.ai/URL" -H "Accept: text/markdown"`): HF model card (benchmark table, license, tech-report PDF link, recommended sampling params), vendor docs/news page (case demos, billing dates).
5. **HN reaction, filtered to the window**: `curl -s "https://hn.algolia.com/api/v1/search_by_date?query=<model>&tags=story&numericFilters=created_at_i%3E<epoch>"` (use https, not http — pipe-to-interpreter and plain-HTTP both trip approval gates). Then `https://hn.algolia.com/api/v1/items/<objectID>` and recursively flatten `children` to read comment threads — this is where community sentiment, comparisons ("above GLM-5.3, close to Opus 5"), skepticism ("benchmarks can't be real"), and workflow anecdotes live. Two sibling story threads (HF link + product link) often exist; read both.
6. **Real pricing via OpenRouter API** (the rendered page is JS — Jina grep of prices fails): `curl -s "https://openrouter.ai/api/v1/models"` then filter by model id; `pricing.prompt`/`completion` are per-token (×1e6 for $/M tokens), plus `context_length`. Compare against the previous version's pricing — same price + big benchmark jump = "price destruction" framing.
7. **Check existing wiki pages first** (`~/wiki/entities/<model>.md`) so the answer references prior-generation context (architecture, KV-cache numbers) and offers a wiki update at the end.

## Framing rules

- Label all vendor benchmarks "self-reported, independent verification pending" — and check if the benchmarks themselves were recently found buggy (search HN in-window for benchmark-integrity posts).
- Separate "model impact" (benchmark deltas vs same-tier and frontier models) from "ecosystem impact" (pricing, API/platform expansion like search APIs, harness optimizations, open-weight license).
- Community reaction: quote both enthusiasm and skepticism. Timestamp every source and keep all inside the requested window.
