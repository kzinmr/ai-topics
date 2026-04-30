---
title: Doug Turnbull - Core Ideas & Philosophy
type: entity-sub
parent: doug-turnbull
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - philosophy
  - search
  - relevance
sources: []
---

# Doug Turnbull: Core Ideas & Philosophy

## Search Relevance as Engineering, Not Magic

Turnbull's foundational philosophy is that **search quality is not a mystical property — it is a systematic engineering problem** that can be measured, tested, and improved iteratively. His methodology emphasizes:

1. **Define "relevant"** for your specific use case and users
2. **Build test collections** — curated queries with human judgments (judgment lists)
3. **Measure continuously** — NDCG, precision, recall, and engagement metrics
4. **Iterate on signals** — adjust ranking features based on measurement feedback
5. **Start with naive baselines** — simple keyword search before complex ML

This approach democratized search relevance, making it accessible to organizations without dedicated IR research teams.

## The Judgment List Methodology

One of Turnbull's most influential contributions is the **judgment list** pattern: building curated collections of queries paired with human relevance judgments. These serve simultaneously as:

- **Test suites** — measuring whether configuration changes improve or degrade quality
- **Training data** — feeding learning-to-rank models
- **Communication tools** — aligning cross-functional teams on what "good" search looks like
- **Regression tests** — preventing quality degradation over time

He advocates for what he calls "grug-brained evals": don't spend months building perfect quality metrics. Start with simple 👍/👎 labels from coworkers and iterate.

## From Keyword to Semantic to Agentic Search

Turnbull has tracked and shaped the industry's evolution through search paradigms:

**Phase 1: Keyword Search (BM25, TF-IDF)** — Exact matching via inverted indices; works well for known-item searches; still the foundation of most production systems.

**Phase 2: Semantic Search (Embeddings)** — Vector representations capture meaning beyond keywords; dense retrieval via HNSW/ANN indexes; late-interaction models (ColBERT) score passages dynamically.

**Phase 3: AI-Powered Search (LLMs, RAG)** — Language models understand query intent, generate answers, and power conversational retrieval.

**Phase 4: Agentic Search** — LLM agents that iterate, refine queries, evaluate results, and recover from failures. "Agents put the Resilient in RAG."

In *AI-Powered Search*, he argues the future is **hybrid** — combining keyword precision, semantic understanding, and generative capabilities rather than replacing one with another.

## Learning to Rank (LTR)

Turnbull was an early and sustained advocate of **learning-to-rank**: using ML models (decision trees, XGBoost, LambdaMART) to combine multiple ranking signals into an optimal ranking function. His contributions include:

- The **Elasticsearch LTR plugin** — open-source integration enabling LTR within Elasticsearch
- **hello-ltr** — Jupyter notebook sandbox for learning and experimenting with LTR
- Production LTR systems at Reddit, where he scaled Learning to Rank to thousands of QPS
- Emphasis on the painful realities of LTR: garbage in, garbage out; the need for quality judgment lists; dealing with position bias and presentation bias

## RAG Isn't a Vector Search Problem

A central thesis in Turnbull's recent writing is that **the RAG community over-indexes on embeddings and under-appreciates classical IR**. His December 2025 article *"RAG Users Want Affordances, Not Vectors"* [[raw/articles/2025-12-09_doug-turnbull-rag-users-want-affordances]] lays out three specific failure modes of pure vector search for RAG:

### Embedding Crowding
Off-the-shelf embedding models are trained on general web data. In specific domains (e.g., finance), distinct concepts like "S1 filings" and "quarterly earnings" appear nearly identical, creating a "clumped" vector space where everything has high similarity (e.g., 0.1 cosine distance).

### The Threshold Problem
Vector search provides a similarity gradient, not a "match/no-match" binary. A correct answer might score 0.9 while a related but incorrect answer scores 0.8 — and there is no universal cutoff because a different query might return the correct answer at 0.6 similarity. **Without classifiers, pure vector retrieval cannot distinguish correct from incorrect information.**

### In-Domain Nuance
General embedding leaderboards do not reflect industry performance:
- "High yield" → junk bonds (risk), not high returns
- "Chinese walls" → information barriers for compliance, not a physical wall

