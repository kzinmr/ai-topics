---
title: "You Don't Need a Graph DB for RAG (Probably)"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags:
  - concept
  - rag
  - graphrag
  - retrieval
  - evaluation
  - architecture
aliases:
  - graph-db-overengineering-rag
  - rag-overengineering
  - floppy-disk-rule
  - context-stuffing-rag
  - silver-bullet-trap-rag
  - hnsw-hidden-graph
sources:
  - path: raw/articles/2026-04-30_hamel-husain-p7-graph-db-rag.md
  - https://hamel.dev/notes/llm/rag/p7-graph-db.html
status: active
---

# You Don't Need a Graph DB for RAG (Probably)

A 2026 article by [[entities/hamel-husain|Hamel Husain]] & [[entities/jo-kristian-bergum|Jo Kristian Bergum]] arguing against premature adoption of graph databases for RAG systems. The core thesis: **GraphRAG is a technique, not a specific technology** — and most teams over-engineer their retrieval stack when simpler alternatives suffice.

## The Silver Bullet Trap

The industry pattern of jumping from vector databases to GraphRAG repeats a common engineering error: **mapping a new technique (GraphRAG) to a specific technology (a graph DB)**. This traps teams in unnecessary infrastructure complexity before they've validated whether they need the technique at all.

> *"There is no single tool that will solve all your problems. The desire to map a new technique (GraphRAG) to a technology (a graph DB) is a trap many engineers fall into."* — Jo Kristian Bergum

## The Floppy Disk Rule (Context Stuffing)

Modern LLMs (e.g., Gemini) handle ~1M tokens — approximately 3MB of text. For small document corpora, **stuffing everything into context** is often cheaper, simpler, and more effective than building a RAG stack.

**When context stuffing works:**
- A few hundred documents
- Low document overlap (few "distractors")
- When you want to sidestep retrieval errors entirely

**The main risk:** "Context rot" — performance degradation when similar-but-irrelevant documents (distractors) are present in context.

### Connection to [[concepts/context-graph|Context Graphs]]
Context stuffing is the simplest form of giving an agent full context. The [[concepts/context-graph|Context Graph]] approach extends this by making decision traces searchable — but for small data, the direct approach (stuff all the data) is often enough.

## GraphRAG Deconstructed

GraphRAG involves three steps, none of which require a graph database:

1. **Offline Processing** — LLM extracts entities (nodes) and relationships (edges) from documents
2. **Triplet Storage** — Data stored as `(source_entity, relationship, target_entity)` triplets
3. **Runtime Traversal** — Traverse relationships at query time

**Storage options for triplets:**
- CSV files
- JSON objects
- Standard relational databases (e.g., **Postgres**)

This directly contrasts with [[concepts/agentic-alternative-to-graphrag|Contextual AI's agentic alternative]], which replaces static triplet traversal with agentic tool-use against a metadata index. Both approaches show that the graph traversal task doesn't require a dedicated graph DB.

## When a Graph DB Is Actually Necessary

A specialized graph database (Neo4j, etc.) is only justified if you can answer "Yes" to:

| Question | Threshold |
|----------|-----------|
| Ultra-low-latency traversal needed? | Sub-millisecond multi-hop queries |
| Graph too massive for Postgres/flat files? | Billions of edges with real-time traversal |
| Complex multi-hop queries required? | "Friends of friends of friends" depth |

> *"Early Facebook ran its massive social graph on MySQL. You can get surprisingly far with general-purpose tools."*

## HNSW as the Hidden Graph

Most RAG practitioners are already using graphs without realizing it. The **HNSW (Hierarchical Navigable Small World)** algorithm — used in virtually all vector databases — is fundamentally a graph structure where:
- **Nodes** = vectors (document embeddings)
- **Edges** = connections between neighbors in embedding space

### Actionable Strategy: Graph-like Retrieval Without a Graph DB

The **"cluster hypothesis"** (similar documents are often co-relevant) enables multi-hop retrieval using standard vector tools:

1. **Initial Search** — Run a standard vector search
2. **Filter/Rerank** — Use an LLM or reranker to find the most relevant result
3. **Expansion** — Perform a second search for documents similar to that specific relevant result (its "neighbors" in the HNSW graph)

This achieves graph-like traversal (node → neighbor → neighbor's neighbor) without any graph database infrastructure.

## Evaluation: The Prerequisite for Complexity

Never adopt GraphRAG or a graph DB without a **Golden Dataset** to prove it helps. Standard IR metrics:

| Metric | What It Measures |
|--------|-----------------|
| **Mean Reciprocal Rank (MRR)** | How high the first relevant document appears |
| **Precision** | % of returned documents that are relevant |
| **Recall** | % of all relevant documents successfully found |

This aligns with [[concepts/harness-engineering|Harness Engineering]] philosophy — measure first, add complexity only when validated.

## Key Takeaways

| Idea | Implication |
|------|------------|
| **Sophistication ≠ Complexity** | Better RAG comes from better evals and reasoning, not more infrastructure |
| **Start Small** | Use context windows for small data; Postgres/SQL for structured relationships |
| **HNSW is a Graph** | Multi-hop-style retrieval via existing vector DB neighbors |
| **Measure First** | No benchmark improvement = no justification for new DB |

## Graph Structure Query for Wiki Knowledge Base

This concept page is designed to serve as a **graph traversal node** in the wiki knowledge base. Cross-references create the following graph edges:

```
[graph-db-overengineering-rag] ──author──→ [hamel-husain]
[graph-db-overengineering-rag] ──coauthor──→ [jo-kristian-bergum]
[graph-db-overengineering-rag] ──contrasts──→ [agentic-alternative-to-graphrag]
[graph-db-overengineering-rag] ──extends──→ [knowledge-graph-memory-agents]
[graph-db-overengineering-rag] ──relates-to──→ [context-graph]
[graph-db-overengineering-rag] ──embodies──→ [harness-engineering]
[graph-db-overengineering-rag] ──teaches──→ [ai-evals]
```

## Related Concepts

- [[concepts/knowledge-graph-memory-agents]] — Knowledge graph memory for agents; this article provides the "you probably don't need a dedicated graph DB" constraint
- [[concepts/agentic-alternative-to-graphrag]] — Contextual AI's metadata search approach; both argue against static graph DBs but propose different alternatives (metadata index vs HNSW expansion)
- [[concepts/context-graph]] — Enterprise context graphs; complementary perspective on graphs as decision traces rather than retrieval infrastructure
- [[concepts/harness-engineering]] — Measure-first philosophy embodied in the evaluation prerequisite
- [[concepts/ai-evals]] — Golden dataset approach to validating retrieval improvements
- [[concepts/agentic-rag]] — Broader taxonomy of agentic retrieval

## Sources

- [P7: You Don't Need a Graph DB (Probably) — Hamel's Blog](https://hamel.dev/notes/llm/rag/p7-graph-db.html)
- [Raw article: 2026-04-30_hamel-husain-p7-graph-db-rag.md](raw/articles/2026-04-30_hamel-husain-p7-graph-db-rag.md)
