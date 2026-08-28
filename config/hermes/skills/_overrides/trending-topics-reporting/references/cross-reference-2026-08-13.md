# Cross-Reference 2026-08-13 — Frontier Model Day

Worked example for the **Frontier Model Day / multi-lab launch cluster** pattern.

## Context

- 9th consecutive no-active-crawl research-note day — but log.md head-scan showed active-crawl DID run (3 new concept pages + Zuckerberg enrichment, no note file). Confirms the "no note ≠ no work" rule from 08-11.
- Previous day's report (08-12) MISSING — dedup anchor was 08-11 report; covered 08-12→13 topics fresh.
- AINews fulltext extraction via open.substack.com worked (`ainews-spacexai-grok-46-and-grok`) — surfaced the whole "Frontier Model Day" narrative before any RSS cycle.

## The Cluster

4 independent lab launches in 48h (8/12-13):
1. **Grok 4.6 + Grok Bot** (xAI) — AA Index 61, $2/$6 per 1M, Terminal-Bench 88.4%, Grok Bot 22.9M views. HN 334pts/381c on the AA article.
2. **Qwen3.8-Max open weights** (Alibaba) — 2.4T/95B MoE actually dropped, vLLM day-0 + B300/MI355X 4-bit checkpoints, **text-only caveat**, Unsloth 1-bit 4.9TB→397GB.
3. **DeepSeek V4 Pro GA** — $0.435/$0.87, ~57× cheaper than Fable 5 (Cline), Terminal-Bench +15.8%. HN 79pts.
4. **MAI-Thinking-1 in Foundry** (Microsoft) — first from-scratch reasoning model.

Treatment: each stayed its OWN topic (different companies validate each other, different domains: capability / open-weights / pricing / platform). Intro carried a "Frontier Model Day — 48時間で4つのフロンティアモデル発表" concentration note. This is the opposite of the coordinated-campaign rule (same-lab critique+launch = ONE topic) and of conference clusters (one source = ONE topic).

## HN Date-Mixing Pitfall (the key lesson)

`search_by_date?query=Qwen3.8-Max` returned a 546pts hit — but `created_at` was **2026-08-06** (the agentic-index ranking article), 7 days before the 8/12-13 weights drop. The weights-drop story itself had NO in-window HN points. Using the 546pts to calibrate the current event would have over-rated it. Always check `created_at` per hit before ★ calibration; if the top hit is stale, either cite it as context or drop it.

Also observed: `Grok 4.6` query top hit was the AA article (334pts) — the correct in-window signal — while the Cursor blog post (13pts) and OpenRouter listing (29pts) were lower. Point calibration should use the strongest in-window authoritative hit, not the launch page.

## Wiki Coverage / Residual Work

Morning pipelines (active-crawl, newsletter-wiki-ingest, blog-wiki-ingest) had ingested 5/7 topics:
- ✅ grok-4-6-launch (event page), deepseek-v4 (V4-Pro-0813), synthid (watermark section), microsoft-mai-models, j-lens (concept page)
- ⚠️ **Residual**: `concepts/qwen-3-8.md` had the Aug 3 announcement + active-params resolution (95B/2.4T) but NOT the actual 8/12-13 weights-drop section (vLLM day-0, B300/MI355X 4bit, text-only caveat, Unsloth 1-bit). Pattern: a page can be touched by pipeline (updated date bumped) yet still miss the day's actual event section — verify by grepping page content for the event, not by `updated:` date alone.
- ⚠️ Low priority: DiG-bench / Conceptual Reasoning Index had no wiki page (AI-for-Science cluster, ★★★☆☆).

## Report Mechanics

- Report saved to `inbox/rss-scans/trending-topics-2026-08-13.md` (14.9KB, 7 topics). Save-only job confirmed again: daily reports are git-untracked (`??` in status); no commit.
- Wikilink verification: batch `[ -f wiki/$f.md ]` check on all 7 action-table targets passed before writing report (0 MISS).
- DB query reused the combined 3a+3b keyword script → promoted to `scripts/trending_db_query.py` in this skill so it is not hand-written per run.
