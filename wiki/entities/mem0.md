---
title: Mem0
created: 2026-05-28
updated: 2026-05-28
type: entity
tags:
  - entity
  - memory-systems
  - ai-agents
  - open-source
  - product
  - agent-framework
  - context-engineering
aliases:
  - mem0ai
  - mem0.ai
sources:
  - raw/articles/2026-05-27_mem0-openclaw-hermes-agent-memory.md
  - https://x.com/i/article/2059652660022910976
  - https://mem0.ai
  - https://docs.mem0.ai
related:
  - "[[entities/hermes-agent]]"
  - "[[entities/openclaw]]"
  - "[[concepts/ai-agent-memory-middleware]]"
  - "[[concepts/agent-memory]]"
---

# Mem0

**Mem0** is an intelligent, open-source memory layer designed for LLMs and AI agents, providing long-term, personalized, and context-aware interactions across sessions. It serves as a **cross-tool persistence layer** — helping agents remember beyond one harness, one session, or one local memory file.

## Core Product

Mem0 provides server-side fact extraction, storage, and retrieval that agents can use regardless of which harness (Hermes, OpenClaw, LangChain, etc.) they run on. Available as both a hosted platform (api.mem0.ai) and self-hostable open-source (GitHub: mem0ai/mem0).

## Integration with Agent Harnesses

### Hermes Agent Integration

Mem0 is one of eight external memory providers for Hermes. Activation: `hermes memory setup`. Writes `memory.provider: mem0` into `~/.hermes/config.yaml`. Three tools are exposed: `mem0_profile`, `mem0_search`, `mem0_conclude`.

Architecture: after each turn, Hermes ships the user/assistant exchange to Mem0 in a background thread for server-side fact extraction. A circuit breaker pauses calls for 2 minutes after 5 consecutive failures — slow/failed calls never block the conversation.

In Hermes, Mem0 **fixes two limitations**:
- The 3,575-character memory ceiling (MEMORY.md + USER.md)
- The substring-match retrieval (Hermes's native memory tool uses substring matching, not semantic search)

### OpenClaw Integration

Mem0 for OpenClaw is the npm package `@mem0/openclaw-mem0`. CLI install:
```bash
openclaw plugins install @mem0/openclaw-mem0
openclaw mem0 init --mode open-source
```

Adds eight memory tools: `memory_search`, `memory_add`, `memory_list`, `memory_get`, `memory_update`, `memory_delete`, `memory_event_list`, `memory_event_status`.

Two modes:
- **Platform**: conversations sent to api.mem0.ai, requires `MEM0_API_KEY`
- **Open-Source**: no Mem0 API key; uses OpenAI `gpt-5-mini` for fact extraction and `text-embedding-3-small` for embeddings (configurable backends)

Default operation: skills mode (triage → recall → dream protocol). Also supports `autoRecall` and `autoCapture` flags. Per-user scoping is automatic via `userId`.

In OpenClaw, Mem0 **fixes two limitations**:
- The silent-truncation-at-20k-char problem
- Server-side extraction so the agent doesn't have to remember to write things down

## "In Context" Blog Series

Mem0 publishes an "In Context" blog series covering AI Agent memory and context engineering. The series analyzes real-world agent memory architectures and trade-offs.

### Published Analyses
- **What OpenClaw and Hermes Agent Reveal About Agent Memory** (May 2026): Deep-dive comparing frozen vs. live system prompts, memory tool APIs, compaction/dreaming mechanisms, and cross-session recall in both harnesses

## Key Technical Insights

From the Hermes vs. OpenClaw analysis:

| Dimension | Hermes | OpenClaw |
|-----------|--------|----------|
| **Memory budget** | 3,575 chars (hard cap) | ~20,000 chars (soft target) |
| **System prompt** | Frozen at session start (cache-optimized) | Live-injected every turn (freshness-optimized) |
| **Write API** | Single tool: add/replace/remove by substring match | File editing + hybrid search tool |
| **Compaction** | None (manual consolidation on overflow) | Auto-compaction + pre-flush + Dreaming |
| **Cross-session** | Separate `session_search` tool (FTS5) | Unified `memory_search` over all sources |

The central trade-off: **cache stability vs. immediate visibility**. Hermes freezes memory at session start for optimal prefix caching; OpenClaw re-injects MEMORY.md every turn for live updates. Neither is wrong — they're different bets about what developers do for hours at a time.

## Related Concepts

- [[concepts/ai-agent-memory-middleware]] — Storage infrastructure layers (L0-L3)
- [[concepts/agent-memory]] — Agent memory design patterns
- [[concepts/harness-engineering]] — The harness layer where Mem0 plugs in
- [[concepts/context-engineering]] — Context management philosophy

## Community

- **Website**: https://mem0.ai
- **Docs**: https://docs.mem0.ai
- **GitHub**: https://github.com/mem0ai/mem0
- **X/Twitter**: @mem0ai

## Sources

- [What OpenClaw and Hermes Agent Reveal About Agent Memory](https://x.com/i/article/2059652660022910976) — May 2026, "In Context" blog
- [[raw/articles/2026-05-27_mem0-openclaw-hermes-agent-memory.md]]
