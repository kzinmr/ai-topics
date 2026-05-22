2026-05-22 | arXiv:2605.19095v1 | ScheduleFree+: Scaling Learning-Rate-Free & Schedule-Free Learning to LLMs
======================================================================================================
Source: https://arxiv.org/html/2605.19095v1
Date: May 18, 2026
Author: Aaron Defazio (FAIR at Meta Super-Intelligence Labs)
Code: https://github.com/facebookresearch/schedule_free

# ScheduleFree+

Extends Schedule-Free Learning to large language model pretraining. Replaces LR schedules with aggressive averaging for stable, anytime training.

## Core Innovations
1. Inner momentum restored into Schedule-Free AdamW → fixes large-batch divergence
2. Polyak step size variant using L1 gradient norm → fully LR-free training
3. Warm-starting (delaying iterate averaging) → improved early loss
4. Annealing outer momentum β (0.9→0.965) + r=1 averaging → large gains on long runs

## Key Results
- 31% training time reduction vs SOTA schedules at 1000 tokens/parameter
- Removes need for decreasing learning rate (warmup still needed)
- Handles batch sizes up to 8M tokens
- Fully learning-rate-free when combined with Polyak steps

## Gradient Norm Drift
Normalization layers cause effective LR to depend on weight norms. Rising gradient norms = increasing effective LR = hurt convergence.
Fix: inverse gradient-norm weighting using EMA of 1/‖g_t‖₁.

## Polyak Step for Schedule-Free AdamW
γ_t = (f(y_t) - f_* + β⟨∇f(y_t), z_t - x_t⟩) / (√(π/2) · ‖∇f(y_t)‖₁)
All quantities EMA-smoothed. Makes LLM training fully LR-free.
