---
title: "Moonshot Kimi K3"
type: concept
created: 2026-07-17
updated: 2026-07-21
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
  - "raw/newsletters/2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8-class-at-.md"
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
| Active Parameters | **~50B** (16 of 896 experts, <2% activation ratio) |
| Context Window | **1M tokens** |
| Reasoning Efforts | Only "max" (no lower effort levels) |
| Attention Mechanism | Kimi Delta Attention (KDA) — up to 6.3x faster decoding |
| Training Innovation | Attention Residuals (AttnRes) — ~25% higher efficiency |
| MoE Architecture | LatentMoE / Stable LatentMoE |
| Activation Function | SiTU (Sigmoid Tanh Unit) |
| Optimization | Per-head Muon, QB/Quantile Load Balancing |
| Hidden System Prompt | ~85 tokens suspected |
| Multimodality | Vision input supported |
| Predecessor | [[concepts/kimi-k2-6\|Kimi K2.6]] (1T, Apr 2026) |

The model is more than **2× the parameter count** of Kimi K2.6's 1T architecture. Active parameter count has not been disclosed as of announcement.

## Innovation Details

### Kimi Delta Attention (KDA)

KDA is Moonshot's novel attention mechanism purpose-built for long-context efficiency. Moonshot claims it enables **up to 6.3x faster decoding** in million-token contexts. The design reportedly started in **January 2025** and took approximately **1.5 years** to reach frontier-class scale.

**vLLM Integration**: Moonshot contributed a KDA prefix caching implementation directly to vLLM, with support available from day 0. This was notable because KDA breaks assumptions behind conventional prefix caching, requiring upstream runtime changes to the vLLM codebase.

### Attention Residuals (AttnRes)

AttnRes is Moonshot's training efficiency innovation, claimed to deliver **~25% higher training efficiency at less than 2% additional cost**. It is used in conjunction with KDA to enable scaling of the non-standard attention stack.

### Community-Identified Architecture Details

From Moonshot's technical blog and community analysis, additional architectural components were identified:

- **LatentMoE / Stable LatentMoE**: The mixture-of-experts implementation with **16 activated experts out of 896 total** — an activation ratio of under 2%.
- **SiTU (Sigmoid Tanh Unit)**: A novel activation function used in the model architecture.
- **Per-head Muon**: Muon optimizer applied per attention head.
- **QB / Quantile Load Balancing**: Load balancing technique for expert utilization.

The combination of KDA + LatentMoE + AttnRes at 2×+ scale over K2.6 was noted by architecture observers as a notable engineering achievement — scaling a non-standard attention stack into a frontier-class model.

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

### Arena.ai Agent Arena Results

Kim K3 achieved standout results in Arena's human-preference evaluations, especially in code domains:

| Arena | Ranking | Score | Detail |
|-------|---------|-------|--------|
| **Frontend Code** | **#1** | **1679 pts** | Jumps from #18 (K2.6) to #1; #1 in 6/7 frontend domains, #2 in Gaming |
| **Text Arena** | #9 | 1486 pts | Jumped from #38; top-10 in creative writing, coding, instruction following |
| **Pairwise Win Rate** | — | **76%** | vs 63% for Claude Fable 5, 58% for GPT-5.6 Sol |

The Frontend Code result was especially prominent because it is a **pairwise human-preference arena**, not a static benchmark — real users preferred K3's frontend code output over all competitors. Multiple user reports showed K3 generating complex web experiences (CS:GO × Portal clone in 3 shots / ~600K tokens / $3.24, web DOS emulator running near 1M context over hours).

### Artificial Analysis Detailed Evaluation

| Metric | Score | Comparison |
|--------|-------|------------|
| **AA Intelligence Index** | **57** | Comparable to Opus 4.8 and GPT-5.5; behind Fable 5 and GPT-5.6 Sol |
| **GDPval v2** | 1668 / 1687 | Above Opus 4.8; behind GPT-5.6 Sol (1747.8) |
| **AutomationBench-AA** | **53% / #1** | Top score |
| **AA-Briefcase (Elo)** | 1547 | +732 from K2.6 |
| **Cost per task** | $0.94 | GPT-5.6 Sol: $1.04; Opus 4.8: $1.80 |
| **Token efficiency** | 21% fewer output than K2.6 | 132M vs 166M tokens across full Intelligence Index |
| **AA-Omniscience accuracy** | **46%** (+18 pts) | vs 33% on K2.6 |
| **AA-Omniscience hallucination** | **51%** (−12 pts) | **Worsened** from 39% on K2.6 |

The hallucination rate regression on AA-Omniscience was flagged as a real weakness despite accuracy gains, and was noted by multiple independent evaluators.

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

## Serving & Infrastructure