### Resulting Principles
- Embeddings alone lack match/non-match awareness
- "Similarity floors don't work consistently" — a cutoff that works for one query may be disastrous for another
- BM25 and lexical matching remain essential complements to vector retrieval
- User engagement data (clicks, hovers, session behavior) is the most valuable signal for improving RAG quality — yet most RAG teams rely exclusively on human/LLM evaluation

He calls this gap **"RAG's big blindspot"** — the lack of engagement-based evaluation in an era obsessed with LLM judges.

### The Affordances Solution
Turnbull invokes Donald Norman's **affordances** concept: users want to manipulate data using specific selectors, not just nearest-neighbor similarity. Effective search is more about **Information Architecture** and **Data Modeling** than semantic similarity.

The solution: use LLMs as **query understanding powerhouses** — translate free-text queries into structured schemas with typed fields:

```python
class Query(BaseModel):
    styles: List[str]
    materials: List[Literal["leather", "suede", "..."]]
    classification: str  # e.g., "Living Room / Sofas"
```

Then decompose similarity spaces by attribute:
- **Style** → CLIP/visual embeddings
- **Material** → Exact taxonomic matches
- **Classification** → Hierarchical ranking (direct matches > siblings > cousins)

### The Tiered Strategy
Great search follows a three-tier approach:
1. **High-Precision Intent** — Structured, filtered results when query is understood
2. **Fallback Retrieval** — BM25 or vector search when confidence is low
3. **Multi-Factor Ranking** — Relevance > similarity: popularity, recency, authority, proximity

**Diversity is critical for agentic loops:** agents need to see a broad range of results to learn how to reformulate queries. Ten identical results kill agent exploration.

This article is a direct predecessor to Turnbull's 2026 "Grep Moment" and "Rag is the What" talk — it established the foundational critique of vector-centric RAG that later evolved into the full agentic search framework.

## Query Understanding > Ranking

Turnbull consistently argues that **query understanding matters more than ranking algorithms**:

- "Content understanding IS query understanding"
- LLMs eliminate the excuse for unstructured query handling — all search is structured now
- Manual search management (synonyms, rules, boosts for specific queries) often outperforms algorithmic approaches
- At Shopify, the user segment with the highest conversions was the one with manually controlled results — proving that domain expertise beats generic ranking models
- "The dirty secret of Google and Amazon search is all the manual annotation, rules, etc they manage"

## Agents Turn Simple Keyword Search into Compelling Experiences

In September 2025, Turnbull published a landmark blog post arguing that **traditional "thick" search APIs are counterproductive for AI agents**:

> "Because of this, I'd argue the traditional, thick search APIs are counterproductive to being used by agents. They may be too complex for agents to reason about effectively."

He demonstrated that agents perform best with **simple, predictable keyword search** (e.g., bare-bones BM25) because:
1. **Transparent reasoning:** Agents can understand exactly how results are produced, enabling them to iteratively refine queries
2. **Predictable behavior:** Simple APIs don't hide query understanding, synonym expansion, or reranking — the agent itself provides these capabilities
3. **Iterative adaptation:** Agents can test multiple queries, evaluate results, and learn from failures in real-time

His experiments showed agents successfully handling abstract queries like `"couch fit for a vampire"` or `"ugliest chair in the catalog"` by iteratively testing keyword variations and reasoning about results.

### LLM-as-a-Judge and Semantic Caching

Turnbull introduced a pattern where agents **self-evaluate** their search results and log interactions:

```
Saved interaction: user_query='ugliest chair in the catalog'
search_tool_query='cow print chair'
quality='good'
reasoning="Returned an adult 'cow print task chair' that clearly fits a loud/novelty aesthetic..."
```

These logged interactions become a **semantic cache** — new queries are matched to past ones via vector similarity, surfacing what worked or failed before. The agent's interaction history evolves into a **knowledge graph of user intent**, connecting similar queries with performance notes.

### The Clickstream Blindspot

