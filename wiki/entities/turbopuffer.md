---
title: turbopuffer
created: 2026-05-20
updated: 2026-06-03
type: entity
tags:
  - search
  - vector-search
  - information-retrieval
  - infrastructure
  - ai-infrastructure
  - database
  - object-storage
  - ann
  - hnsw
  - bm25
  - lexical-search
  - agentic-search
  - platform
  - product
sources:
  - raw/articles/2026-05-05_turbopuffer-ann-v3.md
  - raw/articles/2026-05-20_turbopuffer_reinforcement-learning-sid-ai.md
  - https://turbopuffer.com
  - https://turbopuffer.com/docs
  - https://turbopuffer.com/docs/branching
  - raw/newsletters/2026-05-22-ainews-new-ai-infra-unicorns-exa.md
---

# turbopuffer

turbopuffer is a **fast search engine built on object storage**, combining vector and full-text search with a stateless compute layer over object storage (S3). It hosts 4T+ documents, handles 10M+ writes/s, and serves 25k+ queries/s in production.

The core architectural insight: **decouple compute from storage**, using object storage as the sole source of truth with a memory/SSD caching hierarchy for hot data. This enables stateless horizontal scaling, 100x cheaper cold storage than in-memory vector databases, and copy-on-write namespace branching.

## Architecture

```
┌──────────┐     ┌──────────────────────────────┐     ┌──────────────────┐
│  Client  │────▶│  Query Tier (stateless pool)  │────▶│  Object Storage  │
└──────────┘     │  ├─ Memory Cache (hot)        │     │  (S3, cold)      │
                 │  ├─ NVMe SSD Cache (warm)     │     └──────────────────┘
                 │  └─ Compute (query planning)  │
                 └──────────────────────────────┘
```

- **Stateless query tier**: Any node can serve any query; no shard ownership bottleneck
- **Caching hierarchy**: Memory → NVMe SSD → Object Storage; cold queries p90=444ms, warm p50=8ms
- **Object-storage-native**: Storage engine only "puffs" actively queried namespaces into cache
- **Branching**: Copy-on-write namespace clones in constant time; independent reads/writes

## Namespace Branching (Detailed)

turbopuffer's branching is a **native infrastructure primitive** — one API call creates a fully independent copy-on-write clone of a namespace:

```python
source = tpuf.namespace('branching-example-source')
ns = tpuf.namespace('branching-example')
ns.branch_from(source_namespace='branching-example-source')
```

### Properties
- **Constant-time creation** — regardless of namespace size (metadata operation on object storage)
- **Fully independent** — reads, writes, queries, and deletes on either namespace don't affect the other
- **Branch from branches** — supports multi-level workflows (e.g., per-developer branches from staging)
- **Unlimited** — no limit on child branches per namespace or branch chain depth

### Pricing
- Flat rate of **$0.032 per branch creation**
- Storage billed on logical bytes at standard rates (each branch billed as if independent)
- Planned reduction after production observation of reuse rates

### When to Use Branching vs `copy_from_namespace`
- **Use `branch_from`** for most cases — instant, cheap, CoW
- **Use `copy_from_namespace`** when: need full data isolation, copying across regions/organizations, or re-encrypting with a different CMEK key

### Use Cases
- **Codebase indexing** — embed once, branch per local checkout; only changed files need re-indexing
- **Test pipelines** — branch production, run tests against real data, tear down when done
- **Dev environments** — give each developer a sandbox of a shared dataset
- **Snapshots** — capture state of a changing namespace at a point in time, query the immutable snapshot
- **RL training reproducibility** — preserve exact training environments for ablation studies (used by [[entities/sid|SID AI]])

See: [[branch-aware-search]] for comparison with Qdrant and Neon approaches

## Key Capabilities

