---
title: Timestral (Mistral time-series foundation models)
created: 2026-10-21
updated: 2026-10-21
type: concept
tags: [foundation-models, time-series, forecasting, mistral, cpu, benchmark]
sources:
  - raw/articles/2026-10-15_mistral-timestral-time-series-foundation-models.md
  - https://mistral.ai/news/timestral/
confidence: high
---

# Timestral

**Timestral** is Mistral AI's first family of **time-series foundation models (TSFMs)**, released October 15, 2026. It delivers state-of-the-art **probabilistic, multivariate** forecasting at very small scale — the flagship 209M-parameter model ranks first on the field's three main public benchmarks while using only about two-thirds of the prior SOTA's parameters.

## Model family

Four sizes sharing one architecture and training recipe, each on the Pareto front of accuracy vs. model size:

| Size | Notes |
|------|-------|
| 5M | Fastest/cheapest; 10 ms to forecast 1 day ahead from 3 weeks of 15-min history on an 8-thread CPU |
| 28M | Beats **Chronos-2** (~4× larger) on GIFT-Eval and TIME; 5× faster than 209M |
| 123M | Within 0.2% of the 209M score at ~¾ of its latency |
| 209M | Ranks #1 on GIFT-Eval, TIME, fev-bench; beats TimesFM-3 and Falcon-2.0 with fewer params |

## Benchmarks

Among pre-trained, **zero-shot** models it ranks first across all five metrics from a single checkpoint (no ensembling):
- **GIFT-Eval** — top 10 of 83 comparable pretrained/zero-shot entries (GMean MASE, GMean WQL)
- **TIME** — top 10 of 35 leaderboard entries (GMean MASE, GMean CRPS)
- **fev-bench** — top 10 of 37 entries by SQL skill score

## Techniques

- **Synthetic pre-training** on a large, diverse corpus so learned patterns transfer across series (the TSFM approach vs. per-dataset training from scratch).
- **Covariate-aware attention** — supports past-only and known-future covariates (e.g. forecasting a pump's vibration against a known production schedule).
- **Long-context learning**.
- **Probabilistic, multivariate** forecasting (full predictive distributions, not point forecasts).
- Fine-tuning for domain adaptation via **Mistral Forge**.

## Why CPU matters

Timestral **does not need a GPU at inference** — forecasting runs on a standard server CPU. This is a deliberate positioning: time series is one of the most common enterprise data types (sensor telemetry, observability metrics) and forecasts drive capacity planning, energy, supply chains, risk, and maintenance across *thousands of series*. Being CPU-efficient and small makes per-series forecasting economical at fleet scale, unlike large autoregressive LLM serving.

## Positioning in the TSFM landscape

Timestral enters a space previously served by classical models (ARIMA, linear regression — single-series, no transfer), deep-learning models trained per dataset (PatchTST — no cross-domain transfer), and earlier TSFMs (Chronos, TimesFM). Its contribution is beating larger competitors at 5–209M parameters with CPU-only inference.

## Related

- [[entities/mistral-ai]] — the lab releasing Timestral
- [[concepts/scaling-laws]] — accuracy-vs-size Pareto frontier framing
- [[concepts/edge-ai]] — CPU-only, small-model deployment economics
- [[concepts/mixture-of-experts]] — another parameter-efficiency strategy in modern models
- [[concepts/information-retrieval]] — adjacent enterprise-data analytics domain
