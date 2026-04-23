---
title: "In-Process Sandbox"
created: 2026-04-16
updated: 2026-04-16
tags: [concept, ai-agents, security, sandboxing, capabilities, monty, in-process]
aliases: ["monty-sandbox", "capabilities-based-security", "monty", "capability-sandbox"]
related: [[concepts/harness-engineering/system-architecture/infrastructure-noise.md]], [[harness-engineering]], [[samuel-colvin]]
depth: L2
status: complete
---

# In-Process Sandbox

In-process sandboxing isolates LLM-generated code execution **within the host process** using language-level security boundaries — without requiring Docker, cloud accounts, or external infrastructure. This contrasts with infrastructure-level sandboxing (containers, microVMs) which isolates at the OS/hypervisor level.

> **Note**: This page covers in-process isolation (Monty, capabilities-based security). For infrastructure-level sandboxing, see [[infrastructure]].

## Two Approaches to Sandbox Security

| Approach | Starts With | Security Model | Analogy |
|----------|-------------|----------------|---------|
| **Traditional Sandbox** (Docker, Firecracker) | Full VM/container | Block known-bad things | Firewall blocking bad ports |
| **Capabilities-Based** (Monty) | Nothing | Allow only known-good things | Zero-trust network |

Traditional sandboxing assumes the sandbox is correctly configured, all vulnerabilities are patched, and no escape vectors exist. Capabilities-based security assumes **the code will try to escape** — default = deny everything, only explicitly granted operations succeed.

> *"Start from nothing, then selectively grant capabilities. The default is zero access — no filesystem, no network, no environment variables, strict resource limits. You explicitly opt in to each capability via external functions that you wrote, you control, and you can audit."* — Samuel Colvin

## Monty — Minimal Secure Python Interpreter

[Monty](https://github.com/pydantic/monty) is an open-source (MIT), minimal, secure Python interpreter written in Rust, designed specifically for running LLM-generated code within AI agents.

**Repository**: github.com/pydantic/monty (6.6K+ stars, 40 contributors)

### Architecture

- **From-scratch bytecode VM** — Not CPython, not WASM. Uses Ruff's parser to turn Python source into custom bytecode.
- **Embedded in host process** — No Docker daemon, no cloud account, no API keys needed.
- **Language bindings** — Python, JavaScript/TypeScript, Go (in PR), Dart/Kotlin (in PR).

### Capabilities-Based Security Model

1. **No default access**: The interpreter starts with zero capabilities
2. **External function registration**: Host process explicitly registers what the LLM code can call
3. **Type stubs**: LLM code sees only the interfaces you expose
4. **Resource limits**: Memory, recursion depth, execution time capped by host
5. **No third-party packages**: LLM code cannot `import requests` or access arbitrary libraries

This approach is closer to **formal methods** in mathematics (reflecting Samuel Colvin's PhD background in geometric group theory) than traditional DevOps practice.

### Performance Comparison

| Metric | Monty | Docker | Sandbox Services | Pyodide |
|--------|-------|--------|------------------|---------|
| **Start Latency** | 0.004ms | 195ms | ~1000ms+ | 2800ms |
| **Memory Overhead** | ~5MB | ~100MB+ | ~500MB+ | ~50MB |
| **Binary Size** | ~4.5MB | ~1GB | N/A | ~12MB |

### Supported Features

- Sync/async functions, closures, comprehensions, f-strings, type hints
- Host-defined dataclasses
- Standard modules: sys, typing, asyncio, pathlib
- Type checking (via `ty`)
- Memory, recursion, and execution time limits
- REPL support (for persistent state assumptions)

### Not Supported (By Design)

- Classes (coming soon)
- `match` statements (coming soon)
- Context managers (coming soon)
- Full standard library (added gradually based on LLM demand)
- **Third-party packages** (likely never — Monty is not CPython)

### State Snapshotting

Monty can serialize execution state mid-flight to bytes (single-digit KBs), then resume later or on a different machine. This enables:
- Agent pause/resume across sessions
- Migration between compute environments
- Debugging and replay

## When to Use In-Process vs Infrastructure Sandbox

| Criteria | In-Process (Monty) | Infrastructure (Docker/Firecracker) |
|----------|-------------------|--------------------------------------|
| **Use case** | Simple Python scripts, data transforms | Full application execution, package installation |
| **Latency sensitivity** | Sub-millisecond startup needed | 100ms-2s startup acceptable |
| **Package needs** | Standard library only | Third-party packages (numpy, pandas, requests) |
| **Security model** | Capabilities-based, zero-trust | OS-level isolation, container escape protection |
| **Infrastructure** | No external dependencies | Docker daemon, cloud account, or sandbox service |
| **State persistence** | Snapshot/restore supported | Full filesystem persistence |

## Timeline

- **May 2023**: Repository created
- **Dec 2025**: Built "over Christmas" by Samuel Colvin
- **Feb 2026**: v0.0.7 released (asyncio, dataclass methods, pathlib)
- **Feb 2026**: Talk at Latent Space
- **Mar 2026**: v0.0.9 released (latest)
- **Future**: CodeMode integration in Pydantic AI

## Related

- [[concepts/harness-engineering/system-architecture/infrastructure-noise.md]] — Container, microVM, and gVisor-level isolation
- [[harness-engineering]] — Monty as a harness environment
- [[samuel-colvin]] — Creator

## Sources

- [Monty GitHub Repository](https://github.com/pydantic/monty)
- [Samuel Colvin at Latent Space (Feb 2026)](https://www.youtube.com/watch?v=CeOXx-XTYek)
- [Cloudflare: CodeMode](https://developers.cloudflare.com)
- [Anthropic Blog: Code execution patterns](https://www.anthropic.com)
