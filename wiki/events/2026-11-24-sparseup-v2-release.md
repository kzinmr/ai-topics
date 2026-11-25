---
title: "SPARSEUP-v2 Release (Linkup Research, Nov 2026)"
type: event
created: 2026-11-25
updated: 2026-11-25
tags:
  - announcement
  - search
  - information-retrieval
  - rag
  - beir
  - training
  - open-source
  - retrieval
sources:
  - raw/articles/www.linkup.so--introducing-sparseup-v2-by-linkup--2026-11-24.md
  - https://arxiv.org/pdf/2611.09680
  - https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v2
  - https://x.com/tomaarsen/status/2125257957726392731
related:
  - concepts/gte-moderncolbert
  - entities/denseon-lateon
  - concepts/modernbert
  - concepts/late-interaction-retrieval
  - concepts/lexical-search
  - entities/tom-aarsen
status: active
---

# SPARSEUP-v2 Release (Linkup Research, Nov 2026)

On **2026-11-24**, Linkup Research released **SPARSEUP-v2**, the second version of its learned-sparse retrieval model family. Written by Thibault Formal (Head of Research), the model sets a **new state of the art for sparse encoders under 150M parameters**, reaching **57.2 nDCG@10 on BEIR-15** — surpassing SlideOn (56.7) and matching the late-interaction model [[entities/denseon-lateon|LateOn]] (57.22), while being dramatically cheaper to serve.

The release was amplified in a 5-tweet thread by [[entities/tom-aarsen|Tom Aarsen]] (Hugging Face / Sentence Transformers), who highlighted the released pretrained checkpoint and the visualization showing which vocabulary terms each token activates.

## Why it matters

Learned sparse retrieval (a.k.a. SPLADE-style) represents each document/query as a high-dimensional bag-of-terms with learned weights, allowing a model to **expand a query/document with related terms that never appeared in the input**. This combines the lexical transparency of [[concepts/lexical-search|BM25-style search]] with neural effectiveness, and indexes are far smaller than dense vectors for the same quality.

SPARSEUP-v2's headline contribution is closing the **modality gap**: prior sparse encoders were initialized from dense or multi-vector checkpoints. SPARSEUP-v2 instead **pretrains directly in the sparse modality**, and Linkup demonstrates this beats starting from a multi-vector checkpoint — answering an open research question about why SPARSEUP-v1 lagged its dense sibling DenseOn.

## Key numbers

| Property | Value |
|----------|-------|
| Developer | Linkup Research |
| Backbone | [[concepts/modernbert|ModernBERT-base]] |
| Parameters | 150M |
| Max input | 8,192 tokens (English) |
| License | Apache 2.0 |
| BEIR-15 | 57.2 nDCG@10 (matches LateOn, beats SlideOn 56.7) |
| MTEB (eng, v2) retrieval | 59.71 nDCG@10 — best sparse on the leaderboard (prior: SlideOn 58.62) |
| Retrieval cost | 4.2 FLOPS unpruned vs SlideOn 30.9 (~7× cheaper) |
| Index size | 269 entries/doc avg — 4.6× fewer than SlideOn |

## Three-ingredient recipe

1. **Contrastive Pre-Training (CPT)** on 665M weakly supervised [query, document] pairs (title→query, passage→positive). Sparse-modality CPT at 25% of data already beats the ModernBERT init by ~3 nDCG and a LateOn-initialized SPARSEUP by ~1.6. Full run ≈ 3.5 days on 4× H100 (~50× fine-tuning time) — hence the released pretrained checkpoint.
2. **Cross-encoder distillation** reusing supervised-stage data with teacher scores — gives fine-grained relevance signal and correctly scores mined hard negatives that a plain contrastive loss would wrongly penalize.
3. **Matryoshka training** for multiple pruning budgets at once (top 16/32/64 query entries, 64/128/256 doc entries; 0.8 weight on the unpruned level). Pays off most under aggressive pruning (+1.5 nDCG@10 at 64 entries/doc).

## Positioning vs the sparse/late-interaction field

- **Beats SlideOn** (56.7) at ~7× fewer retrieval FLOPS and a much smaller index.
- **Matches LateOn** ([[entities/denseon-lateon|LightOn's late-interaction SOTA]], 57.22) on ranking while being a sparse (cheaper-to-serve) model; LateOn still leads on long documents (MLDR-en) and LIMIT.
- **Trails on ChemTEB** by ~4 nDCG vs SlideOn/DenseOn — the main domain weakness; **LoTTE** remains SPARSEUP's weakest suite (though v2 gains +5.1 S@5 Forum, +3.9 Search).
- Only learned-sparse models above the cost/quality curve are LACONIC-3B/8B, which have 20–60× more parameters.

## Artifacts

- Model: https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v2
- Pretrained checkpoint: https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v2-pretrain
- Interactive visualization: https://huggingface.co/spaces/Linkup-Platform/sparseup-embed-v2-visualization
- Paper: https://arxiv.org/pdf/2611.09680

## See also

- [[concepts/gte-moderncolbert]] — LightOn's ModernBERT-based late-interaction lineage (GTE-ModernColBERT → LateOn)
- [[entities/denseon-lateon]] — the DenseOn/LateOn models SPARSEUP-v2 benchmarks against
- [[concepts/modernbert]] — backbone architecture
- [[concepts/late-interaction-retrieval]] — the multi-vector paradigm this sparse model competes with
- [[concepts/lexical-search]] — the lexical tradition learned-sparse retrieval modernizes
