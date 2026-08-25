---
title: "Moonshot Kimi K3"
created: 2026-07-17
updated: 2026-08-24
type: concept
tags:
  - model
  - china
  - open-source
  - reasoning
  - moonshot
  - kimi
sources:
  - "raw/articles/simonwillison.net--2026-jul-16-kimi-k3--ac21263e.md"
  - "raw/newsletters/2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8-class-at-.md"
  - "raw/articles/2026-07-24_together-ai-kimi-k3-vs-fable-deepswe.md"
  - "raw/articles/together.ai--blog-kimi-k3-vs-gpt-5-6-sol-on-deepswe-cost-coding-and-routi--a97a06f4.md"
  - "raw/articles/simonwillison.net--2026-jul-27-kimi-k3--f8e3d6fa.md"
  - "raw/articles/modal.com--blog-kimi-k3-by-moonshot-now-available-on-modal--66112a1a.md"
  - "raw/articles/2026-07-28_fireworks-ai_kimik3-on-fireworks.md"
  - "raw/newsletters/2026-07-28-ainews-much-ado-about-open-weights.md"
  - "raw/articles/2026-07-28_fireworks-ai_K3-LoRA-Training.md"
  - "raw/articles/2026-07-29_unsloth_kimi-k3-local-inference.md"
  - "raw/articles/together.ai--blog-kimi-k3-guide--70e2c263.md"
  - "raw/newsletters/2026-08-03-kimi-k3-the-manos-the-mythos-the-legendos.md"
  - "raw/articles/2026-08-01_wafer-ai_kimi-k3-amd-mi355x-serving-benchmark.md"
---

# Moonshot Kimi K3

## Overview

**Kimi K3** is Moonshot AI's most capable model to date, announced July 16, 2026. With **2.8 trillion total parameters** (rounded up to 3T by Moonshot), it is positioned as the first "open 3T-class model" — more than twice the size of its predecessor [[concepts/kimi-k2-6|Kimi K2.6]] (1T). Open weights were released on schedule on **July 27, 2026** (1.56TB on Hugging Face), with day-0 support from Modal, Fireworks AI, and OpenRouter.

K3 represents a significant pricing tier shift for Chinese AI labs: at **$3/M input and $15/M output**, it is the most expensive model from a Chinese provider to date, pricing at the same level as Anthropic's Claude Sonnet series.

## Architecture & Specifications

| Specification | Value |
|---------------|-------|
| Organization | [[entities/moonshot-ai\|Moonshot AI]] |
| Model Type | Mixture of Experts (MoE) |
| Total Parameters | **2.8 Trillion** (marketed as "3T-class") |
| Active Parameters | **~50B** (16 of 896 experts, <2% activation ratio) |
| Context Window | **1M tokens** |
| Reasoning Efforts | low, high, max (default: max) |
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

#### KDA Lineage: From Linear Attention to Gated DeltaNet (Aug 2026)

SemiAnalysis traced the mathematical origins of KDA, deriving it from a lineage of linear attention variants:

1. **Linear attention**: removing the softmax operation allows reordering of operations, reducing attention's computational complexity from quadratic to linear in sequence length
2. **DeltaNet**: improves on linear attention by changing the loss function to minimize the **L2 norm of the value retrieval** — the Delta Rule becomes the basis of DeltaNet's attention equation (an online-learning interpretation of key-value storage)
3. **Gated DeltaNet (GDN)**: adds a gating mechanism on top of DeltaNet's delta rule, improving memory retention and selective recall
4. **KDA**: Moonshot's productionized evolution of this lineage, scaled to frontier-class 2.8T MoE alongside AttnRes and LatentMoE

**FlashKDA**: the algorithm's high-performance implementation is available as open source at [MoonshotAI/FlashKDA](https://github.com/MoonshotAI/FlashKDA), providing the fused kernel-level implementation details behind the 6.3x decoding speedup claims.

Source: SemiAnalysis, "Kimi K3, The Manos, The Mythos, The Legendos" (Aug 2026).

### Attention Residuals (AttnRes)

AttnRes is Moonshot's training efficiency innovation, claimed to deliver **~25% higher training efficiency at less than 2% additional cost**. It is used in conjunction with KDA to enable scaling of the non-standard attention stack.

### Community-Identified Architecture Details

From Moonshot's technical blog and community analysis, additional architectural components were identified:

