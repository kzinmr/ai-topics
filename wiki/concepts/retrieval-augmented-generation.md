---
title: "Retrieval-Augmented Generation (RAG)"
type: concept
created: 2026-04-25
updated: 2026-11-19
tags:
  - concept
  - rag
  - information-retrieval
  - grounding
  - embeddings
aliases:
  - RAG
  - retrieval-augmented-generation
sources:
  - raw/articles/2026-05-08_anthropic-engineering_contextual-retrieval.md
  - raw/articles/2026-08-01_glean_glean-information-retrieval.md
related:
  - "[[concepts/agentic-rag]]"
  - "[[concepts/agentic-retrieval]]"
status: active
---

# Retrieval-Augmented Generation (RAG)

**RAG** grounds an LLM's answer in externally retrieved documents: at query time, a retrieval system pulls relevant passages from a corpus (vector index, BM25, or hybrid) and injects them into the prompt, so the model answers from evidence instead of parametric memory. Introduced by Lewis et al. (2020), it became the default architecture for enterprise Q&A, chatbots over private corpora, and citation-bearing assistants.

## Canonical Pipeline

```
Offline:  docs → chunk → embed (embeddings model) → vector index
                                        └→ BM25 index (lexical)

Online:   query → (optional rewrite/expansion)
              → retrieve top-k (vector / BM25 / hybrid)
              → rerank (cross-encoder or LLM)
              → assemble prompt with citations
              → LLM generates grounded answer
```

Component choices and their pages:

| Stage | Options | Wiki |
|-------|---------|------|
| Chunking | fixed, semantic, structure-aware | chunking |
| Lexical retrieval | BM25, often beats dense for agents | [[concepts/bm25]], [[concepts/dense-retrieval]] |
| Dense retrieval | embedding ANN (HNSW) | [[concepts/vector-search]], [[concepts/vector-databases]] |
| Context enrichment | prepend document context per chunk | [[concepts/contextual-retrieval]] |
| Reranking | cross-encoders, ColBERT | neural reranking, late interaction |
| Evaluation | recall@k, nDCG, groundedness | [[concepts/evaluation/llm-evaluation-harness]], BEIR/MTEB |

## Why RAG (vs. alternatives)

- **Freshness & private data**: knowledge that post-dates training or lives behind ACLs.
- **Verifiability**: citations allow checking — the key enterprise requirement (grounding, factuality).
- **Cost**: retrieving beats fine-tuning for corpus-sized knowledge, and fine-tunes go stale.
- **Versus long context**: stuffing whole corpora into the window suffers context rot and cost ([[concepts/context-engineering/context-rot]], [[concepts/drowning-in-documents-paradox]]); retrieval selects what matters. The frontier is contested — see [[concepts/agentic-alternative-to-graphrag]] and file-system "search-as-code" approaches ([[concepts/search-as-code]]).

## Failure Modes

- **Retrieval misses**: right answer exists in corpus, never retrieved → measure recall separately from generation ([[concepts/evaluation/evals-vs-monitoring-debate]]).
- **Chunk amnesia**: decontextualized chunks lose "which company / from when" — fixed by contextual retrieval ([[concepts/contextual-retrieval]]).
- **Lost-in-the-middle / position effects**: top-k ordering matters ([[concepts/context-engineering/context-rot]]).
- **Sycophantic ungrounding**: model ignores provided context when parametric memory disagrees ([[concepts/sycophancy]]).
- **Query mismatch**: agent-written queries differ radically from human queries — BM25 often beats embedding retrievers for agent workloads ([[concepts/agentic-retrieval]]).

## Evolution: Naïve → Advanced → Agentic

The static retrieve-then-read pipeline has given way to agent-driven retrieval: the LLM decides *what* to retrieve, iterates, reformulates, and follows links — see [[concepts/agentic-rag]] (design patterns) and [[concepts/agentic-retrieval]] (workload characteristics: long structured queries, 20+ calls per task, cost implications). Deep research products are the extreme case: RAG as an iterative loop rather than a one-shot prefill.

## Related Concepts

- [[concepts/agentic-rag]] — agents orchestrate the retrieval pipeline
- [[concepts/agentic-retrieval]] — retrieval infrastructure for agent clients
- [[concepts/contextual-retrieval]] — Anthropic's chunk-context preprocessing
- [[concepts/knowledge-graph-memory-agents]] / [[concepts/agentic-alternative-to-graphrag]] — structured alternatives
- embeddings / [[concepts/vector-databases]] — substrate
- [[concepts/search-as-code]] — file-system-native retrieval for coding agents

## Sources

- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (NeurIPS 2020)
- Anthropic Engineering, "Contextual Retrieval" — `raw/articles/2026-05-08_anthropic-engineering_contextual-retrieval.md`
- Glean, "Information retrieval" overview — `raw/articles/2026-08-01_glean_glean-information-retrieval.md`
