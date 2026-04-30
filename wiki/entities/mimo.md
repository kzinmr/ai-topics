---
title: "MiMo (Xiaomi)"
type: entity
created: 2026-04-30
updated: 2026-04-30
tags: [model, open-source, long-context, xiaomi]
sources:
  - raw/articles/2026-04-28_mimo-v25-pro.md
related:
  - "[[entities/gm8xx8]]"
---

# MiMo (Xiaomi)

**MiMo** is Xiaomi's open-source LLM family. The **MiMo-V2.5-Pro** model (April 2026) represents a significant advancement in long-context reasoning and agentic system design.

## MiMo-V2.5-Pro Specifications
- **Total parameters:** 1.02T MoE (1.02 trillion Mixture of Experts)
- **Active parameters:** 42B
- **Context length:** 1M tokens
- **Architecture:** Hybrid attention (128-token Sliding Window Attention with periodic global attention at ~6:1 ratio) plus a learnable attention sink bias, keeping KV growth bounded
- **Foundation:** Builds directly on V2-Flash

## Significance
MiMo-V2.5-Pro demonstrates how to scale long-context capabilities to 1M tokens while maintaining efficiency through:
1. Hybrid attention patterns (local SWA + periodic global)
2. Learnable attention sink bias to bound KV cache growth
3. MoE architecture for parameter efficiency

## Related
- [[concepts/kv-cache]] — MiMo's approach to KV cache management
- [[concepts/attention-mechanism-variants]] — Hybrid SWA attention
- [[concepts/context-window-management]] — 1M context length

## References

- 2026-04-28_mimo-v2-5-pro-xiaomi

- mimo-v2-5-pro-xiaomi-2026-04-28
