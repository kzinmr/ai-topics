---
source_tweet_id: "2039189127162380339"
source_author_id: "129969370"
source_created_at: "2026-04-01T03:52:28.000Z"
scraped_at: "2026-04-28T23:42:00Z"
title: "On Strengths and Limitations of Single-Vector Embeddings"
url: "https://arxiv.org/abs/2603.29519"
---

# On Strengths and Limitations of Single-Vector Embeddings

**Authors:** Archish S, Mihir Agarwal, Ankit Garg, Neeraj Kayal, Kirankumar Shiragur
**Date:** March 31, 2026
**Subject:** Information Retrieval (cs.IR)

## Executive Summary
This paper investigates why single-vector embedding models often fail in complex retrieval tasks, specifically referencing the LIMIT dataset. While previous research suggested that limited dimensionality was the primary bottleneck, this study argues that domain shift, task misalignment, and the "drowning in documents" paradox are the true drivers of performance degradation.

## Key Findings

### Challenging the Dimensionality Myth
- 2k+1-dimensional vector embeddings suffice for top-k retrieval (Alon et al., 2016)
- Dimensionality alone cannot explain observed failures
- Issue lies in how the space is utilized and how relevance is defined

### Primary Drivers of Failure
1. **Domain Shift:** Models struggle when target data distribution differs from training data
2. **Misalignment:** Disconnect between embedding's mathematical similarity and actual relevance
3. **Tokenization & Linguistics:** Secondary factors, modest gains when controlled

### The "Drowning in Documents" Paradox
- As corpus size grows, relevant documents are "drowned out"
- Embedding similarities act as noisy statistical proxies for relevance
- Single-vector models significantly more vulnerable to noise than multi-vector models

### Single-Vector vs Multi-Vector Comparison
| Feature | Single-Vector | Multi-Vector |
|---------|--------------|--------------|
| Retrieval Quality | Substantial drops on LIMIT | Stronger and more robust |
| Finetuning Impact | Catastrophic forgetting | Minimal forgetting |
| Scalability | Highly susceptible to drowning | Resilient to noise |
| Stability | MSMARCO drops >40% after finetuning | High stability |

## Conclusions
- Finetuning is a double-edged sword for single-vector models
- Architecture matters more than dimensionality size
- Developers should prioritize noise-resistant models for large corpora

