---
title: Russ Cox
type: entity
created: 2026-08-15
updated: 2026-08-15
aliases:
  - rsc
  - research.swtch.com
tags:
  - person
  - open-source
  - compiler
  - go
  - security
  - blogger
  - developer-tooling
sources:
  - raw/articles/research.swtch.com--nih--2cd8df91.md
  - https://research.swtch.com/nih
  - https://research.swtch.com/
---

# Russ Cox

**Russ Cox** (alias `rsc`) is an American software engineer best known as the tech lead of the **Go programming language** at Google (2012–2023), where he drove the language's toolchain, module system, and generics design. He is also the author of the long-running engineering blog at research.swtch.com, where his essays on code search, supply chain security, and compiler bootstrapping have become canonical references in the software-engineering community.

## Overview

Cox studied at Harvard and MIT (PhD under Frans Kaashoek, 2008), worked on the Plan 9 from Bell Labs successor research systems, and joined Google, where he became the de facto tech lead of the Go project after its public launch in 2009. Under his leadership the Go team shipped the 1.x release series, introduced the vendor/ then module-based dependency system (go modules, 2019), and designed the generics proposal that landed in Go 1.18 (2022). He stepped down as tech lead in 2023 (emeritus tech lead, succeeded by Austin Clements) but continues to write and speak about systems engineering.

His research.swtch.com blog is notable for deep, executable essays: "Regular Expression Matching with a Trigram Index" (2012, written after Google Code Search shut down — the n-gram inverted-index lineage cited in [[concepts/code-search-indexing]]), "Zip Files All The Way Down" (a Lempel-Ziv quine that constructs a zip file containing itself), and "Running the Reflections on Trusting Trust Compiler" (2023).

## Running the Reflections on Trusting Trust Compiler (Oct 2023)

The flagship supply-chain essay (raw: `raw/articles/research.swtch.com--nih--2cd8df91.md`): after Ken Thompson's 2023 SCaLE keynote Q&A — where Thompson revealed he still had the original backdoor code from his 1983 Turing Award lecture "Reflections on Trusting Trust" and that **no one had ever asked him for it** — Cox emailed him and became the first person in 40 years to receive `nih.a` ("not invented here"), the actual attack code.

The essay does three things:

1. **Explains the three-step attack** from the 1983 lecture: (Step 1) write a self-reproducing program (quine); (Step 2) notice a compiler can learn behaviors that persist only in its binary, not its source — Ken's example is the numeric values of C string escape sequences; (Step 3) inject the `login` backdoor through a corrupted compiler binary with no trace in source.
2. **Runs the real code**: Cox populated an online Research Unix V6 emulator (login `ken`/`ken`) with `nih.a`, extracted `x.c` + `rc`, and demonstrated `codenih` — the compiler hook that plants the backdoor during preprocessing while deliberately doing nothing when `cc -p` (preprocessor-only mode) is used, to avoid discovery.
3. **States the enduring lesson**: trust in the toolchain is irreducible — a compiler cannot be fully verified against a source-level backdoor, because the compiler is itself a program whose behavior is bootstrapped. This is the foundational case for [[concepts/software-supply-chain-security]].

The post also documents Thompson's controlled release story ("I got somebody to steal it from me, in a very controlled sense... they broke it, because of some technical effect, but they didn't find out what it was and then track it").

## Key Theses

- **Supply chain security is an old problem**: "Supply chain security is a hot topic today, but it is a very old problem" — the essay opens by dating it to October 1983.
- **Executable essays**: Cox's writing convention is that claims should be runnable — he ships emulators, simulators, and code so readers reproduce the result rather than taking his word.
- **Toolchain trust is bootstrapped**: the compiler you use today is compiled by a compiler, whose trust cannot be traced to source alone — the kernel of the trusting-trust argument and a core justification for reproducible builds and minimal bootstrapping.

## Related

- [[concepts/software-supply-chain-security]] — The concept page his trusting-trust essay anchors
- [[concepts/ai-supply-chain-security]] — The AI-era variant: release pipelines, CI/CD runners, package infrastructure
- [[concepts/code-search-indexing]] — His 2012 trigram-index post is a lineage ancestor of modern code search
- [[concepts/compiler-construction]] / [[concepts/compiler-design]] — Compiler internals context for the trusting-trust attack
- Ken Thompson (Bell Labs) — Turing Award lecture author; no entity page yet

## References

- research.swtch.com--nih--2cd8df91
- [research.swtch.com](https://research.swtch.com/) — Blog and research archive
- [Go project](https://go.dev) — Tech lead 2012–2023
