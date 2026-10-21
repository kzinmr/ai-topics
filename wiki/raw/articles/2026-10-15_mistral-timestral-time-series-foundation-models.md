---
title: "Introducing Timestral — Mistral's time-series foundation models"
url: https://mistral.ai/news/timestral/
source: mistral.ai
date: 2026-10-15
fetched_at: 2026-10-21
type: raw-article
tags: [foundation-models, time-series, forecasting, mistral, cpu, benchmark]
confidence: high
---

# Introducing Timestral (Mistral, Oct 15 2026)

Source: https://mistral.ai/news/timestral/

## Summary
State-of-the-art probabilistic forecasting in four sizes (5M–209M params), CPU-efficient, zero-shot ready.

## Key content
Timestral is Mistral's first family of time-series foundation models, delivering state-of-the-art probabilistic, multivariate forecasts with just 209M parameters, outperforming larger models on key benchmarks while supporting past and future covariates. Available in four sizes (5M to 209M parameters), it balances accuracy and efficiency, running efficiently on CPUs and excelling in zero-shot forecasting for diverse domains. The model combines synthetic pre-training, covariate-aware attention, and long-context learning, with fine-tuning options for domain adaptation via Mistral Forge.

The largest model, at just 209M parameters, ranks first on all three of the field's main public benchmarks — **GIFT-Eval, TIME, and fev-bench** — outperforming the previous state of the art with only two-thirds of the model parameters. Results submitted to the GIFT-Eval and TIME leaderboards.

Delivers probabilistic, multivariate forecasts and supports past-only and known-future covariates. The family sits on the Pareto front of forecasting accuracy versus model size.

### Time Series Foundation Models (TSFM) context
Time series is one of the most common data types in enterprise (sensor telemetry to observability metrics). Forecasts drive decisions in capacity planning, energy, supply chains, risk and maintenance. Classical models (ARIMA, linear regression) are fitted to a single series. Deep learning models (PatchTST) learn nonlinear patterns across many related series but are still typically trained from scratch per dataset, so learning doesn't transfer. TSFMs bring pre-training: trained on a large, diverse corpus, the model learns patterns that transfer across series, forecasting zero-shot on unseen data, even in data-scarce domains.

### Benchmark results
Evaluated on GIFT-Eval, TIME and fev-bench. Among pre-trained, zero-shot models it ranks first across all five metrics. Results come from a single checkpoint, without ensembling.
- GIFT-Eval: top ten of 83 comparable pretrained/zero-shot entries (GMean MASE, GMean WQL).
- TIME: top ten of 35 leaderboard entries (GMean MASE, GMean CRPS).
- fev-bench: top ten of 37 entries, by SQL skill score.

### Family & efficiency
Four models: 5M, 28M, 123M and 209M parameters. All share the same architecture and training recipe; every size sits on the Pareto front.
- 28M model beats **Chronos-2** (about four times larger) on GIFT-Eval and TIME.
- 209M model beats **TimesFM-3** and **Falcon-2.0** with fewer parameters.
- Does not need a GPU at inference. On a standard server CPU (8 threads), forecasting one day ahead from three weeks of 15-minute history takes 10 ms (5M) and 140 ms (209M). The 28M model is 5x faster than the 209M; the 123M comes within 0.2% of the 209M score at three quarters of its latency.

### Training recipe
Combines synthetic pre-training, covariate-aware attention, and long-context learning. Fine-tuning for domain adaptation via **Mistral Forge**.

### Industrial example
An industrial plant with thousands of sensors: multivariate forecasting (a pump's vibration, temperature and pressure forecast jointly against the production schedule), catching equipment drift before failure, planning capacity/spare parts across thousands of assets. Finance teams forecast flows, volumes, volatility for positions, hedging, treasury.
