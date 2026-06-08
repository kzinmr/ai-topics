---
title: "OPD Failure Modes"
type: concept
created: 2026-06-08
updated: 2026-06-08
tags:
  - training
  - distillation
  - failure-modes
  - research
aliases:
  - OPD failure modes
  - distillation failure modes
sources:
  - raw/articles/2026-06-08_chinmaykarkar_opd-survey-2026.md
  - https://chinmaykarkar.com/blog/OPD_blog/
  - https://arxiv.org/abs/2604.00626
  - https://arxiv.org/abs/2603.25562
  - https://arxiv.org/abs/2604.16830
related:
  - concepts/on-policy-distillation
  - concepts/on-policy-self-distillation
  - entities/chinmay-karkar
---

# OPD Failure Modes

> **OPD Failure Modes** are the recurring failure patterns in On-Policy Distillation and On-Policy Self-Distillation methods, formalized by recent surveys (Song & Zheng 2026, Fu et al. 2026, Zhang et al. 2026).

## Estimator-Level Failures

### Token-Level KL is a Fragile Proxy
Every OPD/OPSD method optimizes a *token-level sampled* reverse KL on student rollouts, but the theory wants to minimize the *sequence-level* reverse KL. The token-level estimator is biased relative to the sequence-level one, and the bias worsens with stronger future-reward coupling — exactly the regime long-horizon reasoning lives in. This also inflates gradient variance and destabilizes training.

### Prefix Drift and the Unreliable Teacher
Once the student's prefix drifts a few tokens past the teacher's typical support, the teacher's next-token distribution skews to extrapolate into regions it was never trained on. The teacher places near-uniform or weirdly spiky mass on irrelevant tokens, and the student distills that noise.

### Gradient SNR Collapse
On prompts where the student's pass rate is near zero, every rollout contains an early error, the teacher's signal is essentially noise, and the per-prompt gradient SNR vanishes. The model learns nothing from exactly the prompts it most needs to learn from.

### Local Teachability Collapse
Even when the teacher stays well-calibrated, the token-level KL gradient carries almost no signal. The teacher is still right about which token is best, just barely, and the signal degrades gradually. The optimal supervision window is trajectory-specific rather than positional.

## Token-Level Issues

### Imbalanced Supervision
A small number of tokens carry most of the loss while the rest contribute near-zero gradient. An "average" reduction across a sequence is dominated by a few outliers.

### Rock Tokens
Up to 18% of tokens in a trained OPD model exhibit persistently high loss even after the rest of the run has saturated. They absorb a disproportionate share of the gradient norm because of their high occurrence frequency. The student cannot, and probably should not, internalize them from the teacher.

### Tokenizer Mismatch
When teacher and student don't share a tokenizer (or disagree on special tokens and chat templates), naive token alignment produces silent corruption that looks like a normal training run but degrades performance.

## Distributional Failures

### Diversity Collapse
As the student concentrates mass on high-quality outputs, it necessarily shrinks coverage of the teacher's full output distribution: Pass@1 goes up, Pass@k goes down. In aggressive reverse-KL OPD this shows up as the student collapsing onto a single reasoning strategy per prompt.

## OPSD-Specific Failures

### Privileged Information Gap
The teacher's *next-token confidence* is computed under information the deployed model literally cannot see. Teacher-conditioned success is generally not a valid target for deployment-time confidence.

### Epistemic Suppression
OPSD methods that compress reasoning traces (like CRISP) disproportionately delete hedging phrases and uncertainty markers. The result is a shorter trace that is also more confidently wrong on the steps it elided.

### Teacher Capability Assumption
Every method assumes a teacher that, given PI, is meaningfully better than the no-PI student. If that gap is small the whole pipeline degenerates into dense noise rather than dense signal.

## Author's Analysis (Chinmay Karkar)

The deepest issue is **proxy mismatch**: KL between PI-conditioned and no-PI views mixes true informational gain with estimator noise from unequal information states. Distillation often imitates one specific PI instantiation when the real goal is **PI-invariant skill transfer**.

A better target is the average behavior over a family of valid PIs:
$$\bar{\pi}(\cdot \mid x) = \mathbb{E}_{r \sim p(r \mid x)} [\pi_\theta(\cdot \mid x, r)]$$

This object captures skill without overfitting to one hint realization. Shared-rule PI transfers better than instance-specific PI. Robust OPSD will likely be hybrid: self-distilled magnitudes anchored by external verifiers.

## Related Pages

- [[concepts/on-policy-distillation]] — Core OPD concept
- [[concepts/on-policy-self-distillation]] — OPSD concept
- [[entities/chinmay-karkar]] — Survey author
