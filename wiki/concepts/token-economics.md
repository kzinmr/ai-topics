---
title: "Token Economics — LLM Inference Cost & Optimization"
type: concept
created: 2026-04-18
updated: 2026-04-18
tags: [inference, optimization, cost, technique]
aliases: ["cost-per-token", "inference-unit-economics"]
sources: []
---

# Token Economics

LLM inference cost analysis, optimization layers, and the economics of running language models at scale. A prerequisite concept for [[context-engineering]].

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

## Hidden Self-Hosting Costs

ML engineering (quantization, sharding, containers), infrastructure management, observability, continuous tuning. Requires specialized expertise beyond raw hardware costs.

## Related

- [[context-engineering]] — Token economics is a prerequisite for understanding context window optimization trade-offs
- [[local-llm]] — Self-hosting economics and optimization techniques
- [[concepts/local-llm/model-quantization.md]] — Quantization methods (GPTQ, AWQ, EXL2, FP8)
- [[concepts/inference/vllm.md]] — Continuous batching and PagedAttention

## Sources

-  — Spheron & Introl inference economics analysis
- Sebastian Raschka, "A Visual Guide to Attention Variants in Modern LLMs" (Ahead of AI)
