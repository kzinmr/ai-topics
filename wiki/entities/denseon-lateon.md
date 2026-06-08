---
title: "DenseOn & LateOn"
created: 2026-05-28
updated: 2026-05-28
type: entity
tags:
  - model
  - search
  - late-interaction
  - open-source
  - benchmark
  - beir
sources:
  - raw/articles/2026-04-21_antoine-chaffin_denseon-lateon-open-sota-retrieval.md
  - https://huggingface.co/blog/lightonai/denseon-lateon
status: active
---

# DenseOn & LateOn

**DenseOn** and **LateOn** are two open-source retrieval models released by [[entities/lighton|LightOn]] in April 2026, built on the same **ModernBERT** backbone (149M parameters). They represent the current state-of-the-art for single-vector (dense) and multi-vector (ColBERT-style late interaction) retrieval at base scale, respectively. Both are released under **Apache 2.0** with full training data, curation pipelines, and mixture recipes.

> "From ModernBERT and Ettin, to PyLate and LateOn/DenseOn, we released all the code, data and insights for anyone to go from random weights to state-of-the-art results." — Antoine Chaffin

## DenseOn (Single-Vector Dense Retriever)

| Property | Value |
|----------|-------|
| **BEIR Score** | **56.20** NDCG@10 |
| **Parameters** | 149M (ModernBERT) |
| **Output Dim** | 768 |
| **Type** | Dense (single-vector), CLS pooling |
| **Prefixes** | `query:` / `document:` |
| **Notable** | First <150M model past 56 on BEIR |

### Comparison (BEIR)

| Model | Params | BEIR |
|-------|--------|------|
| **DenseOn** | 149M | **56.20** |
| GTE-ModernBERT | 149M | 55.19 |
| Qwen3-Embedding-0.6B | 595M | 55.47 |
| Arctic-Embed-L-v2 | 568M | 55.97 |
| pplx-embed-v1 | 596M | 56.47 |
| jina-v5-text-nano | 239M | 56.40 |

## LateOn (Multi-Vector ColBERT Retriever)

| Property | Value |
|----------|-------|
| **BEIR Score** | **57.22** NDCG@10 |
| **Parameters** | 149M (ModernBERT) |
| **Output Dim** | 128 (per token) |
| **Type** | ColBERT-style multi-vector, MaxSim scoring |
| **Notable** | First ColBERT past 57 on BEIR |

### Comparison (BEIR)

| Model | Params | BEIR |
|-------|--------|------|
| **LateOn** | 149M | **57.22** |
| ColBERT-Zero | 149M | 55.32 |
| GTE-ModernColBERT-v1 | 149M | 54.75 |

## Architecture & Training

### Shared Backbone
- **ModernBERT** (149M params) — bi-directional encoder
- Ettin backbone also available
- Trained with [[concepts/pylate|PyLate]] (LightOn's late interaction library)

### Training Data
- **Pre-training**: 1.4B+ query-document pairs with non-destructive metadata filtering
- **Fine-tuning**: 1.88M queries with hard negatives (2048 nearest neighbors per query, nv-retrieve setup)
- **Proprietary final dataset**: Apache 2.0 compatible

## Decontamination Results

When BEIR evaluation data overlapping with training data is removed:

- **LateOn** holds rank #1 — evidence of genuine generalization
- **DenseOn** stays top-4 — behind ColBERT-Zero (multi-vector) and pplx-embed (dense, larger)
- **ColBERT models generalize better** as a class — all three hold or improve rank

## Key Design Principles

1. **Sub-150M sweet spot**: Large enough for real-world complexity, small enough for high-throughput production
2. **No prompts, no KD**: Results achieved without prompt prefixes or knowledge distillation
3. **Non-destructive curation**: All filters are metadata, applied at training time — no data discarded
4. **Full pipeline release**: Models + data + mixture recipes + curation insights

## Relationships

- **Company**: [[entities/lighton|LightOn]] (Antoine Chaffin, Benjamin Clavié)
- **Framework**: [[concepts/pylate|PyLate]] (CIKM 2025)
- **Backbone**: ModernBERT, Ettin
- **Predecessors**: ColBERT-Zero, GTE-ModernColBERT-v1
- **Related concepts**: [[concepts/colbert|ColBERT]], [[entities/late-interaction|Late Interaction Workshop]], [[concepts/embeddings|Embeddings]], [[concepts/embedding-long-context-degradation|Embedding Long-Context Degradation]]
