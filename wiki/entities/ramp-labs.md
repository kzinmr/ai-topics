---
title: "Ramp Labs"
type: entity
aliases: [ramp-labs, ramp]
tags: [entity, ai-research, multi-agent, kv-cache]
status: complete
description: "AI research company focused on multi-agent system efficiency. Created Latent Briefing — KV cache compaction for efficient memory sharing between agents."
created: 2026-04-27
updated: 2026-04-27
sources: [
  "https://x.com/RampLabs/status/2042660310851449223"
]
related: [
  "[[concepts/latent-briefing]]",
  "[[concepts/kv-cache-compaction]]",
  "[[concepts/multi-agent-systems]]",
  "[[concepts/recursive-language-models]]"
]
---

# Ramp Labs

## Overview

**Type:** AI Research Company
**Focus:** Multi-agent system efficiency, KV cache compaction, token optimization
**Key Publication:** ["Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction"](https://x.com/i/article/2042631550261510144) (April 2026)

## Key Research: Latent Briefing

Ramp Labs' flagship contribution is **Latent Briefing** — a method for sharing relevant memory between agents by operating directly on the model's KV cache rather than serializing context as text.

### The Problem
In hierarchical multi-agent architectures (orchestrator → worker), redundant intermediate reasoning compounds token usage. The orchestrator builds rich reasoning trajectories across many calls, but the worker only sees what the orchestrator explicitly passes. Standard solutions (LLM summarization, RAG) introduce latency or lose cross-dependencies.

### The Solution
1. Worker maintains persistent KV cache of orchestrator's trajectory
2. Task prompt generates query vectors via attention to trajectory
3. Trajectory KV cache compacted using queries as relevance signal
4. Worker initializes with compacted cache — preserving only what it needs

### Results (LongBench v2, Claude Sonnet 4 + Qwen-14B)
- Comparable or improved accuracy vs baseline
- Up to 49% median token savings on medium-length documents
- 65% reduction in worker model token consumption
- ~1.7s median compaction overhead (20× faster than sequential AM)

### Technical Innovations
- Task-guided query vectors (orchestrator's task prompt → query vectors)
- Shared global token selection (cross-head consensus voting)
- MAD normalization thresholding (robust, adaptive compression)
- Batched tensor execution (320 solves → 2-3 GPU batches)

## Research Approach

Ramp Labs focuses on **efficiency as a first-order concern** in agent system design. Rather than optimizing intelligence per token within individual agents, they examine how efficiently tokens are used across agents in the system as a whole.

## Hiring

Ramp Labs is hiring across roles (as noted in their Latent Briefing article).

## Related
- [[concepts/latent-briefing]] — Their flagship research
- [[concepts/kv-cache-compaction]] — The underlying technique
- [[concepts/multi-agent-systems]] — Domain of application
- [[concepts/recursive-language-models]] — RLM framework used for evaluation
