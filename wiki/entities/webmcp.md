---
title: WebMCP
type: entity
aliases:
- web-model-context-protocol
- navigator-modelContext
- w3c-webmcp
created: 2026-04-13
updated: 2026-04-13
tags:
- entity
- technology
- browser-agent
- standard
- w3c
- protocol
status: active
sources:
- https://webmcp.link/
- https://developer.chrome.com/blog/webmcp-epp
- https://developer.chrome.com/blog/webmcp-mcp-usage
- https://pub.towardsai.net/webmcp-making-your-web-app-agent-ready-d7d4d9cb790d
- https://docs.mcp-b.ai/explanation/design/spec-status-and-limitations
---

# WebMCP (Web Model Context Protocol)

**WebMCP**は、W3C Web Machine Learning Community Groupで開発されているブラウザ標準。GoogleとMicrosoftが共同で策定し、AIエージェントがWebアプリケーションと構造的に対話するための`navigator.modelContext` APIを定義する。2026年2月にChrome 146で早期プレビューが開始された。

## 概要

| 項目 | 内容 |
|---|---|
| 標準化団体 | W3C Web Machine Learning Community Group |
| 共同開発 | Google + Microsoft |
| 仕様ステータス | Draft Community Group Report（2026年2月） |
| 実装 | Chrome 146 Canary（フラグ付き） |
| API | `navigator.modelContext` |
| 提案時期 | 2025年8月（共同提案） |

## 核心コンセプト

**「ウェブサイトがAIエージェントにできることを宣言する」**

従来のブラウザエージェント（スクリーンショット解析、DOMスクレイピング）は「推測ベース」だった。WebMCPは逆転の発想で、**ウェブサイト側が構造化されたツール（名前、説明、JSON Schema入力）を明示的に登録**し、エージェントがそれらを発見・呼び出せるようにする。

### 2つのAPIアプローチ

1. **Declarative API（宣言的）**: HTMLフォーム属性で標準アクションを定義
2. **Imperative API（命令的）**: JavaScriptで複雑な動的インタラクションを実行

```javascript
// 例: ツールの登録
navigator.modelContext.registerTool({
  name: "bookFlight",
  description: "フライトを予約する",
  inputSchema: {
    type: "object",
    properties: {
      from: { type: "string" },
      to: { type: "string" },
      date: { type: "string" }
    }
  },
  execute: async (params, agent) => {
    // フライト予約ロジック
    return { success: true, bookingId: "ABC123" };
  }
});
```

## なぜWebMCPが重要か

| 指標 | 値 |
|---|---|
| トークン削減（スクリーンショット比） | 89% |
| ブラウザセッション再利用 | 100% |
| UIセレクターメンテナンス | ゼロ |

### スクリーンショットベースからの脱却
- Anthropic Computer Use / OpenAI CUA: **ビジョンモデルで画面を解析** → 遅い、トークン消費大
- browser-use / Playwright: **DOM構造を直接操作** → 動的UIに弱い
- **WebMCP**: **ウェブサイトがツールを宣言** → 正確、高速、保守容易

## タイムライン

| 日付 | マイルストーン |
|---|---|
| 2025年1月 | MCP-Bプロトタイプ |
| 2025年8月 | Google + Microsoftが共同提案 |
| 2025年9月 | W3C Community Group Draftとして正式受理 |
| 2025年10月 | `navigator.modelContext`のルート命名を解決 |
| 2026年1月 | 二重API戦略（Declarative + Imperative）を決定 |
| 2026年2月 | Chrome 146で早期プレビュー（`chrome://flags/#enable-webmcp-testing`） |
| 2026年3月 | Model Context Tool Inspector（Chrome DevTools拡張）リリース |
| 2026年3月 | Chromeブログ「When to use WebMCP and MCP」公開 |

## WebMCP vs MCP（Anthropic）

| 次元 | MCP（Anthropic） | WebMCP |
|---|---|---|
| 実行場所 | バックエンドサーバー | ブラウザタブ内 |
| プロトコル | JSON-RPC | JavaScript API |
| 可用性 | 常時（デスクトップ/モバイル/クラウド） | ウェブサイト閲覧時のみ |
| 対象 | データソース、外部ツール、ワークフロー | 特定のウェブサイトのUI操作 |
| 標準化 | 業界デファクト | W3Cコミュニティグループ |

### 補完関係
> "WebMCP is not an extension or a replacement of MCP. Instead, WebMCP and MCP address different needs."
> — Chrome Developer Blog, March 2026

## 現在の制限

1. **ヘッドレス実行不可**: ブラウザタブが開いている必要がある
2. **バックグラウンド実行不可**: ページが非表示だとツール呼び出し不可
3. **Firefox/Safari**: パブリックシグナルなし
4. **仕様未確定**: Community Group Draftのため変更の可能性あり
5. **100+のオープンイシュー**: 発見メカニズム、ライフサイクル管理など

## エコシステム

- **MCP-B Polyfill**: `@mcp-b/webmcp-polyfill` — 全ブラウザで標準APIを使用可能
- **MCP-B Global Runtime**: `@mcp-b/global` — ポリフィル付きの本番環境対応
- **Chrome DevTools拡張**: Model Context Tool Inspector
- **デモアプリ**: GoogleChromeLabs/webmcp-tools
- **TypeScript SDK**: WebMCP-org/chrome-devtools-quickstart

## 関連エンティティ

- [[anthropic-computer-use]] — スクリーンショットベースアプローチ
- [[openai-cua]] — OpenAIのComputer-Using Agent
- [[browser-use]] — DOMベース自動化
- [[concepts/death-of-browser]] — ブラウザの脱人間化潮流
- [[browserbase]] — ブラウザインフラ

## Sources

- [WebMCP Official Site](https://webmcp.link/)
- [WebMCP Early Preview (Chrome Blog)](https://developer.chrome.com/blog/webmcp-epp)
- [When to use WebMCP and MCP (Chrome Blog)](https://developer.chrome.com/blog/webmcp-mcp-usage)
- [W3C WebMCP Specification](https://webmachinelearning.github.io/webmcp)
- [WebMCP: Making Your Web App Agent-Ready (Towards AI)](https://pub.towardsai.net/webmcp-making-your-web-app-agent-ready-d7d4d9cb790d)
- [MCP-B Documentation](https://docs.mcp-b.ai/explanation/design/spec-status-and-limitations)
