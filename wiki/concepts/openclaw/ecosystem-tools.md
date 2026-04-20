---
title: "OpenClaw Ecosystem Tools"
aliases:
  - openclaw-ecosystem
  - openclaw-mcp-tools
  - steipete-tools
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - openclaw
  - mcp
  - developer-tools
  - ecosystem
related:
  - concepts/openclaw/_index
  - entities/peter-steinberger
  - concepts/mcp-model-context-protocol
sources:
  - "https://github.com/steipete"
  - "elvis analysis (April 2026)"
---

# OpenClaw Ecosystem Tools

Peter Steinberger（@steipete）が開発した**MCP-first開発者ツールエコシステム**。OpenClawを中核とし、複数のCLI/MCPサーバーが相互連携する構造。

## ツール一覧

### コアフレームワーク

| ツール | 説明 | Stars | URL |
|--------|------|-------|-----|
| **OpenClaw** | パーソナルAIエージェントフレームワーク。Telegram/Discord統合、常駐型エージェント | 135k+ instances | github.com/steipete/openclaw |
| **NemoClaw** | NVIDIAのエンタープライズ版OpenClawラッパー（OpenShell sandbox, Landlock, seccomp） | — | github.com/NVIDIA/OpenClaw |

### MCPサーバー

| ツール | 説明 | Stars |
|--------|------|-------|
| **Peekaboo** | macOS CLI + MCPサーバー。AIエージェント用のスクリーンショット取得 | 3.1k |
| **mcporter** | MCPをTypeScriptで呼び出し、CLIとしてパッケージ化 | 3.8k |
| **gogcli** | Google Suite CLI（Gmail, GCal, GDrive, Google Contacts） | 6.7k |
| **Terminator MCP** | 「I'll be back... with your terminal output!」ターミナル出力をエージェントに返す | — |

### 開発者ユーティリティ

| ツール | 説明 | Stars |
|--------|------|-------|
| **VibeTunnel** (vt.sh) | 任意のブラウザをターミナル化。リモートからエージェント操作 | — |
| **CodexBar** | OpenAI Codex / Claude Codeの使用統計（ログイン不要） | 9.9k |
| **agent-rules** | Claude Code / Cursor用のルールとナレッジベース | 5.7k |
| **tokentally** | LLMトークン + コスト計算用軽量ライブラリ | — |
| **whatmodelispeterusing.com** | Steinbergerが現在使用しているモデルの追跡ページ | — |

### レガシー

| ツール | 説明 | Stars |
|--------|------|-------|
| **Aspects** | Objective-C / Swift用のAOP（Aspect-Oriented Programming）ライブラリ | 8.4k |
| **InterposeKit** | モダンSwiftメソッドスウィズリングライブラリ | — |
| **PSPDFKit** | モバイルPDF SDK（Apple内部で使用、1B+デバイスにデプロイ） | — |

## アーキテクチャ原則

### MCP-First Design
Steinbergerのエコシステムは**Model Context Protocol (MCP)**を中心に設計されている：
- 各ツールは独立したMCPサーバーとして動作
- OpenClawがこれらのMCPサーバーを統合
- CLI経由でも直接利用可能（mcporterでパッケージ化）

### Composable Tools
> "You don't even need to use OpenClaw to benefit from OpenClaw — the patterns will show up in everything downstream for years." — elvis

個々のツールはOpenClawに依存せずに利用可能。例：
- Peekaboo単体でスクリーンショットMCPとして使用
- gogcli単体でGoogle Suite CLIとして使用
- CodexBar単体で使用統計の可視化

### Login-Free Philosophy
CodexBarやVibeTunnelなど、**ログイン不要**で使えるツールを優先。エージェントが自律的に動作する上で、認証フローはボトルネックになる。

## ClawHubマーケットプレイス

OpenClawのスキル拡張は**ClawHub**を通じて配布される：
- 新しいスキルはまずClawHubに提出
- コアへの追加は「製品またはセキュリティ上の強い理由」が必要
- ユーザーは必要に応じてインストール
- Five-Tier Skill Precedenceモデルに従ってロード

## 関連

- [[openclaw/_index]] — OpenClawコンセプト集約
- [[openclaw/five-tier-precedence]] — スキル優先度モデル
- [[peter-steinberger]] — 開発者
- [[mcp-model-context-protocol]] — Model Context Protocol
- [[nvidia-nemoclaw]] — NVIDIAエンタープライズ版
- [[local-first-software]] — ローカルファーストソフトウェア運動