- **LatentMoE / Stable LatentMoE**: The mixture-of-experts implementation with **16 activated experts out of 896 total** — an activation ratio of under 2%.
- **SiTU (Sigmoid Tanh Unit)**: A novel activation function used in the model architecture.
- **Per-head Muon**: Muon optimizer applied per attention head.
- **QB / Quantile Load Balancing**: Load balancing technique for expert utilization.

The combination of KDA + LatentMoE + AttnRes at 2×+ scale over K2.6 was noted by architecture observers as a notable engineering achievement — scaling a non-standard attention stack into a frontier-class model.

## Developer Features (Together AI Guide, Aug 2026)

### Reasoning Effort Control
K3 now supports three reasoning effort levels via `reasoning_effort`: `low`, `high`, and `max` (default). Thinking can also be disabled entirely with `reasoning={"enabled": False}` for instant-mode responses. Thinking tokens are billed as output at $15/M, so setting `reasoning_effort` appropriately for task complexity is important for cost control.

### Preserved Thinking
K3 was trained in **preserved thinking history mode** — the reasoning trace from one turn becomes state that the next turn depends on. Developers can replay `reasoning_content` from previous assistant turns to maintain context across multi-turn conversations. Dropping the trace causes the model to invent fresh reasoning each turn, losing accumulated context.

### Dynamic Tool Loading
K3 supports placing complete tool definitions inside system messages with a `tools` field and no content. This enables **on-demand tool injection**: declare a lightweight search function at conversation start, then inject full tool definitions based on retrieval results. Appending dynamic declarations to the end of messages does not affect the cached prefix.

### Structured Output
Supports `response_format` with `json_schema` and `strict: true`. The `json_object` mode also works for syntactically valid JSON. Important: keep `max_tokens` generous because the entire thinking trace is spent before the first schema-constrained token is emitted.

### Vision
Native vision input with multiple images per request. No limit on image count, but total request body must stay under 100 MB. Recommended max resolution: 4K (4096×2160).

Source: [[raw/articles/together.ai--blog-kimi-k3-guide--70e2c263.md]]

## Benchmarks

Kimi K3's self-reported benchmarks position it firmly in the frontier tier:

| Benchmark | K3 Result | Notes |
|-----------|-----------|-------|
| vs Claude Opus 4.8 max | **Wins most** | Competitive with top non-ultra-premium models |
| vs GPT-5.5 high | **Wins most** | Outperforms OpenAI's previous flagship |
| vs Claude Fable 5 | **Loses** | Anthropic's ultra-premium model still leads |
| vs GPT-5.6 Sol | **Loses** | OpenAI's latest flagship still ahead |

**Cyber milestone (The Signal, Aug 23 2026):** Kimi K3 became the **first open-weight model** that cybersecurity evaluator **Irregular** has seen solve challenges on its cyber-scenario benchmark — a notable open-weights milestone, though it still trails the closed frontier on the same benchmark.

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

### DeepSWE Benchmark (Together AI, July 2026)

Together AI ran 452 DeepSWE rollouts comparing Kimi K3 (max effort) vs Claude Fable 5 (xhigh) on 113 real-world, long-horizon feature requests from live open-source repos. DeepSWE tests software engineering capability across multiple task types and programming languages, graded pass/fail by a hidden test suite.

| Metric | Kimi K3 | Claude Fable 5 | Notes |
|--------|---------|----------------|-------|
| **pass@1** | 68.5% | **69.9%** | Fable leads by 1.4 points |
| **pass@2** | **82.0%** | 80.2% | K3 pulls ahead |
| **pass@4** | **89.4%** | 88.5% | K3 best of any flagship-tier config |
| **Coverage** (≥1 solve) | **89.4%** (101/113) | 88.5% (100/113) | K3 reaches more tasks |
| **4/4 Reliability** | 45 tasks | **58 tasks** | Fable more deterministic |

#### Cost Comparison (DeepSWE)

| Metric | Kimi K3 | Claude Fable 5 |
|--------|---------|----------------|
| Cost per rollout | **$4.65** | $13.41 |
| Full 452-rollout sweep | **$2,103** | $6,010 |
| Solves per $100 | **14.7** | 5.3 |

**2.8x cost efficiency**: Kimi K3 delivers 2.8x more solved tasks per dollar than Claude Fable 5 on DeepSWE.

#### Key Findings

