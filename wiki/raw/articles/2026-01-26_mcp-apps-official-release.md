---
title: "MCP Apps - Bringing UI Capabilities to MCP Clients (Official Release)"
source: Model Context Protocol Blog
author: MCP Team (Anthropic)
url: https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/
published: 2026-01-26
type: article
tags: [mcp, mcp-apps, protocol, official-release, specification]
---

# MCP Apps: Bringing UI Capabilities to MCP Clients

**Date:** January 26, 2026
**Status:** Live / Official MCP Extension

## Overview

MCP Apps is the **first official extension** for the Model Context Protocol (MCP). It allows tools to return **interactive UI components** (dashboards, forms, visualizations) that render directly within a conversation, moving beyond plain text responses. This standardizes work previously done by MCP-UI and the OpenAI Apps SDK.

## Key Technical Architecture

MCP Apps utilize two primary primitives:

1. **Tools with UI Metadata:** Tools include a `_meta.ui.resourceUri` field pointing to a UI resource.
2. **UI Resources:** Server-side resources served via the `ui://` scheme containing bundled HTML/JavaScript.

### The App API

Developers use the `@modelcontextprotocol/ext-apps` package to manage UI-to-host communication via JSON-RPC over `postMessage`.

```javascript
import { App } from "@modelcontextprotocol/ext-apps";
const app = new App();
await app.connect();

// Receive tool results from the host
app.ontoolresult = (result) => {
  renderChart(result.data);
};

// Call server tools from the UI
const response = await app.callServerTool({
  name: "fetch_details",
  arguments: { id: "123" },
});

// Update model context
await app.updateModelContext({
  content: [{ type: "text", text: "User selected option B" }],
});
```

## Core Use Cases

- **Data Exploration:** Interactive charts with filtering and drill-down capabilities.
- **Configuration Wizards:** Multi-step forms with dependent fields (e.g., staging vs. production settings).
- **Document Review:** Inline PDF viewers where users can click to approve or flag specific clauses.
- **Real-time Monitoring:** Live system health metrics that update without re-running the tool.

## Security Model

Multi-layered security approach:
- **Iframe Sandboxing:** Restricted permissions for all UI content.
- **Pre-declared Templates:** Hosts can review HTML content before rendering.
- **Auditable Messages:** All communication is loggable JSON-RPC.
- **User Consent:** Hosts can require explicit approval before a UI component initiates a tool call.

## Client Support & Availability

| Client | Availability |
|--------|-------------|
| **Claude** | Available (Web & Desktop) |
| **Goose** | Available |
| **VS Code** | Available in VS Code Insiders |
| **ChatGPT** | Rolling out (starting week of Jan 26, 2026) |

## Actionable Resources

- **Official SDK:** [`@modelcontextprotocol/ext-apps`](https://www.npmjs.com/package/@modelcontextprotocol/ext-apps)
- **Documentation:** [MCP Apps Guide](https://modelcontextprotocol.io/docs/extensions/apps)
- **Quickstart:** [Getting Started Guide](https://apps.extensions.modelcontextprotocol.io/api/documents/Quickstart.html)
- **Example Servers:** `threejs-server` (3D), `map-server` (maps), `pdf-server` (documents), `system-monitor-server` (dashboards)

## Key Quote

> "With MCP Apps, that contract finally includes the missing human step: when the workflow needs a decision, a selection, or exploration, the client can give you the right interaction without turning the conversation into a choose-your-own-adventure prompt."
> — **Harald Kirschner**, Principal Product Manager, VS Code
