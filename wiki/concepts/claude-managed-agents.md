---
title: "Claude Managed Agents"
type: concept
created: 2026-04-27
updated: 2026-04-27
tags: [anthropic, managed-agents, memory-stores, file-system-memory, multi-agent-sync]
aliases: [claude-managed-agents, claude-platform-agents]
related: [[entities/anthropic]], [[agent-memory]], [[concepts/filesystem-memory]]
---

# Claude Managed Agents

**Claude Managed Agents** is Anthropic's enterprise-grade AI agent platform available on the Claude Platform. Agents run continuously with governance, observability, and guardrails.

## Architecture

### Session Log + Memory Store

Managed Agents use a two-component context model:

1. **Session log** — Claude fetches and transforms session context over the course of a task. The session lives outside the context window, with benefits outlined by [a1zhang](https://x.com/a1zhang) and [lateinteraction](https://x.com/lateinteraction).

2. **Memory store** — Persistent, workspace-scoped collections of text documents that outlive any single session. Claude can write files to persist context across sessions.

## Memory Stores

### How They Work

- Memory stores are mounted into the agent container as directories at `/mnt/memory/<store-name>/`
- A short note about the mount is automatically injected into the system prompt
- Multiple agents can access the same memory store simultaneously
- Real-time sync: edits by one agent are reflected in all other agents' filesystems
- Concurrency handling prevents agents from overwriting each other's memory updates

### Benefits

- **Files are interpretable and sharable** — memory folders can be downloaded and shared externally
- **Export via API** — memories can be exported programmatically
- **Cross-session learning** — agents learn from experience across sessions
- **General tooling** — Claude uses standard file tools (read/write/create/delete) rather than specialized memory APIs

## Scaling Intelligence for Memory

The filesystem-as-memory approach was validated through [DavidSHershey's Claude Plays Pokémon experiment](https://x.com/DavidSHershey):

| Model | Step Count | Memory Files | Organization | Progress |
|-------|-----------|--------------|-------------|----------|
| Sonnet 3.5 | 14,000 | 31 files | Transcript-style (NPC dialogue) | Stuck in second town |
| Opus 4.6 | 14,000 | 10 files | Directory-organized, gym badges, learnings file | Significant progress |

Later models learned to use the filesystem to organize memory much better, demonstrating that with scaling intelligence, general file management tools are sufficient — Claude learns what to save and how to organize its own memories.

## Related Approaches

Several research projects have explored specialized memory tools for agents:
- **CoALA** (tedsumers) — cognitive science-inspired memory management
- **memGPT** (sarahwooders, charlespacker) — operating system models for agent memory
- **Letta.AI** — filesystem-based memory that outperforms specialized tools

The trend shows that general tools (filesystem) with scaling intelligence can match or exceed specialized memory tooling.

## Public Beta Launch (Apr 2026)

Anthropic launched Managed Agents in **public beta** in April 2026, marking the transition from private/preview to generally available platform feature:
- **Platform-level agent orchestration**: Complete execution environment with built-in monitoring, audit trails, and security controls
- **Brain/Hands/Session separation**: Architectural pattern where planning (Brain), execution (Hands), and context management (Session) are independently managed components
- **Enterprise-ready**: Designed for production workloads with governance and compliance features
- **MCP Integration**: Full Model Context Protocol support for external tool integration

This represents a significant shift toward **platform-provided agent infrastructure** rather than developers building custom harnesses. Compare with OpenAI's Symphony approach.

## Getting Started

- [Claude Managed Agents docs](https://docs.anthropic.com)
- Use the `claude-api` skill (built into Claude Code, triggered by `/claude-api`)

## Sources

- [Memory in Claude Managed Agents](https://x.com/RLanceMartin/status/2047720067107033525) — Lance Martin (@RLanceMartin), April 2026
- [Claude Plays Pokémon](https://x.com/DavidSHershey) — David Hershey's memory experiment
- [Anthropic Managed Agents announcement](https://www.anthropic.com/managed-agents) — Jaya Gupta analysis
