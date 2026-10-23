---
title: "KURE — Korea University Retrieval model family"
created: 2026-10-23
updated: 2026-10-23
type: event
tags: [announcement, retrieval, embeddings, multi-vector, colbert, maxsim, neural-reranking, information-retrieval, nlp, huggingface, sentence-transformers, multilingual]
sources:
  - https://huggingface.co/collections/nlpai-lab/kure
  - https://huggingface.co/nlpai-lab/KURE-v3
  - https://huggingface.co/nlpai-lab/KURE-v2
  - https://x.com/tomaarsen/status/2113607601753620588
  - raw/articles/huggingface.co--collections-nlpai-lab-kure--2026-10-23.md
---

# KURE — Korea University Retrieval model family

**KURE (Korea University REtrieval models)** is a Korean–English retrieval toolkit
from the **NLP & AI Lab at Korea University** (`nlpai-lab` on Hugging Face). Announced
in a Tom Aarsen (@tomaarsen) X thread on 2026-10-23, KURE is claimed to be *"the first
major model suite to support all 4 Sentence Transformers model types"* — dense, sparse,
and multi-vector embeddings plus rerankers — for both Korean and English.
Collection: https://huggingface.co/collections/nlpai-lab/kure

## Why it matters

Sentence Transformers normally exposes these model families separately
(`SentenceTransformer` for dense, `SparseEncoder` for sparse/lexical,
`MultiVectorEncoder` for late-interaction/ColBERT-style, `CrossEncoder` for rerankers).
KURE is unusual in shipping a **coherent family covering all four under one brand**,
making it a reference point for teams that want hybrid (dense + sparse + multi-vector +
rerank) retrieval without stitching together models from different labs. Aarsen also
noted the new ~1.1B `KURE-v3` is "really good on English retrieval too", not just Korean.

## The model family

| Model | Type | Size | Notes |
|---|---|---|---|
| `KURE-v3` | Dense embedding (SentenceTransformer) | ~1.1B (1B) | One 2,048d vector per text, **Matryoshka** support down to 256d. Team's Korean eval: 1,024d retains ~99% of full-size score → halve vector storage with little loss. |
| `KURE-v2` | Multi-vector (MultiVectorEncoder) | 154M (0.1B) | Late-interaction: keeps a **128d vector per token**, uses **MaxSim**, letting different query tokens match different document parts. Released August 2026. |
| `KURE-v2-unsupervised` | Multi-vector | 0.1B | Unsupervised variant. |
| `KURE-v1` | Dense (Feature Extraction) | 0.6B | 578k downloads — original release. |
| `KURE-Sparse-base` | Sparse (SparseEncoder) | 0.6B | Lexical/sparse embedding. |
| `KURE-Sparse-nano` | Sparse (SparseEncoder) | 0.1B | Small sparse variant. |
| `KURE-Reranker-base` | CrossEncoder reranker | 1.7B (2B) | Freshly retrained; relevance **logits** (higher is better even when negative). |
| `KURE-Reranker-nano` | CrossEncoder reranker | 149M (0.1B) | Lightweight reranker. |
| `KoE5` | Dense (Feature Extraction) | 0.6B | Korean e5-style embedding, related lab release. |

## Indexing + reranking pipeline

Aarsen's thread framed KURE as an end-to-end "index → retrieve → rerank" workflow:

1. **Three ways to index documents** — dense (v3), sparse (Sparse-base/nano), and multi-vector (v2/ColBERT-style MaxSim).
2. **Retrieve** candidates with the chosen encoder.
3. **Rerank** with `KURE-Reranker-base` (1.7B) or `KURE-Reranker-nano` (149M) via `CrossEncoder`; scores are relevance logits, higher is better.

All stages are usable through the Sentence Transformers library, which is the reason the
release is notable — it's the first suite spanning every Sentence Transformers encoder type.

## Related

- [[entities/tom-aarsen]] — Sentence Transformers maintainer who amplified the release.
- [[concepts/colbert]] / [[entities/late-interaction]] — the multi-vector + MaxSim paradigm used by KURE-v2.
- [[concepts/embeddings]] — dense embeddings; Matryoshka dimension reduction in KURE-v3.
- [[concepts/neural-reranking]] — the CrossEncoder reranker stage.
- [[entities/jo-kristian-bergum]] — fellow retrieval-infrastructure figure (Hornet/Vespa).

## Sources

- HF Collection: https://huggingface.co/collections/nlpai-lab/kure
- KURE-v3 model card: https://huggingface.co/nlpai-lab/KURE-v3
- KURE-v2 model card: https://huggingface.co/nlpai-lab/KURE-v2
- Aarsen thread root: https://x.com/tomaarsen/status/2113607601753620588
