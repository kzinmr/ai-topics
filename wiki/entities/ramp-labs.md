---
title: "Ramp"
type: entity
aliases: [ramp-labs, ramp-builders, ramp-fintech]
tags: [entity, company, ai-agents, fintech, coding-agents, multi-agent, kv-cache]
status: complete
description: "Financial technology company with an AI research division (Ramp Labs). Creator of Inspect — a background coding agent handling ~30% of merged PRs. Also known for Latent Briefing research."
created: 2026-04-27
updated: 2026-04-30
sources: [
  "https://x.com/RampLabs/status/2042660310851449223",
  "https://builders.ramp.com/post/why-we-built-our-background-agent"
]
related: [
  "[[concepts/latent-briefing]]",
  "[[concepts/kv-cache-compaction]]",
  "[[concepts/multi-agent-systems]]",
  "[[concepts/recursive-language-models]]",
  "[[concepts/background-coding-agent]]",
  "[[concepts/modal-sandboxes]]",
  "[[entities/inspect]]"
]
---

# Ramp

**Ramp** is a financial technology company with two distinct engineering tracks:

1. **Ramp Labs** — AI research division focused on multi-agent system efficiency and KV cache optimization
2. **Ramp Builders** — Engineering team that develops internal AI tooling, including the **Inspect** background coding agent

---

## Ramp Labs: AI Research

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

## Ramp Builders: Inspect Background Agent

**Inspect** is Ramp's custom background coding agent, handling ~30% of all merged pull requests.

### Architecture
- Built on **Modal Sandboxes** for near-instant scaling
- Uses **OpenCode** as the agent framework (server-first, typed SDK, open-source)
- **Cloudflare Durable Objects** for per-session SQLite state
- **Cloudflare Agents SDK** for real-time streaming + WebSocket hibernation

### Key Features
- Full developer tool access (Postgres, Sentry, Datadog)
- Multiplayer support — shareable sessions for collaborative review
- Three client interfaces: Slack Bot, Web (code-server), Chrome Extension
- Pre-warmed environments (starts while user types)
- GitHub OAuth for PR creation (user's token, not app bot)

### Client Interfaces
1. **Slack Bot** — Auto-classification, public channel virality, Block Kit updates
2. **Web Interface** — Hosted VS Code, streamed desktop for visual verification, merge rate tracking
3. **Chrome Extension** — Visual editing for non-engineers, DOM/React internals extraction

## Research Approach

Ramp Labs focuses on **efficiency as a first-order concern** in agent system design. Rather than optimizing intelligence per token within individual agents, they examine how efficiently tokens are used across agents in the system as a whole.

## Hiring

Ramp Labs is hiring across roles (as noted in their Latent Briefing article).

## Related
- [[concepts/latent-briefing]] — Their flagship research
- [[concepts/kv-cache-compaction]] — The underlying technique
- [[concepts/multi-agent-systems]] — Domain of application
- [[concepts/recursive-language-models]] — RLM framework used for evaluation
