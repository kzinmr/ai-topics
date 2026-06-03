---
title: Mixedbread
type: entity
aliases: [mixedbread-ai, mxbai]
created: 2026-06-03
updated: 2026-06-03
status: L2
sources:
  - https://www.mixedbread.com/
  - https://www.mixedbread.com/blog/latent-terms
  - https://arxiv.org/abs/2605.29384
  - https://huggingface.co/mixedbread-ai
  - https://mixedbread.com/blog/wholembed-v3
  - https://www.mixedbread.com/blog/edge-v0
related:
  - entities/benjamin-clavie
  - concepts/colbert
  - concepts/late-interaction
  - concepts/information-retrieval
tags:
  - company
  - search
  - embeddings
  - open-source
  - information-retrieval
---

# Mixedbread

Mixedbread (mixedbread-ai) is an AI retrieval and search company focused on building production-grade dense and multi-vector retrieval systems. The company bridges the gap between academic information retrieval research and production search infrastructure, with a strong commitment to open-source model releases.

## Key People

| Person | Role |
|--------|------|
| [[entities/benjamin-clavie|Benjamin Clavié]] | ML Researcher — ColBERT/late-interaction R&D, ModernBERT co-lead, PhD student at NII Tokyo |
| Sean Lee | Co-founder / Engineering |
| Aamir Shakir | Co-founder / Engineering |

## Products and Models

### mxbai-embed Series
The mxbai-embed series is Mixedbread's family of dense embedding models, widely adopted for text embedding and retrieval tasks. The flagship **mxbai-embed-large-v1** has accumulated 22M+ downloads on HuggingFace, establishing Mixedbread as a major provider of open embedding models.

### Wholembed v3 (2026-03)
Wholembed v3 is Mixedbread's breakthrough late-interaction retrieval model — an omnimodal (text, audio, image, video) model supporting 100+ languages. It was the **first semantic search model to surpass BM25** on the LIMIT benchmark (Recall@5: 92.45 vs. BM25's 85.7), overturning the conventional wisdom that semantic search has a hard ceiling against lexical methods.

Wholembed v3 serves as the default engine for **Mixedbread Search**, achieving sub-90ms search latency and sub-120ms reranking. It supports agentic search — optimized for autonomous agent-driven queries rather than just human-written queries.

### mxbai-edge-colbert-v0
A lightweight [[concepts/colbert|ColBERT]] model at 17M/32M parameters that outperforms ColBERTv2 while running efficiently on CPU. Published with the paper "Fantastic (small) Retrievers and How to Train Them" (arXiv:2510.14880). Demonstrates that smarter architecture design (ModernBERT backbone, 48-dim projection, Muon optimizer) can beat larger models.

### Mixedbread Search
A public beta search API (launched 2026-03) offering agentic search support with sub-90ms latency. Includes Vercel Native Integration for developer workflows.

## Research

### Latent Terms (2026)
Mixedbread published research demonstrating that **sparse autoencoders (SAEs) can extract BM25-ready vocabularies from dense retrievers**. This work (arXiv:2605.29384) shows that the latent representations inside dense embedding models encode lexical information that can be surfaced without any BM25 index, effectively bridging the gap between dense and sparse retrieval paradigms.

### ColBERT and Late Interaction
Much of Mixedbread's research builds on [[concepts/colbert|ColBERT]] and the [[concepts/late-interaction|late interaction]] paradigm. The company's approach treats retrieval as **semantic keyword matching** — using token-level embeddings (MaxSim) to achieve cross-encoder-quality ranking at bi-encoder speed. Benjamin Clavié organized the first Late Interaction Workshop at ECIR 2026.

### Wholembed v3 Research
The Wholembed v3 paper demonstrated that a 0.13B parameter ColBERT model can outperform 8B single-vector models on complex search benchmarks (BrowseComp-Plus), highlighting the data efficiency and scaling advantages of late-interaction architectures.

## Philosophy

Mixedbread's approach is grounded in several principles:

- **Retrieval is the bottleneck**: The retrieval layer — not the LLM — determines the success of real-world AI systems
- **Late interaction over single-vector**: Compressing documents into single vectors creates information bottlenecks; token-level representations preserve detail
- **Open-source as bridge**: Releasing models openly to bridge academic IR research and production RAG pipelines
- **Small but mighty**: Smarter architecture design over brute-force scaling (17M param models outperforming ColBERTv2)
- **Search doesn't need to be complicated, it just needs to be good**

## HuggingFace Presence

Mixedbread maintains an active open-source presence at [huggingface.co/mixedbread-ai](https://huggingface.co/mixedbread-ai), with embedding models, ColBERT models, and other retrieval tools available for download.

## Sources

- https://www.mixedbread.com/ — Company website
- https://www.mixedbread.com/blog/latent-terms — Latent Terms blog post
- https://arxiv.org/abs/2605.29384 — Latent Terms paper (2026)
- https://huggingface.co/mixedbread-ai — HuggingFace organization
- https://mixedbread.com/blog/wholembed-v3 — Wholembed v3 release blog (March 2026)
- https://www.mixedbread.com/blog/edge-v0 — mxbai-edge-colbert-v0 blog post
