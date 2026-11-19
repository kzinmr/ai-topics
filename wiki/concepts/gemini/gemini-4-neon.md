---
title: "Gemini 4 Neon"
created: 2026-11-19
updated: 2026-11-19
type: concept
tags: [google, deepmind, google-deepmind, model, multimodal, model-release, coding-agent, reasoning-model]
related:
  - concepts/gemini/gemini-4-carbon
  - concepts/gemini/index
  - concepts/frontier-models-comparison-april-2026
sources:
  - raw/articles/2026-11-18_blog.google_gemini-4-neon.md
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
  - https://news.ycombinator.com/item?id=50552424
confidence: medium
---

# Gemini 4 Neon

**Gemini 4 Neon** is Google DeepMind's November 2026 frontier model, positioned as the fast, price-efficient sibling in the Gemini 4 lineup (alongside Carbon, Argon, Hydrogen). Announced Nov 18, 2026 by Koray Kavukcuoglu (SVP, Google DeepMind / Chief AI Architect). It is pitched as "frontier-level intelligence with fast end-to-end task completion" across software engineering, knowledge work, and science.

## Headline numbers (Google-reported)

- **#3 overall** on the Artificial Analysis Intelligence Index at xhigh thinking level, score **61** — "just behind larger, slower models" (a16z/AI-analysis: comparable to GPT-6.2 Sol but more expensive).
- **#2** on the Vals Index (70.9%), on the Pareto frontier.
- **#1** on Legal Research Bench and Tax Agent Bench; **#1** on most Surge AI categories (finance, accounting, spreadsheet modeling, constraint following).
- **#2 globally** on Arena's Agent Arena Index (1336, across 4,200+ real agent sessions); **#2 on steerability** (mid-task corrections).
- **73.5%** Chartography, **75.8%** Agents' Last Exam v1.1, **#1** on Zapier AutomationBench (56.3%), **#1** on Andon Labs Vending-Bench 2 ($16,843).
- Lowest fabrication rate yet in internal Google Antigravity testing.

## Pricing & availability

- **$3 / 1M input tokens** ($0.15 / 1M cached input = 95% discount), **$15 / 1M output**.
- **1M-token context window.**
- Rolling out: Gemini API, AI Studio, Gemini for business, Google Antigravity (Pro/Ultra), Gemini app (Pro/Ultra).

## Positioning in the lineup

Community (HN) mapping of the Gemini 4 family: **XL** = Carbon/Argon, Astra, Fable; **L** = Neon, Sol, Opus; **M** = Hydrogen, Terra, Sonnet; **S** = Helix(rumored), Luna, Haiku. Neon is widely read as the successor to 3.1 Pro — better and cheaper than the recent Carbon on price-performance, which raised "is Carbon already deprecated?" questions (Google's own lineup page clarifies their distinct roles).

## Third-party speed thesis (micjm)

micjm modeled the Agent Duel leaderboard (model identity + speed + early-voting interaction) and projected Neon at **Elo ~1,066**, just below Opus 5.5 (1,078) — projected to win 48.3% of duels vs Opus. Key driver: **127 tokens/sec on OpenRouter vs Carbon's 46 tps** — "speed is about as important as model identity." onlyrealcuzzo (HN): "might actually be as good as Opus 5.5 … latency by far the best for the level of quality; ~2x more expensive than Sol 6.2 but significantly better and faster."

## Reception / criticism (HN, 866 pts)

- **Naming confusion**: "Credit to Google for outdoing OpenAI and Anthropic in choosing a confusing naming convention" (3wolf); "which model am I supposed to use for what?" (ariwilson).
- **Entitlement friction**: multiple users (mrbungie, ariwilson) reported student / $20-plan accounts cannot access the new models in Antigravity — a recurring access-complaint vs OpenAI/Anthropic.

## Related

- [[concepts/gemini/gemini-4-carbon]] — the cyber-defense-oriented Gemini 4 flagship
- [[concepts/gemini/index]] — full Gemini family
- [[concepts/frontier-models-comparison-april-2026]]

## Sources

- [Introducing Gemini 4 Neon — Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)
- [HN discussion](https://news.ycombinator.com/item?id=50552424)
- [micjm — Gemini 4 Neon looks like an Opus 5.5 competitor](https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model/)
