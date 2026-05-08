---
title: "Voyage AI"
type: entity
created: 2026-05-08
updated: 2026-05-08
tags:
  - company
  - embedding-models
  - rerankers
  - retrieval
  - rag
aliases: ["Voyage", "Voyage AI by MongoDB"]
sources:
  - https://www.voyageai.com/
  - https://blog.voyageai.com/
---

# Voyage AI

Voyage AI specializes in building state-of-the-art embedding models and rerankers for semantic search, retrieval, and retrieval-augmented generation (RAG). Founded by Stanford researchers, the company offers general-purpose, domain-specific, and custom models that outperform general-purpose alternatives in law, finance, code, and multilingual contexts.

| | |
|---|---|
| **Type** | AI Model Provider / Infrastructure |
| **Founded** | 2023 (Palo Alto, CA) |
| **Leadership** | Tengyu Ma (Co-founder & CEO, Stanford professor), Hong Liu (Co-founder), Kaidi Cao (Co-founder) |
| **Key Products** | voyage-4-large (MoE embedding), voyage-4-lite, voyage-multimodal-3.5, rerank-2, voyage-code-3, voyage-finance-2, voyage-law-2 |
| **Website** | [voyageai.com](https://www.voyageai.com) |
| **Tech Blog** | [blog.voyageai.com](https://blog.voyageai.com) |

## Key Facts

- Founded by Tengyu Ma (Stanford assistant professor), Hong Liu, and Kaidi Cao — all Stanford ML researchers
- Voyage's embeddings are the officially recommended embedding models by Anthropic
- Raised $28M Series A led by CRV; acquired by MongoDB
- Voyage-4 series introduces industry-first Mixture-of-Experts (MoE) architecture for embeddings with shared embedding space

## Products & Technology

The Voyage-4 model family features a shared embedding space enabling asymmetric retrieval (e.g., documents embedded with voyage-4-large, queries with voyage-4-lite). Models support up to 32K token context length, Matryoshka learning for variable dimensionality, and quantization-aware training. Domain-specific models exist for finance, legal, and code. Accessible via Python API.

## Related

- [[entities/harvey]] — partnered to build custom legal embeddings
- [[entities/anthropic]] — officially recommends Voyage embeddings for RAG
- [[entities/langchain]] — integrates with Voyage for embedding and retrieval pipelines
- [[entities/cohere]] — competitor in the embedding/rerank space
