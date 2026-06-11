---
title: "HumanLayer (humanlayer.dev)"
type: entity
handle: "@humanlayerhq"
created: 2026-06-01
updated: 2026-06-01
tags:
  - company
  - ai-agents
  - harness-engineering
  - context-engineering
  - coding-agents
  - developer-tooling
  - open-source
aliases:
  - "humanlayer"
  - "humanlayerhq"
sources:
  - "https://humanlayer.dev/"
  - "https://hlyr.dev/ace" — Y Combinator talk: "Getting AI to Work in Complex Codebases" (August 2025)
  - "https://hlyr.dev/12fa" — 12-Factor Agents
  - "https://github.com/humanlayer/humanlayer"
  - "raw/articles/2025-08-29_humanlayer-advanced-context-engineering-coding-agents.md"
related:
  - "[[entities/dex-horthy]]"
  - "[[concepts/context-engineering|Context Engineering]]"
  - "[[concepts/agent-harness]]"
  - "[[concepts/spec-driven-development]]"
---

# HumanLayer

HumanLayer is a company founded by [[entities/dex-horthy|Dex Horthy]] that builds tools for **spec-first, agentic software development**. The company is a key voice in the context engineering and harness engineering movements, focusing on making AI coding agents work reliably in large, brownfield codebases.

## Mission

HumanLayer's core thesis: **the hardest part of AI coding agents is not the model — it's context management**. Their tools and frameworks help engineering teams adopt structured workflows that treat the context window as a finite, degrading resource that must be deliberately managed.

## Products

### HumanLayer Library (Open Source)

An open-source library for **human-in-the-loop agent patterns**. Provides primitives for:
- Approval gates before destructive agent actions
- Structured human review checkpoints in agent workflows
- Integration with existing coding agent harnesses (Claude Code, Codex, Cursor)

### CodeLayer (Private Beta, August 2025)

Described as a "Post-IDE IDE" — "Superhuman for Claude Code." CodeLayer enables:
- Collaborative frequent intentional compaction workflows across large teams
- Spec-first development with research docs and plan files as the source of truth
- Team coordination around AI-generated code reviews and PRs

## Key Contributions

### Frequent Intentional Compaction (FIC)

HumanLayer's signature methodology for getting AI coding agents to work in large brownfield codebases (300K+ LOC). A structured **Research → Plan → Implement** pipeline with human review checkpoints at the highest-leverage points.

**Results from the BAML engagement** (300K LOC Rust codebase):
- Bug fix PR approved overnight by maintainer
- 35K LOC of cancellation + WASM support shipped in 7 hours (estimated 3–5 days each for senior engineer)
- Team of 3 averaging ~$12K/month on Claude Opus tokens
- One developer shipping 6 PRs in a day, rarely editing non-markdown files by hand

### 12-Factor Agents

HumanLayer published the **12-Factor Agents** framework, adapting the Twelve-Factor App methodology to AI agent design. Covers statelessness, context management, tool design, and agent lifecycle patterns.

## Philosophy

- **Spec-driven development**: Specs/plans/research docs are the "real code" — the source of truth for what is being built and why, analogous to source code vs. compiled binary
- **Human review at highest-leverage points**: A bad line of research can cause thousands of bad lines of code. Review research and plans, not just final code
- **Context window optimization**: Every token that enters the window must earn its place. Optimize for correctness → completeness → size → trajectory
- **40–60% context utilization**: Keep the context window partially empty to leave room for reasoning

## Cross-References

- [[entities/dex-horthy]] — Founder
- [[concepts/context-engineering|Context Engineering]] — FIC methodology documented here
- [[concepts/agent-harness]] — HumanLayer's approach to harness design
- [[concepts/spec-driven-development]] — Related philosophy
- [[entities/hellovai]] — BoundaryML/BAML collaborator on live coding sessions
