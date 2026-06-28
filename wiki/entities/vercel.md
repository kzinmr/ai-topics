---
title: "Vercel"
created: 2026-05-06
updated: 2026-06-28
type: entity
tags:
  - entity
  - company
  - platform
  - developer-tooling
  - open-source
  - security
aliases:
  - "Vercel Inc."
  - "vercel.com"
related:
  - concepts/harness-engineering
  - entities/openai
  - entities/vercel-eve
sources:
  - raw/newsletters/2026-05-05-codex-is-gaining-steam.md
  - https://open.substack.com/pub/bensbites/p/codex-is-gaining-steam
  - raw/articles/2026-06-27_vercel-building-agents-with-eve-framework.md
---


# Vercel

**Vercel** is a frontend cloud platform (known for Next.js) that has expanded into the AI agent ecosystem. In May 2026, Vercel released **deepsec**, an open-source security harness using coding agents to find and fix vulnerabilities.

## Overview

| Detail | Value |
|--------|-------|
| **Founded** | 2015 |
| **CEO** | Guillermo Rauch |
| **Key Product** | Vercel platform (Next.js hosting, edge functions) |
| **AI Expansion** | deepsec security harness (May 2026), AI SDK |

## deepsec (May 2026)

**deepsec** is an **open-source security harness** that uses coding agents to automatically find and fix vulnerabilities in codebases. Key characteristics:

- **Agent-driven**: Coding agents scan code for vulnerabilities
- **Automated remediation**: Agents propose and apply fixes
- **Open-source**: Available to the broader ecosystem under an open-source license
- **Harness paradigm**: Fits the [[concepts/harness-engineering]] model — the harness provides the security evaluation framework while coding agents execute within it

### Harness Engineering Context

deepsec exemplifies the **harness engineering** concept where the execution environment is designed to constrain and guide agents:

```
Agent scans code → Harness evaluates findings → Agent proposes fix → Security review gates approval
```

### Comparison to Other Security Approaches

| Tool | Approach | Scope |
|------|----------|-------|
| **Vercel deepsec** | Coding agents in security harness | Vulnerability discovery + automated fix |
| **Devin for Security** | AI agent vulnerability remediation | Pre-existing vulnerability detection + patching |
| **Cursor CI-fix** | Agent monitors CI failures | CI failure remediation |
| **Palantir AIP** | Enterprise security + governance | Platform-level security |

## Eve: Filesystem-First Agent Framework (June 2026)

**[[entities/vercel-eve|Eve]]** is Vercel's open-source (Apache 2.0) framework for building and deploying durable backend AI agents. Announced June 17, 2026, its core idea is that an agent is a directory of files — tools, skills, subagents, schedules, evals, connections, and channels live as plain files on disk, auto-discovered by name. Vercel runs 100+ Eve agents internally, including d0 (30K questions/month), Vertex (92% ticket resolution), and Athena (sales agent built in 6 weeks with no engineers). GitHub: 2,857 ★, 214 forks (as of Jun 28).

## AI Ecosystem Role

Vercel is expanding beyond its frontend hosting roots into AI infrastructure:
- **Eve agent framework**: Filesystem-first durable agent framework (Jun 2026)
- **AI SDK**: Helping developers build AI-powered web applications
- **OpenAI Agents SDK support**: Listed as a sandbox provider for OpenAI's Agents SDK (v0.14.0)
- **World ID / AgentKit**: "Human in the loop" authentication live on Vercel

## Related Concepts

- [[concepts/harness-engineering]] — The security harness paradigm deepsec exemplifies
- [[entities/openai]] — Agents SDK sandbox integration partner

## Sources

- [Codex is gaining steam (Ben's Bites)](https://open.substack.com/pub/bensbites/p/codex-is-gaining-steam) — May 5, 2026
