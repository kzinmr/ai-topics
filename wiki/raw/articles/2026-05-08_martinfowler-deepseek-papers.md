---
title: "The DeepSeek Series: A Technical Overview"
source: "Martin Fowler"
url: "https://martinfowler.com/articles/deepseek-papers.html"
date: 2026-05-08
type: analysis
tags: [deepseek, scaling-laws, mixture-of-experts, fp8-training, grpo, hpc]
scraped: 2026-05-08
---

# The DeepSeek Series: A Technical Overview (Martin Fowler)

## Summary

Martin Fowler's analysis traces DeepSeek's LLM evolution from Jan 2024 to Jan 2025, framed around **HPC Co-Design**: simultaneous optimization of model architecture and hardware infrastructure.

## Four Papers in Series

1. **DeepSeek-LLM (Jan 2024)**: Scaling laws — redefined scale as non-embedding FLOPs/token (M). Data quality justifies larger model for same tokens. 67B model trained on 2T bilingual tokens, outperformed LLaMA-2 70B.

2. **DeepSeek-V2 (Jun 2024)**: Architectural efficiency — Multi-Head Latent Attention (MLA) for KV cache compression, DeepSeekMoE with shared+routed experts, device-limited routing to overcome H800 interconnect limits.

3. **DeepSeek-V3 (Dec 2024)**: 671B params, 14.8T tokens, 2.8M H800 GPU hours. FP8 mixed precision, DualPipe, auxiliary-loss-free load balancing.

4. **DeepSeek-R1 (Jan 2025)**: Emergent reasoning via pure RL (GRPO). R1-Zero (no SFT) → self-verification, reflection, "aha moments". R1 multi-stage pipeline.

## Three Research Arcs

| Arc | Key Technologies |
|-----|-----------------|
| **Efficiency** | MLA (KV compression), FP8 training, DualPipe |
| **Sparsity** | DeepSeekMoE, Device-limited routing, Auxiliary-loss-free gating |
| **Reasoning** | GRPO, Rule-based rewards, Multi-stage RL/SFT pipelines |

## Core Philosophy: HPC Co-Design

DeepSeek builds model architectures specifically to exploit (and work around) the limitations of underlying HPC hardware. This is the unifying thread: every architectural decision is paired with a corresponding infrastructure innovation.
