---
title: "Eli Bendersky"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Eli Bendersky

**URL:** https://eli.thegreenplace.net
**Blog:** eli.thegreenplace.net (thegreenplace.net)
**GitHub:** eliben
**Projects:** pycparser, Bob (Scheme compiler), llvm-clang-samples, wasm-wat-samples, go-ungrammar

## Overview

Eli Bendersky is a systems programmer, compiler enthusiast, and one of the most consistent technical bloggers in the industry. His website thegreenplace.net has been publishing since 2004, accumulating over 1,000 posts spanning C & C++, Python, Go, Rust, LLVM, WebAssembly, compilers, mathematics, machine learning, and hardware.

His most widely used project is **pycparser** (~20M daily downloads from PyPI), a pure-Python C parser that produces Python-style ASTs. He is also the creator of **Bob**, a suite of Scheme language implementations (interpreter, compiler, VM) in Python, recently extended with a WebAssembly compiler targeting the WASM GC extension.

Bendersky's writing is characterized by methodical depth, mathematical rigor, and a commitment to understanding systems from first principles. His recent work has focused heavily on compilers (recursive-descent parsing, WebAssembly code generation, LLVM integration), developer tooling (go generate, AST rewriting), and the intersection of LLMs with traditional software engineering practices.

## Timeline

| Date | Event |
|------|-------|
| 2004 | Began publishing thegreenplace.net — a technical blog covering programming, math, and science |
| 2008 | Created pycparser — a pure-Python C parser using PLY (Python Lex-Yacc) |
| 2010 | Published llvm-clang-samples — self-contained examples of using LLVM and Clang as libraries |
| 2011 | Created Bob — a suite of Scheme implementations in Python (interpreter, compiler, VM) |
| 2014 | Published "Samples for using LLVM and Clang as a library" — explaining the design principles behind llvm-clang-samples |
| 2020 | Published notes on x86-64 stack frame layout — a widely-referenced systems programming resource |
| 2021 | Published "Rewriting Go source code with AST tooling" — comprehensive guide to go/ast and astutil |
| 2021 | Published "A comprehensive guide to go generate" — the definitive reference on Go code generation |
| 2023 | Created go-ungrammar — a Go implementation of the Ungrammar DSL for concrete syntax trees |
| 2024 | Published "Notes on running Go in the browser with WebAssembly" |
| 2024 | Published "Asking an LLM to build a simple web tool" — early exploration of AI-assisted development |
| 2025 | Published "Revisiting 'Let's Build a Compiler'" — translating Jack Crenshaw's classic tutorial to Python/WASM |
| 2025 | Published "LaTeX, LLMs and Boring Technology" — argument for staying with proven tools in the AI era |
| 2025 | Published notes on WASM Basic C ABI, Implementing Forth in Go and C, Bloom filters, Attention mechanisms |
| 2026 | Published "Rewriting pycparser with the help of an LLM" — collaborating with Codex to replace PLY with a hand-written recursive-descent parser |
| 2026 | Published "Compiling Scheme to WebAssembly" — adding WASM GC target to the Bob project |
| 2026 | Published mathematical notes on Lagrange interpolating polynomials and linear algebra for polynomials |

## Core Ideas

### Boring Technology + LLMs = Power Multiplier

In "LaTeX, LLMs and Boring Technology" (October 2025), Bendersky articulated a counterintuitive thesis: the rise of LLMs makes boring technology *more* valuable, not less. His argument:

> "Depending on your particular use case, choosing boring technology is often a good idea. Recently, I've been thinking more and more about how the rise and increase in power of LLMs affects this choice. By definition, boring technology has been around for a long time. Piles of content have been written and produced about it: tutorials, books, videos, reference manuals, examples, blog posts and so on. All of this is consumed during the LLM training process, making LLMs better and better at reasoning about such technology."

This is a profound insight for developer tooling: the tools that will be most augmented by AI are not the new ones, but the ones with decades of accumulated knowledge in their training data. LaTeX, C, Python, SQL — these "boring" technologies become more powerful when paired with LLMs because the models have simply seen more of them.

Conversely, shiny new technologies (Typst, Zig, etc.) have less training material and therefore get less benefit from AI augmentation.

### Recursive-Descent Parsing as the Right Default

Bendersky has been a consistent advocate for hand-written recursive-descent parsers over parser generators. This position was shaped by his encounter with Jack Crenshaw's "Let's Build a Compiler" tutorial in 2003:

> "When I first encountered it (2003), it was taken for granted that if you want to write a parser then lex + yacc are the way to go. Following the development of a simple and clean hand-written parser was a revelation that wholly changed my approach to the subject; subsequently, hand-written recursive-descent parsers have been my go-to approach for almost 20 years now."

