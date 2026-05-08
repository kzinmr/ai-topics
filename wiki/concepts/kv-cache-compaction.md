---
title: "KV Cache Compaction"
created: 2026-04-27
updated: 2026-04-27
tags: [multi-agent, kv-cache, token-efficiency, attention]
aliases: [kv-cache-compaction, attention-matching-compaction]
related: [[concepts/latent-briefing]], [[concepts/multi-agent-systems]], [[concepts/context-management]], [[entities/ramp-labs]]
sources: [
  "https://x.com/RampLabs/status/2042660310851449223"
]
---

# KV Cache Compaction

## Summary

KV Cache Compaction is a technique for reducing token usage in multi-agent systems by operating directly on the model's internal representations. Instead of LLM-based summarization or RAG-based retrieval, it identifies which parts of the context are important via attention patterns and discards the rest at the representation level. The most notable implementation is Ramp Labs' "Latent Briefing."

## Key Concepts

### Attention Matching (AM) Framework
The core idea: given a KV cache of size S, find a compact cache of size t < S that produces nearly identical attention outputs. For each attention head, solve for compacted components (C1, β, C2) where C1 selects high-attention key vectors, β provides bias corrections for missing keys, and C2 reconstructs value vectors via ridge regression.

### Task-Guided Queries
Rather than sampling queries from the context itself, use the orchestrator's task prompt for the specific worker call as the query vector. This enables cache compression that prioritizes information most relevant to the worker's current task.

### Shared Global Scoring
Instead of each attention head independently selecting its own top-k keys, aggregate scores across all layers and heads into a single per-position relevance score. This allows batched execution, significantly reducing overhead.

### MAD Normalization Thresholding
Rather than selecting a fixed number of tokens, keep every position scoring above a statistically derived threshold. MAD (Median Absolute Deviation) normalization provides a robust outlier metric that adapts to different document lengths and question difficulties.

## Key Ideas

- Token usage compounds across agent calls, making efficiency a first-order concern
- LLM summarization introduces 20-60s latency and is lossy
- RAG is brittle, misses cross-chunk dependencies
- KV cache compaction operates at the representation level — no text serialization overhead
- ~1.7s median compaction overhead scales linearly with input length
- Optimal compaction threshold varies by condition: longer documents → lighter compaction, harder questions → aggressive compaction
- Up to 49% median token savings on medium-length (32k-100k token) documents
- 65% reduction in worker model token consumption

## Terminology

- **KV Cache** — Key-Value cache storing attention representations for all tokens
- **Compaction** — Reducing the KV cache size while preserving attention outputs
- **Latent Briefing** — Ramp Labs' implementation of task-guided KV cache compaction for multi-agent systems
- **Attention Matching** — The original AM framework for KV cache compaction (Zweiger et al., 2026)
- **MAD Normalization** — Median Absolute Deviation-based thresholding for robust token selection
- **Recursive Language Model (RLM)** — Architectural framework where an orchestrator decomposes tasks and calls a worker model via REPL

## Experimental Results (Ramp Labs)
Evaluated on LongBench v2 (126 questions, 0-100k token documents):
- Comparable or improved accuracy relative to vanilla RLM baseline
- Up to 49% median token savings on medium-length documents
- 65% reduction in worker model token consumption
- ~1.7s median compaction overhead
- +3pp accuracy gain at optimal thresholds across all conditions

## Pitfalls & Limitations

- **Orchestrator variance** — Non-deterministic orchestrators lead to different decomposition strategies across runs
- **Single benchmark** — Tested only on LongBench v2; other task types may have different attention patterns
- **Over-compaction** — Discards information the worker needs, reducing accuracy
- **Under-compaction** — Leaves too much noise relative to signal, diluting attention

## Related Concepts
- [[concepts/latent-briefing]] — Ramp Labs' implementation
- [[concepts/multi-agent-systems]] — Multi-agent architectures where this is most relevant
- [[concepts/context-management]] — Managing context across agents
- [[entities/ramp-labs]] — Company that developed Latent Briefing
