# Worked example — 2026-10-31 (Saturday daily run)

**Day shape**: Saturday, no active-crawl research note, 91 DB articles (48 AI-relevant), 3 newsletters, Friday-afternoon releases surfacing on HN. Topic axis shifted from model capability to **AI corporate finance + politics** (OpenAI funding shortfall, Anthropic rating warning, congressional no-bailout resolution, tech sell-off) with an agent-safety/supply-chain second thread (OpenAI L0–L3 monitoring disclosure, Cursor VSX backdoor follow-up, SRE deskilling, Proton AI mandate).

## What produced the topics (in yield order)

1. **Points-only Algolia sweep** (`search?tags=story&numericFilters=created_at_i>{yesterday-noon},points>150`) → 6 of 8 topics. THIS was the load-bearing query; none of these titles matched the AI keyword list. See `scripts/hn_points_sweep.py`.
2. Keyword pass (`hn_calibrate.py` argv, `points>60`) → surfaced Qwenputer 698p / NESformer 257p / agent_summary 583p continuations + Claude Duet 124p. Mostly yesterday's stories — front_page-tagged items decayed as documented.
3. blog_ingest checkpoint's afternoon raws (`find -newermt "2026-10-30 12:00"`) → Cursor security notice, Cohere C$4B, Harvey adoption data, Parallel (brotli stub).

## Gated sources and what worked

| Source | Result | Fallback used |
|---|---|---|
| wsj.com (OpenAI funding) | 401 | HN `/items/50312922` comment tree — top comments quote the article + give the "no S-1 to pore over" comparative frame |
| fortune.com (Cisco tokens) | 404 (URL rot) | HN 50304122 thread |
| ft.com / bbc.co.uk | paywall/bot shell | HN thread comment quoting FT lede |
| openai.com/index/* | 403 | RSS-fetched titles + alignment.openai.com (this one plain-fetched fine) |

Recipe applied: walk Algolia item `children` depth ≤2, ~40 comments, strip tags, min length ~90. Cite as thread-derived, never as reading the paywalled piece.

## Wiki actions

5 new pages (openai-misalignment-monitoring, ai-bubble-bailout-resolution, sre-deskilling, proton-ai-mandate-backlash, openai-oct31-policy-bundle), 3 raws, 6 existing-page appends via the heading-anchored insert-before-Related pattern (anchor order `## Related` → `## Related Pages` → `## Sources` → `## References`, EOF fallback) — zero mis-inserts across heterogeneous page shapes.

## Hook friction (all resolved, no --no-verify)

- `ai-bubble` blocked on the new resolution page — page exists as a NAME but was never a tag; sibling `ai-bubble.md` uses `economics/valuation/controversy`. Mapped, didn't mint.
- `emulation` blocked on `weight-compiled-computers.md` — a tag ANOTHER job added earlier that day; removal, not minting. Check `git diff --staged <page> | grep '^+.*tags:'` to see whose token it is.
- Index header counts drifted (2271 vs 2272 lines, 956 vs 957) after a post-script page add — validator does NOT check parity; one reconciliation commit fixed it.

## Confidence treatment

Vendor self-reports (OpenAI's 30-min replay alert, Cursor's "no successful logins") got `confidence: medium` with explicit splits: first-party description of controls = high as *reporting of what they say*; effectiveness claims = self-reported, not audited; replay ≠ prospective validation; "no logins" = vendor telemetry assertion, not confirmed negative. Same pattern as the Qwen/Cohere single-source rule.
