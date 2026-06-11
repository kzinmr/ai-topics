---
title: Matt Palmer
created: 2026-05-29
updated: 2026-05-29
type: entity
tags:
  - person
  - content-creator
  - ai-agents
  - blogger
  - indie-maker
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

## Deployment Walkthrough Details (from Transcript)

The 67-minute companion video covers the full end-to-end deployment in detail:

### Architecture Flow

1. **Chat interface** (Open WebUI) deployed on a custom domain via Fly.io — accepts user input
2. Input passes to a **Modal backend** where a **sandbox spins up** for code execution
3. The sandbox executes code in a **secure environment** and passes results back to the agent
4. Results return to the **Open WebUI chat instance**, gated behind **Cloudflare Access**

> *"End to end, that's exactly how you should deploy a Hermes agent."*

### Prerequisites

- Fly CLI + Docker installed locally (`brew install flyctl`, `fly auth login`)
- Cloudflare account with a domain (Palmer used `mattpalmer.io`)
- Modal account for sandboxed execution
- OpenRouter API key as the LLM provider

### VPS vs. Managed Stack (from Transcript)

Palmer explicitly argues against the "$5 VPS" approach popular in DevOps communities:

- **Cost reality**: Managed solution runs $30–50/month depending on power — "not that much more than a VPS"
- **Time is the real cost**: "Do we have the time to manage an entire solution ourselves? It's kind of a build versus buy trade-off"
- **Security expertise gap**: "Part of expertise I would even say is security. A VPS can be secure if you know what you're doing and you have the time to do so"
- **Defense in depth**: Multiple managed service boundaries provide layered security that a single VPS cannot match

### Key Design Principles

- **Agent ↔ terminal separation**: The agent gateway should never run on the same environment as code execution
- **Least-privilege secret injection**: Sandboxes receive only the credentials needed for each specific command
- **Public internet cannot touch the agent**: Chat UIs communicate over internal networks only
- **Double authentication**: Cloudflare Access + Open WebUI OIDC for all browser-based access

## Related Wiki Pages

- [[concepts/harness-engineering/agent-hosting-aws]] — AWS equivalent architecture mapping based on Matt's design
- [[entities/hermes-agent]] — Hermes Agent platform
