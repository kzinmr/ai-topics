---
name: Monty Sandbox
type: concept
tags: [sandbox, rust, python, security, ai-agents, pydantic, capabilities]
related:
  - [[concepts/code-mode]]
  - [[concepts/capabilities-based-security]]
  - [[concepts/harness-engineering]]
  - [[entities/samuel-colvin]]
depth: L2
status: complete
created: 2026-04-16
---

# Monty — Minimal Secure Python Interpreter for AI Agents

## Definition

Monty is an open-source (MIT), minimal, secure Python interpreter written in Rust, designed specifically for running LLM-generated code within AI agents.

**Repository**: github.com/pydantic/monty (6.6K+ stars, 40 contributors)

## Architecture

- **From-scratch bytecode VM** — Not CPython, not WASM. Uses Ruff's parser to turn Python source into custom bytecode.
- **Embedded in host process** — No Docker daemon, no cloud account, no API keys needed.
- **Language bindings** — Python, JavaScript/TypeScript, Go (in PR), Dart/Kotlin (in PR).

## Security Model: Capabilities-Based

> *"Start from nothing, then selectively grant capabilities. The default is zero access — no filesystem, no network, no environment variables, strict resource limits."* — Samuel Colvin

This contrasts with traditional sandboxing (full VM/container → restrict down), which has:
- Massive attack surface
- Whack-a-mole security patches
- Complex configuration

Monty's approach:
- Zero default access
- Explicit external function registration
- Host-controlled capabilities
- Auditable security boundary

## Performance

| Metric | Monty | Docker | Sandbox Services | Pyodide |
|--------|-------|--------|------------------|---------|
| **Start Latency** | 0.004ms | 195ms | ~1000ms+ | 2800ms |
| **Memory Overhead** | ~5MB | ~100MB+ | ~500MB+ | ~50MB |
| **Binary Size** | ~4.5MB | ~1GB | N/A | ~12MB |

## Supported Features

- Sync/async functions, closures, comprehensions, f-strings, type hints
- Host-defined dataclasses
- Standard modules: sys, typing, asyncio, pathlib
- Type checking (via `ty`)
- Memory, recursion, and execution time limits
- REPL support (for persistent state assumptions)

## Not Supported (By Design)

- Classes (coming soon)
- `match` statements (coming soon)
- Context managers (coming soon)
- Full standard library (added gradually based on LLM demand)
- **Third-party packages** (likely never — Monty is not CPython)

## State Snapshotting

Monty can serialize execution state mid-flight to bytes (single-digit KBs), then resume later or on a different machine. This enables:
- Agent pause/resume across sessions
- Migration between compute environments
- Debugging and replay

## Timeline

- **May 2023**: Repository created
- **Dec 2025**: Built "over Christmas" by Samuel Colvin
- **Feb 2026**: v0.0.7 released (asyncio, dataclass methods, pathlib)
- **Feb 2026**: Talk at Latent Space
- **Mar 2026**: v0.0.9 released (latest)
- **Future**: CodeMode integration in Pydantic AI

## Related

- [[concepts/code-mode]] — The paradigm Monty implements
- [[concepts/capabilities-based-security]] — Security philosophy
- [[concepts/harness-engineering]] — Monty as a harness environment
- [[entities/samuel-colvin]] — Creator
