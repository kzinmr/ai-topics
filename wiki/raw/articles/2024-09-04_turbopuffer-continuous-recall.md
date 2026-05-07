---
title: "Continuous Recall Measurement: How turbopuffer Monitors ANN Quality in Production"
date: 2024-09-04
author: Morgan Gallant (Engineer)
source_url: https://turbopuffer.com/blog/continuous-recall
type: raw-article
tags: [turbopuffer, recall, ann, monitoring, production, quality-assurance]
---

# Continuous Recall Measurement: How turbopuffer Monitors ANN Quality in Production

turbopuffer implements **continuous recall measurement** in production by sampling 1% of all queries and computing recall@10 against exact nearest neighbors. Maintains a **90-95% recall target** with automated alerting.

> "turbopuffer is the first search engine to continuously monitor recall in production — not just in benchmarks."

## Methodology

### Production Query Sampling

1. **1% of production queries** are randomly selected for recall measurement
2. For each sampled query:
   - Run ANN search (fast, approximate)
   - Run exact kNN search (slow, required for ground truth)
3. Compare top-10 results from both methods
4. Compute **recall@10**: fraction of exact top-10 present in ANN top-10 results

### Recall Target

| Metric | Target | Action |
|:---|:---:|:---:|
| **Recall@10** | 90-95% | Normal operation |
| **Recall@10 < 90%** | Alert triggered | Investigate index degradation |
| **Recall@10 > 95%** | Tuning opportunity | May be over-conservative, could optimize for speed |

### Why 90-95%?

> "90-95% recall is the sweet spot. Below 90%, users notice quality degradation. Above 95%, you're likely sacrificing too much performance for marginal recall gains."

## ANN Napkin Math

The blog provides simple formulas for estimating ANN design tradeoffs:

- **Recall vs QPS tradeoff**: Doubling candidates ≈ sqrt(2)x more recall, half QPS
- **Memory vs accuracy**: More centroids = better recall, more memory
- **Dimensionality impact**: Higher dims need proportionally more candidates

## Continuous vs Discrete Monitoring

| Approach | turbopuffer (Continuous) | Traditional (Benchmark) |
|:---|:---:|:---:|
| **Data** | Real production queries | Fixed benchmark queries |
| **Frequency** | Every query (1% sample) | Pre-deployment only |
| **Distribution** | Live traffic distribution | Static, may drift |
| **Index state** | Current production state | Fresh index, unrealistic |
| **Detection** | Real-time degradation | Post-hoc |

## Benefits

1. **Early degradation detection**: Index corruption, data drift, or parameter drift caught within minutes
2. **Confidence in deployments**: Changes can be evaluated on real traffic
3. **Tuning feedback loop**: Performance vs accuracy tradeoffs measured continuously
4. **Customer trust**: SLA on recall quality, not just latency

## Implementation Details

- **Exact kNN computation**: Uses brute-force over the shard's full vector set
- **Sampling bias control**: Random sampling ensures statistical validity
- **Rollup windows**: 5-minute, 1-hour, and 24-hour recall aggregates
- **Alerting**: PagerDuty integration for recall degradation

## Claim

> "turbopuffer is the first search engine to implement continuous recall measurement in production."

This enables a level of quality assurance that traditional vector databases (Pinecone, Weaviate, Qdrant, Milvus) do not provide — ANN accuracy is typically only measured during indexing or benchmarks, not continuously against live traffic.

## Key Contributors

- Morgan Gallant (Engineer) — design and implementation

## Related

- [[raw/articles/2026-05-05_turbopuffer-ann-v3]] — ANN v3 improvements
- [[raw/articles/2025-01-21_turbopuffer-native-filtering]] — Native filtered search
