---
title: "Energy-Based Reasoners (EBR)"
created: 2026-11-19
updated: 2026-11-19
type: concept
tags:
  - reasoning-model
  - transformer-architecture
  - inference
  - research
  - ai-in-science
  - optimization
status: L3
confidence: medium
aliases: [EBR, energy-based reasoner, energy-based reasoning]
sources:
  - raw/articles/2026-11-18_energy-based-reasoners.github.io_ebr-sudoku.md
  - https://news.ycombinator.com/item?id=50543989
---

# Energy-Based Reasoners (EBR)

**Energy-Based Reasoners (EBRs)** are a class of looped/recurrent reasoning models introduced in November 2026 that learn an explicit *energy function* over latent reasoning states and formulate the loop's iterative updates as **gradient descent on that energy**. The result is a small model that scores its own candidate predictions without an external verifier, and gets a natural stopping signal for how long to keep looping. The headline project — a 1.8M-parameter EBR reaching **99.9% accuracy on Sudoku-Extreme while using ~345–385× less inference compute than the next-best model** — hit Hacker News on 2026-11-18 (311 points, HN id 50543989) as "385x more efficient inference."

## The problem: looped reasoners have no progress measure

Recurrent/looped architectures (a single block iterated to build effective depth) are a powerful inductive bias for multi-step reasoning in latent space. But existing looped models are **not guided by an explicit measure of progress** — there is no principled signal for *when to stop looping*. Typically the loop count is fixed at train time or controlled by a hand-tuned confidence threshold, which is brittle on hard instances and wasteful on easy ones.

## The mechanism

EBRs combine two ideas:

1. **Recurrent reasoning block** — as in looped transformers / latent-space reasoners, iterated to scale effective depth.
2. **Energy function E(state)** — learned jointly, serving three roles at once:
   - **Value**: its value scores candidate predictions *without requiring an external verifier* — the model is its own critic.
   - **Gradient**: its gradient guides refinement of the latent reasoning state (the loop step is a descent step).
   - **Stopping**: convergence of the energy gives a natural, per-instance stopping signal — low-energy states are "done".

This makes the loop an *optimization process over an internal energy landscape* rather than a fixed number of forward passes, aligning with the broader energy-based-models (EBM) research program.

## Results (paper-reported)

| Task | Result |
|---|---|
| Sudoku-Extreme | 99.9% accuracy at 1.8M params, ~345× less inference compute than the next-best model (HN title quotes 385×) |
| N-Queens | State-of-the-art coverage, near-100% single-sample accuracy |
| Graph Coloring | State-of-the-art coverage, near-100% single-sample accuracy |

**Confidence caveat:** all numbers are author-reported from the project page / paper, not independently replicated as of 2026-11-19. The compute-efficiency multiplier is relative to a chosen "next-best" baseline, so the 345×/385× figure is sensitive to baseline selection.

## Why it matters

- **Verifier-free self-scoring** removes the external-reward-model dependency that dominates the test-time-scaling / verifier-guided search literature (compare process reward models and best-of-N).
- **Per-instance adaptive compute** is the concrete mechanism behind "reasoning budgets should track problem difficulty," an open issue in [[concepts/reasoning-models|reasoning models]] and token economics.
- **Tiny models for structured search**: 1.8M parameters beating large baselines on Sudoku/N-Queens/graph coloring suggests that for constraint-satisfaction reasoning, architecture (energy + loop) matters far more than scale — a counterpoint to pure-scaling narratives.

## Relation to LeCun's EBM program

The paper operationalizes precisely the "energy-based reasoning" direction Yann LeCun has championed since leaving Meta to found AMI Labs — non-generative, energy/minimization-based models as an alternative to autoregressive LLM reasoning. See [[entities/yann-lecun]] and [[concepts/jepa-planning-methods|JEPA / world models]].

## Authors & venue

William Chen (Duke), Alexi Gladstone (UIUC), Zeyu Li (Duke), Heng Ji (UIUC), Yilun Du (Harvard). Project page `energy-based-reasoners.github.io`, with an arXiv preprint and code linked from it. (Peer-review status unverified at time of writing — treat as preprint.)

## Related pages

- [[entities/yann-lecun]] — EBM advocate; AMI Labs energy-based reasoning program
- [[concepts/jepa-planning-methods]] — LeCun's world-model / energy-based planning alternative
- [[concepts/reasoning-models]] — the autoregressive test-time-scaling paradigm EBR contrasts with
- [[concepts/token-economics]] — adaptive per-instance compute and inference cost
