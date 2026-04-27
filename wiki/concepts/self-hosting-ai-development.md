---
title: "Self-Hosting AI Development"
type: concept
aliases:
  - self-hosting-ai-development
created: 2026-04-25
updated: 2026-04-27
tags:
  - concept
  - self-hosting
  - devops
  - vibe-coding
  - infrastructure
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

## Related Pages

- [[concepts/vibe-coding]] — AI-generated application development
- [[concepts/claude-code-tips]] — Claude Code setup guide (Docker-based)
- [[concepts/harness-engineering/agentic-engineering]] — Agentic engineering practices
- [[entities/xeiaso-net]] — Xe Iaso's perspective on small internet and self-hosting
