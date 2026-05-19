---
title: DeerFlow
created: 2026-05-15
updated: 2026-05-15
type: concept
tags:
  - ai-agents
  - multi-agent
  - harness-engineering
  - open-source
  - sandbox
  - skill-graph
  - deep-research
sources: [raw/articles/2026-05-15_deerflow-bytedance-superagent.md]
---

# DeerFlow

**DeerFlow** (Deep Exploration and Efficient Research Flow) is an open-source SuperAgent harness by ByteDance that orchestrates sub-agents, memory, and sandboxes to handle tasks from minutes to hours. MIT licensed, 67.5k+ GitHub stars.

## Architecture

v2.0 is a ground-up rewrite (no shared code with v1). Built as a backend (Python) + frontend (Node.js) system deployable via Docker.

Core components:
- **Sub-agents**: Parallel and sequential task execution
- **Memory**: Long/short-term memory for context engineering
- **Sandbox**: Docker-based persistent filesystem (recommends AIO Sandbox — Browser, Shell, File, MCP, VSCode Server in one container)
- **Skills**: Progressively loaded, only what's needed when needed. Extensible via custom skill files
- **Multi-model**: Doubao-Seed-2.0-Code, DeepSeek v3.2, Kimi 2.5, OpenAI, Gemini

## Key Features

- **Planning & Sub-tasking**: Plans ahead, reasons through complexity, executes sequentially or in parallel
- **Persistent execution**: Docker sandbox with mounted filesystem for long-running tasks
- **InfoQuest integration**: BytePlus intelligent search and crawling toolset
- **One-line setup**: Coding agents can bootstrap via Install.md with a single prompt

## History

- February 28, 2026: v2.0 claimed #1 GitHub Trending
- Partnership with BytePlus/Volcengine for cloud deployment
- Official site: deerflow.tech

## Related Pages

- [[concepts/gnap-git-native-agent-protocol]] — Git-native agent coordination protocol
- [[concepts/managed-agents]] — Managed agents and vendor lock-in analysis
- [[entities/bernstein]] — Deterministic orchestrator for parallel coding agents
- [[concepts/ml-intern]] — HuggingFace's autonomous ML engineer agent
- [[concepts/granite-4-1]] — IBM enterprise models
