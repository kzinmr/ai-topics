---
title: Tambo
created: 2026-05-11
updated: 2026-08-04
type: entity
status: L3
tags:
  - company
  - open-source
  - tool
  - platform
  - ai-agents
  - mcp
  - developer-tooling
  - web-development
  - generative-ui
aliases: [tambo-ai, tambo.ai, tambo.ai/react]
sources: [https://tambo.co, https://github.com/tambo-ai/tambo, https://docs.tambo.co, https://tambo.co/blog/posts/introducing-tambo-generative-ui]
related: [mcp, vercel, ai-agents, generative-ui, json-render]
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
| GitHub Stars | ~11.2K+ (2026-08), 8,000+ at 1.0 launch |
| License | MIT (SDK); Apache-2.0 (some workspaces e.g. `apps/api`) |
| Stack | React (TypeScript), Zod |
| Investors | The General Partnership, Dan Lewis (Convoy), Drew Houston (Dropbox), Eric Wittman (VSCO) |
| Notable Users | Zapier, Rocket Money, Solink |
| Traction | 500,000+ user messages processed (Feb 2026); SOC 2 + HIPAA compliance at 1.0 |

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
| **Interactable Components** | Persist and update as users refine requests (shopping carts, spreadsheets, task boards) via `withInteractable()` |
| **Streaming Infrastructure** | Progressive props streaming. Auto-handles cancellation, error recovery, reconnection |
| **MCP Support** | Full MCP protocol: tools, prompts, elicitations, and sampling. Connect Linear, Slack, databases, or custom MCP servers |
| **Local Tools** | Client-side tool execution — DOM manipulation, authenticated fetches, React state access from browser functions |
| **Component State** | Agent manages state updates in response to user interaction |
| **User Authentication** | `userKey` (server-side) or `userToken` (OAuth access token) — agent inherits user permissions |
| **Multi-Model** | OpenAI, Anthropic, Gemini, Mistral, Cerebras, OpenAI-compatible providers |
| **Additional Context** | Pass user state, app settings, current page as metadata helpers for better responses |
| **Suggestions** | `useTamboSuggestions()` generates clickable prompt suggestions based on user activity |
| **Component Library** | [ui.tambo.co](https://ui.tambo.co) — Collection of UI primitives for agents |

### Getting Started

```bash
npm create tambo-app my-tambo-app  # auto-initializes git + tambo setup
cd my-tambo-app
npm run dev
```

Templates: [AI Chat with Generative UI](https://github.com/tambo-ai/tambo-template), [AI Analytics Dashboard](https://github.com/tambo-ai/analytics-template).

## Tambo 1.0 (February 2026)

Released as a fullstack, open-source generative UI toolkit — stable for production with **SOC 2 and HIPAA compliance**. Key positioning from the launch post:

> "Most AI interfaces are just chat windows bolted onto existing products. Users try them once and move on. The problem isn't AI, it's that text isn't how people use apps."

The launch noted the industry converging on agents rendering real UI (Anthropic's MCP Apps, Google's A2UI, Vercel's json-render) — "a protocol isn't an implementation," and Tambo positions itself as the drop-in toolkit.

- 8,000+ GitHub stars at launch; 500,000+ user messages processed
- Teams at Zapier, Rocket Money, Solink building generative UI in production
- Quote: "I plugged it into my UI on a Friday and demoed it to my team on Monday." — Jean-Philippe Bergeron, Sr. Fullstack Engineer at Solink

## Pricing

| Plan | Price | Details |
|--------|------|------|
| **Starter** | Free | 10K messages/mo, unlimited users (OAuth), community support |
| **Growth** | $25/mo | 200K messages/mo ($8/100K additional), with analytics and observability |
| **Enterprise** | Annual contract | Negotiable volume, SSO/SAML/SCIM/RBAC, SOC 2/HIPAA/GDPR, 99.99% SLA |

The open-source version is **free and perpetually self-hostable**.

## Generative UI Positioning

Tambo takes a different approach from the Vercel AI SDK. Where Vercel is a general-purpose AI SDK, Tambo specializes in the **Generative UI** paradigm where "AI outputs UI." It uses existing components as-is, providing a layer where the AI decides "which UI to display."

Can be used alongside agent frameworks like LangChain or Mastra, but not required. The agent is included — Tambo runs the LLM conversation loop, streams props, and manages thread state.

### Comparison (from README, 2026-08)

| Feature | Tambo | Vercel AI SDK | CopilotKit | Assistant UI |
|---------|-------|---------------|------------|--------------|
| **Component selection** | AI decides which components to render | Manual tool-to-component mapping | Via agent frameworks (LangGraph) | Chat-focused tool UI |
| **MCP integration** | Built-in (full protocol) | Experimental (v4.2+) | Recently added | Requires AI SDK v5 |
| **Persistent stateful components** | Yes | No | Shared state patterns | No |
| **Client-side tool execution** | Declarative, automatic | Manual via onToolCall | Agent-side only | No |
| **Self-hostable** | MIT (SDK + backend) | Apache 2.0 (SDK only) | MIT | MIT |
| **Hosted option** | Tambo Cloud | No | CopilotKit Cloud | Assistant Cloud |
| **Best for** | Full app UI control | Streaming and tool abstractions | Multi-agent workflows | Chat interfaces |

## Use Cases

- **db-thing** — Conversational DB design. Schema creation → ERD generation → optimization → SQL export
- **Strudel AI** — Live coding music generation. Real-time layering of drums, melody, and synths
- **CheatSheet** — Cheat sheet generation where AI responds with components

## Competitors & Related

- [[entities/vercel]] — General AI SDK (Vercel AI SDK). Also partially covers Generative UI
- [[concepts/mcp]] — Protocol Tambo depends on; its MCP Apps section covers Anthropic's UI-over-MCP standard (ecosystem convergence mentioned in Tambo 1.0 launch)
- [[entities/langchain]] — Can be used alongside as an agent framework
- [[concepts/generative-ui]] — The generative UI paradigm (Claude Visualizer reverse-engineering; complementary angle)
- [[concepts/json-render]] — Vercel's generative UI rendering spec; part of the converging ecosystem

## Creator

Built by **Michael Magán** (CEO, @michaelmagan) and **Michael Milstead** (@MichaelMilstead). Magán is based in Seattle & San Francisco; the pair met at a hackathon and became "obsessed with the idea that the apps we use should adapt to what we're trying to do, not force us to learn their structure." The first version of Tambo was a tiny library that turned React components into tool definitions; it grew into a full toolkit with an agent, React SDK, and component library. Personal site: [magan.info](https://magan.info).
