---
title: ScheduleFree+
created: 2026-05-22
updated: 2026-05-22
type: concept
tags:
  - concept
  - training
  - optimization
  - fine-tuning
  - model
  - methodology
  - benchmark
sources: [raw/articles/2026-05-18_schedulefree-plus-llm-training.md, https://arxiv.org/html/2605.19095v1]
---

# ScheduleFree+

A learning-rate-free and schedule-free training method for large language models, extending [[concepts/schedule-free-learning|Schedule-Free Learning]] to LLM scale. Published by Meta FAIR (Aaron Defazio), May 18, 2026. Achieves up to **31% training time reduction** vs. state-of-the-art schedules at 1000 tokens/parameter.

## Core Idea

Replace learning-rate schedules (warmup-stable-decay) with **aggressive iterate averaging**. The averaged iterate `x_t` is the model to evaluate and return — not the gradient evaluation point `y_t`. The method removes the need for a decreasing learning rate, though warmup remains necessary.

## Four Pillars

1. **Inner Momentum** — Reintroduced into Schedule-Free AdamW to fix large-batch divergence (>2M tokens). Enables training at batch sizes up to 8M tokens.
2. **Polyak Step Size** — Variant using L1 gradient norm with EMA smoothing makes LLM training fully LR-free.
3. **Warm-Starting** — Delaying iterate averaging initially improves early loss.
4. **β-Annealing + r=1 Averaging** — Annealing outer momentum (0.9→0.965) + aggressive averaging gives large gains on long runs.

## Gradient Norm Drift Problem

Normalization layers cause the effective learning rate to depend on weight norms:
- For Adam-like methods: `η_eff ∝ η_t ‖g_t‖₁`
- Rising gradient norms → increasing effective LR → hurt convergence

**Fix**: Inverse gradient-norm weighting — scale learning rate by EMA of `1/‖g_t‖₁`, stabilizing effective LR while allowing stable weight norms.

## Polyak Step for LLMs

```
γ_t = (f(y_t) - f_* + β⟨∇f(y_t), z_t - x_t⟩) / (√(π/2) · ‖∇f(y_t)‖₁)
```

All quantities EMA-smoothed (coefficient 0.9). Fully eliminates manual learning-rate tuning for LLM training.

## Key Results

- **31% reduction** in training time at 1000 tokens/parameter (Chinchilla+ regimes)
- Handles batch sizes up to **8M tokens** (with inner momentum)
- Works from 120M to 2B+ parameter models
- Most effective for **long-duration training**; short runs (20-100 TPP) show no final loss advantage, but anytime stopping is useful

## Code & Availability

- Code: [facebookresearch/schedule_free](https://github.com/facebookresearch/schedule_free)
- Built into PyTorch ecosystem
- Single-file implementation for ScheduleFree+ AdamW

## Relationship to Other Methods

- Contrasts with [[concepts/lora|LoRA]]/[[concepts/peft|PEFT]] — ScheduleFree+ is about training efficiency, not parameter efficiency
- Complements [[concepts/grpo-rl-training|GRPO]]/[[concepts/rlhf|RLHF]] post-training by improving pretraining efficiency
- Provides theoretical foundation for [[concepts/model-averaging|model averaging]] and checkpoint merging during pretraining

## Related

- [[concepts/schedule-free-learning|Schedule-Free Learning]]
- [[concepts/training|LLM Training]]
- [[concepts/optimization|Optimization]]
- [[concepts/model-averaging|Model Averaging]]
- [[entities/meta|Meta AI]]
