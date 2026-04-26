---
title: OpenClaw
type: entity
aliases: [openclaw, open-claw, peter-steinberger-openclaw]
created: 2026-04-15
updated: 2026-04-15
status: L2
sources:
  - https://github.com/NVIDIA/OpenClaw
  - https://build.nvidia.com/spark
  - https://nemoclawai.io/blog/getting-started-nemoclaw-dgx-spark/
  - https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html
tags: [entity, agent-framework, local-llm, open-source, telegram]
---

# OpenClaw

Open-source always-on AI assistant framework created by **Peter Steinberger** (former PSPDFKit CEO). Deploys autonomous agents that run continuously, self-evolve through interaction, and integrate with messaging platforms like Telegram. OpenClaw is the upstream project that **NemoClaw** wraps with enterprise-grade security.

## Core Philosophy

> *"With one command, anyone can run always-on, self-evolving agents anywhere."*

OpenClaw represents a shift from **session-bound** AI tools (Claude Code, ChatGPT conversations) to **persistent, always-on** agents that:
- Run continuously in the background
- Learn and adapt from interactions over time
- Operate across multiple messaging platforms
- Execute tasks autonomously within defined boundaries

## Architecture

```
OpenClaw Agent
  ├── TUI (Terminal UI)
  ├── Telegram Bot Integration
  ├── Local Model Support (Ollama, LM Studio)
  └── API Server
```

## Key Features

| Feature | Description |
|---------|-------------|
| **Always-on** | Runs 24/7 without manual session management |
| **Self-evolving** | Learns from interactions and adapts behavior |
| **Multi-platform** | Telegram, web dashboard, terminal, API |
| **Local inference** | Works with Ollama, LM Studio, llama.cpp |
| **Open source** | MIT-licensed, community-driven development |
| **Lightweight** | Designed for edge devices like DGX Spark |

## Integration with DGX Spark

OpenClaw is a **first-class citizen** on DGX Spark:

- Runs natively on arm64 architecture
- Leverages 128 GB unified memory for large models
- Integrates with LM Studio and Ollama for local inference
- Supports Telegram bot deployment for always-on access

### Quick Start on DGX Spark

```bash
# Install OpenClaw
# (via NemoClaw installer or standalone)
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash

# Launch the agent
openclaw agent --agent main --local -m "hello" --session-id test

# Or use the TUI
openclaw tui
```

## OpenClaw vs NemoClaw

| Aspect | OpenClaw (standalone) | NemoClaw (wrapped) |
|--------|----------------------|-------------------|
| **Security** | Direct host access | OpenShell sandbox |
| **Isolation** | None | Landlock + seccomp + netns |
| **Network** | Unrestricted | Policy-controlled |
| **Multi-tenant** | No | k3s-based pod isolation |
| **Inference** | Any provider | Routed through controlled backends |
| **Use case** | Personal experimentation | Enterprise deployment |

## Configuration

OpenClaw stores configuration in `~/.openclaw/openclaw.json`:

```json
{
  "gateway": {
    "auth": {
      "token": "<your-gateway-token>"
    }
  },
  "agent": {
    "name": "main",
    "model": "ollama/nemotron-3-super:120b",
    "platform": "telegram"
  }
}
```

### Web Dashboard

```
http://127.0.0.1:18789/#token=<your-gateway-token>
```

> ⚠️ **Important:** Use `127.0.0.1`, not `localhost` — the gateway requires an exact origin match.

## Telegram Integration

1. Create a bot token via `@BotFather` on Telegram (`/newbot`)
2. Configure the token in `openclaw.json`
3. Messages to the bot are forwarded to your agent
4. Agent responses are sent back to the user

## Lifecycle Management

| Operation | Command |
|-----------|---------|
| Start agent | `openclaw agent --agent main --local -m "hello"` |
| Launch TUI | `openclaw tui` |
| Check status | `openclaw status` |
| View logs | `openclaw logs --follow` |

## Playbooks Available on DGX Spark

| Playbook | Duration | Description |
|----------|----------|-------------|
| **OpenClaw Local Deployment** | 4w | Full setup with LM Studio/Ollama |
| **NemoClaw + Telegram** | 30 min | Bot integration with local inference |
| **Multi-Agent Chatbot** | 1 hr | Multiple agents coordination |

## Related

- [[nvidia-nemoclaw]] — NemoClaw secure wrapper for OpenClaw
- [[peter-steinberger]] — OpenClaw creator
- [[nvidia-dgx-spark]] — DGX Spark hardware platform
- [[concepts/local-llm/server-dgx-spark]] — Setup guide
- [[concepts/harness-engineering/system-architecture/agent-security-patterns]] — Security patterns
