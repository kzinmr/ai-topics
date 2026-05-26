---
title: "MCP (Model Context Protocol)"
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - concept
  - mcp
  - protocol
  - anthropic
  - tool
  - open-source
aliases: [Model Context Protocol]
sources: ["https://www.anthropic.com/news/model-context-protocol", "https://www.youtube.com/watch?v=0NHCyq8bBcM", "https://www.latent.space/p/mcp", "[[raw/articles/2025-06-10_rlancemartin_state-of-ai-agents-aie-2025]]"]
---


# MCP (Model Context Protocol)

**MCP (Model Context Protocol)** is an **open standard protocol** open-sourced by Anthropic in November 2024, enabling LLMs to communicate with external tools and data sources. It solves the "M×N integration problem" between AI applications and external services.

## Overview

| Item | Detail |
|------|------|
| **Announced** | November 25, 2024 |
| **Developers** | David Soria Parra, Justin Spahr-Summers (Anthropic) |
| **Design Inspiration** | Microsoft's Language Server Protocol (LSP) |
| **Transport** | JSON-RPC 2.0 (stdio, HTTP+SSE, Streamable HTTP) |
| **License** | MIT (open source) |

## The Three Primitives

| Primitive | Control | Description |
|-------------|--------|------|
| **Tools** | Model-controlled | External functions called by the LLM (search, computation, API calls) |
| **Resources** | Application-controlled | Structured data streams (file contents, DB records) |
| **Prompts** | User-controlled | Reusable instruction templates |

## Practical Origins

MCP was born not from abstract architectural design, but from the **convergence of two practical crises** inside Anthropic.

### Personal Frustration (David Soria Parra)

In mid-2024, David Soria Parra joined Anthropic with a mission to "accelerate Anthropic's internal development using Claude." The daily problem he faced:

> Constantly **copy-pasting** between Claude Desktop (powerful features but no file access) and the IDE (file access but no Claude features).

His question: "What does it take for applications to let users build their own integrations?"

Together with Justin Spahr-Summers, they prototyped a protocol modeled on LSP in **about 6 weeks**. The first public implementation appeared in the Zed editor. At an internal hackathon, a demo of an **MCP server controlling a 3D printer** became a talking point. Open-sourced on November 25, 2024.

### Organization-Level Integration Chaos (John Welsh)

The internal reality as described by John Welsh (Anthropic MTS) at AI Engineer World's Fair 2025:

- **Late 2023 to early 2024**: LLM tool calling reached practical usability
- Teams across Anthropic started **building integrations chaotically** (Google Drive, maps, messaging systems, etc.)
- Each team implemented custom endpoints (`/call-tool`, `/get-context`) independently
- **Duplicate functionality, incompatible interfaces, unreusable code** — Welsh calls this "**integration chaos**"
- Porting an integration working for one service to another took **weeks**

Remarkably, many of these custom endpoints had **independently converged on patterns similar to MCP** (tool discovery, resource acquisition, etc.) — evidence that the protocol design was a natural convergence point.

### MCP Gateway — "Pit of Success"

Anthropic adopted MCP as an internal standard and built the **MCP Gateway**:
- Centralized OAuth authentication management
- Rate limiting
- Observability
- Design philosophy: "Make the right way the easiest way"

> *"It's not a competitive advantage to be good at plumbing integrations."* — John Welsh

## The "M×N Problem" MCP Solved

Before MCP: M AI applications × N external services required custom integrations for every combination.

| Before MCP | After MCP |
|------------|-----------|
| M × N custom implementations | M + N standardized connections |
| OpenAI Function Calling, Google Extensions, LangChain Tools — all vendor-specific | Single protocol for all vendors |
| Custom implementation per new data source | Just write one MCP server |

## Industry Timeline

| Date | Event |
|------|----------|
| Jun 2023 | OpenAI Function Calling announced |
| 2023-2024 | Google Extensions, LangChain Tools proliferate |
| ~Jul 2024 | David Soria Parra begins developing MCP concept |
| Sep 2024 | First public MCP implementation in Zed editor |
| Nov 25, 2024 | Anthropic open-sources MCP |
| Jun 2025 | Full MCP track held at AI Engineer World's Fair 2025 |

## Key Sources

- [John Welsh: "What we learned from shipping remote MCP support at Anthropic" (AIEWF 2025)](https://www.youtube.com/watch?v=0NHCyq8bBcM)
- [Theo Chu: "MCP: Origins and Requests For Startups" (AIEWF 2025)](https://www.youtube.com/watch?v=x-8pBqWiTzk)
- [Introducing the Model Context Protocol — Anthropic Blog](https://www.anthropic.com/news/model-context-protocol)
- [Latent.Space: The Creators of Model Context Protocol (podcast with David & Justin)](https://www.latent.space/p/mcp)
- [a16z Podcast: MCP Co-Creator on the Next Wave of LLM Innovation](https://a16z.com/podcast/mcp-co-creator-on-the-next-wave-of-llm-innovation/)
- [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25)
