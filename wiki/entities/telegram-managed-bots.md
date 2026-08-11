---
title: Telegram Managed Bots
type: entity
created: 2026-04-27
updated: 2026-08-11
status: L3
sources:
  - https://core.telegram.org/bots/features#managed-bots
  - https://core.telegram.org/bots
  - raw/articles/2026-04-25-telegram-managed-bots.md
  - raw/articles/core.telegram.org--bots-features-managed-bots.md
tags:
  - platform
  - tool
  - multi-tenancy
  - api
  - managed-agents
  - agent-orchestration
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
- [[entities/telegram]] — Parent platform entity
- [[concepts/telegram-bots]] — Telegram Bot platform concept

Managed Bots are used in combination with other Telegram Bot platform features:

- **Bot-to-Bot Communication** — Inter-bot communication (with infinite loop prevention requirement); enables agent-to-agent flows
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


## Official Managed Bot Flow (Telegram Docs)

Telegram's current documentation describes the lifecycle precisely:

1. **Create a manager bot** — Choose an existing bot or create a new one via @BotFather, then enable **"Bot Management Mode"** in BotFather's MiniApp settings.
2. **Share a creation link** — `https://t.me/newbot/{manager_bot_username}/{new_username}?name={new_name}` (e.g. `https://t.me/newbot/ManagerBot/CoolAIAgentBot?name=Cool+AI+Agent`). The user opens the link and sees a pre-filled (but editable) bot creation window.
3. **Receive the lifecycle event** — On confirmation, the manager bot receives a `managed_bot` update with a `ManagedBotUpdated` object containing basic info about the new bot and its creator.
4. **Take over control** — The manager calls `getManagedBotToken` to fetch the new bot's access token, then controls it via the Bot API: send/receive messages, change profile, settings, and more.

A manager bot can be a **third-party bot** the user chooses, not only a bot they own — which enables bot-marketplace and SaaS-reseller business models.

## Security & Abuse Prevention

- **Token custody** — The manager bot holds access tokens for all subordinate bots; `replaceManagedBotToken` allows rotation if a token leaks. Token handling is the central security surface of the multi-tenant model.
- **Spam/scam risk** — Lowering the barrier to bot creation also lowers the cost of deploying spam, phishing, and scam bots at scale; platform abuse controls (rate limits, Privacy Mode, user reporting) are the main mitigations.
- **Bot-to-Bot Communication Mode** — Must be explicitly enabled in @BotFather; without it, bots generally cannot see messages from other bots. When enabled, a bot receives other bots' messages in groups (directly or via `/command@OtherBot` mentions and replies) — powerful for agentic flows, but an expanded attack surface for prompt injection between agents.
- **Privacy Mode** — Limits what bots see in groups (commands, service messages, forwards only), reducing data exposure for managed bots deployed in shared spaces.

## Ecosystem & Adoption

- **Launch signal** — The April 2026 Managed Bots announcement (@telegram) drew **3,362 bookmarks and 1.28M impressions**, indicating strong early interest from the developer ecosystem.
- **Bot API 9.6 surface** — `can_manage_bots` permission field on `User`, `KeyboardButtonRequestManagedBot` / `request_managed_bot` UI elements, `ManagedBotCreated` / `ManagedBotUpdated` event classes, `getManagedBotToken` / `replaceManagedBotToken`, `savePreparedKeyboardButton` (request users/chats/managed bots from Mini Apps), and deep links for one-click creation.
- **Positioning** — Telegram positions Managed Bots as the no-code layer of its bot platform: "anyone can utilize AI bots to easily develop, launch and manage their own bot — with no coding required."

## Comparison: Telegram Managed Bots vs Other Managed-Agent Platforms

| Aspect | Telegram Managed Bots | Anthropic Managed Agents ([[concepts/managed-agents]]) |
|--------|----------------------|--------------------------------------------------------|
| Unit managed | Bots (messaging endpoints) | Agents (model + tools + prompts) |
| Creation UX | No-code link flow (`t.me/newbot/...`) | API/console-driven provisioning |
| User interface | Telegram chat + Mini Apps | Claude apps / API integrations |
| Multi-tenancy | Manager bot per tenant; token delegation | Per-agent access control |
| Distribution | Shareable creation links, bot marketplace | Enterprise deployment |
| Key risk | Token custody, spam amplification | Prompt injection, tool misuse |

Both implement the same underlying pattern — **hierarchical management of subordinate AI systems** — on different substrates (chat bots vs. general agents).

## Graph Structure Query

```
[telegram-managed-bots] ──part-of──→ [entity: telegram]
[telegram-managed-bots] ──relates-to──→ [concept: telegram-bots]
[telegram-managed-bots] ──embodies──→ [concept: managed-agents]
[telegram-managed-bots] ──relates-to──→ [concept: multi-agents/agent-swarms]
[telegram-managed-bots] ──relates-to──→ [concept: agentic-engineering]
[telegram-managed-bots] ──contrasts──→ [concept: managed-agents]
```

> This section informs graph queries: Telegram Managed Bots is a feature of [[entities/telegram]], documented under [[concepts/telegram-bots]], and is a concrete embodiment of the broader [[concepts/managed-agents]] pattern — while contrasting with Anthropic's agent-native implementation of the same pattern.

## Connection to Other Concepts
- [[concepts/managed-agents]] — Telegram's managed bots are a concrete implementation of the broader managed agent pattern
- [[concepts/agentic-engineering]] — no-code agent creation as infrastructure
- [[concepts/browser-agent/death-of-browser]] — bots as the new application interface layer
- [[concepts/multi-agents/agent-swarms]] — bot-to-bot communication enables swarm-style coordination on Telegram
- [[concepts/human-in-the-loop]] — escalation and human review of managed-bot actions

## See Also
- [[entities/telegram]] — Parent platform entity
- [[concepts/telegram-bots]] — Telegram Bot platform concept
- [[concepts/managed-agents]] — Anthropic's managed agent platform

