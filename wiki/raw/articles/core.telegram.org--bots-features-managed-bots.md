# Telegram Bot Features — Comprehensive Documentation

**Source:** https://core.telegram.org/bots/features
**Accessed:** 2026-04-26
**Type:** Platform documentation / technical reference

## Overview

This page describes individual bot elements and features in detail for the Telegram Bot platform. Telegram bots are a core feature of the Telegram ecosystem, supporting text, files, locations, stickers, voice messages, dice, commands, keyboards, inline requests, deep linking, Mini Apps (Web Apps), payments, bot-to-bot communication, and managed bots.

## Key Features

### Inputs & Interfaces
- Bots accept all Telegram media types (text, files, locations, stickers, voice, dice)
- **Commands:** `/keyword` format (max 32 chars, Latin/numbers/underscores), highlighted in chat with `/` suggestion. Global commands include `/start`, `/help`, `/settings`.
- **Keyboards:** `ReplyKeyboardMarkup` for predefined options; `InlineKeyboardMarkup` for buttons attached to messages with callback, URL, switch-to-inline, game, and payment actions
- **Menu Button:** Appears near message field, shows commands or launches Web Apps, localizable per user/group
- **Web Apps:** JavaScript-based custom interfaces for full flexibility

### Interactions
- **Inline Mode:** `@username` + keyword queryable in any chat
- **Deep Linking:** Parameters via `https://t.me/<bot_username>?start=<param>` (max 64 chars, base64url recommended)
- **Chat/User Selection:** `KeyboardButtonRequestChat` / `KeyboardButtonRequestUser` for user-shared chat/user data

### Integration
- **Mini Apps:** Replace websites with seamless Telegram UI integration, featured in Mini App Store (500M+ monthly users)
- **Bots for Business:** Connect to Telegram Business accounts, uses `business_connection_id`
- **Managed Bots:** Bots can create/manage other bots via "Bot Management Mode" in BotFather
- **Bot-to-Bot Communication:** Bots can interact with each other (with loop prevention requirements)
- **Payments:** Full payment flow with Telegram Stars as primary currency for digital transactions
- **Web Login:** Lightweight authentication framework via widgets or `login_url` inline buttons

### Monetization
- **Telegram Stars:** Primary currency for digital transactions (via in-app purchases or `@PremiumBot`)
- Revenue streams: digital products, paid media, multi-tier subscriptions, 50% ad revenue sharing
- Digital goods must use Telegram Stars (compliance with third-party store policies)

### Bot Management
- **Privacy Mode:** Bots only see commands, service messages, and forwarded messages in groups
- **Local Bot API:** Unlimited file download, 2000MB upload, any port for webhook
- **Status Alerts:** Monitoring for bot health

## Managed Bots (Detailed)

Managed bots allow one bot to create, manage, and share other bots:
- Enable via BotFather "Bot Management Mode"
- Sharing URL: `https://t.me/newbot/{manager}/{new_username}?name={new_name}`
- Manager receives `managed_bot` update
- Uses `getManagedBotToken` to access managed bot tokens

## Bot-to-Bot Communication

Bots can communicate with each other via shared groups or channels. Important: bots must handle infinite loops from other bots responding instantly and continuously, or face platform restrictions.

## Test Environment

Test API endpoint: `https://api.telegram.org/bot<token>/test/METHOD_NAME`

## Key Links

- General Bot Platform Overview: https://core.telegram.org/bots
- Full API Reference: https://core.telegram.org/bots/api
- BotFather documentation: https://core.telegram.org/bots#botfather
