---
title: "MCP-UI Project (→ MCP Apps)"
source: https://mcpui.dev
author: Ido Salomon (@idosal1)
url: https://mcpui.dev/
published: 2025-01-01
updated: 2026-01-26
type: project
tags: [mcp, mcp-apps, mcp-ui, open-source, protocol, ui-components]
---

# MCP-UI → MCP Apps

MCP-UI is an open-source project by **Ido Salomon** (@idosal1) that defines interactive UI components over the Model Context Protocol (MCP). It has been **standardized into MCP Apps** — the official MCP Apps extension is the successor spec, and MCP-UI packages now implement that standard.

**Status:** Merged into official MCP Apps standard ([SEP-1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865))
**License:** Apache 2.0

## SDK Packages

| Language | Package | Registry |
|----------|---------|----------|
| TypeScript/JS | `@mcp-ui/client` | npm |
| TypeScript/JS | `@mcp-ui/server` | npm |
| Ruby | `mcp_ui_server` | RubyGems |
| Python | `mcp-ui-server` | PyPI |

## Key Features

- **Sandboxed Execution:** All remote code runs in sandboxed iframes for security
- **Flexible:** Supports HTML content, works with both MCP Apps hosts and legacy MCP-UI hosts
- **Full Stack Coverage:** Client SDK (`AppRenderer` component) + Server SDK (UI resource utilities)

## Quick Example

**Client Side:** Render tool UIs with `AppRenderer` React component
**Server Side:** Tools declare UI via `_meta.ui.resourceUri` pointing to a `ui://` resource

## Resources

- GitHub: [github.com/idosal/mcp-ui](https://github.com/idosal/mcp-ui)
- Discord: [MCP-UI community](https://discord.gg/CEAG4KW7ZH)
- npm: [@mcp-ui/client](https://www.npmjs.com/package/@mcp-ui/client), [@mcp-ui/server](https://www.npmjs.com/package/@mcp-ui/server)