| Metric | Value |
|--------|-------|
| **Serving speed** (OpenRouter) | ~26–28 tok/s |
| **Reference deployment** | 64+ accelerator supernode |
| **vLLM support** | KDA prefix caching, day 0 |
| **API cached input** | 90% discount ($0.30/1M tokens) |

Observed serving speeds via Moonshot API/OpenRouter were noted as slower than Opus, with speculation that speculative decoding was not yet enabled. Moonshot's blog reportedly recommends **supernode configurations with 64+ accelerators** for best inference efficiency.

The practical deployability of a 2.8T open-weight model was a recurring theme: open weights do not guarantee cheap self-hosting, and frontier infrastructure territory (64+ accelerator guidance) limits practical deployment to well-funded teams.

## Caveats & Controversies

### Benchmark Metric Criticism

**ProgramBench** author Ofir Press objected to Moonshot's metric choice, noting that averaging implementation percentage (rather than counting fully working programs) can overstate usefulness. This inflates partial-credit performance relative to fully working programs.

**Bindu Reddy** warned that K3's benchmark story might be overstated unless validated on hidden/uncontaminated evals like LiveBench, and argued that if the model "thinks forever" on every request, real cost per task could be less favorable.

### Hallucination Regression

Despite accuracy improvements (+18 pts on AA-Omniscience), the model's hallucination rate **worsened from 39% to 51%** — a significant regression that undermines reliability for knowledge-work tasks.

### "Thinks Forever" Risk

Multiple users noted K3 currently appears to "think a lot," preserve long reasoning history, and may require more careful harness support than simpler chat-first APIs. Its "max-only" reasoning effort means every request pays for full reasoning, making the model expensive for simple tasks.

## Community Reaction

K3's launch was widely framed as a **"DeepSeek moment"** for open-source AI — the first time an open model demonstrated competitiveness with top closed models at scale. Key themes:

- **US-China competition**: Many commentators tied K3 to export controls and the narrowing gap between Chinese open labs and US closed labs, arguing K3 weakens the narrative that Chinese models trail by 6–8 months
- **Open model milestone**: "This is no longer 'good for open source' — it's simply competitive with top public closed models"
- **Systems story**: The launch was notable not just for raw capability but for scaling a non-standard attention stack — KDA + AttnRes + sparse MoE at frontier level
- **Counterweight**: Capability parity is not full-stack parity; product reliability, inference scale, and deployment margins may still favor US incumbents
- **Paradox**: Open weights at 2.8T do not mean cheap to run — practical deployability requires frontier infrastructure

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

## Market Analysis: Commodity Intelligence Thesis (Stratechery, July 2026)

Ben Thompson's Stratechery analysis ["Who's Afraid of Chinese Models?"](https://stratechery.com/2026/whos-afraid-of-chinese-models/) uses K3 as the lens for a broader structural argument about the AI industry:

### COGS vs R&D Distinction
- Open-weight models are **not free** — they eliminate R&D costs but not COGS (cost of goods sold)
- Running inference on K3 costs real money: $3/M input, $15/M output tokens
- Revenue directly correlates with COGS in a way that hasn't been true for software since the pre-cloud era

### Tokens ≠ Intelligence
- Jensen Huang's "token factory" framing (tokens-per-second, tokens-per-watt) made sense in the ChatGPT era
- In the reasoning era, **tokens are not a commodity** — different models need different token counts to reach the same answer
- K3 reportedly uses significantly more tokens than Sol (GPT-5.6), potentially negating its price advantage
- What IS fungible is **intelligence** — the correct answer, regardless of token count

### COGS for Intelligence
The cost of producing intelligence depends on five factors:
1. **Model footprint**: Weights and runtime state → memory/accelerator requirements
2. **Inference efficiency**: Architectural choices (MoE) reduce per-token computation
3. **Memory efficiency**: KV cache optimization → more concurrent requests
4. **Serving efficiency**: Batching, scheduling, prefix caching → better GPU utilization
5. **Token efficiency**: Fewer tokens to correct answer → lower inference cost

### Implications
- Intelligence for many economically beneficial tasks is becoming a **commodity**
- In a commodity market, the route to profitability is through **superior cost structure**, not higher prices
- This analysis suggests the AI industry may follow traditional industrial economics more than software economics — marginal costs are back

> **Source**: [Stratechery — Who's Afraid of Chinese Models?](https://stratechery.com/2026/whos-afraid-of-chinese-models/) (July 2026)

## Related Pages

- [[entities/kimi]] — Kimi model family overview
- [[entities/moonshot-ai]] — Moonshot AI company details
- [[concepts/kimi-k2-6]] — Previous generation (1T, Apr 2026)
- [[concepts/kimi-k2-7-code]] — Coding-optimized variant (Jun 2026)
- [[comparisons/llm-api-pricing]] — Cross-provider pricing comparison
- [[concepts/open-model-consortium]] — Open model ecosystem
