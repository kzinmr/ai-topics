---
title: "folk"
created: 2026-05-11
updated: 2026-05-11
type: entity
tags:
  - ai-agents
  - personal-ai
  - tool
  - platform
  - memory-systems
  - ai-native
sources:
  - raw/articles/2026-05-11_getfolk_folk-app.md
aliases: ["folk app", "getfolk", "folk AI"]
related:
  - concepts/personal-ai
  - concepts/agent-memory
  - concepts/ai-agents
---

# folk

folk is a personal AI agent that lives in your messaging apps (iMessage, Telegram, Discord — Signal coming soon) and runs tasks autonomously. Built by [Nozomio Labs](https://www.nozomio.com/), it positions itself as an always-on AI teammate that remembers context across conversations and takes action on the user's behalf.

| | |
|---|---|
| **Website** | [getfolk.app](https://www.getfolk.app/) |
| **Company** | Nozomio Labs |
| **X/Twitter** | [@nozomioai](https://x.com/nozomioai) |
| **GitHub** | [github.com/nozomio-labs](https://github.com/nozomio-labs) |
| **Platforms** | iMessage, Telegram, Discord, Signal (soon) |
| **Pricing** | Pro: $20/mo (standard models), Max: $100/mo (heavier models) |
| **Launch** | 2026 (60,942+ messages sent) |

## Overview

folk is an "AI teammate wherever you chat" — a persistent agent that lives in messaging apps, watching for tasks and taking action. Unlike session-based chat agents, folk runs 24/7 on its own cloud machine, remembers everything about the user, and can access external tools (calendar, GitHub, bank, Polymarket, etc.).

## Core Features

### Always-On Agent

folk runs on a private cloud machine 24/7, with full access to any tools the user connects. Users ask for things in chat, and folk figures out the rest — it doesn't wait for the next message to continue working.

### Persistent Memory

folk maintains a private, encrypted graph of everything it learns about the user — every message, task, and preference. It's described as "linked like a wiki" that grows over time, providing months of context that lets folk pick up where it left off. Users can browse, edit, or delete anything at any time.

### Multi-Platform

Works inside existing messaging apps:
- iMessage
- Telegram
- Discord
- Signal (coming soon)

### Tool Integration

Can access external services including:
- Calendar (booking, scheduling)
- GitHub (repo management)
- Banking (balance, transactions)
- Polymarket (prediction markets)
- Web browsing
- Code execution

## Use Cases (from testimonials)

| Use Case | Description |
|----------|-------------|
| **Date night planning** | Picked restaurant, handled booking, planned schedule, texted updates throughout |
| **Apartment hunting** | Set up constant alerts across Zillow, FB Marketplace, Redfin — user was first to tour and landed the apartment |
| **Task management** | Flight watching, restaurant booking, text drafting, preference memory |

## Pricing

| Plan | Price | Models |
|------|-------|--------|
| Pro | $20/mo | Standard models |
| Max | $100/mo | Heavier models |

Both plans include: unlimited messages & tasks, always-on cloud machine, persistent memory, browsing & code execution, private MCP server. 3-day free trial, no card required to start.

## Architecture Notes

- Runs on own private cloud machine (not shared infrastructure)
- Memory is a private graph, encrypted at rest, end-to-end
- Provides its own MCP server for tool integration
- Built on Vercel (per footer)

## Market Position

folk occupies the "personal AI agent in chat" niche, competing with:
- General-purpose chatbots (ChatGPT, Claude) — differentiated by persistence and proactive behavior
- Task-specific agents (booking bots, etc.) — differentiated by generality and memory
- Other personal AI platforms — differentiated by messaging-native design rather than web/app interface

The product emphasizes "it lives in your texts" as the key UX insight — meeting users where they already are rather than requiring a new app or interface.

## References

- [folk website](https://www.getfolk.app/)
- [Nozomio Labs](https://www.nozomio.com/)

## See Also

- [[concepts/personal-ai]] — Personal AI assistants
- [[concepts/agent-memory]] — Persistent memory in AI agents
- [[concepts/ai-agents]] — AI agent systems
- [[concepts/memory-systems]] — Memory architectures for AI
