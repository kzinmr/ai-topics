---
title: "Desktop Extensions (MCP Bundle)"
type: concept
created: 2026-05-08
updated: 2026-05-24
tags:
  - mcp
  - developer-tooling
aliases:
  - MCP Desktop Extensions
  - .mcpb
  - MCP Bundle
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_desktop-extensions.md
  - https://www.anthropic.com/engineering/desktop-extensions
related:
  - mcp
  - model-context-protocol-mcp
---

# Desktop Extensions (MCP Bundle)

MCPサーバーを依存関係込みで1ファイルにパッケージングし、ダブルクリックでインストール可能にするフォーマット。MCPインストールの複雑さ（Node.js/Python要、手動JSON設定、依存関係地獄）を解決する。

## ファイル形式

- 拡張子: **`.mcpb`** (MCP Bundle, 旧 `.dxt`)
- 実体: **ZIPアーカイブ**

```
extension.mcpb (ZIP archive)
├── manifest.json         # 拡張メタデータ・設定
├── server/               # MCPサーバー実装
│   └── [server files]
├── dependencies/         # 全依存パッケージ/ライブラリ
└── icon.png              # オプション: 拡張アイコン
```

## Before/After

| 従来 | Desktop Extensions |
|------|-------------------|
| Node.jsやPythonのインストールが必要 | 不要 |
| `~/.claude/claude_desktop_config.json` を手動編集 | 不要 |
| パッケージ競合・バージョン不一致の解決 | 自動 |
| MCPサーバー発見はGitHub検索 | ブラウザからダウンロード |
| 更新は手動再インストール | 自動更新対応 |

## インストールフロー

1. `.mcpb` ファイルをダウンロード
2. ダブルクリック → Claude Desktopで開く
3. 「Install」をクリック
4. 完了（ターミナル不要、設定ファイル不要）

## 解決する問題

MCPローカルサーバーは強力だが、インストールの複雑さが非技術ユーザーの障壁になっていた：
- 開発ツール（Node.js, Python等）の要件
- 手動JSON設定ファイル編集
- 依存関係管理
- 発見メカニズムの欠如
- 更新の複雑さ

Desktop Extensionsはこれらすべてを抽象化する。

## See Also

- [[concepts/mcp]] — Model Context Protocol overview
- [[model-context-protocol-mcp]] — Detailed MCP specification
- [[entities/claude-code]] — Claude Code agent harness

## MCP 2026-07-28 RC: Protocol Becomes Stateless

The MCP specification's release candidate for 2026-07-28 introduces a fundamental architectural change: **the protocol is now stateless**.

### Key Changes
- **No handshake** — Connections no longer require an initial negotiation phase
- **No session ID** — Any request can hit any server instance, simplifying load balancing
- **First-class extensions** — New `MCP Apps` and `MCP Tasks` extension points
- **Auth hardening** — Improved authentication flow for production deployments
- **Clearer deprecation policy** — Structured sunset process for older protocol elements

### Implications
- **Easier scaling** — Stateless design removes sticky-session concerns, enabling simpler horizontal scaling
- **Simpler load balancing** — Any server can handle any request, reducing infrastructure complexity
- **Better resilience** — No session state to recover on server restart

> Source: [AINews May 23, 2026](https://www.latent.space/p/ainews-all-model-labs-are-now-agent)