- **Pass@k advantage**: While Fable wins pass@1 on single-attempt reliability, Kimi K3 wins pass@2 and pass@4 — making it the stronger choice for retry-tolerant agent workflows where multiple attempts are acceptable.
- **High cross-vendor similarity**: Per-task correlation between K3 and Fable is 0.72 — the highest cross-vendor similarity in the entire DeepSWE benchmark. Both models succeed and fail on nearly the same tasks (96 shared solves, 8 shared failures), meaning pairing them buys almost no diversity.
- **Coverage vs. reliability tradeoff**: K3 reaches more tasks (broader coverage, only 12 never-cracked tasks) but is less deterministic (fewer 4-for-4 solves). Fable is steadier on any single attempt despite slightly narrower coverage.
- **Language strengths**: K3 wins Go decisively (79 vs 71). Fable leads Python, JavaScript, TypeScript, and Rust — though K3 catches up significantly on Rust, closer than any other model including GPT-5.6 Sol.
- **Failure patterns match**: 65% of failures are near misses for both models, and both protect the repo's existing test suite equally well (11% vs 10% baseline regressions).

> **Source**: [Together AI — Kimi K3 vs Claude Fable 5 on DeepSWE: Cost and Coding](https://www.together.ai/blog/kimi-k3-vs-claude-fable-5-on-deepswe-cost-and-coding) (July 24, 2026)

#### DeepSWE vs GPT-5.6 Sol (Together AI, July 26, 2026)

Together AI ran 904 graded rollouts (113 tasks × 4 trials each) comparing Kimi K3 (max effort) vs GPT-5.6 Sol on DeepSWE. GPT-5.6 Sol took the pass@1 crown with 72.7%, but Kimi K3 wins on pass@k for k > 1 while costing significantly less per rollout.

| Metric | Kimi K3 | GPT-5.6 Sol | Notes |
|--------|---------|-------------|-------|
| **pass@1** | 68.5% | **72.7%** | Sol leads by 4.2 points |
| **pass@2** | **82.0%** | 81.0% | K3 pulls ahead |
| **pass@4** | **89.4%** | 85.8% | K3 best pass@4 on the board |
| **Coverage** (≥1 solve) | **89.4%** (101/113) | 85.8% (97/113) | K3 reaches more tasks |
| **4/4 Reliability** | 76.6% (45 tasks) | **84.5%** (61 tasks) | Sol more deterministic |
| **Cost per rollout** | **$4.65** | $8.37 | K3 44% cheaper per rollout |
| **Solves per $100** | **14.7** | 5.3 | **2.8x more solves per dollar** |
| **Median rollout time** | 66 min | **17 min** | Sol ~4x faster |
| **Open weights** | **Yes** | No | |

**Per-task correlation: 0.46** — significantly lower than K3 vs Fable (0.72), meaning the two models succeed and fail in genuinely different ways. This makes them a strong routing pair.

#### Routing: Kimi K3 → GPT-5.6 Sol Cascade

Because the two models disagree on 18 of 113 tasks, a **Kimi-first cascade with verifier** (run K3, escalate to Sol when tests fail) achieves **~85.6% accuracy**, covering **108/113 tasks** — beating either model alone and even a perfect one-shot router (83.4%). This is cheaper than Sol alone since Kimi clears ~70% of the queue before Sol is invoked.

| Routing Strategy | Accuracy | Cost/task |
|------------------|----------|-----------|
| Best single model (Sol) | 72.7% | $8.37 |
| Perfect oracle router | 83.4% | ~$6.07 |
| **Cascade: K3 → Sol on failure** | **85.6%** | $7.30 |
| Both models, keep either | 85.6% | $13.02 |

The hard ceiling for this pair is 95.6% (5 tasks solved by neither model). Past that, a third model is needed.

#### Language Breakdown (Kimi K3 vs GPT-5.6 Sol)

| Language | Winner | Score |
|----------|--------|-------|
| **Go** | Tie | 79–79 |
| **Python** | Sol | 74–68 |
| **TypeScript** | Sol | 66–60 |
| **JavaScript** | Sol | 75–65 |
| **Rust** | **Kimi K3** | 65–60 |

#### Failure Mode Differences

The models fail in very different ways: **GPT-5.6 Sol** breaks the repo's existing baseline tests in 20% of failures (consistent with other GPT models). **Kimi K3** has only 11% baseline test failures but **65% near misses** where >80% of new tests pass but some fail — K3 gets close but doesn't fully pass, while Sol is more likely to break existing functionality.

> **Source**: [Together AI — Kimi K3 vs GPT-5.6 Sol on DeepSWE: Cost, Coding, and Routing](https://www.together.ai/blog/kimi-k3-vs-gpt-5-6-sol-on-deepswe-cost-coding-and-routing) (July 26, 2026)

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
- Reasoning effort now supports three levels: **low**, **high**, and **max** (default) — though at launch only "max" was available
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

Multiple users noted K3 currently appears to "think a lot," preserve long reasoning history, and may require more careful harness support than simpler chat-first APIs. Its default "max" reasoning effort means most requests pay for full reasoning unless explicitly reduced.

## Community Reaction

K3's launch was widely framed as a **"DeepSeek moment"** for open-source AI — the first time an open model demonstrated competitiveness with top closed models at scale. Key themes:

- **US-China competition**: Many commentators tied K3 to export controls and the narrowing gap between Chinese open labs and US closed labs, arguing K3 weakens the narrative that Chinese models trail by 6–8 months
- **Open model milestone**: "This is no longer 'good for open source' — it's simply competitive with top public closed models"
- **Systems story**: The launch was notable not just for raw capability but for scaling a non-standard attention stack — KDA + AttnRes + sparse MoE at frontier level
- **Counterweight**: Capability parity is not full-stack parity; product reliability, inference scale, and deployment margins may still favor US incumbents
- **Paradox**: Open weights at 2.8T do not mean cheap to run — practical deployability requires frontier infrastructure

## Open Weight Status

**Released July 27, 2026** — Moonshot delivered on schedule. The weights are **1.56TB on Hugging Face** ([`moonshotai/Kimi-K3`](https://huggingface.co/moonshotai/Kimi-K3)), making K3 the largest open-weight model available, surpassing DeepSeek's 1.6T V4 Pro.

### Licensing Evolution

K3's license marks a significant departure from K2's Modified MIT:

- **K2 (Jul 2025)**: "Modified MIT" — added a paragraph requiring attribution ("Kimi K2" on UI) for products with >100M MAU or >$20M monthly revenue
- **K3 (Jul 2026)**: No longer calls itself "modified MIT." Requires a **separate agreement with Moonshot AI** for any "Model as a Service" business exceeding $20M aggregate revenue over any consecutive 12 months

Moonshot consistently uses the term "open weight" (not "open source") in their own materials, acknowledging the license is not OSI-compliant.

> **Source**: [Simon Willison — moonshotai/Kimi-K3](https://simonwillison.net/2026/Jul/27/kimi-k3/) (Jul 27, 2026)

## Day-0 Inference Providers

K3's open-weight release triggered immediate availability across major inference platforms:

### Modal
- **460 tokens/sec** on release day via custom **DFlash** speculator tuned to K3's architecture
- 360% faster interactivity (100→460 tok/s), 88% higher throughput (800K→1.5M TPM/GPU)
- DFlash training: 32 B300 nodes (28 running K3 at TP8 for hidden states, 4 training draft model)
- Day 0 vLLM integration thanks to Moonshot's upstream KDA prefix caching contribution
- Shared API ($30/mo free tier) + dedicated Auto Endpoints

> **Source**: [Modal Blog — Kimi K3 by Moonshot now available on Modal](https://modal.com/blog/kimi-k3-by-moonshot-now-available-on-modal) (Jul 27, 2026)

### Fireworks AI
- US-hosted, zero data retention
- Day-0 training for K3 serving
- Competes directly with Opus 5 on benchmarks (K3 vs Opus 5 comparison published)

> **Source**: [Fireworks AI — Kimi K3 on Fireworks](https://fireworks.ai/blog/kimik3-on-fireworks) (Jul 27, 2026)

### OpenRouter
- Available from **7 providers** at launch
- Consistent pricing: $3/M input, $15/M output (matching Moonshot's own rates)

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

## Distillation Allegations (July 2026)

### White House Accusation
US Tech & Science Advisor Michael Kratsios (@mkratsios47) publicly alleged that Moonshot AI engaged in "large-scale, covert industrial distillation" of Anthropic's Fable to build Kimi K3. The accusation cited:
- Access to NVIDIA GB300 clusters in Thailand as the mechanism
- Dismissed Moonshot's claims of architectural innovation (KDA, AttnRes) as "minor modifications" atop copied weights

### Pushback and Open Questions
- Critics noted the lack of public evidence — no benchmark similarity analysis, weight comparison, or training data forensics was presented
- Moonshot's existing contributions (KDA in vLLM, AttnRes paper) argued against wholesale theft — building those innovations would be unnecessary if weights were simply copied
- The accusation came amid broader Trump administration efforts to restrict Chinese AI models (Axios, July 2026)

### Ecosystem Impact
- **ClinePass adoption**: K3 went from 0% to 16% token usage in 3 days, becoming its #3 most-used open-weight model, per @cline
- **Policy response**: Administration officials framed the incident as evidence for stronger AI model export controls and provenance tracking
- **IP concerns**: Legal observers noted the difficulty of proving distillation without model weight access, and questioned whether trade secret claims could hold given Fable's public deployment via API
- **Paradoxical effect**: The allegations may accelerate adoption — demanding provenance gives K3 more attention, and ban attempts may drive users toward decentralized hosting

### LoRA Training on Fireworks

In July 2026, [[entities/fireworks-ai|Fireworks AI]] made K3 available for **Multi-LoRA serving and training** via its Serverless Training platform. This marked one of the first production-grade LoRA customization offerings for a 2.8T-parameter open-weight model.

**Pricing and Performance**: Pay-per-token pricing for training runs is competitive — approximately **$65 for a small RL run** (20 steps, 860K training tokens, completing in 30–60 minutes). LoRA adapters themselves are cheap to train (megabytes in size) and can be served in two modes:

- **Live merge**: Adapter weights are merged into the base model at load time with no inference overhead
- **Multi-LoRA**: Multiple adapters share a single base deployment, enabling many specialized behaviors without per-adapter infrastructure

**KV-Cache Efficiency**: Fireworks' KV-cache-aware serving architecture means multi-turn agent runs bill at **20% of the standard prefill rate**, significantly reducing cost for conversational and agentic workloads.

**Demonstration Use Cases**:

- **Countdown** (dense reward): Teaches the model a new objective function via a dense reward signal that provides feedback at every step. The model learns to maximize a continuous score, demonstrating fine-grained behavioral steering.
- **Frozen Lake** (sparse reward): Teaches a tool-calling loop via a sparse reward signal that only fires when the agent reaches the goal. The model must discover the correct multi-step strategy through exploration, with reward only at completion.

**Key Insight**: "The reward is the lever that decides what the model is aiming at" — dense vs sparse reward design significantly affects learning curves and determines which behaviors the model internalizes during post-training.

**Numerics Alignment**: Training and inference use consistent numerical representations, ensuring that behavior observed during LoRA training transfers faithfully to production serving without quantization drift or precision mismatch.

**The Post-Training Flywheel**: This capability enables a complete feedback loop:
1. **Train** a LoRA adapter on a specific task or domain
2. **Deploy** with zero overhead via live merge or Multi-LoRA
3. **Monitor** production behavior and collect real-world feedback
4. **Collect** new training data from observed failures or edge cases
5. **Re-train** the adapter with improved data, closing the loop

This infrastructure makes [[concepts/post-training]] practical for ongoing model improvement and enables the [[concepts/lora|LoRA]]-based customization paradigm that many enterprises require for production deployment.

## Local Inference (Unsloth) — July 2026

[[entities/unsloth|Unsloth]] released Dynamic GGUF quantizations enabling Kimi K3 to run on consumer-accessible hardware. Key quant tiers:

| Quant | Size (GB) | Top-1 Accuracy | Perplexity | Hardware Requirement |
|-------|-----------|----------------|------------|---------------------|
| **UD-IQ1_S** | 594 | 78.9% | 2.58 | 610 GB (Mac Studio + 128GB RAM) |
| UD-IQ1_M | 649 | 81.2% | 2.36 | 665 GB |
| UD-IQ2_XXS | 711 | 84.1% | 2.13 | 726 GB |
| UD-Q2_K_XL | 861 | 90.4% | 1.74 | 880 GB |
| UD-Q4_K_XL | 1,510 | ~99% | 1.46 | 1.5 TB (near-full precision) |
| UD-Q8_K_XL | 1,560 | Lossless | 1.46 | 1.6 TB (truly lossless vs MXFP4) |

**Key findings**:
- 1-bit Dynamic GGUF shrinks K3 from 1.56TB → **594GB (62% smaller)** while retaining ~79% accuracy
- 2-bit at 861GB achieves **90% accuracy** while being 45% smaller
- Community quants are dramatically worse: IQ1_M at 619GB achieved 54.56 PPL (21× worse than Unsloth's 594GB IQ1_S)
- Unsloth required a custom llama.cpp fork for K3 vision support (mmproj with RMSNorm, non-square fused QKV, post-norm projector)

**Deployment options**:

- **Unsloth Studio**: Open-source web UI with automatic RAM offloading, multi-GPU detection, self-healing tool calling, code execution, and Cloudflare HTTPS tunneling
- **llama.cpp**: Custom fork required (`unslothai/llama.cpp#48`); supports CUDA, Metal, and CPU inference
- **Hardware**: DGX Station or Mac Studio with 128GB+ RAM; best speed/quality tradeoff at IQ1_S (594GB)
- **Inference speed**: ~20 tok/s on B200s, >120 tok/s throughput

K3 is thinking-only with `preserve_thinking` always enabled. Thinking effort: low/high/max. Context: 1M tokens. Default params: temp=1.0, top_p=0.95 (chat) / top_p=1.0 (agentic).

**Source**: [[raw/articles/2026-07-29_unsloth_kimi-k3-local-inference.md|Unsloth Docs — Kimi K3 How to Run Locally]], [GGUF on HuggingFace](https://huggingface.co/unsloth/Kimi-K3-GGUF)

## AMD MI355X Serving Performance — August 2026

In August 2026, [[entities/wafer-ai|Wafer]] published a serving benchmark demonstrating Kimi K3 running on a single 8-GPU AMD MI355X node at production-grade throughput. This is significant because K3 requires **16× NVIDIA B200 GPUs across two servers** due to memory constraints, but fits within **one 8× MI355X node** thanks to AMD's higher HBM capacity per GPU.

### Why Single-Node Matters

| Factor | NVIDIA B200 | AMD MI355X | Implication |
|--------|------------|------------|-------------|
| **GPU memory** | 192 GB HBM3 | 288 GB HBM3e | MI355X's 50% more HBM enables single-node deployment |
| **GPUs needed** | 16 (2 nodes) | 8 (1 node) | No inter-node communication overhead |
| **Node memory** | 1,536 GB/node | 2,304 GB/node | Full model (~1.5 TB) fits in one AMD node |

### Performance Benchmarks

| Metric | AMD MI355X (8-GPU, 1 node) | NVIDIA B200 (16-GPU, 2 nodes) | MI355X Advantage |
|--------|---------------------------|-------------------------------|-----------------|
| **Aggregate throughput** | **952 tok/s** | ~250 tok/s | **3.8×** |
| **Single-stream decode** | **118 tok/s** | ~91 tok/s | **1.3×** |
| **Perf/$ (vs B300)** | **48 tok/s/$** | 33 tok/s/$ | **1.45×** |

The 3.8× aggregate throughput advantage stems primarily from eliminating inter-node communication — a single 8-GPU node communicates via intra-node interconnects (Infinity Fabric) rather than network-bound inter-node links. The 1.3× single-stream advantage reflects AMD's per-GPU HBM bandwidth and compute efficiency for large-batch decode.

### Implications

- **AMD's HBM capacity advantage** translates directly to TCO wins for frontier MoE model serving, where model footprint dominates deployment topology
- **Single-node frontier serving** simplifies deployment, reduces networking costs, and eliminates the tail-latency risks of multi-node inference
- This benchmark validates AMD's MI355X as a viable alternative to NVIDIA B200/B300 for large open-weight model inference, particularly for models like K3 where memory capacity is the binding constraint
- The result aligns with AMD's broader strategy of competing on memory capacity and total cost of ownership in the inference market

**Source**: [[raw/articles/2026-08-01_wafer-ai_kimi-k3-amd-mi355x-serving-benchmark.md|@wafer_ai — Kimi K3 on AMD MI355X Benchmark]] (Aug 1, 2026)


## Related Pages

- [[entities/kimi]] — Kimi model family overview
- [[entities/moonshot-ai]] — Moonshot AI company details
- [[concepts/kimi-k2-6]] — Previous generation (1T, Apr 2026)
- [[concepts/kimi-k2-7-code]] — Coding-optimized variant (Jun 2026)
- [[comparisons/llm-api-pricing]] — Cross-provider pricing comparison
- [[concepts/open-model-consortium]] — Open model ecosystem
