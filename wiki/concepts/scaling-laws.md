---
title: "Scaling Laws"
created: 2026-06-26
updated: 2026-08-09
type: concept
tags:
  - training
  - model
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
  - "[[raw/articles/2026-08-07_gilesthomas-chinchilla-check]]"
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

## Chinchilla Re-Evaluation (Giles Thomas, Aug 2026)

Giles Thomas conducted a practical re-evaluation of the Chinchilla heuristic (20 tokens per parameter) using GPT-2-style models at ~163M parameter scale. His experiment tested whether scaling model size and tokens equally truly outperforms simply overtraining a smaller model on more data.

**Experimental Setup**: Thomas trained GPT-2-style models (no weight-tying, no QKV bias) with three configurations on a held-back test set:
- **jax-gpt2-chinchilla**: 163M params, trained on ~3.26B tokens (20 tokens/param) — Chinchilla-optimal baseline
- **jax-gpt2-2x-chinchilla**: same size, trained on ~6.52B tokens (40 tokens/param) — overtrained
- **jax-gpt2-2-epoch-chinchilla**: same size, ~3.26B unique tokens repeated (2 epochs) — compute-matched control

The overtrained models achieved test loss of ~3.325 vs 3.419 for the Chinchilla-optimal baseline, confirming that overtraining improves absolute performance on a fixed-size model.

**Chinchilla-Scaled Comparison**: To match the compute budget of the overtrained models (~7.09 × 10^18 FLOPs), Thomas scaled both parameters and tokens by √2 (since FLOPs ≈ 6ND). Target: ~231M params trained on ~4.6B tokens. He trained two architectural variants:
- **slightly-larger**: 15 layers, d_emb=896, 14 heads → ~236M params (+2.21% over target, ~4.6% more FLOPs)
- **slightly-smaller**: 14 layers, d_emb=896, 14 heads → ~226M params (-1.97% under target, ~4% fewer FLOPs)

**Key Results** (test loss, lower is better):

| Model | Test Loss | Improvement vs overtrained |
|-------|-----------|---------------------------|
| slightly-larger | 3.280 | 1.35% |
| slightly-smaller | 3.293 | 0.962% |
| jax-gpt2-2x-chinchilla | 3.325 | — (baseline) |
| jax-gpt2-chinchilla | 3.419 | — |

Both Chinchilla-scaled models beat the overtrained ones. Notably, the slightly-smaller model achieved this despite using ~4% less compute — a strong directional signal. However, the improvement (~0.96–1.35%) was small enough that it could fall within the noise of random weight initialization: an earlier three-seed analysis estimated 3σ ≈ 0.026, comparable to the 0.032–0.045 absolute gap. Thomas characterized this as a "tentative success" — directional confirmation, not a slam dunk.

**Practical Insight — Scaling Models Is Non-Trivial**: A key lesson from the experiment is that "scale N and D equally" glosses over the real engineering difficulty. With d_emb constrained to multiples of 64 (matching GPT-2's head:dimension ratio of 1/64), granularity is coarse — going from d_emb=896 to 832 overshoots by 9.25%. Even with only two architectural dials (layers, embedding dimension), hitting an exact target parameter count required curve-fitting to GPT-2 paper configurations and iterative spreadsheet work. FLOPs estimation using Chinchilla Appendix F formulas was necessary because embedding parameters dominate at small scales.

**Implications for Practitioners**: Chinchilla's core claim held directionally — equal scaling of N and D produced better models than overtraining alone. However, the marginal gain (~1%) must be weighed against the engineering friction of designing correctly-sized architectures. For deployment-constrained scenarios (e.g., mobile devices with fixed RAM budgets), overtraining a smaller model may remain the pragmatic choice even if it is not compute-optimal in theory. Thomas noted that the experiment used a single random seed for each scaled model vs. a different seed for the overtrained models, so a multi-seed study would be needed for statistical rigor.


## See Also

- [[concepts/chinchilla|Chinchilla]]
- [[concepts/compute-optimal-training|Compute-Optimal Training]]
- [[concepts/training|Training]]
- [[concepts/knowledge-distillation|Knowledge Distillation]]
- [[entities/lilian-weng|Lilian Weng]] — comprehensive survey author
