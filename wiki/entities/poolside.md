---
title: Poolside
created: 2026-04-29
updated: 2026-07-24
type: entity
tags: [company, model, coding-agents]
sources:
  - raw/newsletters/2026-04-28-builders.md
  - raw/newsletters/2026-06-28-latest-open-artifacts-22-zyphra-cohere-and-poolside-are-expanding-the-breadth-of.md
  - raw/articles/2026-07-24_poolside-latent-space.md
  - raw/articles/2026-07-24_ainews-laguna-s21.md
---

# Poolside

**Poolside** is a foundation model lab focused on **agentic coding models**. As of April 2026, it has publicly shipped its first models and products.

## Key Products & Models

### Laguna Model Family (April 2026)

| Model | Total Params | Activated | Type | License |
|-------|-------------|-----------|------|---------|
| **Laguna M.1** | 225B | 23B | MoE | Apache 2.0 |
| **Laguna XS.2** | 33B | 3B | MoE | **Apache 2.0** (open-weight) |

### Laguna S 2.1 (July 2026)

| Model | Total Params | Active Params | Type | Context | License |
|-------|-------------|---------------|------|---------|--------|
| **Laguna S 2.1** | 118B | 8B | MoE | 1M tokens | OpenMDW-1.1 |

Laguna S 2.1 is Poolside's most capable model to date, notable for:
- **Architecture**: 118B total parameter MoE with 8B activated per token.
- **Context window**: Up to 1M tokens — significantly larger than the Laguna M.1 (131K).
- **Thinking modes**: Supports both thinking and no-thinking modes per request.
- **Benchmarks**: Outperforms DeepSeek V4 Flash on agentic coding tasks while being cheaper; competitive with Thinking Machines models ~10× its size. Reddit community assessment: \"Cheaper than Deepseek v4 Flash, Better than V4 Pro.\"
- **Deployment**: Small enough to run on a single NVIDIA DGX Spark; supported on OpenRouter and various inference providers.
- **License**: OpenMDW-1.1 — Poolside explicitly framed open-weight releases as a way to avoid intelligence concentration in 'three or four companies.'
- **Ecosystem**: Amplified by infra partners including @DannieHerz, @tuhinone, @ctnzr; GGUF quantized versions available on HuggingFace.

**Laguna XS.2** is Poolside's first open-weight release, notable for:
- **Architecture**: 40 layers total, with 10 global attention + 30 sliding window attention layers (3:1 ratio). Sigmoid gating with per-layer rotary scales.
- **Experts**: 256 experts with 1 shared expert.
- **KV Cache**: FP8 quantization for reduced memory per token.
- **Context window**: 131,072 tokens.
- **Reasoning**: Native interleaved thinking between tool calls, with enable/disable per request.
- **Performance**: 44.5% on SWE-bench Pro, 30.1% on Terminal-Bench 2.0.
- **Deployment**: Runs on a single GPU (e.g., Mac with 36GB RAM via Ollama).

### Product Previews

- **pool**: Terminal-based coding agent.
- **Shimmer**: Cloud development experience for iterating on web apps, APIs, and CLIs.

## Background

Poolside has been building an internal **"Model Factory"** over several years, encompassing proprietary data pipelines, training stack, and agent infrastructure. Their initial focus was on **public sector deployments** with strict security requirements (on-prem, air-gapped).

The April 2026 Laguna release marked their first public shipping of foundation models. In June 2026, Poolside released Laguna M.1 under Apache 2.0, affirming that open weights are now their default. "Open weights are now our default. We'll keep building toward the frontier and releasing increasingly capable models in the open."

## Training Stack

- **Optimizer**: Muon (not AdamW)
- **Data**: 30T tokens for Laguna XS.2, with data automixing and async off-policy agent RL
- **Post-training**: Agent reinforcement learning for agentic coding capabilities

## Model Factory

Poolside operates an internal 'Model Factory' capable of 10,000–20,000 experiments per month (detailed in Latent Space podcast with Eiso Kant, July 2026). Key capabilities:
- **Streaming data**: Data is streamed directly into training pipelines without batch pre-processing bottlenecks.
- **Reproducible experimentation**: Infrastructure designed for reproducible ML experiments at scale.
- **Agentic training**: AI agents increasingly write code, launch jobs, evaluate results, and modify the pipelines used to train future models — a closed-loop self-improvement system.
- **Low-precision compute**: Optimized for low-precision training without quality degradation.
- **Rapid iteration**: Can take a model from pre-training to release in approximately 8 weeks.
- **Data automixing**: Dynamic mixing of training data sources during training.
- **Agent RL**: Asynchronous off-policy agent reinforcement learning for post-training.

## Relationships

- [[entities/openai]] — Competes in the agentic coding space
- [[entities/anthropic]] — Competes in the agentic coding space
- [[entities/nvidia]] — Working with NVIDIA on model development
- [[concepts/harness-engineering]] — Poolside's approach to agentic coding models
- [[concepts/serving-llms-vllm]] — Laguna XS.2 supported on vLLM (PR #41129)

## Sources

- [Poolside Blog: Introducing Laguna XS.2 and M.1](https://poolside.ai/blog/introducing-laguna-xs2-m1) (April 2026)
- [Poolside Blog: A Deeper Dive](https://poolside.ai/blog/laguna-a-deeper-dive)
- [HuggingFace: poolside/Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)
- [Ollama: Laguna XS.2](https://ollama.com/library/laguna-xs.2)
- [Ben's Bites: Building gets easier (Apr 30, 2026)](https://open.substack.com/pub/bensbites/p/building-gets-easier)
