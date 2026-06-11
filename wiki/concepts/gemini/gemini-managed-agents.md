---
title: "Gemini Managed Agents"
type: concept
aliases:
  - gemini-managed-agents
  - antigravity-managed-agents
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - ai-agents
  - antigravity
  - google
  - coding-agents
  - agent-runtime
  - sandbox
  - developer-tooling
sources:
  - raw/articles/ai.google.dev--managed-agents-quickstart--2026-05-29.md
  - https://ai.google.dev/gemini-api/docs/managed-agents-quickstart
status: active
---

# Gemini Managed Agents

**Gemini Managed Agents** is a hosted agent runtime API from Google, exposed through the Gemini API (`generativelanguage.googleapis.com/v1beta/interactions`). A single API call provisions a sandboxed Linux environment, runs the **Antigravity** agent loop (code execution, browsing, shell), and returns results. Launched as a preview in May 2026.

## Core Architecture

```
Client (Python/JS/REST)
        ↓
  Gemini API (v1beta/interactions)
        ↓
  Antigravity Agent (preview-05-2026)
        ↓
  Sandboxed Linux Environment ("remote" or persisted)
        ├── Code execution (Python)
        ├── File system
        ├── Browser
        ├── Shell
        └── Custom tool extensions
```

## Key Design Properties

### 1. Single-Call Agent Loop
One `POST /v1beta/interactions` provisions the environment, runs the agent, and returns the final output. No polling, no state machine management on the client side.

### 2. Two-Dimensional State Model
- **Conversation context** (chat history, reasoning, tool use) — tracked via `previous_interaction_id`
- **Environment state** (files, packages, sandbox) — tracked via `environment` (ID or `"remote"`)

This enables flexible patterns:
- Reset conversation, keep files (omit `previous_interaction_id`)
- Keep conversation, fresh sandbox (`environment="remote"`)
- Full multi-turn with shared everything

### 3. Automatic Context Compaction
Native compaction at ~135k tokens prevents "context rot" and maintains agent focus across long sessions — no manual context window management needed.

### 4. Streaming
Real-time step deltas (reasoning tokens, tool call updates, incremental text) via `stream=True`.

### 5. File Download
Snapshot environments as tarballs via the Files API — download any artifacts the agent creates.

### 6. Custom Agent Persistence
Save conversation states as named agents via `managed_agents.create()`. Reuse across sessions. Share with other Google users.

## Built-in Tools

| Tool | Description |
|------|-------------|
| **Code execution** | Python in sandboxed Linux |
| **File system** | Read/write within environment |
| **Browser** | Web access from sandbox |
| **Shell** | Command execution |
| **Custom extensions** | User-defined tool integration |

## API Reference

```python
from google import genai

client = genai.Client()

# Basic interaction
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt.",
    environment="remote",
)

# Multi-turn
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a chart.",
)

# Streaming
stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize top 5 stories, save as PDF.",
    environment="remote",
    stream=True,
)

# Save custom agent
saved = client.managed_agents.create(
    display_name="My Agent",
    agent="antigravity-preview-05-2026",
    interaction_id=interaction.id,
)
```

### REST
```bash
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{"agent": "antigravity-preview-05-2026", "input": [{"type": "text", "text": "..."}], "environment": {"type": "remote"}}'
```

## SDKs
- Python: `google-genai` (`client.interactions`)
- JavaScript: `@google/genai`
- REST: Direct HTTP with API key auth

## Comparison with Other Agent Runtimes

| Feature | Gemini Managed Agents | Claude Code | Codex CLI | Pydantic AI + Monty |
|---------|----------------------|-------------|-----------|---------------------|
| **Hosting** | Google-managed | Local terminal | Local terminal | Self-hosted |
| **Sandbox** | Built-in Linux sandbox | Permission-based | Docker/local | Custom Rust VM |
| **API** | REST + gRPC (streaming) | Terminal/stdio | Terminal/stdio | Python library |
| **Multi-turn memory** | Built-in + compaction | Session-based | Session-based | Application-managed |
| **Custom agent persisting** | Yes (managed_agents) | No | No | No |
| **Browser** | Built-in | Via MCP | Via MCP | Via external functions |
| **Pricing** | Gemini API pricing | Anthropic API | OpenAI API | Free (MIT) |

## Strategic Significance

Gemini Managed Agents represents Google's entry into the **agent-as-a-service** space, competing with:
- **Anthropic's Claude Code** (local agent runtime)
- **OpenAI's Codex CLI** (terminal-based agent)
- **Pydantic AI + Monty** (library + sandbox)

The key differentiator is **fully managed infrastructure** — no local setup, no Docker, no sandbox configuration. A single API call gets you a complete agent execution environment with streaming, file persistence, and multi-turn memory.

## Related Pages
- [[entities/deepmind]] — Google DeepMind, develops Antigravity and Gemini models
- [[concepts/monty-sandbox]] — Pydantic's secure Python interpreter (competing sandbox approach)
- [[concepts/harness-engineering/agent-runtime]] — General concept of agent execution environments
- [[concepts/agent-loop-orchestration]] — How agent loops are structured
- [[concepts/programmatic-tool-calling]] — The paradigm of agents writing code to interact with tools
- [[concepts/programmatic-tool-calling]] — Comparison of code execution approaches
