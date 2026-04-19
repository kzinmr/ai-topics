---
title: "Writing Effective Tools for AI Agents"
aliases:
  - writing-tools-for-agents
  - tool-design-principles
  - mcp-tool-design
  - agent-tool-ergonomics
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-architecture
  - harness-engineering
  - anthropic
  - mcp
  - tool-design
status: draft
sources:
  - "https://www.anthropic.com/engineering/writing-tools-for-agents"
---

# Writing Effective Tools for AI Agents

Anthropicが実践した、AIエージェント向けのツール設計方法论。「エージェントのためにツールを書き、エージェントを使ってツールを最適化する」アプローチ。

## 核心哲学

> "Instead of writing tools and MCP servers the way we'd write functions and APIs for other developers or systems, we need to design them for agents."

> "Tools optimized for agent context limits and reasoning patterns are often more intuitive for human developers as well."

**従来のソフトウェア開発とは異なる設計思想が必要：エージェントは非決定的であり、幻覚を見たり、仕様の解釈を誤ったりする。エージェントのコンテキスト制約と推論パターンに合わせて設計する。**

## 反復的開発ワークフロー

### 1. プロトタイプを素早く構築
- `llms.txt`ファイルでLLMフレンドリーなドキュメントを提供
- ローカルMCPサーバーまたはDesktop Extension (DXT) でツールをラップ
- Claude Code: `claude mcp add [args...]`
- Claude Desktop: `Settings > Developer/Extensions`
- 手動テストで粗い部分を特定。実際のユーザーフィードバックでユースケースを具体化

### 2. 評価を構築・実行
- **タスク設計**: 現実世界の複雑さに基づく。表面的なサンドボックスを避ける。強力なタスクは数十回のツール呼び出しを必要とする
- **検証**: フレキシブルなマッチング（フォーマット/句読点のバリエーションを許可）。単一戦略に過学習しない
- **実行**: シシンプルなエージェントルループ（whileループでLLM APIとツール呼び出しを交互に）
- **CoTトリガー**: ツール呼び出し前に推論/フィードバックを出力させる。interタスク

### 3. エージェントで自動最適化
- 評価トランスクリプトをClaude Codeに貼り付け、ツールの自動リファクタリング、不整合の修正、説明の改善
- ホールドアウトテストセットで改善を検証（訓練評価への過学習を防止）

> "Most of the advice in this post came from repeatedly optimizing our internal tool implementations with Claude Code."

## ツール設計の5原則

### 1. 適切なツールを選択する

> More tools ≠ better performance.

| ❌ 悪い例 | ✅ 良い例 |
|---|---|
| `list_contacts`, `list_users`, `create_event` | `search_contacts`, `schedule_event`, `get_customer_context` |

- 複数ステップのワークフローを統合
- コンテキストを浪費する生データダンプを避ける
- 高インパクトなツールに集中

### 2. 名前空間を戦略的に設計する

- サービス/リソースでグループ化（例: `asana_search`, `jira_search`）
- コンテキスト負荷を削減し、ツールの混乱を防止
- **プレフィックス vs サフィックスの命名はLLMによって異なる影響** — 実証的にテスト

### 3. 意味のあるコンテキストを返す

> Resolving cryptic IDs to human-readable formats significantly reduces hallucinations.

| ❌ 低いシグナル | ✅ 高いシグナル |
|---|---|
| `uuid`, `mime_type` | `name`, `image_url` |

- 技術的IDよりも意味的フィールドを優先
- 暗号的なIDを人間可読なフォーマットに解決するだけで幻覚が大幅に減少

### 4. トークン効率を最適化する

> Claude Code defaults to a 25,000-token response cap.

- ページネーション、フィルタリング、切り捨てを適切なデフォルトで実装
- **Conciseモード**: ~1/3のトークンで本質的な情報を維持
- **Detailedモード**: 下流呼び出しに必要な技術的IDのみ取得

```python
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

### 5. 説明をプロンプトエンジニアリングする

> The most effective optimization lever.

- 新入社員をオンボーディングするように書く: 暗黙のコンテキストを明示化
- 厳格なデータモデルを使用
- パラメータを明確に命名（`user_id` > `user`）
- **小さな調整が劇的な成果を生む**（例: SWE-bench VerifiedのSOTA結果）

## 現実世界の修正例

### Web検索のバイアス修正
- **問題**: Claudeがweb検索クエリに常に`2025`を追加し、結果にバイアス
- **修正**: ツール説明のみの改善で解決

### エラーレスポンス設計
- 不透明なトレースバックの代わりに、エージェントをトークン効率的な戦略に誘導する明確で実行可能な指示
- 例: 広範な検索の代わりにフィルターの使用を提案

## 評価戦術

### 強力なタスク vs 弱いタスク

| ✅ 強力（複雑、複数ステップ） | ❌ 弱い（過度に単純） |
|---|---|
| `「Janeと来週会議をスケジュール...ノートを添付...会議室を予約」` | `「jane@acme.corpと来週会議をスケジュール」` |
| `「顧客ID 9182が三重請求を報告...ログを見つける...他に影響があるか確認」` | `「顧客9182の請求を確認」` |

### 評価メトリクス
- トップレベル精度
- 実行時間
- ツール呼び出し回数
- トークン消費
- エラーレート

### パターン診断
| パターン | 診断 | 修正 |
|---|---|---|
| 冗長な呼び出し | ページネーション/トークン制限を調整 |
| パラメータエラー | 説明/例を改善 |
| エージェントフィードバックの省略 | 明示的出力よりも有益な場合がある |

## 関連概念

- [[../_index]] — 上位インデックス
- [[advanced-tool-use]] — 高度なツール使用
- [[building-effective-agents]] — エージェント構築の基本原理
- [[code-execution-with-mcp]] — MCPとのコード実行
- [[evals-skills]] — 評価スキル