This philosophy directly motivated his 2026 pycparser rewrite: replacing the PLY-based YACC parser with a hand-written recursive-descent implementation, collaborated on with an LLM coding agent.

### LLMs as Collaborative Partners, Not Replacements

Bendersky's 2026 post "Rewriting pycparser with the help of an LLM" is one of the most nuanced accounts of AI-assisted programming from an experienced systems programmer. He didn't ask an LLM to write the parser — he designed the approach, wrote the conformance tests, set up the prompts, reviewed the output iteratively, and made the architectural decisions:

> "Could I have done this myself, without an agent's help? Sure. But it would have taken me much longer, assuming that I could even muster the will and concentration to engage in this project. I estimate it would take me at least a week of full-time work."

His key insight: the value of LLMs in systems programming is not in replacing human understanding but in eliminating the "potential well" — the mental overhead that prevents experienced developers from tackling projects they know how to do but don't feel like doing.

### Conformance Testing as the Safety Net for AI-Assisted Development

Bendersky identified why LLM agents succeed on some projects and fail on others:

> "Agents seem to do well [with] conformance suites. And pycparser has a very extensive one. Over 2500 lines of test code parsing various C snippets to ASTs. I figured the LLM can either succeed or fail and throw its hands up in despair, but it's quite unlikely to produce code that passes all tests by accident."

This is a critical principle: the more comprehensive your test suite, the more safely you can delegate implementation to an LLM. The tests define the contract; the LLM fills in the implementation.

### Strong Typing Makes AI More Effective

From the pycparser rewrite experience, Bendersky drew a practical conclusion about language choice:

> "While working on this, it became quite obvious that static typing would make the process easier. LLM coding agents benefit from type information. Based on this experience, I'd bet that coding agents will be somewhat more effective in strongly typed languages like Go, TypeScript and especially Rust."

This is an empirical observation, not an ideological preference — derived from the actual experience of collaborating with Codex on a complex refactoring project.

### WebAssembly as a Compilation Target Worth Understanding

Bendersky's recent work has focused heavily on WebAssembly as both a runtime and a compilation target. His work includes:

- Notes on the WASM Basic C ABI (November 2025)
- Compiling Scheme to WebAssembly using the WASM GC extension (January 2026)
- Revisiting "Let's Build a Compiler" with WASM as the output target (December 2025)
- Notes on running Go in the browser with WebAssembly (October 2024)

His approach is characteristically practical: he doesn't just theorize about WASM, he builds real compilers targeting it, works through the ABI details, and documents the gotchas.

### LLVM as a Library — With Realistic Expectations

In 2014, Bendersky published llvm-clang-samples to address a real gap: LLVM's C++ API is powerful but poorly documented for library use, and the API changes constantly. His repository provides self-contained, buildable examples that work against specific LLVM releases.

His approach to API stability is pragmatic: "LLVM's and Clang's C++ API is changing constantly; C++ API stability is not a design goal of the LLVM community." Rather than fighting this, he embraces it — maintaining the repository against both released versions and bleeding-edge revisions.

### go generate: Code Generation Without Metaprogramming

His 2021 guide "A comprehensive guide to go generate" remains the definitive reference on Go's code generation ecosystem. He emphasizes that `go generate` is deliberately minimal:

> "It's very important to emphasize that the above is the whole extent of automation Go provides for code generation. For anything else, the developer is free to use whatever workflow works for them."

This minimalism appeals to his engineering sensibility — provide the mechanism, not the policy. Let developers build what they need on top of simple primitives.

### Resilient Parsing: Don't Quit on the First Error

When implementing go-ungrammar, Bendersky invested significant effort in error recovery:

> "Just for fun, I spent more time on error recovery than strictly necessary for such a simple input language. The lexer never gives up when encountering non-sensical input; it simply emits an ERROR token and keeps going. The parser doesn't quit on the first error either; instead, it collects all the errors it encounters and tries to recover."

This is the mark of someone who builds tools for humans, not just for machines. A parser that crashes on the first error is technically correct but practically useless. A parser that recovers and reports all errors is genuinely helpful.

### Mathematics as a Lens on Systems

Bendersky's blog regularly features mathematical explorations — polynomial interpolation, linear algebra, convolutions, softmax derivatives, Hilbert spaces, Cramer's rule, Bloom filters. These aren't abstract exercises; they're directly connected to his systems programming work. Understanding the math behind attention mechanisms, for example, informs how you implement them efficiently.

### Scheme as a Teaching Language

