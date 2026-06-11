---
title: "Contextual Retrieval"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - rag
  - model
  - search
  - anthropic
aliases:
  - Contextual Embeddings
  - Contextual BM25
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_contextual-retrieval.md
  - https://www.anthropic.com/engineering/contextual-retrieval
related:
  - rag-systems
  - retrieval-augmented-generation
  - context-engineering
---

# Contextual Retrieval

Contextual Retrieval is a preprocessing technique that dramatically improves retrieval accuracy in RAG systems. It appends the full document's context to each chunk **before** indexing them into embedding/BM25 indexes.

**Core idea**: Use Claude to auto-complete the context that is lost from standalone chunks ("which company's" data, "from when" data).

## Method

### Two Sub-Techniques

1. **Contextual Embeddings**: Prepend context to chunks before embedding
2. **Contextual BM25**: Create BM25 indexes with the same contextualized chunks

### Transformation Example

```
# Before
original_chunk = "The company's revenue grew by 3% over the previous quarter."

# After
contextualized_chunk = "This chunk is from an SEC filing on ACME corp's 
performance in Q2 2023; the previous quarter's revenue was $314 million. 
The company's revenue grew by 3% over the previous quarter."
```

### Context Generation Prompt

```xml
<document>{{WHOLE_DOCUMENT}}</document>
Here is the chunk we want to situate within the whole document
<chunk>{{CHUNK_CONTENT}}</chunk>
Please give a short succinct context to situate this chunk within the
overall document for the purposes of improving search retrieval of the chunk.
```

Generated context is typically 50-100 tokens. Processed with Claude 3 Haiku.

## Performance Improvement

| Method | Retrieval Failure Rate Reduction | Top-20 Failure Rate |
|------|--------------|-------------|
| Baseline (Standard RAG) | — | 5.7% |
| Contextual Embeddings Only | **-35%** | 3.7% |
| Contextual Embeddings + Contextual BM25 | **-49%** | 2.9% |
| + Reranking (Cohere) | **-67%** | 1.9% |

- **Improvement across all embedding models** (Gemini Text 004, Voyage especially effective)
- Validated across multiple domains (codebases, fiction, arXiv papers, scientific papers)

## Cost

With Prompt Caching, a **one-time cost of $1.02 per million document tokens** (assuming 800-token chunks, 8k-token documents, 50-token context instruction, 100-token context per chunk).

## Implementation Considerations

- **Chunk boundaries**: Choice of size, boundaries, and overlap affects retrieval performance
- **Embedding models**: Gemini and Voyage are particularly effective
- **Custom contextualization prompt**: Including domain-specific glossaries further improves results
- **Chunk count**: Top-20 is more effective than Top-10/Top-5 (but watch for information overload)
- **Reranking**: Involves a latency-cost tradeoff

## Comparison with Prior Methods

Anthropic also evaluated the following existing methods, but none were as effective as Contextual Retrieval:
- Appending document summaries to chunks → limited improvement
- Hypothetical Document Embedding (HyDE)
- Summary-based indexing

## See Also

- [[rag-systems]] — RAG systems overview
- [[retrieval-augmented-generation]] — RAG fundamentals
- [[concepts/context-engineering|Context Engineering]] — Context engineering for AI agents
- [[contextual-retrieval]] — (self)
