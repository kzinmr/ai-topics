# Pydantic AI Harness — Official Capability Library

**Source:** [github.com/pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness)
**Date:** 2026-04-30
**License:** MIT

## Summary

**Pydantic AI Harness** is the official "batteries-included" capability library for Pydantic AI. It provides standalone building blocks — tools, lifecycle hooks, and instructions — that extend agent functionality without requiring framework changes.

## Architecture

### Core Abstraction: Capability

A `Capability` is an `AbstractCapability` subclass bundling:
- **Toolsets** — Collections of tools provided to the agent
- **Hooks** — Lifecycle methods (`before_model_request`, `wrap_run`, `after_tool_execute`) that intercept agent graph execution
- **Instructions** — System prompts and behavioral guidelines
- **Model Settings** — Configuration for the underlying model
- **Guards** — Input/output validation, cost budgets, secret masking

### Graduation Model

Capabilities start in the harness → stabilize → prove broadly essential → graduate into Pydantic AI core. This keeps the core lean while allowing rapid experimentation.

### Ecosystem Integration

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

### CodeMode (Flagship)

Wraps **all tools into a single `run_code` tool** powered by [Monty](https://github.com/pydantic/monty) sandbox. The model writes Python that calls multiple tools with loops, conditionals, variables, and `asyncio.gather` — all inside one tool call.

**Problem:** Standard tool calling requires one model round-trip per tool call. An agent needing 10 items makes 11+ model calls — slow, expensive, context-heavy.

**Solution:** CodeMode collapses sequential calls into one script execution.

```python
paris, tokyo = await asyncio.gather(
    get_weather(city='Paris'),
    get_weather(city='Tokyo'),
)
paris_c = await convert_temp(fahrenheit=paris['temp_f'])
tokyo_c = await convert_temp(fahrenheit=tokyo['temp_f'])
{'paris': paris_c, 'tokyo': tokyo_c}
```

### Capability Matrix

| Category | Capability | Status |
| :--- | :--- | :--- |
| **Tools & Execution** | Code Mode | ✅ Available |
| | File System | 🚧 PR #177 |
| | Verification Loop | 🚧 PR #169 |
| **Context Mgmt** | Sliding Window | 🚧 PR #191 |
| | Context Compaction | 🚧 PR #191 |
| **Memory** | Persistence (KV) | 🚧 PR #176/179 |
| **Orchestration** | Sub-agents | 🚧 PR #178 |
| | Planning | 🚧 PR #180 |
| **Safety** | Guardrails (In/Out) | 🚧 PR #182 |
| | Secret Masking | 🚧 PR #172 |
| **Reliability** | Loop Detection | 🚧 PR #186 |
| | Tool Error Recovery | 🚧 PR #171 |

## Coding Standards

- **Type Safety:** Pyright strict mode mandatory. No `Any` types.
- **Testing:** 100% branch coverage required.
- **Linting:** Ruff (line-length=120, single quotes, max-complexity=15).

## AICA (AI Code Assistant) Workflow

The repo uses a "Ralph loop" state-machine: TRIAGE → GOALS → PLAN → CODE → VERIFY → REVIEW → PUBLISH. PR review uses DDD+ protocol (do, dismiss, discuss, waiting, done).

## Sources

- [pydantic/pydantic-ai-harness GitHub](https://github.com/pydantic/pydantic-ai-harness)
- [AGENTS.md (Developer Guidelines)](https://github.com/pydantic/pydantic-ai-harness/blob/main/AGENTS.md)
- [Code Mode Documentation](https://pydantic.dev/docs/ai/harness/code-mode/)
- [Samuel Colvin: Monty blog post](https://pydantic.dev/articles/pydantic-monty)
