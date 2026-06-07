---
title: "turbopuffer"
tags:
  - entity
  - service
  - vector-search
  - search
  - protocol
created: 2026-05-07
updated: 2026-06-03
team:
  - name: Simon Hørup Eskildsen
    role: Co-founder & CEO
    background: Former Shopify
  - name: Justine
    role: Co-founder & CTO
    background: Former Shopify
  - name: Nathan VanBenschoten
    role: Chief Architect
    focus: Vector search, SPFresh, RaBitQ, ANN v3
  - name: Adrien Grand
    role: Engineer
    focus: BM25, MAXSCORE, full-text search
  - name: Morgan Gallant
    role: Engineer
    focus: Full-text search, inverted indexes, recall monitoring
  - name: Nikhil Benesch
    role: Engineer
    focus: LSM tree, infrastructure
  - name: Xavier Denis
    role: Engineer
    focus: Rust performance, SIMD optimization
  - name: Bojan Serafimov
    role: Engineer
    focus: Native filtered vector search
type: entity
related:
  - concepts/zero-disk-architecture
  - concepts/object-storage-queue
  - concepts/turbopuffer-rank-by-attribute
  - concepts/absurd-durable-execution
---

# turbopuffer

## Overview

**turbopuffer** is a vector search + full-text search engine built with object storage (S3/GCS/Azure Blob) as the sole persistence layer. Unlike traditional vector databases, the primary data store is object storage, with SSD/RAM functioning only as cache. This "Object-Storage-Native" architecture achieves **6–100x cost reduction** compared to traditional approaches and 99.99% uptime.

**Official site:** https://turbopuffer.com/
**GitHub:** None (proprietary)

---

## Product Details

### Basic Specifications

| Item | Value |
|:---|:---|
| **Type** | Managed search engine (Vector + BM25 Full-Text Search + Aggregation) |
| **Primary Storage** | S3 / GCS / Azure Blob (Source of Truth) |
| **Cache** | NVMe SSD + Memory hierarchical cache |
| **Vector Index** | SPFresh (centroid-based ANN) — v3 adds RaBitQ quantization + AVX-512 support |
| **Full-Text Search Index** | Custom LSM Tree on Object Storage |
| **API** | REST (JSON) |
| **License** | Proprietary (managed service) |
| **Founded** | Unknown (~2024?) |

### Performance (v1 Benchmark)

| Scenario | Latency |
|:---|:---|
| Cold Query (1M vectors, 3GB) | 444ms p90 |
| Warm Query (same) | **10ms** p90 |
| Cold Query (1M docs BM25, 300MB) | 285ms p90 |
| Warm Query (same) | **18ms** p90 |
| WAL write (500kB) | 285ms p50 |

### Performance (ANN v3 — May 2026)

| Configuration | Latency (p99) | Recall@10 | QPS/Node |
|:---|:---:|:---:|:---:|
| **100B vectors, ANN v3** | **200ms** | >90% | ~100K |
| 10B vectors, ANN v3 | ~50ms | >95% | ~100K |
| 1B vectors, ANN v3 | ~20ms | >97% | ~100K |
| 1M vectors (v1 baseline) | ~10ms (warm) | Baseline | ~1K |

**ANN v3 Technical Innovations:**
- **RaBitQ Binary Quantization**: 768-dimensional f32 vectors compressed 16-32x, distance computation converted to XOR+popcount
- **AVX-512 VPOPCNTDQ**: 512 comparisons per cycle, 32x compute density vs f32 dot product
- **SPFresh Hierarchical Clustering**: 100x branching factor hierarchical clustering
- **Random Sharding**: Linear scaling across storage-optimized VMs

### Native Filtering

Introduced January 2025. Natively integrates filtering into SPFresh clustering-based indexes.

| Method | Recall with Filter | Latency | Scalability |
|:---|:---:|:---:|:---:|
| **Pre-filter** | 100% | O(n) — Slow | Poor |
| **Post-filter** | 0-60% (selectivity-dependent) | Fast | Good |
| **Native (turbopuffer)** | **>90%** | **Fast** | **Good** |

**Two-Layer Index:**
1. **Cluster level**: `(attribute_value, cluster_id)` → bitmap — fast bitmap operations
2. **Row level**: `(cluster_id, vector_id)` → vector — ANN within filter-passing clusters only

### Continuous Recall Measurement

