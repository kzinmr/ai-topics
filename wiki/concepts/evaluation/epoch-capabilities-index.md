---
title: "Epoch Capabilities Index (ECI)"
created: 2026-05-30
updated: 2026-05-30
type: concept
tags:
  - benchmark
  - evaluation
  - methodology
  - lab
sources: []
---

# Epoch Capabilities Index (ECI)

The **Epoch Capabilities Index (ECI)** is a composite metric developed by [[entities/epoch-ai]] that combines scores from 40+ distinct benchmarks into a single "general capability" scale. It enables meaningful comparisons between AI models even over timespans long enough for individual benchmarks to reach saturation.

## Methodology

The ECI is built on an **Item Response Theory (IRT)** model — the same statistical framework used in IQ testing and educational assessment. The core insight: instead of comparing models on individual benchmarks (which saturate and become uninformative), stitch together benchmarks of varying difficulties into a unified scale.

### Three Latent Parameters

1. **Model capability (C_m)**: A single number representing each model's underlying capability (this becomes the ECI score)
2. **Benchmark difficulty (D_b)**: How hard each benchmark is overall
3. **Benchmark slope (α_b)**: How quickly the benchmark saturates — how rapidly performance changes as capability increases around the difficulty threshold

The relationship is modeled as:

```
performance(m, b) = σ(α_b × [C_m - D_b])
```

Where σ is the logistic (sigmoid) function. This produces an S-curve with three regimes:
- **Regime 1**: Model capability << benchmark difficulty → performance at random baseline
- **Regime 2**: Model capability ≈ benchmark difficulty → performance grows proportionally to capability
- **Regime 3**: Model capability >> benchmark difficulty → benchmark saturated (~100%)

### Scale Calibration

The ECI scale is calibrated so that:
- **Claude 3.5 Sonnet = 130**
- **GPT-5 = 150**

The scale is linear (a 10-point jump is equally "impressive" regardless of where it occurs), but benchmark accuracy is not linearly related to ECI points due to differing difficulties and slopes. As with Elo scores, there is no maximum achievable ECI.

A **5-point gain in ECI** roughly corresponded to a doubling of the METR Time Horizon at the time of ECI's launch.

### Bootstrap Uncertainty

ECI scores are estimated with uncertainty. Epoch AI uses bootstrap resampling (resampling benchmark scores with replacement and refitting the model) to generate confidence intervals. An open-weight model is considered to have "caught up" to a previous SOTA if it outperforms that SOTA in at least 5% of paired bootstrap samples.

## Domain-Specific ECIs

The ECI framework also produces domain-specific indices:
- **SWE ECI**: Uses only software engineering benchmarks
- **Math ECI**: Uses only math benchmarks

Domain-specific ECIs keep the benchmark difficulty and slope parameters from the general ECI fit, and only refit the model capability parameters. This means domain-specific scores are on the same scale as the general ECI, allowing direct comparison (e.g., a model with higher math ECI than general ECI performs better on math than on average). However, this scaling means domain ECIs cannot be used to assess progress trends across domains — they are all scaled to increase at the same overall pace as the general ECI.

## Data Coverage

As of 2026:
- **1,123+ distinct evaluations** across **147+ models**
- **37-40+ underlying benchmarks** (the count grows as new benchmarks are added)
- Minimum 4 benchmark evaluations required for a model to receive an ECI score
- Minimum 2 benchmarks within a domain required for domain-specific ECI

Sources include:
- Epoch AI internally run evaluations
- Benchmark creator-reported scores
- Model developer-reported scores (model cards, technical reports)

## Key Findings from ECI Analysis

### AI Capabilities Progress Has Accelerated

Using ECI data from Dec 2021 to Dec 2025, Epoch AI fitted a two-segment piecewise linear model and found:
- **Pre-breakpoint slope (before April 8, 2024)**: 8.337 ECI/year
- **Post-breakpoint slope (after April 8, 2024)**: 15.459 ECI/year
- **Acceleration factor**: 1.85×
- Bayes factor of 10^9 in favor of the piecewise model over simple linear regression

### Open vs. Closed Model Gap

See [[concepts/open-vs-closed-model-gap]] for the full analysis. Key findings:
- Jan 2023–Oct 2025: 3 months lag (~7 ECI points)
- Jan 2026–May 2026: 4 months lag (8 ECI points, 90% CI: 7-11)

## Limitations

1. **Benchmark dependence**: ECI inherits limitations of its component benchmarks. Models can be optimized for specific benchmarks without genuine capability improvement
2. **Underelicitation**: Newer models may score lower if evaluated through suboptimal APIs or providers (see "Why benchmarking is hard" by Epoch AI)
3. **Closed model opacity**: Leading closed labs may withhold their most capable models, meaning the "frontier" ECI may be lower than true state-of-the-art
4. **Real-world gap**: Benchmarks rarely capture the complexities of real-world tasks
5. **Abstract scale**: ECI points are meaningful only for comparison, not as absolute measures

## Related Pages

- [[entities/epoch-ai]] — Organization behind the ECI
- [[concepts/open-vs-closed-model-gap]] — Open vs. closed model capability gap measured via ECI
- [[concepts/benchmark-optimization]] — The broader challenge of benchmarking AI models
- [[entities/met]] — METR (collaborator on benchmarking, Time Horizon metric)

## Sources

- [ECI Documentation](https://epoch.ai/data/eci-documentation)
- [ECI Interactive Explorer](https://epoch.ai/eci)
- [A Rosetta Stone for AI Benchmarks](https://epoch.ai/blog/a-rosetta-stone-for-ai-benchmarks) (paper)
- [AI capabilities progress has sped up](https://epoch.ai/data-insights/ai-capabilities-progress-has-sped-up)
- [Why benchmarking is hard](https://epoch.ai/gradient-updates/why-benchmarking-is-hard)
- [ECI Public GitHub Repository](https://github.com/epoch-research/eci-public)
