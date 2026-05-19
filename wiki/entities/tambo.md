---
title: Tambo
created: 2026-05-11
updated: 2026-05-11
type: entity
status: L2
tags:
  - company
  - open-source
  - tool
  - platform
  - ai-agents
  - mcp
  - developer-tooling
  - web-development
aliases: [tambo-ai, tambo.ai, tambo.ai/react]
sources: [https://tambo.co, https://github.com/tambo-ai/tambo, https://docs.tambo.co]
related: [mcp, vercel-ai-sdk, ai-agents]
---

# Tambo

> Build agents that speak your UI — オープンソースの **Generative UI** ツールキット for React

Tambo は、React アプリに AI エージェントを組み込むためのオープンソースツールキット。既存の React コンポーネントを Zod スキーマで登録するだけで、エージェントがユーザーの発話に応じて適切なコンポーネントを選択・レンダリングする。「Show me sales by region」→ `<Chart>`、「Add a task」→ `<TaskBoard>` という具合。

**GitHub**: [tambo-ai/tambo](https://github.com/tambo-ai/tambo) | **NPM**: `@tambo-ai/react` | **Website**: [tambo.co](https://tambo.co)

## Key Facts

| Item | Detail |
|------|--------|
| Founded | 2024, Seattle, WA |
| Co-founders | Michael Magán (CEO), Michael Milstead |
| GitHub Stars | ~2.5K+ (2026-05) |
| License | MIT |
| Stack | React (TypeScript), Zod |
| Investors | The General Partnership, Dan Lewis (Convoy), Drew Houston (Dropbox), Eric Wittman (VSCO) |
| Notable Users | Zapier, Rocket Money, Solink |

## アーキテクチャ

Tambo はフルスタック構成で、React SDK + バックエンド（会話状態管理とエージェント実行）を提供する。

```
ユーザー発話 → Tambo Agent (LLM) → コンポーネント選択 + Props ストリーミング → UI 描画
```

**3層構造**:
1. **React SDK** (`@tambo-ai/react`) — `<TamboProvider>`, スレッド管理, ストリーミング, コンポーネントレンダリング用フック
2. **Built-in Agent** — LLM 会話ループ実行。外部フレームワーク不要。OpenAI / Anthropic / Gemini / Mistral / OpenAI互換API対応
3. **Backend** — Tambo Cloud（ホスト版）または Docker セルフホスト

## 主要機能

| 機能 | 説明 |
|------|------|
| **Generative Components** | Zod スキーマを LLM tool definition に変換、エージェントがコンポーネントを関数呼び出し感覚で選択 |
| **Streaming Infrastructure** | Props をプログレッシブストリーミング。キャンセル・エラーリカバリ・再接続を自動処理 |
| **MCP Support** | Model Context Protocol 経由で DB/API/外部システムと接続 |
| **Component State** | ユーザー操作に応じた状態更新をエージェントが管理 |
| **User Authentication** | エージェントがユーザーの権限を継承、AI機能を安全に保つ |
| **Multi-Model** | OpenAI, Anthropic, Gemini, Mistral, OpenAI互換プロバイダ対応 |
| **Component Library** | [ui.tambo.co](https://ui.tambo.co) — エージェント向けUIプリミティブ集 |

## 価格

| プラン | 料金 | 内容 |
|--------|------|------|
| **Starter** | Free | 10K messages/mo, 無制限ユーザー(OAuth), コミュニティサポート |
| **Growth** | $25/mo | 200K messages/mo ($8/100K追加), 分析・可観測性付き |
| **Enterprise** | 年額契約 | 交渉可能ボリューム, SSO/SAML/SCIM/RBAC, SOC 2/HIPAA/GDPR, 99.99% SLA |

オープンソース版は **無料で永続セルフホスト可能**。

## Generative UI の位置づけ

Tambo は Vercel AI SDK とは異なるアプローチを取る。Vercel が汎用的な AI SDK であるのに対し、Tambo は **「AI が UI を出力する」** という Generative UI パラダイムに特化。既存のコンポーネントをそのまま使い、AI が「どの UI を表示すべきか」を判断するレイヤーを提供する。

LangChain や Mastra などのエージェントフレームワークと併用可能だが、必須ではない。

## Use Cases

- **db-thing** — 会話型DB設計。スキーマ作成→ERD生成→最適化→SQLエクスポート
- **Strudel AI** — ライブコーディング音楽生成。ドラム・メロディ・シンセをリアルタイム重ね合わせ
- **CheatSheet** — AIがコンポーネントで応答するチートシート生成

## 競合・関連

- [[vercel-ai-sdk]] — 汎用AI SDK。Generative UIも部分的にカバー
- [[mcp]] — Tambo が依存するプロトコル
- [[langchain]] — エージェントフレームワークとして併用可能
