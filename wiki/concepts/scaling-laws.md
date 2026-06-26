---
title: "Scaling Laws"
created: 2026-06-26
updated: 2026-06-26
type: concept
tags:
  - training
  - deep-learning
  - survey
  - benchmark
  - evaluation
  - inference
  - methodology
sources:
  - "[[raw/articles/2026-06-24_lilianweng_scaling-laws-carefully]]"
  - https://arxiv.org/abs/2001.08361
  - https://arxiv.org/abs/2203.15556
  - https://arxiv.org/abs/2406.12907
  - https://arxiv.org/abs/2305.16264
  - https://arxiv.org/abs/2605.01640
related:
  - "[[entities/lilian-weng]]"
  - "[[concepts/chinchilla]]"
  - "[[concepts/compute-optimal-training]]"
---

# Scaling Laws

Scaling laws are empirical power-law relationships describing how [[concepts/training|training]] loss decreases predictably as model size (N), dataset size (D), and compute (C) are scaled up. They appear as straight lines on log-log plots and enable extrapolation from small runs to predict requirements for larger models.

## Core Formulation

The joint scaling law (Kaplan et al. 2020):

**L(N, D) = [(Nc/N)^αN/αD + Dc/D]^{αD} + E**

Where:
- **N** = model size (parameter count)
- **D** = dataset size (token count)
- **C ≈ 6ND** = training FLOPs (2ND forward + 4ND backward)
- **E** = irreducible loss
- **αN, αD** = fitted exponents

The extent of overfitting depends predominantly on the ratio N^αN / D, meaning data must grow proportionally with model size.

## Historical Development

### Early Foundations (1992–2020)
- **Amari et al. (1992)**: Derived four types of learning curves, all following power laws
- **Hestness et al. (2017)**: First large-scale empirical study across 4 domains (NMT, image, language, speech). Found architecture changes the offset but not the exponent — the slope is a property of the problem domain
- **Rosenfeld et al. (2020)**: Joint model of error as function of both N and D across ResNet, WRN, LSTM, Transformer

### Kaplan et al. (2020)
Popularized scaling laws for Transformer language models. Key conclusions:
- Loss scales as power law with N, D, C individually
- Larger models are more sample-efficient
- Architectural details matter less than sheer scale
- **Compute-optimal allocation**: N ∝ C^0.74, D ∝ C^0.03 → model size should grow faster than data

### Chinchilla (Hoffmann et al. 2022)
Overturned Kaplan's allocation recommendation with three complementary methods:
- **Method 1**: Fix model sizes, vary token budget
- **Method 2**: IsoFLOP profiles — each curve's minimum flags optimal model size
- **Method 3**: Parametric fit with Huber loss + L-BFGS

**Key result**: α ≈ β, so **N and D should scale equally** (N ∝ C^0.50, D ∝ C^0.50). Chinchilla (70B, 1.4T tokens) outperformed Gopher (280B, 300B tokens) under same compute — demonstrating most large models were undertrained.

### Reconciling Kaplan and Chinchilla (Pearce & Song 2024)
Two explanations for the disagreement:
1. **Small model bias**: Kaplan's experiments were on smaller models; log-log extrapolation amplifies fit differences
2. **Embedding counting**: Kaplan excluded embeddings (N_nonemb), Chinchilla included total (N_total). The local exponent α(N) ≈ 0.73 in Kaplan's model size range, converging to Chinchilla's 0.50 at larger scales

## Why Power Law?

Two leading hypotheses:
1. **Data manifold dimensionality** (Sharma & Kaplan 2020): Language modeling as regression on a d-dimensional manifold. Resolution scales as N^{-1/d}
2. **Quantized skill acquisition** (Michaud et al. 2023): Skills learned in discrete chunks with power-law frequency distribution. Common skills first, rare later

## Data-Limited Scaling

When unique high-quality data is finite, classical infinite-data assumptions break down.

### Repetition Effects
- **Hernandez et al. (2022)**: Controlled repetition causes double-descent in test loss
- **Muennighoff et al. (2023)**: Token value decays exponentially with repetition. Effective data D_eff = U · (1 - exp(-r/h)). Excess parameters decay faster than repeated data → prefer more epochs over more parameters
- **Lovelace et al. (2026)**: Larger models are MORE sensitive to repetition. Added explicit overfitting penalty L_overfit = γ · (N/D)^α · r^β. Strong weight decay reduces the penalty

## Practical Challenges

Scaling law fitting is sensitive to:
- Parameter counting methodology (embedding inclusion)
- Loss precision and aggregation (sum vs average)
- Fit region (small vs large models)
- Undertrained small runs biasing the fit

**Besiroglu et al. (2024)** found concrete issues in Chinchilla's method 3: averaging Huber loss instead of summing caused premature L-BFGS termination; rounding to 2 digits made derived exponents look worse.

## Implications

- Enables **compute budget planning** from small-scale experiments
- Guides **data collection strategy** (how much unique data needed)
- Informs **training efficiency** (when to stop, how to balance N and D)
- Foundation for [[concepts/compute-optimal-training|compute-optimal training]] strategies
- Critical input for [[concepts/ai-economics|AI economics]] and infrastructure planning

## See Also

- [[concepts/chinchilla|Chinchilla]]
- [[concepts/compute-optimal-training|Compute-Optimal Training]]
- [[concepts/training|Training]]
- [[concepts/knowledge-distillation|Knowledge Distillation]]
- [[entities/lilian-weng|Lilian Weng]] — comprehensive survey author
