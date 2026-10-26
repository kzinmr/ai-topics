---
title: "LLM Price Collapse 2026 (OpenAI–Anthropic Tit-for-Tat)"
created: 2026-10-26
updated: 2026-10-26
type: concept
tags: [concept, token-economics, ai-economics, openai, anthropic, open-weight, inference-api, business-model]
sources:
  - raw/articles/minimaxir.com--2026-10-cheap-llms--c10a2b50.md
confidence: medium
---

# LLM Price Collapse 2026 (OpenAI–Anthropic Tit-for-Tat)

Between June and October 2026, effective frontier LLM prices fell by up to **80% within months** through a tit-for-tat of price cuts between OpenAI and Anthropic, under pressure from open-weight models and a commoditized inference-provider market. Max Woolf (minimaxir) analyzes the mechanism (2026-10-24, HN 328 pts).

## The price-cut timeline (input / output / cache-read per MTok)

| Date | Event | Price |
|---|---|---|
| Jun 26 | GPT-5.6 Sol/Luna launch | $5/$30/$0.50 · $1/$6/$0.10 |
| Jun 30 | Claude Sonnet 5 launch pricing (meant to be temporary) | $2/$10/$0.20 |
| Jul 24 | Claude Opus 5 | $5/$25/$0.50 |
| Jul 30 | **OpenAI cuts GPT-5.6 Luna 80%** | $0.20/$1.20/$0.02 |
| Aug 10 | Anthropic makes Sonnet 5 cut permanent | — |
| Aug 21 | GPT-5.6 Sol cut ~20% (3 months) | $4/$20/$0.40 |
| Sep 1 | Claude Fable 5.1 — **cache read cut 75%** ($1 → $0.25) | $10/$50/$0.25 |
| Sep 3 | GPT-6 Astra (no cache discount) | $10/$50/$1 |
| Sep 22 | **GPT-6 Sol at half GPT-5.6 Sol's price**; same day Claude Opus 5.5 ("requires less compute to serve") | $2/$10/$0.20 · $4/$20/$0.20 |
| Sep 29 | GPT-6.1 Sol (after GPT-6 Sol dud) — cache halved again → cumulative −75% | $2/$10/$0.10 |

Two structural observations:

- **Cache read is where the war is.** In agentic coding, cache reads are **96–99% of token spend** (the cache holds the whole prior conversation each turn) with 90–100% hit rates — so Fable 5.1's 75% cache-read cut ≈ 70–75% real cost reduction. Both labs converged on cache read = 5% of input price. See [[concepts/prompt-caching]].
- **The cuts are reciprocals.** Each cut follows a competitor move by days; Luna's 80% cut is read as a direct answer to DeepSeek V4 Flash's $0.0028 cache read.

## Why 80% cuts are sustainable (the externality)

1. **Commoditization + zero switching cost.** A harness toggle (OpenCode, Zed) or an OpenRouter endpoint string swaps models; "sufficient substitutes" exist from Google, Meta, and open-weight labs.
2. **Inference-provider competition.** DeepSeek V4.1 Flash 1017 (AA index 45 vs 24) is hosted by **29 distinct OpenRouter providers**, with Cloudflare and DeepInfra within 10% of DeepSeek's own effective cost. Providers won't serve unprofitable models — so market price trends to marginal cost, capping what the labs can charge. This is the "loss-leading will reverse to monopoly pricing" thesis's missing premise: OpenAI/Anthropic are not a duopoly and inference has low barriers to entry.
3. **Genuine efficiency gains.** Opus 5.5's "less compute to serve" claim is credible; Vercel AI gateway data shows cost-per-token down to **43.3% of April 2026** while *aggregate spend rises* — models improve faster than they cheapen (Jevons-style rebound; cf. [[events/the-plunging-price-of-thought-epoch-sep-2026]]'s 47%/quarter measurement).

## IPO angle

Both labs are rumored to IPO (Anthropic within months, OpenAI 2027) while leaking billions in losses — cutting the primary revenue line 80% before an S-1 is "the opposite of what you'd want." Counterpoint: reported inference gross margins as healthy as ~80%, plus margin re-capture via subscriptions: OpenAI simultaneously cut Codex $200-tier usage allowance 50% "to reflect our increasingly efficient models." Woolf's own behavior illustrates weak demand elasticity in the labs' preferred direction — 4× more efficient usage led him to cut his plan quota to 1/5, net-neutral spend. Also flagged: Opus 5.5 obsoleted Fable 5.1/GPT-6 Astra discussion entirely within a month — deliberate self-cannibalization has no observed cost so far.

Open question worth tracking: if inference gets *too* efficient, does that undercut the data-center buildout thesis ([[concepts/ai-native-demand-indicators]])?

## Related

- [[comparisons/llm-api-pricing]] — living price table (weekly monitor)
- [[concepts/token-economics]]
- [[concepts/open-weight-vs-closed-llm-gap]] — Kimi K3.1 Pro at $2/$10/$0.20, AA 55 vs Opus 5.5's 58
- [[events/the-plunging-price-of-thought-epoch-sep-2026]]
- [[concepts/ai-benchmarks/benchmaxxing]]
- [[entities/openrouter]]

## Sources

- [OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why? — Max Woolf, minimaxir (2026-10-24)](https://minimaxir.com/2026/10/cheap-llms/) — raw: `raw/articles/minimaxir.com--2026-10-cheap-llms--c10a2b50.md`
