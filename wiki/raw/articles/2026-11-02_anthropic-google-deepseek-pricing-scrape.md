---
title: "Anthropic / Google / DeepSeek pricing — live scrape evidence (2026-11-02)"
type: raw-note
created: 2026-11-02
sources:
  - https://docs.anthropic.com/en/docs/about-claude/models
  - https://cloud.google.com/vertex-ai/generative-ai/pricing
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://openrouter.ai/api/v1/models
fetched_at: 2026-11-02T12:12:00Z
confidence: high
---

# Anthropic / Google / DeepSeek — live pricing data (2026-11-02)

## Anthropic — docs.anthropic.com model overview (Next.js RSC, embedded ModelComparisonSheet JSON)

Current lineup JSON (verbatim fields):

| Model | releasedOn | inputPerMTok | outputPerMTok | cacheWrite5m | cacheWrite1h | cacheRead | maxOutput | ctx |
|---|---|---|---|---|---|---|---|---|
| Claude Fable 5.1 | 2026-09-01 | 10 | 50 | 12.5 | 20 | 0.25 | 128K | 1M |
| Claude Opus 5.5 | 2026-09-22 | 4 | 20 | 5 | 8 | 0.20 | 128K | 1M |
| Claude Sonnet 5.5 | 2026-09-28 | 2 | 10 | 2.5 | 4 | 0.10 | 128K | 1M |
| Claude Haiku 5.5 | 2026-10-07 | 0.10 | 0.50 | 0.125 | 0.20 | 0.01 | 128K | 1M |

- Haiku 5.5 long-prompt pricing (>100K input): $0.50 in / $2.50 out / cache write $0.625 / cache read $0.05.
- `cacheReadExceptions`: Fable 5.1 / Mythos 5.1 multiplier 0.025×; Opus 5.5 / Sonnet 5.5 multiplier 0.05× (vs base input).
- Rendered pricingLines: Fable 5.1 "$10 / $50", Opus 5.5 "$4 / $20", Sonnet 5.5 "$2 / $10", Haiku 5.5 "From $0.10 / From $0.50".
- Legacy models still in docs: Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5 (intro $2/$10 — **introductory window through 2026-08-31 has expired as of 2026-11-02**), Sonnet 4.6, Haiku 4.5.
- Batch extended-output models listed: Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5, Haiku 5.5, Opus 4.8/4.7/4.6, Sonnet 4.6.

## Google — cloud.google.com/vertex-ai/generative-ai/pricing (Global endpoint, $/1M)

- **Gemini 4 Argon** (NEW): intro **$2.00 in / $10.00 out / cached $0.10 through 2026-11-30** (promo = 50% credits back on net spend); **standard from 2026-12-01: $4.00 / $20.00 / cached $0.20**. Non-global +10%. "Gemini 4 Argon Cyber Permissive" at standard rate $4/$20. 1M output completions; >32K completions billed for retrievable tokens even on failed requests (from 2026-11-13).
- **Gemini 3.8 Flash** (NEW): intro $0.75/$3.75 (cached $0.075) through 2026-12-31 → standard $1.50/$7.50 from 2027-01-01. Gemini 3.8 Flash Cyber: $1.50/$7.50 (cached $0.15).
- Gemini 3.7 Flash & 3.6 Flash: intro $0.75/$3.75 through 2026-12-31 (unchanged).
- Gemini 3.5 Flash $1.50/$9.00, 3.5 Flash-Lite $0.30/$2.50, 3.1 Flash-Lite $0.25/$1.50, 3 Flash Preview $0.50/$3.00, 3.1 Pro Preview $2.00/$12.00 (all unchanged).
- Non-global endpoints = 1.1× Global multiplier.

## DeepSeek — api-docs.deepseek.com

- The Docusaurus page served a JS shell to curl ("Your Docusaurus site did not load properly") — raw parse unavailable this run.
- Model ids present in page HTML: `deepseek-flash`, `deepseek-v4-pro`, `deepseek-v4-flash`, `deepseek-v4-flash-vision-exp`.
- Cross-check (OpenRouter + wiki event page `events/2026-10-17-deepseek-v4.1-flash-1017-release.md`): DeepSeek-V4.1-Flash-1017 listed at **$0.15 in / $0.60 out, 1M ctx** (unchanged from V4.1-Flash); deepseek-v4-pro OpenRouter $1.60/$3.20.
- DeepSeek official peak/off-peak numbers could NOT be re-verified via curl this run — V4-Flash/V4-Pro wiki rows carried forward as previously verified 2026-08-17.

## Cross-check summary

All Anthropic/Google figures above were also spot-checked against `openrouter.ai/api/v1/models` (claude-opus-5.5 $4/$20, claude-sonnet-5.5 $2/$10, claude-haiku-5.5 $0.10/$0.50, claude-fable-5.1 $10/$50, gemini-4-argon $2/$10, gemini-3.8-flash $0.83/$4.12 [OR markup]).
