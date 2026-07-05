---
title: Tambo
created: 2026-05-11
updated: 2026-05-11
type: entity
status: L2
tags:
  - company
  - open-source
  - tool
  - platform
  - ai-agents
  - mcp
  - developer-tooling
  - web-development
aliases: [tambo-ai, tambo.ai, tambo.ai/react]
sources: [https://tambo.co, https://github.com/tambo-ai/tambo, https://docs.tambo.co]
related: [mcp, vercel-ai-sdk, ai-agents]
---

# Tambo

> Build agents that speak your UI — Open-source **Generative UI** toolkit for React

Tambo is an open-source toolkit for embedding AI agents into React applications. Simply register existing React components with Zod schemas, and the agent selects and renders the appropriate component based on user utterances. For example, "Show me sales by region" → `<Chart>`, "Add a task" → `<TaskBoard>`.

**GitHub**: [tambo-ai/tambo](https://github.com/tambo-ai/tambo) | **NPM**: `@tambo-ai/react` | **Website**: [tambo.co](https://tambo.co)

## Key Facts

| Item | Detail |
|------|--------|
| Founded | 2024, Seattle, WA |
| Co-founders | Michael Magán (CEO), Michael Milstead |
| GitHub Stars | ~2.5K+ (2026-05) |
| License | MIT |
| Stack | React (TypeScript), Zod |
| Investors | The General Partnership, Dan Lewis (Convoy), Drew Houston (Dropbox), Eric Wittman (VSCO) |
| Notable Users | Zapier, Rocket Money, Solink |

## Architecture

Tambo has a full-stack architecture, providing a React SDK + backend (conversation state management and agent execution).

```
User utterance → Tambo Agent (LLM) → Component selection + Props streaming → UI rendering
```

**3-layer architecture**:
1. **React SDK** (`@tambo-ai/react`) — `<TamboProvider>`, thread management, streaming, hooks for component rendering
2. **Built-in Agent** — LLM conversation loop. No external framework required. Supports OpenAI / Anthropic / Gemini / Mistral / OpenAI-compatible APIs
3. **Backend** — Tambo Cloud (hosted) or Docker self-host

## Key Features

| Feature | Description |
|------|------|
| **Generative Components** | Converts Zod schemas to LLM tool definitions; agents select components like function calls |
| **Streaming Infrastructure** | Progressive props streaming. Auto-handles cancellation, error recovery, reconnection |
| **MCP Support** | Connects to DBs, APIs, and external systems via Model Context Protocol |
| **Component State** | Agent manages state updates in response to user interaction |
| **User Authentication** | Agent inherits user permissions, keeping AI capabilities secure |
| **Multi-Model** | Supports OpenAI, Anthropic, Gemini, Mistral, OpenAI-compatible providers |
| **Component Library** | [ui.tambo.co](https://ui.tambo.co) — Collection of UI primitives for agents |

## Pricing

| Plan | Price | Details |
|--------|------|------|
| **Starter** | Free | 10K messages/mo, unlimited users (OAuth), community support |
| **Growth** | $25/mo | 200K messages/mo ($8/100K additional), with analytics and observability |
| **Enterprise** | Annual contract | Negotiable volume, SSO/SAML/SCIM/RBAC, SOC 2/HIPAA/GDPR, 99.99% SLA |

The open-source version is **free and perpetually self-hostable**.

## Generative UI Positioning

Tambo takes a different approach from the Vercel AI SDK. Where Vercel is a general-purpose AI SDK, Tambo specializes in the **Generative UI** paradigm where "AI outputs UI." It uses existing components as-is, providing a layer where the AI decides "which UI to display."

Can be used alongside agent frameworks like LangChain or Mastra, but not required.

## Use Cases

- **db-thing** — Conversational DB design. Schema creation → ERD generation → optimization → SQL export
- **Strudel AI** — Live coding music generation. Real-time layering of drums, melody, and synths
- **CheatSheet** — Cheat sheet generation where AI responds with components

## Competitors & Related

- [[vercel-ai-sdk]] — General AI SDK. Also partially covers Generative UI
- [[concepts/mcp]] — Protocol that Tambo depends on
- [[entities/langchain]] — Can be used alongside as an agent framework
