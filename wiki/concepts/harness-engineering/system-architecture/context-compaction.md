---
title: "Context Compaction"
type: concept
aliases:
  - compaction
  - context-compression
  - native-compaction
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - architecture
  - harness-engineering
  - context-management
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
---

# Context Compaction

A mechanism that **compresses unnecessary data while preserving critical information** when a long-running agent reaches the context window limit. A native feature of the OpenAI Responses API.

## Problem

In agent loops, tool call results, reasoning summaries, and conversation history accumulate. In long tasks, this can exceed 200K tokens, filling the context window.

> "Long-running tasks fill the context window... the limited context window quickly fills up."

## OpenAI's Approach

The model is trained to generate **encrypted, token-efficient compressed items** on its own.

### Two Modes

| Mode | Description | Use Case |
|------|-------------|---------|
| **Server-side** | Auto-triggers at configurable thresholds. Allows some overshoot | Long-running tasks, automated operation |
| **Standalone** | Manual control via `/compact` endpoint | Explicit compression timing |

### Mechanism

```
Before: [System prompt] + [Conversation history 1-150] + [Many tool results]
                    ↓
After: [Compressed item (encrypted)] + [High-value conversation history subset]
```

- Compressed items are in a model-readable format, preserving critical state
- Server-side compression evolves with each model release (tracks training)
- Eliminates need for complex client-side summarization logic

## Codex's Self-Improvement

> "Codex helped us build the compaction system while serving as an early user of it. When one Codex instance hit a compaction error, we'd spin up a second instance to investigate. The result was that Codex got a native, effective compaction system just by working on the problem."

** Codex investigated its own compaction errors and improved the compaction system itself**. This is a concrete example of "models building tools for themselves."

## Related Concepts

- [[concepts/context-window-management]] — Higher-level concept of compaction (Simon Willison's strategic management)
- [[concepts/harness-engineering/system-architecture/agent-loop-orchestration]] — Source of context accumulation that requires compaction
- [[entities/openai]] — The underlying API that implements compaction

## References

- [OpenAI: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- [[entities/openai]] — OpenAI
