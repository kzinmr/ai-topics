---
title: agentmemory
created: 2026-05-18
updated: 2026-05-18
type: entity
entity_type: tool
tags:
  - memory-systems
  - coding-agents
  - ai-agents
  - harness-engineering
  - architecture
  - open-source
  - mcp
  - bm25
sources:
  - https://github.com/rohitg00/agentmemory
  - https://alphasignalai.substack.com/p/how-agentmemory-works-and-how-to
  - raw/articles/2026-05-18_agentmemory-persistent-memory-for-coding-agents.md
aliases:
  - "@agentmemory/agentmemory"
  - agent-memory
---

# agentmemory

**agentmemory** is a persistent memory system for AI coding agents, built on the [[entities/iii-platform|iii engine]]'s three primitives (Function, Trigger, Worker). It silently captures every tool-use action an agent takes, compresses observations into searchable memory, and injects the most relevant context into future sessions — eliminating the need to re-explain architecture, bugs, and preferences across sessions.

- **GitHub**: [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) — 12K+ stars, Apache-2.0
- **Creator**: Rohit Ghumare (rohitg00), top contributor to iii-hq/iii
- **Language**: TypeScript (81.4%), ~21,800 LOC, 800 tests, 123 functions
- **npm**: `@agentmemory/agentmemory` (v0.9.18)
- **Homepage**: [agent-memory.dev](https://agent-memory.dev) / [agentmemory.space](https://agentmemory.space)

> "The gist extends Karpathy's LLM Wiki pattern with confidence scoring, lifecycle, knowledge graphs, and hybrid search: agentmemory is the implementation."

## Architecture

agentmemory is structured as three layers — Capture, Pipeline, Retrieval — plus a consolidation cycle that compresses raw observations into longer-term memory tiers.

### Capture Layer

Twelve Claude Code lifecycle hooks fire automatically with **zero manual `add()` calls**:

| Hook | Fires When |
|------|-----------|
| `SessionStart` | New agent session begins |
| `UserPromptSubmit` | User sends a prompt |
| `PreToolUse` | Before a tool is invoked |
| `PostToolUse` | After a tool completes |
| `PostToolUseFailure` | Tool invocation fails |
| `PreCompact` | Before context compaction |
| `SubagentStart` | Subagent spawns |
| `SubagentStop` | Subagent finishes |
| `Notification` | System notification |
| `TaskCompleted` | Task marked complete |
| `Stop` | Agent stops processing |
| `SessionEnd` | Session terminates |

Each hook is a standalone Node script that reads JSON from stdin, POSTs to `localhost:3111`, and exits. Non-Claude agents capture via `memory_save` MCP tool or `/agentmemory/observe` REST endpoint.

### Pipeline Layer

Every observation passes through four stages:

1. **SHA-256 dedup** — Anything repeating within 5 minutes is skipped
2. **Privacy filter** (`src/functions/privacy.ts`) — Strips API keys, bearer tokens, GitHub tokens, AWS keys, Google keys, JWTs, npm tokens, GitLab tokens, DigitalOcean keys
3. **BM25 indexing** — Always-on synthetic path: indexes observation in BM25 without calling any LLM
4. **LLM compression** (optional) — If `AGENTMEMORY_AUTO_COMPRESS=true`, a configured provider (Anthropic, MiniMax, Gemini, OpenRouter) compresses observations into structured facts. **Off by default since v0.8.8** due to per-token cost on active sessions.

### Retrieval Layer

Three parallel streams in `src/state/hybrid-search.ts`:

| Stream | Method | Details |
|--------|--------|---------|
| **BM25** | Lexical | Porter stemming, synonym expansion, always runs |
| **Vector** | Cosine similarity | all-MiniLM-L6-v2 384-dim embeddings (free local via `@xenova/transformers`, or hosted via Gemini/OpenAI/Voyage/Cohere/OpenRouter) |
| **Graph** | Entity-relationship | Knowledge graph traversal across sessions |

Results are fused with **Reciprocal Rank Fusion (k=60)** and diversified (max 3 results per session) to prevent noise dominance from a single session.

### 4-Tier Memory Consolidation

Memories progress through four tiers, analogous to sleep consolidation:

| Tier | Content | Lifecycle |
|------|---------|-----------|
| **Working** | Raw observations | Short-lived, high-volume |
| **Episodic** | Compressed session summaries | Mid-term, synthesized |
| **Semantic** | Extracted facts and patterns | Long-term, generalizable |
| **Procedural** | Workflows and decision patterns | Persistent, reusable |

Memories decay on an **Ebbinghaus-style forgetting curve**. Frequently accessed memories strengthen; stale ones auto-evict. Contradictions are detected and resolved on write, with provenance traces linking back to source observations.

### Context Assembly

When a new session starts, `mem::context` assembles:

- Pinned memory slots
- Project profile
- Recent session summaries (last 3–5 sessions)
- High-importance observations (access frequency × recency)

Default budget: **2,000 tokens**. **SessionStart context injection is OFF by default** (`AGENTMEMORY_INJECT_CONTEXT=false` since v0.8.10). Token efficiency: ~1,900 tokens/session, ~170K tokens/year, **~$10/year** (or **$0** with local embeddings).

## Performance

### LongMemEval-S (ICLR 2025)

| System | R@5 | R@10 | MRR |
|--------|-----|------|-----|
| **agentmemory** | **95.2%** | **98.6%** | **88.2%** |
| BM25-only fallback | 86.2% | 94.6% | 71.5% |

### Competitor Comparison

| | agentmemory | mem0 (53K ⭐) | Letta/MemGPT (22K ⭐) | Built-in (CLAUDE.md) |
|---|---|---|---|---|
| **Type** | Memory engine + MCP server | Memory API layer | Full agent runtime | Static file |
| **Retrieval R@5** | 95.2% | 68.5% | 83.2% | N/A (grep) |
| **Capture** | 12 hooks (zero manual) | Manual `add()` calls | Agent self-edits | Manual editing |
| **Search** | BM25 + Vector + Graph (RRF) | Vector + Graph | Vector (archival) | Loads all into context |
| **Multi-agent** | MCP + REST + leases + signals | API (no coordination) | Letta runtime only | Per-agent files |
| **External deps** | None (SQLite + iii-engine) | Qdrant / pgvector | Postgres + vector DB | None |
| **Memory lifecycle** | 4-tier consolidation + decay + auto-forget | Passive extraction | Agent-managed | Manual pruning |
| **Token efficiency** | ~1,900 tokens/session ($10/yr) | Varies | Core memory in context | 22K+ at 240 obs |
| **Self-hosted** | Yes (default) | Optional | Optional | Yes |

## Integration

### Agent Support Matrix

| Agent | Integration Method | Hooks |
|-------|-------------------|-------|
| **Claude Code** | Plugin marketplace → `/plugin install agentmemory` | 12 hooks + MCP auto-wired |
| **Codex CLI** | `codex plugin install agentmemory` | 6 hooks + MCP |
| **Cursor** | MCP config (`~/.cursor/mcp.json`) | MCP tools |
| **Cline / Roo Code / Windsurf** | MCP config block | MCP tools |
| **Gemini CLI** | `gemini mcp add agentmemory ...` | MCP tools |
| **Hermes** | `~/.hermes/config.yaml` → `memory.provider: agentmemory` | Full guide in repo |
| **OpenClaw** | MCP config or deeper memory plugin | `integrations/openclaw/` |
| **pi** | Copy `integrations/pi` to extensions folder | MCP tools |
| **OpenCode** | `opencode.json` with `mcp` key | MCP tools |
| **Aider** | REST API directly | No MCP needed |

**Universal MCP config** (merge into existing `mcpServers`):
```json
{
  "mcpServers": {
    "agentmemory": {
      "command": "npx",
      "args": ["-y", "@agentmemory/mcp"],
      "env": { "AGENTMEMORY_URL": "http://localhost:3111" }
    }
  }
}
```

### MCP Tool Surface

51 MCP tools total (7 visible by default; `AGENTMEMORY_TOOLS=all` exposes all 51):
- **Core**: `memory_save`, `memory_recall`, `memory_smart_search`, `memory_sessions`, `memory_export`, `memory_audit`, `memory_governance_delete`
- **Extended**: `memory_file_history`, `memory_profile`, `memory_graph_query`, `memory_team_share`, `memory_lease`, `memory_signal_send`, `memory_mesh_sync`

4 slash commands: `/recall`, `/remember`, `/session-history`, `/forget`

### Programmatic Access

All core operations are iii functions (`mem::remember`, `mem::observe`, `mem::context`, `mem::smart-search`, `mem::forget`). Any language with an iii SDK can call them over `ws://localhost:49134`.

```python
from iii import register_worker
iii = register_worker("ws://localhost:49134")
iii.connect()
iii.trigger({"function_id": "mem::smart-search", "payload": {"project": "demo", "query": "how do tokens refresh"}})
```

## Technical Stack

agentmemory is **already a running iii instance**. It does not depend on Express, Postgres, Redis, pm2, or Prometheus — iii-engine replaces them all:

| Traditional Stack | agentmemory Equivalent |
|---|---|
| Express.js / Fastify | iii HTTP Triggers |
| SQLite / Postgres + pgvector | iii KV State + in-memory vector index |
| SSE / Socket.io | iii Streams (WebSocket) |
| pm2 / systemd | iii-engine worker management |
| Prometheus / Grafana | iii OTEL + health monitor |

- **Engine**: iii-sdk (WebSocket to iii-engine on port 49134)
- **State**: File-based SQLite via iii-engine's StateModule (`./data/state_store.db`)
- **Build**: TypeScript → ESM via tsdown
- **Test**: vitest (800 tests, ~1.7s)
- **REST**: Port 3111, Streams: Port 3112, Viewer: Port 3113
- **Pricing**: Solo (private), Team ($20/mo), Enterprise (custom)

## Relationship to iii Platform

agentmemory is the most prominent application built on iii-engine, demonstrating that a non-trivial backend service (memory engine, REST API, WebSocket streams, MCP server, observability, viewer) can be built entirely from iii primitives with **no external dependencies** beyond SQLite. It validates the iii thesis: "the harness IS the backend."

## Related

- [[entities/iii-platform]] — The iii engine agentmemory is built on
- [[concepts/bm25]] — BM25 lexical retrieval used in the hybrid search pipeline
- [[concepts/embeddings]] — Vector embeddings for semantic similarity search
- [[concepts/vector-search]] — Dense vector retrieval component
- [[concepts/agent-harness]] — Agent harness concept (agentmemory is a memory layer for harnesses)
- [[concepts/agent-memory]] — Agent memory systems overview
