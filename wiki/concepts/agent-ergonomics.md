---
title: Agent Ergonomics
type: concept
aliases: [agent-oriented-language-design]
created: 2026-05-11
updated: 2026-05-18
status: L2
sources: [raw/articles/2026-01-20_wesmckinney_agent-ergonomics.md, https://wesmckinney.com/blog/agent-ergonomics/, raw/articles/2026-05-18_armin-ronacher_a-language-for-agents.md, https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/, raw/articles/2026-05-18_vercel-labs_zero-language-for-agents.md, https://github.com/vercel-labs/zero]
tags: [agentic-engineering, software-engineering, developer-tooling, programming-language, ai-coding]
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

## Armin Ronacher's Language Design Principles (2026)

While McKinney's framework focuses on the **toolchain/ecosystem level** (compile speed, distribution, dependency management), Armin Ronacher's February 2026 essay *"A Language For Agents"* drills into **language syntax and feature design** — the concrete choices that make a language agent-friendly or agent-hostile.

### Why New Languages Will Emerge

| Old Assumption | New Reality |
|----------------|--------------|
| Typing is laborious → push for brevity (type inference, dynamic typing) | Code is cheap to produce → **understanding code is critical** |
| Less code to write is always better | More explicit code can be better for human review and agent comprehension |
| All code is human-written | Some code will be **only consumed by machines**, but must be explainable to non-programmers |

> *"The cost of writing code is going down, but because we are also producing more of it, understanding what the code does is becoming more important."*

### The Eight Design Principles

#### 1. Context Without Language Server Protocol (LSP)
Agents often skip running the LSP (laziness, snippets, individual GitHub files). A language should offer a **single coherent experience** both with and without LSP — no split between "IDE mode" and "text mode."

#### 2. Braced Syntax Over Significant Whitespace
Whitespace-based indentation (Python) causes token inefficiency and surgical edit errors. Agents often disregard indentation and rely on formatters to fix it later. However, pure brace-based syntax can suffer from closing-parenthesis miscounts (Lisp/Scheme) — balance is needed.

#### 3. Explicit Flow Context (Effect Markers)
Implicit context (like async locals) leads to unconfigured dependencies. Ronacher proposes **declared effects** in function signatures, auto-propagated by a code formatter:

```rust
fn issue(sub: UserId, scopes: []Scope) -> Token
    needs { time, rng }
{
    return Token{
        sub,
        exp: time.now().add(24h),
        scopes,
    }
}

test "issue creates exp in the future" {
    using time = time.fixed("2026-02-06T23:00:00Z");
    using rng  = rng.deterministic(seed: 1);

    let t = issue(user("u1"), ["read"]);
    assert(t.exp > time.now());
}
```

The agent can precisely mock side effects based on error messages — the function signature tells it exactly what dependencies to supply.

#### 4. Results Over Exceptions
Agents **fear exceptions** — they catch everything, log poorly, and recover badly. Checked exceptions propagate everywhere, causing cascading changes. **Typed result types** may be better, but require strong type/object system support for composability.

#### 5. Minimal Diffs & Line-Friendly Syntax
Agents read files line-by-line → multi-line strings confuse them (they edit embedded code thinking it's real code). **Zig's prefix-based multi-line strings** are a rare good solution. Syntax should minimize reformatting and avoid trailing-comma oddities (JSON). Diff stability is key.

#### 6. Make It Grep-able
**Go's approach:** symbols are used with package qualifier (`context.Context`), aliasing discouraged. Agents rely on `grep` for external files not indexed. Findability reduces false positives in automated code modifications.

#### 7. Local Reasoning
Agents work with a few loaded files; they lack full codebase awareness. The language must enable understanding code in isolation, without hidden global dependencies or non-local effects.

#### 8. Dependency-Aware Build Tools
Go's model is ideal: no circular imports, clear package layout, cached test results. Build tooling should easily determine what needs rebuilding/retesting — agents thrive on predictability.

### What Agents Explicitly Hate

- **Macros** — Hard for humans, worse for agents. Generics/comptime produce recognizable patterns and are preferred.
- **Re-exports & Barrel Files** — Break the one-to-one mapping between declaration and import location. Go's per-directory flat namespace is a good middle ground.
- **Aliasing** — Agents complain about many aliases. A language should encourage good naming and discourage import-time aliasing.
- **Flaky Tests & Dev Env Divergence** — Agents both create and suffer from flaky tests. Languages should make deterministic tests the default.
- **Multiple Failure Conditions** — TypeScript's `tsc` passing while other checks fail can gaslight the agent. One command that definitively says pass/fail is ideal.

### Ronacher's Meta-Argument

> *"We are slowly getting to the point where facts matter more, because you can actually measure what works by seeing how well agents perform with it. No human wants to be subject to surveys, but agents don't care. We can see how successful they are and where they are struggling."*

He calls for: (1) **outsider art** — people who haven't built languages before trying their hand, and (2) **deliberate documentation** of what works from first principles, moving beyond opinion wars.

## Concrete Implementation: Zero by Vercel Labs (May 2026)

Three months after Ronacher's essay, Vercel Labs shipped **[[entities/zero-language|Zero]]** — a language that implements nearly all eight design principles in a single coherent package:

| Ronacher Principle | Zero Implementation |
|---------------------|----------------------|
| Context without LSP | JSON diagnostics with repair metadata work without editor tooling |
| Braced syntax | `{}` blocks, no significant whitespace |
| Explicit effects | `World` capability + `raises` keyword |
| Results over exceptions | `check` + `raises` + `choice` types |
| Minimal diffs | Braced syntax, explicit types → stable formatting |
| Grep-ability | `use std.codec` — package-qualified imports |
| Local reasoning | Signature declares all effects and capabilities |
| Dependency-aware builds | Package manifests (`zero.json`), explicit targets |

Zero's **agent-first tooling** goes beyond Ronacher's principles: its `--json` flag on `check`, `graph`, `size`, `routes`, and `doctor` produces structured output that agents consume programmatically. Diagnostics include **repair metadata** (`{"repair": {"id": "declare-missing-symbol"}}`) giving agents fix plans, not just error messages.

Key differentiator vs McKinney's Go/Rust framing: Zero is a **new language**, not a repurposed existing one. It validates Ronacher's thesis that the agent era creates space for language innovation. Launched May 15, 2026 — 2,045 GitHub stars in 3 days.

## Related Concepts

- [[concepts/harness-engineering/agentic-engineering]] — Professional patterns for coding agent usage
- [[concepts/vibe-coding-vs-agentic-engineering]] — Vibe coding vs professional agent use
- [[entities/wes-mckinney]] — Author of the agent ergonomics thesis (ecosystem/tooling perspective)
- [[entities/armin-ronacher]] — Language syntax/feature design perspective on agent-oriented languages
- [[concepts/programming-languages]] — Type systems, compilers, language design
