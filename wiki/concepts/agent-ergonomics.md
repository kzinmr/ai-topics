---
title: Agent Ergonomics
type: concept
aliases: [agent-oriented-language-design]
created: 2026-05-11
updated: 2026-05-11
status: L2
sources: [raw/articles/2026-01-20_wesmckinney_agent-ergonomics.md, https://wesmckinney.com/blog/agent-ergonomics/]
tags: [agentic-engineering, software-engineering, developer-tooling]
---

# Agent Ergonomics

Programming language and toolchain design principles optimized for AI coding agents rather than human developers. Coined by Wes McKinney in his January 2026 essay *"From Human Ergonomics to Agent Ergonomics."*

## Core Principle

> "Human ergonomics in programming languages matters much less now."

When AI agents are the primary code authors, traditional programming language design values — readability, simplicity, concise syntax — become secondary. What matters instead is optimizing the **agentic loop**: the compile-edit-test cycle that agents execute at 10-100x human frequency.

## Agent Ergonomics vs Human Ergonomics

| Dimension | Human Ergonomics | Agent Ergonomics |
|-----------|-----------------|------------------|
| Primary author | Human developer | AI coding agent |
| Most important | Readability, simplicity, ecosystem | Compile speed, distribution, runtime perf |
| Iteration speed | ~10-20 compile-test cycles/day | ~100-1000+ compile-test cycles/day |
| Distribution concern | pip/conda environments OK | Self-contained static binaries ideal |
| Language preference | Python, TypeScript, Ruby | Go, Rust |
| Code review | Human reads and understands | Automated review (roborev) essential |

## Key Requirements for Agent-Ergonomic Languages

1. **Ultrafast compile-test cycles**: Every second of compile time is multiplied by 100x agent iterations. Go's sub-second builds are a decisive advantage.
2. **Static binaries with zero dependencies**: Painless distribution — `scp` a single binary to deploy.
3. **Predictable dependency management**: Deterministic, reproducible builds without environment hell.
4. **Lean runtime footprint**: No interpreter, no JIT, no virtual machine overhead.
5. **Good runtime performance**: Agents may generate suboptimal code; fast runtimes compensate.

## Go vs Rust for Agent Ergonomics

| Factor | Go | Rust |
|--------|-----|------|
| Compile speed | Ultrafast (seconds) | Slow for release builds (minutes) |
| Memory safety | GC | Ownership/borrowing (no GC) |
| Concurrency | goroutines (simple) | async/tokio (complex) |
| Learning curve (for agents) | Lower | Higher |
| Agent preference | Strong edge for iteration speed | Tradeoff for memory safety |

McKinney's assessment: Go has a "substantial edge over Rust" due to compile times, though Rust's memory safety without GC is valuable for certain workloads.

## Python's Position

Python remains dominant in data science and ML due to:
- Ecosystem moat: NumPy, pandas, PyTorch, JAX
- Massive training data for LLMs → better code quality
- Superior for exploratory work (notebooks)

But for **agentic engineering tooling**, Python's weaknesses become liabilities:
- Slow test cycles (interpreted, no compilation step but startup overhead)
- Distribution challenges (interpreter, venv, dependency resolution — though `uv` helps)
- Higher memory usage, slower runtime

## Implications

### Where Value Lives (Four-Layer Model)

1. **Compute/compiler kernels** (CUDA, MLIR, Apache Arrow) ← Durable value
2. **Database/caching layers** (ADBC connectivity) ← Durable value
3. **Language bindings/orchestration** ← Thinning
4. **Application/agent interfaces** ← Thinnest

The bottom two layers hold the most long-term value; the top two become commoditized.

### Code Review Shift

When agents write code in languages the human doesn't know well, automated code review becomes essential. McKinney built [roborev](https://github.com/wesm/roborev) specifically because he cannot effectively review Go/Rust code manually.

### Era Shift

This is not the end of Python, but "the end of an era" — Python transitions from the primary implementation language to an orchestration/exploration layer on top of systems built in agent-ergonomic languages.

## Related Concepts

- [[concepts/harness-engineering/agentic-engineering]] — Professional patterns for coding agent usage
- [[concepts/vibe-coding-vs-agentic-engineering]] — Vibe coding vs professional agent use
- [[entities/wes-mckinney]] — Author of the agent ergonomics thesis
