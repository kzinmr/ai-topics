---
title: "Scaling Laws, Carefully"
author: Lilian Weng
date: 2026-06-24
source: https://lilianweng.github.io/posts/2026-06-24-scaling-laws/
type: article
tags:
  - training
  - deep-learning
  - survey
  - benchmark
  - evaluation
  - methodology
---

# Scaling Laws, Carefully

**Author:** Lilian Weng
**Published:** 2026-06-24
**Source:** https://lilianweng.github.io/posts/2026-06-24-scaling-laws/

---

Scaling laws are one of the most critical empirical findings in deep learning. The observation is simple in form: the training loss decreases predictably as we scale up model size, dataset size, and compute, following a power-law curve, which appears as a straight line on a log-log plot. We can view scaling laws as a framework for describing the relationship between compute, loss, model size and data; at its core, it is about how to allocate precious compute optimally between model size (N) and dataset size (D).

This predictability makes scaling laws highly valuable in practice. A common workflow is to fit scaling laws on a handful of small runs and then extrapolate to estimate the token and compute requirements for larger models.

| Symbol | Note |
| --- | --- |
| N | Model size, measured in parameter count. |
| D | Training dataset size, usually measured in token count. |
| C | Training compute in FLOPs. C ≈ 6ND (Kaplan et al. 2020), where 2ND accounts for the forward pass and 4ND for backpropagation. |
| E | Irreducible loss |
| L, L̂ | Test loss / test loss prediction function |
| ε | Generalization error |

## Early Days: ML Loss Predictability

The predictability of generalization error with scale had already been investigated before scaling laws became a mainstream concept.

**Amari et al. (1992)** derived four types of learning curves using a Bayesian approach and the annealed approximation:
1. Deterministic learning algorithm, noiseless data, one unique solution: L ∝ 1/N
2. Deterministic learning algorithm, noiseless data, multiple equivalent solutions: faster learning per data point
3. Deterministic learning algorithm, noisy data: harder learning due to noise
4. Stochastic learning algorithm, noisy data: irreducible loss from capacity limits

All four types follow a power law: L(N) = AN^{-α} + E

**Hestness et al. (2017)** — one of the earliest empirical studies — observed across four domains (NMT, image classification, language modeling, speech recognition):
- Generalization error scales as a power law across factors (e.g. data size)
- Architecture changes the offset but not the exponent of the power-law fit
- The slope of the power law appears to be a property of the problem domain, not the model architecture
- Learning curves break into three stages: small-data region, power-law region, irreducible-error region

**Rosenfeld et al. (2020)** modeled error as a joint function of both model size and data size across diverse architectures (ResNet, WRN, LSTM, Transformer) and optimizers (Adam, SGD). They combined single-axis power laws into a joint form: L(N, D) = (Nc/N)^αN + (Dc/D)^αD + E

## Scaling Laws in Data-Infinite Region

### Kaplan et al.'s Scaling Laws (2020)

Kaplan et al. popularized scaling laws in the language modeling community. Key findings:

- Loss scales as a power law with N, D, and C individually; all three must scale in tandem
- Training curves follow predictable power laws roughly independent of model size
- Larger models are more sample-efficient
- Architectural details (width, aspect ratio) matter less than sheer scale
- Given fixed compute, it's more efficient to train a very large model and stop before convergence

**Joint dependence equation:** L(N, D) = [(Nc/N)^αN/αD + Dc/D]^{αD} + E

**Compute-optimal allocation (Kaplan):** For 10x compute → scale model ~5.5x, tokens ~1.8x. αN/αD ≈ 0.74/0.03 → model size should grow faster than dataset size.

**Training FLOPs approximation:** C ≈ 6ND (forward: 2ND, backward: 4ND)

### Chinchilla Scaling Laws (Hoffmann et al. 2022)

The Chinchilla paper studied the optimal model size vs token count under fixed compute budget with more careful experimental design.

**Three methods for fitting:**
1. **Fix model sizes, vary token budget** — record minimal loss per FLOP budget
2. **IsoFLOP profiles** — fix compute budget, plot loss vs parameter count; each curve's minimum flags optimal model size
3. **Parametric fit** — fit L(N, D) = E + A/N^α + B/D^β using Huber loss + L-BFGS

**Key result:** α ≈ β, meaning model size and training tokens should scale at equal rates. For every doubling of model size, also double training tokens.

**Chinchilla vs Gopher demonstration:** Under same compute as Gopher (280B params, 300B tokens), Chinchilla (70B params, 1.4T tokens) — 4x smaller, 4x more data — outperformed across the board.

