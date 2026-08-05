---
title: "Wish Factory"
type: concept
tags:
  - ai-agents
  - agentic-engineering
  - autonomous-agents
  - human-agent-collaboration
  - github
  - ai-automation
  - coding-agents
created: 2026-08-05
updated: 2026-08-05
aliases: [Wish Factory Pattern]
sources:
  - raw/articles/2026-08-04_yegge-ai_shape-of-things-to-come.md
  - https://yegge.ai/essays/the-shape-of-things-to-come/
---

# Wish Factory

## Overview

The **Wish Factory** is a pattern where end users (players, customers, admins) submit feature requests or bug reports through a natural language interface, and an AI agent automatically triages, implements, tests, and ships the fix — often without any human in the loop.

The term was coined by [[entities/steve-yegge]] in "The Shape of Things to Come" (Aug 2026), inspired by **Guy Podjarny**'s description of [[entities/tessl]] — a tool that accepts GitHub Issues (not PRs) and implements them autonomously.

## How It Works

### Yegge's Implementation (Wyvern)
1. **Sage agent** logs into the game and listens on a moderator/admin channel
2. Admin types: `"sage - players say the new fireball spell is lagging them during Live Quests"`
3. Sage **investigates**, creates a Beads issue
4. The issue gets picked up by the Wheelhouse fleet for implementation
5. Fix ships, reporter gets **in-game mail**, all players notified by **Herald** on Discord

### Extended to Players
- Players can submit wishes directly (with more guardrails, reviews, triage)
- Quality-of-life bugs that don't affect game balance are **auto-granted**
- Yegge's vision: by end of 2027, the game becomes like the **Giant's Drink** from *Ender's Game* — building itself around each player as they play

## Key Properties

| Property | Description |
|----------|-------------|
| **Input** | Natural language wishes (bug reports, feature requests) |
| **Processing** | Agent triage → investigation → Beads issue → fleet implementation |
| **Output** | Shipped fix + notification to requester |
| **Human role** | Guardrails and review for risky changes; fully automated for safe QoL fixes |
| **Inspiration** | Guy Podjarny / Tessl (GHI → agent implementation) |

## Significance

The Wish Factory represents a shift from **software factory** (developer-centric CI/CD) to **wish factory** (user-centric autonomous implementation). Key implications:

- **End-user agency**: Non-technical users directly influence software through natural language
- **Reduced friction**: No need for detailed specs, Jira tickets, or developer handoffs
- **Autonomous scope**: Safe to auto-grant low-risk wishes; needs guardrails for balance-affecting changes
- **Scale**: Works best when you have a large surface area of "safe" QoL improvements

## Related

- [[entities/steve-yegge]] — Coined the term, implemented it for Wyvern
- [[concepts/wheelhouse]] — The orchestration harness that enables Wish Factory in Wyvern
- [[entities/beads]] — The issue tracker where wishes become implementation tasks
- [[concepts/land-rush-cicd]] — CI/CD pattern needed to ship at wish-factory speeds
- [[concepts/agentic-engineering]] — Broader engineering discipline
- [[concepts/agent-orchestration]] — Orchestration patterns underlying Wish Factory

## Sources

- https://yegge.ai/essays/the-shape-of-things-to-come/ (Aug 2026, §"The Wish Factory")
