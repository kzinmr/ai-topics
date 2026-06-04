---
title: "Token Economics — LLM Inference Cost & Optimization"
type: concept
created: 2026-04-18
updated: 2026-06-04
tags:
  - inference
  - optimization
  - economics
  - methodology
aliases: ["cost-per-token", "inference-unit-economics"]
sources: [raw/newsletters/2026-05-28-altman-walks-back-job-apocalypse.md, raw/articles/2026-05-27_jayagup10_token-budget-wars.md, "[[raw/articles/2026-06-03_solo-ai-agency-kimi-2-6]]", "[[raw/articles/2026-06-03_glean_token-yield-architecture]]"]
---

# Token Economics

LLM inference cost analysis, optimization layers, and the economics of running language models at scale. A prerequisite concept for [[concepts/context-engineering]].

## The Great Inversion

Training was the primary cost center (2021–2023). **Inference now consumes 55–80% of enterprise AI GPU spend.** Training is a fixed compute job; inference costs accumulate indefinitely post-launch.

## Core Metric: Cost Per Million Tokens (CPM)

```
CPM = (GPU $/hr) / (tokens_per_sec × 3600 / 1,000,000)
```

### GPU Comparison (Llama 3.1 70B, FP16, Batch 256)

| GPU | $/hr (On-Demand) | Throughput | CPM |
|---|---|---|---|
| A100 80G SXM4 (8x) | $8.40 | ~1,400 tok/s | ~$1.67 |
| H100 SXM5 (8x) | $19.20 | ~2,800 tok/s | ~$1.90 |
| H100 FP8 quant (8x) | $19.20 | ~5,200 tok/s | ~$0.95-1.10 |
| B200 SXM6 (8x) | $59.44 | ~5,200 tok/s | ~$3.18 |

**Key insight:** A100 has the lowest FP16 CPM, but **H100 wins with FP8 quantization** (~$0.95-1.10 CPM) by doubling throughput without changing $/hr.

## API Pricing Landscape (Dec 2025)

LLM inference costs declined **10x annually** — faster than PC compute or dotcom bandwidth. GPT-4 equivalent performance now costs $0.40/million tokens vs $20 in late 2022.

| Tier | Model | Input ($/M) | Output ($/M) |
|------|-------|-------------|-------------|
| Budget | Gemini Flash-Lite | $0.075 | $0.30 |
| Mid-Tier | Claude Sonnet 4 | $3.00 | $15.00 |
| Frontier | Claude Opus 4.5 | $5.00 | $25.00 |
| Disruptor | DeepSeek R1 | $0.55 | $2.19 |

Provider variation: identical models vary **10x** across providers ($0.90 → $9.50/M tokens).

## Four Optimization Layers (Apply in Order)

### 1. Model Layer (30–75% Cost Reduction)
- **FP8 Quantization (H100):** 1.3–2x throughput gain, <2% quality loss
- **FP4 Quantization (B200):** +1.5–2x gain over FP8
- **INT4 (GPTQ/AWQ):** Fits 70B model on single H100, cuts 8-GPU pod to 2–3 GPUs
- **Distillation:** 70B → 14B cuts GPU needs 4–8x
- **Right-Sizing:** 14B at FP8 often matches 70B at INT4 on standard NLP tasks

### 2. Runtime Layer (40–80% Throughput Gain)
- **Continuous Batching (vLLM/PagedAttention):** Utilization from 15–30% → 60–80% (3–4x effective throughput)
- **Speculative Decoding:** Small draft model generates candidates, large target verifies in parallel. 2–4x gain for output-heavy workloads
- **KV Cache Optimization:** INT8/FP8 quantization cuts VRAM 30–50% for 32k+ contexts

### 3. Infrastructure Layer (40–65% Unit Cost Reduction)
- **Spot vs On-Demand:** On-demand for sync APIs (sub-2s P99); spot for batch/async
- **Auto-Scaling Trigger:** Scale by pending request queue depth (>50 req/GPU), not CPU/memory
- **GPU Right-Sizing:** 14B FP8 on 1x H100 PCIe ($2.01/hr) can outperform 4x A100 SXM4 ($4.20/hr)

