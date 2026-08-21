---
title: "OpenRouter — GPT-5.6 Sol model page (50% discount listing)"
url: https://openrouter.ai/openai/gpt-5.6-sol
date: 2026-08-17
fetched_at: 2026-08-21
source: openrouter.ai
tags: [openrouter, openai, gpt, pricing, model, token-economics]
hn: "632 points / 448 comments on HN (2026-08-17, https://news.ycombinator.com/item?id=49337602)"
extraction: partial_js_blocked — page is Next.js; facts extracted from embedded RSC JSON payload
---

# GPT-5.6 Sol — 50% off on OpenRouter (August 17, 2026)

## What happened

On **August 17, 2026**, OpenRouter's GPT-5.6 Sol model page displayed a **"50% off $5.00"** badge — GPT-5.6 Sol input pricing cut from **$5.00 to $2.50 per 1M tokens** (output from $15 to $7.50) — via a provider-level discount on the OpenAI route. The story hit HN front page at **632 points / 448 comments** with the title "GPT-5.6 Sol Pricing Cut by 50% on OpenRouter".

## Verified facts (from the page's embedded data)

- **Discount**: `"discount": 0.5` on the OpenAI provider variant — 50% off. `display_pricing` confirms: $5.00 → struck-through, new price applied.
- **Scope**: The discount applies **only to the OpenAI-hosted provider on OpenRouter**. Azure, Amazon Bedrock, and other OpenRouter providers for the same model show `"discount": 0` (unchanged pricing).
- **Official OpenAI API pricing unchanged**: HN commenters confirmed `developers.openai.com/api/docs/models/gpt-5.6-sol` still shows $5/$15 — this is a **channel-specific promotion**, not a list-price cut.
- **Vercel AI Gateway offered the same 50% off** (vercel.com changelog: "GPT-5.6 Sol is 50% off on AI Gateway").
- **Model facts** (unchanged): 1,050,000 token context window; up to 128,000 completion tokens; supports reasoning, tool calling, structured outputs; model permaslug `openai/gpt-5.6-sol-20260709`; release date 2026-07-09 (GA).
- **High-context tier**: above 272K prompt tokens, pricing jumps (prompt $5→$10, completion $15→$22.50 at list; 2× multiplier).

## Context: the GPT-5.6 family price trajectory

- **June 26-27, 2026**: GPT-5.6 family announced (Sol $5/$30, Terra $2.50/$15, Luna $1/$6) in a restricted preview.
- **July 9, 2026**: GA.
- **July 30, 2026**: OpenAI cut prices — Luna -80% to $0.20/$1.20, Terra -20% to $2/$12; Sol-driven inference optimization cut serving costs ~20%.
- **August 17, 2026**: Sol -50% on OpenRouter (and Vercel) only → **$2.50/$7.50** effective via those channels.

So the effective Sol price dropped from $5/$15 (GA list) to $2.50/$7.50 (OpenRouter channel) in under six weeks.

## HN discussion themes (from thread, https://news.ycombinator.com/item?id=49337602)

- **"Who is subsidizing this, and why?"** — consensus: OpenAI is the funder (OpenRouter attributes the promotion to OpenAI via X); OpenRouter takes a flat fee and does not run sales itself. Vendors selling cheaper through third-party channels than first-party is called "weird" but common (Apple/Amazon retail sales analogy).
- **Strategy theories**: (a) price-A/B testing through a third party before an official cut; (b) market-share capture on OpenRouter (the de-facto public usage leaderboard) ahead of IPO narrative; (c) market segmentation — OpenRouter users are price-sensitive, enterprise API/Bedrock/Azure customers stay at list; (d) funneling users from competing models (Kimi K3, Grok 4.6) at the new price point; (e) flex-tier steering hypothesis (OpenRouter routing Sol users to the already-discounted flex tier).
- **ZDR (zero data retention) gap**: the discount applies to the standard OpenAI route; users with ZDR-only toggles on OpenRouter do **not** get the discount. Fable/Mythos (Anthropic) do not offer ZDR at all, and several commenters noted Anthropic's frontier models are banned in some enterprises specifically due to retention terms.
- **Competition**: commenters framed the cut as "opening salvos of an all-out token price war" — open-weight Chinese models (DeepSeek V4-Flash at ~$0.18/1M, Kimi K3, GLM 5.2) have been forcing frontier-lab price discipline; "reasoning as a service is looking more and more like a commodity."
- **Usage skepticism**: one commenter with OpenRouter token telemetry noted GPT-5.6 Sol usage was "unchanged on the day" of the cut (~101B tokens/day the prior day), and that OpenRouter does not do private inference.

## Significance for the wiki

- This is the **first major channel-exclusive price cut on a frontier model**: a lab's flagship discounted 50% through a third-party gateway while its own API list price stays put. It establishes **gateway-level promotions** (OpenRouter, Vercel AI Gateway) as a new pricing instrument, distinct from both list-price cuts and subscription plans.
- Ties to [[entities/openrouter]] (Stripe acquisition context: OpenRouter becoming a payment/routing rail) and [[concepts/gpt/gpt-5-6]] (price-performance frontier section).
- The ZDR carve-out illustrates the fragmentation of inference privacy tiers (ZDR vs standard vs frontier-model exclusions).

## Sources

- https://openrouter.ai/openai/gpt-5.6-sol (scraped 2026-08-21; 50% badge + RSC pricing JSON)
- https://news.ycombinator.com/item?id=49337602 (632 pts, discussion of scope/funding)
- https://vercel.com/changelog (same 50% off on Vercel AI Gateway)
- https://x.com/OpenRouter/status/2089416739398254662 (OpenRouter attributing promotion to OpenAI, per HN comments)
