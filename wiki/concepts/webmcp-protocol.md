---
title: WebMCP (Web Model Context Protocol)
created: 2026-08-27
updated: 2026-11-15
type: concept
tags: [mcp, protocol, ai-agents, web-development, browser]
sources:
  - raw/articles/2026-08-04_webmcp-teaching-websites-to-talk-to-ai-agents
  - https://sreenathmenon.com/blog/2026-08-04-webmcp-teaching-websites-to-talk-to-ai-agents/
  - https://news.ycombinator.com/item?id=49450417
  - https://ui-sdk.dev/docs/agents/connect-an-agent/webmcp
related:
  - [[entities/webmcp]]
  - [[concepts/mcp]]
  - [[concepts/death-of-browser]]
  - [[concepts/agent-harnesses]]
---

# WebMCP (Web Model Context Protocol)

## Overview

WebMCP (Web Model Context Protocol) is a proposed web standard that allows websites to expose structured tools and data to AI agents. Developed jointly by Google (Chrome) and Microsoft (Edge) in the W3C Web Machine Learning Community Group, WebMCP brings the MCP (Model Context Protocol) paradigm into the browser: the web page itself becomes a place that offers tools, running in the tab you already have open, with the session you're already logged into.

## Core Shift: From Scraping to Declaring

The traditional approach to agent-web interaction involves screen-scraping: the agent loads a page, reads the raw HTML, tries to figure out which elements do what, and clicks buttons. WebMCP inverts this: instead of the agent guessing what your site can do by staring at it, your site declares what it can do, as a set of clean, structured tools the agent can call directly.

## Key Features

- **Discovery**: A standard way for a page to say "I offer these tools" (checkout, filter_results, book_table), so an agent can list them
- **Schemas**: Each tool declares its inputs and outputs as JSON Schema, so the agent knows exactly what to pass
- **State**: A shared understanding of what's on the page right now, so the agent knows what it can actually act on

## Maturity

WebMCP is a **Community Group draft**, not a finished W3C standard and not yet on the standards track. It's available as a Chrome origin trial. This is exactly why now is the moment to learn it and shape it.

## Technical Implementation

WebMCP provides a small JavaScript API for web pages to register tools that an AI agent can discover and call. The API allows:

1. **Registering tools**: Declare available functions with JSON Schema inputs/outputs
2. **Tool discovery**: Agents can query what tools are available
3. **Tool invocation**: Agents can call declared tools with structured arguments
4. **State awareness**: Agents understand the current page state

## Example Use Cases

- **E-commerce**: Expose checkout, cart, search, and filter tools
- **Documentation**: Expose search and content retrieval tools
- **API access**: Wrap REST APIs as WebMCP tools
- **Booking systems**: Expose availability checking and booking tools

## Relationship to MCP

WebMCP extends MCP (Model Context Protocol) to the web context. While MCP provides a standard way to call tools on a server, WebMCP brings that same idea into the browser. The key difference is that WebMCP tools run in the context of the user's existing session, with their authentication and state.

## Availability

- **Chrome**: Origin trial (available now)
- **Edge**: In development
- **Firefox**: Not yet announced

## Framework adoption: Vercel UI SDK (Nov 2026)

The first shadcn-ecosystem implementation surface landed via the **Vercel UI SDK**, whose agent-integration guide ships a dedicated **WebMCP** page — *"Let the agent built into a browser read and use your components"* (`ui-sdk.dev/docs/agents/connect-an-agent/webmcp`). This is a meaningful maturity signal: WebMCP support is no longer only a Chrome origin-trial API, but something a component library can wire up for you, so a site's **typed React component catalog doubles as its agent tool surface**.

Notably this is the same substrate the UI SDK used for **SPEC-01/HARDWARE** (61 hardware-themed components with haptics/sound, installable from a shadcn registry, released by Vercel's @shuding on Nov 14 2026) — the registry/SDK layer is becoming both the human-facing design system and the agent-facing tool surface. Amplified on X by Vercel's **@ctatedev** (Nov 13, "Interesting") — see [[entities/chris-tate]]. Related direction: [[concepts/agentic-web]], [[concepts/generative-ui]].

## See Also

- [[entities/webmcp]] — WebMCP entity page
- [[concepts/mcp]] — Model Context Protocol (server-side)
- [[concepts/death-of-browser]] — The death of the browser paradigm
- [[concepts/agent-harnesses]] — Agent harness architectures
