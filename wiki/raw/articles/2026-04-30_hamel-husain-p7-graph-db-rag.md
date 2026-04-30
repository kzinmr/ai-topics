# P7: You Don't Need a Graph DB (Probably)

**Author:** Hamel Husain & Jo Kristian Bergum
**Source:** https://hamel.dev/notes/llm/rag/p7-graph-db.html
**Scraped:** 2026-04-30

## Summary

The article argues against prematurely adopting graph databases for RAG systems. It deconstructs GraphRAG as a technique (not a specific technology), demonstrates how graph-like retrieval can be achieved with standard tools (Postgres, HNSW), and advocates for evaluation-first architecture decisions.

## Key Points

### 1. The "Silver Bullet" Trap
The industry shift from vector DB to GraphRAG repeats a pattern: mapping a new technique to a specific technology. Bergum warns this is a common engineering error.

### 2. The Floppy Disk Rule (Context Stuffing)
Modern LLMs handle ~1M tokens (~3MB text). For small corpora, stuffing everything into context is cheaper, simpler, and often more effective than building a RAG stack. "Context rot" (distractors) is the main risk.

### 3. GraphRAG Deconstructed
GraphRAG = offline LLM entity extraction + triplet storage + runtime traversal. Triplets can be stored in CSV, JSON, or Postgres — no graph DB needed.

### 4. When Graph DB Is Actually Necessary
Ultra-low-latency traversal, massive scale beyond Postgres, complex multi-hop queries (e.g., "friends of friends of friends").

### 5. HNSW as Hidden Graph
HNSW (Hierarchical Navigable Small World) used in all vector DBs IS a graph structure. You can do graph-like retrieval via: vector search → filter/rerank → expand to neighbors.

### 6. Evaluation Prerequisite
Never adopt GraphRAG without a Golden Dataset. Metrics: MRR, Precision, Recall.

## Key Quote
> "There is no single tool that will solve all your problems. The desire to map a new technique (GraphRAG) to a technology (a graph DB) is a trap many engineers fall into."
