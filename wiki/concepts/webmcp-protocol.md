---
title: WebMCP (Web Model Context Protocol)
created: 2026-08-27
updated: 2026-08-27
type: concept
tags: [mcp, protocol, ai-agents, web-development, browser]
sources:
  - raw/articles/2026-08-04_webmcp-teaching-websites-to-talk-to-ai-agents
  - https://sreenathmenon.com/blog/2026-08-04-webmcp-teaching-websites-to-talk-to-ai-agents/
  - https://news.ycombinator.com/item?id=49450417
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

## See Also

- [[entities/webmcp]] — WebMCP entity page
- [[concepts/mcp]] — Model Context Protocol (server-side)
- [[concepts/death-of-browser]] — The death of the browser paradigm
- [[concepts/agent-harnesses]] — Agent harness architectures
