---
title: "Self-Distilled Reasoner: On-Policy Self-Distillation (OPSD)"
source: https://siyan-zhao.github.io/blog/2026/opsd/
authors: Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, Aditya Grover
affiliations: UCLA, HKU, Meta Superintelligence Labs
date: 2026-05-18
tags: [article, opsd, distillation, reasoning, training, post-training, grpo]
---

# Self-Distilled Reasoner: On-Policy Self-Distillation (OPSD)

**Authors:** Siyan Zhao† (UCLA), Zhihui Xie (HKU), Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen∗, Aditya Grover∗ (Meta Superintelligence Labs)
**Source:** https://siyan-zhao.github.io/blog/2026/opsd/

---

## Core Problem

Training LLMs for reasoning faces trade-offs between efficiency and effectiveness:

| Method | Strengths | Weaknesses |
|--------|-----------|------------|
| SFT | Uses expert demonstrations | Exposure bias — model never sees its own errors |
| RL (GRPO) | On-policy; better generalization | Expensive (8 rollouts/problem); sparse binary reward; **reward diversity collapse** |
| Knowledge Distillation | Dense token-level supervision | Off-policy; requires external teacher |

**Key insight:** Modern LLMs can rationalize a correct answer more easily than generate it (evaluation > generation). So: *can a model serve as its own teacher?*

---

## Method: On-Policy Self-Distillation (OPSD)

A single model plays two roles differing only in **conditioning context**:

- **Student** p_S(·|x): sees only the problem x (inference-time conditions)
- **Teacher** p_T(·|x, y^*): has privileged access to ground-truth solution y^*

Teacher does NOT generate tokens; rationalization is implicit through one forward pass. Teacher is **fixed at initial policy** for stability.

### Training Procedure

1. **On-Policy Sampling**: ŷ ~ p_S(·|x)
2. **Distribution Computation**: Both policies compute next-token distributions conditioned on same student prefix
3. **Per-Token Matching**: Full-vocabulary divergence objective using **generalized Jensen-Shannon divergence (JSD_β)**:

```
JSD_β(p_T || p_S) = β·KL(p_T || m) + (1-β)·KL(p_S || m)
```
where m = β·p_T + (1-β)·p_S (interpolated distribution).

Total loss (gradients flow only through student):
```
L(θ) = E_{(x,y*)~S} [ E_{ŷ~p_S(·|x)} [ D(p_T || p_S)(ŷ | x) ] ]
```

**Per-Token Pointwise KL Clipping**: Caps per-vocabulary-entry divergence to prevent stylistic tokens ("wait", "therefore") from dominating.

---

## Policy-Gradient Perspective

OPSD = policy gradient with **dense, token-level reward**:

- Per-token reward: r_n = log p_T(ŷ_n | x, y*, ŷ_<n) − log p_S(ŷ_n | x, ŷ_<n)
- OPSD maximizes expected per-token reward
- **Key difference from STaR**: OPSD learns from EVERY token, even when final answer is wrong

### Comparison with STaR

| | STaR | OPSD |
|---|------|------|
| Reward | 𝟙(y = y*) | Per-token log-ratio |
| Granularity | Sequence-level (binary) | Token-level (dense) |
| Incorrect trajectories | Discarded entirely | Still provide learning signal |
| Credit assignment | None | Implicit via teacher distribution |

---

## Experimental Results

**Setup:** Competition-level math benchmarks, Qwen3 family, OpenThoughts data.
**Efficiency:** OPSD uses **1 rollout/problem, 1024 gen length** (vs GRPO: 8 rollouts, 16k length).

### Key Findings

- **OPSD > SFT**: SFT degrades because it learns from concise solutions (shortens generation); OPSD converts solutions into dense supervision without shortening
- **OPSD ≥ GRPO** at drastically lower token cost
- **GRPO reward diversity collapse**: >50% of batches have zero reward std within 100 steps → no gradient signal. OPSD avoids this entirely via dense distillation.

---

## Relationship to SDAR

This OPSD (reasoning-focused, JSD_β divergence) is the foundational technique that SDAR adapted for **multi-turn agent training**. Key differences:

| Aspect | OPSD (Zhao et al.) | SDAR (Lu et al.) |
|--------|-------------------|-------------------|
| Domain | Math reasoning | Multi-turn agent tasks |
| Teacher context | Ground-truth solution y* | Retrieved skills |
| Divergence | JSD_β (symmetric-ish) | Reverse-KL (mode-seeking) |
| Gate | None | Sigmoid gate on Δ_t |
| Primary objective | OPSD only | GRPO + gated OPSD auxiliary |
| Stability concern | KL clipping for stylistic tokens | Multi-turn drift → asymmetric trust |

SDAR's key contribution is solving OPSD's multi-turn instability through gating — the core OPSD idea (same model as teacher + student with privileged context) originates from this work.
