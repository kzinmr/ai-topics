---
title: "DenseOn with the LateOn: Open State-of-the-Art Single and Multi-Vector Models"
source: https://www.linkedin.com/pulse/denseon-lateon-open-state-of-the-art-single-models-antoine-chaffin-prwbe/
date_published: 2026-04-21
author: Antoine Chaffin
source_site: LinkedIn (Antoine Chaffin)
type: raw_article
topics: [retrieval, embeddings, colbert, late-interaction, dense-retrieval, open-source, beir, benchmark]
---

# DenseOn with the LateOn: Open State-of-the-Art Single and Multi-Vector Models

**Author:** Antoine Chaffin (LightOn)
**Published:** April 21, 2026

## Key Announcements

LightOn has released a new generation of open retrieval models and the full training pipeline:

- **DenseOn:** Single-vector dense retriever (<150M parameters)
- **LateOn:** Multi-vector ColBERT-style retriever (same ModernBERT 149M backbone)
- **Full data and tooling:** 1.4B+ query-document pairs, metadata filters, hard-negative mining datasets, best mixture configuration

Everything is open under Apache 2.0 to avoid the pitfalls of closed, non-reproducible models.

## Model Performance

### DenseOn (Single-Vector, Base-Size)

| Metric | Value |
|--------|-------|
| **BEIR score** | **56.20** |
| Model size | 149M parameters (ModernBERT) |
| Notable wins | Beats GTE-ModernBERT (55.19), Arctic-Embed-L-v2 (568M, 55.97), Qwen3-Embedding-0.6B (595M, 55.47) |
| Competitive with | pplx-embed-v1 (596M, 56.47), jina-v5-text-nano (239M, 56.40) |

> "DenseOn is the first <150M to beat the 56 mark on BEIR and even beats Qwen3-Embedding-0.6B"

### LateOn (Multi-Vector, ColBERT-style)

| Metric | Value |
|--------|-------|
| **BEIR score** | **57.22** |
| Model size | 149M parameters (ModernBERT) |
| Notable wins | Beats previous SOTA ColBERT-Zero (55.32) by ~2 points, GTE-ModernColBERT-v1 (54.75) by ~2.5 points |

> "LateOn is the first ColBERT to beat the 57 (and thus 56) mark, outperforming the previous state-of-the-art, ColBERT-Zero, by almost two points"

*Results achieved without prompts or knowledge distillation — room for further improvement remains.*

## Decontamination & Generalization

The team removed all BEIR evaluation data overlapping with their training set:

- **LateOn stays #1** overall
- **DenseOn stays top-4**, only behind ColBERT-Zero (multi-vector) and pplx-embed (dense, larger)
- **ColBERT models generalize better:** all three ColBERT-style models hold or improve rank; two take top-3 spots
- **Dense models show mixed behavior:** GTE-ModernBERT falls from 8th to *last* (curation quality); Qwen3-Embedding drops significantly (possible BEIR overlap); jina-v5 and pplx-embed-v1 hold stronger

## Data Curation & Release

### Pre-training Dataset
- **1.4B+ query-document pairs**
- Includes new high-quality web dataset built on FineWeb-Edu
- Non-destructive curation: per-source filters, dedup, cross-encoder relevance scoring
- Filters stored as metadata, applied at training time — no data discarded

### Fine-Tuning Dataset
- **1.88M queries** with hard negatives from 2048 closest elements (nv-retrieve setup)
- All 2048 elements + retriever scores released

## Open Tooling
- **Models:** DenseOn, LateOn, ColBERT-Zero
- **Backbones:** ModernBERT, Ettin
- **Late interaction library:** PyLate
- **Full pipeline:** from random weights to production-ready SOTA models

## Selected Quotes

> "We don't just release models that outperform every model their size and models 4× bigger... We also release the large-scale curated datasets and findings so you can do the same."

> "When I started working at LightOn, two years ago, I was looking at all the top models and thinking 'wow, imagine the work that it would be to achieve this.' Today, I am proud to say that with this release, LightOn put out a whole pipeline to go from totally random weights to state-of-the-art results."
