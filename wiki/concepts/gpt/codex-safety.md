---
title: "Codex Safety at OpenAI"
type: concept
created: 2026-05-10
updated: 2026-05-10
tags:
  - security
  - company
  - sandbox
  - infrastructure
  - governance
  - openai
sources:
  - https://openai.com/index/running-codex-safely
  - raw/articles/openai.com--index-running-codex-safely--09a84312.md
---

# Codex Safety at OpenAI

> "Security teams need ways to govern how agents operate: what they can access, when human approval is required, which systems they can interact with, and what telemetry exists to explain their behavior."
>
> — OpenAI, May 2026

## Overview

OpenAI published detailed guidance on deploying Codex safely within enterprise environments, covering **sandboxing, approval policies, managed network access, and agent-native telemetry**. This represents OpenAI's own internal deployment patterns for Codex across their engineering teams.

## Core Design Principles

OpenAI deploys Codex with a simple principle:
- **Be productive inside a bounded environment**
- **Low-risk everyday actions should be frictionless**
- **Higher-risk actions should stop for review**

## Control Surfaces

### Sandboxing

The sandbox defines the **technical execution boundary**:
- Where Codex can write
- Whether it can reach the network
- Which paths remain protected

### Approval Policy

Determines when Codex must ask for permission to perform actions:
- Users can approve actions once, or approve action types for a session
- **Auto-review mode**: Codex sends planned action and recent context to an auto-approval subagent
  - Automatically approves low-risk actions without interrupting the user
  - Still stops on higher-risk or actions with unintended consequences
  - Keeps Codex moving on routine work

### Network Policy

OpenAI does **not** run Codex with open-ended outbound access:
- Managed network policy allows expected destinations
- Blocks destinations Codex should not reach
- Requires approval for unfamiliar domains
- Lets Codex complete common, known-good workflows without giving it broad network access

### Authentication Management

- CLI and MCP OAuth credentials stored in secure OS keyring
- Login forced through ChatGPT
- Access pinned to ChatGPT enterprise workspace
- Keeps Codex usage tied to workspace-level controls
- Makes Codex activity available in the ChatGPT Compliance Logs Platform

### Command Rules

Codex does **not** treat every shell command as equally safe:
- Common benign commands allowed without approval outside sandbox
- Specific dangerous commands can be blocked or require approval
- Lets Codex move quickly through ordinary engineering tasks
- Forces review or blocks patterns not wanted outside sandbox

### Configuration Layers

Applied through a combination of:
1. **Cloud-managed requirements** — admin-enforced controls, users cannot override
2. **macOS managed preferences** — consistent baseline with flexibility
3. **Local requirements files** — per-team/user/environment tuning

Configurations apply across all local Codex surfaces: desktop app, CLI, and IDE extension.

## Agent-Native Telemetry

### The Problem with Traditional Logs

> "Traditional security logs are still useful when looking at actions taken by Codex, but they mostly answer what happened: a process started, a file changed, a network connection was attempted. Defenders are still left to figure out why Codex did something, or the user's intent."

### Codex's Agent-Aware Telemetry

Codex supports **OpenTelemetry log export** for various events:
- User prompts
- Tool approval decisions
- Tool execution results
- MCP server usage
- Network proxy allow/deny events
- Activity logs through OpenAI Compliance Platform (Enterprise/Edu)

### AI-Powered Security Triage

OpenAI uses Codex logs alongside an **AI-powered security triage agent**:

1. **Endpoint alert**: Says Codex did something unusual
2. **Endpoint security tool**: Reports suspicious event occurred
3. **Codex logs**: Explain surrounding intent by user and agent
4. **AI triage agent**: Inspects original request, tool activity, approval decisions, tool results, network policy decisions
5. **Security team**: Reviews analysis to distinguish between expected agent behavior, benign mistakes, and activity warranting escalation

### Operational Use

The same telemetry helps understand:
- How internal adoption is changing
- Which tools and MCP servers are being used
- How often network sandbox is blocking or prompting
- Where the rollout still needs tuning

OpenTelemetry logs can be centralized in **SIEM** and compliance logging systems.

## Key Insight

> "With those capabilities in place, security teams can enable Codex with greater confidence, balancing developer productivity with the visibility and control required for enterprise security."

## Related

- [[entities/codex]] — OpenAI Codex coding agent
- [[concepts/ai-agent-safety]] — Broader AI agent safety practices
- [[concepts/testing-ai-agents]] — Testing agents before deployment
- [[concepts/supply-chain-security]] — Software supply chain security

## References

- [Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely) — OpenAI News, May 2026
