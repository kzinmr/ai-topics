---
title: Salesforce Headless 360
created: 2026-05-05
updated: 2026-05-05
type: entity
tags: [platform, headless-saas, agentic-engineering, mcp, enterprise, product]
sources: [raw/articles/2026-05-01_salesforce-8-ways-ai-agents-evolving-2026.md, raw/articles/2026-05-05_ai-agent-news-weekly-apr28-may4.md]
---

# Salesforce Headless 360

**Salesforce Headless 360** is the company's May 2026 restructuring of its platform as an **agent-first platform**, exposing every workflow, object, and business logic through APIs, [[concepts/model-context-protocol-mcp|MCP]] tools, and CLI commands. The browser UI is now optional.

## Core Thesis

> The UI is no longer the primary product; programmatic access is.

AI agents now have full Salesforce data access with inherited human permissions — reading, writing, and acting across CRM data from any surface (Slack, ChatGPT, etc.) without a browser tab.

## Key Capabilities

- **API-First Access:** Every workflow and business object exposed via APIs
- **MCP Integration:** Native [[concepts/model-context-protocol-mcp|Model Context Protocol]] tool support
- **CLI Access:** Command-line interface for agent-driven operations
- **Inherited Permissions:** Agents operate with the same permission model as human users
- **No GUI Required:** The browser is now optional for CRM operations

## Context in the Headless SaaS Movement

Salesforce Headless 360 exemplifies the [[concepts/headless-saas|Headless SaaS]] paradigm — SaaS products rebuilt with agent-first APIs as the primary interface, following the vision articulated by [[entities/ivan-burazin|Ivan Burazin]] (Daytona CEO).

## Relationship to Agentforce

Headless 360 is part of the broader Salesforce Agentforce platform evolution:

- **Agentforce Runtime:** Rebuilt to reduce LLM calls from 4→2 before first token
- **HyperClassifier:** Proprietary SLM handling topic classification 30x faster than general-purpose models
- **Agentforce Observability:** Session-level tracing, intent categorization, anomaly alerting
- **Trusted Gateway:** Admin-defined access controls to prevent MCP "tool poisoning attacks"

## Connections
- Implements [[concepts/headless-saas|Headless SaaS]] at enterprise scale
- Uses [[concepts/model-context-protocol-mcp|MCP]] as the universal agent-tool interface
- Part of [[concepts/agent-governance|Agent Governance]] via trusted gateway model
- Builds on [[entities/salesforce|Salesforce]]'s broader AI platform strategy
