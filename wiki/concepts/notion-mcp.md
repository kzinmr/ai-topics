---
title: "Notion MCP"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [mcp, developer-tooling, claude-code]
sources:
  - "[[raw/articles/2026-05-xx_notion_mcp-setup]]"
related:
  - "[[concepts/mcp]]"
  - "[[entities/notion]]"
---

# Notion MCP

Notion's officially provided **Model Context Protocol (MCP) server**. Enables AI tools to read and write to Notion workspaces.

- **Endpoint**: `https://mcp.notion.com/mcp`
- **Authentication**: OAuth 2.0
- **Permissions**: Based on the user's Notion access permissions

## Setup (By Major Tool)

| Tool | Setup Method |
|--------|---------|
| **Claude Code** | `claude mcp add --transport http notion https://mcp.notion.com/mcp` → Authenticate at `/mcp` |
| **Cursor** | Settings → MCP → `{"mcpServers": {"notion": {"url": "https://mcp.notion.com/mcp"}}}` |
| **VS Code (Copilot)** | `.vscode/mcp.json` → `{"servers": {"notion": {"type": "http", "url": "..."}}}` |
| **Claude Desktop** | Settings → Connectors → Add URL → OAuth |
| **Windsurf** | Add to `mcp_config.json` |
| **ChatGPT** | chatgpt.com/Connectors → Add URL |
| **Codex** | `~/.codex/config.toml` → `codex mcp login notion` |

### Plugin for Claude Code

[Notion plugin for Claude Code](https://github.com/makenotion/claude-code-notion-plugin) — Bundles pre-built skills and slash commands on top of the MCP server.

## Scopes

| Scope | Description |
|---------|------|
| `local` | Available only in the current project (default) |
| `project` | Shared with the team via `.mcp.json` |
| `user` | Available across all projects |

## References

- [Connecting to Notion MCP — Notion Developers](https://developers.notion.com/docs/get-started-with-mcp)
