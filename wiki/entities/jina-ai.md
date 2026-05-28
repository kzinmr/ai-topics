---
title: Jina AI
created: 2026-05-28
updated: 2026-05-28
type: entity
tags:
  - company
  - search
  - embeddings
  - open-source
  - information-retrieval
  - rag
sources:
  - raw/articles/2025-03-07_jina_long-context-embedding-models-blind-beyond-4k.md
  - https://jina.ai/about-us/
  - https://hanxiao.io/about/
status: active
parent: elastic
---

# Jina AI

Jina AI is a search AI company founded in 2020 by **Han Xiao**, acquired by **[[entities/elastic|Elastic]]** (NYSE: ESTC) in October 2025. It provides best-in-class embeddings, rerankers, web readers, deepsearch, and small language models for multilingual and multimodal data. Han Xiao now serves as VP of AI at Elastic.

## Company Facts

| Field | Detail |
|-------|--------|
| **Founded** | 2020 |
| **Founder** | Han Xiao (Ph.D., TU Munich) |
| **HQ** | Sunnyvale, California, USA |
| **Acquired by** | Elastic (Oct 2025) |
| **Total Funding** | $37.5M |
| **Employees** | ~13 (2026) |
| **Open Source** | Yes (Apache 2.0 for many models) |

## Key Products

### Embedding Models

- **[[concepts/embedding-long-context-degradation#jina-embeddings-v3|jina-embeddings-v3]]** (2024.9): 570M params, 8K context, 1024-dim output, 5 task-specific LoRA adapters (retrieval.query, retrieval.passage, separation, classification, text-matching). Based on XLM-RoBERTa with RoPE. Matryoshka Representation Learning enables dimension truncation down to 32. Outperforms OpenAI/Cohere on MTEB English tasks.
- **[[entities/jina-embeddings-v4|jina-embeddings-v4]]** (2025.6): Universal multimodal multilingual embeddings. EMNLP 2025 MRL Workshop.
- **[[entities/jina-embeddings-v5-omni|jina-embeddings-v5-omni]]** (2026): Multimodal embeddings (text, image, video, audio) via frozen-encoder model composition. "Geometry-preserving Embeddings via Locked Aligned Towers."
- **jina-embeddings-v5-text** (2026.2): Task-targeted embedding distillation. SIGIR 2026.

### Other Products

- **Reader API** (`r.jina.ai`): URL content extraction/fetching
- **Search API** (`s.jina.ai`): Web search with SERP results
- **Reranker**: jina-reranker-m0 for search result re-ranking
- **DeepSearch**: Multi-step web research capability

## Notable Research

- **Long-context embedding blindness study** (Mar 2025): Demonstrated that jina-embeddings-v3 — despite its 8K token support — loses retrieval capability beyond ~4K tokens, with near-random discrimination (AUC 0.50) at 8K. See [[concepts/embedding-long-context-degradation|Embedding Long-Context Degradation]].
- **Fashion-MNIST** (pre-Jina): Han Xiao created this widely-cited benchmark (12,000+ citations).

## Relationships

- **Parent**: [[entities/elastic|Elastic]] (acquired Oct 2025)
- **Founder**: Han Xiao → now VP of AI at Elastic
- **Competitors/Peers**: [[entities/cohere|Cohere]] (embeddings), [[entities/openai|OpenAI]] (embeddings)
- **Related concepts**: [[concepts/embeddings|Embeddings]], [[concepts/embedding-long-context-degradation|Embedding Long-Context Degradation]], [[concepts/information-retrieval|Information Retrieval]], [[concepts/mrcr|MRCR]]
