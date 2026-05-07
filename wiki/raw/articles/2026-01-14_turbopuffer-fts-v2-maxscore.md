---
title: "Vectorized MAXSCORE over WAND: Why turbopuffer Chose Dynamic Pruning"
date: 2026-01-14
authors: [Adrien Grand, Morgan Gallant]
source_url: https://turbopuffer.com/blog/fts-v2-maxscore
type: raw-article
tags: [turbopuffer, full-text-search, maxscore, wand, dynamic-pruning, bm25, vectorized]
---

# Vectorized MAXSCORE over WAND: Why turbopuffer Chose Dynamic Pruning

turbopuffer chose **MAXSCORE** over **WAND** (Weak-AND) for query-time dynamic pruning in FTS v2. The decision was driven by the shift toward long, LLM-generated queries where WAND's overhead per document becomes a bottleneck.

> "For long queries with many terms, MAXSCORE is strictly better than WAND. The essential terms find candidates, and all terms score them."

## Term-Centric vs Document-Centric

### WAND (Document-Centric)
- Iterates through documents, maintaining a pivot
- For each document: checks if top essential terms can beat current threshold
- **Advantage**: Can skip documents that can't possibly make the top-K
- **Disadvantage**: High overhead per document — pivot maintenance, term ordering checks

### MAXSCORE (Term-Centric)
- Processes posting lists one block at a time
- **Essential terms**: Terms with high max scores — iterated fully to find candidates
- **Non-essential terms**: Terms with low max scores — only processed for candidate documents
- **Advantage**: Lower overhead per document, better memory locality

```
WAND:
  For each doc in pivot:
    Check if doc can beat threshold using essential terms
    If yes: score fully
    If no: skip

MAXSCORE:
  For each essential term block:
    Add all docs in block to candidate set
  For each candidate doc:
    Score using all terms (essential + non-essential)
```

## Why MAXSCORE Wins for Long Queries

Long queries (10-100+ terms, common with LLM-generated queries) have:
- **Many low-importance terms** (non-essential)
- **Few high-impact terms** (essential)
- **High WAND pivot overhead**: Per-document checks scale with query length

### Block-Max Variants

Both WAND and MAXSCORE have **block-max variants** that use precomputed block-level max scores:

- **Block-Max WAND**: Uses block max scores to skip blocks instead of individual postings
- **Block-Max MAXSCORE** (used by turbopuffer): Uses fixed-size block boundaries as the skip unit

## turbopuffer's Batching Approach

turbopuffer's implementation uses the **fixed-size block architecture** from FTS v2 to enable efficient MAXSCORE:

1. **Block-level max scores** stored per block (~256 postings)
2. **Block-at-a-time iteration** from posting iterators
3. **Memory locality**: Processing 256 postings at a time fits in L1 cache
4. **SIMD-friendly**: Bitpacked block can be decoded and processed with SIMD instructions

```
Performance comparison on 200M document corpus:
                        WAND (block)    MAXSCORE (block)
Short queries (3 terms):  1.0x (base)    0.95x (slightly slower)
Medium queries (10 terms): 1.0x           1.3x (30% faster)
Long queries (50+ terms):  1.0x           2.5x (150% faster)
```

## Key Insights

1. **LLM queries changed the workload** — longer queries make MAXSCORE increasingly advantageous
2. **Block-at-a-time processing** is essential for both algorithms on object storage
3. **Memory locality** in turbopuffer's batching approach benefits MAXSCORE more than WAND
4. **Fixed-size blocks** enable both algorithms, but MAXSCORE derives more benefit from the structure

## Key Contributors

- Adrien Grand (Engineer) — MAXSCORE implementation, benchmark analysis
- Morgan Gallant (Engineer) — block architecture integration

## Related

- [[raw/articles/2026-02-03_turbopuffer-fts-v2]] — FTS v2 overview
- [[raw/articles/2026-01-14_turbopuffer-fts-v2-postings]] — Inverted index design
- [[raw/articles/2026-01-07_turbopuffer-bm25-scaling]] — BM25 scaling model
