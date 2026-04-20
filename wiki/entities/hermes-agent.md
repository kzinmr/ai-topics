---
title: "Hermes Agent Architecture"
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [ai-agents, open-source-ai, tooling, framework]
aliases: ["Hermes Agent", "nousresearch/hermes-agent"]
sources:
  - https://hermes-agent.nousresearch.com/docs/developer-guide/architecture/
  - https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop/
  - https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly/
  - https://github.com/NousResearch/hermes-agent
---

# Hermes Agent Architecture

**Overview:** An integrated agent execution platform built around `AIAgent` core, with persistent state, prompt assembly, tool runtime, gateway, and plugin/memory provider layers.

**Creator:** [[teknium]] (Ryan Lopopolo), Nous Research Co-founder & Head of Post-Training
**GitHub:** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) (68,000+ stars as of April 2026)
**Version:** v0.9.0 (April 2026)
**Documentation:** [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)

## Architecture Layers

```
Input Surface (CLI / Gateway / ACP / Cron / Batch)
    ↓
Execution Core (`run_agent.py` → `AIAgent`)
    ↓
Support Layer (Prompt Builder / Provider Resolver / Tool Registry / Compression / Memory-Session)
    ↓
External Connections (Terminal Backends / Platform Adapters / MCP / Plugins)
```

## 1. Core: `AIAgent`

The architectural center of Hermes. The `AIAgent` class in `run_agent.py` consolidates:

- **Effective prompt assembly** — constructs structured system prompts from multiple sources
- **Provider/API mode selection** — supports `chat_completions`, `codex_responses`, `anthropic_messages` modes
- **Interruptible LLM calls** — can pause/abort execution on new user input mid-flight
- **Tool execution** — sequential for single/interactive tools, parallel for non-interactive tools
- **Session history management**
- **Compression / retry / fallback model handling**

### API Execution Modes

| Mode | Description |
|------|-------------|
| `chat_completions` | Standard OpenAI-compatible API |
| `codex_responses` | OpenAI Codex CLI agent interface |
| `anthropic_messages` | Anthropic Messages API |

### Callback Surface

UI and integrations attach via callbacks:
- `tool_progress_callback` — tool execution progress
- `thinking_callback` — model thinking/reasoning output
- `clarify_callback` — user clarification requests
- `stream_delta_callback` — streaming response deltas

### Key Design Decisions

- **Shared iteration budget** between parent and child agents with budget pressure hints
- **Fallback model** support — switches to alternate provider/model on specific failure paths (main agent loop only, not subagent delegation/cron/auxiliary tasks)

## 2. Single-Turn Execution Flow

1. Append user message to history
2. Preflight compression (if needed)
3. Load or construct cached system prompt
4. Build API messages, inject ephemeral layers
5. Apply prompt caching → LLM call
6. If tool call: execute → append result to history → loop
7. If final text: save session → return response

## 3. Prompt Assembly

Hermes separates **cached system prompt** (persistent across turns) from **ephemeral additions** (injected only at API call time).

### Cached System Prompt Assembly Order

1. `SOUL.md` — agent identity
2. Tool-aware behavior guidance
3. Honcho static block
4. Optional system message
5. Frozen MEMORY snapshot
6. Frozen USER snapshot
7. Skills index
8. Context files (`.hermes.md` / `AGENTS.md` / `CLAUDE.md` / `.cursorrules` — priority first-match)
9. Timestamp / optional session ID
10. Platform hint

### Design Principles

- **Mid-session stability:** Memory and context files are frozen after session start. Changes via `memory` tool don't affect the current prompt — preserves provider-side prompt cache.
- **Prompt caching:** Anthropic native and Claude-via-OpenRouter cache system prompt + last 3 non-system messages (TTL: 5 min default).
- **Stable prefix:** Long conversations use context compression while keeping the stable prefix unchanged.

## 4. Persistent State: Sessions, Memory, Search

### Two-Tier Persistence

| Tier | Storage | Contents |
|------|---------|----------|
| Primary | `~/.hermes/state.db` (SQLite + FTS5) | Session ID, platform source, user ID, title, model, system prompt snapshot, full message history, token counts, timestamps, parent session ID |
| Archive | `~/.hermes/sessions/` (JSONL) | Raw conversation transcripts |

### `session_search` Tool

Full-text search (FTS5) across past sessions:
1. Find relevant messages via FTS5
2. Summarize top matching sessions
3. Extract and analyze target conversations

This creates a **bounded memory + searchable transcript archive** dual-layer design.

### Memory System

| File | Purpose |
|------|---------|
| `~/.hermes/memories/MEMORY.md` | Environment facts, conventions, learned procedures, tool quirks |
| `~/.hermes/memories/USER.md` | User preferences, communication style, pet peeves |