Introduced September 2024. **Samples 1% of real production queries** to continuously monitor recall@10.

- **Target**: 90-95% recall@10
- **Detection**: Detects index degradation within minutes
- **Claim**: First search engine to implement continuous recall monitoring in a real production environment

### Cost Comparison (per TB/month)

| Architecture | Cost |
|:---|:---:|
| RAM + 3x SSD (traditional) | $3,600 |
| 3x SSD only | $600 |
| **turbopuffer (S3 + SSD Cache)** | **$70** |
| Raw S3 | $20 |

---

## Architecture

### Object-Storage-Native LSM

![turbopuffer architecture diagram showing client → API → Memory/SSD Cache → Object Storage (S3)](/docs/architecture)

- **All persistent state lives on object storage** — compute nodes are fully stateless
- **WAL (Write-Ahead Log)** — Writes are first appended to WAL, then asynchronously merged into the LSM Tree. WAL also lives on object storage
- **LSM Tree on S3** — While most implementations are designed for local disk, turbopuffer built a custom LSM implementation that operates on S3 from the ground up
- **Query Planning** — Limits round trips to object storage to a maximum of 3
- **SPFresh** — Centroid-based approximate nearest neighbor search. More compatible with object storage than graph-based approaches (HNSW/DiskANN). Minimizes round trips and write amplification

### Cache Hierarchy (Pufferfish Effect)

```
Cold (Object Storage)  →  Warm (NVMe SSD)  →  Hot (RAM)
      ~500ms                  ~tens of ms           <10ms
```

"Pufferfish Effect" — The more data is searched, the more it inflates up into the cache, becoming faster. Unused data stays in cold storage, compressing costs.

### Consistency Model

| Mode | Latency | Characteristics |
|:---|:---|:---|
| **Strong Consistency (default)** | ~10ms floor | GET IF-NOT-MATCH confirms latest. Readable immediately after write |
| **Eventual Consistency** | <10ms | Cache only. Old data may be visible for a period after writes |

---

## Timeline

| Date | Event |
|:---|:---|
| 2024-09-04 | Morgan Gallant publishes "Continuous Recall Measurement" — introduces recall@10 continuous measurement via 1% query sampling in production ([[raw/articles/2024-09-04_turbopuffer-continuous-recall]]) |
| 2025-01-21 | Bojan Serafimov publishes "Native Filtering" — SPFresh clustering-based filtering method ([[raw/articles/2025-01-21_turbopuffer-native-filtering]]) |
| 2025-09 | Jason Liu publishes architecture deep-dive "TurboPuffer: Object Storage-First Vector Database Architecture" |
| 2025-11 | turbopuffer product launch — S3/GCS-native search engine |
| 2026-01-07 | Adrien Grand publishes "BM25 Scaling Surprises" — power-law model of query length vs latency ([[raw/articles/2026-01-07_turbopuffer-bm25-scaling]]) |
| 2026-01-14 | Morgan Gallant & Adrien Grand publish "FTS v2 Postings" — 9.9x index compression via fixed-size block partitioning ([[raw/articles/2026-01-14_turbopuffer-fts-v2-postings]]) |
| 2026-01-14 | Adrien Grand & Morgan Gallant publish "Vectorized MAXSCORE over WAND" — rationale for migrating to MAXSCORE dynamic pruning ([[raw/articles/2026-01-14_turbopuffer-fts-v2-maxscore]]) |
| 2026-02-03 | Adrien Grand, Morgan Gallant & Nikhil Benesch announce "FTS v2" — 20x faster full-text search, 10x smaller inverted index ([[raw/articles/2026-02-03_turbopuffer-fts-v2]]) |
| 2026-03-05 | Official blog published — "turbopuffer: fast search on object storage" detailing architecture and cost benefits |
| 2026-03-08 | Xavier Denis publishes "Rust Zero-Cost Abstractions vs SIMD" — 220ms→47ms speedup via batch iterators ([[raw/articles/2026-03-08_turbopuffer-rust-zero-cost-simd]]) |
| 2026-04 | Rank by Attribute feature released (Adrien Grand) — combined BM25 + numeric attribute ranking ([[concepts/turbopuffer-rank-by-attribute]]) |
| 2026-05-05 | Nathan VanBenschoten publishes "ANN v3" — 100B vector 200ms p99 search via RaBitQ quantization + AVX-512 VPOPCNTDQ ([[raw/articles/2026-05-05_turbopuffer-ann-v3]]) |
| 2026-05-07 | Object Storage Queue blog published — case study of rebuilding their indexing queue on object storage ([[concepts/object-storage-queue]]) |

