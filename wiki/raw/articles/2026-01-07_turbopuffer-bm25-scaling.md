---
title: "BM25 Scaling Surprises: When More Terms Mean Lower Latency"
date: 2026-01-07
author: Adrien Grand (Engineer)
source_url: https://turbopuffer.com/blog/bm25-latency-musings
type: raw-article
tags: [turbopuffer, bm25, latency, scaling, full-text-search, power-law]
---

# BM25 Scaling Surprises: When More Terms Mean Lower Latency

Adrien Grand discovered a counterintuitive property of BM25 search: **adding more terms to a query can decrease latency**, because non-essential terms add less work than essential terms save through pruning.

> "For BM25 search, the relationship between query length and latency is not what most people expect."

## Essential vs Non-Essential Terms

In BM25, terms contribute to scoring with diminishing returns:

- **Essential terms** (high IDF, high max score): Drive candidate selection
- **Non-essential terms** (low IDF, low max score): Slightly refine scoring

When a query goes from 3 terms to 10 terms:
- The 3 essential terms might each require scanning many postings
- The 7 additional non-essential terms add minimal work because MAXSCORE skips their blocks
- **Net effect**: Latency can decrease because essential terms are more selective

## The Power Law of Query Scaling

turbopuffer modeled query latency scaling using a power law:

$$f(n) = C \cdot n^K$$

Where:
- **n** = number of query terms
- **K** = scaling exponent (K=1.0 is linear, K<1.0 is sublinear)
- **C** = constant factor

### Key Finding: Long Queries Scale More Linearly

| Query Length Range | K (Scaling Exponent) | Behavior |
|:---|:---:|:---:|
| Short (1-5 terms) | K = 0.35 | Highly sub-linear |
| Medium (5-20 terms) | K = 0.65 | Moderately sub-linear |
| Long (20-100+ terms) | K = 0.92 | Nearly linear |

**Why?** Essential terms hit diminishing returns — once you have 10+ essential terms, additional terms add proportional work because all essential terms are already being processed.

## top_k Scaling Model

Beyond term count, the **top_k parameter** also affects latency:

$$latency \propto top\_k \cdot \text{(number of essential terms)}$$

| top_k | Latency Scaling | Intuition |
|:---|:---:|:---|
| Small (top-10) | Sub-linear | Few candidates needed, pruning is very effective |
| Medium (top-100) | ~Linear | More candidates needed, more work |
| Large (top-1000) | Super-linear | Many candidates, pruning less effective |

## Test Environment

Benchmarks run on a **200M document corpus** from **Common Crawl**:

| Parameter | Value |
|:---|:---|
| **Index size** | ~52 GiB (FTS v2 format: ~5 GiB) |
| **Corpus** | 200M Common Crawl documents |
| **Vocabulary** | ~50M unique terms |
| **Query types** | Natural language, keyword, mixed |

## Practical Implications

1. **Don't fear long queries** — LLM-generated queries with 50+ terms don't cost 50x more than 1-term queries
2. **Query optimization is non-trivial** — adding useful terms can actually help
3. **Essential term detection** is critical for performance — turbopuffer's MAXSCORE implementation identifies essential terms via block-level max scores
4. **BM25 scaling is friendlier than dot-product similarity** — IDF naturally limits the impact of common terms

## Key Contributors

- Adrien Grand (Engineer) — discovery, modeling, benchmarking

## Related

- [[raw/articles/2026-01-14_turbopuffer-fts-v2-maxscore]] — Vectorized MAXSCORE
- [[raw/articles/2026-02-03_turbopuffer-fts-v2]] — FTS v2 overview
- [[raw/articles/2026-01-14_turbopuffer-fts-v2-postings]] — Inverted index design
