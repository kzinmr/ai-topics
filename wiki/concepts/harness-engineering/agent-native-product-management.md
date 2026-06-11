---
title: "Agent-native Product Management"
created: 2026-05-02
updated: 2026-05-02
type: concept
tags:
  - concept
  - product-management
  - ai-agents
  - agentic-engineering
  - mcp
  - harness-engineering
aliases:
  - ai-native-product-management
  - pm-with-agents
  - agent-native-pm
sources:
  - raw/articles/2026-05-02_guide-to-agent-native-product-management.md
---

# Agent-native Product Management

Agent-native Product Management is an approach where product managers use AI agents (particularly coding agents like Claude Code) as the primary interface for planning, monitoring, and shipping software. Introduced by [[entities/marcus-moretti|Marcus Moretti]] of [[entities/every-inc|Every]], it represents a shift from traditional PM tooling (Jira, spreadsheets, manual reporting) to agent-driven workflows.

## Core Principles

### 1. The Conversation is the Work
PM work happens entirely within a chat interface with an AI agent (e.g., Claude Code, Codex). There is no separate tool for tickets, dashboards, or reports — everything is managed through the conversation.

### 2. 80/20 Planning to Execution
The traditional SDLC ratio of 20% planning / 80% execution is inverted. With agents handling execution (code, tickets, queries), PMs spend 80% of their time on strategy, user research, and design thinking.

### 3. Living Strategy Documents
The `ce:strategy` skill produces a `strategy.md` file based on Richard Rumelt's *Good Strategy Bad Strategy* framework:
- **Target Problem:** A recurring, expensive pain point
- **Approach:** A specific "guiding policy" 
- **Persona:** Focused target (per *Crossing the Chasm*)
- **Metrics:** 3–5 S.M.A.R.T. KPIs
- **Tracks:** 2–4 multi-month initiatives

### 4. Automated Product Health (Pulse)
The `ce:product-pulse` skill generates daily product health reports by connecting agents to data sources via **[[concepts/mcp|MCP (Model Context Protocol)]]**:
- **Product Analytics:** PostHog, Mixpanel, Amplitude
- **Tracing:** Datadog, Sentry, Logfire
- **Payments:** Stripe, Paddle
- **Database:** Read-only SQL replicas

The report covers: headlines, usage metrics (with deltas), system performance (p50/p95/p99 latency), and follow-up items.

### 5. Agent-Managed Backlogs
Instead of writing tickets manually, PMs use `/ce-ideate` and `/ce-plan` commands. The agent writes, moves, and updates tickets on GitHub Issues or Linear via MCP. Kanban is simplified to: Now / Next / Later and In Progress / Done.

## Relationship to Harness Engineering

Agent-native PM can be seen as the **product management application** of [[concepts/harness-engineering|Harness Engineering]]. While harness engineering focuses on optimizing the agent's execution environment (tools, context, feedback loops), agent-native PM focuses on the *planning and monitoring* layers:

| Layer | Harness Engineering | Agent-native PM |
|-------|--------------------|-----------------|
| Planning | Build-Verify Loop | ce:strategy |
| Execution | Context engineering, tools | ce:ideate, ce:plan |
| Monitoring | Eval-driven optimization | ce:product-pulse |
| Feedback | Loop detection | Pulse followups |

## Tooling

- **Plugin:** `EveryInc/compound-engineering-plugin` (GitHub, open-source)
- **Install:** `/plugin marketplace add EveryInc/compound-engineering-plugin` in Claude Code
- **Routines:** Schedule `/ce:product-pulse` daily via Claude Code Routines

## The Qualitative Balance

Agents cannot replace:
- Direct user interviews (15-min call booking links in marketing emails)
- Design thinking and product vision
- Domain expertise and judgment

Feedback platforms with MCPs (Canny, Featurebase) bridge qualitative input into the agent's context.

## Related Pages

- [[entities/every-inc]] — Publisher and origin company
- [[entities/marcus-moretti]] — Creator of this framework
- [[entities/kieran-klaassen]] — Creator of Compound Engineering
- [[concepts/compound-engineering-every]] — The broader engineering philosophy
- [[concepts/harness-engineering]] — Related engineering discipline
- [[concepts/mcp]] — Model Context Protocol for data integration
- [[entities/claude-code]] — Primary agent used
