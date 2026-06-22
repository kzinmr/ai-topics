---
title: "Massive Text Embedding Benchmark (MTEB)"
type: concept
aliases:
  - mteb
  - MTEB leaderboard
  - text embedding benchmark
created: 2026-06-15
updated: 2026-06-15
tags:
  - benchmark
  - model
  - evaluation
  - huggingface
  - search

---

# Massive Text Embedding Benchmark (MTEB)

The Massive Text Embedding Benchmark (MTEB) is a comprehensive benchmark for evaluating text embedding models. It provides a standardized leaderboard that compares embedding models across multiple tasks and domains.

## History

MTEB was originally developed as part of the Sentence Transformers ecosystem to provide rigorous, standardized evaluation of text embedding models. The benchmark covers multiple tasks including:

- Semantic Textual Similarity (STS)
- Information Retrieval
- Clustering
- Pair Classification
- Reranking
- Summarization

## v3 Leaderboard (June 2026)

In June 2026, a major update (v3) to the MTEB Leaderboard was released by Roman Solomatin, Kenneth Enevoldsen, Isaac Chung, and Tom Aarsen. Key improvements:

- **Performance**: Significantly faster than previous versions
- **Scalability**: Built on FastAPI and Svelte for better reliability
- **Customization**: Filtering by domain, language, modality, and individual tasks
- **Transparency**: Dataset inspection, zero-shot tracking, training data visibility
- **Model comparison**: Pin models for head-to-head analysis
- **API access**: Scores available via CSV download or API endpoint

The leaderboard is hosted at: https://huggingface.co/spaces/mteb/leaderboard

## Related Libraries

- **Sentence Transformers**: Python library for generating text embeddings, uses MTEB for evaluation
- **MTEB Python package**: Evaluation framework for running benchmarks on embedding models

## Related People

- **Tom Aarsen** -- MTEB maintainer, lead of Sentence Transformers at Hugging Face
- **Roman Solomatin** -- Led the v3 leaderboard development
- **Kenneth Enevoldsen** -- MTEB contributor
- **Isaac Chung** -- MTEB contributor

## Related Concepts

- [[embeddings]] -- Dense vector representations that MTEB evaluates
- [[semantic-search]] -- Primary use case for embedding models benchmarked by MTEB
- [[huggingface]] -- Host platform for the MTEB leaderboard
