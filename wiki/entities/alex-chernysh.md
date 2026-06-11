---
title: Alex Chernysh
created: 2026-05-10
updated: 2026-05-10
type: entity
tags:
  - person
  - lab
  - multi-agent
  - open-source
  - orchestration
aliases:
  - alex-chernysh
  - '@alex_chernysh'
  - chernistry
sources:
  - https://alexchernysh.com/
  - https://github.com/chernistry
  - https://bernstein.run/
  - https://x.com/alex_chernysh
related:
  - "[[entities/bernstein]]"
  - "[[concepts/bernstein]]"
  - "[[concepts/multi-agents/multi-agent-orchestration]]"
---

# Alex Chernysh

**Alex Chernysh** (@alex_chernysh, chernistry) is an Applied AI Systems & Platform Engineer based in Tel Aviv. He is the creator and solo maintainer of **Bernstein**, the leading open-source deterministic multi-agent orchestrator for CLI coding agents.

## Overview

Chernysh specializes in production AI systems — retrieval, evals, and agent infrastructure. His work emphasizes determinism, auditability, and on-prem deployability in multi-agent orchestration. He is available for forward-deployed AI engineering and architecture audits.

## Key Projects

### Bernstein (2025–Present)
Created and solo-maintains Bernstein, an open-source deterministic orchestrator for 40+ CLI AI agents. Apache 2.0 licensed, ~54,000 monthly PyPI installs, 296+ GitHub stars. Key differentiators:
- Deterministic Python scheduler — zero LLM tokens on coordination
- HMAC-SHA256 audit chain with per-artefact lineage
- Git worktree isolation per agent
- On-prem and air-gapped deployment
- MCP server mode

See [[entities/bernstein]] for full details.

### HireEx (hireex.ai)
Daily job shortlist tool that automates job search workflows.

### RightLayout (May 2026)
Mac AI tool — documented his experience shipping and then letting go of a side project.

## Writing & Blog

Chernysh publishes engineering notes on his personal site (alexchernysh.com):
- **RightLayout: Shipping a Mac AI Tool, Then Letting Go** (May 8, 2026)
- **Forecasting Without Prophecy: a plain-text discipline** (May 2, 2026)
- **Need a job? Sip your drink. We'll look for you.** (Apr 23, 2026)

## Philosophy

Chernysh's work is guided by a "plain-text discipline" in AI systems engineering — prioritizing:
- **Determinism over magic**: Scheduling decisions should be replayable and auditable
- **Local-first**: No SaaS dependency, no telemetry by default
- **Security by architecture**: HMAC-chained audit trails, Ed25519 signed agent cards, tamper-evident logs
- **Ship first, iterate fast**: Bernstein v1.x went from 18 to 44 adapters through rapid community-driven iteration

## Community
- **Website**: https://alexchernysh.com/
- **GitHub**: https://github.com/chernistry
- **X**: https://x.com/alex_chernysh
- **LinkedIn**: https://www.linkedin.com/in/alex-chernysh/

## Sources
- [Personal Website](https://alexchernysh.com/)
- [GitHub](https://github.com/chernistry)
- [Bernstein Official](https://bernstein.run/)