Turnbull identified a critical risk in agentic search: **agents lack access to implicit human behavior signals**. Traditional search relies on decades of noisy but valuable clickstream data. An agent may rate highly engaging results as "meh" because they don't align with logical deduction — creating a mismatch between reasoning quality and actual user satisfaction.

## Semantic Search Without Embeddings

In January 2026, Turnbull published a provocative argument: **semantic search does not require embeddings**. He decomposed semantic search into three pillars:

1. **Representation** — A shared space mapping queries and content
2. **Similarity Function** — Measures proximity in that space
3. **Match Criteria** — Explicit inclusion/exclusion logic ("It is the thing, or it's not the thing")

Embeddings excel at the first two pillars but fail catastrophically at the third. Users reject "semantically close but wrong" results (e.g., baseballs appearing for fruit queries).

### Hierarchical Taxonomies as the Alternative

Turnbull proposed using **managed hierarchical taxonomies** instead:

```
Baby & Kids / Toddler & Kids Playroom / Indoor Play / Rocking Horses / Novelty Rocking Horses
```

By tokenizing category paths hierarchically and feeding them into BM25, you get natural specificity scoring: root nodes have high document frequency (lower BM25 score), while leaf nodes have low document frequency (higher BM25 score). This provides **precise match criteria** — "it is the thing or it's not" — which embeddings fundamentally cannot do.

### LLM-Augmented Taxonomy Building

Turnbull demonstrated a clever trick: prompt small LLMs to **creatively generate plausible taxonomy paths** for queries before mapping them to real ones:

> "Be creative and hallucinate a set of classifications for the query below that look like the real classifications... If you feel inspired, return many unique values in a list."

The hallucinated paths (e.g., `'Baby & Kids / Toys / Pretend Play & Dress Up / Hobby Horses'`) use natural language closer to the actual taxonomy, improving mapping accuracy. Small models suffice since creativity matters more than precision at this stage.

## Bayesian BM25 and Score Calibration

In 2026, Turnbull published work on **Bayesian BM25** — a method for calibrating BM25 scores into probabilities:

> `P(R) = prob(embeddings) × prod(lexical)`

This provides a principled way to combine lexical and embedding scores in hybrid search, treating them as probabilistic signals rather than arbitrary numbers. It addresses a long-standing pain point: BM25 scores are unbounded and hard to interpret (0.5? 5.1? 12.51?), making them difficult to fuse with vector similarity scores.

## Throwaway Code Over Design Docs

Reflecting on the AI coding revolution, Turnbull advocates for **rapid, disposable prototypes** over lengthy architecture documents:

> "If you have discipline to throw away your first idea, draft, throwaway code — you can move faster than any design doc."

With AI generating code, **tests become the most important artifact to maintain**: "The tests are the code now."

## SearchArray: Making Search Less Weird

Turnbull built **SearchArray** (304 GitHub stars) to make search relevance experimentation accessible:

> "Traditional search engines are weird. As my job looks more and more like ML engineering, these backend systems feel even stranger."

SearchArray is a pandas extension array backed by an inverted index. It lets practitioners run full end-to-end search relevance experiments in a single Colab notebook — no Solr or Elasticsearch instance required. Under the hood it uses Cython-optimized roaring bitmap intersections for phrase search.

> "If I had Relevant Search to write over again, I'd use a tool like this. Get lexical search away from the baggage of any one particular giant search stack."

## The Business Case for Search

Turnbull frames search relevance as a **business problem**, not a technical one:

- Better search → higher conversion rates → more revenue
- Better search → fewer support queries → lower costs
- Better search → improved user satisfaction → higher retention

His track record proves this:
- **Reddit**: 2% DAU increase from ML ranking improvements
- **Daydream**: 2× conversion rate improvement from CLIP-based hybrid search
- **Shopify**: 10% YoY revenue improvement from merchant search optimization

## Don't Have F-You Money? Build an F-You Network

Beyond technical work, Turnbull is known for pragmatic career advice:

> "Start with Who, not Why. Work with amazing people you love collaborating with, the rest falls out."

He advocates building a professional network through genuine service and deep expertise — a safety net that provides career resilience independent of any single employer.

## Related

- [[doug-turnbull]] — Main entity page
