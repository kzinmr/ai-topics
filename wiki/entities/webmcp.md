---
title: WebMCP
type: entity
aliases:
- web-model-context-protocol
- navigator-modelContext
- w3c-webmcp
created: 2026-04-13
updated: 2026-05-26
tags:
  - entity
  - developer-tooling
  - browser-agent
  - methodology
  - protocol
status: active
sources:
- https://webmcp.link/
- https://developer.chrome.com/blog/webmcp-epp
- https://developer.chrome.com/blog/webmcp-mcp-usage
- https://pub.towardsai.net/webmcp-making-your-web-app-agent-ready-d7d4d9cb790d
- https://docs.mcp-b.ai/explanation/design/spec-status-and-limitations
---

# WebMCP (Web Model Context Protocol)

**WebMCP** is a browser standard being developed by the W3C Web Machine Learning Community Group. Co-designed by Google and Microsoft, it defines the `navigator.modelContext` API for AI agents to structurally interact with web applications. An early preview launched in Chrome 146 in February 2026.

## Overview

| Item | Details |
|---|---|
| Standards Body | W3C Web Machine Learning Community Group |
| Co-developers | Google + Microsoft |
| Spec Status | Draft Community Group Report (February 2026) |
| Implementation | Chrome 146 Canary (flag-enabled) |
| API | `navigator.modelContext` |
| Proposal Date | August 2025 (joint proposal) |

## Core Concept

**"Websites declare what AI agents can do"**

Traditional browser agents (screenshot analysis, DOM scraping) were "guess-based." WebMCP flips the paradigm: **the website explicitly registers structured tools (name, description, JSON Schema input)** that agents can discover and invoke.

### Two API Approaches

1. **Declarative API**: Define standard actions via HTML form attributes
2. **Imperative API**: Execute complex dynamic interactions via JavaScript

```javascript
// Example: Registering a tool
navigator.modelContext.registerTool({
  name: "bookFlight",
  description: "Book a flight",
  inputSchema: {
    type: "object",
    properties: {
      from: { type: "string" },
      to: { type: "string" },
      date: { type: "string" }
    }
  },
  execute: async (params, agent) => {
    // Flight booking logic
    return { success: true, bookingId: "ABC123" };
  }
});
```

## Why WebMCP Matters

| Metric | Value |
|---|---|
| Token Reduction (vs screenshot) | 89% |
| Browser Session Reuse | 100% |
| UI Selector Maintenance | Zero |

### Moving Beyond Screenshot-Based Approaches
- Anthropic Computer Use / OpenAI CUA: **Analyze screen via vision models** → slow, high token consumption
- browser-use / Playwright: **Direct DOM manipulation** → fragile with dynamic UIs
- **WebMCP**: **Sites declare tools** → accurate, fast, easy to maintain

## Timeline

| Date | Milestone |
|---|---|
| January 2025 | MCP-B prototype |
| August 2025 | Google + Microsoft joint proposal |
| September 2025 | Accepted as W3C Community Group Draft |
| October 2025 | Resolved `navigator.modelContext` root naming |
| January 2026 | Dual API strategy (Declarative + Imperative) finalized |
| February 2026 | Early preview in Chrome 146 (`chrome://flags/#enable-webmcp-testing`) |
| March 2026 | Model Context Tool Inspector (Chrome DevTools extension) released |
| March 2026 | Chrome blog "When to use WebMCP and MCP" published |

## WebMCP vs MCP (Anthropic)

| Dimension | MCP (Anthropic) | WebMCP |
|---|---|---|
| Execution Location | Backend server | Inside browser tab |
| Protocol | JSON-RPC | JavaScript API |
| Availability | Always (desktop/mobile/cloud) | Only when browsing websites |
| Target | Data sources, external tools, workflows | UI operations on specific websites |
| Standardization | Industry de facto | W3C Community Group |

### Complementary Relationship
> "WebMCP is not an extension or a replacement of MCP. Instead, WebMCP and MCP address different needs."
> — Chrome Developer Blog, March 2026

## Current Limitations

1. **No Headless Execution**: A browser tab must be open
2. **No Background Execution**: Tool calls blocked when page is hidden
3. **Firefox/Safari**: No public signals
4. **Unstable Spec**: Subject to change as Community Group Draft
5. **100+ Open Issues**: Discovery mechanisms, lifecycle management, etc.

## Ecosystem

- **MCP-B Polyfill**: `@mcp-b/webmcp-polyfill` — Use the standard API across all browsers
- **MCP-B Global Runtime**: `@mcp-b/global` — Production-ready with polyfills
- **Chrome DevTools Extension**: Model Context Tool Inspector
- **Demo App**: GoogleChromeLabs/webmcp-tools
- **TypeScript SDK**: WebMCP-org/chrome-devtools-quickstart

## Related Entities

- [[entities/anthropic-computer-use]] — Screenshot-based approach
- [[entities/openai-cua]] — OpenAI's Computer-Using Agent
- [[entities/browser-use]] — DOM-based automation
- [[concepts/death-of-browser]] — The de-humanization of the browser trend
- [[entities/browserbase]] — Browser infrastructure

## Sources

- [WebMCP Official Site](https://webmcp.link/)
- [WebMCP Early Preview (Chrome Blog)](https://developer.chrome.com/blog/webmcp-epp)
- [When to use WebMCP and MCP (Chrome Blog)](https://developer.chrome.com/blog/webmcp-mcp-usage)
- [W3C WebMCP Specification](https://webmachinelearning.github.io/webmcp)
- [WebMCP: Making Your Web App Agent-Ready (Towards AI)](https://pub.towardsai.net/webmcp-making-your-web-app-agent-ready-d7d4d9cb790d)
- [MCP-B Documentation](https://docs.mcp-b.ai/explanation/design/spec-status-and-limitations)
