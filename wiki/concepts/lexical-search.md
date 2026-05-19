---
title: Lexical Search
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - search
  - lexical-search
  - tokenization
  - bm25
sources: [raw/articles/2026-05-13_softwaredoug_lexical-search-bm25.md]
---

# Lexical Search

Lexical search is the foundational approach to information retrieval where documents are matched to queries through **token-based matching** against an inverted index. Unlike [[embeddings|semantic search]] which relies on vector similarity, lexical search depends entirely on the quality of tokenization — it only finds what the tokenizer can represent.

> "Only as smart as your tokenizer." — Doug Turnbull

## Core Pipeline

```
Documents → Tokenizer → Inverted Index → Query Tokenization → Match & Score
```

1. **Tokenization**: Documents are broken into tokens (words, n-grams) by a tokenizer
2. **Indexing**: An inverted index maps each token to the documents containing it
3. **Query Processing**: The search query is tokenized using the same tokenizer
4. **Matching**: Query tokens are looked up in the inverted index to find candidate documents
5. **Scoring**: Matching documents are ranked using a scoring function (typically [[bm25|BM25]])

## Tokenization

Tokenization is the most critical component — it defines what constitutes a "match." The tokenizer must be applied consistently to both documents and queries.

**Naive whitespace tokenizer** fails with punctuation:
```python
whitespace_tokenize("Doug, can we help you?")
# ['Doug,', 'can', 'we', 'help', 'you?'] — punctuation attached!

# Query "Doug complaint" won't match — "Doug," ≠ "Doug"
```

**Better tokenizer** handles lowercase + punctuation stripping:
```python
def better_tokenize(text):
   lowercased = text.lower()
   without_punctuation = lowercased.translate(str.maketrans('', '', punctuation))
   return without_punctuation.split()
```

**Advanced tokenization considerations:**
- Stemming to root forms (e.g., "running" → "run")
- Synonym expansion (e.g., "car" ↔ "automobile")
- Entity recognition (e.g., "New York" as single token)
- Multi-lingual normalization

## Query Processing

### Match Operators

**AND** — all query terms must appear in the document:
```python
matches = np.ones(len(docs), dtype=np.bool)
for token in query_tokens:
    matches &= (index.score(token) > 0)
```

**OR** — at least one query term must appear:
```python
matches = np.zeros(len(docs), dtype=np.bool)
for token in query_tokens:
    matches |= (index.score(token) > 0)
```

### Query DSLs

Production search engines (Elasticsearch, Solr, OpenSearch) expose complex query DSLs that map to token-level matching logic:

```json
{
  "query": {
    "multi_match": {
      "query": "leather pants",
      "fields": ["title", "description", "category"],
      "operator": "or"
    }
  }
}
```

Understanding how the DSL translates to token matching across fields is essential for tuning search relevance.

## Multi-field Search

Real search applications involve multiple fields (title, description, body, tags). Two strategies:

### Naive Sum (across fields)
```python
# Accumulates scores across all fields — biases toward docs matching in multiple fields
field_scores += score
```

### DisMax (term-centric)
```python
# Takes the MAXIMUM score per term across fields — avoids multi-field bias
field_scores = np.maximum(field_scores, score)
```

DisMax ("**Dis**junction **Max**imum") is the standard approach in Elasticsearch, Solr, and OpenSearch. It's also known as "term-centric" search: each query term independently selects the best-matching field.

## Lexical vs. Semantic Search

| Dimension | Lexical Search | Semantic Search (Embeddings) |
|-----------|---------------|------------------------------|
| Matching | Exact token match | Vector similarity |
| Precision | High (exact matches) | Variable (semantic neighbors) |
| Recall | Low (misses synonyms) | High (finds related concepts) |
| Speed | Very fast (inverted index) | Moderate (ANN) |
| Interpretability | High (why this matched) | Low (black-box similarity) |
| Infrastructure | Simple (Lucene, Solr) | Complex (vector DB, GPU) |

## Relationship to BM25

Lexical search provides the **match** — BM25 provides the **score**. The two are inseparable in practice: lexical matching identifies candidate documents, and [[bm25|BM25]] ranks them by relevance.

> "BM25 ≈ Relevance Given Match" — BM25 answers "how much is this passage *about* that match?"

## Lexical Search in the Agent Era

Doug Turnbull argues that with the rise of AI agents, lexical search gains new importance:

- **Dumb retrievers, smart agents**: Agents handle semantic understanding; BM25/lexical search provides precise, fast term-based retrieval as a tool
- **"RAG isn't a vector search problem"**: The embedding-centric view of RAG is the wrong lens — lexical search with agent reasoning is often more effective
- **Agentic search**: LLM agents using lexical search as one tool among many, orchestrating multi-step retrieval with evaluation feedback loops

## Related Pages

- [[bm25]] — Scoring algorithm built on lexical search
- [[embeddings]] — Semantic alternative to lexical matching
- [[entities/doug-turnbull]] — Leading voice in agentic search
- [[entities/daniel-tunkelang]] — Search relevance pioneer
- [[concepts/rag]] — Retrieval-Augmented Generation
