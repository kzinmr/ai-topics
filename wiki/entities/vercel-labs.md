---
title: "Vercel Labs"
type: entity
created: 2026-05-18
updated: 2026-05-18
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

## Related

- [[concepts/agent-first-design]] — The agent-first language design philosophy Zero exemplifies
- [[entities/armin-ronacher]] — Theorized the design principles Zero implements
- [[concepts/vercel]] — Parent company and platform
- [[concepts/agent-ergonomics]] — Broader agent-tool interaction design