**Bounded store** with character limits. Only durable facts that matter across sessions are retained.

### External Memory Providers

Pluggable memory backends (Honcho, RetainDB, ByteRover). Built-in memory always remains active; external provider is single-select addition. Capabilities:
- Pre-turn prefetch
- Post-turn sync
- Session-end extraction
- Provider-specific tools

### Compression & Session Lineage

After compression:
- Middle turns are summarized for lighter context
- Parent session ID preserved in database
- Maintains both "lightweight active session" and "searchable ancestor history"

## 5. Tool Runtime: Self-Registering Registry

### Architecture

```
Tool Module (import-time registry.register())
    ↓
model_tools.py (AST discovery of registry.register() calls)
    ↓
MCP Tools + Plugin Tools (additional discovery)
    ↓
Tool Execution (pre-hook → dispatch → post-hook)
```

**Self-registering:** New built-in tools require no manual central list update — just include `registry.register()` at module level.

### Toolsets

| Toolset | Purpose |
|---------|---------|
| `web` | Web search and extraction |
| `terminal` | Shell command execution |
| `file` | File read/write/search/patch |
| `browser` | Web page interaction |
| `vision` | Image analysis |
| `image_gen` | Image generation |
| `skills` | Skill loading and management |
| `memory` | Persistent memory operations |
| `session_search` | Past conversation search |
| `cronjob` | Scheduled task management |
| `code_execution` | Sandboxed Python execution |
| `delegation` | Subagent spawning |
| `clarify` | User clarification dialogs |
| `MCP` | Model Context Protocol servers |

Toolsets can be enabled/disabled by platform preset. `check_fn` determines availability based on API keys or binary presence.

### Execution Flow

```
Model response → model_tools.handle_function_call()
    → plugin pre-hook
    → registry dispatch
    → plugin post-hook
```

**Special cases:** `todo`, `memory`, `session_search`, `delegate_task` bypass the registry — handled directly in agent loop due to agent-level state requirements.

### Safety: Terminal Approval

- `DANGEROUS_PATTERNS` detection
- CLI/Gateway approval prompts
- Session-level approval state
- Persistent allowlist
- Optional smart approval
- Multiple terminal backends: local, docker, ssh, singularity, modal, daytona

## 6. Subagent Delegation vs `execute_code`

### `delegate_task`

| Property | Value |
|----------|-------|
| Purpose | Reasoning-heavy subtasks requiring independent agent judgment |
| Isolation | Complete — fresh conversation, separate terminal, restricted toolsets |
| Context | Child knows nothing of parent conversation — only `goal` + `context` |
| Return | Final summary only |
| Parallelism | Up to 3 concurrent children |
| Restrictions | No recursive delegation, no memory writes |

### `execute_code`

| Property | Value |
|----------|-------|
| Purpose | Mechanical multi-step pipelines in a single turn |
| Isolation | Sandboxed — temporary directory, process group, no dangerous env vars |
| Context | Python script runs via `hermes_tools.py` stub, RPC calls back to parent |
| Return | `print()` output only |
| Communication | Unix domain socket for tool call results |

### When to Use Which

| Scenario | Use |
|----------|-----|
| Needs reasoning, decision-making, multi-step judgment | `delegate_task` |
| Loop/filter/process large data mechanically | `execute_code` |
| Parallel independent workstreams | `delegate_task` (up to 3) |
| Single-turn data transformation | `execute_code` |

## 7. Gateway: Persistent Frontend Layer

### Architecture

```
GatewayRunner
    ├── Platform Adapters (14+ messaging platforms)
    ├── MessageEvent normalization
    ├── Session key resolution
    ├── Slash command dispatch
    └── AIAgent instantiation (as needed)
```

The gateway is not an alternative to the agent core — it's the **persistent orchestration layer connecting AIAgent to the messaging world**.

### Message Flow

- **Two-level message guard** (adapter + runner)
- New input to running session → queued + interrupt event raised
- `/approve`, `/deny` commands → inline dispatch bypass
- Session key resolution, authorization, running-agent guard, DM pairing

### Background Maintenance

- Cron ticking
- Session expiry handling
- Memory flush
- Cache refresh

### Hooks

- Location: `~/.hermes/hooks/` (`HOOK.yaml` + `handler.py`)
- Types: `pre_tool_call`, `post_tool_call`, `pre_llm_call`, `post_llm_call`, `on_session_start`, `on_session_end`
- Non-blocking — hook failures don't crash the agent
- Work in both CLI and gateway modes

## 8. Provider Runtime

### Resolution Priority

```
Explicit override > config.yaml > environment variables > provider defaults/auto
```

### Auxiliary Tasks

Independent provider/model/base_url for:
- Vision processing
- Web extraction summarization
- Compression
- Session search
- Skills hub
- MCP helper
- Memory flush

