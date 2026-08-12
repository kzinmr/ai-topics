---
title: OpenHands (Agent Canvas)
created: 2026-08-12
updated: 2026-08-12
type: entity
tags:
  - product
  - platform
  - coding-agents
  - open-source
  - self-hosted
  - developer-tools
  - agent-platform
  - agent-framework
  - acp
  - agent-communication-protocol
  - automation
  - sandbox
  - deterministic
sources:
  - raw/articles/2026-08-12_openhands_agent-canvas-readme.md
---

# OpenHands (Agent Canvas)

**OpenHands** (branded as **Agent Canvas**) is an open-source, self-hosted developer control center for coding agents. Developed by All Hands AI, it provides a unified interface for running, managing, and orchestrating coding agents across local, remote, and cloud backends. The project was formerly known as **OpenDevin** before rebranding.

## Overview

OpenHands Agent Canvas turns coding agents into a self-hosted, always-on engineering team. It serves as a developer control center for starting agent conversations and automating everyday software engineering tasks — such as generating reports that publish to Slack or automatically decomposing GitHub issues into actionable tasks.

By default, it runs locally on the developer's machine but can connect to multiple "agent backends" — running agents in Docker containers, on virtual machines (VMs), or within company infrastructure. Users can optionally run agents on OpenHands Cloud or OpenHands Enterprise infrastructure.

Agent Canvas runs the open-source OpenHands agent out of the box, but is designed to work with any third-party agent, including [[entities/claude-code|Claude Code]], [[entities/codex|Codex]], Gemini, or any agent compatible with the Agent Communication Protocol (ACP).

The project is currently in **beta** and is distributed as an npm package (`@openhands/agent-canvas`), with a Docker image available at `ghcr.io/openhands/agent-canvas`. All Hands AI also runs an [incubator program](https://github.com/OpenHands/incubator-program) for community contributors.

## Key Features

- **Self-hosted deployment**: Run agents locally, in Docker, on VMs, or on any machine that can host an agent server backend. The frontend can switch between different backends without losing context.
- **Multi-agent support**: Works with OpenHands' native agent, Claude Code, Codex, Gemini, and any ACP-compatible agent.
- **Pre-built automations**: Create workflows that integrate with Slack, GitHub, Linear, Notion, and other third-party services. Automations can run on a schedule or in response to webhook events.
- **Deterministic sandboxing**: Agents can run inside Docker sandboxes for isolation and reproducibility.
- **Bring your own model**: Compatible with any LLM provider via configurable LLM profiles.
- **Multi-file context**: Agents work across multiple files and project contexts.
- **Flexible backends**: Supports local, remote (dedicated machines, cloud VMs), and managed cloud backends that can be shared with a team or kept personal.

## Architecture

Agent Canvas is powered by the [OpenHands Agent Server](https://github.com/OpenHands/software-agent-sdk/tree/main/openhands-agent-server), a REST API for running multiple agents on a single machine. The architecture consists of:

- **Agent Canvas frontend**: A web-based UI (accessible at `http://localhost:8000` or `http://localhost:8000/canvas` for Docker) for managing agents and viewing their output.
- **Agent Server**: A backend REST API that runs on a single host/port and manages agent lifecycle. Multiple agent servers can be connected to a single Agent Canvas frontend.
- **Automation Server**: An optional companion that runs agents on schedules or in response to events from external services (e.g., Slack messages, GitHub webhooks).

The Agent Server can be deployed:
- Directly on a developer's laptop (without sandbox — full filesystem access)
- On a dedicated machine like a Mac Mini
- On a cloud virtual machine
- Inside OpenHands Cloud (the commercial offering)

The Agent Canvas frontend connects to multiple Agent Servers simultaneously, allowing developers to switch between personal agents running locally and shared team agents running on cloud infrastructure.

## Comparison to Other Coding Agents

OpenHands occupies a distinct niche compared to other coding agent platforms:

| Dimension | OpenHands (Agent Canvas) | [[entities/claude-code|Claude Code]] | [[entities/codex|Codex]] |
|-----------|-------------------------|-------------|-------|
| **Deployment** | Self-hosted, open-source | Cloud + CLI | Cloud + CLI |
| **Agent support** | Multi-agent (any ACP agent) | Single agent (Claude) | Single agent (Codex) |
| **Automation** | Built-in scheduled + webhook automations | Limited (routines) | Limited |
| **Backend flexibility** | Local, Docker, VM, Cloud | Anthropic-managed | OpenAI-managed |
| **Team sharing** | Yes (shared agent servers) | Via Claude Code Desktop | Limited |
| **Open source** | Yes (full stack) | No | No |

Unlike Cursor and GitHub Copilot, which are primarily IDE-integrated tools, OpenHands is a standalone platform that functions as an "always-on" engineering team — agents continue running even when the developer's IDE is closed, making it suitable for background tasks like code review, dependency updates, and scheduled reporting.

## Related Pages

- [[concepts/coding-agents/coding-agents|Coding Agents]] — Overview of the coding agent ecosystem
- [[entities/claude-code|Claude Code]] — Anthropic's CLI coding agent, supported as a backend
- [[entities/codex|Codex]] — OpenAI's CLI coding agent, supported as a backend
