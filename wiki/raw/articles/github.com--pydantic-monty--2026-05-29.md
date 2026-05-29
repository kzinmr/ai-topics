# Monty: Minimal, Secure Python Interpreter in Rust for AI

**Source:** https://github.com/pydantic/monty
**Retrieved:** 2026-05-29
**Via:** X post by @samuelcolvin (2026-05-29)
**Archived for:** wiki knowledge base (update to existing Monty Sandbox page)

---

**Stars:** 7,243 ⭐ | **Forks:** 320 | **Open Issues:** 61
**Language:** Rust (69.8%) + Python (27.6%)
**License:** MIT
**Latest Release:** v0.0.17 (2026-04-22)
**Contributors:** 40 (top: samuelcolvin, davidhewitt)

## Purpose

> **To run code written by agents.** LLMs can work faster, cheaper and more reliably if they're asked to write Python (or Javascript) code, instead of relying on traditional tool calling. Monty makes that possible without the complexity of a sandbox or risk of running code directly on the host.

Avoids the cost, latency, and complexity of full container-based sandboxes. Startup in **single-digit microseconds**.

## ✅ Capabilities
- Run a reasonable subset of Python for agentic code
- Complete environment isolation (blocked filesystem, env vars, network)
- Type-checking with modern type hints (ships with `ty`)
- Snapshotting — pause at external function calls, serialize to bytes, resume later
- Extreme startup speed (<1 μs), runtime 5× faster to 5× slower than CPython
- Callable from Rust, Python, JavaScript (no CPython dependency)
- Resource control (memory, allocations, stack depth, execution time)
- STDOUT/STDERR capture
- Async & sync external functions
- Limited stdlib: sys, os, typing, asyncio, re, datetime, json, dataclasses

## ❌ Limitations
- No full stdlib
- No third-party libraries (e.g., Pydantic itself)
- No class definitions (coming soon)
- No match statements (coming soon)

## Motivation

Inspired by:
- Codemode from Cloudflare
- Programmatic Tool Calling (Anthropic)
- Code Execution with MCP (Anthropic)
- Smol Agents (Hugging Face)

Monty will soon power **codemode** in Pydantic AI.

## Usage Example
```python
import pydantic_monty

m = pydantic_monty.Monty(code, inputs=['prompt'], script_name='agent.py')

# Execution pauses at external function calls
result = m.start(inputs={'prompt': 'testing'})

# Resume with actual data
result = result.resume({'return_value': 'hello world'})
```

---

## Key Takeaway

Monty has grown significantly since launch (7.2K stars, 40 contributors, v0.0.17). It's positioned as the secure execution layer for agent-generated code, with snapshot-based pause/resume allowing agents to interleave reasoning and code execution. Will become the codemode runtime for Pydantic AI.
