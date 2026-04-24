---
title: "Agentic Web — 人間向けからエージェント向けへWebのパラダイムシフト"
type: concept
created: 2026-04-22
updated: 2026-04-22
tags: [concept, web-infrastructure, ai-agents, cross-cutting]
status: active
sources:
  - "Richard MacManus — The Agentic Web (Apr 2026)"
  - "https://ricmac.org/2026/04/07/the-agentic-web/"
aliases:
  - agentic-web
  - websites-as-capabilities
  - ax-agent-experience
---

# Agentic Web

> "The web is transitioning from a human-centric read/write platform to an Agentic Web, where AI systems interact with websites on behalf of users."

**概要:** Webサイトが「人間が読むもの」から「エージェントが操作するランタイム」へ変遷する潮流。Tim Berners-Leeのビジョンの進化 — 知識が機械によってアクセス、解釈、実行される。

## 4つの原動力

### 1. Webサイトが機能を公開
- **MCP:** Anthropic Nov 2024、AIが外部アクションをトリガーする主要方法
- **WebMCP:** ブラウザにMCPツールを直接提供（拡張/Chrome Canary必要、ネイティブ化予定）
- **カスタムチャットボット:** ベクトルDB搭載のサイト固有AIアシスタントが標準化
- **経済レイヤー:** 情報取得→トランザクション実行（予約、購入、サブスクリプション）

### 2. ユーザーインターフェースの変化
- 初期AI: ヘッドレスブラウザ + スクレイピング/フォーム記入
- 現在/未来: サイト所有者に案内され、メインストリームブラウザに組み込まれ、高度ツールで強化
- **発見のシフト:** リンク/検索検索 → 自然言語プロンプト
- **SEO進化:** 従来SEO → **「AIリトリバル最適化」**（AIの選択、引用、信頼性への最適化）

### 3. ブラウザがAIランタイムへ進化
- **オンデバイスAI:** Gemini NanoなどのSLMがブラウザ内でプライベート・低レイテンシAI実行を可能に
- **相互作用モード:**
  - `Browsing Mode`: 人間らしいナビゲーション＆UIパース
  - `Tool Mode`: 構造化機能への直接呼び出し
- **トレンド:** ナビゲーションからツールベース相互作用への明確な移行

### 4. 開発者プラットフォームの適応
- Cloudflare, Vercel, Netlifyが爆発的成長。VercelはNext.js経由でエージェントホスティング + MCPエンドポイント
- **標準化エージェントUI:**
  - MCP-UI (Anthropic連携、Shopifyで使用)
  - OpenAI Apps SDK & AgentKit
  - MCP Apps (インタラクティブUIのオープン標準)
  - Google A2UI (エージェントUIフレームワーク)
- **UIはデバッグレイヤー:** トランザクションサービスは人間のUIを完全に削除する可能性あり

## 影響: ロール別

### プロダクトチーム
- エージェント＋人間の両方をデザイン。マシン可読な機能を公開。AX (Agent Experience) をUXに統合。

### パブリッシャー
- **脅威:** 直接訪問減少、AIがコンテンツアクセスを仲介
- **機会:** AIシステムへの信頼できる「情報源」になる
- **課題:** 補償危機、Really Simple Licensing (RSL) プロトコルなどの新解決策

### 開発者
- マシン可読なシステムをデフォルトで構築。エンドポイントではなくオーケストレーションで思考。
- ハイブリッドスタック: ブラウザAI + クラウド推論 + MCP + 従来Webインフラ

## Related Concepts

- [[death-of-browser]] — ブラウザのパラダイムシフト
- [[webmcp]] — ブラウザネイティブのMCP標準
- [[anthropic-computer-use]] — Anthropic Computer Use
- [[openai-cua]] — OpenAI CUA
- [[browser-use]] — オープンソースブラウザ自動化
- [[browserbase]] — 信頼性の高いブラウザ自動化インフラ
