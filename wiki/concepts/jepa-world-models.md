---
title: JEPA World Models
created: 2026-07-15
updated: 2026-11-17
type: concept
tags:
  - world-models
  - model
  - lab
  - jepa
  - methodology
  - yann-lecun
sources:
  - raw/articles/2026-07-15_lemario-jepa-world-model.md
  - raw/articles/2026-11-13_haddyalchaer_600-experiments-jepa-world-models.md
---

# JEPA World Models

**Joint Embedding Predictive Architecture (JEPA)** is a self-supervised learning framework championed by [[entities/yann-lecun|Yann LeCun]]. Unlike traditional world models that predict raw pixels (VAE/GAN approach), JEPA predicts in a learned latent space — learning semantically meaningful dynamics without wasting capacity on pixel-perfect reconstruction.

## Architecture

1. **Vision Encoder**: Compresses observations (e.g., 224×224 frames) into compact latent vectors (e.g., 192 dimensions).
2. **Action Encoder** (for action-conditioned variants): Compresses action sequences into latent vectors.
3. **Causal Predictor**: Transformer blocks with AdaLN-Zero predict future state representations conditioned on actions.
4. **Regularizer**: SIGReg, VICReg, or similar prevents representation collapse by projecting latents onto random directions and matching to a standard Gaussian.

## Key Advantage

JEPA operates in a compact latent space (~192 dimensions vs millions of pixels), enabling the model to focus on semantically meaningful dynamics. It is related to I-JEPA (Meta's image-based JEPA for self-supervised representation learning, arXiv:2301.08243).

## LeMario (Proof of Concept)

**LeMario** (Benjamin Bai, July 2026) is a from-scratch implementation of a JEPA world model trained on Super Mario Bros, based on LeWorldModel (arXiv:2603.19312). It hit Hacker News front page with 108 points.

Training: 737,134 frames from 280 expert episodes across 32 Mario levels. Results showed short-horizon prediction success (one-step error 0.013773, beating persistence by 45.5% at 5-step) but failure at long-horizon planning — revealing the gap between predictive state and control state in world models.

## LeWM Planning Study (Haddy Alchaer, Nov 2026)

**Haddy Alchaer** ran ~600 experiments on **LeWM** (arXiv:2603.19312, Maes/Le Lidec/Scieur/LeCun/Balestriero) on the Push-T benchmark and reported (2026-11-13, HN 295 points) that the *predictor is not the bottleneck* — four planning-side changes, **with zero retraining**, took long-horizon success (goal 75 steps away) from **22% → 85%**, matching an oracle that is handed ideal expert subgoals:

1. **Subgoal chaining at the model's native horizon.** LeWM plans accurately to ~25 steps (89.7% at 25 steps vs 22% at 75). Splitting long tasks into 25-step segments added ~58 points; swapping in the simulator's *exact physics* added only 20 — evidence that compounding-horizon planning, not prediction error, limits LeWM.
2. **Latent memory graph with a jump cost.** ~460k demonstration frames embedded by LeWM's own encoder, linked along demonstrations and by embedding proximity; graph search picks subgoals. Embedding distance tracks physical reachability (87% pairwise accuracy). Charging a cost for cross-demonstration jumps (else search strings unphysical paths) lifted 62% → 85%.
3. **Symmetry-augmented memory.** Push-T's physics is shift/rotate/mirror invariant; when states near the goal are deleted (93% → 32%), transformed copies of distant demonstration segments restore 85%, and a 1%-demonstration graph plus transforms ≈ a 10% graph.
4. **The goal cost was "wrong."** Goal *images* pin the pusher's position too. With exact physics, scoring block-only vs block+pusher flipped 30/50 tasks from failure to success (p ≈ 2e-9) — a **specification artifact of image-defined goals**, not a model failure. Scoring a plan against the closest of 16 pusher-shifted goal variants doubled harder-test success (11% → 23%). Generalization: a goal should be a *set of acceptable end states*, not one frame.

Methodological caveat surfaced by the study: the standard Push-T evaluation is easier than it looks (84% of test goals lie on paths demonstrations already travel; official 50-episode score 68% vs 44% on 250 fresh episodes; one seed flip moved 38/250 outcomes). Remaining gap: goals *against* the direction of the data — the open problem is a high level that proposes subgoals beyond demonstrations (vs H-JEPA, arXiv:2610.06805, which only matches flat LeWM on Push-T). See also [[concepts/jepa-planning-methods]].

## Related Research

| Paper | arXiv | Key Contribution |
|---|---|---|
| I-JEPA | 2301.08243 | Image-based JEPA for self-supervised learning (Meta) |
| VICReg | 2105.04906 | Variance-Invariance-Covariance Regularization |
| VICRegL | 2210.01571 | Local + global feature learning extension |
| LeWorldModel | 2603.19312 | Stable end-to-end JEPA from pixels (~15M params) |
| Factorized Latent Dynamics for Video JEPA | 2605.17165 | Auxiliary objectives for video JEPA |

## Significance

JEPA represents a promising direction for [[concepts/world-models-science|world model]] research that could lead to more sample-efficient, interpretable models. The approach is central to LeCun's vision of autonomous machine intelligence and contrasts with end-to-end generative approaches dominant in the field.

## External Links
- [LeMario Project Page](https://www.benjamin-bai.com/projects/lemario)
- [LeMario GitHub](https://github.com/benyebai/LeMario)
- [I-JEPA Paper](https://arxiv.org/abs/2301.08243)
- [LeWorldModel Paper](https://arxiv.org/abs/2603.19312)
- [Haddy Alchaer, "After 600 experiments, here's what I discovered about JEPA world models" (Nov 2026)](https://haddyalchaer.com/jepa)
- [H-JEPA Paper](https://arxiv.org/abs/2610.06805)
