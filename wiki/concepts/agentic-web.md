---
title: "Agentic Web — The Web Paradigm Shift from Human-Centric to Agent-Centric"
type: concept
created: 2026-04-22
updated: 2026-04-22
tags: [concept, ai-agents]
status: active
sources:
  - "Richard MacManus — The Agentic Web (Apr 2026)"
  - "https://ricmac.org/2026/04/07/the-agentic-web/"
aliases:
  - agentic-web
  - websites-as-capabilities
  - ax-agent-experience
---

# Agentic Web

> "The web is transitioning from a human-centric read/write platform to an Agentic Web, where AI systems interact with websites on behalf of users."

**Summary:** The trend of websites transitioning from "things humans read" to "runtimes that agents operate." An evolution of Tim Berners-Lee's vision — knowledge being accessed, interpreted, and executed by machines.

## 4 Driving Forces

### 1. Websites Expose Capabilities
- **MCP:** Anthropic Nov 2024, primary way for AI to trigger external actions
- **WebMCP:** Provides MCP tools directly in the browser (requires extension/Chrome Canary, planned for native support)
- **Custom chatbots:** Site-specific AI assistants with vector DBs becoming standard
- **Economic layer:** Information retrieval → transaction execution (bookings, purchases, subscriptions)

### 2. User Interface Transformation
- Early AI: Headless browser + scraping/form filling
- Present/Future: Guided by site owners, embedded in mainstream browsers, enhanced with advanced tools
- **Discovery shift:** Links/search → Natural language prompts
- **SEO evolution:** Traditional SEO → **"AI Retrieval Optimization"** (optimizing for AI selection, citation, and trustworthiness)

### 3. Browsers Evolve into AI Runtimes
- **On-device AI:** SLMs like Gemini Nano enable private, low-latency AI execution within the browser
- **Interaction modes:**
  - `Browsing Mode`: Human-like navigation & UI parsing
  - `Tool Mode`: Direct calls to structured capabilities
- **Trend:** Clear shift from navigation to tool-based interaction

### 4. Developer Platform Adaptation
- Cloudflare, Vercel, Netlify experiencing explosive growth. Vercel offers agent hosting + MCP endpoints via Next.js
- **Standardized agent UI:**
  - MCP-UI (Anthropic integration, used by Shopify)
  - OpenAI Apps SDK & AgentKit
  - MCP Apps (open standard for interactive UI)
  - Google A2UI (agent UI framework)
- **UI as debug layer:** Transaction services may eliminate human UI entirely

## Impact by Role

### Product Teams
- Design for both agents and humans. Expose machine-readable capabilities. Integrate AX (Agent Experience) into UX.

### Publishers
- **Threat:** Declining direct visits, AI mediates content access
- **Opportunity:** Becoming a trusted "source" for AI systems
- **Challenge:** Compensation crisis, new solutions like Really Simple Licensing (RSL) protocol

### Developers
- Build machine-readable systems by default. Think in terms of orchestration, not endpoints.
- Hybrid stack: Browser AI + Cloud inference + MCP + Traditional web infrastructure

## Related Concepts

- [[concepts/browser-agent/death-of-browser]] — The browser paradigm shift
- [[entities/webmcp]] — Native browser MCP standard
- [[entities/anthropic-computer-use]] — Anthropic Computer Use
- [[entities/openai-cua]] — OpenAI CUA
- [[entities/browser-use]] — Open-source browser automation
- [[entities/browserbase]] — Reliable browser automation infrastructure
