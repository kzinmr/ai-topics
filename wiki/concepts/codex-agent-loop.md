---
title: "Codex Agent Loop"
created: 2026-05-27
updated: 2026-05-27
type: concept
status: complete
tags:
  - codex
  - openai
  - coding-agents
  - agent-loop
  - developer-tooling
  - prompt-caching
aliases:
  - codex-agent-loop
  - Codex harness
related:
  - concepts/codex-app-server
  - concepts/codex-goal
  - concepts/codex-prompting
  - entities/openai-codex
  - concepts/mcp
sources:
  - raw/articles/2026-01-23_openai-unrolling-the-codex-agent-loop.md
---

# Codex Agent Loop

The **agent loop** (a.k.a. the **Codex harness**) is the central orchestration logic inside Codex CLI that drives all interactions between the user, the language model, and tools. It is the shared engine powering every Codex surface — CLI, VS Code extension, macOS desktop app, web app, and partner IDEs — through the [[concepts/codex-app-server|App Server]].

---

## The Loop

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  User    │ ──→ │  Model   │ ──→ │  Tool    │
│  Input   │     │ Inference│     │  Call?   │
└──────────┘     └──────────┘     └────┬─────┘
                                       │ Yes
                                  ┌────▼─────┐
                                  │ Execute   │
                                  │ Tool      │
                                  └────┬─────┘
                                       │
                                  ┌────▼─────┐
                                  │ Append    │
                                  │ Output    │──→ back to Model Inference
                                  └──────────┘
                                       │ No (assistant message)
                                  ┌────▼─────┐
                                  │ Turn End  │
                                  └──────────┘
```

1. User input is assembled into a structured prompt
2. Model inference via OpenAI **Responses API**
3. Model outputs either: **final assistant message** (turn ends) or **tool call request**
4. If tool call: agent executes it in a sandbox, appends output to prompt, re-queries model
5. Loop repeats until model emits no more tool calls

The loop is **fully stateless**: every API call sends the complete conversation history. Codex does NOT use `previous_response_id` — this choice simplifies provider architecture and enables Zero Data Retention compliance.

---

## Prompt Assembly

Each Responses API request is built from three main components, ordered for maximum cache efficiency:

### 1. `instructions` (system message)
Sourced from either `model_instructions_file` in `~/.codex/config.toml` or base instructions bundled with the model (e.g., `gpt-5.2-codex_prompt.md`). Highest priority.

### 2. `tools`
Functions the model can call. Codex includes:
- **Shell tool** — spawned local processes (sandboxed)
- **`update_plan`** — built-in task planning
- **`web_search`** — API-provided (cached by default, configurable to live)
- **MCP server tools** — user-configured custom tools, enumerated deterministically

### 3. `input` (ordered list)
The conversation history and immediate context, assembled in this exact order:

| Order | Content | Role | Purpose |
|-------|---------|------|---------|
| 1 | Sandbox permissions | `developer` | File/network limits, approval policy, writable folders |
| 2 | Developer instructions | `developer` | From user's `config.toml` |
| 3 | Skills context | `user` | Preamble + metadata for configured skills |
| 4 | Environment context | `user` | Current working directory, shell type |
| 5 | **User's actual message** | `user` | Appended last |

### Role Hierarchy (decreasing weight)
```
system > developer > user > assistant
```

The `system` role is **server-controlled** — clients cannot override it. This gives the API provider a safety backstop.

---

## Prompt Caching Strategy

Prompt caching is the critical performance optimization that makes the agent loop viable over long conversations.

### The Prefix Matching Constraint

The Responses API caches computation based on **exact prefix matches** between requests. If a new prompt's beginning matches a previously cached prompt exactly, only the new suffix needs processing.

Codex exploits this with an **append-only discipline**:

- All **static content** (instructions, tools, developer messages) is placed first
- **Variable content** (user message, tool outputs, environment) is appended last
- New turns only **add** items — never modify, insert, or reorder earlier messages

This makes sampling cost **linear** (not quadratic) over the conversation.

### Cache Miss Triggers

| Trigger | Why it breaks the prefix |
|---------|------------------------|
| MCP tool list changes | `tools/list_changed` notification reorders tools → prefix no longer matches |
| Model switch | Different model → different model-specific instructions → prefix mismatch |
| Sandbox config change | Modified permissions in earlier messages → prefix not identical |
| Working directory change | New cwd alters environment context → prefix mismatch |

**Mitigation**: When environment changes are needed, Codex appends a new developer message with updated info instead of rewriting the original.

---

## Context Window Management

Long agent sessions with many tool calls risk **context window exhaustion** — the prompt exceeds the model's maximum token limit.

### Automatic Compaction

When token count exceeds `auto_compact_limit` (configurable threshold), Codex calls the **`/responses/compact`** endpoint:

```
Full conversation (N turns)
        │
        ▼
