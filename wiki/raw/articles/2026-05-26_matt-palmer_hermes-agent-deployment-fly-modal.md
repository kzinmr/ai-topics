---
title: "Deploy a Hermes Agent with Fly, Modal, OpenRouter, and Cloudflare Access — Matt Palmer"
created: 2026-05-26
author: Matt Palmer (@mattppal)
source: YouTube
url: https://www.youtube.com/watch?v=USmG-RXYzd8
type: talk
duration: "67:31"
tags: [hermes-agent, youtube, cloudflare, modal, ai-infrastructure, agent-infrastructure, docker, sandbox, platform, agent-security, self-hosted, serverless]
---

# Talk Overview

Matt Palmer walks through deploying a Nous Research Hermes Agent using a managed stack: Fly.io hosts the agent gateway and an Open WebUI frontend, Modal provides sandboxed code execution, and Cloudflare Access gates the chat interface behind GitHub OAuth. The build covers Docker-based Fly deployments, persistent volumes, OIDC configuration for double authentication, custom domain setup via CNAME, and isolating secrets between the agent and its terminal backend.

Companion template repo: https://github.com/mattppal/hermes-agent-template

## Core Thesis

A secure, production-grade Hermes Agent deployment requires **defense in depth** across multiple managed services rather than a single VPS. The agent core (gateway) must be separated from the code execution backend (terminal), and the chat UI must be gated behind authentication with protection from the public internet.

## Architecture

```
Internet → Cloudflare Access (GitHub OAuth) → Open WebUI (Fly.io, public)
                                                    │
                                          Fly internal network
                                          http://<app>.internal:8642/v1
                                                    │
                                            Hermes Agent Gateway
                                            (Fly.io, private, no public HTTP)
                                            + persistent volume
                                                    │
                                            Modal Sandboxes
                                            (isolated code execution)
                                                    │
                                            OpenRouter (LLM provider)
```

## Key Design Decisions

### Managed vs VPS ($30-50/mo vs $5/mo)

Matt chose managed services because:
- **Time**: Managing a VPS requires ongoing security hardening, monitoring, and patching. Managed services offload this.
- **Expertise**: "I'm not a security researcher. I want to spend my time building cool agents."
- **Security**: Each managed service provides its own security boundary — defense in depth vs. a single-server surface area.

### Agent ↔ Terminal Backend Separation

The Hermes agent gateway runs separately from the terminal backend:
- The agent holds secrets, processes messages, manages memory/skills
- The terminal backend (Modal) executes code in isolated sandboxes
- Secrets are passed through to sandboxes on a **least-privilege** basis — only what's needed for the specific command
- This prevents the "all secrets in one place" flaw common in personal agents (OpenClaw, local backend setups)

### Why Modal for Sandboxing

- Isolated, ephemeral environments per command execution
- No persistent storage, no interactive access to the agent's secrets
- If malicious code executes in a sandbox, the blast radius is contained
- "Principle of least privilege — only giving access to these sandboxes what they absolutely require"

### Cloudflare Access + Open WebUI OIDC (Double Authentication)

- Cloudflare provides: rate limiting, bot protection, DDoS protection (free tier)
- GitHub OAuth through Cloudflare Access
- Open WebUI OIDC backed by Cloudflare Access provides a second auth layer
- SSO-only login, no local signup, no password login

### Communication Isolation

- Only Open WebUI can communicate with the Hermes agent (Fly internal network)
- The public internet cannot reach the agent directly
- Adding additional messaging clients (Slack, Telegram) creates new public entry points that bypass Cloudflare protection — each must be evaluated carefully

## Deployment Steps

1. **Prerequisites**: Fly CLI, Docker, Cloudflare account with domain, Modal account, OpenRouter API key
2. **Clone template**: `git clone https://github.com/mattppal/hermes-agent-template`
3. **Configure `.env`**: App names, region, domain, model provider, admin email, OIDC values, secrets
4. **Cloudflare Zero Trust**: Create Access Application with OIDC, configure GitHub OAuth provider, set redirect URLs
5. **Fly setup**: `make create-apps`, `make create-volumes`, `make check-oidc`, `make sync-secrets`, `make deploy`
6. **Custom domain**: CNAME record in Cloudflare DNS pointing `chat.<domain>` → `<app>.fly.dev`
7. **Validation**: `make smoke` — curl-based endpoint checks

## Common Failure Points (from live debugging)

- **OIDC redirect URI mismatch**: Must add both the Fly dev domain (*.fly.dev) AND the custom domain to Cloudflare Access redirect URLs
- **Cloudflare cookie issues**: Stale cookies after configuration changes → clear site data
- **Modal token validation failure**: Rotate token pair, update `.env`, re-run `make sync-secrets`, redeploy
- **Open WebUI slow startup**: DB migrations and volume initialization take several minutes on first deploy
- **Environment variable changes require redeploy**: Updating `.env` alone is not enough — must run `make deploy-openwebui`

## Limitations / Future Work

- No skills configuration covered in this tutorial (basic deployment only)
- Adding Slack/Telegram/WhatsApp bypasses Cloudflare Access protection — each is a separate public entry point to the agent
- Messaging platform integrations require careful security review per endpoint

## Key Quotes

> "I'm not a security researcher. I'm not a security expert. I know things about security. I know what to ask agents. I know how to understand if something's secure. But I don't really want to spend all of my time provisioning, managing this VPS. I want to spend my time building cool agents."

> "The agent will only pass through the credentials to this container for Gcal and it won't have access to anything else that's stored on the agent. So if something bad happens... that is limited to this environment."

> "This is a big flaw in some of the personal agents that you see out there today. OpenClaw has this flaw. There are a lot of other tools that have this flaw. And if you do what is recommended here and go with a local backend, you're putting all of your credentials and all of these important things in the same place."

> "Every time we open an endpoint to our agent we have to be very careful with what we're opening up."

## Connection to Wiki Concepts

- [[concepts/agent-hosting-aws]] — AWS equivalent architecture mapping
- [[entities/hermes-agent]] — Hermes Agent platform page
- [[entities/matt-palmer]] — Author entity page
