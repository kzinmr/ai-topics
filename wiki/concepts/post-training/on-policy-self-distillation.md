---
title: "On-Policy Self-Distillation (OPSD)"
type: concept
created: 2026-05-18
updated: 2026-06-03
tags:
  - training
  - reasoning
  - self-distillation
  - evolutionary-algorithms
  - gepa
aliases:
  - OPSD
  - On-Policy Self-Distillation
  - Self-Distilled Reasoner
sources:
  - raw/articles/2026-05-18_siyan-zhao_opsd-self-distilled-reasoner.md
  - raw/articles/2026-05-12_ar0cket1_on-policy-self-distillation.md
  - https://siyan-zhao.github.io/blog/2026/opsd/
  - https://x.com/i/article/2054081238236020736
  - raw/articles/2026-06-08_chinmaykarkar_opd-survey-2026.md
  - https://chinmaykarkar.com/blog/OPD_blog/
related:
  - concepts/post-training/on-policy-distillation
  - concepts/post-training/sdar-self-distilled-agentic-rl
  - concepts/model-distillation
  - concepts/post-training/grpo-rl-training
  - concepts/gepa
  - entities/siyan-zhao
  - entities/ar0cket1
  - entities/chinmay-karkar
status: complete
---

# On-Policy Self-Distillation (OPSD)

> **On-Policy Self-Distillation (OPSD)** is a post-training technique where a single LLM serves as both student and teacher — the teacher sees the ground-truth solution as privileged context, providing dense token-level supervision on the student's own on-policy trajectories. Introduced by Siyan Zhao et al. (UCLA / Meta Superintelligence Labs, 2026) for math reasoning tasks.

OPSD is a **specific variant** of the broader On-Policy Distillation (OPD) paradigm. While [[concepts/post-training/on-policy-distillation|OPD]] (Thinking Machines Lab, Oct 2025) uses a separate or same-family teacher model, OPSD uses the **exact same model** — the teacher is distinguished only by conditioning on privileged information (ground-truth solutions for reasoning, or retrieved skills for agent tasks).

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

[[concepts/post-training/sdar-self-distilled-agentic-rl|SDAR]] (Lu et al., 2026) adapts OPSD for **multi-turn agent training**. The core idea is identical (same model as teacher with privileged context), but SDAR:

- Replaces JSD_β with **reverse-KL gap** (Δ_t)
- Uses privileged **retrieved skills** instead of ground-truth solutions
- Introduces a **sigmoid gate** to handle asymmetric trust (negative teacher signals may be unreliable)
- Keeps GRPO as **primary objective** (OPSD is auxiliary only)

See [[concepts/post-training/sdar-self-distilled-agentic-rl]] for the full SDAR method.

## Empirical KL Analysis & Stability (ar0cket1, May 2026)

Independent experiments by [[entities/ar0cket1|ar0cket1]] (@ar0cket1) on Olmo 3 7B (math data from Nemotron Math v2) revealed deep behavioral differences between OPSD and OPD at the token level. The experiments used 25 hand-written hint types across 10 problems, with 4 student rollouts per problem.

### KL Divergence Profile

| Metric | OPSD | OPD |
|--------|------|-----|
| Mean KL | Similar to OPD (controllable) | Similar to OPSD (controllable) |
| **Max KL** | **13.249** | **3.736** |
| KL mass concentration | Distributed (many moderate KL tokens) | Concentrated (few outlier high-KL tokens) |
| Low-entropy token impact | **High** (messes with high-confidence tokens) | Low |

**Key finding:** OPSD exhibits **KL shocks** — individual tokens with very high KL divergence. These are much more frequent in OPSD than OPD. While OPD concentrates its KL mass in sparse, outlier tokens, OPSD distributes KL mass more broadly. OPSD also disproportionately messes with high-confidence (low-entropy) tokens, contributing to instability.

### Positive Pressure Token Rate (Critical Concern)

A striking asymmetry in **directional pressure**:

| Direction | OPSD | OPD |
|-----------|------|-----|
| **Down-weights student-chosen token** | **83%** | 20% |
| **Up-weights student-chosen token** | 17% | **80%** |

OPSD predominantly **down-weights** the tokens the student model actually chose (83% of the time), while OPD predominantly **up-weights** the student's choices (80%). This "negative bias" proved extremely stubborn — across 40 hand-written hints, ar0cket1 could not significantly budge this ratio toward OPD-like behavior. This is one of the largest concerns about OPSD in practice: the teacher is telling the student "you're wrong" far more often than "you're right" at the token level.

### OPSD vs OPD: Token-Level Behavioral Analysis

- **OPD** rewards productive search — using invariants, rephrasing problems productively. It functions as a "perfect PRM."
- **OPSD** touches almost the opposite tokens. It is most active on tokens like: "problem", "Let", "First", "Alternatively", "Wait", "equation", "find." It concentrates around bringing back search paths that were already explored and skipped, and rewards tokens that reintroduce answer constraints or solution-validity checks.
- OPSD's signal is driven by **moving the search toward the hint's suggestion**, regardless of whether that direction is productive.

## Hint Optimization via GEPA (Evolutionary Prompt Engineering)

