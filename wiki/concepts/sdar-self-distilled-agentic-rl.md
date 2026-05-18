---
title: "Self-Distilled Agentic Reinforcement Learning (SDAR)"
type: concept
created: 2026-05-18
updated: 2026-05-18
tags:
  - reinforcement-learning
  - distillation
  - grpo
  - post-training
  - training
aliases:
  - SDAR
  - Self-Distilled Agentic RL
  - gated-opsd
sources:
  - raw/papers/2026-05-18_2605.15155_sdar-self-distilled-agentic-rl.md
  - https://arxiv.org/abs/2605.15155
  - https://github.com/ZJU-REAL/SDAR
  - raw/articles/2026-05-18_siyan-zhao_opsd-self-distilled-reasoner.md
  - https://siyan-zhao.github.io/blog/2026/opsd/
related:
  - concepts/grpo-rl-training
  - concepts/on-policy-distillation
  - concepts/on-policy-self-distillation
  - concepts/multi-teacher-on-policy-distillation
  - concepts/model-distillation
  - concepts/rlhf
status: complete
---

# Self-Distilled Agentic Reinforcement Learning (SDAR)

> **SDAR** is a post-training method that combines GRPO-based RL with gated On-Policy Self-Distillation (OPSD) for stable multi-turn LLM agent training. It introduces a **sigmoid gate** at the token level that lets each token autonomously decide its distillation intensity — amplifying teacher endorsements while softly attenuating unreliable negative signals.

