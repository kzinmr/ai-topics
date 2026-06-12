---
title: 'GRPO Memory Modeling'
type: concept
created: 2026-06-12
updated: 2026-06-12
tags: [reinforcement-learning, grpo, training, memory-efficiency, optimization]
sources:
  - url: https://x.com/sheriyuo/status/2063295181131247674
    title: 'RL Interview Questions 2026 — Q20'
    date: 2026-06-06
  - url: https://newsletter.semianalysis.com/p/scaling-reinforcement-learning-environments-reward-hacking-agents-scaling-data
    title: 'SemiAnalysis: Scaling RL'
    date: 2026-06-10
---

# GRPO Memory Modeling

A breakdown of how many model copies live in GPU memory during [[grpo]] training, and which optimizations can reclaim the most space.

## Model Copies During Training

| Role | Purpose | Optimizer States? | Always Present? |
|------|---------|-------------------|-----------------|
| **Actor** | Policy being trained | Yes | Yes |
| **Reference** | Frozen copy for KL penalty | No | Yes (unless β=0) |
| **Reward model** | Scores completions | No | Only if learned rewards |
| **Rollout engine** | Generates completions | No | May share actor weights |

**Total: 2–4 copies** depending on configuration. See also [[grpo-rl-training]] for the full training loop.

## Comparison with PPO

PPO requires **at minimum 4 model copies**: Actor + Critic + Reference + Reward.

[[grpo]] eliminates the critic entirely—advantages are computed from group-normalized rewards—saving roughly **1 model copy worth of memory** (params + optimizer + gradients). On a 7B model that is ~20 GB saved before any other optimization.

## Concrete Memory Budget (7B, BF16)

| Component | Formula | Size |
|-----------|---------|------|
| Parameters | 7B × 2 bytes | ~14 GB |
| Gradients | same as params | ~14 GB |
| Adam optimizer states | 2 × params (m + v) | ~28 GB |
| FP32 master weights (mixed precision) | 7B × 4 bytes | ~28 GB |

### Default GRPO (no optimizations)

- **Actor**: 14 + 14 + 28 + 28 ≈ **84 GB**
- **Reference**: **14 GB** (params only, inference mode)
- **Total: ~98 GB** across devices

### With LoRA (rank 16) on Actor

Only the adapter parameters (~0.4 GB optimizer states for r=16) need full-precision copies. See [[fine-tuning/peft-lora-qlora]].

- **Actor**: 14 + 0.4 + 0.4 ≈ **28 GB** (frozen base + trainable adapters)
- **Reference**: **14 GB**
- **Total: ~42 GB** — a **57% reduction**

### With LoRA + β=0 (drop reference model)

LoRA acts as an implicit regularizer; many teams set KL weight (β) to zero, which **eliminates the reference model copy entirely**.

- **Total: ~28 GB** — a **71% reduction** from baseline

## Key Optimizations

| Optimization | Savings | Trade-off |
|-------------|---------|-----------|
| **LoRA on actor** | ~56 GB optimizer+gradients | Slight quality ceiling on hard tasks |
| **β=0 (drop reference)** | ~14 GB | No KL regularization; rely on LoRA for stability |
| **Rule-based rewards** (math/code) | ~14 GB reward model | Limited to domains with verifiable answers |
| **Quantized reference** (INT4) | ~10.5 GB | Negligible quality impact on KL estimation |
| **vLLM / SGLang rollout** | 30–50% KV-cache reduction | Extra engine setup; see [[inference/vllm]] |
| **Gradient checkpointing** | ~30% of activations | ~25% more compute time |

## Rollout Engine Sharing

In **synchronous** frameworks (e.g., single-node DeepSpeed-Chat), the actor weights double as the rollout model—no extra copy. In **async** setups (e.g., separate vLLM server), the rollout engine holds its own copy, adding ~14 GB. The async approach is faster but costs one additional model in memory. See [[grpo-infrastructure]] for deployment patterns.

## Summary

The critical insight: GRPO already saves one model copy over PPO by removing the critic. The highest-leverage further optimization is **LoRA + β=0**, which collapses a ~98 GB memory footprint to ~28 GB on a 7B model—making single-node 8×A100 training feasible where it otherwise would not be. For broader context on algorithmic trade-offs, see [[rl-algorithms-for-llm-training]].