### Reconciling Kaplan and Chinchilla

**Disagreements:**
- Kaplan: N ∝ C^0.74, D ∝ C^0.03 → grow model faster than data
- Chinchilla: N ∝ C^0.50, D ∝ C^0.50 → equal scaling

**Why they disagree:**
1. **Small model bias:** Kaplan experimented on smaller models (768M–1.5B); Chinchilla reached 10x+ larger scales. Log-log extrapolation amplifies small fit differences.
2. **Embedding parameter counting:** Kaplan excluded embeddings (N_nonemb), Chinchilla included total params (N_total). Pearce & Song (2024) showed the relationship between N_total and N_nonemb is not a clean power law, and the local exponent α(N) ≈ 0.73 in Kaplan's model size range.

## Why Power Law?

Two hypotheses:
1. **Sharma & Kaplan (2020):** Language modeling as regression on a low-dimensional data manifold. Finer partition → smaller error. Resolution scales as N^{-1/d}.
2. **Michaud et al. (2023) / Brill (2024):** Skills learned in discrete "quantized" chunks with power-law frequency distribution. Common skills first, rare skills later → smooth power-law decay.

## Scaling Laws in Data-Limited Region

Classic scaling laws assume unlimited unique data. In practice, high-quality data is finite.

### Hernandez et al. (2022)
- Studied controlled repetition: 90% non-repeated + 10% repeats
- Observed double-descent phenomenon: test loss can worsen then improve with repetition
- Memorization of repeated data causes flat/increasing trend mid-training

### Muennighoff et al. (2023)
- ~400 experiments, 10M–9B params, up to 900B tokens, up to 1500 epochs
- Decomposed tokens into unique tokens U and repeats r
- Effective data: D_eff = U · (1 - exp(-r/h)) — token value decays exponentially with repetition
- Key finding: excess parameters decay faster in value than repeated data → allocate more on epochs than parameters
- Weakness: underestimates final test loss of failing models

### Lovelace et al. (2026)
- ~300 models, 15M–1B params, 50M–6B unique tokens
- Larger models are MORE sensitive to repetition
- Added explicit overfitting penalty: L_overfit = γ · (N/D)^α · r^β
- Strong weight decay reduces the overfitting penalty from data repetition

## Trickiness of Fitting Scaling Laws in Reality

Scaling law fitting is sensitive to:
- How you count parameters
- Precision rounding
- Loss aggregation (sum vs average)
- Fit region (small vs medium vs all models)

**Besiroglu et al. (2024)** found issues in Chinchilla's method 3:
- High loss scale in L-BFGS-B minimizer from averaging instead of summing Huber loss → premature termination
- Rounded α, β to 2 digits → derived exponents looked more off than they were

## References

1. Amari et al. (1992) "Four Types of Learning Curves" Neural Computation
2. Hestness et al. (2017) "Deep Learning Scaling is Predictable, Empirically" arXiv:1712.00409
3. Rosenfeld et al. (2020) "A Constructive Prediction of the Generalization Error Across Scales" ICLR 2020, arXiv:1909.12673
4. Kaplan et al. (2020) "Scaling Laws for Neural Language Models" arXiv:2001.08361
5. Sharma & Kaplan (2020) "A Neural Scaling Law from the Dimension of the Data Manifold" arXiv:2004.10802
6. Bahri et al. (2021) "Explaining Neural Scaling Laws" arXiv:2102.06701
7. Rae et al. (2021) "Scaling Language Models: Methods, Analysis & Insights from Training Gopher" arXiv:2112.11446
8. Hoffmann et al. (2022) "Training Compute-Optimal Large Language Models" NeurIPS 2022, arXiv:2203.15556
9. Hernandez et al. (2022) "Scaling Laws and Interpretability of Learning from Repeated Data" arXiv:2205.10487
10. Michaud et al. (2023) "The Quantization Model of Neural Scaling" NeurIPS 2023, arXiv:2303.13506
11. Muennighoff et al. (2023) "Scaling Data-Constrained Language Models" NeurIPS 2023, arXiv:2305.16264
12. Besiroglu et al. (2024) "Chinchilla Scaling: A Replication Attempt" arXiv:2404.10102
13. Pearce & Song (2024) "Reconciling Kaplan and Chinchilla Scaling Laws" TMLR 2024, arXiv:2406.12907
14. Brill (2024) "Neural Scaling Laws Rooted in the Data Distribution" arXiv:2412.07942
15. Lovelace et al. (2026) "Prescriptive Scaling Laws for Data Constrained Training" arXiv:2605.01640
