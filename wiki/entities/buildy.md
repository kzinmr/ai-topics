---
title: Buildy
created: 2026-05-11
updated: 2026-05-11
type: entity
status: L2
tags: [company, platform, tool, ai-agents, mcp, personal-ai, developer-tooling, web-development]
aliases: [buildy.so]
sources: [https://buildy.so, https://buildy.so/llms.txt, https://buildy.so/llms-full.txt]
related: [mcp, codex, claude-code, openclaw, cursor]
---

# Buildy

> Built by your AI. Used by both of you. — A platform where AI agents build and persist personalized web apps for you

Buildy is a runtime platform for AI agents (Claude Code / Codex / Cursor, etc.) to build and deliver **personal web apps**. Simply POST an ES module to get a public URL with persistent storage. Own multiple small apps under one account, accessible from any agent.

**Website**: [buildy.so](https://buildy.so) | **API**: `app.buildy.so` | **Docs for AI**: [llms-full.txt](https://buildy.so/llms-full.txt)

## Core Concept

> **"Built by your AI. Used by both of you."**

Buildy bridges the gap between "AI writing code" and "humans using it." An AI agent writes a web app, Buildy hosts it, and the human accesses it from anywhere — browser, phone, or chat.

## Three Pillars

| Pillar | Description |
|----|------|
| **Persistence** | Real URL + real storage. Close the tab and it's still there tomorrow |
| **Portability** | Build with Codex → use with ChatGPT → update with Claude. One MCP, all agents |
| **A Home** | Manage multiple small apps in one account. Habit trackers, shopping lists, budgets... all here |

## Architecture

```
AI Agent (Claude/Codex/Cursor/...) 
  → ES Module (Workers/WinterTC fetch handler + optional inline UI)
    → POST https://app.buildy.so/app
      → Public URL + KV Storage
        ← User accesses via browser/phone/chat
```

- **Runtime**: Workers/WinterTC-compatible `fetch` handler
- **Storage**: Key-value store (per-app, single-tenant)
- **UI**: Inline HTML/CSS (iframe rendering)
- **Auth**: Device Code Pairing Flow (`/pair/start` → `/pair/poll`) or PAT (Personal Access Token)

## Supported Agents & Clients

### Code Editors (via API)
Cursor, Claude Code, Codex CLI, Cline, Windsurf, Continue, Zed, Gemini CLI

### Chat (via MCP)
Claude Desktop, Claude.ai (Pro), ChatGPT (Plus + Developer Mode), Goose, Perplexity

### Coming Soon
Grok, Gemini (chat)

## Key Features

| Feature | Status | Description |
|------|------|------|
| **Live URLs** | ✅ Live | Real URL for each app. Accessible from browser, phone, shareable |
| **Persistent Storage** | ✅ Live | Data persists. Close the chat and it's still there tomorrow |
| **Multi-Agent** | ✅ Live | One MCP install, works with Claude/ChatGPT/Codex/Cursor |
| **Build Anywhere, Use Anywhere** | ✅ Live | Build with one agent, use with another |
| **Hooks / API** | ✅ Live | POST /api/log, call_app sync, cron digest |
| **Share by Link** | ✅ Live | Share URL → recipient opens with AI, same data |
| **Custom Domains** | 🔜 Planned | Custom domains |
| **Notifications** | 🔜 Planned | Push/Email/SMS |
| **Schedules** | 🔜 Planned | Scheduled execution (cron) |
| **Shared Memory** | 🔜 Planned | Context sharing between apps |
| **Versions** | 🔜 Planned | Undo agent edits, rollback to any point |
| **Activity Log** | 🔜 Planned | Audit log of all reads/writes/executions |
| **Mobile Apps** | 🔜 Planned | iOS/Android native apps |
| **Integrations** | 🔜 Planned | Gmail, Google Calendar, Sheets, Drive, Notion, Linear, GitHub and 24 others |

## Pricing

The first app is **free, no signup required**. Only register an account when you decide "I want to keep this."

## Competitors & Related

- [[replit]] — Full-stack app development with AI Agent. For more serious development
- [[lindy]] — AI App Builder. Full-stack for founders
- [[vercel-v0]] — AI UI generation. Component-level
- [[mcp]] — Protocol Buildy uses for agent connections
- [[claude-code]], [[codex]], [[cursor]] — Coding agents where Buildy operates

## Observations

What makes Buildy interesting is its focus on the **"persist what AI creates"** layer. While Vercel v0 and Replit Agent lean toward "development," Buildy emphasizes "usage." Its comprehensive AI-facing documentation (`llms.txt` / `llms-full.txt`) reflects an AI-first design philosophy.

Use cases include habit trackers, shopping lists, budget management, workout logs — "small personal tools." A product to watch in the Personal AI context rather than enterprise.
