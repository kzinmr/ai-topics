---
title: "Advanced Tool Use (Claude Developer Platform)"
type: concept
created: 2026-04-25
updated: 2026-05-08
tags:
  - tool-use
  - mcp
  - context-engineering
  - developer-tooling
aliases:
  - programmatic tool calling
  - Tool Search Tool
  - deferred tool loading
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_advanced-tool-use.md
  - https://www.anthropic.com/engineering/advanced-tool-use
related:
  - code-execution-with-mcp
  - mcp
  - context-engineering
  - building-effective-agents
---

# Advanced Tool Use (Claude Developer Platform)

2026年3月、Anthropicがリリースした3つの高度なツール使用機能。数百〜数千のツールを扱うエージェントのための基盤。

## 3つの新機能

| 機能 | 課題 | 解決策 |
|------|------|--------|
| **Tool Search Tool** | 全ツール定義をコンテキストに前置（58ツール=55Kトークン） | オンデマンド発見（~500トークンの検索ツールのみ前置） |
| **Programmatic Tool Calling** | 自然言語ツール呼び出し=推論パス毎 + 中間結果がコンテキスト蓄積 | コード実行環境からのツール呼び出し |
| **Tool Use Examples** | JSONスキーマは構造的妥当性しか示せず、使用パターンが伝わらない | ツールの効果的な使い方を示す例のユニバーサル標準 |

## Tool Search Tool

### トークン節約効果

| | 従来 | Tool Search Tool |
|---|---|---|
| 前置トークン | ~72K（50+ MCPツール） | ~500（検索ツールのみ） |
| 実行時トークン | — | ~3K（3-5の関連ツール） |
| 合計消費 | ~77K（会話開始前） | **~8.7K（95%削減）** |

### 精度向上

| モデル | 従来 | Tool Search Tool |
|--------|------|-----------------|
| Opus 4 | 49% | **74%** (+25pp) |
| Opus 4.5 | 79.5% | **88.1%** (+8.6pp) |

### 仕組み

```json
{
  "tools": [
    {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
    {"name": "github.createPullRequest", "defer_loading": true, ...}
  ]
}
```

- `defer_loading: true` → コンテキストに初期ロードされない
- 必要なときだけClaudeが検索→該当ツールだけ展開
- Prompt Cachingは壊れない（遅延ツールは初期プロンプトから除外）

### 使用判断
- ✅ ツール定義>10Kトークン / ツール選択精度問題 / 複数MCPサーバー / 10+ツール
- ❌ 小規模ツールライブラリ / 全ツールを常時使用 / コンパクトな定義

## Programmatic Tool Calling

### 解決する2つの問題

1. **コンテキスト汚染**: 10MBログファイル解析→全ファイルがコンテキストに入る（必要なのは要約だけ）
2. **推論オーバーヘッド**: ループ・条件分岐・データ変換のたびに推論パスが必要

### 動作
- サンドボックス化されたPython REPL内からツール呼び出し
- コードで結果を処理（フィルタリング・集計・変換）→最終結果のみコンテキストに注入
- 例: Claude for Excel — 数千行のスプレッドシートをコンテキスト過負荷なしで操作

## Tool Use Examples

```json
{
  "name": "search_customers",
  "examples": [
    {
      "description": "Search by email domain",
      "input": {"query": "@example.com", "field": "email"},
      "output": {"customers": [{"id": 123, "name": "ACME Corp"}]}
    }
  ]
}
```

- JSONスキーマだけでは表現できない使用パターン・オプションパラメータの使いどころ・API規約を伝達

## See Also

- [[concepts/code-execution-with-mcp]] — Code execution with MCP
- [[concepts/mcp]] — Model Context Protocol
- [[concepts/context-engineering]] — Context engineering for AI agents
- [[tool-use-tax]] — Tool calling performance overhead
