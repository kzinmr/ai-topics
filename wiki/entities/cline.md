---
title: Cline
type: entity
created: 2026-07-12
updated: 2026-07-12
tags:
  - coding-agents
  - autonomous-agents
  - developer-tooling
  - ai-agents
  - ide
  - open-source
  - cline
sources:
  - raw/articles/2026-07-12_cline-autonomous-coding-agent.md
  - https://github.com/cline/cline
---

# Cline

Cline is an open-source autonomous coding agent that operates as a VS Code extension, JetBrains plugin, CLI assistant, and Node.js SDK. With over 64,000 GitHub stars and built in TypeScript, it competes directly with [[entities/devin]], [[entities/cursor-3]], [[entities/claude-code]], and [[entities/openai-codex]] in the [[concepts/coding-agents/coding-agents]] space. Created July 2024, it is one of the fastest-growing coding agent projects in the AI ecosystem.

## GitHub Stats

- **Stars**: 64,558 (as of July 2026)
- **Forks**: 6,893
- **Language**: TypeScript
- **Created**: July 6, 2024
- **Repository**: [github.com/cline/cline](https://github.com/cline/cline)
- **License**: Open source
- **Documentation**: [docs.cline.bot](https://docs.cline.bot)
- **Community**: Discord, Reddit (r/cline)

## Key Features

### Multi-Modal Deployment

Cline ships as four products from a single codebase:

| Product | Description |
|---------|-------------|
| **VS Code Extension** | AI coding assistant with file editing, command execution, web browsing, and human-in-the-loop approval |
| **JetBrains Plugin** | Same experience across IntelliJ IDEA, PyCharm, WebStorm, GoLand, and other JetBrains IDEs |
| **CLI** | Terminal-based interactive chat or fully headless mode for CI/CD and scripting |
| **SDK** (`@cline/sdk`) | Node.js programmatic agent API for building custom agents and integrations |

### Kanban Multi-Agent Board

A web-based task board (`npm i -g kanban`) runs many agents in parallel. Each card gets its own git worktree, auto-commit, and dependency chains — enabling fleets of agents working simultaneously on large codebases.

### Plan and Act Mode

Toggle between **Plan mode** (explore, ask clarifying questions, lay out strategy) and **Act mode** (execute the plan). Every file edit and terminal command requires approval by default, keeping the developer in control. Optionally toggle auto-approve for fully autonomous operation.

### Model Agnostic

Cline is not locked to a single AI provider. Supported backends include:

- **Anthropic**: Claude Opus, Sonnet, Haiku
- **OpenAI**: GPT series models
- **Google**: Gemini series
- **OpenRouter**: 200+ models from any provider
- **AWS Bedrock / Azure / GCP Vertex**: All hosted models
- **Cerebras / Groq**: Fast inference
- **Ollama / LM Studio**: Local models
- **Any OpenAI-compatible API**: Self-hosted or third-party endpoints

### Extensible with Plugins and MCP

Cline supports both custom plugins (via the SDK's `createTool` API with lifecycle hooks) and [[concepts/mcp]] servers for connecting to databases, APIs, cloud infrastructure, and external systems. Developers can register tools for logging, auditing, policy enforcement, or domain-specific capabilities.

### Rules and Skills

Project-specific rules are defined in `.clinerules` files, automatically picked up by CLI, VS Code extension, and JetBrains plugin. Skills allow the model to load specific rules when needed.

### Multi-Agent Teams

Coordinate multiple agents working together on complex tasks via `cline --team-name`. A coordinator agent breaks work into subtasks and delegates to specialist agents, each with their own tools and context. Team state persists across sessions.

### Scheduled Agents

Run agents on cron schedules for recurring automations: daily PR summaries, weekly dependency checks, codebase health reports. Schedules persist across restarts and run independently of any terminal session.

### Messaging Platform Integration

Chat with the agent from Slack, Telegram, Discord, Google Chat, WhatsApp, and Linear. Each conversation thread maps to an agent session with full context.

## Architecture / How It Works

Cline's architecture follows a **plan-then-execute** pattern (also known as [[concepts/self-driving-codebases|self-driving codebases]]):

1. **Context Gathering**: Reads project structure, understands file relationships, and monitors linter/compiler errors
2. **Planning**: In Plan mode, explores the codebase and lays out a strategy with clarifying questions
3. **Execution**: In Act mode, makes coordinated changes across files, runs bash commands, watches terminal output in real time
4. **Self-Correction**: Monitors linter and compiler errors as it works, fixing issues like missing imports, type mismatches, and syntax errors proactively
5. **Review**: Every edit appears as a diff for review, modification, or reversion. All changes are tracked with checkpoints for easy undo

The VS Code and JetBrains extensions share a common agent core. The CLI runs the same engine in terminal or headless mode. The SDK exposes this engine programmatically for custom [[concepts/agent-harnesses]].

## Comparison to Other Coding Agents

| Dimension | Cline | Devin | Cursor | Claude Code | OpenAI Codex |
|-----------|-------|-------|--------|-------------|--------------|
| **Open Source** | Yes (full) | No (proprietary) | No (proprietary) | No (proprietary) | No (proprietary) |
| **IDE Support** | VS Code, JetBrains, CLI, SDK | Web IDE + Desktop | Standalone IDE (Cursor 3) | CLI + VS Code | CLI + SDK |
| **Model Freedom** | Any provider (10+ backends) | Proprietary models | Proprietary + API keys | Anthropic only | OpenAI only |
| **Multi-Agent** | Built-in teams + Kanban | Limited | Fleet agents (Cursor 3) | Limited | Via SDK |
| **Extensibility** | Plugins + MCP + SDK | Limited | Extensions (new in 3) | MCP | SDK |
| **Plan/Act Mode** | Explicit toggle | Implicit | Implicit | Implicit | Implicit |
| **Pricing** | Free (BYO API keys) | Subscription ($500+/mo) | Subscription ($20+/mo) | API usage | API usage |
| **Created** | July 2024 | March 2024 | 2023 (Cursor 3: Apr 2026) | 2025 | 2021 (Codex CLI: 2025) |

Cline's key differentiators are its **full open-source model**, **provider agnosticism**, **explicit Plan/Act toggle**, and **multi-agent team coordination** built into the core product.

## Timeline

- **July 6, 2024**: Initial release on GitHub
- **2025**: CLI and SDK products launched; JetBrains plugin added
- **2026**: Kanban multi-agent board released; team coordination and scheduled agents introduced; surpasses 64K GitHub stars

## Related Pages

- [[concepts/coding-agents/coding-agents]] — Overview of the coding agent landscape
- [[entities/devin]] — Cognition AI's proprietary coding agent
- [[entities/cursor-3]] — Anysphere's IDE rebuilt for agent-driven development
- [[entities/claude-code]] — Anthropic's CLI coding agent
- [[entities/openai-codex]] — OpenAI's coding agent and SDK
- [[concepts/self-driving-codebases]] — The broader paradigm of autonomous codebase modification
- [[concepts/agent-harnesses]] — Agent execution environments and frameworks
- [[concepts/mcp]] — Model Context Protocol, supported by Cline for extensibility
