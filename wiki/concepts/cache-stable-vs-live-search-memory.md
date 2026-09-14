---
title: "Cache-Stable vs Live-Search Memory (Agent Memory Tradeoff)"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [concept, agent-memory, memory-systems, agent-harness, hermes-agent, openclaw, mem0, design-patterns, context-engineering]
sources:
  - raw/articles/2026-05-27_mem0-openclaw-hermes-agent-memory.md
confidence: medium
description: "The two coherent poles of long-running agent memory design: cache-stable (Hermes: small, frozen, hard-capped prompt memory optimized for stable cached sessions) vs live-search (OpenClaw: file-native, searchable, evolving memory workspace). Both integrate Mem0 as cross-tool persistence; the tradeoff is cache/prefix stability vs immediate live recall."
related: [ai-memory-systems, memory-systems-design-patterns, hermes-agent-architecture, self-evolving-agents, context-engineering, kv-cache]
confidence_note: "Single-source concept (Mem0 engineering blog, May 2026) — framing is well-supported by the two named harnesses' public designs, but the two-pole taxonomy is the author's."
---

# Cache-Stable vs Live-Search Memory (Agent Memory Tradeoff)

**Cache-stable vs live-search memory** names the two coherent design poles for long-running agent memory, identified by Mem0's engineering team in ["What OpenClaw and Hermes Agent Reveal About Agent Memory"](https://x.com/i/article/2059652660022910976) (May 2026). The core question the two harnesses force into the open: **should agent memory be optimized for stable, cached long sessions, or for immediate, live recall?** ([raw](raw/articles/2026-05-27_mem0-openclaw-hermes-agent-memory.md))

## Why Memory Became Architecture

Long-running coding agents all hit the same failure: memory fades over time. A chat session is not one clean prompt — it stretches across hours, days, files, decisions, preferences, and half-finished work. "That is why memory is no longer just a feature. It is part of the agent architecture."

## The Two Poles

| Dimension | Cache-stable (Hermes) | Live-search (OpenClaw) |
|---|---|---|
| Model | Tightly curated **working set** | Evolving **workspace** |
| Mutability | Frozen during session; edits deferred/controlled | Changes while the agent works |
| Storage | Two files, hard caps: `MEMORY.md` (2,200 chars) + `USER.md` (1,375 chars) in `~/.hermes/memories/` | File-native memory, searchable, grows freely |
| Optimized for | Prompt-cache stability — identical prefix across long sessions → KV-cache hits, predictable token cost | Immediate live recall — newest facts retrievable the moment they're written |
| Failure mode | Cap pressure forces lossy curation; stale until curated in | Prefix churn breaks caches; retrieval quality becomes the bottleneck |

Both harnesses lean on markdown files for memory, both target extended multi-day sessions, and both solve "survives across sessions, accumulates context, gets more useful over time." The divergence is *where* they place the constraint: Hermes bounds the prompt-resident set to keep it frozen and small; OpenClaw bounds nothing and relies on search over an ever-growing store.

## The Third Layer: Cross-Tool Persistence

Both integrate the [[entities/mem0|Mem0]] plugin, which addresses a problem neither pole solves: memory that survives **one harness, one session, or one local memory file**. Mem0 sits underneath as a cross-tool persistence layer — the tradeoff above is intra-agent; cross-agent/cross-tool continuity is an orthogonal axis.

## Analysis

The tradeoff is a direct consequence of [[concepts/kv-cache|KV-cache]] economics: any prompt mutation invalidates the cache from the mutation point onward, so a frozen memory block is a *cache-performance decision* dressed as a memory feature. Conversely, live-search memory converts every "what do I know?" into a retrieval call — moving cost from tokens to query-time, and moving the quality risk from curation to ranking. This is the memory-systems instance of the general harness principle in [[concepts/agent-harnesses]]: as models and compaction improve, some manual scaffolding gets absorbed — but the cache-stability vs freshness tension is economic, not capability-based, so it is unlikely to disappear.

Related evidence in the wiki: Hermes's frozen, capped design also appears in [[concepts/hermes-agent-architecture]]; the broader vendor landscape (ChatGPT vs Claude vs Cognition) is mapped in [[concepts/ai-memory-systems]] and [[concepts/memory-systems-design-patterns]], where the same split appears as "bitter lesson" retrieval-over-curated-context vs curated memory tool.

## Open Questions

- Is there a hybrid — frozen prompt-resident core + append-only live journal excluded from the cached prefix? (Several 2026 harnesses are converging on this; the Mem0 article predates them.)
- Do hard caps (2,200 chars) actually preserve the *right* facts? Curation policy is unexamined by the cache-stable pole.
- As compaction improves (see [[concepts/agent-native-tool-fallacy]]'s "re-compact 272k almost unlimited times" observation), does the cost case for frozen memory weaken?

## See Also

- [[concepts/hermes-agent-architecture]] — the cache-stable pole's full architecture
- [[concepts/ai-memory-systems]] — vendor-level design philosophy comparison
- [[concepts/memory-systems-design-patterns]] — Anthropic vs OpenAI vs Cognition patterns
- [[concepts/kv-cache]] — the economics behind the frozen-memory choice
