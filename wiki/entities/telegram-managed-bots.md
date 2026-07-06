---
title: Telegram Managed Bots
type: concept
created: 2026-04-27
updated: 2026-04-27
status: L2
sources: [https://core.telegram.org/bots/features#managed-bots, https://core.telegram.org/bots]
tags: []
---

# Telegram Managed Bots

Telegram Bot platform's **Managed Bots** feature is a system where one bot can create, manage, and share other bots. Officially introduced in 2025-2026, it enables hierarchical management and multi-tenancy in the Telegram Bot ecosystem.

## Core Concept

Managed Bots is a feature where a manager bot controls the lifecycle of subordinate bots (managed bots). It becomes available when 'Bot Management Mode' is enabled in Telegram's BotFather.

**Key Features**:
- Manager bot can create, manage, and share new bots
- Share URL format: `https://t.me/newbot/{manager}/{new_username}?name={new_name}`
- Manager accesses each managed bot's token via `getManagedBotToken`
- `managed_bot` update event notifies the manager bot
- Multi-tenant bot infrastructure for organizations, teams, and SaaS providers

## Architecture

```
Manager Bot
    ├── Managed Bot A (token via getManagedBotToken)
    ├── Managed Bot B (token via getManagedBotToken)
    └── Managed Bot C (token via getManagedBotToken)
```

Each managed bot operates as an independent bot, but token management, configuration, and sharing are handled through the manager bot. Everything can be centrally managed via the official Telegram API.

## Use Cases

| Use Case | Description |
|----------|-------------|
| **SaaS Multi-tenant** | Generate and manage individual bots per customer via one manager bot |
| **Organization/team** | Auto-create bots with access permissions per team member |
| **Bot marketplace** | Management and deployment platform for official/third-party bots |
| **White-label bots** | Customize and distribute bots per enterprise brand |

## Related Features
- [[entities/telegram-managed-bots]]

Managed Bots are used in combination with other Telegram Bot platform features:

- **[Bot-to-Bot Communication](bot-to-bot-communication.md)** — Inter-bot communication (with infinite loop prevention requirement)
- **Mini Apps (Web Apps)** — JavaScript-based Telegram UI integration
- **Payments** — Digital transactions using Telegram Stars as currency
- **Web Login** — Lightweight authentication via widget/`login_url`

## Significance

Managed Bots evolved the Telegram Bot platform from a simple chatbot framework into a **multi-tenant bot management platform**. It provides the infrastructure for SaaS companies and organizations to efficiently deploy and manage individualized bots for each customer/team. Especially in integration with AI agent platforms (AI-powered support bots, AI content agents, etc.), managed bots become a critical infrastructure component.

## References

- [Telegram Bot Features — Managed Bots](https://core.telegram.org/bots/features#managed-bots)
- [Telegram Bot Platform Overview](https://core.telegram.org/bots)
- [Telegram Bot API Reference](https://core.telegram.org/bots/api)

## Definition / Core Idea
Telegram Managed Bots allow a "manager bot" to provision, configure, and control subordinate bots through the Bot API. Users interact with the manager bot's UI to spin up specialized bots (AI agents, business bots, games, productivity tools) without writing code.


## Key Features (Bot API 9.6)
- **`can_manage_bots`** field added to `User` class — grants management permissions
- **`KeyboardButtonRequestManagedBot`** and **`request_managed_bot`** — UI element for users to request bot creation
- **`ManagedBotCreated`** and **`ManagedBotUpdated`** — event classes for lifecycle management
- **`getManagedBotToken`** / **`replaceManagedBotToken`** — programmatic token access
- **`savePreparedKeyboardButton`** — allows bots to request users, chats, and managed bots from Mini Apps
- Deep links: `https://t.me/newbot/{manager_bot_username}/{suggested_bot_username}` for one-click bot creation


## Implications
- **Democratization**: Anyone can deploy AI agents and specialized bots without coding skills
- **Ecosystem Growth**: Expected wave of trading alert bots, portfolio trackers, community management tools
- **Risk**: Lower barrier to deployment also means more potential for spam and scam bots
- **Platform Play**: Positions Telegram as a bot infrastructure provider, not just a messaging app


## Connection to Other Concepts
- [[concepts/managed-agents]] — Telegram's managed bots are a concrete implementation of the broader managed agent pattern
- [[concepts/agentic-engineering]] — no-code agent creation as infrastructure
- [[browser-agent/death-of-browser]] — bots as the new application interface layer


## TODO: Research Items- [ ] Track adoption metrics and third-party manager bot ecosystems
- [ ] Compare with other no-code agent platforms (Anthropic Managed Agents, etc.)
- [ ] Document security and abuse prevention mechanisms


## See Also
- [[entities/telegram-managed-bots]]