---

## Full-Text Search (FTS v2)

turbopuffer released **FTS v2** in February 2026, achieving 20x faster full-text search and 10x smaller inverted indexes.

### Fixed-Size Block Partitioning

v1 used variable-size blocks partitioned by document clusters, but v2 uses **~256 posting fixed-size blocks**.

| Method | Block Size | Compression Ratio | Skip Precision |
|:---|:---:|:---:|:---:|
| **v1 (cluster-based)** | Variable (42–1,204) | Low | Poor |
| **v2 (fixed-size)** | ~256 | High (9.9x reduction) | Good |

**Why N=256:**
1. **Compression efficiency**: Sufficient density for delta encoding + bit packing
2. **Skip performance**: Optimal as the minimum unit for MAXSCORE pruning
3. **Overhead balance**: Block metadata (~32B) amounts to 1.6%

### MAXSCORE Dynamic Pruning

Migrated from WAND (Weak-AND) to **MAXSCORE**. Particularly effective for LLM-generated queries (long text, many tokens).

| Algorithm | Approach | Long Query (50+ tokens) Performance |
|:---|:---|:---:|
| **WAND** | Document-centric (high pivot management overhead) | 1.0x (baseline) |
| **Block-MAXSCORE** | Term-centric (required terms find candidates, all terms score) | **2.5x** |

"Required terms find candidates, all terms score" — Combined with fixed-size blocks, processing 1 block (256 postings) fits in L1 cache and offers high SIMD compatibility.

### Quickwit Bitpacking

Adopted Quickwit's bitpacking library, achieving **741M postings/sec** decompression throughput.

| Method | Decompression Throughput |
|:---|:---:|
| **Quickwit bitpacking** | 741M postings/s |
| VByte (baseline) | 200M postings/s |
| Simple-8b | 400M postings/s |

### word_v3 Tokenizer

- NFKC normalization
- Improved handling of numbers and alphanumeric combinations
- Locale-aware case folding
- Efficient prefix queries

### Index Size (MSMARCO Dataset)

| Component | FTS v1 | FTS v2 | Reduction |
|:---|:---:|:---:|:---:|
| **Doc IDs** | 25.7 GiB | 2.62 GiB | 9.8x |
| **Term Frequencies** | 12.2 GiB | 1.12 GiB | 10.9x |
| **Positions** | 13.7 GiB | 1.48 GiB | 9.3x |
| **Total** | **51.6 GiB** | **5.22 GiB** | **9.9x** |

### BM25 Scaling Model

A paradoxical property of BM25 discovered by Adrien Grand: **an increase in token count can sometimes lead to lower latency**.

$$f(n) = C \cdot n^K$$

| Query Length | K Value (Scaling Exponent) | Behavior |
|:---|:---:|:---|
| Short (1-5 words) | K=0.35 | Strongly sublinear |
| Medium (5-20 words) | K=0.65 | Moderately sublinear |
| Long (20-100+ words) | K=0.92 | Nearly linear |

Required terms (high IDF) drive candidate selection, while non-required terms (low IDF) are efficiently skipped via MAXSCORE.

---

## Team

| Name | Role | Focus / Background |
|:---|:---|:---|
| **Simon Hørup Eskildsen** | Co-founder & CEO | Former Shopify |
| **Justine** | Co-founder & CTO | Former Shopify |
| **Nathan VanBenschoten** | Chief Architect | Vector search, SPFresh, RaBitQ, ANN v3 |
| **Adrien Grand** | Engineer | BM25, MAXSCORE, full-text search |
| **Morgan Gallant** | Engineer | Full-text search, inverted indexes, recall monitoring |
| **Nikhil Benesch** | Engineer | LSM Tree, infrastructure |
| **Xavier Denis** | Engineer | Rust performance, SIMD optimization |
| **Bojan Serafimov** | Engineer | Native Filtered Vector Search |

---

## Key Customers

| Customer | Use Case | Impact |
|:---|:---|:---|
| **Cursor** | Codebase search (billions of vectors) | 95% cost reduction, 23.5% Eval improvement |
| **Notion AI** | Semantic search / RAG | Large-scale vector search operations |
| **Linear** | Issue search | Full-text search + semantic search |
| **Superhuman** | Email search | Fast full-text search |
| **Readwise** | Highlight search | Full-text search |
| **Suno** | Music generation-related search | — |

