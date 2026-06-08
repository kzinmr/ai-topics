---
title: "Hermes Codex App-Server Runtime"
created: 2026-05-27
updated: 2026-05-27
type: concept
status: complete
tags:
  - coding-agents
  - openai
  - architecture
  - ai-agents
  - protocol
aliases:
  - hermes-codex-runtime
  - codex_app_server runtime
related:
  - concepts/codex-app-server
  - concepts/codex-agent-loop
  - comparisons/harness-backend-routing
  - comparisons/codex-app-server-vs-claude-agent-sdk
sources:
  - raw/articles/2026-05-27_hermes-codex-app-server-runtime.md
---

# Hermes Codex App-Server Runtime

**Hermes Agent officially supports Codex App Server as an execution backend.** This is not a hack — it is an opt-in feature built into Hermes' design.

When enabled, `openai/*` and `openai-codex/*` turns are delegated to the **Codex CLI app-server** instead of Hermes' own tool loop. All terminal commands, file edits, sandboxing, and MCP tool calls execute inside Codex's runtime — Hermes becomes the **shell layer** around it (sessions DB, slash commands, gateway, memory & skill review).

> **Why**: Use ChatGPT subscription — no API key required. Codex's toolset and sandbox are used directly.

---

## Architecture: Hermes = Shell, Codex = Engine

```
┌─────────────────────────────────┐          JSON-RPC          ┌──────────────────────────┐
│       Hermes (Shell Layer)      │ ←───────────────────────→ │   Codex App Server       │
│                                 │    Thread/Turn/Item       │                          │
│  - sessions DB                  │                           │  - shell                 │
│  - slash commands (/codex-runtime)│                         │  - apply_patch           │
│  - gateway (Discord/Slack/Telegram)│                        │  - update_plan           │
│  - memory / session_search      │                           │  - view_image            │
│  - skill review                 │                           │  - web_search            │
│  - goal judge (auxiliary client)│                           │  - native plugins        │
│                                 │                           │    (Linear, GitHub,       │
│  ┌───────────────────────────┐  │     MCP server (stdio)    │     Gmail, Calendar...)  │
│  │ Hermes tool callback      │──│────────────────────────→  │                          │
│  │ - web_search (Firecrawl)  │  │   Codex → Hermes tools    │  Subscription flat-fee   │
│  │ - browser automation      │  │                           │                          │
│  │ - vision_analyze          │  │                           └──────────────────────────┘
│  │ - image_generate          │  │
│  │ - skill_view / skills_list│  │
│  │ - text_to_speech          │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

---

## Three Tool Sources

In Codex Runtime mode, the model's available tools come from three independent sources:

### 1. Codex Built-in Tools (always on)
- `shell` — arbitrary commands inside sandbox
- `apply_patch` — structured multi-file diff
- `update_plan` — internal todo/plan tracker (Hermes' `todo` equivalent)
- `view_image` — load local image into conversation
- `web_search` — Codex's built-in search

### 2. Native Codex Plugins (auto-migrated)
Hermes queries Codex's `plugin/list` RPC and enables every installed plugin automatically:
- Linear, GitHub, Gmail, Google Calendar, Outlook, Canva, etc.
- OAuth handled in Codex — Hermes never touches credentials

### 3. Hermes Tool Callback (MCP Server)
Hermes registers itself as an MCP server in `~/.codex/config.toml`. When Codex needs Hermes-only tools, it spawns `hermes_tools_mcp_server` via stdio:
- `web_search` / `web_extract` (Firecrawl-backed)
- Browser automation (Camofox/Browserbase)
- `vision_analyze`, `image_generate`, `text_to_speech`
- `skill_view` / `skills_list`

---

## What's NOT Available

The following Hermes tools are unavailable on Codex Runtime (require the running agent loop context):

| Tool | Reason | Alternative |
|------|--------|-------------|
| `delegate_task` | Needs Hermes' loop for sub-agent spawn | Switch via `/codex-runtime auto` |
| `memory` | Persistent store is on Hermes side | Same |
| `session_search` | Cross-session search | Same |
| `todo` | Hermes' todo | Use Codex's `update_plan` |

---

## Workflow Integration

### `/goal` (Ralph Loop)
- **Works.** Goals persist in `state_meta` keyed by session ID.
- Continuation prompts injected as user messages, Codex executes natively.
- Goal judge runs via **auxiliary client** (runtime-independent).
- Each continuation is a fresh Codex turn — may re-trigger approval prompts for writes.
- Suppress with `default_permissions = ":workspace"`.

### Kanban (Multi-Agent Worktree Dispatch)
- **Works.** If `model.openai_runtime: codex_app_server` is set globally, Kanban workers inherit Codex runtime.
- Worker handoff tools (`kanban_complete`, `kanban_block`, `kanban_comment`, `kanban_heartbeat`) available via callback.
- Sandbox: `workspace-write` + board DB dir + kanban workspace roots as extra writable roots.

---

## Hermes' Remaining Unique Value

Even when fully on Codex Runtime, Hermes continues to provide:

1. **Persistent Memory Layer** — `memory` / `session_search` unavailable on Codex Runtime, but dynamically switchable via `/codex-runtime auto`
2. **Multi-Channel Gateway** — Discord/Slack/Telegram simultaneous presence
3. **Skill Graph** — Reusable procedural knowledge (wiki management, cron job management, comparative analysis, etc.)
4. **Kanban Orchestration** — Multi-worker parallel dispatch
5. **Hybrid Execution** — `/codex-runtime auto` switches between Codex and Hermes native dynamically