Published May 2026 by Zhejiang University, Meituan, and Tsinghua University ([arXiv:2605.15155](https://arxiv.org/abs/2605.15155), [GitHub: ZJU-REAL/SDAR](https://github.com/ZJU-REAL/SDAR)).

## Motivation

### The Gap in Agent Post-Training

Two paradigms exist for post-training LLM agents:

| Paradigm | Signal Granularity | Problem |
|----------|-------------------|---------|
| **RL (e.g., GRPO)** | Trajectory-level (coarse) | Only knows *if* a trajectory succeeded, not *which tokens* were good |
| **On-Policy Self-Distillation (OPSD)** | Token-level (dense) | Teacher is the same model + privileged context → signals can be unreliable |

### Two Critical Observations

**Observation 1: Multi-turn OPSD is unstable.** When the student agent drifts from the teacher-supported trajectory, token-level supervision becomes increasingly unreliable. This causes surging per-turn KL divergence and catastrophic degradation. Naïve GRPO+OPSD **collapses entirely** on small models (Qwen3-1.7B: from 37% to 9.5% on Search-QA).

**Observation 2: Teacher signals are asymmetric.** The teacher is not an independently stronger model — it's the same policy with privileged context (retrieved skills). Key insight: **over 50% of tokens have negative gaps** (teacher assigns lower probability than student). These negatives may stem from:
- Poor skill retrieval quality
- Teacher's inability to utilize skills into reliable token preferences
- Multi-turn drift compounding across turns

→ **Design philosophy**: Trust positive teacher endorsements **strongly**, treat negative rejections **conservatively**.

## Method

### Architecture

SDAR keeps RL as the primary optimization backbone and adds OPSD as a **gated auxiliary objective**:

$$\\mathcal{L}_{\\text{SDAR}} = \\underbrace{\\mathcal{L}_{\\text{GRPO}}}_{\\text{primary, untouched}} + \\lambda_{\\text{SDAR}} \\cdot \\underbrace{\\mathcal{L}_{\\text{SDAR}}^{\\text{aux}}}_{\\text{gated OPSD}}$$

### Token-Level Sigmoid Gating

The core innovation is a **detached sigmoid gate** $g_t$ applied at each token:

$$\\Delta_t = \\log \\pi_T(y_t \\mid s_t^+) - \\log \\pi_\\theta(y_t \\mid s_t) \\quad \\text{(reverse-KL gap)}$$

$$g_t = \\sigma(\\beta \\cdot \\Delta_t) \\in (0,1) \\quad \\text{(gap gating, default)}$$

$$\\ell_t^{\\text{SDAR}} = g_t \\cdot \\bigl(\\log \\pi_T(y_t \\mid s_t^+) - \\log \\pi_\\theta(y_t \\mid s_t)\\bigr)$$

**Three gating strategies** are explored:

| Strategy | Signal | Behavior |
|----------|--------|----------|
| **Gap gating** (default) | $\\Delta_t$ (teacher-student gap) | Amplifies positive endorsements, attenuates negative rejections |
| **Entropy gating** | $h_t$ (student entropy) | Targets high-uncertainty tokens |
| **Soft-OR gating** | $1-(1-h_t)(1-\\Delta_t)$ | Combines both signals |

The gate is detached (`sg`): gradients flow only through the student's log-probability, preventing the teacher from dominating the optimization.

### Key Properties

- **Gradient bounded** by $g_t \\in (0,1)$ → no amplification of unreliable signals
- **Monotonic in $\\Delta_t$** → positive-gap tokens get weight near 1.0; negative-gap tokens near 0.0
- **Self-paced curriculum** — no hyperparameter schedules, no heuristics
- **RL advantage gradient remains unbiased** — only the auxiliary term is gated

## Results

All experiments use GRPO as the RL backbone. SDAR adds the gated OPSD auxiliary loss.

| Model | ALFWorld (succ%) | Search-QA (avg%) | WebShop (score/acc) |
|-------|-----------------|-------------------|---------------------|
| Qwen2.5-3B + GRPO | 75.0 | 36.4 | 79.8 / 63.3 |
| Qwen2.5-3B + SDAR | **84.4** (+9.4) | **43.4** (+7.0) | 85.0 / 68.0 |
| Qwen2.5-7B + GRPO | 81.2 | 42.0 | 80.9 / 72.6 |
| Qwen2.5-7B + SDAR | **85.9** (+4.7) | **49.0** (+7.0) | **89.4 / 82.8** (+10.2 acc) |
| Qwen3-1.7B + GRPO+OPSD | 37.9 (collapse) | 9.5 (collapse) | — |
| Qwen3-1.7B + SDAR | **77.7** | **41.2** | 75.4 / 61.7 |

### Key Takeaways

1. **SDAR consistently beats GRPO** by 5–10pp across benchmarks and model scales
2. **Prevents collapse** on small models where naïve GRPO+OPSD catastrophically fails
3. **Outperforms hybrid methods** (Skill-SD, RLSD) that use fixed distillation schedules
4. **KL divergence stays flat across turns** — critical for long-horizon agents (traditional OPSD: KL diverges 10× by turn 4)

## Relationship to Related Techniques

| Method | Teacher | Gate Mechanism | Primary Objective | Multi-turn Stable |
|--------|---------|---------------|-------------------|-------------------|
| [[concepts/grpo-rl-training\|GRPO]] | None (group baseline) | N/A | RL advantage | ✓ |
| [[concepts/on-policy-distillation\|OPD]] | Separate model or same model | None | Distillation only | ✗ |
| GRPO+OPSD (naïve) | Same policy + skills | None | RL + distillation | ✗ (collapses) |
| Skill-SD | Same policy + skills | Fixed schedule | RL + scheduled OPSD | Partial |
| RLSD | Separate models | Fixed schedule | RL + scheduled OPSD | Partial |
| **SDAR** | Same policy + skills | **Adaptive sigmoid gate** | RL + gated OPSD | **✓** |

### SDAR vs OPD

SDAR is a specific instance of On-Policy Distillation where:
- The teacher is the **same model** with privileged context (skills) — not a stronger model
- The core problem is **asymmetric trust** in teacher signals, not just combining RL + distillation
- The solution is **token-level gating**, not teacher ensemble or fixed schedules

See [[concepts/on-policy-distillation]] for the foundational OPD work by Thinking Machines Lab (Oct 2025).
See [[concepts/multi-teacher-on-policy-distillation]] for MOPD, the 2026 production-scale evolution.

## Implementation Details

- **RL backbone**: GRPO (Group Relative Policy Optimization)
- **Distillation**: Reverse-KL (mode-seeking), detached gate prevents teacher dominance
- **Hyperparameters**: λ_SDAR=0.01, β=5.0, 150 training steps, 8×H800 GPUs
- **Skill retrieval**: SkillBank with Qwen2.5-3B-Instruct via keyword matching / UCB
- **Models tested**: Qwen2.5-3B, Qwen2.5-7B, Qwen3-1.7B (Instruct variants)

## Related Pages

- [[concepts/grpo-rl-training]] — GRPO algorithm, the RL backbone
- [[concepts/on-policy-self-distillation]] — OPSD: the foundational same-model self-distillation technique SDAR builds on
- [[concepts/on-policy-distillation]] — Foundational OPD technique (Thinking Machines Lab, 2025)
- [[concepts/multi-teacher-on-policy-distillation]] — Multi-teacher production OPD (2026)
- [[concepts/model-distillation]] — General category of knowledge distillation
- [[concepts/rlhf]] — Broader RLHF context
