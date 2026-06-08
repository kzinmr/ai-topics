---
title: "Semantic IDs for Generative Search and Recommendation"
url: https://research.atspotify.com/2025/9/semantic-ids-for-generative-search-and-recommendation
date_published: 2025-09-18
date_ingested: 2026-06-08
source: spotify-research
authors:
  - Gustavo Penha
  - Edoardo D'Amico
  - Marco De Nadai
  - Enrico Palumbo
  - Alexandre Tamborrino
  - Ali Vardasbi
  - Max Lefarov
  - Shawn Lin
  - Timothy Heath
  - Francesco Fabbri
  - Hugues Bouchard
venue: "RecSys 2025, Late Breaking Results"
tags:
  - semantic-ids
  - generative-retrieval
  - information-retrieval
  - embeddings
  - llm
  - search-ranking
  - dense-retrieval
  - spotify
  - recsys-2025
---

# Semantic IDs for Generative Search and Recommendation

**Source:** [Spotify Research Blog](https://research.atspotify.com/2025/9/semantic-ids-for-generative-search-and-recommendation)
**Paper:** [Semantic IDs for Joint Generative Search and Recommendation](https://research.atspotify.com/publications/semantic-IDs-for-joint-generative-search-and-recommendation) — RecSys 2025, Late Breaking Results

## Summary

Large Language Model (LLM)-based generative frameworks are transforming search and recommendation. A central challenge is how to represent items as discrete tokens that LLMs can process. Traditional approaches (unique IDs, sequential IDs, item titles) face limitations in scalability and cold-start handling.

**Semantic IDs** tokenize items based on their embeddings, allowing similar items to share tokens and promoting better generalization. However, the effectiveness depends strongly on the underlying embedding space: search-fine-tuned embeddings enhance retrieval, while recommendation-tuned embeddings yield better recommendation quality.

## Key Findings

### Task-specific Semantic IDs fail to generalize

Three embedding approaches were evaluated in a joint generative Search & Recommendation (S&R) model on MovieLens-25M:

- **Content-based embeddings** (as in DSI [1], TIGER [2])
- **Search-tuned embeddings** (as in RIPOR [3])
- **Recommendation-tuned embeddings** (as in TokenRec [4])

Results show that Semantic IDs tuned for search significantly improve retrieval but degrade recommendation performance, and vice versa — a fundamental tension when unifying both tasks.

### Multi-task Bi-encoder Approach

To capture both tasks in a single set of Semantic IDs, the authors propose fine-tuning a bi-encoder model jointly for search and recommendation via contrastive learning:

- **Query–item pairs** from the search dataset
- **Co-occurring item–item pairs** from the recommendation dataset

The resulting embeddings are clustered and discretized with **RQ-KMeans** to form Semantic IDs.

### Comparison Methods

- **Separate**: Each task has its own set of Semantic ID tokens
- **Fused SVD**: Embeddings reduced to common dimensionality and concatenated
- **Multi-task**: Joint bi-encoder fine-tuning (proposed)

### Results

The Multi-task approach lies on the **Pareto frontier** — no other cross-task method improves one task without reducing the other. However, a performance gap remains compared to task-specific Semantic IDs optimized for a single task.

## Related Work

- **DSI** (Tay et al., NeurIPS 2022) — Transformer memory as a differentiable search index
- **TIGER** (Rajput et al., NeurIPS 2023) — Recommender systems with generative retrieval
- **RIPOR** (Zeng et al., The WebConf 2024) — Scalable and effective generative information retrieval
- **TokenRec** (Qu et al., arXiv:2406.10450) — Learning to tokenize ID for LLM-based generative recommendation
- **Bridging Search and Recommendation** (Penha et al., RecSys 2024) — Prior work examining joint training benefits with atomic IDs

## Authors

Gustavo Penha, Edoardo D'Amico, Marco De Nadai, Enrico Palumbo, Alexandre Tamborrino, Ali Vardasbi, Max Lefarov, Shawn Lin, Timothy Heath, Francesco Fabbri, Hugues Bouchard — Spotify Research
