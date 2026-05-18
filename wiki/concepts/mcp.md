---
title: "MCP (Model Context Protocol)"
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - concept
  - mcp
  - protocol
  - anthropic
  - tool
  - open-source
aliases: [Model Context Protocol]
sources: ["https://www.anthropic.com/news/model-context-protocol", "https://www.youtube.com/watch?v=0NHCyq8bBcM", "https://www.latent.space/p/mcp", "[[raw/articles/2025-06-10_rlancemartin_state-of-ai-agents-aie-2025]]"]
---


# MCP (Model Context Protocol)

**MCP (Model Context Protocol)** は、Anthropicが2024年11月にオープンソース化した、LLMが外部ツール・データソースと通信するための**標準プロトコル**。AIアプリケーションと外部サービス間の「M×N統合問題」を解決する。

## 概要

| 項目 | 詳細 |
|------|------|
| **発表日** | 2024年11月25日 |
| **開発者** | David Soria Parra, Justin Spahr-Summers (Anthropic) |
| **設計インスピレーション** | MicrosoftのLanguage Server Protocol (LSP) |
| **トランスポート** | JSON-RPC 2.0 (stdio, HTTP+SSE, Streamable HTTP) |
| **ライセンス** | MIT (オープンソース) |

## 3つのプリミティブ

| プリミティブ | 制御権 | 説明 |
|-------------|--------|------|
| **Tools** | モデル制御 | LLMが呼び出す外部機能（検索、計算、API呼び出し） |
| **Resources** | アプリケーション制御 | 構造化データストリーム（ファイル内容、DBレコード） |
| **Prompts** | ユーザー制御 | 再利用可能な指示テンプレート |

## 実用的起源 (Practical Origins)

MCPは抽象的なアーキテクチャ設計からではなく、Anthropic社内で起きた**2つの実践的危機の収斂**から生まれた。

### 個人レベルのフラストレーション (David Soria Parra)

2024年半ば、David Soria Parraは「Claudeを使ってAnthropic内部の開発を加速する」ミッションで入社。彼が直面した日常的な問題：

> Claude Desktop（強力な機能があるがファイルにアクセスできない）とIDE（ファイルにアクセスできるがClaudeの機能がない）の間で、**常にコピー＆ペースト**を繰り返していた。

彼の問い：「アプリケーションがユーザーに独自の統合を構築させるには何が必要か？」

Justin Spahr-Summersとともに、LSPをモデルにしたプロトコルを**約6週間**でプロトタイピング。最初の公開実装はZedエディタで登場。社内ハッカソンでは**MCPサーバーが3Dプリンターを制御**するデモが話題に。2024年11月25日にオープンソース化。

### 組織レベルの統合カオス (John Welsh)

John Welsh (Anthropic MTS) が AI Engineer World's Fair 2025 で語った社内実態：

- **2023年末〜2024年初頭**: LLMのツール呼び出しが実用レベルに到達
- Anthropic社内の各チームが**無秩序に統合を構築**し始める（Google Drive, 地図, メッセージングシステムなど）
- 各チームがカスタムエンドポイント (`/call-tool`, `/get-context`) を独自実装
- **重複機能、非互換インターフェース、コード再利用不能** — Welsh はこれを「**integration chaos（統合カオス）**」と呼ぶ
- あるサービスで動作する統合を別のサービスに移植するのに**数週間**かかる状態

驚くべきことに、これらのカスタムエンドポイントの多くが**MCPと似たパターンに独立収斂**していた（ツール発見、リソース取得など）— プロトコルの設計が自然な収束点だった証拠。

### MCP Gateway — 「成功のピット」

AnthropicはMCPを社内標準として採用し、**MCP Gateway** を構築：
- OAuth認証の一元管理
- レート制限制御
- オブザーバビリティ
- 「正しいやり方を最も簡単なやり方にする」設計思想

> *"It's not a competitive advantage to be good at plumbing integrations."* — John Welsh

## MCPが解決した「M×N問題」

MCP以前：M個のAIアプリケーション × N個の外部サービスの組み合わせ分だけカスタム統合が必要だった。

| Before MCP | After MCP |
|------------|-----------|
| M × N のカスタム実装 | M + N の標準化された接続 |
| OpenAI Function Calling, Google Extensions, LangChain Tools — すべてベンダー固有 | 単一プロトコルで全ベンダー対応 |
| 新しいデータソースごとに独自実装 | MCPサーバーを1つ書くだけ |

## 業界タイムライン

| 日付 | イベント |
|------|----------|
| Jun 2023 | OpenAI Function Calling 発表 |
| 2023-2024 | Google Extensions, LangChain Tools が乱立 |
| ~Jul 2024 | David Soria Parra が MCP コンセプト開発開始 |
| Sep 2024 | Zedエディタで初の公開MCP実装 |
| Nov 25, 2024 | AnthropicがMCPをオープンソース化 |
| Jun 2025 | AI Engineer World's Fair 2025 でMCPトラック全編開催 |

## 主要ソース

- [John Welsh: "What we learned from shipping remote MCP support at Anthropic" (AIEWF 2025)](https://www.youtube.com/watch?v=0NHCyq8bBcM)
- [Theo Chu: "MCP: Origins and Requests For Startups" (AIEWF 2025)](https://www.youtube.com/watch?v=x-8pBqWiTzk)
- [Introducing the Model Context Protocol — Anthropic Blog](https://www.anthropic.com/news/model-context-protocol)
- [Latent.Space: The Creators of Model Context Protocol (podcast with David & Justin)](https://www.latent.space/p/mcp)
- [a16z Podcast: MCP Co-Creator on the Next Wave of LLM Innovation](https://a16z.com/podcast/mcp-co-creator-on-the-next-wave-of-llm-innovation/)
- [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25)
