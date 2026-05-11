---
title: "Delphi Scaling Laws"
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [scaling, training, research, open-source, benchmark, optimization, ai-research, data-science]
sources:
  - raw/articles/2026-04-14_openathena_delphi-scaling-laws.md
aliases: ["Delphi", "Delphi scaling suite", "Marin Delphi"]
related:
  - concepts/scaling-laws
  - concepts/pythia
  - concepts/chinchilla-scaling
  - concepts/isoflop-sweep
---

# Delphi Scaling Laws

Delphi is the Marin team's first open scaling suite, developed by Will Held at Open Athena (a nonprofit accelerating academia with frontier AI capabilities). It achieves the most accurate public scaling-law extrapolation to date: the scaling law, fit on runs up to 3e20 FLOPs, predicted the loss of a **1e23 FLOP run (25B parameters, 600B tokens) within 0.2%** — extrapolating **300× past the largest run used in the fit**.

## Three Components

Delphi has three parts:

1. **Scaling Recipe**: A functional-form mapping from compute budget to full training configuration (architecture, batch size, learning rate, optimizer settings, schedule, initialization). Derived from a reference model tuned at small scale, then analytically extended to larger scales.

2. **Scaling Suite**: A set of models trained with the same recipe at increasing compute budgets. Released with all checkpoints, training mixture, and recipe — fully reproducible from public data sources (Nemotron-CC, StarCoderData, ProofPile 2).

3. **Scaling Law**: The empirical power-law relationship between compute (FLOPs) and validation loss. Fit on seven IsoFLOP optima (3e18–3e20 FLOPs), validated on held-out runs at 1e21, 1e22, and 1e23 FLOPs — all within 0.5% of the fit.

## How It Works

### IsoFLOP Sweeps

At each compute budget from 3e18 to 3e20 FLOPs, Delphi trains multiple Qwen 3 architecture models on a mixture of Nemotron-CC, StarCoderData, and ProofPile 2. Each sweep varies the tradeoff between model size and training duration while keeping total compute fixed. The best configuration at each budget is called "compute-optimal." From these points, a power law is fit and used to forecast larger runs.

### Scaling Recipe Details

| Component | Specification |
|-----------|--------------|
| Architecture | Qwen 3 |
| Tokenizer | Llama 3 |
| Data mixture | Nemotron-CC + StarCoderData + ProofPile 2 |
| LR schedule | WSD (Warmup-Stable-Decay), 10% warmup, 0 floor |
| Mixed precision | f32 params, bf16 compute |
| Parallelism | FSDP |

## Attempt 1 → Attempt 2: What Went Wrong and How It Was Fixed

### First Attempt: Clean on Small Runs, Divergent on Large

The initial recipe followed published scaling prescriptions (muP learning rate scaling, log-corrected depth-to-width ratios, batch size targeting fixed step count). The seven IsoFLOP buckets from 3e18 to 3e20 FLOPs looked healthy internally. But extrapolation failed catastrophically:

- **1e22 held-out run**: missed the forecast by **2.5%**
- **1e23 held-out run**: **diverged entirely**

The problem: the recipe's hyperparameters didn't scale correctly to longer training horizons.

### Second Attempt: Token-Horizon Correction + AdamH

Two key fixes:

1. **Token-horizon learning rate correction**: The original recipe scaled learning rate with √(batch_size), which produced excessively large learning rates for data-heavy runs. The fix introduced an explicit token-horizon adjustment, bringing learning rates more in line with what manual tuning would produce (e.g., Marin 32B used learning rates 10× lower with even larger batch sizes).

2. **AdamH optimizer (no weight decay in hyperparameter search)**: Weight decay was pinned at 0.1 across all runs in the first attempt, scaling with neither model width nor training length. AdamH removes weight decay from the hyperparameter search entirely, using a different regularization approach that generalizes better across scale.

With these fixes, the same seven-point IsoFLOP fit predicted the 1e23 run within **0.2%**, and held-out runs at 1e21 and 1e22 both landed within **0.5%** across multiple random seeds.

## Downstream Benchmark Forecasting

Delphi also forecasts downstream task performance via a **two-step regression**:
1. **Compute scaling law**: Predict validation loss from FLOPs
2. **Observational scaling law**: Predict benchmark scores (MMLU, HumanEval, GSM8K) from validation loss

This allows predicting not just loss but actual capability metrics at frontier-scale compute without training the large models.

## Delphi's Scaling Law Extrapolation

The fit curve places known models at their estimated compute budgets (from Epoch AI's database):

| Model | Estimated FLOPs | Delphi Prediction |
|-------|----------------|-------------------|
| Marin 32B | ~3e22 | On curve |
| Kimi K2.5 | Frontier | On curve |
| DeepSeek V4 | Frontier | Near curve |
| GPT-4 | ~2e25 | Near curve |
| Claude Opus | Frontier | Near curve |
| GPT-5 | Frontier | Near curve |

## Key Insights for Scaling Research

1. **Small-run health ≠ large-run predictability**: A scaling law that looks clean on the fit data can diverge dramatically when extrapolated. Validation must include held-out runs far beyond the fit range.

2. **Token-horizon effects dominate at scale**: The parts of a recipe most likely to break are those involving training duration — learning rate schedules, momentum terms, and regularization. Scaling prescriptions derived from fixed-duration experiments often fail when duration changes.

3. **Recipe as falsifiable baseline**: By making the recipe itself the variable of study (rather than individual model configurations), a failing run points directly to the recipe rather than a single hyperparameter table entry.

4. **Open release enables community use**: All checkpoints, fit coefficients, and the recipe are publicly released. Scripts deterministically reproduce the training mixture from public sources, enabling the community to use Delphi as Pythia was used — for studies on memorization, training trajectory analysis, emergence, and model provenance.

## References

- [Open Athena Blog: Scaling Laws That Extrapolate 300× Past the Fit](https://openathena.ai/blog/delphi/) (April 14, 2026)
- [Pythia scaling suite (EleutherAI)](https://www.eleuther.ai/papers-blog/pythia-a-suite-for-analyzing-large-language-modelsacross-training-and-scaling)
- [Epoch AI large-scale AI models database](https://epoch.ai/data/notable-ai-models)

## See Also

- [[concepts/scaling-laws]] — General concept of scaling laws in ML
- [[concepts/chinchilla-scaling]] — Chinchilla optimal scaling (Hoffmann et al., 2022)
- [[concepts/pythia]] — EleutherAI's open scaling suite
- [[entities/open-athena]] — Nonprofit behind Delphi
