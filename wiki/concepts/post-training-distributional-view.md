---
title: "Post-Training Distributional View"
created: 2026-05-11
updated: 2026-05-11
type: concept
status: L2
tags:
  - training
  - fine-tuning
  - reinforcement-learning
  - inference
aliases: ["Distributional Lens on Post-Training", "SFT vs RL vs OPD"]
sources: [raw/articles/2026-05-10_nrehiew_sft-rl-opd-distributional-lens.md]
related: [entities/nrehiew, concepts/on-policy-distillation, concepts/grpo]
---

# Post-Training Distributional View

A mental model for understanding post-training methods through the lens of **distribution reshaping**. Proposed by wh (@nrehiew_) in a widely-bookmarked 2026 X post (573 bookmarks, 181K views).

## Core Insight

> A language model is a distribution over sequences. When we post-train it and attempt to teach it a task, we are reshaping this distribution.

The key question for any post-training method is: **What is the target distribution, and how directly does the method approach it?**

## Three Methods, Three Approaches

### Supervised Fine-Tuning (SFT)
- **Target distribution**: The teacher/expert's output distribution
- **Approach**: Mode-seeking — narrows the model toward high-probability teacher outputs
- **Characteristic**: Off-policy. The student learns from a fixed dataset of idealized outputs
- **Limitation**: Exposure bias — at inference time, the model generates its own imperfect trajectories that differ from training data

### Reinforcement Learning (RL)
- **Target distribution**: A reward-shaped distribution
- **Approach**: Indirect — shapes behavior through scalar reward signals
- **Characteristic**: On-policy. The model generates its own rollouts and receives feedback
- **Limitation**: Sparse signal (binary reward per episode), requires multiple rollouts (GRPO uses 8+), gradient vanishes when all samples are correct

### On-Policy Distillation (OPD)
- **Target distribution**: Teacher distribution evaluated on student's own trajectories
- **Approach**: Direct matching — the teacher provides dense token-level supervision on student-generated sequences
- **Characteristic**: On-policy + dense feedback. Combines RL's distributional realism with SFT's rich training signal
- **Advantage**: Eliminates exposure bias while providing O(n) bits of information per episode (vs O(1) for RL)

## Distributional Comparison

| Dimension | SFT | RL (GRPO/PPO) | On-Policy Distillation |
|-----------|-----|---------------|----------------------|
| **Sampling** | Off-policy (teacher data) | On-policy (student rollouts) | On-policy (student rollouts) |
| **Signal density** | Dense (per-token) | Sparse (per-episode) | Dense (per-token) |
| **Target definition** | Direct (teacher outputs) | Indirect (reward function) | Direct (teacher distribution) |
| **Exposure bias** | High | Low | Low |
| **Information per episode** | O(n) tokens | O(1) bits | O(n) tokens |
| **Distribution match** | Forward KL (mode-seeking) | Reverse KL via reward | Reverse KL (direct) |

## Why the Distributional View Matters

This framework explains several empirical observations:

1. **RL retains more pre-training capabilities than SFT** — because RL operates on-policy, maintaining distributional proximity to the student's prior (Chen et al., 2025)

2. **Self-distillation resists catastrophic forgetting** — on-policy self-distillation can serve as a principled RL alternative for continual learning (SDFT, Shenfeld et al., 2026)

3. **OPD can surpass teacher performance** — by decoupling the reference model and introducing reward scaling (G-OPD/ExOPD, Yang et al., 2026)

4. **The distribution IS the curriculum** — what the student samples during training determines what it learns. This is why data mixing, token weighting, and trajectory selection matter.

## Key Insight

The shift from SFT → RL → OPD represents progressively better alignment between **training distribution and inference distribution**. SFT suffers from exposure bias because the training distribution (teacher outputs) differs from the inference distribution (self-generated). RL fixes this but provides sparse feedback. OPD fixes both: on-policy sampling with dense teacher guidance.

## See Also
- [[entities/nrehiew]]
- [[concepts/on-policy-distillation]]
- [[concepts/grpo]]
- [[concepts/distillation]]
