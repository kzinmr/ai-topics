---
title: Google Antigravity
created: 2026-05-23
updated: 2026-05-23
type: entity
tags: [entity, product, google, platform, agentic-engineering, coding-agents, ai-agents, agent-sdk, agent-framework, multi-agent, orchestration, developer-tooling, cli, infrastructure]
sources: [https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/, https://ai.google.dev/gemini-api/docs/antigravity-agent, https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/]
---

# Google Antigravity

Google's **agent-first development platform**, announced at I/O 2026 (May 19, 2026). Antigravity is the unified runtime, harness, and SDK for building, managing, and deploying AI agents powered by [[entities/gemini-3-5-flash|Gemini 3.5 Flash]]. It represents Google's bet that the developer experience of the future is agent-native, not app-native.

## Overview

> "Google Antigravity is our agent-first development platform for developers to take an idea and turn it into a production-ready app."

Antigravity provides three surfaces — desktop, CLI, and SDK — all sharing the same agent harness that powers Google's own products including [[concepts/gemini-spark|Gemini Spark]], Daily Brief, and AI Mode in Search.

## Platform Components

### Antigravity 2.0 (Desktop)
- Standalone desktop application — central home for agent interaction
- Orchestrate multiple agents to execute tasks **in parallel**
- **Dynamic subagents** for parallelized workflows
- **Scheduled tasks** for background automation
- Ecosystem integrations: Google AI Studio, Android, Firebase
- Export from Google AI Studio with full project context preserved

### Antigravity CLI
- Lightweight terminal surface for maximum velocity
- Create agents instantly without a GUI
- Google encourages migration from Gemini CLI to Antigravity CLI

### Antigravity SDK
- Programmatic access to the same agent harness
- Optimized for Gemini models (especially 3.5 Flash)
- Define custom agent behaviors and host on your own infrastructure

## Managed Agents (Gemini API)

Launched alongside Antigravity: **Managed Agents in the Gemini API**. A single API call provisions:

- Isolated Linux sandbox with code execution (Bash, Python, Node.js)
- File management (read, write, edit, search across interactions)
- Web access (Google Search + URL fetching)
- **Automatic context compaction** at ~135K tokens for long-running sessions
- Customization via AGENTS.md and SKILL.md files (mounted directly into sandbox)

Each interaction creates or resumes an environment, preserving all files and state across calls. Available via the Interactions API and Google AI Studio.

## Agent Capabilities Demo (with Gemini 3.5 Flash)

When paired with Antigravity, Gemini 3.5 Flash demonstrated:
- Paper-to-playable-game synthesis: AlphaZero paper → fully playable game (6 hours, two agents)
- Legacy code migration: messy codebase → Next.js
- Self-improving game loop: builder agent + player agent in rapid iteration
- City landscape generation, interactive animations, hardware mockups, branding concepts

## Enterprise Adoption (May 2026)

| Partner | Use Case |
|---|---|
| **Shopify** | Parallel subagents for global merchant growth forecasts |
| **Macquarie Bank** | 100+ page document reasoning for customer onboarding |
| **Salesforce Agentforce** | Multi-turn tool calling with context retention |
| **Ramp** | Multimodal OCR with historical pattern reasoning |
| **Xero** | Autonomous multi-week 1099 tax workflows |
| **Databricks** | Real-time data monitoring and issue diagnosis |

## Technical Details

- Default tools: `code_execution`, `google_search`, `url_context`
- Filesystem enabled via `environment` parameter
- Pay-as-you-go pricing based on underlying Gemini token usage
- Preview status — features and schemas may change
- Unsupported: `temperature`, `top_p`, `top_k`, structured outputs, MCP tool (not yet)

## Related

- [[entities/gemini-3-5-flash|Gemini 3.5 Flash]] — the default model powering Antigravity
- [[concepts/gemini-spark|Gemini Spark]] — 24/7 personal agent built on Antigravity
- [[entities/gemini-enterprise-agent-platform|Gemini Enterprise Agent Platform]]
- [[entities/google-adk|Google ADK 2.0]]
- [[concepts/coding-agents|Coding Agents]]
- [[concepts/agentic-engineering|Agentic Engineering]]
