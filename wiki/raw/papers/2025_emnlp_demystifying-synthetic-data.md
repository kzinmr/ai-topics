---
title: "Demystifying Synthetic Data in LLM Pre-training: Scaling Laws, Benefits, and Pitfalls"
authors: Feiyang Kang, Newsha Ardalani, Michael Kuchnik, Youssef Emad, Mostafa Elhoushi, Shubhabrata Sengupta, Shang-Wen Li, Ramya Raghavendra, Ruoxi Jia, Carole-Jean Wu
source: arXiv / EMNLP 2025
url: https://arxiv.org/abs/2510.01631
published: 2025-10-02
venue: EMNLP 2025 (Main Conference)
type: paper
tags:
  - synthetic-data
  - scaling-laws
  - data-mixture
  - model-collapse
  - meta
  - post-pretraining
---

# Demystifying Synthetic Data in LLM Pre-training

## Core Innovation

Large-scale empirical investigation (>1000 LLMs, >100k GPU hours) comparing natural web data, diverse synthetic types (rephrased text, generated textbooks), and mixtures under a unified scaling law framework.

## Key Findings

- **The "30% Rule"**: 1/3 rephrased synthetic + 2/3 natural web data speeds up training **5-10×** at larger budgets (to reach same validation loss)
- **Synthetic data alone is not faster** than natural web texts
- **Larger generator models don't necessarily help** — ~8B param generators are sufficient for effective synthetic pre-training data
- **Rephrased synthetic data**: No model collapse observed at tested scales
- **Textbook-style data**: Shows higher loss on downstream domains, especially at smaller budgets

## Connection to Scaling Hypothesis

Provides emperical guidance for Daniel Han's "Approach #4" — the Data Wall can be pushed further via strategic synthetic data mixing, but the mixture ratio and synthetic data type matter enormously.
