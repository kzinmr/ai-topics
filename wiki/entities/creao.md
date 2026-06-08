---
title: "CreaoAI (CREAO)"
created: "2026-05-31"
updated: "2026-05-31"
type: entity
tags:
  - company
  - harness-engineering
  - agent-platform
  - enterprise-saas
  - ai-adoption
  - multi-agent
  - platform-economics
sources:
  - "https://creao.ai/ai-super-agent"
  - "https://creao.ai/blog/the-self-healing-agent-harness"
  - "https://creao.ai/blog/we-built-an-agent-platform.-then-the-agents-rebuilt-it."
  - "https://docs.creao.ai/features/agents"
  - "https://www.unite.ai/peter-pang-co-founder-and-cto-of-creao-interview-series/"
  - "https://sv101.fireside.fm/251"
  - "raw/articles/2026-05-24_anorthchen_agent-harness-business.md"
---

# CreaoAI (CREAO)

## Overview

**CreaoAI** (CREAO) is a Palo Alto-based AI agent platform company founded in 2025. Their product, the **CREAO Super Agent**, is a general-purpose AI agent with a bias for action that executes real tasks in dedicated computing environments, connects to business tools via APIs, carries context across sessions, and runs scheduled workflows.

CREAO is a leading voice in the [[concepts/harness-engineering|harness engineering]] movement, articulating the thesis that "the harness layer must be productized for agent businesses to grow" (per [[entities/anorth-chen|North Chen]], Head of Community).

## Key Facts

| Attribute | Detail |
|-----------|--------|
| **Founded** | 2025 (launched Sept 2025) |
| **HQ** | Palo Alto, California |
| **Website** | [creao.ai](https://creao.ai/) |
| **Users** | 200,000+ (organic adoption since launch) |
| **Team** | ~25 employees, <10 engineers |
| **Funding** | $25M total across 3 rounds (latest $10M from Prosperity7 Ventures, 2026) |
| **Docs** | [docs.creao.ai](https://docs.creao.ai/) |

## Leadership

| Name | Role | Background |
|------|------|------------|
| Peter Pang | Co-founder & CTO | PhD Physics (Stony Brook), ex-Meta LLaMA foundation team (~6 years), ex-Apple ML Engineer |
| Cheng Kai (Kai) | Co-founder & CEO | AI-first organizational transformation |
| Clark | Co-founder & CPO | AI-first go-to-market strategy |
| [[entities/anorth-chen|North Chen]] | Head of Community | Harness platform economics thesis author |

## Platform Architecture

CREAO's architecture embodies the harness platform thesis:

### Super Agent

The core product — a general-purpose AI agent that:
- Executes real tasks in fully isolated sandbox environments
- Connects to business tools via APIs and connectors
- Carries context across sessions (cross-session memory with proactive capture, deduplication, relevance-based recall)
- Runs scheduled workflows autonomously (daily, weekly, monthly, custom cron)
- Orchestrates across multiple AI models (fast models for routine work, capable models for complex reasoning)
- Users save successful conversations as reusable agents with structured input forms and version control

### The Self-Healing Agent Harness

CREAO built an internal harness system that runs a self-healing loop on three components:

1. **The Grader** — Tri-judge panel (Anthropic + OpenAI + Google judges in parallel) scores every live agent response asynchronously
2. **The Engineering Pipeline** — Six daily jobs turn low scores into Linear tickets, draft PRs, and verified fixes
3. **The Bridge** — AI-gated grey rollouts where Grader scores decide whether new code ships (10% → 20% → 50% → 100%)

This replaces staging environments, manual QA review, and human release approvals.

### AI-First Organization

CREAO practices what it preaches:
- **99% of production code written by AI** (Peter Pang stated in 2026: "I haven't written a single line of code in 2026")
- **3-8 production deployments per day**
- **Bug-to-fix cycle: 1-2 hours** (vs. 1 week previously), with AI auto-submitting patches for 50%+ of issues
- **No product manager role** — alignment costs eliminated by AI-led coordination
- **10-person team completed in 2 weeks what previously required 100 people over 4-5 months**

### Write Autonomy System

Production-grade action governance:
- **Read actions** — always execute immediately
- **Write actions** — require approval by default, configurable to full-auto
- **Destructive actions** — blocked if validation fails
- **Audit trail** — all actions logged for review

### Agent Brain

Knowledge and capability management:
- **Memory system** — cross-session memory with proactive capture, deduplication, relevance-based recall
- **Skills** — modular instruction packages (SKILL.md format), installable from GitHub repos or uploaded as ZIP
- **Connectors** — 20+ integrations (Gmail, Slack, Google Sheets, Notion, etc.)
- **Secrets** — encrypted credential management, per-user scoping, environment variable injection at runtime

## Harness Platform Positioning

North (Head of Community) articulated CREAO's positioning as an agent harness platform:

> "The harness layer must be productized for agent businesses to grow."
> ("The harness layer must be productized for agent businesses to grow")

### Three-Layer Model (North Chen)

| Layer | Analogy | Components | Who builds it |
|-------|---------|------------|---------------|
| **LLM (Brain)** | Intelligence only | Input/output text, no tools, no memory, no time awareness | OpenAI, Anthropic, Google, DeepSeek |
| **Harness (Body/Nervous System)** | Meta-capabilities | Context management, tool execution, sandbox, state, observability, safety, model routing, error recovery | Platform companies (CREAO, Warp, LangChain) |
| **Agent (Professional)** | Domain expertise | Business logic, domain prompts, CRM/workflow integration, success criteria | Business teams using a harness platform |

**Key thesis**: "Model determines the ceiling, harness determines the realization rate".

### The Agent Economy

CREAO argues that the purchasing behavior of client companies is being rewritten by AI:
- SaaS dashboards designed for humans are becoming irrelevant
- The real audience for marketing content may be AI agents, not humans
- "When the system makes an error, don't try to correct the intelligence, but think about how to fix the system" (Clark, CPO)

## Industry Context

CREAO operates in the emerging "agent harness platform" category alongside:
- [[entities/anthropic]] (Claude Code — coding agent harness)
- [[entities/openai]] (Codex — coding agent harness)
- [[entities/warp-terminal]] (Oz — multi-harness control plane)
- [[concepts/managed-agents]] — meta-harness pattern

## Related Entities

- [[entities/anorth-chen]] — Head of Community, author of the harness platform economics thesis
- [[entities/peter-pang]] — Co-founder & CTO, former Meta LLaMA researcher, author of "Self-Healing Agent Harness"
- [[concepts/harness-engineering]] — CREAO is a leading practitioner and advocate
- [[concepts/agent-economics]] — Platform economics of agent infrastructure
- [[concepts/service-as-software]] — AI agents as operational services
