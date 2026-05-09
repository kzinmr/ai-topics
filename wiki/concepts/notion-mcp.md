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

Notionが公式提供する**Model Context Protocol (MCP) サーバー**。AIツールがNotionワークスペースの読み取り・書き込みを行えるようになる。

- **エンドポイント**: `https://mcp.notion.com/mcp`
- **認証**: OAuth 2.0
- **権限**: ユーザーのNotionアクセス権限に準拠

## セットアップ（主要ツール別）

| ツール | 設定方法 |
|--------|---------|
| **Claude Code** | `claude mcp add --transport http notion https://mcp.notion.com/mcp` → `/mcp` で認証 |
| **Cursor** | Settings → MCP → `{"mcpServers": {"notion": {"url": "https://mcp.notion.com/mcp"}}}` |
| **VS Code (Copilot)** | `.vscode/mcp.json` → `{"servers": {"notion": {"type": "http", "url": "..."}}}` |
| **Claude Desktop** | Settings → Connectors → URL追加 → OAuth |
| **Windsurf** | `mcp_config.json` に追加 |
| **ChatGPT** | chatgpt.com/Connectors → URL追加 |
| **Codex** | `~/.codex/config.toml` → `codex mcp login notion` |

### Claude Code用プラグイン

[Notion plugin for Claude Code](https://github.com/makenotion/claude-code-notion-plugin) — MCPサーバーに加え、事前構築済みスキルとスラッシュコマンドをバンドル。

## スコープ

| スコープ | 説明 |
|---------|------|
| `local` | 現在のプロジェクトでのみ利用可能（デフォルト） |
| `project` | `.mcp.json` 経由でチーム共有 |
| `user` | 全プロジェクトで利用可能 |

## 参照

- [Connecting to Notion MCP — Notion Developers](https://developers.notion.com/docs/get-started-with-mcp)
