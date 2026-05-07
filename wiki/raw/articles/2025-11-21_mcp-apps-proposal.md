---
title: "MCP Apps: Extending Servers with Interactive User Interfaces (Proposal)"
source: Model Context Protocol Blog
author: MCP-UI Community Working Group (Anthropic, OpenAI)
url: https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/
published: 2025-11-21
type: article
tags: [mcp, mcp-apps, protocol, proposal, sep, specification]
---

# MCP Apps: Extending Servers with Interactive User Interfaces

**Date:** November 21, 2025
**Key Proposal:** [SEP-1865 (MCP Apps Extension)](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865)
**Collaborators:** Anthropic, OpenAI, and the MCP-UI Community Working Group.

## 1. Overview: The Shift to Agentic Apps

The MCP Apps Extension standardizes how MCP servers deliver interactive user interfaces (UIs) to host applications. Previously, MCP was limited to text and structured data (JSON), forcing host applications to build custom rendering logic for specialized data.

### Key Benefits:
- **Reduced Client Burden:** Servers provide the UI, so clients don't have to build custom renderers for every data type.
- **Complex Input:** Enables gathering multiple related settings or complex user inputs through visual forms rather than awkward text prompts.
- **Standardization:** Prevents ecosystem fragmentation by unifying patterns from MCP-UI and the OpenAI Apps SDK.

## 2. Technical Specification Highlights

### Pre-declared Resources
UI templates use the `ui://` URI scheme. This allows hosts to prefetch and review templates before execution, improving security and performance.

**Example: Registering a UI Resource and Linking to a Tool**
```json
// Server registers UI resource
{
  "uri": "ui://charts/bar-chart",
  "name": "Bar Chart Viewer",
  "mimeType": "text/html+mcp"
}

// Tool references it in metadata
{
  "name": "visualize_data_as_bar_chart",
  "description": "Plots some data as a bar chart",
  "inputSchema": { ... },
  "_meta": {
    "ui/resourceUri": "ui://charts/bar-chart"
  }
}
```

### Communication & Rendering
- **Transport:** Uses existing MCP JSON-RPC protocol over `postMessage`. UI developers can use the standard `@modelcontextprotocol/sdk`.
- **Initial Format:** Supports `text/html` rendered in sandboxed **iframes**.
- **Deferred Features:** External URLs, remote DOM, and native widgets are planned for future iterations.

## 3. Security & Compatibility

### Security-First Design
1. **Iframe Sandboxing:** Restricted permissions for all UI content.
2. **Auditable Messages:** All UI-to-host communication is loggable and structured.
3. **User Consent:** Hosts can require explicit approval for any tool calls initiated by the UI.

### Backward Compatibility
- **Optional Extension:** Existing MCP implementations do not need to change.
- **Text Fallbacks:** Servers are encouraged to provide text-only fallbacks so they remain functional on hosts that do not support the UI extension.

## 4. Actionable Information for Developers

- **Review the Spec:** [SEP-1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865)
- **Early Access SDK:** [github.com/modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps)
- **Community:** `#mcp-ui` channel in the MCP Contributors Discord

> "The MCP Apps Extension is starting to look like an agentic app runtime: a foundation for novel interactions between AI models, users, and applications."
