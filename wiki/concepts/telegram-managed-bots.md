---
title: Telegram Managed Bots
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [agentic-engineering, platforms, no-code]
aliases: ["Managed Bots", "Telegram Bot API 9.6"]
sources:
  - https://core.telegram.org/bots/api-changelog
  - https://core.telegram.org/bots/features
status: complete
---

# Telegram Managed Bots

A no-code bot creation system introduced in **Bot API 9.6** (April 3, 2026), where existing Telegram bots can create and manage other bots on behalf of users — eliminating the need for coding or BotFather interaction.

## Definition / Core Idea

Telegram Managed Bots allow a "manager bot" to provision, configure, and control subordinate bots through the Bot API. Users interact with the manager bot's UI to spin up specialized bots (AI agents, business bots, games, productivity tools) without writing code.

## Key Features (Bot API 9.6)

- **`can_manage_bots`** field added to `User` class — grants management permissions
- **`KeyboardButtonRequestManagedBot`** and **`request_managed_bot`** — UI element for users to request bot creation
- **`ManagedBotCreated`** and **`ManagedBotUpdated`** — event classes for lifecycle management
- **`getManagedBotToken`** / **`replaceManagedBotToken`** — programmatic token access
- **`savePreparedKeyboardButton`** — allows bots to request users, chats, and managed bots from Mini Apps
- Deep links: `https://t.me/newbot/{manager_bot_username}/{suggested_bot_username}` for one-click bot creation

## Architecture

```
User → Manager Bot (UI) → Bot API → Managed Bot (subordinate)
                                    ↑
                        Token fetched via getManagedBotToken
                        Updates received via ManagedBotUpdated
```

The manager bot acts as an orchestrator layer, receiving user intent through its interface and translating it into Bot API calls for the managed bot.

## Implications

- **Democratization**: Anyone can deploy AI agents and specialized bots without coding skills
- **Ecosystem Growth**: Expected wave of trading alert bots, portfolio trackers, community management tools
- **Risk**: Lower barrier to deployment also means more potential for spam and scam bots
- **Platform Play**: Positions Telegram as a bot infrastructure provider, not just a messaging app

## Connection to Other Concepts

- [[managed-agents]] — Telegram's managed bots are a concrete implementation of the broader managed agent pattern
- [[agentic-engineering]] — no-code agent creation as infrastructure
- [[death-of-browser]] — bots as the new application interface layer

## TODO: Research Items
- [ ] Track adoption metrics and third-party manager bot ecosystems
- [ ] Compare with other no-code agent platforms (Anthropic Managed Agents, etc.)
- [ ] Document security and abuse prevention mechanisms
