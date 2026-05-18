---
title: "GRPO RL Training"
type: concept
aliases:
  - grpo-rl-training
  - GRPO
  - Group Relative Policy Optimization
created: 2026-04-25
updated: 2026-05-18
tags:
  - concept
  - reinforcement-learning
  - training
  - fine-tuning
status: complete
related:
  - concepts/multi-teacher-on-policy-distillation
  - concepts/on-policy-distillation
  - concepts/sdar-self-distilled-agentic-rl
  - concepts/model-distillation
  - concepts/deepseek-r1
sources:
  - https://arxiv.org/abs/2402.03300
  - raw/papers/2026-05-18_2605.15155_sdar-self-distilled-agentic-rl.md
---

# GRPO (Group Relative Policy Optimization)

> **GRPO** (Group Relative Policy Optimization) is a reinforcement learning algorithm for post-training LLMs that eliminates the need for a separate value/critic model by computing advantages relative to a group of sampled completions. Popularized by [[concepts/deepseek-r1|DeepSeek-R1]] (Jan 2025), it has become a standard RL backbone for reasoning, agent, and format-enforcement training.

First proposed by Shao et al. (DeepSeek, 2024) in "[DeepSeekMath: Pushing the Limits of Mathematical Reasoning](https://arxiv.org/abs/2402.03300)".

## Core Mechanism

### Advantage Computation

Unlike PPO (Proximal Policy Optimization), which requires a separate value model to estimate baselines, GRPO computes advantages **within a group**:

For each prompt $x$, sample $G$ completions ${y_1, ..., y_G}$. For each completion $y_i$:

$$A_{i,t} = \\frac{r_i - \\text{mean}(\\{r_1,...,r_G\\})}{\\text{std}(\\{r_1,...,r_G\\})}$$

where $r_i$ is the reward assigned to completion $i$ (from a reward model, verifier, or environment).

### Advantages
- **No critic model needed** — saves memory and compute (no separate value network)
- **Group-relative normalization** — naturally handles reward scale drift
- **Simplicity** — fewer hyperparameters than PPO

### Limitations
- **Trajectory-level only** — knows whether a trajectory succeeded, not which tokens were good
- **Group size $G > 1$ required** — can't operate with single samples (unlike OPD-based methods)
- **Reward model dependency** — quality depends on reward/verifier accuracy

## GRPO as an RL Backbone

GRPO forms the RL backbone for many post-training methods:

| Method | What it adds to GRPO | Reference |
|--------|---------------------|-----------|
| **GRPO (vanilla)** | Group-relative advantage | DeepSeekMath (2024) |
| **[[concepts/multi-teacher-on-policy-distillation\|MOPD]]** | Teacher-student log-ratio replaces advantage; $G=1$ possible | Yumo Xu (2026) |
| **[[concepts/sdar-self-distilled-agentic-rl\|SDAR]]** | Gated OPSD auxiliary loss; GRPO objective untouched | Lu et al. (2026) |
| **Skill-GRPO** | Privileged skills in training context | SDAR paper baseline |

## SDAR's Relationship to GRPO

[[concepts/sdar-self-distilled-agentic-rl|SDAR]] uses GRPO as its primary RL backbone and adds a gated token-level distillation term:

$$\\mathcal{L}_{\\text{SDAR}} = \\underbrace{\\mathcal{L}_{\\text{GRPO}}}_{\\text{unchanged}} + \\lambda \\cdot \\mathcal{L}_{\\text{SDAR}}^{\\text{aux}}$$

Key insight: **SDAR does not modify GRPO's advantage computation**. The auxiliary distillation term is gated at the token level, ensuring that unreliable teacher signals never corrupt the RL gradient. This is why SDAR avoids the catastrophic collapse that naïve GRPO+OPSD suffers.

## Related Pages

- [[concepts/sdar-self-distilled-agentic-rl]] — SDAR: gated OPSD on top of GRPO for multi-turn agent training
- [[concepts/multi-teacher-on-policy-distillation]] — MOPD: GRPO with teacher-student log-ratio advantage
- [[concepts/on-policy-distillation]] — Foundational OPD (reverse-KL distillation)
- [[concepts/model-distillation]] — Broader distillation category
- [[concepts/deepseek-r1]] — DeepSeek-R1, which popularized GRPO for reasoning RL
- [[concepts/_index]]
