---
title: "Agent queries cost more to serve"
author: Jo Kristian Bergum
source: https://hornet.dev/blog/agentic-query-workloads-change-retrieval-cost
date: 2026-06-03
tags:
  - agentic-retrieval
  - information-retrieval
  - bm25
  - hornet
  - search-infrastructure
  - cost-optimization
---

# Agent queries cost more to serve

**Source**: https://hornet.dev/blog/agentic-query-workloads-change-retrieval-cost
**Author**: Jo Kristian Bergum (CEO, Hornet)
**Date**: June 3, 2026
**Category**: Proof

## Summary

Agent queries are longer and carry more operators than human queries. On the same engine and index, that distribution shift cuts serving capacity **8.4x**, and agents are now the workload to optimize for.

## Key Points

### The Query Mix Problem

- Most people think serving capacity only runs out because query volume spikes — but just as often, the **query mix changes** and the system overloads at a traffic level that used to be safe.
- Examples: a frontend adding filters to every query, a customer sending longer queries, or phrase matching becoming more common.
- A phrase query made of common words ("to be or not to be") is more CPU-expensive than a simple AND between two rare words.
- "Benchmark your system with a realistic query mix. Otherwise you are in for a surprise once you get real users."

### Agents Query Differently

- Agent queries are **5x longer** than the human median and add phrase and filter operators that each cost extra query-processing work.
- A typical human query (AOL log): "home depot" — 2 terms.
- A typical GPT-5 BrowseComp agent query: `site:snooker.org 2021 UK Championship final Zhao Xintong Brecel "Frame scores"` — 10 terms with site: filter, year, and quoted phrase match.

### Query Length Percentiles

| Percentile | Human (AOL, 36M queries) | Agent (GPT-5 BrowseComp, 19,279 queries) |
|------------|--------------------------|------------------------------------------|
| Median | 2 terms | 10 terms |
| p90 | 5 terms | 17 terms |
| p99 | 8 terms | — |
| First-query mean | — | 19 terms |

The agent median sits **past the human 99th percentile**.

### 8.4x Serving Capacity Swing

Same engine (Hornet), same data (100M English Common Crawl WET documents), same hardware (single AWS Graviton4, 32 vCPUs, 128 GiB memory), same BM25(body) top-10 retrieval. Only the query workload changed.

| Workload | QPS at <500ms p99 |
|----------|-------------------|
| AOL human keyword queries | 3,236 QPS |
| MS MARCO human questions | 1,151 QPS |
| BrowseComp GPT-5 agent queries | 384 QPS |

That is an **8.4x spread** in serving capacity on the same system.

### Engine Benchmark on Agent Queries

On BrowseComp GPT-5 agent queries over 100M documents:
- **Hornet**: 384 QPS at <500ms p99
- **Closest alternatives**: ~230 QPS at same latency target
- Hornet sustains roughly **1.6x the throughput** per node
- To absorb the same agentic query volume with competing engines, you need ~1.6x the machines

### Hornet's Technical Approach

- Posting lists stored in compact, fixed-size blocks with metadata to skip blocks that cannot make top-k
- Blocks decode with **SIMD** for bulk decompression
- Query processing chosen by query shape:
  - **DAAT** (document-at-a-time) with dynamic pruning when rare terms carry the score
  - **BAAT** (block-at-a-time) accumulation when long queries spread weight across many common terms
- Long agent queries land in BAAT far more often than two-word human queries

### Key Takeaway

> "A two-word query typed by a human was the primary workload that dynamic top-k pruning algorithms were optimized for. Agents are the new user of retrieval infrastructure."

## Related

- [This is what agentic retrieval looks like](https://hornet.dev/blog/this-is-what-agentic-retrieval-looks-like) — Part 2 (May 2026)
- [Deep research is a retrieval problem](https://hornet.dev/blog/deep-research-is-a-retrieval-problem) — Part 1 (Mar 2026)
- [The scaling dimensions of keyword search](https://hornet.dev/blog/the-scaling-dimensions-of-keyword-search)
