---
title: 'Eve (Legal AI)'
created: 2026-08-10
updated: 2026-08-10
type: entity
tags:
  - company
  - legal-tech
  - ai-agents
  - multi-agent
  - voice-ai
  - startup
sources:
  - raw/newsletters/2026-08-09-exclusive-interview-with-the-co-founder-ceo-of-eve-jay-madheswaran.md
  - https://read.getsuperintel.com/p/exclusive-interview-with-the-co-founder-ceo-of-eve-jay-madheswaran
---

# Eve (Legal AI)

**Eve** is a legal-tech AI company building an AI operating system for law firms. Founded in 2023 by **Jay Madheswaran** (Co-Founder & CEO), Eve raised a **$103 million Series B** at a valuation above **$1 billion** in September 2025. In June 2026 the company launched **EveOS**, pitched as an operating system for a law firm rather than another tool inside one. Eve reports more than **1,400 plaintiff firms** and over **200,000 active matters** on the platform.

> **Disambiguation:** this page covers the legal AI company Eve. [[entities/vercel-eve|Vercel's Eve]] is a different thing — an open-source agent framework for building durable AI agents, unrelated to legal tech.

## Key Facts

- **Founded:** 2023, by Jay Madheswaran
- **Funding:** $103 million Series B at a valuation above $1 billion (September 2025)
- **Flagship product:** EveOS, launched June 2026 — an operating system for a law firm, not another tool inside one
- **Scale:** 1,400+ plaintiff firms; 200,000+ active matters on the platform
- **Focus:** plaintiff-side firms — intake, case data, and matter workflows
- **Naming:** the company was formerly known as Eve Legal; it now brands simply as Eve (distinct from [[entities/vercel-eve|Vercel's Eve]])

## Multi-Agent Architecture

Per the August 2026 Superintel+ exclusive interview, Eve runs a multi-agent architecture in which specialized agents divide up a case file between them:

- **Atlas** — the case data layer. Per Madheswaran: *"Everything starts with Atlas, which is our case data layer."* Atlas ingests and structures case data that the other agents build on.
- **Jenny** — the AI voice specialist handling intake, capturing new matters as they come in.
- **Auditor** — takes the review/audit portion of the case file, checking the work of the other agents.
- **Analyst** — takes the analysis portion of the case file, working on top of Atlas's data layer.

The division of labor across named agents mirrors the team-of-agents pattern seen elsewhere in the agent ecosystem (see [[concepts/multi-agents/agent-team-swarm]]).

## Positioning

Eve positions EveOS as the operating system for the modern law firm, going head-to-head with [[entities/harvey|Harvey]], the legal AI incumbent. Where Harvey targets large firms and enterprises (100,000+ lawyers, 60%+ of the AmLaw 100, built on citation-grounded research and workflow agents), Eve focuses on **plaintiff firms** and sells a platform-level operating system rather than point tools. Eve's multi-agent design — with Atlas as the case data layer and Jenny handling voice-based intake — differentiates it on intake experience and matter-scale operations, a different wedge into the legal AI market than Harvey's big-law research and drafting focus.

## Related

- [[entities/harvey]] — the legal AI incumbent and Eve's primary competitor
- [[entities/vercel-eve]] — Vercel's agent framework also named "Eve" (different company, unrelated product)
- [[concepts/multi-agents/agent-team-swarm]] — the multi-agent team division-of-labor pattern Eve's architecture follows

## Sources

- Superintel+ exclusive interview with Jay Madheswaran, Co-Founder & CEO of Eve (2026-08-09), captured in `raw/newsletters/2026-08-09-exclusive-interview-with-the-co-founder-ceo-of-eve-jay-madheswaran.md`
- https://read.getsuperintel.com/p/exclusive-interview-with-the-co-founder-ceo-of-eve-jay-madheswaran
