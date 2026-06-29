---
title: Poolside
created: 2026-04-29
updated: 2026-06-29
type: entity
tags: [company, model, coding-agents]
sources:
  - raw/newsletters/2026-04-28-builders.md
  - raw/newsletters/2026-06-28-latest-open-artifacts-22-zyphra-cohere-and-poolside-are-expanding-the-breadth-of.md
---

# Poolside

**Poolside** is a foundation model lab focused on **agentic coding models**. As of April 2026, it has publicly shipped its first models and products.

## Key Products & Models

### Laguna Model Family (April 2026)

| Model | Total Params | Activated | Type | License |
|-------|-------------|-----------|------|---------|
| **Laguna M.1** | 225B | 23B | MoE | Apache 2.0 |
| **Laguna XS.2** | 33B | 3B | MoE | **Apache 2.0** (open-weight) |

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
