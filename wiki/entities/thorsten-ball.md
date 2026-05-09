---
title: Thorsten Ball
type: entity
created: 2026-05-04
updated: 2026-05-09
tags:
  - person
  - developer-tooling
  - sourcegraph
aliases:
  - thorstenball
  - mrnugget
sources:
  - raw/articles/2026-05-04_thorsten-ball-joy-and-curiosity-84.md
  - raw/articles/2026-02-19_ampcode-coding-agent-is-dead.md
  - raw/articles/2026-05-06_ampcode-neo-rebuilt.md
  - raw/articles/2025-04-15_ampcode-how-to-build-a-code-editing-agent.md
---

# Thorsten Ball

Thorsten Ball is a software engineer, technical author, and newsletter writer based in Germany. He is the author of two highly regarded books on programming language implementation, and writes the weekly **Register Spill** newsletter covering software engineering, AI, and the developer ecosystem.

## Key Facts

- **Books**: *Writing An Interpreter In Go* (2016) and *Writing A Compiler In Go* — self-published, widely praised for clarity and hands-on approach
- **Newsletter**: [Register Spill](https://registerspill.thorstenball.com) — weekly digest of software engineering insights (8,000+ subscribers)
- **Current**: Works remotely at [[entities/sourcegraph]] on [[entities/amp|Amp]] (ampcode.com), where he leads the coding agent product. Authored the influential "[[concepts/harness-commoditization|The Coding Agent Is Dead]]" manifesto (Feb 2026) and architected the [[concepts/amp-neo|Amp Neo]] rebuild (May 2026).
- **Previous**: Worked at [[entities/zed|Zed]] on the Zed code editor
- **Social**: [@thorstenball](https://twitter.com/thorstenball) on X/Twitter, @mrnugget on GitHub/Mastodon

## Books

### Writing An Interpreter In Go (2016)
A practical, step-by-step guide to building a complete interpreter (Monkey language) in Go. Known for demonstrating that programming language implementation is accessible with no prior compiler experience. The code from the original 2016 release (Go 1.7) still compiles and runs with Go 1.23 — a testament to Go's backward compatibility.

### Writing A Compiler In Go
Companion volume that extends the interpreter into a bytecode compiler and virtual machine. Together, the books form a complete, self-contained curriculum for understanding how programming languages work — from parsing to execution.

## Register Spill Newsletter

Weekly newsletter covering:
- Software engineering philosophy and the shifting developer tooling landscape
- AI/LLM impact on development practices and education
- Technical deep-dives (algorithms, security, performance)
- Curated insights from across the industry (the "messages I'd send if you'd asked me what's on my mind")

Notable issues:
- **Joy & Curiosity #84** (May 2026) — Covered software degradation, Mitchell Hashimoto leaving GitHub, AI-mediated competence loss, Mistral's strategy, Zed 1.0, and Daniel Lemire's SIMD algorithm

## Amp and Coding Agent Philosophy

Thorsten Ball is the primary author of Amp's strategic communications and technical direction. His writings have shaped the coding agent discourse:

- **"How to Build a Code-Editing Agent"** (April 2025) — [[concepts/minimal-coding-agent]] pattern: 400 lines of Go, three tools, heartbeat loop. Demonstrated agent harness simplicity.
- **"The Coding Agent Is Dead"** (February 2026) — Articulated the [[concepts/harness-commoditization]] thesis: frontier models have become so capable that harness differentiation is shrinking. Announced Amp's pivot from editor extensions to CLI-only.
- **"Amp, Rebuilt"** (May 2026) — Launched [[concepts/amp-neo|Amp Neo]]: remote-controllable, auto-compaction, Plugin API, 79% less CPU.

## Related

- [[entities/mitchell-hashimoto]] — Featured in Joy & Curiosity #84 (GitHub exodus)
- [[entities/zed]] — Former employer, code editor reaching 1.0
- [[entities/sourcegraph]] — Current employer
