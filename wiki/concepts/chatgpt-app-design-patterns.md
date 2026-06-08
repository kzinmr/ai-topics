---
title: "ChatGPT App Design Patterns"
type: concept
created: 2026-06-02
updated: 2026-06-02
tags:
  - openai
  - methodology
  - tool
  - developer-tooling
  - frontend
  - streaming
  - developer-experience
  - ai-agents
  - product-management
sources:
  - raw/articles/2025-11-24_openai-developers-blog_what-makes-a-great-chatgpt-app.md
  - raw/articles/2026-02-04_openai-developers-blog_15-lessons-building-chatgpt-apps.md
  - raw/articles/2026-03-21_openai-developers-blog_designing-delightful-frontends-with-gpt-5-4.md
related:
  - concepts/openai-responses-api
  - concepts/openai-agents-sdk
  - entities/openai
status: active
---

# ChatGPT App Design Patterns

## Overview

ChatGPT Apps are interactive experiences that run inside ChatGPT conversations, built with the Apps SDK and backed by [[concepts/openai-agents-sdk|MCP servers]]. Unlike traditional apps where users navigate to your product, ChatGPT Apps are **capabilities the model can call** -- they surface inside ongoing conversations as one of several tools the model orchestrates.

A ChatGPT app is best understood as a set of well-defined tools that perform tasks, trigger interactions, or access data. The "unit of value" is not your full product but the specific capabilities you offer at the right moment in conversation. This paradigm shift from "we own the screen" to "we are a capability the model calls" drives all design decisions.

## The Three Value Dimensions

Every ChatGPT app should clearly deliver on at least one of:

1. **Know** -- Provide new context or data unavailable in ChatGPT (live prices, internal metrics, user-specific data, sensor streams)
2. **Do** -- Take real actions on the user's behalf (create records, send messages, schedule bookings, trigger workflows)
3. **Show** -- Present information in structured, actionable UIs that plain text cannot match (comparisons, tables, charts, visual game state)

If an app doesn't move the needle on at least one dimension, it adds little value beyond what users can already do in ChatGPT.

## Design Principles

### Select Capabilities, Don't Port Your Product

- List core **jobs-to-be-done**, not feature checklists
- For each job, ask: "Without an app, what can't the user do in a ChatGPT conversation?"
- Turn gaps into a handful of clearly named operations (e.g., `search_properties`, `create_support_ticket`)
- Operations should be concrete enough for the model to choose confidently and simple enough to chain with other tools

### Design for Conversation and Discovery

- **Vague intent**: Use existing context, ask 1-2 clarifying questions max, produce something concrete quickly
- **Specific intent**: Parse the query, call the right capabilities, return focused structured results -- don't ask users to repeat themselves
- **No brand awareness**: Explain your app's role in one line, deliver useful output immediately, offer a clear next step

### Build for the Model as Well as the User

You design for two audiences: the human in the chat and the model runtime that decides when to call your app. Key practices:

- **Clear, descriptive actions and parameters** -- Use straightforward names (`search_jobs`, `get_rate_quote`); ambiguity is a tax on routing
- **Privacy by design** -- Only require fields you truly need; avoid "blob" params
- **Predictable, structured outputs** -- Stable schemas with IDs and clear field names; pair a brief summary with machine-friendly data
- **Ecosystem fit** -- Keep actions small and focused; make outputs easy to pass to other apps; avoid long tunnel-like flows

## 15 Practical Lessons (Alpic / Skybridge)

From production experience building two dozen ChatGPT Apps across travel, retail, and SaaS:

### Context Management

1. **Not all context should be shared** -- Different parts need intentionally different views of state. Use `structuredContent` for the model and widget; use `_meta` for widget-only data (e.g., secret words in games)
2. **Lazy-loading doesn't translate well** -- Tool calls have latency overhead. Front-load data into the initial tool response; hydrate widgets via `window.openai.toolOutput`
3. **The model needs visibility** -- When users interact with widgets, the model must know what they're looking at. Use `window.openai.setWidgetState(state)` or declarative `data-llm` attributes on components
4. **Different interactions require different APIs** -- Widget-to-server, widget-to-model, and model-to-server paths serve different purposes; be intentional about which mechanism handles what

