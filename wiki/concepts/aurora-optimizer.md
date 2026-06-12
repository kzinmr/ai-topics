---
title: "Aurora Optimizer"
created: 2026-05-19
updated: 2026-05-19
type: concept
tags:
  - optimization
  - training
  - fine-tuning
  - open-source
sources:
  - raw/newsletters/2026-05-18-import-ai-457-ai-stuxnet-cursed-muon-optimizer-and-positive-alignment.md
  - https://blog.tilderesearch.com/blog/aurora
  - https://github.com/tilde-research/aurora-release
---

# Aurora Optimizer

**A leverage-aware optimizer for rectangular matrices** developed by Tilde Research (May 2026), designed to fix a hidden flaw in the [[concepts/adam-optimizer|Muon optimizer]]: the silent death of MLP neurons during training.

## The Problem: Muon's Neuron Death

The [[concepts/adam-optimizer|Muon optimizer]] — which earned praise for beating AdamW on the nanoGPT speedrun — inherits **row-norm anisotropy on tall matrices** (up and gate projections in MLP layers). This causes some neurons to receive persistently small updates early in training and fail to recover:

- By step 500, **more than 25% of MLP neurons are effectively dead**, producing a sharply bimodal distribution of leverage scores
- Dead neurons starve downstream layers of gradient flow, propagating dysfunction throughout the model
- Row-normalizing updates (NorMuon/U-NorMuon) fixes this but sacrifices the precision of the polar factor — which is both empirically and theoretically important

## Aurora's Solution

Aurora reframes the update selection problem: **what is the correct update under the joint constraint of left semi-orthogonality and uniform row norms?** It solves for steepest descent under both constraints simultaneously, achieving row uniformity without sacrificing orthogonalization precision.

For tall matrices, Aurora solves: U* = argmax_U Tr(G^T U) s.t. U^T U = I_n, ‖U_i‖² = m/n ∀i

The solution forces all singular values of U to equal 1, producing a valid semi-orthogonal update — not a corrupted one.

**Two implementations:**
- **Vanilla Aurora**: Practical drop-in replacement; untuned, only 6% overhead over traditional Muon
- **Riemannian Aurora**: Constrained gradient projection on the combined Stiefel/equal-row-leverage manifold

For wide and square matrices, row normality is already implied by orthogonality — Aurora leaves those parameters unchanged.

## Benchmarks

| Setting | Aurora | Muon | NorMuon |
|---------|--------|------|---------|
| 1.1B param, ~100B tokens | **loss 2.26** | 2.31 | 2.33 |
| MMLU (1.1B) | **+10 points** over Muon | baseline | — |
| 600M (independent: Pleias/Doria) | **best** | worse | worse |
| modded-nanoGPT speedrun | **3175 steps (SoTA)** | 3500 | 3225 (prior SoTA) |

Aurora's advantage grows **monotonically with MLP expansion factor** — wider MLPs amplify the exact pathology Aurora corrects. This makes it particularly effective for dense transformers with typical 4x+ expansion factors.

For MoE architectures with smaller per-expert hidden dimensions, the neuron death pathology is expected to be less severe (though not absent for tall experts).

## Key People

- **Alec Dewulf, Dhruv Pai, Li Yang, Ashley Zhang, Ben Keigwin** — Tilde Research

## Related Pages

- [[concepts/adam-optimizer]] — Adam/AdamW, the current standard optimizer for LLM training
- [[concepts/deepseek-v4]] — Uses Muon optimizer; potential beneficiary of Aurora
- [[concepts/post-training/prime-rl-post-training]] — Post-training optimization context (Prime Intellect)
- [[concepts/modded-nanogpt]] — nanoGPT speedrun benchmark where Aurora set SoTA
