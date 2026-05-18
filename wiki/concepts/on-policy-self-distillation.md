---
title: "On-Policy Self-Distillation (OPSD)"
type: concept
created: 2026-05-18
updated: 2026-05-18
tags:
  - training
  - reasoning
aliases:
  - OPSD
  - On-Policy Self-Distillation
  - Self-Distilled Reasoner
sources:
  - raw/articles/2026-05-18_siyan-zhao_opsd-self-distilled-reasoner.md
  - https://siyan-zhao.github.io/blog/2026/opsd/
related:
  - concepts/on-policy-distillation
  - concepts/sdar-self-distilled-agentic-rl
  - concepts/model-distillation
  - concepts/grpo-rl-training
  - entities/siyan-zhao
status: complete
---

# On-Policy Self-Distillation (OPSD)

> **On-Policy Self-Distillation (OPSD)** is a post-training technique where a single LLM serves as both student and teacher — the teacher sees the ground-truth solution as privileged context, providing dense token-level supervision on the student's own on-policy trajectories. Introduced by Siyan Zhao et al. (UCLA / Meta Superintelligence Labs, 2026) for math reasoning tasks.

OPSD is a **specific variant** of the broader On-Policy Distillation (OPD) paradigm. While [[concepts/on-policy-distillation|OPD]] (Thinking Machines Lab, Oct 2025) uses a separate or same-family teacher model, OPSD uses the **exact same model** — the teacher is distinguished only by conditioning on privileged information (ground-truth solutions for reasoning, or retrieved skills for agent tasks).

## Core Intuition

Modern LLMs exhibit an asymmetry: **evaluation > generation**. A model can more easily rationalize why a correct answer is right than generate that answer from scratch. OPSD exploits this by giving the teacher access to the ground-truth solution y^*, letting it serve as a token-level oracle on the student's own trajectories.

| Method | Sampling | Supervision | Teacher |
|--------|----------|-------------|---------|
| SFT | Off-policy (expert traces) | Dense (per-token) | External (human/stronger model) |
| GRPO | On-policy | Sparse (trajectory-level reward) | None (group baseline) |
| Knowledge Distillation | Off-policy | Dense (per-token) | External (stronger model) |
| **OPSD** | **On-policy** | **Dense (per-token)** | **Self (same model + privileged context)** |

## Method

### Architecture

A single model plays two roles that differ **only in conditioning context**:

- **Student policy** π_S(·|x): sees only the problem — inference-time conditions
- **Teacher policy** π_T(·|x, y^*): sees problem + ground-truth solution — training-only privilege

The teacher is **frozen at the initial policy** weights — it never generates tokens, only computes next-token distributions in one forward pass.

### Training Loop

1. **On-Policy Sampling**: ŷ ~ π_S(· | x) — student generates a full trajectory
2. **Distribution Computation**: Both policies compute next-token distributions at every position n, conditioned on the same student prefix ŷ_<n
3. **Per-Token Matching**: Minimize divergence between teacher and student distributions

### Loss Function

OPSD uses **generalized Jensen-Shannon divergence (JSD_β)**:

$$\\text{JSD}_\\beta(p_T \\| p_S) = \\beta \\cdot D_{\\text{KL}}(p_T \\| m) + (1-\\beta) \\cdot D_{\\text{KL}}(p_S \\| m)$$

where $m = \\beta \\cdot p_T + (1-\\beta) \\cdot p_S$ is the interpolated distribution.

The total loss (trajectory-averaged, token-wise):

$$\\mathcal{L}(\\theta) = \\mathbb{E}_{(x,y^*)\\sim \\mathcal{S}} \\left[ \\mathbb{E}_{\\hat{y}\\sim p_S(\\cdot|x)} \\left[ \\frac{1}{|\\hat{y}|} \\sum_{n=1}^{|\\hat{y}|} D(p_T \\| p_S)(\\hat{y} \\mid x) \\right] \\right]$$

Gradients flow **only through the student** — the frozen teacher provides stable targets.

### Per-Token KL Clipping

Stylistic tokens ("wait", "therefore", "however") often dominate the divergence despite carrying little reasoning content. Per-token pointwise KL clipping caps each vocabulary entry's contribution, preventing these tokens from hijacking the training signal.

## Policy-Gradient Interpretation

OPSD can be viewed as a policy-gradient method with **dense token-level reward**:

$$r_n(x, \\hat{y}) = \\log p_T(\\hat{y}_n \\mid x, y^*, \\hat{y}_{<n}) - \\log p_S(\\hat{y}_n \\mid x, \\hat{y}_{<n})$$

$$J_{\\text{OPSD}}(\\theta) = \\mathbb{E}\\left[\\frac{1}{|\\hat{y}|}\\sum_n r_n(x, \\hat{y})\\right]$$

### Comparison with STaR

| Aspect | STaR | OPSD |
|--------|------|------|
| Reward signal | 𝟙(y = y^*) — binary | Per-token log-ratio — dense |
| Granularity | Sequence-level | Token-level |
| Incorrect trajectories | **Discarded entirely** | **Still provide learning signal** |
| Credit assignment | None | Implicit via teacher distribution |

OPSD's key advantage: **it learns from every token**, even when the final answer is wrong. If the student makes an arithmetic error at step 3 but reasoning at steps 1-2 is sound, OPSD reinforces steps 1-2 while STaR discards the entire trajectory.

## Experimental Results

**Setup:** Competition-level math benchmarks, Qwen3 model family, OpenThoughts training data.

**Efficiency:** OPSD = **1 rollout/problem, 1024 tokens generation** vs GRPO = **8 rollouts, 16k tokens**.

### Main Findings

1. **OPSD > SFT**: SFT degrades on OpenThoughts because it learns from concise solutions, shortening test-time generation. OPSD converts concise solutions into dense supervision without shortening.
2. **OPSD ≥ GRPO** at drastically lower token cost (~64× fewer tokens).
3. **GRPO reward diversity collapse**: >50% of batches show zero reward standard deviation within 100 steps → no gradient. OPSD entirely avoids this.

## Relationship to Related Methods

### OPSD vs OPD (Thinking Machines Lab)

Both are on-policy distillation, but differ in teacher construction:

| Aspect | OPD (Thinking Machines) | OPSD (Zhao et al.) |
|--------|------------------------|---------------------|
| Teacher | Separate or same-family model | **Same model** + privileged context |
| Divergence | Reverse-KL | JSD_β |
| Domain | General post-training | Math reasoning |
| Teacher role | Generates reference distribution | Computes distributions only (frozen) |

### OPSD → SDAR

[[concepts/sdar-self-distilled-agentic-rl|SDAR]] (Lu et al., 2026) adapts OPSD for **multi-turn agent training**. The core idea is identical (same model as teacher with privileged context), but SDAR:

- Replaces JSD_β with **reverse-KL gap** (Δ_t)
- Uses privileged **retrieved skills** instead of ground-truth solutions
- Introduces a **sigmoid gate** to handle asymmetric trust (negative teacher signals may be unreliable)
- Keeps GRPO as **primary objective** (OPSD is auxiliary only)

See [[concepts/sdar-self-distilled-agentic-rl]] for the full SDAR method.

## Related Pages

- [[concepts/on-policy-distillation]] — Broader OPD paradigm (Thinking Machines Lab, 2025)
- [[concepts/sdar-self-distilled-agentic-rl]] — SDAR: OPSD + gating for agent training
- [[concepts/grpo-rl-training]] — GRPO, the RL backbone both OPSD and SDAR compare against
- [[concepts/model-distillation]] — General category of knowledge distillation
- [[entities/siyan-zhao]] — Lead author
