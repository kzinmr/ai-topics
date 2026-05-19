---
title: Baidu (Ernie)
created: 2026-05-16
updated: 2026-05-16
type: entity
tags:
  - company
  - model
  - training
  - optimization
  - china
sources: [raw/articles/the-decoder.com--baidu-ernie-5-1-94-percent-cost-reduction--2026-05-16.md]
---

# Baidu (Ernie)

**Baidu** is a Chinese technology company and one of the country's leading AI labs, developing the **Ernie** (Enhanced Representation through Knowledge Integration) family of language models. In May 2026, Baidu released Ernie 5.1, demonstrating significant advances in training efficiency.

## Ernie Model Family

### Ernie 5.1 (May 2026)

A smaller model distilled from Ernie 5.0, achieving competitive performance at dramatically reduced cost:

- **Parameters**: ~1/3 of Ernie 5.0's total parameters, ~1/2 active parameters per query
- **Pre-training cost**: 6% of what comparable models require (94% reduction)
- **Search Arena Leaderboard**: 1,223 points — 4th place globally, 1st among Chinese models (as of May 9, 2026)
- **Agent tasks**: Claims to beat DeepSeek-V4-Pro on tau3-bench and SpreadsheetBench-Verified
- **Knowledge/reasoning**: Close to Gemini 3.1 Pro on GPQA and MMLU-Pro
- **Text Arena**: 13th place (1,476 points) — Claude Opus variants hold top spots

### Once-For-All Elastic Training

Baidu's key innovation: instead of separate pre-training runs for each model size, the "Once-For-All elastic training framework" optimizes an entire family of differently sized models in a single run. The framework simultaneously varies:
- **Elastic depth**: Number of transformer layers
- **Elastic width**: Number of expert blocks
- **Elastic sparsity**: Active experts per query (Top-K routing)

See [[concepts/elastic-training]] for details.

### Four-Stage Training Pipeline

Ernie 5.1 uses specialized expert models for code, logic, and agent tasks, designed to prevent capability interference during learning. Baidu also rebuilt its RL infrastructure with decoupled subsystems (model updates, response generation, evaluation) coordinated by a central controller.

### Availability

Accessible through Baidu's platforms. Model weights are **closed**, making independent verification impossible.

## See Also

- [[concepts/elastic-training]]
- [[concepts/mixture-of-experts]]
- [[concepts/training]]
- [[concepts/inference]]
- [[entities/deepseek]]
