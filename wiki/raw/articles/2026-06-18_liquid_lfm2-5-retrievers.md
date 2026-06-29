---
title: "LFM2.5 Retrievers: Bi-directional LFMs for Fast Multilingual Search"
source: "https://www.liquid.ai/blog/lfm2-5-retrievers"
date: "2026-06-18"
type: article
author: "Liquid AI"
tags: [liquid-ai, retrieval, colbert, embeddings, multilingual, open-source]
---

# LFM2.5 Retrievers: Bi-directional LFMs for Fast Multilingual Search

**Published**: June 18, 2026
**Source**: Liquid AI Blog

Two new multilingual retrieval models: **LFM2.5-ColBERT-350M** and **LFM2.5-Embedding-350M**. Both are 350M-parameter models and the first bidirectional members of the LFM family, building on LFM2.5-350M-Base from March.

They are built for fast and reliable multilingual and cross-lingual search across **11 languages**: Arabic, German, English, Spanish, French, Italian, Japanese, Korean, Norwegian, Portuguese, and Swedish.

- **LFM2.5-Embedding-350M**: Turns each document into a single vector. Fastest search, smallest index.
- **LFM2.5-ColBERT-350M**: Converts each token into a vector. Word-by-word matching for higher accuracy via MaxSim late interaction.

## Architecture
Both models use a bidirectional encoder adapted from the causal LFM2 architecture:
- Bidirectional attention mask (full context access)
- Non-causal short convolutions (symmetric local mixing)

## Training
Three-stage recipe: (1) English contrastive pretraining, (2) multilingual/cross-lingual distillation from a strong teacher, (3) hard-negative fine-tuning.

## Benchmarks
Best-in-class multilingual and cross-lingual performance on NanoBEIR and MKQA-11 across all 11 languages.

| Model | NanoBEIR AVG | MKQA-11 AVG |
|-------|-------------|-------------|
| LFM2.5-ColBERT-350M | 0.605 | 0.694 |
| LFM2.5-Embedding-350M | 0.577 | 0.691 |
| Qwen3-Embedding-0.6B | 0.556 | 0.638 |
| gte-multilingual-base | 0.528 | 0.675 |

## Deployment
- GGUF quantized versions for llama.cpp (CPU/laptop/edge)
- MacBook M4 Max FP16 latency: 7-36ms
- H100 BF16 latency: 1.3-26.4ms (internal GPU stack)
- Available on HuggingFace

## Links
- https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M
- https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M
