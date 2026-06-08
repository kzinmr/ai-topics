---
title: Notion
type: entity
created: 2026-05-20
updated: 2026-05-20
tags:
  - company
  - product
  - ai-native
  - developer-tooling
aliases:
  - Notion Labs
  - notion.so
sources:
  - raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--c27d9b81.md
  - https://www.notion.so/
  - https://developers.notion.com/
related:
  - concepts/notion-mcp
  - concepts/notion-cli
  - concepts/agent-native-product-management
---

# Notion

**Notion** is a knowledge work decacorn that has been building AI tooling since before ChatGPT. Under the leadership of engineering leads like **Sarah Sachs** and product thinkers like **Simon Last**, Notion has evolved from a document/workspace tool into an agent-native system of record for enterprise work.

## Overview

Notion was founded as a unified workspace for notes, docs, and project management. By 2025-2026, the company had pivoted aggressively toward AI-native product design, launching features like Q&A (2023), unified AI (2024), Meeting Notes (2025), and **Custom Agents** (2026). The company's AI strategy is guided by the "Agent Lab" thesis: not just wrapping a model, but understanding how people collaborate and building the right product system around frontier capabilities.

## AI Product Evolution

| Year | Feature | Significance |
|------|---------|-------------|
| 2023 | Q&A | Early AI-powered document queries |
| 2024 | Unified AI | Consolidated AI capabilities across all surfaces |
| 2025 | Meeting Notes | High-signal data capture powering search, agents, workflows |
| 2026 | Custom Agents | User-configurable agents with tool access, permissions, and memory |

## Custom Agents Architecture

Notion's Custom Agents represent a significant investment in agent-native product design. The feature was rebuilt **four or five times** before production readiness, spanning from early tool-calling experiments in 2022 to the current architecture.

### Agent Harness Evolution
1. **Early JavaScript coding agents** — initial experiments, too fragile
2. **Custom XML** — structured but complex
3. **Markdown and SQL-like abstractions** — simpler, more maintainable
4. **Tool definitions with progressive disclosure** — current approach
5. **Shortened system prompt** — reduced complexity exposed to the model

### Key Design Principles
- **Progressive tool disclosure**: Agents only see tools relevant to their current context
- **Shared databases as primitives**: Agents compose by sharing Notion databases
- **Agent-to-agent invocation**: Agents can call other agents
- **Manager agents**: Supervising dozens of specialized agents
- **Memory as pages and databases**: Notion's existing data model serves as agent memory
- **Self-configuring agents**: Agents that can inspect their own failures and edit their own instructions

### Eval Framework
Notion runs a three-tier evaluation system:
- **Regression tests** in CI — must pass before deployment
- **Launch-quality evals** — report card requiring 80-90% pass rate on user journeys
- **Frontier/Headroom evals** — intentionally designed to pass only ~30% of the time to see where model capabilities are going

Notion maintains a dedicated **Model Behavior Engineer** role and **evals team** ("agent dev velocity") to ensure every team can maintain their own evals. A custom agent triggers alerts to teams when major failures are detected in nightly eval runs.

## Meeting Notes as Growth Loop

Meeting Notes became one of Notion's strongest growth loops by serving as **high-signal data capture** rather than just transcription. It powers:
- Search across company knowledge
- Custom agent context and workflows
- Follow-up automation
- Broader system of record for company collaboration

## Organizational Structure for AI

Notion organizes AI work across three layers:
1. **Core AI capabilities and infrastructure** (~50 people under Sarah Sachs) — eval framework, model behavior understanding, agent harness
2. **Product packaging teams** (30-40 people) — how AI shows up in chat, Custom Agents, Meeting Notes
3. **Every product surface** — every team building for humans also builds for agents, since "the majority of traffic will come from agents"

## Engineering Culture

- **"Demos over memos"** — prototypes must be working feature flags, not mockups
- **Low-ego teams comfortable deleting their own work** — critical when rebuilding harnesses multiple times
- **Security brought in early** — not as an afterthought
- **Hackathons for company-wide AI literacy** — encouraging all employees to build agentic tool loops
- **"Simon Vortex"** — a rapid prototyping mode where senior engineers swarm on problems with high velocity and daily direction changes

## Notion's Position on Foundation Models

Notion is **not eager to train a foundation model**. Instead, the company focuses on:
- Fine-tuning and optimization for specific use cases
- **Retrieval/ranking** as a critical investment area as more searches come from agents
- Using the best available models through API providers
- Building the product system around models, not the models themselves

## Pricing Model

Notion prices Custom Agents using **credits as an abstraction** over:
- Tokens consumed
- Model type (auto-selects the right model for the right task)
- Serving tier
- Web search costs
- Future sandbox costs

Usage-based pricing was necessary because agent workloads vary dramatically in cost.

## MCP and CLI Strategy

Notion supports both MCP and CLI approaches:
- **Notion MCP** (`mcp.notion.com/mcp`) — OAuth-authenticated server for AI tools
- **Notion CLI** (`ntn`) — terminal-first interface designed for both humans and agents
- Simon Last is bullish on CLI's self-debugging nature; MCP makes sense for standardized tool access

## Key People

- **Sarah Sachs** — Engineering leadership, Core AI capabilities
- **Simon Last** — Product/Engineering, agent harness architecture
- **Ivan Zhao** — CEO, company vision

## Related Tools

- [[concepts/notion-mcp]] — Notion's MCP server implementation
- [[concepts/notion-cli]] — Notion's command-line interface
- [[concepts/agent-native-product-management]] — Product philosophy driving Notion's AI features

## Sources

- [Latent Space Podcast: Notion's Token Town — Simon Last & Sarah Sachs](raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--c27d9b81.md) — April 2026 podcast transcript
- [Notion Developers](https://developers.notion.com/)
- [Notion Custom Agents Launch](https://www.notion.so/)
