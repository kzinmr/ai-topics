---
title: Buildy
created: 2026-05-11
updated: 2026-08-07
type: entity
status: L3
tags: [company, platform, tool, ai-agents, mcp, personal-ai, developer-tooling, web-development]
aliases: [buildy.so]
sources: [https://buildy.so, https://buildy.so/llms.txt, https://buildy.so/llms-full.txt, https://buildy.so/docs]
related: [mcp, codex, claude-code, openclaw, cursor]
---

# Buildy

> **"Software that's finally yours."** — Chat apps disappear; Buildy apps stick around. Ask any AI to build an app; Buildy gives it a real URL and a database — and your AI can use it and update it long after the chat is closed.

Buildy is a runtime platform for AI agents (ChatGPT, Claude, Claude Code, Codex, Cursor, Gemini, Grok, Perplexity, OpenClaw, Goose, and more) to build and deliver **personal web apps**. Simply POST an ES module to get a public URL with persistent storage. Own multiple small apps under one account, accessible from any agent.

**Website**: [buildy.so](https://buildy.so) | **API**: `app.buildy.so` | **Docs for AI**: [llms.txt](https://buildy.so/llms.txt) / [llms-full.txt](https://buildy.so/llms-full.txt)

## Core Concept

> **"Built by your AI. Used by both of you."**

Buildy bridges the gap between "AI writing code" and "humans using it." An AI agent writes a web app, Buildy hosts it, and the human accesses it from anywhere — browser, phone, or chat. The same app appears in three places: a real shareable link, direct AI access, and inline rendering inside MCP Apps-capable chat clients.

## Three Pillars

| Pillar | Description |
|----|------|
| **Persistence** | Real URL + real storage. Close the tab and it's still there tomorrow |
| **Portability** | Build with ChatGPT → use with Claude → update with Codex. One MCP, all agents |
| **A Home** | Manage multiple small apps in one account. Habit trackers, shopping lists, budgets... all here |

## Architecture

```
AI Agent (ChatGPT/Claude/Codex/Cursor/OpenClaw/...) 
  → ES Module (Workers/WinterTC fetch handler + optional inline UI)
    → POST https://app.buildy.so/app
      → Public URL + KV Storage
        ← User accesses via browser/phone/chat
```

- **Runtime**: Workers/WinterTC-compatible `fetch` handler
- **Storage**: Key-value store (per-app, single-tenant)
- **UI**: Inline HTML/CSS (iframe rendering + inline rendering in MCP Apps-capable clients)
- **Auth**: Device Code Pairing Flow (`/pair/start` → `/pair/poll`) or PAT (Personal Access Token)

## Agent-Facing Documentation Surfaces

Buildy maintains an unusually complete AI-facing doc stack (all in markdown):

| Surface | Purpose |
|---------|---------|
| [llms.txt](https://buildy.so/llms.txt) | Umbrella index of every agent-facing surface |
| [docs/llms.txt](https://buildy.so/docs/llms.txt) | Scoped **author surface** — prose/how-to for building apps |
| [api/llms.txt](https://buildy.so/api/llms.txt) | Scoped **contract surface** — machine-readable specs (`openapi.json`, `.well-known/*`, `pricing.md`, `clients.txt`) |
| [start.md](https://buildy.so/start.md) | Entry point: routes by surface (MCP tools vs HTTP API), walks the build flow |
| [build-mcp.md](https://buildy.so/build-mcp.md) / [build-http.md](https://buildy.so/build-http.md) | Per-surface starter guides |
| [open.md](https://buildy.so/open.md) | Entry point for *using* (not building) an existing app |
| [design.md](https://buildy.so/design.md) | Sandbox rules; avoiding the generic-AI-app look |
| [inspo.md](https://buildy.so/inspo.md) | Curated example apps to open/remix |
| [remix.md](https://buildy.so/remix.md) | Fork/remix flow — `get_app_source` / `GET /app/<id>/source`, `set_remixable` |
| [profile.md](https://buildy.so/profile.md) | Handle and sharing tools — `set_handle`, `rename_app`, `set_starter_prompt` |
| [llms-full.txt](https://buildy.so/llms-full.txt) | Full build manual — module shape, capabilities, HTTP API, device-code pairing, worked examples |

## Supported Agents & Clients

### Code Editors (via API)
Cursor, Claude Code, Codex CLI, Cline, Windsurf, Continue, Zed, Gemini CLI

### Chat (via MCP / MCP Apps)
ChatGPT, Claude, Claude.ai, Grok, Perplexity, OpenClaw, Goose

### Coming Soon
(Cross-agent support actively expanding — "Works with ChatGPT, Claude, OpenClaw, and more")

## Key Features

| Feature | Status | Description |
|------|------|------|
| **Live URLs** | ✅ Live | Real URL for each app. Accessible from browser, phone, shareable |
| **Persistent Storage** | ✅ Live | Data persists. Close the chat and it's still there tomorrow |
| **Multi-Agent** | ✅ Live | One MCP install, works with ChatGPT/Claude/Codex/Cursor/OpenClaw |
| **Build Anywhere, Use Anywhere** | ✅ Live | Build with one agent, use with another |
| **Inline MCP Apps Rendering** | ✅ Live | Renders inline inside MCP Apps-capable chat clients |
| **Hooks / API** | ✅ Live | POST /api/log, call_app sync, cron digest |
| **Share by Link** | ✅ Live | Share URL → recipient opens with AI, same data |
| **Remix / Fork** | ✅ Live | `set_remixable` lets any visitor auto-fork the app source |
| **Context-aware builds** | ✅ Live | Agent already knows your context — app arrives with details pre-filled (e.g., budget app seeded from home-remodel chats) |
| **Custom Domains** | 🔜 Planned | Custom domains |
| **Notifications** | 🔜 Planned | Push/Email/SMS |
| **Schedules** | 🔜 Planned | Scheduled execution (cron) |
| **Shared Memory** | 🔜 Planned | Context sharing between apps |
| **Versions** | 🔜 Planned | Undo agent edits, rollback to any point |
| **Activity Log** | 🔜 Planned | Audit log of all reads/writes/executions |
| **Mobile Apps** | 🔜 Planned | iOS/Android native apps |
| **Integrations** | 🔜 Planned | Gmail, Google Calendar, Sheets, Drive, Notion, Linear, GitHub and 24 others |

## Pricing

The first app is **free, no signup required**. Only register an account when you decide "I want to keep this." A **For Work** offering exists for team usage (see buildy.so).

## Competitors & Related

- [[replit]] — Full-stack app development with AI Agent. For more serious development
- [[lindy]] — AI App Builder. Full-stack for founders
- [[vercel-v0]] — AI UI generation. Component-level
- [[concepts/mcp]] — Protocol Buildy uses for agent connections
- [[concepts/claude-code/claude-code]], [[entities/codex]], [[cursor]] — Coding agents where Buildy operates

## Observations

What makes Buildy interesting is its focus on the **"persist what AI creates"** layer. While Vercel v0 and Replit Agent lean toward "development," Buildy emphasizes "usage." Its comprehensive AI-facing documentation (`llms.txt` / `llms-full.txt` / scoped author+contract surfaces) reflects an AI-first design philosophy — the docs are written for agents to read, not just humans.

Use cases include habit trackers, shopping lists, budget management, workout logs, run logs — "small personal tools." A product to watch in the Personal AI context rather than enterprise, with the For Work tier as its enterprise toehold.
