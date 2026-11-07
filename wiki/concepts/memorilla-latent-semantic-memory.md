---
title: "Memorilla (Latent Semantic Memory for LLMs)"
created: 2026-11-07
updated: 2026-11-07
type: concept
tags:
  - agent-memory
  - memory-systems
  - retrieval
  - continual-learning
  - embeddings
  - context-compression
aliases: [Memorilla, latent semantic memory, memory tokens]
sources:
  - raw/articles/arxiv.org--arxiv-org-abs-2610-21375--58bff78c.md
  - https://arxiv.org/abs/2610.21375
  - https://news.ycombinator.com/item?id=50395919
confidence: high
---

# Memorilla (Latent Semantic Memory for LLMs)

**Memorilla** is a memory system for *frozen* LLMs that gathers information from an entire document collection into a **fixed number of query-dependent "memory tokens"** injected into the model's input embedding space (arXiv:2610.21375, submitted Oct 15 2026, v3 Nov 3 2026). Authors: Adibvafa Fallahpour, Parsa Idehpour, Vignesh Kothapalli, Nikita Mounier, Shirley Wu, Shayan Pardis, **Jure Leskovec** (Stanford). HN: 105 points.

## Mechanism

1. Documents (user chats, book chapters, agent turns) are **encoded once** into reusable embeddings.
2. At query time, a learned retriever selects query-specific information and **places it directly in the LLM's input embedding space** as ~16 memory tokens — not as retrieved text in the context window.
3. The LLM stays frozen; only the memory/retrieval sidecar is trained.

This positions Memorilla between RAG (text retrieval into context) and parametric memory: retrieval results live in *latent* space, so the token cost of "remembering a corpus" is decoupled from corpus size.

## Results (paper-reported)

- Using only **16 memory tokens**, best performance vs baselines including **Mem0** and **MemoRAG** on **5 of 8 benchmarks** spanning personalization, long-document QA, and knowledge-intensive QA.
- **FactKG: 84.33% accuracy vs 80.43% for full-context inference, with 108× fewer tokens** representing the source documents.
- **Continual learning in agents**: in a TextWorld environment where the document count = the agent's past turns, Memorilla reduces wandering back to already-explored rooms and lifts average success rate from **18.6% (full-history in-context learning) to 24.2%**.

> **Confidence note**: numbers are the authors' own evaluations; no independent replication yet as of 2026-11-07. Preprint (cs.LG/cs.AI) — no peer review stated on the arXiv page.

## Why it matters

- It is the strongest recent datapoint that **latent-space memory can beat full-context** on knowledge tasks — memory-as-tokens sidesteps both context-window limits and context degradation of the kind tracked in [[concepts/context-engineering/context-management]].
- The TextWorld result is an early demonstration of **continual learning without weight updates**, targeting the agent-trajectory setting ([[concepts/lifelong-agent-memory]]).
- Comparison against Mem0/MemoRAG makes it a direct competitor in the agent-memory-system lineage the wiki already tracks.

## Related

- [[entities/mem0]] — baseline memory system defeated on 5/8 benchmarks
- [[concepts/llm-memory-architecture]] — taxonomy this fits under (latent memory variant)
- [[concepts/lifelong-agent-memory]] — the continual-learning goal
- [[concepts/context-engineering/context-compression]] — same token-economics motive, different mechanism (learned tokens vs text compression)

## Sources

- [arXiv:2610.21375](https://arxiv.org/abs/2610.21375) — raw: `raw/articles/arxiv.org--arxiv-org-abs-2610-21375--58bff78c.md`
- [HN discussion](https://news.ycombinator.com/item?id=50395919) (105 pts, verified Nov 7 2026)
