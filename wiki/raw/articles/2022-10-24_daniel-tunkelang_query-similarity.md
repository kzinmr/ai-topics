---
title: "Query Similarity"
author: Daniel Tunkelang
source: https://queryunderstanding.com/query-similarity-49dde9f78043
date: 2022-10-24
publication: Query Understanding (Medium)
tags:
  - query-understanding
  - query-similarity
  - embeddings
  - search
  - information-retrieval
---

# Query Similarity

> "A query is an expression of an information-seeking intent. A search engine's first job is to infer searchers' intents from their queries — that's the whole point of query understanding!"

## Superficial Query Variation

Easily recognizable differences that rarely change intent:
- **Stemming/Lemmatization**: singular vs. plural (cat video vs. cat videos)
- **Word order**: shoes nike = nike shoes (exceptions handled by query segmentation)
- **Stop words**: shoes men ≈ shoes for men
- **Tokenization**: twenty one / twenty-one / twentyone
- **Spelling**: louie vitton purse → Louis Vuitton purse

## Semantic Query Variation

Deeper, context-dependent equivalences:
- **Synonyms**: couch ≈ sofa (but context matters: bifocal glasses vs. wine glasses)
- **Redundancy**: ipad pro already implies apple
- **Paraphrasing**: coffee mug ≈ 12 oz mug; pixel charging cable ≈ usb c to usb c cable

## Measuring Query Similarity

### Method 1: Direct Query Vector Embedding
Use sentence embedding models (HuggingFace Sentence Transformers). Problem: pre-trained models often underperform unless domain-matched. Better: train/fine-tune, but requires labeled query pairs.

### Method 2: Bag of Documents (Post-Search Behavior)
1. Map documents to vectors (pre-trained model)
2. Aggregate (mean) vectors of documents users engaged with for each query
3. Measure cosine similarity between aggregated query vectors
- Works for head and torso queries (sufficient history)
- Provides labeled training data for tail queries

### Extending to Tail Queries
Use head/torso query vectors as labeled training data to train/fine-tune a sentence transformer for online query vectorization.

## Summary

Superficial variation (stemming, word order, stop words, tokenization, spelling) is easy to recognize. Semantic variation (synonyms, redundancy, paraphrasing) requires learning from post-search behavior via embedding vectors.
