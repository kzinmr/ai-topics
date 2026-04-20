---
title: Aleksey Kladov
created: 2026-04-09
updated: 2026-04-10
tags:
- person
- blogger
- hn-popular
- developer-tools
- compiler-tools
- language-server
- rust
- zig
- systems-programming
aliases:
- matklad
- matklad.github.io
---

# Aleksey Kladov

| | |
|---|---|
| **Blog** | [matklad.github.io](https://matklad.github.io) |
| **RSS** | https://matklad.github.io/feed.xml |
| **GitHub** | [@matklad](https://github.com/matklad) |
| **Role** | Creator of rust-analyzer, core contributor to tree-sitter ecosystem, compiler tools researcher |
| **Known for** | rust-analyzer (Rust LSP server), Resilient LL Parsing Tutorial, tree-sitter advocacy, IDE architecture |
| **Bio** | Compiler engineer and language tools researcher. Best known as the creator of rust-analyzer, the production-grade Language Server Protocol implementation for Rust. Writes extensively about compiler architecture, IDE design, parsing theory, build systems, and dependency management. Has also done significant analysis of Zig's design philosophy. |

## Overview

Aleksey Kladov (blog handle "matklad") is one of the most influential writers on compiler tooling and IDE architecture in the modern open-source ecosystem. As the creator and primary architect of **rust-analyzer**, he has shaped how the Rust language delivers IDE experiences to millions of developers. His blog is a rare combination of deep theoretical rigor and practical engineering — he doesn't just describe what works, he explains *why* the alternatives fail.

Kladov's writing spans compiler internals (parsing, incremental computation, code generation), IDE architecture (LSP design, editor integration, state management), and software engineering philosophy (dependency management, testing strategy, open-source ethics). His consistent thesis: **understand your data model first, push complexity to the edges, and let simplicity emerge from clear boundaries.**

## Core Ideas

### Three Architectures for Responsive IDEs

Kladov's framework for building IDE-grade compiler tooling identifies three architectural approaches, ranked by preference:

1. **Direct pipeline** — Parse, analyze, and serve from a clean data model. Preferred when the language supports separate compilation (e.g., Zig's per-file parsing).
2. **Immutable state + diff** — Maintain full semantic state, update immutably. Good for languages where files can't be parsed in isolation.
3. **Query-based incremental computation** — Model the compiler as a dependency graph of queries. The fall-back option when nothing else works.

> *"Listen to your inner Grug and push the need for queries as far down the compilation pipeline as possible, sticking to more direct approaches."*

His critique of query-based compilers (Salsa, rust-analyzer's incremental engine) is that profiling them is "a special genre of hurdle racing" — the indirection of the query system makes performance debugging nearly impossible. The best architecture avoids queries entirely by designing the language and compiler pipeline to minimize cross-file dependencies.

### Rust vs. Zig: A Scalability Comparison

Kladov has written extensively contrasting Rust and Zig as design philosophies:

- **Rust is a scalable language** — vertically (from embedded to web services) and horizontally (across large teams). Its module system, Cargo's rigid package semantics, and mandatory function signatures enable composability at scale. Rust "is not for lone genius hackers."
- **Zig is a spartan language** — aimed at producing "just the right assembly." It has one powerful feature (`comptime`) that subsumes most of Rust's special-cased machinery. Zig "kinda is" for lone hackers who want explicit control.

> *"Rust provides you with a language to precisely express the contracts between components. Zig provides you with a language to precisely express the machine."*

### The Fundamental Law of Software Dependencies

> *"Canonical source code for software should include checksums of the content of all its dependencies."*

Kladov's "law" extends beyond package lockfiles:
- **Source code** → mandates content-addressed VCS (git)
- **Third-party libraries** → mandates lockfiles with checksums
- **Compilers** → should specify *hashes*, not just versions, so you "no longer need to trust the party that distributes your compiler"
- **Build processes** → must be reproducible to produce meaningful hashes

The law is instrumental: the value isn't in the hashes themselves, but in the discipline required to achieve them — learning your actual dependency graph, automating downloads, fixing reproducibility, and isolating per-project dependencies.

### SemVer Is Not About You

Kladov reframes semantic versioning away from the prescriptivist debate ("are you using it right?") toward a descriptivist analysis of what version resolvers actually do:

> *"The real reason of SemVer is for managing transitive dependencies... SemVer is a library maintainer saying when two versions of their library can be unified."*

- If major is not bumped → versions can be unified (deduplicated)
- If major is bumped → duplication is forced
- Each new major version *virally amplifies* unsatisfiable dependency graphs across the ecosystem

He advocates the Ember 2.0 pattern ("deprecate than remove") as the fundamentally right way to handle major version bumps — but notes it still lacks a catchy name and widespread adoption.

### Resilient LL Parsing

Kladov's tutorial on resilient parsing established a new standard for language-server-grade parsers:

- **Resilience over error recovery** — "Incomplete code is the ground truth, and only the user knows how to correctly complete it." The parser should recognize valid structure from whatever is written, not attempt to guess fixes.
- **LL over GLR** — Code is written top-down and left-to-right, so LL parsers naturally recognize valid prefixes of incomplete constructs.
- **Dynamic syntax trees** — Use a flexible `Tree { kind, children }` structure rather than rigid ASTs, allowing errors anywhere in the tree.
- **Advancement assertions** — His recent "Parsing Advances" essay introduces `advance_push()`/`advance_pop()` to materialize the mental model of "this function consumes a token" into compile-time assertions, replacing OOM crashes with precise error locations.

### Open Source Moral Obligations

Kladov argues that publishing software with a proper README and installation instructions constitutes an implicit social contract:

> *"If I create expectations between me and my users, I am on the hook for conforming to them... The license says 'AS IS' but that's a statement about legality, not ethicality."*

His framework for maintainer obligations:
1. **Don't lie in your README** — non-negotiable baseline
2. **Don't be actively hostile to users** — no backdoors, no sabotaged releases
3. **Doing nothing is OK** — maintainers can stop working on a project without ethical violation
4. **Explicit carve-outs are allowed** — if your README says "hobby project, not for production," you've reset expectations

> *"If you publish your software and gain users, ask yourself: 'do I actually want to have users?' It is totally fine if the answer is 'no'!"*

### IDE Philosophy: Lower to Plain Text

Kladov consistently advocates for implementing IDE features by "lowering to plain text" rather than creating dedicated GUIs:

> *"In a smart editor, it is often possible to implement any given feature either by 'lowering' it to plain text, or by creating a dedicated GUI. And the lowering approach almost always wins, because it gets to re-use all existing functionality for free."*

His "Missing IDE Feature" essay — advocating for "fold method bodies by default" — exemplifies this: rather than a sidebar outline panel, fold the implementation details in-place, preserving native editing workflows (Shift+Down, Ctrl+X/V to move functions between blocks).

## Key Quotes

> *"Code is read more often than written, and this is one of the best multipliers for readability. Most of the code is in method bodies, but most important code is in function signatures."*

> *"The bigger benefit is that these asserts materialize the mental map of advancing functions in the source code, so it doesn't have to be mental anymore!"*

> *"Not doing queries is simpler, faster, and simpler to make faster."*

> *"There's no such thing as atomic upgrade of dependencies across the ecosystem. Propagating your new major version will virally amplify the number of unsatisfiable graph dependencies."*

> *"Resilience is a more fruitful framing than error recovery — incomplete code is the ground truth."*

> *"It is absolutely ok for a maintainer to do absolutely nothing."*

## Recent Themes (2024–2026)

### Parsing & Compiler Architecture
- **Against Query-Based Compilers** (Feb 2026) — His most comprehensive critique of the Salsa/incremental computation approach, advocating for manual chunking of compiler pipelines instead
- **Parsing Advances** (Dec 2025) — Introduced advancement assertions to prevent infinite loops in resilient LL parsers
- Continued development of tree-sitter ecosystem analysis and practical parsing tutorials

### IDE & Editor Tooling
- **A Missing IDE Feature** (Oct 2024) — Campaign for "fold method bodies by default" across all editors
- **LSP could have been better** (Oct 2023, still widely cited) — Architectural critique of LSP's RPC model, advocacy for level-triggered state synchronization
- **Zig Language Server And Cancellation** — Deep analysis of consistency models for language servers

### Dependency & Build Engineering
- **The Fundamental Law of Software Dependencies** (Sep 2024) — Checksums for everything, including compilers
- **SemVer Is Not About You** (Nov 2024) — Descriptivist reframing of version management
- **CI In a Box** — Reproducible, containerized CI workflows
- **Fast Rust Builds** — Practical optimization of large Rust workspace compilation

### Open Source Philosophy
- **Unless Explicitly Specified Otherwise, Open Source Software With Users Carries Moral Obligations** (Oct 2023) — Widely-shared essay on maintainer ethics
- **Open Source Can't Coordinate** — Analysis of why OSS projects struggle with large-scale coordination
- **Two Kinds of Code Review** / **Effective Pull Requests** — Process improvement for collaborative development

## Related

- [[rust]] — Programming language Kladov built IDE tooling for
- [[zig]] — Programming language Kladov frequently analyzes for architectural comparison
- [[language-server-protocol]] — Protocol Kladov has extensively critiqued and contributed to
- [[tree-sitter]] — Parsing library Kladov advocates for in IDE contexts
- [[incremental-computation]] — Architecture Kladov critiques as "hurdle racing" for profiling
- [[resilient-parsing]] — Kladov's approach to handling incomplete code in language servers

## Sources

- [Against Query Based Compilers](https://matklad.github.io/2026/02/25/against-query-based-compilers.html) (Feb 2026)
- [Parsing Advances](https://matklad.github.io/2025/12/28/parsing-advances.html) (Dec 2025)
- [A Missing IDE Feature](https://matklad.github.io/2024/10/14/missing-ide-feature.html) (Oct 2024)
- [The Fundamental Law Of Software Dependencies](https://matklad.github.io/2024/09/03/the-fundamental-law-of-dependencies.html) (Sep 2024)
- [SemVer Is Not About You](https://matklad.github.io/2024/11/23/semver-is-not-about-you.html) (Nov 2024)
- [Resilient LL Parsing Tutorial](https://matklad.github.io/2023/05/21/resilient-ll-parsing-tutorial.html) (May 2023)
- [Zig And Rust](https://matklad.github.io/2023/03/26/zig-and-rust.html) (Mar 2023)
- [LSP could have been better](https://matklad.github.io/2023/10/12/lsp-could-have-been-better.html) (Oct 2023)
- [Unless Explicitly Specified Otherwise, Open Source Software With Users Carries Moral Obligations](https://matklad.github.io/2023/10/18/obligations.html) (Oct 2023)
- [Rust Is a Scalable Language](https://matklad.github.io/2023/03/28/rust-is-a-scalable-language.html) (Mar 2023)
- [Zig Language Server And Cancellation](https://matklad.github.io/2023/05/06/zig-language-server-and-cancellation.html) (May 2023)
- [rust-analyzer Guide](https://rust-analyzer.github.io/book/contributing/guide.html)