The Bob project — his suite of Scheme implementations — has been a vehicle for exploring language design for over 15 years. Adding a WebAssembly compiler in 2026 demonstrates his commitment to using Scheme as a testbed for new compilation targets:

> "Scheme has built-in data structures, lexical closures, garbage collection, etc. It's much more challenging [than toy languages that are at the C level]."

The WASM GC extension makes this particularly interesting: representing Scheme's objects (pairs, symbols, closures) in a typed garbage-collected WASM environment requires careful mapping between the language's semantics and the runtime's capabilities.

### Book Reviews as Technical Analysis

Bendersky's quarterly reading summaries are unusually technical. When reviewing "Rust Atomics and Locks" by Mara Bos, he doesn't just summarize — he critiques the absence of benchmarks:

> "It would be nice if the accompanying repository had test harnesses to observe how the code behaves, and some benchmarks. Without this, many claims made in the book feel empty without real data to back them up."

This reflects his broader philosophy: claims without evidence are just opinions. Systems programming requires measurement, not just description.

## Key Quotes

> "By definition, boring technology has been around for a long time. Piles of content have been written and produced about it. All of this is consumed during the LLM training process, making LLMs better and better at reasoning about such technology."

> "Following the development of a simple and clean hand-written parser was a revelation that wholly changed my approach to the subject."

> "Agents seem to do well [with] conformance suites. And pycparser has a very extensive one. I figured the LLM can either succeed or fail, but it's quite unlikely to produce code that passes all tests by accident."

> "While working on this, it became quite obvious that static typing would make the process easier. LLM coding agents benefit from type information."

> "Could I have done this myself, without an agent's help? Sure. But it would have taken me much longer, assuming that I could even muster the will and concentration to engage in this project."

> "Without benchmarks, many claims made in the book feel empty without real data to back them up."

> "LLVM's and Clang's C++ API is changing constantly; C++ API stability is not a design goal of the LLVM community."

> "The lexer never gives up when encountering non-sensical input; it simply emits an ERROR token and keeps going."

> "Scheme has built-in data structures, lexical closures, garbage collection, etc. It's much more challenging [than toy languages]."

> "It's very important to emphasize that [go generate's] automation is the whole extent of automation Go provides. For anything else, the developer is free to use whatever workflow works for them."

## Recent Themes (2024–2026)

- **LLM-assisted development**: Using Codex for complex refactoring projects (pycparser rewrite)
- **WebAssembly compilation**: Scheme → WASM, Go → WASM, C → WASM ABI exploration
- **Compiler education**: Translating classic compiler tutorials to modern languages and targets
- **Boring technology advocacy**: Arguing for proven tools augmented by LLMs over shiny new alternatives
- **Static typing for AI**: Observing that LLM agents work better with type information
- **Conformance testing**: Using extensive test suites as safety nets for AI-assisted refactoring
- **Mathematical foundations**: Polynomial interpolation, linear algebra, attention mechanisms
- **Developer tooling**: go generate, AST rewriting, resilient parsing, plugin systems

## Related Concepts

- [[concepts/pycparser]] — His most widely used project (~20M daily downloads), pure-Python C parser
- [[concepts/webassembly]] — Recent focus as both compilation target and runtime
- [[concepts/compiler-design]] — Recursive-descent parsing, syntax-directed translation, code generation
- [[concepts/llvm]] — Library usage, API stability challenges, Clang tooling
- [[concepts/go-tooling]] — go generate, AST rewriting, astutil, stringer
- [[concepts/llm-assisted-development]] — Practical experience with Codex and other AI coding agents
- [[concepts/boring-technology]] — His thesis on proven tools + LLMs vs. shiny new alternatives
-  — The Bob project: interpreter, compiler, VM, WASM target
-  — Using test suites as safety nets for AI-assisted refactoring
-  — Error recovery in lexers and parsers

## Influence Metrics

- pycparser: ~20M daily downloads from PyPI, the most widely used pure-Python C parser
- llvm-clang-samples: widely referenced for learning LLVM/Clang library usage
- "A comprehensive guide to go generate": definitive reference in the Go ecosystem
- His blog has published 1,000+ posts since 2004 across compilers, systems programming, math, and ML
- "Rewriting pycparser with the help of an LLM" (2026): influential account of AI-assisted systems programming
- "LaTeX, LLMs and Boring Technology" (2025): widely cited argument for proven tools in the AI era
- Consistent presence on Hacker News and r/programming with high-quality technical analysis

## References

- eli.thegreenplace.net--2026-thoughts-on-webassembly-as-a-stack-machine--370f4288
