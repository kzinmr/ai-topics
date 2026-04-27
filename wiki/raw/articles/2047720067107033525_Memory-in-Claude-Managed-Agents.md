# Memory in Claude Managed Agents

**Source:** [X/Twitter — @RLanceMartin (Lance Martin)](https://x.com/RLanceMartin/status/2047720067107033525)
**Date:** April 27, 2026
**Type:** X Native Article

## Article Content

Claude Managed Agents now has memory! It's stored as files and accessible across sessions. Multiple agents can access the same memory store with real-time sync.

This is a major capability for Claude Managed Agents — persistent, sharable memory that survives across sessions and can be shared across multiple agents working on the same task.

### Memory Implementation Details

- Memory stored as files in `/mnt/memory/<store-name>/` in agent containers
- Multiple agents can access the same memory store
- Real-time synchronization between agents
- Concurrency handling: prevents agents from overwriting each other's updates
- Memories can be exported via the API
- Files are interpretable and sharable

### Claude Plays Pokémon — Scaling Validation

DavidSHershey's Claude Plays Pokémon experiment demonstrated filesystem-as-memory with different model generations:

| Model | Files | Organization | Progress |
|-------|-------|-------------|----------|
| Sonnet 3.5 | 31 files | Transcript-style (NPC dialogue) | Stuck in second town |
| Opus 4.6 | 10 files | Directory-organized, gym badges, learnings | Significant progress |

As models scale, they learn to organize memory more efficiently — fewer files, better structure, distilled learnings from failures.

### Memory Store Concepts

**Memory stores** are workspace-scoped collections of text documents. They're:
- Mounted in agent containers at `/mnt/memory/<store-name>/`
- Injected into the system prompt automatically
- Synced in real-time across multiple agents
- Exposable via API for external tools

### Filesystem vs Specialized Memory Tools

The article compares different approaches:
- **Filesystem-based** (Claude Managed Agents) — general tools, flexible, interpretable
- **CoALA** (tedsumers) — cognitive science-inspired memory layer
- **memGPT** (sarahwooders, charlespacker) — OS-style context management
- **Custom memory APIs** — specialized database approaches

### Context Model

The article also describes Claude's context model:
- **Session log** — the running conversation history
- **Memory store** — persistent files accessed via tools
- Combined, they form the agent's working memory

---

*This article was fetched from X/Twitter using the xurl CLI. The article body was extracted from tweet 2047720067107033525.*
