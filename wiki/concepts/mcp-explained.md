---
title: "MCP Explained (Runlayer interactive tutorial)"
created: 2026-11-07
updated: 2026-11-07
type: concept
tags:
  - mcp
  - agent-tooling
  - agent-communication
  - tool-use
  - education
aliases: [mcp-explained.com]
sources:
  - raw/articles/mcp-explained.com--mcp-explained-com--1a2e7b07.md
  - https://mcp-explained.com/
  - https://news.ycombinator.com/item?id=50379249
confidence: high
---

# MCP Explained (Runlayer interactive tutorial)

**MCP Explained** (mcp-explained.com) is an interactive, browser-based tutorial on the Model Context Protocol, built by **Runlayer** ("the operating layer for AI"). Frontpaged on HN (Nov 2026, 338 points, 133 comments — id 50379249). It targets the mental model rather than the SDK: lessons on Tools, a "spec time machine" for diffing protocol versions, and a "Break it" sandbox; the reference flow is pinned to **MCP spec 2025-11-25**.

## The framing worth keeping

The landing page compresses MCP into a few sentences that are useful as a canonical definition:

- **Roles**: *Host* = the AI app you use (Claude, Cursor, ChatGPT, an agent); *Server* = a small program exposing tools, data, or prompts; *Model* decides what to use but **never talks to a server directly** — the app calls the server and hands the result back.
- **"Not REST"**: JSON-RPC over stdin/stdout or one HTTP endpoint, and **servers can talk back** (bidirectional).
- **"Not just JSON-RPC"**: JSON-RPC is only the envelope; MCP defines what goes inside it — the methods, **capability negotiation**, transports, and auth.
- A notable pedagogical honesty: the interactive sequence diagram flags harness features that are **not in the spec** ("Nothing new on the wire: client and servers still speak plain `tools/list` and `tools/call`") — a useful discipline when teaching MCP, since many "MCP features" people cite are harness implementation details.

## Position in the wiki's MCP map

The wiki already tracks the protocol itself ([[concepts/mcp]]), the [[concepts/mcp-2026-07-28-spec]] evolution, the ecosystem taxonomy ([[concepts/mcpacific-mcp-ecosystem-taxonomy]]), and tooling ([[concepts/mcporter]], [[concepts/code-execution-with-mcp]]). MCP Explained is the **canonical on-ramp/tutorial artifact** for that cluster — the page to link when explaining MCP from first party-neutral ground, alongside the official spec.

Note: the raw capture is thin (landing page only — lessons are client-rendered), so this page documents the framing rather than lesson contents.

## Related

- [[concepts/mcp]] — the protocol proper
- [[concepts/mcp-2026-07-28-spec]] — the newer spec this tutorial's "spec time machine" spans
- [[concepts/code-execution-with-mcp]] — the code-API alternative framing

## Sources

- [mcp-explained.com](https://mcp-explained.com/) — raw: `raw/articles/mcp-explained.com--mcp-explained-com--1a2e7b07.md`
- [HN discussion](https://news.ycombinator.com/item?id=50379249) (338 pts, verified Nov 7 2026)
