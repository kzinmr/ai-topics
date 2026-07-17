---
title: "Moonshot Kimi K3"
type: concept
created: 2026-07-17
updated: 2026-07-17
tags:
  - model
  - china
  - open-source
  - reasoning
  - moe
  - moonshot
  - kimi
  - frontier-models
sources:
  - "raw/articles/simonwillison.net--2026-jul-16-kimi-k3--ac21263e.md"
---

# Moonshot Kimi K3

## Overview

**Kimi K3** is Moonshot AI's most capable model to date, announced July 16, 2026. With **2.8 trillion total parameters** (rounded up to 3T by Moonshot), it is positioned as the first "open 3T-class model" — more than twice the size of its predecessor [[concepts/kimi-k2-6|Kimi K2.6]] (1T). The model is currently available via kimi.com and the Moonshot API, with an **open weight release promised by July 27, 2026**.

K3 represents a significant pricing tier shift for Chinese AI labs: at **$3/M input and $15/M output**, it is the most expensive model from a Chinese provider to date, pricing at the same level as Anthropic's Claude Sonnet series.

## Architecture & Specifications

| Specification | Value |
|---------------|-------|
| Organization | [[entities/moonshot-ai\|Moonshot AI]] |
| Model Type | Mixture of Experts (MoE) |
| Total Parameters | **2.8 Trillion** (marketed as "3T-class") |
| Active Parameters | TBD |
| Context Window | TBD |
| Reasoning Efforts | Only "max" (no lower effort levels) |
| Hidden System Prompt | ~85 tokens suspected |
| Multimodality | Vision input supported |
| Predecessor | [[concepts/kimi-k2-6\|Kimi K2.6]] (1T, Apr 2026) |

The model is more than **2× the parameter count** of Kimi K2.6's 1T architecture. Active parameter count has not been disclosed as of announcement.

## Benchmarks

Kimi K3's self-reported benchmarks position it firmly in the frontier tier:

| Benchmark | K3 Result | Notes |
|-----------|-----------|-------|
| vs Claude Opus 4.8 max | **Wins most** | Competitive with top non-ultra-premium models |
| vs GPT-5.5 high | **Wins most** | Outperforms OpenAI's previous flagship |
| vs Claude Fable 5 | **Loses** | Anthropic's ultra-premium model still leads |
| vs GPT-5.6 Sol | **Loses** | OpenAI's latest flagship still ahead |

### Artificial Analysis Evaluation

- **Long-horizon knowledge work Elo**: 1547 (+732 from K2.6)
- **Ranking**: Behind only Claude Fable 5 on this evaluation
- **Cost per task**: $0.94 (similar to GPT-5.6 Sol at $1.04; ~½ of Opus 4.8 at $1.80)
- **Token efficiency**: 21% fewer output tokens than K2.6

### Arena.ai Frontend Code

K3 is the **#1 model on Arena.ai's Frontend Code arena**, surpassing even Claude Fable 5 — a notable achievement for a non-Anthropic model in a code-focused evaluation.

## Pricing

| Metric | Value | Comparison |
|--------|-------|------------|
| Input tokens | **$3.00/M** | Same as Claude Sonnet 4.6/5 |
| Output tokens | **$15.00/M** | Same as Claude Sonnet 4.6/5 |
| Cost per task (AA eval) | **$0.94** | GPT-5.6 Sol: $1.04, Opus 4.8: $1.80 |
| Predecessor pricing | K2.6 at $0.95/$4.00 | K3 is ~3× input, ~3.75× output |

This pricing makes K3 the **most expensive model from a Chinese AI lab**, matching the [[comparisons/llm-api-pricing|Claude Sonnet pricing tier]]. It represents Moonshot's confidence in frontier-class quality.

## Pelican Benchmark Analysis

Simon Willison's standard pelican SVG generation test (via OpenRouter):

| Metric | Value |
|--------|-------|
| Input tokens | 95 |
| Output tokens | 16,658 |
| Reasoning tokens | 13,241 (~80% of output) |
| Total cost | **$0.25** |

Notable observations:
- Only one reasoning effort level available: **"max"** — no lighter/cheaper option
- This means every request pays for full reasoning, making the model expensive for simple tasks
- Vision input works well; alt text generation is high quality
- ~85 token hidden system prompt suspected

## Open Weight Status

K3 is **not yet open weight** as of July 16, 2026. Moonshot has committed to releasing open weights **by July 27, 2026**. This would make it the largest open-weight model available, surpassing DeepSeek's 1.6T V4 Pro.

Prior Moonshot open-weight releases (K2, K2.5, K2.6) have used a **Modified MIT License** requiring attribution for products exceeding 100M monthly users or $20M monthly revenue.

## Competitive Position

K3 slots into a new tier for Chinese models — frontier-class pricing with frontier-class benchmarks:

| Competitor | Comparison |
|-----------|-----------|
| **Claude Fable 5** ($10/$50) | K3 loses benchmarks but is 3× cheaper |
| **GPT-5.6 Sol** ($5/$30) | K3 loses benchmarks but is cheaper |
| **Claude Opus 4.8** ($5/$25) | K3 wins most benchmarks at lower price |
| **GPT-5.5** ($5/$30) | K3 wins most benchmarks at lower price |
| **Claude Sonnet 4.6/5** ($3/$15) | K3 matches pricing, likely superior quality |
| **DeepSeek V4 Pro** ($0.44/$0.87) | DeepSeek far cheaper but lower quality tier |
| [[concepts/kimi-k2-6\|Kimi K2.6]] ($0.95/$4) | K3 is successor; 2× params, 3×+ pricing |

The pricing strategy suggests Moonshot believes K3's quality justifies Sonnet-level economics, marking a shift from the "cheaper Chinese alternative" positioning of prior Kimi models.

## Related Pages

- [[entities/kimi]] — Kimi model family overview
- [[entities/moonshot-ai]] — Moonshot AI company details
- [[concepts/kimi-k2-6]] — Previous generation (1T, Apr 2026)
- [[concepts/kimi-k2-7-code]] — Coding-optimized variant (Jun 2026)
- [[comparisons/llm-api-pricing]] — Cross-provider pricing comparison
- [[concepts/open-model-consortium]] — Open model ecosystem
