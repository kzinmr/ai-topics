---
title: "Vercel Labs"
type: entity
created: 2026-05-18
updated: 2026-10-19
tags:
  - company
  - product
  - open-source
  - developer-tooling
  - programming-language
  - infrastructure
sources:
  - raw/articles/2026-05-18_vercel-labs_zero-language-for-agents.md
---

# Vercel Labs

**Vercel Labs** is the research and development division of **Vercel**, the frontend cloud and web deployment platform. In May 2026, Vercel Labs released **Zero**, a systems programming language designed explicitly for AI agent—first development.

## Zero Language

See [[concepts/agent-first-design]] for the full concept page. Key features:
- **Capability-based I/O** — functions declare what they touch via `World` capability; compiler rejects unavailable capabilities at compile time
- **Explicit effects** — `raises` keyword for fallibility, `check` for fallible operations
- **Cross-target checks** — compiler verifies target-neutral code for multiple targets
- **C boundary support** — C ABI exports, target-aware interop metadata
- **Agent-first tooling** — all diagnostics output structured JSON with repair metadata and stable diagnostic codes

Zero is Apache 2.0 licensed. Lead contributor: ctate. Written primarily in C (65.9%).

## Relation to Vercel

Vercel is primarily known for:
- **Frontend Cloud** — hosting and deployment platform for Next.js and modern web apps
- **Next.js** — React framework (sponsors its development)
- **Edge Functions** — serverless compute at the edge

Zero represents Vercel Labs' bet on the **agent-first future of programming**, where agent-tooling compatibility becomes a competitive advantage for developer platforms.

## Other Vercel Labs projects (2026)

- **scriptc** — an experimental **TypeScript-to-native compiler** (compiles TS/JS to native executables and WebAssembly using type info; static builds need no Node/JS engine). Self-hosted (compiles its own source) as of Sep 2026; **tsc-ts** (Oct 2026) proves the pipeline by compiling a full TypeScript port of the tsgo 7.0.2 compiler, 2.8–4.2× faster than tsgo on real codebases. See [[concepts/scriptc-typescript-native-compiler]].
- **tsc-ts** — TypeScript-written port of the TypeScript 7.0.2 (tsgo) compiler, natively compiled by scriptc; verified stage-by-stage against tsgo on TypeScript's test corpus. `npm i tsc-ts`.
- **fx** ([vercel-labs/fx](https://github.com/vercel-labs/fx)) — "The tiny open native coding agent", a Unix-like minimal CLI coding-agent harness (Zig, Apache-2.0). Featured by [[entities/chris-tate|Chris Tate]], including running Sonnet 5.5 in it.
- **json-render** / **agent-browser** / **Is Agentic** — see [[entities/chris-tate]].

## Related

- [[concepts/agent-first-design]] — The agent-first language design philosophy Zero exemplifies
- [[entities/armin-ronacher]] — Theorized the design principles Zero implements
- [[entities/vercel]] — Parent company and platform
- [[concepts/harness-engineering/agent-ergonomics]] — Broader agent-tool interaction design