Since hand-written hints consistently produced OPSD's negative-skewed KL geometry, ar0cket1 turned to **automated hint optimization** using [[concepts/gepa|GEPA]] (Genetic-Pareto Prompt Evolution):

### Approaches Tried

| Approach | Result |
|----------|--------|
| **Answer-only hint conditioning** | Worst — huge KL shocks |
| **RL-direction + OPSD magnitudes** | Didn't create OPD-like KL geometry |
| **Verifyable reward or token masking** | Removes KL shocks but doesn't close the OPSD-OPD geometry gap |
| **Reversing KL direction** | Produced more OPD-like behavior (better positive/negative ratio) — interesting but likely impractical |
| **GEPA general hint prompt optimization** (20+ hours on RTX 6000 Pro) | **Minimized KL shocks** to ~1/2 of naive OPSD, with 2× mean KL. But couldn't significantly improve positive KL pull |
| **GEPA per-task hint optimization** (width 3, depth 8) | ~2× cost of regular OPD, 4-5× more sample efficient than RL. No major improvement over general hint gen prompt |
| **Greedy single-problem GEPA** (40 rounds of mutation) | Could drop KL but couldn't escape the inherent negative bias |

### Surprising Finding: General > Specific

A counter-intuitive result: the **general hint generation prompt** (optimized on a separate dataset) outperformed GEPA optimization **specifically targeted** at individual problems. Even on the problem the specific optimization was designed for, the general prompt did better. This suggests that broad hint-generation strategies may be more robust than problem-specific fine-tuning.

### Full Solution as Hint

Giving the full ground-truth solution as a hint is **extremely unstable**. However, ar0cket1 found it's possible to create more stable variants that bring the KL closer to OPD's mean KL.

## Continual Learning Economics

ar0cket1 provides a cost analysis of OPSD-based continual learning if OPSD can be solved (unlimited upper bound like RL, 10× sample efficiency):

| Spend | Effective RL-equivalent Tokens | Assessment |
|-------|-------------------------------|------------|
| $100,000 | 15.48B | Negligible |
| $1,000,000 | 154.56B | Alright, not huge |
| $10,000,000 | 1.55T | **Meaningful** |

Key assumptions: ~$50/M output tokens for frontier inference, ~$65/M tokens for continual learning training (inference + backward pass, only ~$15 premium over raw inference). Model lifespan ~2 months before obsolescence.

**Bottom line:** Even with solved OPSD, continual learning is viable primarily for large corporations with huge engineering teams generating high token throughput.

## Additional OPSD Variants (Chinmay Karkar Survey, June 2026)

Chinmay Karkar's survey covers several important OPSD extensions:

### SDFT (Shenfeld et al., 2026)
Reframes OPSD for **continual learning**. Uses an **EMA-updated teacher checkpoint** as the PI-conditioned view, avoiding stale guidance from frozen checkpoints and noise chasing from fully live checkpoints.

### SDPO (Hübotter et al., 2026)
Stretches what PI is allowed to be: uses **environment's own textual feedback** (runtime errors, judge critiques, test traces) as PI instead of reference solutions. Works at test time too — same objective doubles as training-time and inference-time procedure.

### GATES (Stein et al., 2026)
Targets document-grounded QA where the PI-conditioned teacher is sometimes wrong. Derives reliability signal online via **consensus gating** — only distills when multiple PI-conditioned rollouts agree on the same answer.

### CRISP (Sang et al., 2026)
Most stripped-down PI: a single **"be concise" instruction**. Automatically compresses easy problems hard and leaves deliberation on hard ones intact. Reverse KL between with-instruction and without-instruction views.

### RLSD (Yang et al., 2026)
Pushes back on pure self-distillation. Takes **update magnitudes from self-distillation** and **update directions from RLVR** (verifier correctness). Prevents "severe information leakage and unstable long-term training" from pure OPSD.

### CaOPD (Zhang et al., 2026)
First paper to take the **capability vs calibration** split seriously. Reveals that teacher-conditioned success is not a valid target for deployment-time confidence.

## Open Problems

1. **Does reducing KL shocks improve practical training?** The KL divergence analysis alone has limited predictive power — the reduction in shocks achieved by GEPA optimization needs direct training-run validation.
2. **Is OPD-like behavior necessary?** Making OPSD fully OPD-like may not be the right proxy. OPSD's different geometry might work if the KL shocks can be controlled.
3. The **positive pressure asymmetry** (83% down-weight vs OPD's 80% up-weight) appears to be an inherent property of current OPSD formulations — not fixable by hint optimization alone.
4. Whether **reversed-KL OPSD** could work in practice remains an unexplored direction.

## Related Pages

- [[concepts/post-training/on-policy-distillation]] — Broader OPD paradigm (Thinking Machines Lab, 2025)
- [[concepts/post-training/sdar-self-distilled-agentic-rl]] — SDAR: OPSD + gating for agent training
- [[concepts/post-training/grpo-rl-training]] — GRPO, the RL backbone both OPSD and SDAR compare against
- [[concepts/model-distillation]] — General category of knowledge distillation
- [[entities/siyan-zhao]] — Lead author
