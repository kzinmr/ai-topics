---
title: "Agent-First Design"
type: concept
aliases:
  - agent-first-design
created: 2026-04-25
updated: 2026-05-18
tags:
  - concept
  - programming-language
  - agentic-engineering
  - developer-tooling
  - harness-engineering
  - coding-agents
sources:
  - raw/articles/2026-05-18_armin-ronacher_a-language-for-agents.md
  - raw/articles/2026-05-18_vercel-labs_zero-language-for-agents.md
---

# Agent-First Design

**Agent-first design** is the philosophy that programming languages should be designed with **AI coding agents as first-class users**, not as an afterthought. Emerging in 2025–2026, this movement argues that agents consume code differently than humans—via line-by-line reading in context windows, grep-based navigation, and structured diagnostic output—and that existing languages (Python, Rust, Swift) were designed for human ergonomics, not machine reasoning.

The core thesis, articulated by [[entities/armin-ronacher]] in his February 2026 essay *"A Language For Agents"*, is that **the cost of writing code is dropping**, so the breadth of a language's ecosystem matters less than its clarity, grepability, and agent-friendly structure.

## Why New Languages Can Succeed

Ronacher identifies three factors that determine whether a language is agent-friendly:

1. **Ecosystem breadth matters less** — missing functionality can be reimplemented by the agent from another language's library. Ronacher now uses TypeScript/JavaScript where he'd have used Python because agents perform better.
2. **Tooling stability > training data** — languages with rapid churn (Zig) or painful tooling (Swift) degrade agent success, even with good training data representation.
3. **Agent performance is measurable** — unlike surveys, agents give objective feedback on language design; we can measure what works.

## Design Principles (Ronacher's Framework)

### 1. Context Without LSP
Agents often work without a running Language Server Protocol (LSP)—reading from GitHub, documentation snippets, or raw files. A language must be comprehensible in both LSP and non-LSP contexts.

### 2. Braced Syntax
Significant whitespace (Python) causes token inefficiency and surgical edit errors. Agents struggle with whitespace-based indentation during surgical changes.

### 3. Explicit Flow Context (Effect Markers)
Functions should declare required effects (time, rng, database) in their signatures. Auto-formatting propagates these annotations, enabling precise mocking in tests.

### 4. Results Over Exceptions
Agents fear exceptions—they try to catch everything and do poor recovery. Typed result types (Result/Option) are preferred for composability and error path clarity.

### 5. Minimal Diffs & Line-Friendly Syntax
Agents read files line-by-line. Multi-line strings confuse them. A language should require less reformatting and avoid constructs that span many lines.

### 6. Grepability (Go-style)
Package-qualified symbols (like `context.Context` instead of `Context`) make code findable through basic tools. Discouraged aliasing means fewer false positives for automation.

### 7. Local Reasoning
Code must be understandable in isolation, without hidden global dependencies. Agents work with a few loaded files and lack spatial awareness of the full codebase.

### 8. Dependency-Aware Build Tools
Clear package structure, forbidding circular imports, cached test results. Go is the gold standard here.

### What Agents Hate
- **Macros** — confusing for both humans and agents
- **Re-exports & barrel files** — break the one-to-one mapping between declaration and import location
- **Aliasing** — agents complain about many aliases
- **Flaky tests & dev env divergence** — agents both create and suffer from flaky tests

## Concrete Implementations

### Vercel Zero (2026)
[[entities/vercel-labs]]'s **Zero** is the first systems language built explicitly for agent-first design. It implements Ronacher's principles:
- Capability-based I/O (`World` capability, compiler-rejected at compile time if unavailable)
- Explicit effects via `raises` and `check` keywords
- `--json` structured diagnostics with repair metadata (`{"repair": {"id": "declare-missing-symbol"}}`)
- Stable diagnostic codes (NAM003, TAR002, MET001, etc.) for reliable agent recovery
- Machine-readable skill manifests (`zero skills get zero --full`)

Zero is Apache 2.0 licensed and written primarily in C (v0.1.2, May 2026).

## Related Concepts

- [[entities/armin-ronacher]] — Author of "A Language For Agents", primary theorist of agent-first design
- [[entities/vercel-labs]] — Creators of Zero, the agent-first systems language
- [[concepts/agent-ergonomics]] — Broader topic of how agents interact with code and tools
- [[concepts/harness-engineering/agentic-engineering]] — Professional patterns for coding agent usage
- [[concepts/programming-languages]] — Type systems, compilers, language design

## See Also

- [A Language For Agents](https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/) by Armin Ronacher
- [Zero — The Programming Language for Agents](https://github.com/vercel-labs/zero) by Vercel Labs