### UI Design

5. **Three display modes** -- Apps render **inline** (quick interactions), **fullscreen** (complex widgets like maps), or **picture-in-picture** (stays on top during follow-ups). Design for all three
6. **UI consistency matters** -- Use the OpenAI Apps SDK UI Kit (Tailwind CSS) for native-feeling components
7. **Language-first filtering** -- Replace sidebar checkboxes with natural language. Provide the model a List of Values (LOV) for tool parameters so it can map "sunny" directly to `weather="sunny"`
8. **Files unlock richer interactions** -- Let files flow through both sides: tools consume uploads via `openai/fileParams`; widgets use `window.openai.uploadFile` and `getFileDownloadUrl`

### Production Readiness

9. **CSPs are the new CORS** -- Apps run in a double-nested iframe. Declare `connectDomains`, `resourceDomains`, `frameDomains`, and `redirectDomains` carefully in the manifest
10. **Small widget flags have outsized impact** -- `widgetDomain`, tool annotations (`readOnly`, `destructiveHint`, `openWorldHint`), and `widgetAccessible` define critical boundaries
11. **Hot reload is essential** -- Build a Vite plugin to intercept MCP resource requests and inject real-time updates into the ChatGPT iframe
12. **Not every test belongs in ChatGPT** -- Use a local emulator for React state and layout iteration; reserve real ChatGPT tests for model interaction validation
13. **Mobile testing requires explicit support** -- Tunnel local servers with domain forwarding for iOS/Android testing
14. **React hooks speed up frontend work** -- Abstract low-level SDK APIs into hooks like `useCallTool`, `useWidgetState`, `useLocale`; use Zustand for complex state
15. **Encode lessons into reusable tooling** -- Frameworks like Skybridge and Codex Skills capture patterns so teams don't rediscover them

## Frontend Design with GPT-5.4

GPT-5.4 brings stronger image understanding, more functionally complete apps, and native computer use (Playwright integration for self-verification). Key techniques for high-quality frontends:

### Prompt Engineering for UI

- **Define design system upfront** -- Specify typography, color palette, layout constraints (e.g., two typefaces max, one accent color)
- **Provide visual references** -- Attach screenshots or mood boards to guide layout rhythm, spacing, and imagery treatment
- **Structure as narrative** -- Hero (identity/promise) → Supporting imagery → Product detail → Social proof → Final CTA
- **Dial back reasoning** -- Low/medium reasoning levels often produce stronger frontend results; the model stays fast and focused

### Design Rules (Frontend Skill)

- **One composition** per viewport, not a dashboard (unless it is one)
- **Brand first** -- Brand name must be a hero-level signal, not just nav text
- **Full-bleed hero** -- Edge-to-edge dominant visual, no inset images or rounded cards
- **No cards by default** -- Use sections, columns, lists, and media blocks; cards only when they are the interaction
- **Expressive typography** -- Avoid default stacks (Inter, Roboto, Arial)
- **Motion with purpose** -- At least 2-3 intentional motions (entrance sequence, scroll effect, hover reveal)

### Canvas and Generative UI

GPT-5.4 can generate production-ready frontends incorporating subtle interactions, well-crafted animations, and beautiful imagery. With Playwright integration, the model can iteratively inspect rendered pages, test multiple viewports, navigate application flows, and detect issues -- enabling longer, more autonomous development workflows.

## Related Pages

- [[concepts/openai-responses-api]] -- API foundation for ChatGPT App tool calls and state management
- [[concepts/openai-agents-sdk]] -- Agent framework with sandbox execution for app backends
- [[entities/openai]] -- Platform provider; ChatGPT Apps SDK and App Directory launched May 2026
