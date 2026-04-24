---
title: "Neural Garbage Collection"
type: concept
created: 2026-04-23
updated: 2026-04-23
tags: [inference, reinforcement-learning, kv-cache, optimization, context-management]
aliases: ["neural-gc", "kv-cache-eviction"]
sources:
  - https://substack.com/app-link/post?publication_id=1084089&post_id=195193203
---

# Neural Garbage Collection

**Neural Garbage Collection** is a reinforcement learning approach that jointly learns reasoning capability and KV-cache retention/eviction without proxy objectives. Instead of separately optimizing for reasoning quality and cache efficiency, a single RL agent learns which context tokens to retain and which to evict based on their actual contribution to task completion.

## Core Idea

Traditional KV-cache management uses heuristic eviction strategies (e.g., sliding window, attention sinks preservation, token importance scoring). Neural Garbage Collection replaces these handcrafted rules with an end-to-end RL agent that directly optimizes for the same objective that matters: **task completion quality with minimal context tokens**.

> *"RL jointly learns reasoning and KV-cache retention/eviction without proxy objectives"* — AINews #21 (April 2026)

## Why It Matters

### 1. Eliminates Proxy Objective Problem
Previous approaches optimize proxies (attention scores, token entropy, positional importance) that correlate poorly with actual reasoning contribution. Neural GC trains directly on the reward signal — the model itself learns what to keep.

### 2. Joint Optimization
Reasoning and context management are not independent problems. A token's value for cache eviction depends on what reasoning task is being performed. Joint training captures this interdependence.

### 3. Context Window Efficiency
Directly applicable to [[context-engineering]], [[concepts/harness-engineering/system-architecture/context-compaction.md]], and [[context-window-management]]. Reduces token waste without quality degradation.

## Relation to Tokenmaxxing

[[tokenmaxxing]] and **Neural Garbage Collection** form complementary optimization layers:
- **Tokenmaxxing** = workflow strategy (how to use tokens efficiently)
- **Neural GC** = model-level optimization (how to manage KV-cache at inference time)

Where tasteful tokenmaxxing achieves efficiency through behavioral changes (depth-first workflows, trace-driven optimization), Neural GC achieves efficiency through architectural changes (RL-optimized cache eviction).

## Related Concepts

- [[token-economics]] — Cost framework that Neural GC helps optimize at inference time
- [[context-engineering]] — Dynamic token curation; Neural GC as a learned approach
- [[concepts/harness-engineering/system-architecture/context-compaction.md]] — Reducing context window waste; Neural GC as RL-based compaction
- [[speculative-decoding]] — Inference acceleration; Neural GC complements by reducing context size
- [[inference]] — LLM Inference Optimization overview

## Sources

-  — AINews #21, Latent.Space (April 2026) — "Neural Garbage Collection" mention in Post-Training, RL & Inference Optimization section
