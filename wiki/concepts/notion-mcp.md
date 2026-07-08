---
title: "Notion MCP"
type: concept
created: 2026-05-09
updated: 2026-07-08
status: L2
tags: [mcp, developer-tooling, claude-code]
sources:
  - "[[raw/articles/2026-05-xx_notion_mcp-setup]]"
  - "[[raw/articles/merge.dev--blog-notion-mcp-codex--377672e7]]"
  - "[[raw/articles/merge.dev--blog-notion-mcp-cursor--53090c10]]"
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

## Third-Party Notion MCP Providers

### Merge Agent Handler

[Merge Agent Handler](https://www.merge.dev/agent-handler) provides a managed Notion MCP integration that wraps the Notion API with centralized authentication, OAuth management, audit trails, and per-operation access scoping.

- **How it works**: Install the Merge CLI (`pipx install merge-api`), authenticate via `merge login`, and run a setup command that writes tool-calling instructions to `AGENTS.md` (Codex) or `.cursorrules` (Cursor). Merge manages OAuth token storage and refresh on behalf of the user.
- **Key features**:
  - **Centralized auth**: Single sign-on flow; no token state lives in the repo or local environment.
  - **OAuth management**: Automatic credential refresh — no manual token rotation.
  - **Audit trails**: Every tool call is logged with input, output, and identity, providing a full observability layer.
  - **Per-operation scoping**: Define which Notion pages, databases, and operations each agent is allowed to reach; Merge enforces those boundaries.
- **Supported tools**: Codex (via `AGENTS.md`), Cursor (via `.cursorrules`), Claude Code (via `AGENTS.md`), and any toolchain that can invoke the Merge CLI (`merge search-tools` and `merge execute-tool`).
- **Enterprise features**: SCIM provisioning via Okta/Microsoft Entra ID, DLP policy enforcement, user-level audit logging (via [Agent Handler for Employees](https://www.merge.dev/agent-handler-employees)).

Sources:
- [How to connect a Notion MCP with Codex (4 steps) — Merge Blog](https://www.merge.dev/blog/notion-mcp-codex)
- [How to connect a Notion MCP to Cursor (4 steps) — Merge Blog](https://www.merge.dev/blog/notion-mcp-cursor)

## References

- [Connecting to Notion MCP — Notion Developers](https://developers.notion.com/docs/get-started-with-mcp)
