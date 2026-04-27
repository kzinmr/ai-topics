---
title: Telegram Bots
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [platform, tool]
sources: [raw/articles/core.telegram.org--bots-features-managed-bots.md]
---

# Telegram Bots

Telegram bots are programmatic interfaces within the Telegram messaging platform that can process user inputs, generate responses, and integrate with external services. They form a core component of Telegram's developer ecosystem.

## Definition

A Telegram bot is an account operated by software that interacts with users through the Telegram API. Bots can receive and send messages of all types, process commands, display inline content, and run Mini Apps.

## Key Features

### Input Types
- **Text messages:** Direct communication with bots
- **Commands:** `/keyword` format with `/start`, `/help`, `/settings` as global defaults
- **Keyboards:** Reply keyboards (predefined options) and inline keyboards (buttons attached to messages)
- **Files and media:** Documents, images, voice messages, locations, stickers
- **Inline mode:** Type `@username` + query in any chat to interact

### Integration Capabilities
- **Mini Apps (Web Apps):** JavaScript applications running inside Telegram
- **Bots for Business:** Integration with Telegram Business accounts
- **Managed Bots:** Bots that can create/manage other bots
- **Bot-to-Bot Communication:** Inter-bot messaging via shared groups/channels
- **Payments:** Full payment processing with Telegram Stars

### Managed Bot Architecture
The **Managed Bots** feature allows bots to programmatically create and manage other bots:
- Enable "Bot Management Mode" in BotFather
- Share new bots via URL pattern: `https://t.me/newbot/{manager}/{new_username}?name={new_name}`
- Manager receives `managed_bot` update events
- Token management via `getManagedBotToken`

This enables **bot orchestration** patterns where an AI agent can spawn, configure, and manage sub-bots for specialized tasks — relevant to [[agent-swarms]] and multi-agent coordination.

### Bot Management
- **Privacy Mode:** Bots only see commands, service messages, and forwarded messages in groups
- **Local Bot API:** Self-hosted Bot API with unlimited file transfers (2000MB upload)
- **Test Environment:** Separate API endpoint for testing

## AI Relevance

Telegram bots are increasingly used for AI-powered services:
1. **No-code AI bot development** — Telegram allows anyone to create AI bots without programming
2. **Multi-bot orchestration** — Managed bots enable hierarchical agent structures
3. **Agent-to-agent communication** — Bot-to-bot messaging supports coordination patterns
4. **Deployment surface** — Telegram provides a large user base (500M+ Mini Apps) for AI service distribution
5. **Monetization** — Telegram Stars enables AI service monetization

## Related Concepts

- [[agent-swarms]] — Multi-agent coordination (bot-to-bot patterns)
- [[memory-architecture]] — Agent memory in multi-bot systems
- [[claude-code]] — Agentic coding platforms
- [[telegram]] — Parent platform entity

## References

- [Telegram Bot Features](https://core.telegram.org/bots/features)
- [Telegram Bot API Reference](https://core.telegram.org/bots/api)
