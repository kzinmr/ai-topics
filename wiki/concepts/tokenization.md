---
title: "Tokenization"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - concept
  - tokenization
sources:
  - wiki/concepts/semantic-ids
---

# Tokenization

**Tokenization** is the process of converting text into discrete tokens — subword units that serve as the basic input units for language models. Common tokenization algorithms include BPE (Byte-Pair Encoding), WordPiece, and SentencePiece. Tokenization determines vocabulary size, affects model efficiency, and influences how models handle rare words, multilingual text, and code.

## Related
- [[concepts/tokenizer-objective-vs-search]] — What actually makes a good tokenizer: objective (log-likelihood) dominates over search procedure (BPE vs UnigramLM)
- [[concepts/dense-retrieval]] — Tokenizer output feeds embedding models
- [[concepts/semantic-ids]] — Semantic IDs as a form of discrete tokenization for retrieval
- [[concepts/information-retrieval]] — How tokenization affects IR pipelines
