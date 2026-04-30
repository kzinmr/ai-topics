---
title: "pydantic-ai-harness — Official Capability Library for Pydantic AI"
type: concept
description: "Official batteries-included capability library for Pydantic AI agents — CodeMode with Monty sandbox, MCP integration, context management, memory, orchestration, guardrails, and composable agent extensions. Provides the Harness layer that pairs with Monty as Open Runtime."
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
  - agent-architecture-decomposition
created: 2026-04-30
updated: 2026-04-30
sources:
  - https://github.com/pydantic/pydantic-ai-harness
  - https://ai.pydantic.dev/capabilities/
  - https://ai.pydantic.dev/hooks/
  - https://pydantic.dev/articles/pydantic-monty
  - https://github.com/pydantic/pydantic-ai-harness/releases/tag/v0.2.0
---

# pydantic-ai-harness

## TL;DR

**pydantic-ai-harness** is the official "batteries-included" capability library for [Pydantic AI](https://ai.pydantic.dev/), maintained by the Pydantic team. It provides standalone building blocks — tools, lifecycle hooks, and instructions — that extend agent functionality without requiring framework changes.

The key insight: **Pydantic AI core ships only model/framework-level capabilities** (web search, tool search, thinking). Everything else lives in the harness as modular, pick-and-choose components.

**Important positioning**: This repo is best understood as a **公式インキュベータ兼roadmap** rather than a "多機能な完成品". Capabilities are developed here first, then graduated to core once proven essential and stable. The published API (as of v0.2.0) is essentially just `CodeMode` — the other capabilities listed in the matrix are still in PR stage. The repo structure reflects this: `pydantic_ai_harness/` (current code), `tests/`, and `legacy/pydantic-harness/` (compatibility shim from the pre-rename era).

**Versioning**: The library is on a **0.x policy** — minor version bumps may include breaking changes. v0.1.1 renamed the package from `pydantic-harness` to `pydantic-ai-harness`; the `legacy/` directory preserves backward compatibility. Adoption guidance: treat this as **"公式だが、まだ固めている最中の層"**.

**Positioning in the 3-layer architecture** ([agent-architecture-decomposition]]):
- **Runtime**: Pydantic Monty (Rust-based secure Python interpreter) — [[concepts/monty-sandbox]]
- **Harness**: pydantic-ai-harness (capability library) — this page
- Together they form a complete **Open Runtime + Open Harness** stack for production agents.

## The Capabilities Model

### Core Abstraction

A `Capability` is an `AbstractCapability` subclass that bundles:

| Component | Purpose |
|---|---|
| **Toolsets** | Collections of tools provided to the agent |
| **Hooks** | Lifecycle methods (`before_model_request`, `wrap_run`, `after_tool_execute`) that intercept agent graph execution |
| **Instructions** | System prompts and behavioral guidelines |
| **Model Settings** | Configuration for the underlying model |
| **Guards** | Input/output validation, cost budgets, secret masking |

### Graduation Model

Capabilities follow a **staging pipeline**:

```
pydantic-ai-harness (experimental) → stabilize → prove essential → graduate to Pydantic AI core
```

This keeps the core lean while allowing rapid experimentation. Capabilities are versioned at 0.x (APIs still stabilizing).

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
│  ├── FileSystem                                  │
│  ├── Verification Loop                           │
│  ├── Sliding Window / Context Compaction         │
│  ├── Memory (KV persistence)                     │
│  ├── Sub-agents / Planning                       │
│  ├── Guardrails / Secret Masking                 │
│  └── Loop Detection                              │
└─────────────────────────────────────────────────┘
```

## Key Capabilities

### CodeMode (Flagship Capability)

**CodeMode wraps all tools into a single `run_code` tool** powered by [Monty](https://github.com/pydantic/monty) sandbox. The model writes Python that calls multiple tools with loops, conditionals, variables, and `asyncio.gather` — all inside one tool call.

**Problem**: Standard tool calling requires one model round-trip per call. An agent needing 10 items makes 11+ model calls — slow, expensive, context-heavy.

**Solution**: CodeMode collapses sequential calls into one script execution.

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

# Model writes Python code internally:
# paris, tokyo = await asyncio.gather(
#     get_weather(city='Paris'),
#     get_weather(city='Tokyo'),
# )
# paris_c = await convert_temp(fahrenheit=paris['temp_f'])
# ...
```

**Runtime + Harness coupling**: CodeMode requires `[code-mode]` extra, which installs Monty (the Runtime). The Harness provides the orchestration layer that decides *when* to write code vs. use sequential tool calls.

#### CodeMode as RLM Foundation

