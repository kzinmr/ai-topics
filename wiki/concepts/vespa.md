---
title: "Vespa"
type: concept
created: 2026-04-25
updated: 2026-11-13
tags:
  - concept
  - infrastructure
  - search
  - information-retrieval
  - vector-search
  - open-source
sources:
  - https://github.com/vespa-engine/vespa
  - https://docs.vespa.ai
aliases:
  - vespa
  - Vespa.ai
---

# Vespa

**Vespa** is an open-source (Apache-2.0, ~7.2k stars) **AI search platform** developed at Vespa Inc. (Oslo; formerly Yahoo Search & Advertising engineering). It is one of the few systems that combines, in a single engine: **large-scale vector similarity search (HNSW), classic lexical/text ranking (BM25), tensor computation for ML models, and real-time updates across a full-corpus document database** — which is why it keeps appearing in hybrid-retrieval and agent-RAG infrastructure discussions in this wiki.

## Why it matters for AI/RAG

- **Hybrid search as a first-class feature** — lexical + nearest-neighbor + learned ranking can be combined in one query (best of both, without a separate vector DB + search stack). See [[concepts/agentic-retrieval]] and [[concepts/rag-not-dead-series]].
- **Tensors in the search tier** — Vespa's ranking expressions run embedding models and cross-encoders (late interaction / ColBERT-style reranking, see [[concepts/late-interaction-retrieval]]) inside the query pipeline at ranking time.
- **Real-time corpus at scale** — streaming updates to billions of documents, which distinguishes it from batch-indexed alternatives.
- Powers the search infrastructure at companies like **Shopify, Qualcomm, Discord, Costco, Strava** (per Vespa Inc. case studies).

## Architecture essentials

```
Documents ──▶ Content nodes (proton)
              ├─ Document DB + index modules
              ├─ HNSW vector indexes
              └─ Attribute/vector store
Query ──▶ Container nodes (JAX-RPC/Java)
              ├─ Query pipeline
              ├─ Ranking: first-phase → second-phase (tensor models)
              └─ YQL query language (SQL-like)
```

- **YQL** — SQL-like query language over document schemas.
- **Ranking stages** — multi-phase cutover (cheap coarse ranking → expensive learned models) is built into the engine.
- **Marpa/HSWANN & HNSW** — ANN indexes with periodic dump/repair; [[concepts/hornet]] and Vespa's HNSW work are documented in the wiki.
- **Vespa Cloud** — hosted service; the open-source engine is fully self-hostable.

## Positioning vs. alternatives

| System | Strength | Weakness vs. Vespa |
|---|---|---|
| Elasticsearch | Ecosystem, lexical search | Tensor/ML ranking and large-scale ANN are bolt-ons |
| Dedicated vector DBs (Qdrant, Milvus) | Pure ANN simplicity | No lexical BM25, no in-engine ranking models |
| Lucene/Solr | Mature text search | Limited vector + tensor support |
| **Vespa** | Hybrid lexical+vector+tensors, real-time, multi-phase ranking | Steeper operational learning curve, heavier footprint |

Notable in wiki coverage: Doug Turnbull ([[entities/softwaredoug]], [[entities/doug-turnbull]]) has repeatedly analyzed Vespa's ranking/HNSW internals; [[entities/jo-kristian-bergum]] is Vespa's CEO; [[entities/sheshansh-agrawal]] worked on Vespa ranking.

## Related

- [[concepts/vector-databases]] — category context
- [[concepts/late-interaction-retrieval]] — ColBERT-style reranking in the search tier
- [[concepts/agentic-retrieval]] — agent-driven hybrid retrieval
- [[concepts/hornet]] — ANN index work in the Vespa ecosystem
- [[concepts/search-engines]] — broader IR landscape
- [[entities/softwaredoug]] — prominent Vespa/IR analyst
