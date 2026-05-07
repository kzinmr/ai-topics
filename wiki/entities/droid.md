---
title: Droid (Factory)
type: entity
aliases: [factory-droid, factory-ai, factory-droid-cli]
created: 2026-05-07
updated: 2026-05-07
status: L2
tags:
  - entity
  - coding-agent
  - enterprise
  - cli
  - ide
  - ci-cd
  - ai-agents
sources:
  - https://github.com/Factory-AI/factory
  - https://factory.ai/
  - https://docs.factory.ai/pricing
  - https://docs.factory.ai/integrations/github-app
  - https://docs.z.ai/devpack/tool/droid
  - https://factory.ai/product/cli
  - https://factory.ai/product/ide
related:
  - "[[entities/claude-code]]"
  - "[[entities/copilot-cli]]"
  - "[[entities/opencode]]"
  - "[[entities/codex]]"
  - "[[concepts/agent-harness-comparison]]"
---

# Droid (Factory)

> **Droid** is Factory's enterprise-grade AI coding agent that lives across your terminal, IDE, Slack, Linear/Jira, and CI/CD pipelines. The "agent-native development platform" — top-performing in terminal benchmarks, with specialized sub-agents (CodeDroid, Review Droid, QA Droid) for the full SDLC.

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | Factory AI (San Francisco) |
| リポジトリ | [Factory-AI/factory](https://github.com/Factory-AI/factory) |
| 公式サイト | [factory.ai](https://factory.ai) |
| 初回リリース | 2025 |
| 対応環境 | CLI, Desktop, Web, VS Code, JetBrains, Vim, Zed, Slack/Teams, Linear/Jira, Mobile |
| 価格 | Free tier / Pro $20/mo / Team $50/mo / Enterprise custom |
| X/Twitter | [@FactoryAI](https://x.com/FactoryAI) |

## Key Features

### Specification Mode
- Press **Shift+Tab** to activate
- Describe features in plain language
- Get automatic planning before implementation
- Approve plans before any code changes

### Auto-Run Mode (3 levels)
| Level | Permissions | Use Case |
|-------|-------------|----------|
| **Low** | Edits and read-only commands | Safe exploration |
| **Medium** | Reversible commands (package installs, builds, git) | Development |
| **High** | All commands except explicitly dangerous | Autonomous execution |

### Multi-Platform Presence
- **CLI** — Terminal-native with slash commands, custom sub-agents, native diff viewing
- **IDE** — Works across VS Code (forks), JetBrains, Vim, Zed (ACP support)
- **Slack/Teams** — In-chat agent invocation for incident response
- **Linear/Jira** — Auto-trigger from issue assignment, implement + create PRs
- **Desktop/Web** — Full standalone app

### Enterprise Features
- SOC-2 compliant
- SSO/SAML
- Dedicated compute
- Compliance auditing
- Cost tracking with `/cost` command
- MCP (Model Context Protocol) support

### Droid Sub-Agent Ecosystem
- **CodeDroid** — Implementation agent
- **Review Droid** — Automated code review (GitHub/GitLab PRs)
- **QA Droid** — Testing agent
- **Custom sub-agents** — Via `/install-code-review`, droid-factory packages

### CI/CD Integration
- **Droid Action** — AI-powered code reviews, security scans, PR descriptions on GitHub Actions
- **Massively parallel execution** — Launch hundreds of agents with single command
- **Self-healing builds** — Agents diagnose failures and fix tests
- **JSON event streams** — Full observability for every automated task

## Model Support

| Models | How |
|--------|-----|
| Claude, GPT, Gemini | Default premium models |
| **Droid Core** (open-weight) | Free pool — smaller models for cost efficiency |
| **BYOK** | Bring your own API keys |
| Any model per task | Switch based on performance or cost |

## Pricing

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | Basic usage, Droid Core models |
| Pro | $20/mo | Desktop/CLI/SDK, cloud background agents, usage tracking |
| Team | $50/mo | Team features, shared billing |
| Enterprise | Custom | SOC-2, SSO, dedicated compute, compliance |

**Droid Core**: Free pool of leading open-weight models that kick in when premium model rate limits are exhausted.

## Positioning

Factory positions Droid as the **most comprehensive agent-native platform** — covering the entire SDLC from IDE to CI/CD, with special attention to enterprise requirements. Unlike Claude Code (single-surface CLI) or Copilot CLI (GitHub-only), Droid aims to be everywhere developers work.

**Key differentiator**: Multi-agent architecture (specialized Droids per task type) rather than one monolithic agent.