### Search Tool Diversity
Single query planner routes across multiple index types:
- **Dense vector (ANN)**: Approximate nearest neighbor via [[raw/articles/2026-05-05_turbopuffer-ann-v3|ANN v3]] (SPFresh + RaBitQ + AVX-512)
- **BM25**: Full-text lexical search
- **Sparse vector**: Learned sparse representations
- **Regex / Glob**: Pattern-matching search
- **Metadata filtering**: Native, index-aware filtering across all modalities

### Scale Limits

| Metric | Production | Current Limit |
|--------|-----------|---------------|
| Max documents (queried simultaneously) | 100B+ @ 10TB | Unlimited |
| Max documents (per namespace) | 500M+ @ 2TB | 500M @ 2TB |
| Max namespaces | 250M+ | Unlimited |
| Max write throughput (global) | 10M+ writes/s @ 32GB/s | Unlimited |
| Max queries (global) | 25k+ queries/s | Unlimited |
| Vector search recall@10 | 90-100% | 90-100% |

### Economics
- **Cold storage**: ~100x cheaper than memory-resident vector databases
- **Warm SSD cache**: ~6-20x cheaper than in-memory
- **Namespace pinning**: Reserve compute for high-QPS namespaces at predictable cost
- **Scale-to-zero**: Inactive namespaces pay only object storage costs

## Role in RL-for-Search Training

turbopuffer serves as the search backend for [[entities/sid|SID AI]]'s RL training of [[concepts/agentic-search|agentic search]] models like SID-1. The RL training workload imposes unique demands that turbopuffer's architecture is particularly suited for:

### Bursty, High-QPS Reads
During synchronous RL rollouts (GRPO), all 4,096 attempts fire initial searches simultaneously, creating **1k+ QPS bursts**. turbopuffer's stateless query tier absorbs these bursts by spreading traffic across the shared compute pool, while new nodes hydrate cache from object storage on demand (vs. copying shards, which takes minutes).

### Diverse Tool Indices
RL training benefits from the widest possible set of search tools. turbopuffer builds and maintains all index types (ANN, BM25, sparse, regex, glob) under a single query planner, reducing engineering overhead.

### Massive Namespaces → Scale to Zero
Training namespaces can sit cold for weeks between experiments. turbopuffer's object-storage-first model means cold namespaces incur only low storage cost. Namespace pinning keeps active namespaces hot during training runs.

### Corpus Branching for Reproducibility
Real-world corpora evolve, but training questions reference specific document versions. turbopuffer's native branching creates copy-on-write clones, allowing corpus updates on new branches while preserving exact training environments for ablation studies.

## Notable Users
- **SID AI**: RL training backend for SID-1 (1k+ QPS, 10M+ document corpora, 1,000+ training steps)
- **Linear**: Issue search via embeddings + full-text (Jori Lallo, co-founder)
- **Notion**: Co-founder Akshay Kothari cited cost savings: "turbopuffer's economics have changed the way we think about building products"

## Related Pages
- [[concepts/agentic-search]] — Agentic search paradigm and SID-1 integration
- [[entities/sid]] — SID AI research lab
- [[raw/articles/2026-05-05_turbopuffer-ann-v3]] — ANN v3 technical details (SPFresh, RaBitQ, AVX-512)
- [[concepts/grpo-rl-training]] — GRPO algorithm used in SID-1 training
- [[raw/articles/2026-05-20_turbopuffer_reinforcement-learning-sid-ai]] — Full article on SID-1 RL training with turbopuffer

## External Links
- **Website**: https://turbopuffer.com
- **Documentation**: https://turbopuffer.com/docs
- **Blog**: https://turbopuffer.com/blog
- **ANN v3 Post**: https://turbopuffer.com/blog/ann-v3

### $100M ARR Milestone (May 2026)

turbopuffer crossed **$100M annualized run-rate in March 2026**, growing from $1M to $100M ARR in **19 months**. The company is **profitable** with less than $1M in external funding.

This represents one of the fastest growth trajectories in AI infrastructure: bootstrapped-like capital efficiency with hyper-growth ARR.
