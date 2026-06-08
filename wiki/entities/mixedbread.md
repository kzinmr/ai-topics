---
title: Mixedbread
created: 2026-06-04
updated: 2026-06-04
type: entity
tags:
  - company
  - search
  - model
  - developer-tooling
  - open-source
sources:
  - raw/articles/2026-06-02_mixedbread_dense-retrievers-know-more.md
  - https://www.mixedbread.com/blog/latent-terms
  - https://x.com/mixedbreadai
status: active
---

# Mixedbread

Mixedbread (mixedbread ai inc.) is an AI company focused on search and retrieval technology. They develop embedding models, sparse retrieval methods, and search APIs. Known for their research on Latent Terms — extracting BM25-ready vocabularies from dense retrieval models via Sparse AutoEncoders.

## Products & Research

- **Search API / Embedding API**: Core product offering semantic search, vector search, and retrieval capabilities
- **Wholembed-v3**: Late interaction embedding model using MaxSim scoring
- **Latent Terms** (Jun 2026): Research demonstrating that dense retrieval models contain extractable sparse vocabularies following Zipfian distributions, compatible with BM25. arXiv: [2605.29384](https://arxiv.org/abs/2605.29384)
- Blog: [mixedbread.com/blog](https://www.mixedbread.com/blog)

## Key People

- [[entities/ben-clavie|Ben Clavie]] — Researcher, lead author of Latent Terms paper
- Sean Lee — Co-author on Latent Terms
- Aamir Shakir — Co-author on Latent Terms
- Makoto P. Kato — Co-author on Latent Terms

## Research Focus

Mixedbread's research centers on understanding and improving information retrieval:

1. **Scoring operator expressiveness**: Demonstrating that the bottleneck in retrieval is not model capacity but the expressiveness of scoring operators (cosine similarity vs MaxSim vs BM25)
2. **Sparse extraction from dense models**: Using SAEs to extract latent vocabularies from retrieval-trained models
3. **Late interaction**: Multi-vector retrieval via MaxSim (ColBERT-style) as superior to single-vector approaches

## Related

- [[concepts/late-interaction]] — Late interaction retrieval paradigm that Mixedbread's models leverage
- [[entities/antoine-chaffin]] — LightOn researcher who analyzes Mixedbread's work from a retrieval theory perspective
- [[entities/ben-clavie]] — Research lead at Mixedbread
