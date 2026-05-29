---
title: Matt Palmer
created: 2026-05-29
updated: 2026-05-29
type: entity
tags: [person, content-creator, hermes-agent, blogger, indie-maker]
aliases: [@mattppal, mattppal]
related: [entities/hermes-agent, concepts/agent-hosting-aws]
sources: [raw/articles/2026-05-26_matt-palmer_hermes-agent-deployment-fly-modal.md]
---

# Matt Palmer

Matt Palmer (@mattppal) is an engineer and content creator who works at [[conductor|Conductor]] (an AI coding tool). He publishes technical walkthroughs and deployment templates focused on AI agent infrastructure, with an emphasis on practical, secure, managed-stack architectures.

## Notable Work

### Hermes Agent Template (May 2026)

Created [hermes-agent-template](https://github.com/mattppal/hermes-agent-template) — a production-ready deployment template for [[entities/hermes-agent]] using:
- **Fly.io** for the agent gateway and Open WebUI frontend
- **Modal** for sandboxed code execution
- **Cloudflare Access** with GitHub OAuth for authentication
- **OpenRouter** as the LLM provider

The template includes a full Makefile-driven deployment pipeline (Docker builds, Fly secrets management, OIDC configuration, smoke tests) and a companion 67-minute walkthrough video.

### Philosophy

Advocates for **managed-service stacks over VPS** for personal AI agent hosting. Core arguments:
- Time and expertise are the real costs — not the $5 VPS price tag
- "I'm not a security researcher. I want to spend my time building cool agents."
- Defense in depth through multiple service boundaries beats a single-server security posture

### Key Design Principles

- **Agent ↔ terminal separation**: The agent gateway should never run on the same environment as code execution
- **Least-privilege secret injection**: Sandboxes receive only the credentials needed for each specific command
- **Public internet cannot touch the agent**: Chat UIs communicate over internal networks only
- **Double authentication**: Cloudflare Access + Open WebUI OIDC for all browser-based access

## Related Wiki Pages

- [[concepts/agent-hosting-aws]] — AWS equivalent architecture mapping based on Matt's design
- [[entities/hermes-agent]] — Hermes Agent platform
