---
title: "Foundation Capital"
type: entity
description: "Venture capital firm that published 'AI's Trillion-Dollar Opportunity: Context Graphs' — arguing that the next trillion-dollar platforms will be built by capturing decision traces, not adding AI to existing data"
tags: [company, vc, foundation-capital, context-graph, investor]
status: complete
related:
  - "[[context-graph]]"  # Their core thesis
  - "[[jaya-gupta]]"     # Partner who co-authored the article
  - "[[playerzero]]"     # Path 3 startup in their portfolio
status: complete
created: 2026-04-20
sources: []
---

# Foundation Capital

## Overview

**Type:** Venture Capital Firm  
**Focus:** Enterprise AI, Agent Infrastructure, Context Graphs  
**Key Publication:** ["AI's Trillion-Dollar Opportunity: Context Graphs"](https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity) (December 22, 2025)

## Core Thesis

Foundation Capital's central argument in the Context Graphs article:

1. **Decision traces > rules** — Agents need access to how rules were applied in specific cases, not just what the rules say
2. **Execution path advantage** — Systems of agents startups sit in the orchestration layer at decision time and can capture context that incumbents (Salesforce, Snowflake) cannot
3. **Context graph as moat** — The accumulated structure of decision traces becomes the real source of truth for autonomy
4. **Three startup paths** — Replace entire systems (Regie), replace modules (Maximor), or create new systems of record (PlayerZero)

## Key People

- **Jaya Gupta** — Partner, co-author of Context Graphs article
- **Ashu Garg** — Co-author of Context Graphs article

## Featured Portfolio Companies

The article features three startups as exemplars of different paths:

| Company | Path | Description |
|---------|------|-------------|
| [Regie.ai](https://www.regie.ai/) | Path 1 | AI-native sales engagement replacing Outreach/Salesloft |
| [Maximor](https://www.maximor.ai/) | Path 2 | Finance automation; ERP-agnostic audit-ready agents |
| [PlayerZero](https://playerzero.ai/) | Path 3 | SRE automation with context graph as engineering world model |

## Relationship to the Context Graph Concept

Foundation Capital's article is the canonical source for the "context graph" thesis in AI agent infrastructure. Key contributions:

- **Articulates the "two clocks problem"** — State clock vs. decision clock divergence
- **Identifies the execution path advantage** — Being in the orchestration layer at commit time vs. bolting on governance post-hoc
- **Maps the five-plane architecture** — State → Orchestration → Decision → Control → Observability
- **Provides the three-path framework** — Replace all, replace modules, create new

## Critical Reception

The article was described as "super provocative" and "went very viral" but with noted disagreements:

> "I thought it was super provocative. I agreed with many parts of it. I disagree with a few parts around. You know, it's not gonna be as easy as just if we just had the agent traces, then we can finally do that work because there's just so much more other stuff that we haven't been able to capture and digitize."

— Referenced reaction in [Latent Space podcast](https://latent.space/) (episode discussing the article)

Key criticisms:
- **Incumbent response underweighted** — Salesforce Agentforce, ServiceNow Now Assist, Snowflake Cortex Agents, Databricks Agent Bricks are all actively moving into the space
- **Connection is harder than capture** — The "two clocks" linking problem across heterogeneous systems is non-trivial
- **Trillion-dollar winner unproven** — Multiple vertical winners may be more likely than a single platform

## Related

- [[context-graph]] — The main concept page
- [[jaya-gupta]] — Partner who co-authored the article
- [[playerzero]] — Path 3 startup (context graph as engineering world model)
- [[arize]] — Observability layer mentioned in the article