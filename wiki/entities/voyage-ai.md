---
title: "Voyage AI"
type: entity
created: 2026-05-08
updated: 2026-06-30
tags:
  - company
  - rag
aliases: ["Voyage", "Voyage AI by MongoDB"]
sources:
  - https://www.voyageai.com/
  - https://blog.voyageai.com/
  - raw/articles/blog.voyageai.com--2026-06-29-voyage-context-4--47aada90.md
---

# Voyage AI

Voyage AI specializes in building state-of-the-art embedding models and rerankers for semantic search, retrieval, and retrieval-augmented generation (RAG). Founded by Stanford researchers, the company offers general-purpose, domain-specific, and custom models that outperform general-purpose alternatives in law, finance, code, and multilingual contexts.

| | |
|---|---|
| **Type** | AI Model Provider / Infrastructure |
| **Founded** | 2023 (Palo Alto, CA) |
| **Leadership** | Tengyu Ma (Co-founder & CEO, Stanford professor), Hong Liu (Co-founder), Kaidi Cao (Co-founder) |
| **Key Products** | voyage-4-large (MoE embedding), voyage-4-lite, voyage-context-4, voyage-multimodal-3.5, rerank-2, voyage-code-3, voyage-finance-2, voyage-law-2 |
| **Website** | [voyageai.com](https://www.voyageai.com) |
| **Tech Blog** | [blog.voyageai.com](https://blog.voyageai.com) |

## Key Facts

- Founded by Tengyu Ma (Stanford assistant professor), Hong Liu, and Kaidi Cao — all Stanford ML researchers
- Voyage's embeddings are the officially recommended embedding models by Anthropic
- Raised $28M Series A led by CRV; acquired by MongoDB
- Voyage-4 series introduces industry-first Mixture-of-Experts (MoE) architecture for embeddings with shared embedding space

## Products & Technology

The Voyage-4 model family features a shared embedding space enabling asymmetric retrieval (e.g., documents embedded with voyage-4-large, queries with voyage-4-lite). Models support up to 32K token context length, Matryoshka learning for variable dimensionality, and quantization-aware training. Domain-specific models exist for finance, legal, and code. Accessible via Python API.

### Voyage-context-4 (June 2026)

voyage-context-4 is the next-generation contextualized chunk embedding model from Voyage AI, released June 29, 2026. It produces chunk embeddings that capture full document context without manual metadata or context augmentation.

**Key innovations:**
- New Mixture-of-Experts (MoE) backbone for improved context-aware embeddings
- Built-in auto-chunking — send entire documents, the model chunks them automatically, removing the need for a separate chunking pipeline
- No context window limit — documents longer than 32K tokens are split and embedded transparently
- Native support for overlapping chunks for compatibility with pre-existing pipelines
- Supports Matryoshka dimensions: 2048, 1024, 512, 256

**Performance:** Averaged across 39 datasets spanning 8 domains (technical documentation, web, code, medical, conversation, law, finance, long-context):
- Chunk-level retrieval: 2.08% improvement over voyage-context-3
- Document-level retrieval: 1.4% improvement over voyage-context-3
- Single-embedding evaluation: beats voyage-4-large by 0.45%, OpenAI v3 large by 28.80%
- especially strong on LongEmbed: 7.11% over single-vector embeddings

**Pricing:** $0.12/1M tokens (33% reduction from voyage-context-3's $0.18/1M)

**Availability:** Available via Voyage API and MongoDB Atlas (Atlas Embedding and Reranking API). First 200M tokens free.

## Related

- [[entities/harvey]] — partnered to build custom legal embeddings
- [[entities/anthropic]] — officially recommends Voyage embeddings for RAG
- [[entities/langchain]] — integrates with Voyage for embedding and retrieval pipelines
- [[entities/cohere]] — competitor in the embedding/rerank space
