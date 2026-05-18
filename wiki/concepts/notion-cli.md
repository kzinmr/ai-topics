---
title: "Notion CLI (ntn)"
created: 2026-05-14
updated: 2026-05-14
type: concept
status: L2
tags:
  - developer-tooling
  - tool
  - mcp
  - notion-mcp
  - notion-cli
aliases: ["ntn", "Notion CLI"]
sources: [raw/articles/2026-05-13_notion-cli-ntn-developer-docs.md]
related: [concepts/notion-mcp]
---

# Notion CLI (ntn)

`ntn` is the official Notion CLI — a command-line interface tool by Notion that brings the full Notion API, Workers management, and file operations to the terminal. Announced May 2026 by [@NotionDevs](https://x.com/NotionDevs), it is explicitly designed for both **human developers and AI coding agents**.

## Installation

```bash
curl -fsSL https://ntn.dev | bash
```

The install script auto-detects platform (Darwin arm64/x86_64, Linux x86_64/arm64 via musl). Rosetta 2 detection ensures native arm64 binaries on Apple Silicon. No Windows support.

## Core Capabilities

### 1. Notion Workers
Create, deploy, and operate small TypeScript programs that extend Notion with syncs, tools, and webhooks:
```bash
ntn workers new       # Scaffold a project
ntn workers deploy    # Build and upload
ntn workers list      # List deployed workers
```
Workers require a Business or Enterprise plan.

### 2. API Requests
Make authenticated requests to the Notion API with inline JSON construction:
```bash
ntn api v1/users                           # GET users
ntn api v1/pages parent[page_id]=abc123    # POST with inline body fields
ntn api v1/pages/abc123 -X PATCH archived:=true  # PATCH with typed assignment
```

### 3. Data Sources
Create, query, and manage data sources from the terminal.

### 4. File Uploads
Upload static assets (images, PDFs) to Notion:
```bash
ntn files create < photo.png
ntn files create --external-url https://example.com/photo.png
```

## AI Agent Relevance

ntn is explicitly positioned as a tool for AI coding agents — enabling programmatic Notion access from agent harnesses without browser-based auth or GUI interaction. Combined with [[concepts/notion-mcp]] (the official MCP server), it provides a terminal-native bridge between coding agents and Notion workspaces.

## Comparison with Notion MCP

| Aspect | ntn (CLI) | [[concepts/notion-mcp]] |
|--------|-----------|-------------------------|
| **Interface** | Shell commands | MCP protocol |
| **Agent integration** | Bash tool / shell execution | Native MCP client |
| **Workers management** | ✅ Full (new, deploy, list) | ❌ Not covered |
| **File uploads** | ✅ Native | ❌ Not covered |
| **API requests** | ✅ Inline JSON syntax | ✅ Via MCP tools |
| **Auth** | OAuth 2.0 (browser-based `ntn login`) | OAuth 2.0 |

## Pricing
- **CLI**: Free on all plans
- **Workers**: Requires Business or Enterprise plan
- **API access**: Free tier available; rate limits apply

## See Also
- [[concepts/notion-mcp]] — Official Notion MCP server
- [Notion Developer Docs](https://developers.notion.com/cli/get-started/overview)
- [ntn.dev](https://ntn.dev) — Install script
