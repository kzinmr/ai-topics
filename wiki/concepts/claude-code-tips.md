---
title: Claude Code Tips
type: concept
created: 2026-04-27
updated: 2026-04-27
tags:
  - concept
  - agentic-engineering
  - anthropic
  - dev-tooling
  - docker
  - security
aliases: ["claude-code-best-practices", "claude-code-docker"]
sources:
  - raw/articles/timsh.org--claude-inside-docker--6842418e.md
  - raw/articles/timsh.org--why-you-should-self-host--bff25172.md
---

# Claude Code Tips

> Practical setup guides and configuration advice for Claude Code, with a focus on security isolation, Docker integration, and efficient workflows.

## Docker-Based Claude Code Setup

For users who want to run Claude Code securely without granting it full filesystem and terminal access to their host machine, running Claude Code **inside a Docker container** via VSCode's Dev Containers feature is a lightweight and effective approach.

### Why Docker-Isolate Claude Code

1. **Filesystem isolation** — Claude can only access files inside the container or explicitly mounted volumes
2. **Credential protection** — Host SSH keys, secrets, and personal data remain inaccessible
3. **Terminal sandboxing** — Worst-case scenario is the container breaks and stops, not data loss
4. **No external access** — External integrations require explicit opt-in

This addresses a real concern: AI agents with full terminal access present a security risk comparable to giving a unknown freelancer unfettered access to your machine.

### Setup (5 Minutes)

Based on [timsh.org's guide](https://timsh.org/claude-inside-docker/):

1. **Prerequisites**: Docker + VSCode installed, Claude subscription active
2. **Clone the template**: `git clone https://github.com/tim-sha256/claude-in-docker.git`
3. **Open in VSCode** — the `devcontainer.json` is pre-configured
4. **"Reopen in Container"** — VSCode builds and enters the dev container
5. **Verify**: Run `claude` in the integrated terminal

### Fine-Grained GitHub Token

Inside the container, use a **fine-grained GitHub personal access token** instead of SSH keys:

- Create at `https://github.com/settings/personal-access-tokens/new`
- Grant access to specific repositories only
- Set Repository Permissions → Contents → "Read and write"
- This single permission is sufficient for basic git operations

Unlike a container-specific SSH key (which can't have granular permissions), a fine-grained token limits Claude to only the repositories and operations you explicitly authorize.

### Who This Is For

- Casual users who want Claude Code without the $40/month Cursor Pro subscription
- Developers concerned about AI agent security
- Anyone who values a clear cost/benefit: $20 Claude subscription + Docker isolation

## Related Pages

- [[concepts/harness-engineering/agentic-engineering]] — Agentic engineering practices
- [[concepts/vibe-coding]] — Contrasting development style
- [[concepts/self-hosting-ai-development]] — Self-hosting AI applications
- [[entities/xeiaso-net]] — Xe Iaso's perspective on AI abstraction costs