### Current Scale

- 3.5T+ documents hosted
- 10M+ writes/s
- 25k+ queries/s
- 99.99% uptime since launch

---

## Relationship with Zero Disk Architecture

turbopuffer is one of the most representative commercial products embodying [[concepts/zero-disk-architecture]].

- **Object Storage Exclusive Dependency**: "No Dependencies" — no stateful dependencies on the critical path other than object storage
- **Stateless Compute Nodes**: Rust binary loads namespaces directly from S3 buckets. Node failure → another node takes over immediately
- **Ultimate Durability**: Leverages S3's 99.999999999% durability directly. Design philosophy learned from "pager fatigue" during the Shopify era

> "The fewer stateful dependencies, the more nines of uptime." — Simon Hørup Eskildsen

---

## Related Pages

- [[concepts/object-storage-queue]] — Queue implementation pattern on object storage, implemented by turbopuffer
- [[concepts/turbopuffer-rank-by-attribute]] — Combined BM25 + numeric attribute ranking feature
- [[concepts/zero-disk-architecture]] — Zero Disk Architecture concept (turbopuffer is a representative commercial implementation)
- [[concepts/absurd-durable-execution]] — Postgres-Native Durable Execution (a contrasting "Just One Service" approach)

## References

### turbopuffer Official Blog
- [turbopuffer: Fast Search on Object Storage](https://turbopuffer.com/blog/turbopuffer) — Official announcement blog ([[raw/articles/2026-05-07_turbopuffer-fast-search-object-storage]])
- [How to Build a Distributed Queue in a Single JSON File](https://turbopuffer.com/blog/object-storage-queue) — Queue implementation blog ([[raw/articles/2026-05-07_object-storage-queue-turbopuffer]])
- [ANN v3: 100B Vector Search at 200ms p99](https://turbopuffer.com/blog/ann-v3) — Third-generation ANN with RaBitQ quantization + AVX-512 ([[raw/articles/2026-05-05_turbopuffer-ann-v3]])
- [Rust Zero-Cost Abstractions vs SIMD](https://turbopuffer.com/blog/zero-cost) — 4.7x speedup via batch iterators ([[raw/articles/2026-03-08_turbopuffer-rust-zero-cost-simd]])
- [FTS v2: 20x Faster Full-Text Search](https://turbopuffer.com/blog/fts-v2) — Second-generation full-text search ([[raw/articles/2026-02-03_turbopuffer-fts-v2]])
- [FTS v2 Postings: Building Better Inverted Indexes](https://turbopuffer.com/blog/fts-v2-postings) — Fixed-size blocks and 9.9x compression ([[raw/articles/2026-01-14_turbopuffer-fts-v2-postings]])
- [Vectorized MAXSCORE over WAND](https://turbopuffer.com/blog/fts-v2-maxscore) — Rationale for dynamic pruning selection ([[raw/articles/2026-01-14_turbopuffer-fts-v2-maxscore]])
- [BM25 Scaling Surprises](https://turbopuffer.com/blog/bm25-latency-musings) — Power-law relationship of query length and latency ([[raw/articles/2026-01-07_turbopuffer-bm25-scaling]])
- [Native Filtering](https://turbopuffer.com/blog/native-filtering) — Clustering-based filtered search ([[raw/articles/2025-01-21_turbopuffer-native-filtering]])
- [Continuous Recall Measurement](https://turbopuffer.com/blog/continuous-recall) — recall@10 monitoring in production ([[raw/articles/2024-09-04_turbopuffer-continuous-recall]])

### Official Documentation
- [Architecture Documentation](https://turbopuffer.com/docs/architecture)
- [Concepts: Cache Hierarchy, LSM, SPFresh](https://turbopuffer.com/docs/concepts)
- [Tradeoffs](https://turbopuffer.com/docs/tradeoffs)

### Third-Party Analysis
- [TurboPuffer: Object Storage-First Vector Database Architecture](https://jxnl.co/writing/2025/09/11/turbopuffer-object-storage-first-vector-database-architecture/) — Technical deep-dive by Jason Liu
- [turbopuffer — Why Now Tech Primer](https://whynowtech.substack.com/p/turbopuffer) — Detailed analysis by Alex Mackenzie