/responses/compact endpoint
        │
        ▼
Compacted representation
  ├─ type=compaction item with encrypted_content
  └─ preserves model's latent understanding
```

The compacted block **replaces** the original history, freeing context window space while maintaining conversation continuity. The `encrypted_content` is opaque to clients — only the model can interpret it.

**Historical note**: Earlier Codex versions required users to manually run `/compact`. The current automatic compaction was a key UX improvement.

---

## Stateless Design Decision

Codex deliberately chose **not** to use the Responses API's `previous_response_id` parameter:

> *"Codex does not use an optional 'previous_response_id' parameter that would allow the API to reference stored conversation state ... every request is fully stateless."* — Ars Technica summary

### Rationale

| Approach | Pros | Cons |
|----------|------|------|
| `previous_response_id` (stateful) | Smaller requests, server-managed history | Server must store data; ZDR incompatible; provider lock-in |
| Full history each time (stateless) | ZDR-friendly; provider-agnostic; explicit control | Larger requests; quadratic prompt growth; relies on caching |

Codex chose stateless to support **Zero Data Retention** customers and simplify multi-provider architecture. Prompt caching mitigates the performance cost.

---

## Relationship to App Server

The agent loop is the **what** — the orchestration logic. The App Server is the **how** — the protocol that exposes this loop to remote clients:

```
┌──────────────────────────────────────────┐
│              App Server                   │
│  (JSON-RPC: Thread → Turn → Item)        │
│                                           │
│  ┌────────────────────────────────────┐  │
│  │        Codex Core (Harness)        │  │
│  │  ┌──────────────────────────────┐  │  │
│  │  │      Agent Loop              │  │  │
│  │  │  User→Model→Tool→Repeat      │  │  │
│  │  └──────────────────────────────┘  │  │
│  └────────────────────────────────────┘  │
└──────────────────────────────────────────┘
```

The App Server's `item/*` notifications (streaming agent output) and `turn/*` lifecycle events are direct manifestations of the agent loop's state transitions.

---

## Key Takeaways

1. **The loop is deceptively simple** — user → model → tool → repeat — but the engineering around it (prompt construction, caching, compaction) is where the complexity lives.
2. **Stateless by choice** — every call carries full history. This is a tradeoff: simpler architecture but requires caching and compaction to be practical.
3. **Append-only prompt discipline** — the most important rule for cache performance. Never modify earlier messages; always append.
4. **Automatic compaction is essential** — without it, long agent sessions inevitably hit the context window limit.
5. **MCP integration is fragile** — tool ordering must be deterministic; `tools/list_changed` notifications can silently break caching.

---

## Bugs & Hard-Earned Lessons

From the engineering team's notes:

- **MCP tool enumeration ordering**: Initially non-deterministic, causing intermittent cache invalidation. Fixed by enforcing a stable sort order.
- **Tool call accumulation**: Early versions could accumulate tool calls without checking remaining context window, causing mid-turn failures. Fixed by proactive token budgeting before each tool execution.
- **Developer instructions truncation**: Bad truncation of developer instructions when combined with long skill metadata caused cryptic model behavior.