### Fallback Behavior

- Triggers on auth failure or retry exhaustion
- One-time in-place runtime switch
- **Limited to main agent loop** — doesn't apply to subagent delegation, cron, or auxiliary tasks

## 9. Extension Model: Plugins

### Plugin Types

| Type | Purpose |
|------|---------|
| General plugins | Add tools, hooks, slash commands, CLI commands, skills, message injection |
| Memory providers | External memory backends (Honcho, RetainDB, ByteRover) |
| Context engines | Alternative compression/context processing |

### Discovery

| Location | Default State |
|----------|--------------|
| `~/.hermes/plugins/` | Enabled |
| Project-local `.hermes/plugins/` | Disabled (trust-on-enable) |
| pip entry points | Enabled |

### Plugin Hooks

`pre_tool_call`, `post_tool_call`, `pre_llm_call`, `post_llm_call`, `on_session_start`, `on_session_end` — trusted code that can intercept and modify agent loop behavior.

## 10. Architectural Characteristics

1. **AIAgent-centric design** — All orchestration converges on one core. Gateway/CLI are frontends, not alternatives.
2. **Prompt-cache-aware state** — Frozen memory snapshots, ephemeral layer separation, stable prefix preservation. Cache stability is a first-class architectural constraint.
3. **Three-tier memory** — Built-in bounded memory, searchable session archive, optional external memory provider. Separates durable facts from conversation history.
4. **Execution primitive separation** — Distinct primitives for normal tool loops, subagent delegation, code execution, cron, and gateway delivery — each with different token costs and isolation philosophies.

## Design Tradeoffs

| Tradeoff | Impact |
|----------|--------|
| Wide `AIAgent` responsibilities | Easy to understand conceptually, but core implementation complexity is high |
| Memory stability over immediacy | `memory` tool writes don't affect current session prompt — preserves cache, sacrifices real-time consistency |
| Blank-slate subagents | Prevents parent context pollution, but requires careful `goal`/`context` writing |

## Recommended Code Reading Order

1. `run_agent.py` — Core agent implementation
2. `agent/prompt_builder.py` — Prompt assembly logic
3. `agent/context_compressor.py` — Context compression
4. `model_tools.py` / `tools/registry.py` — Tool runtime
5. `hermes_state.py` — State management
6. `gateway/run.py` — Gateway orchestration
7. `gateway/session.py` — Session management

## Skill Self-Improvement Architecture

Hermes Agent employs an **autonomous skill creation loop** that distinguishes it from other agent frameworks:

### Mechanism
- **Prompt Nudge:** System prompt instructs the agent to consider saving a skill every N tool calls
- **Background Review:** After task completion, automated scan identifies skill-worthy patterns
- **Pre-Compression Flush:** Durable knowledge saved to disk before context compression triggers
- **Blunt Dedup Rule:** If an existing skill covers the pattern, patch it in place. Only create new skills if nothing matches.

### Empirical Results
- Ships with **123 bundled SKILL.md files** covering GitHub PR workflows, Obsidian, Google Workspace, Linear, Notion, Typefully, Perplexity, deep research, and more
- Agent creates novel skills autonomously (e.g., `extract-social-testimonial` skill created without developer prompting)
- Tool Gateway integration: One subscription unlocks 300+ models, web scraping, browser automation, image generation, cloud terminal, TTS

### Known Challenge: Skill Explosion Problem
Analysis by elvis (9-hour source code study, April 2026) identified a long-tail failure mode: the agent creates adjacent redundant skills faster than it consolidates them. Example: three separate skills for "image + local filesystem + model can see it" emerged independently. This is tracked as a product prioritization issue — expected resolution involves invocation metrics-based consolidation and stronger creation-time deduplication.

See [[skill-architecture-patterns]] for detailed comparison with OpenClaw's governance model.

## Related Pages

- [[teknium]] — Hermes Agent creator, Nous Research co-founder
- [[harness-engineering/agentic-workflows]] — Agentic Engineering patterns (related design philosophy)
- [[claude-memory]] — File-based memory architecture (comparable design)
- [[harness-engineering]] — Harness Engineering framework (related orchestration concepts)
- [[ai-agent-memory-middleware]] — AI Agent Memory Middleware (complementary memory layer concepts)
- [[skill-architecture-patterns]] — Skill self-improvement vs governed approaches (Hermes vs OpenClaw)

## Sources

- https://hermes-agent.nousresearch.com/docs/developer-guide/architecture/
- https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop/
- https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly/
- https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching/
- https://hermes-agent.nousresearch.com/docs/user-guide/sessions/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers
- https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/tools/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution/
- https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-internals/
- https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks/
- https://github.com/NousResearch/hermes-agent/releases
- Architecture document authored by Kazuki Inamura (2026-04-16)
