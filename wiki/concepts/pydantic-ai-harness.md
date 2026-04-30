---
title: "pydantic-ai-harness — Official Capability Library for Pydantic AI"
type: concept
description: "Official batteries-included capability library for Pydantic AI agents — CodeMode with Monty sandbox, MCP integration, and composable agent extensions."
category: concepts
sub_category: AI Agent Architectures
tags: [pydantic, ai-agents, harness-engineering, sandboxing, mcp, code-execution]
status: complete
related:
  - pydantic-ai
  - monty-sandbox
  - logfire
  - samuel-colvin
  - harness-engineering
created: 2026-04-30
updated: 2026-04-30
sources:
  - https://github.com/pydantic/pydantic-ai-harness
  - https://ai.pydantic.dev/capabilities/
  - https://ai.pydantic.dev/hooks/
---

# pydantic-ai-harness

## TL;DR

**pydantic-ai-harness** is the official "batteries-included" capability library for [Pydantic AI](https://ai.pydantic.dev/), maintained by the Pydantic team. It provides standalone building blocks — tools, lifecycle hooks, instructions, and model settings — that extend what a Pydantic AI agent can do without framework changes.

The key insight: **Pydantic AI core ships only model/framework-level capabilities** (web search, tool search, thinking). Everything else lives in the harness as modular, pick-and-choose components.

## Architecture Philosophy

```
┌─────────────────────────────────────────────────┐
│              Pydantic AI Core                    │
│  (model support, fundamental capabilities)       │
│  ├── Web Search                                  │
│  ├── Tool Search (deferred tools)                │
│  └── Thinking                                    │
├─────────────────────────────────────────────────┤
│            pydantic-ai-harness                   │
│  (standalone, composable capabilities)           │
│  ├── CodeMode (Monty sandbox)                    │
│  ├── MCP server connectors                       │
│  ├── Lifecycle hooks                             │
│  └── ...more capabilities stabilize here first   │
└─────────────────────────────────────────────────┘
```

**Graduation model:** Capabilities start in the harness → stabilize → prove broadly essential → graduate into Pydantic AI core. This keeps the core lean while allowing rapid experimentation.

## Key Capabilities

### CodeMode

The flagship capability. CodeMode wraps **all tools into a single `run_code` tool** powered by [Monty](https://github.com/pydantic/monty) sandbox, enabling the model to orchestrate multiple tool calls with Python code instead of one model round-trip per call.

```python
from pydantic_ai import Agent
from pydantic_ai.capabilities import MCP
from pydantic_ai_harness import CodeMode

agent = Agent(
    'anthropic:claude-sonnet-4-6',
    capabilities=[
        MCP('https://api.githubcopilot.com/mcp/'),
        CodeMode(),
    ],
)

result = agent.run_sync(
    'Rank the open PRs on pydantic/pydantic-ai-harness by thumbs-up reactions.'
)
```

**Why this matters:** Instead of the agent making 10 sequential tool calls (each requiring a full LLM round-trip), CodeMode lets the model write a single Python script that calls all 10 tools at once. This dramatically reduces latency and token cost for multi-step operations.

### Monty Sandbox Integration

CodeMode requires the `[code-mode]` extra, which installs [Monty](https://github.com/pydantic/monty) — Pydantic's Rust-based secure Python interpreter. Monty provides:

- Sub-interpreter isolation
- Resource limits (memory, CPU time)
- Capability-based security (no arbitrary filesystem/network access)

### Logfire Observability

When combined with [Logfire](https://pydantic.dev/logfire), every agent run gets a trace. With CodeMode, you see the `run_code` span with each nested tool call as a child span — making it easy to debug what the model's code actually did.

```python
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness import CodeMode

logfire.configure()
logfire.instrument_pydantic_ai()

agent = Agent('anthropic:claude-sonnet-4-6', capabilities=[CodeMode()])
```

## Capability Matrix

The harness team studied leading coding agents, agent frameworks, and Claw-style assistants to map every capability area that matters for production agents. The matrix tracks:

| Capability Area | Status | Notes |
|----------------|--------|-------|
| Code Execution | ✅ CodeMode | Powered by Monty sandbox |
| MCP Integration | ✅ Core | From pydantic-ai core |
| Web Search | ✅ Core | From pydantic-ai core |
| Tool Search | ✅ Core | Deferred tools from pydantic-ai |
| Thinking | ✅ Core | Model-level capability |
| ...more | 🔄 Stabilizing | See repo for current matrix |

## Installation

```bash
# Basic installation
uv add pydantic-ai-harness

# With code execution support (includes Monty sandbox)
uv add "pydantic-ai-harness[code-mode]"
```

**Requirements:** Python 3.10+, `pydantic-ai-slim>=1.80.0`

## Relationship to Harness Engineering

pydantic-ai-harness embodies the broader **harness engineering** trend: the realization that the differentiator for production AI agents is not the base model, but the surrounding execution environment — tools, security boundaries, observability, and lifecycle management.

Key design principles:
1. **Separation of concerns** — Core handles model/framework; harness handles capabilities
2. **Gradual graduation** — Proven capabilities move from harness to core
3. **Composability** — Pick and choose only what you need
4. **Security-first** — Monty sandbox as the default for code execution

## See Also

- [[concepts/pydantic-ai]] — Core Pydantic AI framework
- [[concepts/monty-sandbox]] — Secure Python sandbox (Rust-based)
- [[concepts/logfire]] — Observability and tracing
- [[entities/samuel-colvin]] — Pydantic creator
- [[concepts/harness-engineering]] — Broader harness engineering pattern
