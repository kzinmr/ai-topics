---
title: "Every Inc."
created: 2026-05-02
updated: 2026-05-25
type: entity
tags:
  - entity
  - company
  - ai-native
  - product-management
  - agent-employees
  - human-agent-collaboration
sources:
  - raw/articles/2026-05-02_guide-to-agent-native-product-management.md
  - raw/articles/2026-05-21_after-automation.md
---

# Every Inc.

**Every** is a media and software company founded in 2020 by Dan Shipper (CEO & cofounder). It publishes a daily newsletter about technology and builds multiple AI-native software products. Every is known for pioneering **[[concepts/compound-engineering-every|Compound Engineering]]** — an AI-native software development philosophy.

## Key Facts

- **Founded:** 2020
- **Founder/CEO:** [[entities/dan-shipper|Dan Shipper]]
- **Lead Investors:** Bedrock, Reid Hoffman, Starting Line
- **Team Size:** ~30 people (as of May 2026)
- **Revenue:** 7-figure (as of 2025), from newsletter subscriptions + software products + consulting
- **Philosophy:** "Two-slice teams" — small, cross-functional teams (often single-person) running entire products with AI assistance

## Products

- **Spiral** — AI writing partner for automating repetitive creative work (GM: [[marcus-moretti]])
- **Cora** — AI email assistant (GM: [[kieran-klaassen]])
- **Sparkle** — File management tool (Mac)
- **Monologue** — Voice dictation software
- **Lex** — AI-powered writing tool

## AI Coworker Agents

Every deploys internal agents as first-class team members, @-mentionable in Slack:

| Agent | Role | Function |
|---|---|---|
| **Claudie** | Consulting | Writes sales proposals, drafts training decks, tracks project todos |
| **Andy** | Editorial | Collects "nuggets" from internal Slack, creates story digests for newsletter |
| **Viktor** | General | Gathers growth metrics, analyzes surveys, turns discussions into research memos |

**Embedded agent:** **Fin** (customer service platform) participated in 65% of 202 support conversations and closed 40.1% of actionable conversations without humans (May 2026).

**Agent maintenance reality:** Personal agents failed because employees abandoned them. Every now has a dedicated AI engineer team centrally managing all agents. Even a PowerPoint automation requires **24 skills, 18 scripts, $62 in tokens per deck.**

## Work Patterns

Every operates in two modes (see [[concepts/after-automation]]):

1. **Agent Employees** — Async delegation: agents produce output without human in the loop (Claudie, Andy, Viktor, Fin)
2. **Human-Agent Collaboration** — [[concepts/human-sandwich|Human Sandwich]] pattern: synchronous back-and-forth in shared workspaces (Codex, Claude Code, Cowork)

By May 2026:
- No one writes code by hand — all engineering is AI-assisted
- 95% of CEO's work emails handled by AI (via Cora in Codex)
- Managers commit code like ICs; engineers talk directly to customers

## Compound Engineering

Every's open-source **compound-engineering-plugin** (GitHub: `EveryInc/compound-engineering-plugin`, 7,000+ stars) provides agent-agnostic skills for AI-native development:

- `/ce-strategy` — AI-led product strategy interviews based on *Good Strategy Bad Strategy*
- `/ce-product-pulse` — Automated product health reports via MCP-connected data sources
- `/ce-ideate`, `/ce-plan`, `/ce-brainstorm` — AI-assisted feature planning

See [[concepts/agent-native-product-management]] for the PM-focused application.

## Significance

Every is notable as a radical demonstration of AI-first operations: running 5 software products with single-person engineering teams, being "100% AI-written code" (per Dan Shipper), and achieving 7-figure revenue with minimal headcount. The company's experience forms the basis for the [[concepts/after-automation|After Automation]] paradox: more automation creates more expert human work, not less.

## Related Pages

- [[entities/dan-shipper]] — CEO and cofounder
- [[entities/marcus-moretti]] — GM of Spiral, author of Agent-native PM guide
- [[entities/kieran-klaassen]] — GM of Cora, author of Compound Engineering guide
- [[concepts/after-automation]] — The automation paradox observed at Every
- [[concepts/human-sandwich]] — Kieran's collaboration pattern
- [[concepts/ai-slop]] — Dan's definition of AI slop
- [[concepts/agent-native-product-management]]
- [[concepts/compound-engineering-every]]
