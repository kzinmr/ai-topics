---
title: "Compiler Explorer (Godbolt)"
type: concept
aliases:
  - compiler-explorer
  - godbolt
  - Compiler Explorer
created: 2026-04-25
updated: 2026-11-18
tags:
  - concept
  - developer-tooling
  - compiler
  - developer-tools
  - open-source
sources:
  - https://godbolt.org/
  - https://github.com/compiler-explorer/compiler-explorer
---

# Compiler Explorer (Godbolt)

**Compiler Explorer** — universally known as **Godbolt**, after its creator Matt Godbolt — is the web service at [godbolt.org](https://godbolt.org/) that compiles C, C++, Rust, D, Haskell, Go, Zig, and ~40 other languages on demand and shows the **generated assembly side by side with the source**, with each machine instruction highlighted back to the line that produced it. It is the standard tool for the question "what does my code *actually* become?", and it quietly became shared infrastructure for compiler research, performance engineering, and — increasingly — **AI-agent verification of code generation**.

## How it works

```
┌─────────────── Browser UI (Monaco editor) ───────────────┐
│  source pane  │  assembly pane  │  output / exec pane     │
└───────┬───────────────────────────────────────────────────┘
        │ REST/WS
┌───────▼──────────────────────────────┐
│  Compiler Explorer server (TypeScript)│
│  compiles via remote "compilers"      │
└───────┬──────────────────────────────┘
        │ ssh/exec queues
┌───────▼──────────────────────────────┐
│  Compiler farm (AWS / GCP instances)  │
│  hundreds of compiler versions:        │
│  gcc 2.1 → trunk, clang 3.0 → trunk,  │
│  msvc, rustc, gccrs, zig, icpx …       │
└──────────────────────────────────────┘
```

Key properties that made it indispensable:

- **Every historical compiler version is addressable** — you can diff how clang 9 vs clang 18 optimizes the same loop, which turned micro-optimization folklore into reproducible evidence.
- **Per-line assembly attribution** — the visual core of countless "what does the compiler do" blog posts (SIMD, autovectorization, and performance-engineering discussions).
- **Execution mode** — compile-and-run with output, making it a lightweight compiler fuzzing/teaching harness.
- **Permanent permalinks + `shortlink` API** — every claim in a blog post or bug report can pin an exact compiler/version/options triple. This reproducibility is why GCC/LLVM bug reports routinely embed godbolt links.

## The AI-agent connection

Two directions link Godbolt to this wiki's core subject:

1. **Agents as compiler-bug hunters.** LLM agents have found real miscompiles in GCC/Clang/ICC — Matt Godbolt's own tooling and community have been central to the "finding miscompiles for fun and not profit" line of work ([[concepts/ai-agent-compiler-bug-finding]], [[concepts/carlini-c-compiler-agents]]). Compiler Explorer's one-click reproducible compiler matrix is the test bench these agents target; differential testing across versions is essentially automated Godbolt usage ([[concepts/american-fuzzy-lop]], [[concepts/fuzzing]]).
2. **Agents verifying their own generated code.** An emerging agent pattern: after generating C/C++/Rust, query the Compiler Explorer API to inspect emitted assembly (did the loop vectorize? did bounds checks vanish?) before shipping — using the compiler's output as a **verification signal**, not just a build artifact.

## Matt Godbolt

The service was created in 2012 by **Matt Godbolt**, a C++ developer (Bloomberg, Jane Street, Optiver) who built it as a weekend project and has maintained it as open source (GitHub: `compiler-explorer/compiler-explorer`, ~10k stars) with community sponsorship. Godbolt is a frequent conference speaker on compiler realities and C++ performance; the project runs on cloud credits donated by AWS/GCP/ARM and a compiler-farm operation that is itself an interesting piece of infrastructure (per-version containerized toolchains, queueing, cost management).

## Related Concepts

- [[concepts/compiler-design]] / [[concepts/compiler-construction]] — the discipline the tool illustrates
- [[concepts/ai-agent-compiler-bug-finding]] — LLM agents finding miscompiles
- [[concepts/carlini-c-compiler-agents]] — Agentic coding for C compiler bugs
- [[concepts/fuzzing]] — differential testing across compiler versions
- verification of agent-produced code (cf. [[concepts/ai-agent-compiler-bug-finding]])


## Sources

- [godbolt.org](https://godbolt.org/)
- [compiler-explorer/compiler-explorer on GitHub](https://github.com/compiler-explorer/compiler-explorer)
- Matt Godbolt's talks, e.g. "Massively Parallel Programming" / CppCon material
