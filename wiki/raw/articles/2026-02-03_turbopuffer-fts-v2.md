---
title: "FTS v2: 20x Faster Full-Text Search on Object Storage"
date: 2026-02-03
authors: [Adrien Grand, Morgan Gallant, Nikhil Benesch]
source_url: https://turbopuffer.com/blog/fts-v2
type: raw-article
tags: [turbopuffer, full-text-search, bm25, inverted-index, maxscore, tokenizer, lsm-tree]
---

# FTS v2: 20x Faster Full-Text Search on Object Storage

turbopuffer's second-generation full-text search engine delivers **20x faster search** and **10x smaller inverted indexes** through fixed-size block partitioning, MAXSCORE dynamic pruning, and a redesigned tokenizer.

> "FTS v2 is the biggest leap in search performance since turbopuffer launched. We made indexes 10x smaller and search 20x faster."

## Key Improvements

| Metric | FTS v1 | FTS v2 | Improvement |
|:---|:---:|:---:|:---:|
| **Index size (MSMARCO)** | 51.6 GiB | 5.22 GiB | 9.9x smaller |
| **Search latency** | baseline | 20x faster | 20x |
| **Inverted index structure** | Cluster-based | Fixed-size block | — |
| **Pruning algorithm** | WAND | MAXSCORE | — |
| **Tokenizer** | standard | word_v3 | — |

## Architecture

### Fixed-Size Block Partitioning

Instead of clustering postings by document clusters (v1), FTS v2 partitions the inverted index into **fixed-size blocks** of ~256 postings each:

```
FTS v1 (Cluster-based):
  ┌─────────────────────┐
  │ Term: "database"    │
  │ Block: docs 1-100   │  ← variable size, cluster-based
  │ Block: docs 101-250 │
  │ Block: docs 251-500 │
  └─────────────────────┘

FTS v2 (Fixed-size block):
  ┌─────────────────────┐
  │ Term: "database"    │
  │ Block: 256 postings │  ← always ~256 postings
  │ Block: 256 postings │
  │ Block: 256 postings │
  └─────────────────────┘
```

**Why N=256?** Three factors balanced:
1. **Compression efficiency**: Block size must be large enough for effective delta encoding + bitpacking
2. **Skip performance**: Block skip granularity — smaller blocks = more precise skipping, but more overhead
3. **Overhead balance**: Metadata per block (document ID range, max scores, block stats)

### KV-Store Inverted Index on LSM+S3

The inverted index is built on top of turbopuffer's custom LSM tree on object storage:

- **Key**: `(term, block_id)` — each block is a KV pair
- **Value**: Bitpacked posting list (document IDs, term frequencies, positions)
- **LSM levels**: Written to L0→L1→L2, eventually compacted into S3-resident SSTables
- **Cache-friendly**: Block size optimized for NVMe SSD page size (4KB)

## MAXSCORE Dynamic Pruning

FTS v2 replaces WAND (Weak-and) with MAXSCORE for query evaluation:

- **Term-centric evaluation**: Find candidates from essential terms, score with all terms
- **Upper bound per block**: Each block stores max contribution score for its term
- **Dynamic pruning**: Skip blocks whose max contribution < current top-K threshold
- **Efficient for long queries**: Especially beneficial for LLM-generated queries with many terms

See [[raw/articles/2026-01-14_turbopuffer-fts-v2-maxscore]] for detailed comparison.

## word_v3 Tokenizer

New tokenizer improvements:

- **Unicode normalization**: NFKC normalization
- **Number handling**: Improved tokenization of numbers and mixed alphanumeric
- **Case folding**: locale-aware
- **Substring matching**: prefix queries through efficient index structure

## Additional Features

- **Rank-by-filter**: Scoring is computed only for documents that match the filter
- **Prefix queries**: Efficient prefix search using the block index
- **Regex filtering**: Regular expression filtering on indexed fields
- **Performance**: All new features designed for object storage access patterns

## Key Contributors

- Adrien Grand (Engineer) — MAXSCORE, BM25 optimizations
- Morgan Gallant (Engineer) — fixed-size block design, tokenizer
- Nikhil Benesch (Engineer) — LSM integration, infrastructure

## Related

- [[raw/articles/2026-01-14_turbopuffer-fts-v2-postings]] — Deep dive on inverted index design
- [[raw/articles/2026-01-14_turbopuffer-fts-v2-maxscore]] — Vectorized MAXSCORE vs WAND
- [[raw/articles/2026-01-07_turbopuffer-bm25-scaling]] — BM25 scaling surprises
