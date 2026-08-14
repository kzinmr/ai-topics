---
title: "Voyage AI"
type: entity
created: 2026-05-08
updated: 2026-08-14
tags:
  - company
  - rag
aliases: ["Voyage", "Voyage AI by MongoDB"]
sources:
  - https://www.voyageai.com/
  - https://blog.voyageai.com/
  - raw/articles/blog.voyageai.com--2026-06-29-voyage-context-4--47aada90.md
  - raw/articles/2026-08-08_fireworks-ai_voyage-ai-models-now-on-fireworks.md
  - raw/articles/blog.voyageai.com--2026-08-13-voyage-code-4--cce0287e.md
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

## Fireworks Partnership — Native Inference Platform (August 2026)

On August 5, 2026, Fireworks AI announced it became the **first and only dedicated inference platform** Voyage AI has partnered with. The full Voyage lineup now runs natively on Fireworks — the **Voyage 4 family** (voyage-4-large, voyage-4, voyage-4-lite, voyage-4-nano), **voyage-multimodal-3.5**, and **rerank-2.5** — enabling a complete embed → retrieve → rerank → generate pipeline on one platform, one API, one latency domain. [[entities/fireworks-ai]] also serves open-weight generation models and post-training (RFT), closing the loop between retrieval grounding and specialized intelligence.

**Benchmark position (Voyage 4 series, average retrieval quality):** voyage-4-large is top-performing — +1.87% vs voyage-4, +4.80% vs voyage-4-lite, +3.87% vs Gemini Embedding 001, **+8.20% vs Cohere Embed v4**, and **+14.05% vs OpenAI v3 Large**.

**Positioning:** The partnership resolves the consolidation tradeoff — teams previously chose between a separate retrieval vendor (two bills, two latency profiles, wider security/compliance surface) or a single platform with capped retrieval quality. Voyage on Fireworks keeps proprietary data inside fewer trust boundaries without sacrificing frontier retrieval quality.

## Voyage-code-4 — Code Retrieval for Coding Agents (August 2026)

On August 13, 2026, Voyage AI released **voyage-code-4**, a next-generation code embedding model purpose-built for the retrieval patterns of coding agents. Since voyage-code-3 launched in December 2024, coding *agents* now issue many of the code retrieval queries — they explore, backtrack, and re-query across multiple steps, often starting from a goal as vague as *"find everywhere we mishandle empty arrays."* voyage-code-4 targets exactly that workload.

**Key innovations:**
- **New training corpus mined from completed pull requests**: conventional code embedding corpora (source files paired with docstrings/comments) teach what code *says* but not what code *does wrong* — the context an agent needs when starting from a bug report. The new corpus spans hundreds of thousands of natural-language queries across hundreds of programming languages and tens of thousands of repositories, substantially larger than the voyage-code-3 corpus.
- **Matryoshka learning**: supports 2048, 1024, 512, and 256 dimensional embeddings.
- **Quantization**: float32, signed/unsigned int8, and binary precision with minimal quality loss.
- **Pricing**: $0.12 per 1M tokens — a third below voyage-code-3.

**Performance:**
- **Agentic code retrieval** (new benchmark of 19 datasets built from issue-fixing pull requests, where each query is an issue description and relevant documents are the files the merged fix touched): voyage-code-4 outperforms voyage-code-3, Cohere Embed v4, Gemini Embedding 2, and OpenAI v3 large by **27.54%, 28.25%, 31.03%, and 48.58%** respectively (NDCG@10).
- **Traditional code search** (the 28 voyage-code-3 evaluation datasets across five categories): outperforms the same models by **13.98%, 19.21%, 16.01%, and 40.06%** respectively.
- The agentic benchmarks are being added to the RTEB evaluation suite.

**Why agents need semantic retrieval:** most agents today rely on full-text search (grep), which works when the agent knows the identifier it seeks but returns no useful hits for symptom-based queries (e.g., a bug report). Semantic retrieval with voyage-code-4 complements full-text search and significantly reduces wasted token usage — an agent may issue dozens of retrieval queries per task, each consuming prompt tokens, output tokens, and wall-clock time.

**Availability:** via the Voyage API and MongoDB Atlas Embedding and Reranking API; first 200 million tokens free.

## Related

- [[entities/fireworks-ai]] — first dedicated inference platform partner (August 2026); native Voyage lineup hosting
- [[entities/harvey]] — partnered to build custom legal embeddings
- [[entities/anthropic]] — officially recommends Voyage embeddings for RAG
- [[entities/langchain]] — integrates with Voyage for embedding and retrieval pipelines
- [[entities/cohere]] — competitor in the embedding/rerank space
