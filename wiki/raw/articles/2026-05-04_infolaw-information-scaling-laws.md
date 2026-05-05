---
title: "InfoLaw: Information Scaling Laws for Large Language Models with Quality-Weighted Mixture Data and Repetition"
source: https://arxiv.org/abs/2605.02364
date: 2026-05-04
scraped: 2026-05-05
authors: [Fengze Liu, Weidong Zhou, et al.]
tags: [scaling-laws, data-quality, pretraining, overtraining, icml-2026]
venue: ICML 2026
---

# InfoLaw: Information Scaling Laws for LLMs with Quality-Weighted Data

**Source:** arXiv:2605.02364
**Authors:** Fengze Liu, Weidong Zhou, et al.
**Date:** May 4, 2026
**Venue:** ICML 2026

## Executive Summary
**InfoLaw (Information Scaling Laws)** is a novel framework designed to solve the limitations of standard scaling laws, which often fail when data is repeated (overtraining) or when data mixtures change. By modeling pretraining as **information accumulation**, InfoLaw accurately predicts model loss across varying compute budgets, data qualities, and repetition levels.

> "InfoLaw predicts performance on unseen data recipes and larger scale runs (up to 7B, 425B tokens) with 0.15% mean and 0.96% max absolute error in loss."

## The Problem: Scaling Law Limitations
Standard scaling laws (like Chinchilla) typically assume unique data. However, in modern LLM training:
- **Data Scarcity:** High-quality data is limited, leading researchers to "overtrain" by repeating data.
- **Diminishing Returns:** Simply upweighting high-quality data works initially, but excessive repetition can degrade performance.
- **Recipe Uncertainty:** Selecting the optimal mixture of data sources at scale is currently "underdetermined" without expensive trial runs.

## Key Innovation: Information Accumulation
InfoLaw shifts the focus from "token count" to **"information density."** The framework treats pretraining as a process where:
1. **Quality** determines the density of information per token.
2. **Repetition** induces scale-dependent diminishing returns.
3. **Model Size** interacts with these factors to determine the final loss.

## Performance & Validation
Tested on models up to **7B parameters** and **425B tokens**:
- **Mean Absolute Error (MAE):** 0.15% in loss prediction.
- **Max Absolute Error:** 0.96%.

### Actionable Insights
- **Extrapolation:** Reliably predicts performance on unseen data recipes.
- **Overtraining Optimization:** Finds the "sweet spot" for data repetition.
- **Compute Efficiency:** Selects optimal data recipes for specific compute budgets without full-scale training runs.
