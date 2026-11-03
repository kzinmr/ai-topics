---
title: "Self-Hosting AI Development"
type: concept
aliases:
  - self-hosting-ai-development
created: 2026-04-25
updated: 2026-11-03
tags:
  - concept
  - infrastructure
  - developer-tooling
  - coding-agents
status: enriched
sources:
  - raw/articles/timsh.org--why-you-should-self-host--bff25172.md
---

# Self-Hosting AI Development

> Strategies and patterns for deploying AI-generated applications to self-hosted infrastructure, covering the full pipeline from development to production.

## Overview

Self-hosting is emerging as a practical alternative to Vercel/Railway for AI-generated applications ("vibecoded" apps). The key driver: AI-generated apps often need dependency flexibility (Redis, Postgres, cron jobs, WebSockets) that serverless platforms constrain or charge premium rates for.

## The Coolify + Hetzner Pattern

Based on practical experience deploying AI-built applications, a lightweight self-hosting stack has emerged:

### Infrastructure
- **VPS**: Hetzner CX22 (2 vCPU, 4GB RAM, €3.79/month) or larger depending on need
- **Deployment Platform**: [Coolify](https://coolify.io/) — open-source, self-hosted PaaS
- **Database**: Postgres (built-in Coolify service)
- **TLS/SSL**: Let's Encrypt (automatic via Coolify)

### Why Self-Host AI Apps

1. **Cost**: A €3.79/month VPS vs $20/month Railway bill for a small app
2. **No scaling fees**: Fixed monthly cost regardless of compute usage
3. **Full control**: Access to cron, WebSockets, Postgres extensions, Redis
4. **Learning value**: Understanding deployment infrastructure is valuable DevOps education
5. **No lock-in**: Applications remain portable, not tied to a specific platform

### Real-World Stack

A typical production configuration:
```yaml
Provider:      Hetzner
Instance:      CX22 (2C, 4GB, €3.79/mo)
Platform:      Coolify (Docker-based)
Database:      Postgres via Coolify
Storage:       40GB SSD + optional 400GB volume (€5/mo)
```

### Downsides and Mitigations

| Challenge | Mitigation |
|-----------|------------|
| No DDoS protection | Cloudflare proxying in front of VPS |
| Database backups | Automated snapshot scripts |
| Security maintenance | Coolify handles updates; regular OS patching |
| Reproducibility | Dockerfile in each project repo |
| Not turnkey | ~1 hour setup vs 5 minutes for Vercel |

### Who It's For

- **Developers** with Docker/Linux comfort who value cost predictability
- **AI-generated app creators** hitting platform constraints (cron, WebSockets, extensions)
- **Small commercial apps** generating enough revenue to justify the setup investment
- Anyone who wants to **understand infra basics** rather outsource entirely

## Revolut case study: self-hosted GLM at $0.30/M tokens (Nov 2026)

Fintech scale evidence for the open-weight self-hosting thesis (HN 50350004, 103 pts, 2026-11-03): Revolut's AI-ops lead David Abitbol reports running **56 Nvidia B200s** serving GLM with a blended cost of **~$0.30 per million tokens — roughly 1/10th of what they paid Anthropic and OpenAI** (per-commenter estimate: ~$2.5-3M hardware, possibly rented metal). Thread takeaways: (a) frontier-required slice of enterprise workloads keeps shrinking (InsidiousWombat — "the new norm" is buying open models off your cloud provider, not bare-metal self-hosting); (b) frontier labs may counter with $2k/month/seat bulk-token enterprise plans (aurareturn); (c) B200 depreciation risk vs Nvidia roadmap (AidenVennis); (d) data-sovereignty motive independent of cost (jacquesm — inference suppliers "absolutely not" trustworthy long-term with your data). Cross-ref [[concepts/open-weight-vs-closed-llm-gap]], [[entities/martin-alderson]] (open-weight margin collapse analysis).

## Related Pages

- [[concepts/vibe-coding]] — AI-generated application development
- [[concepts/claude-code/claude-code-tips]] — Claude Code setup guide (Docker-based)
- [[concepts/harness-engineering/agentic-engineering]] — Agentic engineering practices
- [[entities/xeiaso-net]] — Xe Iaso's perspective on small internet and self-hosting
