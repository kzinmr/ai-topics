# Cloudflare Code Mode MCP — Server-Side Code Execution Pattern

**Source:** https://blog.cloudflare.com/code-mode-mcp/
**Date:** 2026-04-30 (published)

## Summary

Cloudflare introduced **Code Mode** for its Model Context Protocol (MCP) server, collapsing the entire Cloudflare API (2,500+ endpoints) into just two tools: `search()` and `execute()`. This reduces context window usage by **99.9%** (from ~1.17M tokens to ~1,000 tokens).

## Key Innovation

Instead of exporting each API endpoint as a separate MCP tool (traditional approach), Cloudflare's MCP server exports only 2 tools:

1. **`search()`** — Agent writes JavaScript to filter the OpenAPI spec
2. **`execute()`** — Agent writes async JavaScript arrow functions to perform API actions

Code runs in a **Dynamic Worker isolate** (V8 sandbox) with no filesystem access and disabled external fetches by default.

## Context Reduction Comparison

| Approach | Mechanism | Token Cost |
|---|---|---|
| Traditional MCP | Every endpoint = 1 tool | ~1.17M tokens |
| Server-Side Code Mode | search() + execute() | ~1,000 tokens |

## Open Source

Cloudflare released both the [Cloudflare Agents SDK](https://github.com/cloudflare/agents) and the [Code Mode SDK](https://github.com/cloudflare/agents/tree/main/packages/codemode).

## Authentication

OAuth 2.1 compliant with scoped API tokens via Workers OAuth Provider.

## Future: MCP Server Portals

Unified gateway for multiple MCP servers (GitHub, databases, etc.) with fixed token footprint regardless of number of connected services.
