---
title: "RAG Users Want Affordances, Not Vectors"
created: 2025-12-09
author: Doug Turnbull (@softwaredoug)
source: Blog (softwaredoug.com)
url: https://softwaredoug.com/blog/2025/12/09/rag-users-want-affordances-not-vectors
type: article
tags: [agentic-search, rag, vector-search, affordances, query-understanding, information-architecture, bm25, structured-search]
aliases:
  - rag-is-not-a-vector-search-problem
  - rag-users-want-affordances-not-vectors
---

# RAG Users Want Affordances, Not Vectors

A foundational article by Doug Turnbull arguing that RAG has been mischaracterized as a "vector search problem" — users want **affordances** (structured query understanding, domain-specific filters, explicit match criteria), not just semantic similarity.

## Core Thesis

The industry mistakenly treated RAG as a simple question-answering system where a natural language question is encoded into an embedding to find a similar passage. This fails for three fundamental reasons.

### 1. The Failure of Pure Vector Search

**Embedding Crowding:** Off-the-shelf models are trained on general web data. In specific domains (e.g., finance), distinct concepts like "S1 filings" and "quarterly earnings" appear nearly identical to a general model, leading to a "clumped" vector space where everything has high similarity (e.g., 0.1 cosine distance).

**Lack of Binary Filtering:** Vector search provides a similarity gradient, not a "match/no-match" binary.
- **The Threshold Problem:** A correct answer might have 0.9 similarity, while a related but incorrect answer has 0.8. There is no universal cutoff; a different query might return the correct answer at 0.6 similarity.
- **Result:** Without classifiers, pure vector retrieval cannot distinguish between correct and incorrect information.

**In-Domain Nuance:** General leaderboards do not reflect industry performance:
- "High yield" → might mean junk bonds (risk), not actual high returns
- "Chinese walls" → refers to information barriers for compliance, not a physical wall

### 2. Users Want Affordances, Not Just Similarity

Turnbull invokes Donald Norman's concept of **affordances**: the perceived and actual properties of a thing that determine how it could possibly be used.

> Users want to manipulate data using **specific selectors**. Effective search is more about Information Architecture and Data Modeling than semantic similarity.

**LLMs as Query Understanding Powerhouses:** Instead of using LLMs just to generate answers, use them to translate free-text queries into structured schemas:

```python
class Query(BaseModel):
    styles: List[str] = Field(description="The visual style the user wants.")
    materials: List[Literal["leather", "suede", "..."]] = Field("The material.")
    classification: str = Field("How the item is classified, i.e. Living Room / Sofas")
```

**Decomposing Similarity Spaces:** By structuring the query, different retrieval techniques apply to different attributes:
- **Style** → CLIP/visual embeddings
- **Material** → Exact taxonomic matches
- **Classification** → Hierarchical ranking (direct matches > siblings > cousins)

### 3. The Search Engine Approach to RAG

Great search (and RAG) should follow a **tiered strategy**:

1. **High-Precision Intent** — When query is understood, provide structured, filtered results
2. **Fallback Retrieval** — When confidence is low, BM25 or vector search
3. **Multi-Factor Ranking** — Relevance > similarity: popularity, recency, authority, proximity

**Diversity and Agentic Loops:** Agents need to see a broad range of results to learn how to reformulate queries effectively. Ten identical results kill agent exploration.

### 4. Conclusion: The Vector Distraction

> Vector search should be a **component**, not the entire system. Teams should incrementally layer vector retrieval into existing keyword search. **RAG is about query understanding** to explore a corpus, not just finding the nearest neighbor.

## Connection to Wiki

This article is a direct predecessor to Turnbull's 2026 "Grep Moment" and "Rag is the What" talk — it established the foundational critique of vector-centric RAG that later evolved into the full agentic search framework. Key ideas that carry forward:

- **[[concepts/agentic-search]]** Level 1 — BM25/sparse retrieval over dense for agent queries (confirmed by Meng et al. 2026)
- **[[concepts/agentic-search]]** Level 2 — LLM as query understanding engine (harness layer)
- **Neural retrieval as component, not the system** — confirmed by SID-1 approach where RL-trained model drives simple tools
- **Affordances > Vectors** — The structured schema approach is what Turnbull later calls "all search is structured now"

## Sources

- [Original article](https://softwaredoug.com/blog/2025/12/09/rag-users-want-affordances-not-vectors)
