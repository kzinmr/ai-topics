---
title: Elie Bakouch
type: entity
created: 2025-11-17 16:10:46
updated: 2026-04-10 10:00:00
aliases: [eliebak, eliebakouch]
status: active
description: "ML engineer and researcher at Hugging Face, known for work on SmolLM, pretraining optimization, MoE scaling laws, and data-centric model training."
tags: [person]
sources: []
---


# Elie Bakouch

**X/Twitter:** [@eliebakouch](https://x.com/eliebakouch)
**Hugging Face:** [hf.co/eliebak](https://huggingface.co/eliebak)
**Role:** ML Engineer & Researcher, Hugging Face
**Focus:** LLM Pretraining, MoE Scaling Laws, Data-Centric Training, Synthetic Data

## Overview

Elie Bakouch (known online as **eliebak** on Hugging Face and **@eliebakouch** on X) is an ML engineer and researcher at **Hugging Face**, where he works on the pretraining and optimization of language models. He is a key contributor to the **SmolLM** family of small language models and has published influential research on **Mixture-of-Experts (MoE) scaling laws**, **data-centric training methodologies**, and **synthetic data pipelines**.

Bakouch's work sits at the intersection of practical model training and theoretical understanding. He has co-authored papers on μ-Parametrization for MoE architectures, optimal sparsity in Mixture-of-Experts language models, and compute-optimal training beyond fixed durations. His Hugging Face profile documents active contributions to the open-source ML ecosystem, including model releases, dataset curation, and community engagement through AMAs and public discussions.

His research philosophy emphasizes **data quality over quantity**, **architectural efficiency**, and **transparent, reproducible training processes**. He has been particularly influential in the small language model community, where resource constraints demand careful optimization of every training decision.

## Timeline

| Date | Event |
|------|-------|
| ~2023 | Joined Hugging Face as ML engineer/researcher |
| 2024 | Co-authored "Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations" with Alexander Hägele, Atli Kosson, Loubna Ben Allal, Leandro von Werra, Martin Jaggi |
| 2024 | Contributed to **SmolLM** development — small language models optimized for edge deployment |
| 2025 | Co-authored "SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model" with Loubna Ben Allal, Anton Lozhkov, and others |
| Jan 2025 | Co-authored "Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models" — submitted to Hugging Face Papers |
| Feb 2025 | SmolLM2 released with full dataset release to facilitate future research on LM development |
| 2025 | Active in MoE sparsity research and community discussions on Hugging Face |
| 2025 | Participated in Hugging Face AMA on r/LocalLLaMA about SmolLM, FineWeb, and related research |
| Feb 2026 | Created "Sparsity Viz" Hugging Face Space — interactive visualization of MoE model sparsity across many LLMs |
| 2026 | Contributing to **SmolLM3** — smol, multilingual, long-context reasoner |
| 2026 | Engaged in synthetic pretraining research, commenting on Motif-2.6B tech report and training methodologies |

## Core Ideas

### Data-Centric Training

Bakouch is a strong advocate for **data-centric approaches** to language model training — the idea that carefully curated, high-quality training data matters more than raw scale. SmolLM2's training methodology exemplifies this: rather than simply scaling up parameters, the team focused on optimizing the data mixture, quality filtering, and training recipe.

> "SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model"

The paper and its accompanying dataset release reflect his belief that transparency and reproducibility are essential for advancing the field. By releasing all datasets used in SmolLM2's training, the team enabled other researchers to build on their work rather than treating the data pipeline as a proprietary secret.

### Mixture-of-Experts Scaling Laws

Bakouch's research on **MoE scaling laws** has been influential in understanding how to optimally configure sparse architectures. His work on "Parameters vs FLOPs" explores the tradeoff between model capacity (number of parameters) and computational cost (FLOPs) in sparse MoE models.

Key findings from his research:
- There exists an **optimal level of sparsity** that balances training efficiency with model performance
- The optimal sparsity depends on the **compute budget** and the **downstream task**
- MoE models can achieve better performance per FLOP than dense models, but only with careful architectural design

His work on μ-Parametrization for MoE (2025) extends the theoretical framework of μP (Maximal Update Parameterization) to MoE architectures, providing guarantees for **stable and predictable training dynamics** across model widths.

### Compute-Optimal Training Beyond Fixed Durations

In collaboration with Alexander Hägele and others, Bakouch co-authored research on **scaling laws that go beyond fixed training durations**. Traditional Chinchilla-style scaling laws assume a fixed relationship between model size and training tokens, but their work shows that optimal training strategies depend on the specific compute budget and task requirements.

This research has practical implications for teams training models under resource constraints: it provides a framework for deciding **how many tokens to train on** and **when to stop**, rather than following a predetermined schedule.

### Small Language Models

Bakouch's work on SmolLM, SmolLM2, and SmolLM3 reflects a broader philosophy: **small models, well-trained, can punch above their weight**. The SmolLM family is designed for edge deployment, where parameter budgets are constrained but performance requirements remain high.

SmolLM3 (2026) extends this with **multilingual capabilities** and **long-context reasoning**, demonstrating that small models can be specialized for diverse use cases without sacrificing their efficiency advantages.

### Synthetic Data and Training Environments

Bakouch has shown strong interest in **synthetic data pipelines** for model training. His comments on the Motif-2.6B tech report reveal engagement with cutting-edge synthetic pretraining approaches:

> "Motif 2.6B tech report is pretty insane, first time i see a model with differential attention and polynorm trained at scale!"

He specifically noted Motif's use of:
- 2.5T tokens with a "data mixture schedule" to continuously adjust the mixture over training
- WSD with "Simple moving average" averaging the last 6 checkpoints every 8B tokens
- Training on FineMath, FineWeb2, DCLM, TxT360
- EvolKit and "dataset fusion" for compressed knowledge
- Normalized GPT, QK-Norm, and Cross Layer Attention

### Community Engagement and Open Science

Bakouch is active in the open-source ML community through Hugging Face AMAs, public discussions, and tool development. His **Sparsity Viz** Hugging Face Space provides an interactive visualization of MoE sparsity across many models, making complex research accessible to practitioners.

He has participated in the r/LocalLLaMA community, answering questions about SmolLM training, FineWeb dataset curation, and other research topics. This community engagement reflects his belief that open science requires not just open code and data, but also open discussion and knowledge sharing.

## Key Quotes

> "Motif 2.6B tech report is pretty insane, first time i see a model with differential attention and polynorm trained at scale!"

> "It's trained on 2.5T of token, with a 'data mixture schedule' to continuously adjust the mixture over training."

## Key Projects

### SmolLM / SmolLM2 / SmolLM3
Family of small language models optimized for edge deployment. SmolLM2 introduced data-centric training methodologies; SmolLM3 adds multilingual and long-context capabilities.

### Sparsity Viz
Interactive Hugging Face Space for visualizing MoE model sparsity across many LLMs. Makes complex architectural research accessible to practitioners.

### FineWeb
Large-scale web dataset used for training SmolLM and other models. Bakouch contributed to its curation and quality filtering.

### μ-Parametrization for MoE
Theoretical framework extending Maximal Update Parameterization to Mixture-of-Experts architectures, enabling stable training dynamics across model widths.

### Local LLM Research
Active engagement with the local/open-source LLM community through AMAs, discussions, and practical experimentation with small model training.

## Related Wikilinks

- [[concepts/smollm]] — Small language model family he contributed to
- [[hugging-face]] — His employer and primary platform
- [[concepts/mixture-of-experts]] — His research focus area
- [[concepts/scaling-laws]] — Compute-optimal training research
- [[concepts/fineweb]] — Training dataset he helped curate
-  — His training philosophy-  — Community he actively participates in
-  — Emerging training methodology he follows

## Sources

- [Hugging Face: eliebak](https://hf.co/eliebak)
- [X/Twitter: @eliebakouch](https://x.com/eliebakouch)
- [SmolLM2 Paper (arXiv:2502.02737)](https://arxiv.org/abs/2502.02737)
- [Scaling Laws Paper (arXiv:2405.xxxxx)](https://paperswithcode.com/search?q=author%3AElie+Bakouch)
- [MoE Sparsity Paper (arXiv:2501.12370)](https://huggingface.co/papers/2501.12370)
- [μ-Parametrization for MoE (arXiv:2508.09752)](https://huggingface.co/papers/2508.09752)
- [Motif-2.6B Tech Report Discussion](https://huggingface.co/Motif-Technologies/Motif-2.6B)
- [Sparsity Viz Space](https://huggingface.co/spaces/eliebak/sparsity-viz)
- [Hugging Face r/LocalLLaMA AMA](https://www.reddit.com/r/LocalLLaMA/)
