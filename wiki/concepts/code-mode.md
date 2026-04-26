---
title: "CodeMode — LLM Code Execution Over Sequential Tool Calling"
tags: [[concepts/code-execution-agents-latency-monty-pydantic-ai-tool-calling-sandbox]]
created: 2026-04-16
updated: 2026-04-16
type: concept
---

# CodeMode — LLM Code Execution Over Sequential Tool Calling

## Definition

CodeMode is the paradigm where LLMs write code (typically Python) for batch execution rather than making sequential tool calls. Coined by Cloudflare and independently developed by Anthropic, Pydantic, and others.

> *"LLMs work faster, cheaper and more reliably when they write code instead of making sequential tool calls."* — Samuel Colvin

## The Execution Continuum

| Approach | Control | Capability | Start Latency | Cost Model |
|----------|---------|------------|---------------|------------|
| **Tool Calling** | High | Low | Sequential (4-7 round trips, ~12s) | Per-token |
| **CodeMode (Monty)** | High-Medium | Medium | 0.004ms | In-process, zero infra |
| **Sandbox Services** (Modal, E2B, Daytona) | Medium | High | ~1000ms+ | Per-execution billing |
| **Coding Agents** (Claude Code, Cursor) | Low | Very High | Minutes | High |
| **Full Computer Use** | None | Maximum | Minutes | Very high |

## Why It Works

1. **Parallel Execution**: LLM writes a single Python script using `asyncio.gather()` instead of 4-7 sequential tool calls
2. **Native Control Flow**: Loops, conditionals, transforms, comprehensions — all expressed naturally in code
3. **Lower Token Usage**: Weather comparison example: 4.1k input tokens (tool calling) vs 3.3k (CodeMode), $0.019 vs $0.017
4. **Composable**: Code can chain operations, handle errors, and transform data in ways tool calling cannot

## Monty Implementation (Pydantic)

- Minimal, secure Python interpreter written in Rust
- From-scratch bytecode VM using Ruff's parser
- **Capabilities-based security**: Zero default access, explicit grants
- **State snapshotting**: Serialize execution mid-flight to bytes, resume elsewhere
- **Binary size**: ~4.5MB, memory overhead ~5MB

## Key Advocates

- **Samuel Colvin** (Pydantic): Built Monty, advocates "start from nothing" security
- **Andrej Karpathy**: Popularized code-over-sequential-tool-calls paradigm
- **Anthropic**: Documented in multiple blog posts on agent patterns
- **Cloudflare**: Coined the term "CodeMode"

## Related Patterns

- [[concepts/harness-engineering]] — Monty as a harness environment
- [[concepts/structured-outputs]] — Type safety constrains LLM output
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Alternative to MCP tool execution