### 4. FinOps Layer (Prevents Waste Accumulation)
- Tag at submission: `model_name`, `use_case_id`, `team/product`
- Emit token metrics: compute CPM weekly
- Budget alerts at 80% (not 100%)
- Review cadence: weekly for inference, monthly for training

## Breakeven Analysis

| Model | Utilization to Beat API | Minimum Scale |
|-------|------------------------|---------------|
| 7B | ~50% | — |
| 13B | ~10% | — |
| Any self-hosted | — | >8,000 conv/day |

**Compounding effect:** Quantization (4x) + Continuous Batching (2x) + Speculative Decoding (2x) ≈ **16x effective cost reduction**.

## Real-World Case Study: $39K → $16K/Month

Llama 3.1 70B, 500 DAU, peak 9am-6pm weekdays:

| Metric | Before | After |
|--------|--------|-------|
| Monthly GPU Cost | ~$29,200 | ~$14,951 |
| GPU Utilization | 22% | 68% |
| Total Monthly Spend | ~$39,100 | ~$16,151 |

Applied: FP8 quantization, continuous batching, spot instances for batch jobs, provider switch to eliminate egress fees. **Net savings: 59%.**

## API vs Self-Host Decision

**Choose API when:** sporadic/unpredictable traffic, <8,000 conv/day, limited engineering capacity
**Choose Self-Host when:** consistent high-volume traffic, >50% sustainable GPU utilization, data sovereignty requirements
**Hybrid (optimal for most):** Route baseline to self-hosted; overflow to APIs during spikes


## The Inference Capacity Gap (Epoch AI, May 2026)

Epoch AI has warned of a growing gap between global inference capacity and token demand:

> "The next bottleneck is not whether models can answer questions—it's whether the world can serve enough fast, high-quality inference."

Key concerns:
- **Agentic workloads** (long-context, multi-turn) consume orders of magnitude more inference compute than simple Q&A
- **Token demand** for agentic applications is growing faster than inference infrastructure can scale
- The shift from single-turn to multi-turn interactions creates a **compounding demand effect** — each agent session may consume 100-1000× the tokens of a single API call
- Inference capacity is geographically concentrated, creating **latency and sovereignty bottlenecks** for global agent deployment

The Epoch AI analysis reframes the inference capacity discussion from "how cheap can inference get?" to "can infrastructure scale faster than agent-driven demand?"

## Token-to-Outcome Attribution (Marginal Token Utility)

Beyond raw token pricing and optimization, enterprises face a deeper challenge: connecting inference spend to business outcomes. See [[concepts/token-to-outcome-attribution]] for the full framework. Key concepts:

- **Marginal token utility**: The business value created by each additional dollar of inference. Most companies cannot see this number.
- **Token budget wars** (Jaya Gupta, May 2026): Enterprises are shifting from "is AI useful?" to "where is AI actually creating leverage?" — the fight for ownership of token allocation.
- **Retry tails**: Workflow completion rate drops from 90% to 70% → effective cost rises ~28% due to compounding failures.
- **Context inflation**: Doubling context length roughly quadruples reasoning cost (O(n²) attention). Systems routinely over-supply.
- **Routing waste**: Easy classification tasks running on frontier models — across millions of calls, the cost difference is often the difference between manageable and board-level problem.

The fundamental insight: two enterprises with identical token bills can be running completely different operations — one converting inference into outcomes, the other paying for thrash that looks identical on the line item.

## AI Spend vs Labor: BPO as Benchmark (Jaya Gupta, May 2026)

The enterprise conversation is shifting from "cost per token" to **"cost per completed outcome"**:
- BPO contracts are already priced in completed units (per ticket, claim, invoice, review) — making them the easiest AI comparison baseline
- Internal labor is harder to benchmark: productivity gains show up as avoided hiring or diffuse capacity, not eliminated headcount
- A claim requiring three retries, human correction, and a frontier model may be more expensive than the outsourced labor it was supposed to replace

## Solo AI Agency Economics (June 2026)

A real-world case study of token economics enabling a new business model — a solo operator running a $40k MRR AI automation agency with zero employees. The entire delivery engine runs on AI inference at ~$350/month.

