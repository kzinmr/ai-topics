---
title: KV-Aware Routing
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [inference, optimization]
sources:
  - raw/articles/2026-04-25-nvidia-dynamo-agentic-inference.md
---

# KV-Aware Routing

KV-aware routing is an inference optimization technique where the request router selects workers not just based on current load, but also on KV cache overlap — i.e., whether a worker already has the relevant context (key-value cache) loaded.

## How It Works

When an agentic coding session makes multiple API calls:
1. The router checks which workers have overlapping KV cache entries
2. Requests are routed to workers that already hold relevant context
3. This avoids recomputing KV state from scratch on each call
4. [[nvidia-dynamo]] uses this as a core component of its Request Plane

## Why It Matters

- **Reduces KV recomputation waste:** Traditional routing ignores cache overlap
- **Improves latency:** Workers with pre-loaded context respond faster
- **Lowers cost per token:** Especially important for agentic workflows with hundreds of calls per session

## Connection to Broader Trends

KV-aware routing is part of the shift from throughput-optimized inference to context-aware inference, which is essential for [[agentic-engineering]] workloads. It connects to [[context-engineering]] as a runtime optimization layer.

## Related

- [[nvidia-dynamo]]
- [[context-engineering]]
- [[inference]]
- [[agentic-engineering]]
