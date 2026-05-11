---
title: Nicolas Bustamante
created: 2026-04-30
updated: 2026-05-11
type: entity
tags:
  - person
  - ai-agents
  - fintech
  - harness-engineering
  - microsoft
aliases: ["@nicbstme"]
sources:
  - raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md
  - raw/articles/2026-05-01_nicolas-bustamante_agent-memory-engineering.md
description: "AI for knowledge workers at Microsoft. Previously CEO of Fintool (acq. Microsoft), CEO of Doctrine (acq. Summit Partners). Authored comprehensive Agent Memory Engineering analysis comparing Claude Code, Codex, and Hermes memory architectures."
---

# Nicolas Bustamante

## Overview

**Nicolas Bustamante** (@nicbstme) is an AI entrepreneur now working on agentic AI experiences for Microsoft Office (Word, Excel, PowerPoint). Previously CEO of **Fintool** (YC-backed, acquired by Microsoft, March 2026) and CEO of **Doctrine** (Europe's largest legal information platform, acquired by Summit Partners, 2023). Dropped out of École Normale Supérieure at 21.

Author of two influential 2026 analyses: "Lessons from Building AI Agents for Financial Services" (April) and **"Agent Memory Engineering"** (May) — a deep comparison of how Claude Code, Codex CLI, and Hermes handle memory, which concluded that simple markdown + bash beats every clever architecture.

## Key Contributions

### Agent Memory Engineering (May 2026)

Comprehensive analysis of three production agent memory architectures. Key findings:
- **Models are post-trained on their harness**: memory behavior is inseparable from the agent
- **Every clever architecture lost**: vector DBs, knowledge graphs, dedicated memory agents all lost to markdown + bash
- **Three architectures identified**: Bounded Snapshot (Hermes), Two-Phase Async Pipeline, Typed Live Writes (Claude Code)
- **Five design questions** every memory system must answer: storage format, load strategy, write discipline, signal gate, cold start
- **Cold start is unsolved**: no standard for bootstrapping agent memory from existing user data

→ See [[concepts/agent-memory-engineering]]

### AI Agent Architecture in Financial Services (April 2026)

Bustamante articulated several foundational patterns:

1. **S3-First Architecture**: Using object storage as the primary data source, with databases as secondary indexes
2. **Markdown-Based Skills**: Allowing non-engineers to encode financial methodologies as `.md` files
3. **Pre-Warmed Sandboxes**: Eliminating latency by warming up execution environments proactively
4. **AskUserQuestion Tool**: Agent-initiated human clarification for high-stakes decisions
5. **"The Model Will Eat Your Scaffolding"**: Designing for model obsolescence as capabilities improve

### Moat Philosophy

> "Your moat is not the model. Your moat is everything you build around it — financial data, domain-specific skills, reliable infrastructure, and trust."

This perspective positions infrastructure and data quality as the real competitive advantage, not the underlying LLM.

## Technical Stack (as described by Bustamante)

- AWS (S3, Lambda, ABAC)
- PostgreSQL (secondary index)
- Temporal (durable execution)
- Redis Streams (real-time updates)
- Braintrust (evaluation framework)
- Claude (Sonnet for complex tasks, Haiku for simple queries)

## Related Entities

- [[entities/fintool]] — Company where Bustamante works
- [[concepts/s3-first-architecture]] — Architecture pattern he pioneered
- [[concepts/markdown-based-skills]] — Skill system he designed

## Sources

- Nicolas Bustamante, "Lessons from Building AI Agents for Financial Services", LinkedIn, April 2026
