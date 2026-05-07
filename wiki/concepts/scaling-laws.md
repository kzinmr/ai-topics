---
title: "Scaling Laws"
type: concept
aliases:
  - scaling-laws
  - neural-scaling-laws
  - chinchilla-scaling
created: 2026-04-25
updated: 2026-05-05
tags:
  - concept
  - training
  - pretraining
  - data-quality
  - compute-optimal
sources:
  - raw/articles/2026-05-04_infolaw-information-scaling-laws.md
  - https://arxiv.org/abs/2605.02364
related:
  - chinchilla
  - pretraining
  - data-quality
---

# Scaling Laws

**Scaling Laws** describe the predictable relationship between model performance (loss) and training resources — compute, data, and model size. They guide optimal resource allocation for LLM pretraining.

## Classic Scaling Laws

### Kaplan et al. (2020) — OpenAI
- Power-law relationship between loss and compute, dataset size, and model parameters.
- Established that larger models are more sample-efficient.

### Chinchilla (2022) — DeepMind
- **Optimal compute allocation**: Model parameters and training tokens should scale roughly equally.
- A compute-optimal 70B model trained on 1.4T tokens matches a 280B model trained on 300B tokens.
- Formula: $N_{opt} \propto C^{0.5}$, $D_{opt} \propto C^{0.5}$

## Modern Extensions

### InfoLaw: Information Scaling Laws (Liu et al., ICML 2026)

**InfoLaw** extends scaling laws to account for **data quality, mixture weights, and repetition** — factors that classic laws assume away.

#### Core Innovation
InfoLaw treats pretraining as **information accumulation** rather than token counting:
1. **Quality** determines information density per token.
2. **Repetition** induces scale-dependent diminishing returns.
3. **Model size** interacts with both to determine final loss.

#### Key Findings
- Predicts performance on **unseen data recipes** at larger scales
- Accuracy: **0.15% mean absolute error**, 0.96% max absolute error in loss prediction
- Validated up to **7B parameters, 425B tokens**
- Identifies the "sweet spot" where high-quality data benefits are outweighed by repetition harms

#### Practical Implications
- **Overtraining optimization**: Find optimal repetition levels without trial runs
- **Data mixture selection**: Predict optimal quality-weighting for a given compute budget
- **Extrapolation**: Reliably predict large-scale performance from small-scale experiments

> "InfoLaw predicts performance on unseen data recipes and larger scale runs with 0.15% mean and 0.96% max absolute error in loss."

## Data-Centric AI Era

The shift from Chinchilla (token-count) to InfoLaw (information-density) reflects the broader transition to **data-centric AI**:
- High-quality data is scarce → must maximize utility per token
- Overtraining is increasingly common → must model repetition decay
- Recipe selection is underdetermined → must predict without expensive trials

## Related Concepts

- [[altman-three-observations]] — Economic framework: logarithmic scaling, 10x/year cost deflation, super-exponential value
- [[pretraining]] — LLM pretraining methodology
- [[chinchilla]] — Optimal compute allocation
- [[data-quality]] — Data curation and quality filtering
- [[overtraining]] — Training beyond unique data
- [[compute-optimal-training]] — Finding optimal model size / data ratios

## Sources

- [InfoLaw: Information Scaling Laws](https://arxiv.org/abs/2605.02364) — Liu et al., ICML 2026
- [Raw article](raw/articles/2026-05-04_infolaw-information-scaling-laws.md)
- [Chinchilla Paper](https://arxiv.org/abs/2203.15556) — Hoffmann et al., NeurIPS 2022