CodeMode is the natural foundation for implementing RLM-style agents on pydantic-ai. See [[concepts/code-mode]] for the full "Agent around REPL" pattern — three implementation tiers from minimal (`CodeMode + output function`) to graph-native (`pydantic-graph` + Monty snapshots).

Key architectural principle: **Monty is a REPL sandbox, not an agent host**. Conversation control, output validation, approval, history management, and durability belong on the Pydantic AI side (the "around"); code execution belongs inside Monty (the "REPL"). This separation keeps each layer focused and composable.

#### Deferred Tool Calls — Current Status

The CodeMode documentation historically stated that "approval/deferred tools are excluded from the sandbox." However, v0.2.0 release notes introduced `HandleDeferredToolCalls` for inline resolution. The current implementation branches: if a handler exists, the deferred call is resolved; if not, it errors. So the accurate reading is **"not fully forbidden — handler-required and actively evolving"**, rather than the earlier "complete prohibition." The documentation may lag behind the implementation here.

### Full Capability Matrix

| Category | Capability | Status | Notes |
| :--- | :--- | :--- | :--- |
| **Tools & Execution** | Code Mode | ✅ Available | Powered by Monty sandbox |
| | File System | 🚧 PR #177 | Read/write/search with path traversal prevention |
| | Verification Loop | 🚧 PR #169 | Auto-run tests after edits, auto-fix failures |
| **Context Mgmt** | Sliding Window | 🚧 PR #191 | Trim history to stay within token limits |
| | Context Compaction | 🚧 PR #191 | LLM-powered summarization of old messages |
| **Memory** | Persistence (KV) | 🚧 PR #176/179 | Save/restore conversation state and memory |
| **Orchestration** | Sub-agents | 🚧 PR #178 | Delegate tasks to specialized child agents |
| | Planning | 🚧 PR #180 | Break complex tasks into structured plans |
| **Safety** | Guardrails | 🚧 PR #182 | Input/output validation and cost/token budgets |
| | Secret Masking | 🚧 PR #172 | Detect and redact secrets in I/O |
| **Reliability** | Loop Detection | 🚧 PR #186 | Detect and break repetitive agent loops |
| | Tool Error Recovery | 🚧 PR #171 | Auto-retry failed tool calls |

*Note: Several capabilities are being upstreamed from community partner [vstorm-co](https://github.com/vstorm-co).*

### Logfire Observability

When combined with [Logfire](https://pydantic.dev/logfire), every agent run gets a trace. With CodeMode, you see the `run_code` span with each nested tool call as a child span — making it easy to debug what the model's code actually did.

## Development Workflow

### AICA (AI Code Assistant) Integration

The repo uses a state-machine workflow called the **"Ralph loop"**:

```
TRIAGE → GOALS → PLAN → CODE → VERIFY → REVIEW → PUBLISH
```

PR review uses the **DDD+ protocol**: do, dismiss, discuss, waiting, done.

### Coding Standards

| Standard | Requirement |
|---|---|
| **Type Safety** | Pyright strict mode. No `Any` types. |
| **Type Narrowing** | No typecasting (`cast()`); use narrowing. |
| **Testing** | 100% branch coverage (`make testcov`). |
| **Linting** | Ruff (line-length=120, single quotes, max-complexity=15). |
| **Security** | PRs modifying `pyproject.toml`/`uv.lock` from non-members are auto-closed. |

## Positioning in Harrison Chase's 3-Layer Framework

Pydantic uniquely provides **both Runtime and Harness**:

| Layer | Pydantic Component | Role |
|---|---|---|
| **Open Runtime** | Monty | Secure Python bytecode VM (0.004ms startup, deny-by-default) |
| **Open Harness** | pydantic-ai-harness | Capability library (CodeMode, memory, orchestration, guards) |
| **Open Models** | Model-agnostic | Works with Claude, GPT, Gemini, Ollama, etc. via Pydantic AI core |

This is different from:
- **Claude Code / OpenClaw**: Runtime = bash, Harness = proprietary
- **LangChain Deep Agents**: Runtime = container, Harness = LangChain orchestration
- **RLM**: Runtime = Python REPL, Harness = recursive context decomposition

Samuel Colvin's design philosophy: *"Start from nothing, then selectively grant capabilities."* This applies to both Monty (no filesystem/network by default) and the Harness (no tools by default — you compose what you need).

## See Also

- [[concepts/pydantic-ai]] — Core Pydantic AI framework
- [[concepts/monty-sandbox]] — Secure Python sandbox (Rust-based)
- [[concepts/logfire]] — Observability and tracing
- [[entities/samuel-colvin]] — Pydantic creator
- [[concepts/harness-engineering]] — Broader harness engineering pattern
- [[concepts/agent-architecture-decomposition]] — 3-layer framework context
- [[concepts/code-mode]] — Code execution pattern for agents
