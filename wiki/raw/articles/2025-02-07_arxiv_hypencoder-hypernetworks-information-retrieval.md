---
title: "Hypencoder: Hypernetworks for Information Retrieval"
type: raw-article
source_url: https://arxiv.org/abs/2502.05364
authors:
  - Julian Killingback
  - Hansi Zeng
  - Hamed Zamani
affiliation: University of Massachusetts Amherst
published: 2025-02-07
revised: 2025-05-01
venue: SIGIR 2025
tags:
  - information-retrieval
  - neural-ranking
  - hypernetworks
  - dense-retrieval
  - bi-encoder
---

# Hypencoder: Hypernetworks for Information Retrieval

**arXiv:** https://arxiv.org/abs/2502.05364
**PDF:** https://arxiv.org/pdf/2502.05364
**Code:** https://github.com/jfkback/hypencoder-paper

## Abstract

Existing information retrieval systems are largely constrained by their reliance on vector inner products to assess query-document relevance, which naturally limits the expressiveness of the relevance score they can produce. We propose a new paradigm; instead of representing a query as a vector, we use a small neural network that acts as a learned query-specific relevance function. This small neural network takes a document representation as input (in this work we use a single vector) and produces a scalar relevance score. To produce the small neural network we use a hypernetwork, a network that produces the weights of other networks, as our query encoder. We name this category of encoder models Hypencoders. Experiments on in-domain search tasks show that Hypencoders significantly outperform strong dense retrieval models and even surpass reranking models and retrieval models with an order of magnitude more parameters. To assess the extent of Hypencoders' capabilities, we evaluate on a set of hard retrieval tasks including tip-of-the-tongue and instruction-following retrieval tasks. On harder tasks, we find that the performance gap widens substantially compared to standard retrieval tasks. Furthermore, to demonstrate the practicality of our method, we implement an approximate search algorithm and show that our model is able to retrieve from a corpus of 8.8M documents in under 60 milliseconds.

## Key Contributions

1. **Theoretical proof** that inner product similarity functions fundamentally limit the types of relevance retrieval models can express
2. **Hypencoder framework** — uses a hypernetwork to generate query-specific neural network weights as a relevance function
3. **Graph-based approximate search algorithm** for efficient retrieval at scale
4. **State-of-the-art results** on MSMARCO, TREC DL, DL-Hard, TREC TOT, and FollowIR benchmarks
5. **Open-sourced** training, retrieval, and evaluation code

## Architecture

### Three Paradigms Compared

- **Bi-encoder (dense retrieval):** Query → vector, Document → vector, Score = inner product
- **Cross-encoder (reranking):** Concatenate (query, doc) → transformer → scalar score (slow, cannot precompute)
- **Hypencoder:** Query → hypernetwork → small neural network (q-net), Document → vector, Score = q-net(document_vector)

### Hyperhead Layers

- Attention-based layers that produce weight and bias matrices for q-net
- Query embeddings E_q are concatenated with a column of ones (to model bias)
- Learnable key/value parameters θ_K, θ_V project query embeddings to weight space
- Single-head scaled-dot-product attention with learnable query matrix Q_i
- ReLU activation + layer normalization + point-wise feed-forward
- Base weights θ_H allow learning query-independent universal patterns

### q-net

- Simple feed-forward architecture with residual connections
- Takes document vector (768-dim from BERT [CLS]) as input
- Produces scalar relevance score
- Layer depth is a configurable hyperparameter

### Training

- Same as bi-encoder training (query encoder + document encoder)
- Uses distillation training setup
- Novel contributions are architectural, not training-technique specific

### Efficient Retrieval

- Graph-based greedy search on document-to-document neighbor graph
- Documents are nodes connected by L2 distance edges
- Algorithm: start with random candidates → score with q-net → explore neighbors of top candidates → repeat
- Complexity: O(|C_initial| + nCandidates × maxIter) — not tied to corpus size
- 8.8M documents in ~60ms on single NVIDIA L40S GPU

## Results

### In-Domain (MSMARCO, TREC DL '19/'20)

- Significantly outperforms strong bi-encoders (TAS-B, CL-DRD, ANCE)
- Surpasses reranking models (MonoBERT, cross-SimLM)
- Outperforms RepLLaMA (7B params, 60x larger) on TREC DL
- Only ColBERTv2 (multi-vector) beats it in nDCG@10

### Out-of-Domain (BEIR: TREC COVID, NFCorpus, FiQA, DBPedia, Touché)

- Strong zero-shot generalization in Q&A and entity retrieval
- Demonstrates that complex similarity function does not hurt generalization

### Hard Retrieval Tasks

- TREC DL-Hard, TREC Tip-of-the-Tongue (TOT), FollowIR
- Performance gap widens on harder tasks compared to standard retrieval
- Only model to achieve positive p-MRR on FollowIR (instruction-following retrieval)

### Efficiency

- Exhaustive search: high latency
- Efficient 1 (speed-optimized): C=10K, nCandidates=64, maxIter=16
- Efficient 2 (quality-optimized): C=100K, nCandidates=328, maxIter=20
- Both achieve significant speedup over exhaustive with minimal quality loss

## Authors

- **Julian Killingback** — UMass Amherst, co-author with Zamani group
- **Hansi Zeng** — UMass Amherst, IR researcher (also co-authored scaling sparse/dense retrieval in decoder-only LLMs)
- **Hamed Zamani** — UMass Amherst, IR professor, leads the lab