| Metric | Value | Notes |
|--------|-------|-------|
| **Monthly revenue** | $40,000 | 14 clients across 3 retainers |
| **Kimi 2.6 inference** | ~$240/month | 90% of all production work |
| **Premium model (Opus)** | ~$110/month | 10% high-stakes work |
| **Total AI inference** | ~$350/month | Replaces 3-5 person team |
| **Infrastructure + SaaS** | ~$400/month | Hosting, platform, CRM |
| **Effective margin** | >90% | ~$39k take-home on $40k revenue |

**Key insight:** The cost of delivering the work fell through the floor while the value clients pay stayed exactly the same. The same production load on a frontier model would cost $1,500-$5,000+/month and hit rate limits — collapsing the business model. The margin exists because the delivery runs on an economics-appropriate model (Kimi 2.6 at $0.50/$2 per million), not because of clever pricing.

**Implications:** This validates the token economics thesis at the extreme — when inference is cheap enough, headcount stops being leverage and becomes a liability. The agency with 20 employees isn't more powerful than the solo operator with a sharp system; it's slower, heavier, and running on a fraction of the margin.

Source: [[raw/articles/2026-06-03_solo-ai-agency-kimi-2-6]]

## Token Yield — An Architecture Problem (Glean, June 2026)

A reframing of token economics from Glean: enterprises need a better metric than raw token usage. The right question is not how many tokens a system consumes, but what useful outcome the system produces per token consumed — **token yield**.

### Problem Scope

Enterprise AI token spend is scaling quickly (Deloitte: average 36% of digital initiative budgets to AI; Ramp: 4x YoY increase; Uber burned through its entire 2026 AI coding budget in 4 months), but business value is not rising at the same rate. Token yield is fundamentally an **architecture** question, not just a model question — because token usage is shaped by the full system around the model: how context is retrieved, how tools are exposed, how work is decomposed, how models are routed, and how prior execution is reused.

### Four Architectural Levers

| # | Lever | Problem | Solution |
|---|-------|---------|----------|
| 1 | **Context quality** | Noisy retrieval forces reasoning over irrelevant data → token bloat | Retrieve better, not more. Centralized indexes cut tokens ~50% vs off-the-shelf MCP tools (83k vs 43k tokens for same task) |
| 2 | **Model routing** | Frontier model default for every step → paying premium for routine work | Right-size model per step. Operational work (search, planning, validation) doesn't need frontier reasoning |
| 3 | **Continual learning** | Solving the same class of problem from scratch every time → repeated exploratory cost | Accumulate execution traces. Skip failed paths. Each completed task should improve the economics of the next related one |
| 4 | **Harness design** | Naive harness keeps expanding context window → cost grows with workflow | Scope tools to current step. Distribute across specialized agents. Externalize intermediate state. Give each model only the working set it needs |

### Glean vs Off-the-Shelf MCP Benchmark

In a Claude Cowork-style task evaluation, Glean's centralized enterprise index was:
- Preferred **2.5x** as often as off-the-shelf MCP tools
- Off-the-shelf MCP tools consumed ~30% more tokens
- When MCP tools won on correctness, they needed **83k tokens vs 43k** for Glean

Poor context architecture forces the system to compensate with more tool calls, more reasoning loops, and more over-fetching — a hidden tax that compounds across every task.

### Key Insight

> "The real AI moat is execution efficiency." The agencies/enterprises that win won't be those with the best models — they'll be those that extract the most useful work per token through superior architecture.

Source: [[raw/articles/2026-06-03_glean_token-yield-architecture]]

## Hidden Self-Hosting Costs

ML engineering (quantization, sharding, containers), infrastructure management, observability, continuous tuning. Requires specialized expertise beyond raw hardware costs.

## Related

- [[concepts/context-engineering]] — Token economics is a prerequisite for understanding context window optimization trade-offs
- [[concepts/local-llm]] — Self-hosting economics and optimization techniques
- [[concepts/local-llm/model-quantization]] — Quantization methods (GPTQ, AWQ, EXL2, FP8)
- [[concepts/inference/vllm]] — Continuous batching and PagedAttention

## Sources

-  — Spheron & Introl inference economics analysis- Sebastian Raschka, "A Visual Guide to Attention Variants in Modern LLMs" (Ahead of AI)
