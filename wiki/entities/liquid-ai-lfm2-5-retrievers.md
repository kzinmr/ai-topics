---
title: "LFM2.5 Retrievers (Liquid AI)"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [model, retrieval, colbert, embeddings, multilingual, open-source, late-interaction, maxsim, multi-vector, edge-ai, cpu-inference]
sources: [raw/articles/2026-06-18_liquid_lfm2-5-retrievers.md]
---

# LFM2.5 Retrievers

**LFM2.5-ColBERT-350M** and **LFM2.5-Embedding-350M** are 350M-parameter multilingual retrieval models released by Liquid AI on June 18, 2026. They are the first **bidirectional** members of the LFM family, built from LFM2.5-350M-Base.

## Models

| Model | Approach | Use Case |
|-------|----------|----------|
| **LFM2.5-Embedding-350M** | Single dense vector per document (CLS pooling) | Fastest search, smallest index |
| **LFM2.5-ColBERT-350M** | Per-token vectors with MaxSim late interaction | Higher accuracy, better generalization |

## Architecture

Both models adapt the causal LFM2 architecture to a bidirectional encoder:
- **Bidirectional attention mask** — every token attends to full left and right context
- **Non-causal short convolutions** — symmetric local mixing around each token
- Shared backbone, differing only in final representation: CLS pooling vs. per-token embeddings

## Multilingual Coverage

11 languages: Arabic, German, English, Spanish, French, Italian, Japanese, Korean, Norwegian, Portuguese, Swedish.

## Training Recipe

Three stages:
1. Large-scale contrastive pretraining in English
2. Multilingual and cross-lingual distillation from a strong teacher (all 11 languages)
3. Final fine-tuning on hard-mined negatives

## Benchmarks

**Best-in-class** multilingual/cross-lingual performance on NanoBEIR and MKQA-11:

| Model | Type | NanoBEIR AVG | MKQA-11 AVG |
|-------|------|-------------|-------------|
| LFM2.5-ColBERT-350M | colbert | **0.605** | **0.694** |
| LFM2.5-Embedding-350M | bienc | 0.577 | 0.691 |
| Qwen3-Embedding-0.6B | bienc | 0.556 | 0.638 |
| gte-multilingual-base | bienc | 0.528 | 0.675 |

## Deployment

- **GGUF quantized versions** for llama.cpp — runs on CPUs, laptops, edge devices
- MacBook M4 Max FP16: 7.3-36.3ms latency
- H100 BF16 (internal GPU stack): 1.3-26.4ms latency
- Available on HuggingFace: [LFM2.5-ColBERT-350M](https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M), [LFM2.5-Embedding-350M](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M)

## Related
- [[concepts/colbert]] — ColBERT late interaction retrieval
- [[concepts/embeddings]] — Dense vector embeddings
- [[concepts/multilingual]] — Multilingual AI models
- [[concepts/retrieval]] — Information retrieval systems
