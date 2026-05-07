---
title: GitHub Copilot CLI
type: entity
aliases: [copilot-cli, gh-copilot-cli, github-copilot-cli]
created: 2026-05-07
updated: 2026-05-07
status: L2
tags:
  - entity
  - coding-agent
  - github
  - microsoft
  - cli
  - ai-agents
sources:
  - https://github.com/github/copilot-cli
  - https://github.com/features/copilot/cli
  - https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli
  - https://github.blog/changelog/2026-04-07-copilot-cli-now-supports-byok-and-local-models/
  - https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli
  - https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference
related:
  - "[[entities/claude-code]]"
  - "[[entities/codex]]"
  - "[[entities/opencode]]"
  - "[[entities/droid]]"
  - "[[concepts/github-copilot-billing]]"
  - "[[concepts/microsoft-copilot-wave-3]]"
  - "[[concepts/agent-harness-comparison]]"
---

# GitHub Copilot CLI

> **GitHub Copilot CLI** brings Copilot's agentic AI capabilities directly to your terminal — powered by the same harness as GitHub's Copilot coding agent. Features built-in sub-agents (explore, code-review, research, general-purpose), MCP-powered extensibility, BYOK/local model support, and deep GitHub workflow integration.

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | GitHub (Microsoft) |
| リポジトリ | [github/copilot-cli](https://github.com/github/copilot-cli) |
| 公式サイト | [github.com/features/copilot/cli](https://github.com/features/copilot/cli) |
| 初回リリース | 2025 (replaced retired gh copilot extension) |
| 対応環境 | Terminal (CLI) |
| 価格 | Included in Copilot Free/Pro/Pro+/Business/Enterprise |
| インストール | `curl -fsSL https://gh.io/copilot-install | bash` |

## Key Features

### Built-in Sub-Agents
Copilot CLI ships with specialized sub-agents, each with default model assignments:

| Agent | Default Model | Description |
|-------|---------------|-------------|
| **explore** | Claude Haiku 4.5 | Fast codebase exploration, searches files, reads code, answers questions (safe to parallelize) |
| **code-review** | Claude Sonnet 4.5 | High signal-to-noise code review, analyzes diffs for bugs and security issues |
| **general-purpose** | Claude Sonnet 4.5 | Full-capability agent for complex multi-step tasks in separate context |
| **research** | Claude Sonnet 4.6 | Deep research agent generating reports from codebase + web |
| **rubber-duck** | Complementary model | Constructive critique of proposals, designs, implementations |
| **configure-copilot** | Varies | NL-based configuration management (MCP, agents, skills) |

### Advanced Agent Features
- **`/fleet`** — Parallelized sub-agents for multi-file operations
- **`/plan`** → merged code — Full workflow from planning to PR
- **Autopilot mode** — Autonomous multi-step task completion without step-by-step approval
- **Steering** — Guide agent behavior mid-execution
- **Remote steering** — Monitor/respond from GitHub.com or GitHub Mobile
- **`/pr` command** — PR management from terminal
- **Custom agents** — Invoke specialized agents via NL

### BYOK & Local Models (April 2026+)
Copilot CLI now supports **bring-your-own-key** and **local models**:
- Connect any model provider (OpenAI-compatible)
- Offline mode for air-gapped environments
- GitHub authentication optional
- **Requirements**: Model must support tool calling + streaming, 128K+ context window
- Built-in sub-agents inherit your provider config automatically

### MCP-Powered Extensibility
- Ships with GitHub's MCP server by default
- Supports custom MCP servers
- Skills system for reusable workflows
- Custom agents via NL configuration

### GitHub Workflow Integration
- Direct access to repositories, issues, pull requests via NL
- Authenticated with existing GitHub account
- Cloud agent handoff — delegate tasks from CLI to cloud agent
- Code review in terminal → GitHub.com loop

## Model Support

| Tier | Models | How |
|------|--------|-----|
| 🥇 Default | Claude Sonnet 4.5/4.6, Claude Haiku 4.5 | GitHub-hosted model routing |
| 🥇 BYOK | Any OpenAI-compatible API | Custom provider config |
| 🥇 Local | Ollama, LM Studio, etc. | Local endpoint (air-gap capable) |

## Pricing

| Plan | Price | Copilot CLI Access |
|------|-------|--------------------|
| Copilot Free | $0 | ✅ Basic access |
| Copilot Pro | $10/mo | ✅ Full access |
| Copilot Pro+ | $39/mo | ✅ Priority access |
| Copilot Business | $19/user/mo | ✅ Enterprise features |
| Copilot Enterprise | $39/user/mo | ✅ Full + customization |

## Positioning

Copilot CLI is GitHub's answer to Claude Code — but deeply integrated with the GitHub ecosystem. Its key differentiator is **seamless GitHub workflow integration**: issues → planning → code → PR → review, all from the terminal without switching tools.

**Key differentiator vs competitors**: GitHub integration depth (repos, issues, PRs, code review all native), sub-agent specialization, and the `/fleet` parallel execution model.

**History note**: The "GitHub CLI Copilot extension" was retired and replaced by the new standalone Copilot CLI. Do not confuse with the old `gh copilot` extension.
