---
title: "Mu - Tools for Agents"
created: 2026-08-03
updated: 2026-08-03
type: concept
tags:
  - product
  - tool
  - mcp
  - agent-tooling
  - developer-tools
  - open-source
  - agent-infrastructure
  - go
  - startup
  - cli
  - api
sources:
  - raw/articles/2026-08-03_micro-mu-tools-for-agents.md
---

# Mu - Tools for Agents

## Overview

**Mu** is an open-source MCP server and web application that provides AI agents with access to real-world services and data. Built as a single Go binary, it functions as both a server (`mu --serve`) and a command-line interface. Agents connect via the [[concepts/mcp|Model Context Protocol (MCP)]] to access tools spanning news, web search, email, markets, weather, video, places, images, files, calendars, contacts, and more. It is available as a live service at micro.mu and can be self-hosted under the AGPL-3.0 license.

Mu was announced as a Show HN on August 3, 2026 by Asim Aslam (micro/mu), receiving 50 points on Hacker News. Notably, the project's contributors are described as "one human and four agents," reflecting its agent-first development philosophy.

## How It Works

Mu exposes all its capabilities as MCP tools that any MCP-compatible agent can call. Agents connect via a single endpoint:

```
https://micro.mu/mcp
```

The connection can be scoped to specific services using query parameters:

```
https://micro.mu/mcp?tools=news,web,mail
```

Authentication is via Personal Access Tokens (Bearer). The backend LLM — Claude, Atlas Cloud (DeepSeek), or a local Ollama/OpenAI-compatible endpoint — uses these tools to compose responses, maintain per-user memory, and act on real-world data.

## Tool Categories

Mu organizes its capabilities into 18 service areas:

| Service | Key Tools | Description |
|---|---|---|
| **Agent** | `agent`, `chat` | Compose multi-tool answers |
| **Apps** | `apps_build`, `apps_run`, `apps_edit` | Build and run small web tools |
| **Calendar** | `events_create`, `events_free`, `events_list` | Schedule and check availability |
| **Contacts** | `contacts_find`, `contacts_add`, `contacts_list` | Name-to-address resolution |
| **Files** | `files_put`, `files_get`, `files_list`, `files_share` | File storage with URL access |
| **Faith** | `islam_today`, `islam_prayer`, `islam_qibla`, `quran`, `hadith` | Religious tools |
| **Images** | `images_generate`, `images_search` | Image creation and search |
| **Mail** | `mail_inbox`, `mail_send`, `mail_address` | Real SMTP server with DKIM |
| **Markets** | `markets_list` | Crypto, futures, commodities, currencies |
| **News** | `news_list`, `news_read`, `news_search` | RSS aggregation with full articles |
| **Places** | `places_search`, `places_nearby`, `places_eta` | POI, geocoding, travel time |
| **Storage** | `db_create`, `db_get`, `db_list`, `db_update`, `db_delete` | Per-caller persistent records |
| **Video** | `video_list`, `video_search` | Curated channels, no ads |
| **Wallet** | `wallet_balance` | Credits and USDC top-up |
| **Weather** | `weather_forecast` | Conditions, forecast, pollen |
| **Web** | `web_search`, `web_fetch` | Search and page reading |
| **Writing** | `blog_*`, `social_*`, `stream_*` | Publish, read, discuss |

## Architecture

Mu is a single Go binary with a registry-driven CLI: any tool added to the server automatically becomes a CLI subcommand. It supports authentication via username/password, passkeys (WebAuthn), and Google OAuth. The web app presents a dashboard with cards for each service (headlines, prices, weather, unread mail) with an inline agent that acts on visible content.

Self-hosting is straightforward via a one-line install script, Docker Compose, or building from source. Configuration of feeds, prompts, and LLM providers is done through JSON files and environment variables.

## Relationship to the MCP Ecosystem

Mu is part of the growing ecosystem of MCP servers that bridge AI agents to real-world data and services. It differs from simpler MCP servers in its breadth: rather than providing a single capability (e.g., just web search), Mu bundles 18 service categories into one connection. This positions it as a general-purpose "agent toolkit" rather than a specialized integration.

The project is related to the broader [[concepts/mcp|MCP]] ecosystem and the trend toward [[concepts/infrastructure|agent infrastructure]] standardization. Its CLI-first, single-binary design philosophy aligns with tools like [[concepts/claude-code/claude-code-auto-mode|Claude Code]] in prioritizing developer ergonomics.

## Community Reception

The HN discussion revealed mixed sentiment:

- **Skepticism about MCP**: Some developers questioned the value proposition of MCP servers in general, comparing them unfavorably to simpler tool integration patterns
- **Agent-authored code**: The "one human, four agents" contributor structure generated both amusement and concern about AI-generated code quality
- **Value proposition clarity**: Several commenters noted that the project's marketing copy (some AI-written) made it harder to understand what Mu actually does
- **Faith tools**: The inclusion of Islamic religious tools (prayer times, Quran, hadith) as a first-class service category was noted as unusual and interesting

## Open Questions

- **Adoption trajectory**: Will Mu find a user base beyond the MCP-curious developer community?
- **Sustainability**: How will the hosted service at micro.mu be funded long-term?
- **Scope management**: Can a single project maintain quality across 18+ service integrations?
- **Competition**: How does Mu compare to purpose-built MCP servers for individual services?

## Related Pages

- [[concepts/mcp]] — Model Context Protocol
- [[concepts/infrastructure]] — Agent infrastructure and tooling
- [[concepts/claude-code/claude-code-auto-mode]] — Claude Code agent
- [[concepts/infrastructure]] — Agent tooling landscape
- [[entities/deepseek]] — DeepSeek (Atlas Cloud backend)
