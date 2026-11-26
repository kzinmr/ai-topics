---
title: "ZJIT"
type: concept
aliases:
  - zjit
  - Ruby ZJIT
created: 2026-04-25
updated: 2026-11-26
tags:
  - concept
  - compiler
  - open-source
related:
  - "[[entities/max-bernstein]]"
  - "[[concepts/yjit]]"
sources:
  - https://github.com/Shopify/zjit
  - https://github.com/ruby/ruby/tree/master/zjit
  - raw/articles/bernsteinbear.com--blog-inlining-heuristics--48699265.md
---

# ZJIT

**ZJIT** is the next-generation **method-level just-in-time compiler for Ruby**, developed by Shopify (notably [[entities/max-bernstein|Max Bernstein]]) and now **upstreamed into CRuby** (`ruby/ruby`, `zjit/` directory). It is a deliberate second attempt at Ruby JITing: where YJIT compiles YARV bytecode block-by-block to low-level IR, ZJIT compiles **entire methods** through a **high-level SSA-based intermediate representation**.

## Why a Second Ruby JIT?

| Dimension | YJIT | ZJIT |
|---|---|---|
| Compilation unit | Basic block | Whole method |
| IR | Low-level, direct to machine code | High-level SSA-based IR |
| Optimization style | Interprocedural, type-feedback heavy | Traditional compiler pipeline |
| Design goal | Maximum speed | Readability, modularity, approachability for outside contributors |
| Language of implementation | Rust | Rust |

The design philosophy is intentionally **textbook**: ZJIT sacrifices some of YJIT's type-feedback interprocedural optimizations in exchange for a clean, modular compiler architecture that a new contributor can actually understand end-to-end. Bernstein has been transparent about its early state — openly sharing benchmarks, inlining heuristics experiments, deopt tracing (Perfetto), and unresolved design decisions on his blog.

## Timeline

- **2024–2025** — Developed at Shopify as a research project (`Shopify/zjit`); public write-ups on railsatscale and Bernstein's blog.
- **Upstreamed** — Merged into `ruby/ruby` as the `zjit/` directory; the Shopify repo now states "development has moved... this repository is mostly for historical interest."

## Key Engineering Topics (via Bernstein's blog)

- **Inlining heuristics** — when method-level compilation pays for itself
- **SSA from bytecode** — building an SSA IR from YARV stack bytecode
- **Partial SSI / local variables support** — speculation and deoptimization
- **Perfetto tracing** — visualizing side-exits, guard failures, and deopts instead of guessing

> "An IR is not a data structure. It's a way of thinking about a program."
> — Max Bernstein, *What I talk about when I talk about IRs*

## Related

- [[entities/max-bernstein]] — core ZJIT developer; five-runtime compiler engineer
- [[concepts/yjit]] — the preceding Ruby JIT (Shopify, 2021)
- Compiler/runtime lineage: Bernstein's work spans Skybison, Cinder, CPython, PyPy, Pyjion — ZJIT is his fifth-runtime perspective applied to Ruby

## Sources

- [Shopify/zjit (historical)](https://github.com/Shopify/zjit) — scraped 2026-11-26
- [ruby/ruby zjit/ directory](https://github.com/ruby/ruby/tree/master/zjit)
- [bernsteinbear.com](https://bernsteinbear.com) — ZJIT design & performance posts
