---
title: "Latent Briefing"
created: 2026-04-27
updated: 2026-04-27
tags: [multi-agent, kv-cache, token-efficiency, ramp-labs]
aliases: [latent-briefing]
related: [[concepts/kv-cache-compaction]], [[concepts/multi-agent-systems]], [[concepts/recursive-language-models]], [[entities/ramp-labs]]
sources: [
  "https://x.com/RampLabs/status/2042660310851449223"
]
---

# Latent Briefing

## Summary

Latent Briefing is Ramp Labs' implementation of task-guided KV cache compaction for efficient memory sharing between agents in hierarchical multi-agent systems. Instead of passing full context as text between orchestrator and worker agents, it compacts the orchestrator's reasoning trajectory into a compact KV cache that the worker model initializes with. This reduces token usage by 42-57% while maintaining or improving accuracy.

## How It Works

In standard RLM (Recursive Language Model) architecture:
1. Orchestrator decomposes task and makes repeated calls to worker via REPL
2. Worker only sees what orchestrator explicitly passes (query + document)
3. Orchestrator's accumulated reasoning across many calls is unused by the worker

Latent Briefing changes this:
1. Worker maintains a persistent KV cache of orchestrator's trajectory
2. On each call, the trajectory is forward-passed through the worker model
3. Task prompt generates query vectors via attention to the trajectory
4. Trajectory's KV cache is compacted using these queries as relevance signal
5. Worker initializes with compacted KV cache, preserving only what it needs

## Technical Details

### Task-Guided Query Vectors
Forward pass the trajectory and task prompt through the worker model. Attention scores between the task prompt and trajectory keys reveal which parts of the trajectory the worker considers relevant.

### Shared Token Selection
Aggregate attention scores across all layers and heads into a single per-position relevance score. Instead of 320 independent editors each selecting their own top-k, they vote on which sections to keep.

### Thresholding with MAD Normalization
Keep every position scoring above a statistically derived MAD-normalized threshold. The threshold parameter controls aggressiveness (e.g., t=−1.0 for 18% compaction, t=2.0 for 79% compaction).

### Real-Time Optimization
Shared global mask enables batched tensor operations across all 320 attention heads. GPU memory optimizations (in-place softmax, CPU offload, chunked prefills, adaptive batch sizing) reduce overhead from 30+ seconds to ~1.7s.

## Performance Results
Evaluated on LongBench v2 (Claude Sonnet 4 orchestrator, Qwen-14B worker):
- Accuracy: Compaction matches or improves baseline (+3pp at optimal thresholds)
- Token savings: 42-57% median worker token reduction
- Latency: ~1.7s median compaction overhead (20× faster than sequential AM, 10-30× faster than LLM summarization)
- Scaling: Linear with trajectory length, small fraction of overall call cost

## Best Practices by Condition

| Condition | Optimal Threshold | Compaction Rate | Rationale |
|-----------|-------------------|-----------------|-----------|
| Long documents (32k-100k) | t=-1.0 | 18% | Preserve broad coverage for dispersed information |
| Hard questions | t=2.0 | 79% | Strip speculative reasoning noise |
| Short, easy documents | t=1.0 | 68% | Remove redundancy without risk |

## Related Concepts
- [[concepts/kv-cache-compaction]] — The underlying technique
- [[concepts/multi-agent-systems]] — Where this is applied
- [[concepts/recursive-language-models]] — The RLM framework used
- [[entities/ramp-labs]] — Developer of Latent Briefing
