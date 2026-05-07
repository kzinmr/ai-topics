---
title: "turbopuffer: Fast Search on Object Storage"
author: Simon Hørup Eskildsen (Co-founder & CEO, turbopuffer)
source: turbopuffer.com
date: 2026-03-05
tags: [vector-search, full-text-search, object-storage, zero-disk, database]
url: https://turbopuffer.com/blog/turbopuffer
---

# turbopuffer: Fast Search on Object Storage

turbopuffer is a search engine built on object storage (S3/GCS) as the primary source of truth. Up to 100x cost reduction for cold storage, 6-20x for warm storage.

## Architecture

- Object-Storage-First LSM tree — object storage is the primary durable layer, not a tier
- No stateful dependencies in critical path other than object storage
- Multi-tenancy & sharding at the core (Shopify heritage)
- Query planning limited to max 3 roundtrips to object storage
- Compute = Rust stateless nodes; Cache = NVMe SSD + memory tier

## Storage Cost per TB/month

| Architecture | Cost |
|:---|:---:|
| RAM + 3x SSD (incumbents) | $3,600 |
| 3x SSD | $600 |
| S3 + SSD Cache (turbopuffer) | **$70** |
| S3 (Raw) | $20 |

## Performance (1M 768-dim vectors / 3GB)

- Cold query: 444ms p90
- Warm query: **10ms** p90
- Full-text (1M docs BM25): 285ms p90 cold, 18ms p90 warm

## Vector Index

- SPFresh — centroid-based approximate nearest neighbor (ANN) index
- Designed for object storage: minimizes roundtrips vs graph-based (HNSW/DiskANN)
- Incremental index updates via LSM tree + WAL on object storage

## Customers

- Cursor: billions of vectors → 95% cost reduction, 23.5% eval improvement
- Notion AI, Linear, Superhuman: semantic search and RAG
- Readwise, Suno

## Scale

- 3.5T+ documents hosted
- 10M+ writes/s
- 25k+ queries/s
- 99.99% uptime since launch
