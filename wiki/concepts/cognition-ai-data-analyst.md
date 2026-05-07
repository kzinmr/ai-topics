---
title: "Cognition AI Data Analyst — Devinをデータ分析エージェントにする設計"
type: concept
aliases:
  - cognition-data-analyst
  - devin-data-analyst
  - ai-data-analyst-pattern
created: 2026-04-13
updated: 2026-05-07
tags:
  - concept
  - cognition
  - devin
  - dana
  - data-analysis
  - mcp
  - ai-agent-engineering
status: complete
sources:
  - https://devin.ai/ai-data-analyst-1
  - https://devin.ai/ai-data-analyst-2
  - https://cognition.ai/blog/how-cognition-uses-devin-to-build-devin
related:
  - code-execution-with-mcp
  - cognition-devin-philosophy
  - closing-agent-loop
---

# Cognition AI Data Analyst — Devinをデータ分析エージェントにする設計

Cognitionチームが提唱する、AIソフトウェアエンジニア（Devin）を24/7オンデマンドデータサイエンティストとして活用するアプローチ。SQL専用ツールではなく、**コードベースの文脈理解+データ分析+可視化**を統合したエージェント設計。

## 核心洞察

> "Previously, knowledge fragmentation made it extremely difficult to trace data anomalies back to their source... Getting answers often took days or weeks. Now, it takes minutes."

> "If you assume that every question would take an hour to answer, we estimate that it would take a data team **150+ hours per month** to do this work manually. With Devin, we can do it in minutes."

## なぜAIソフトウェアエンジニアをデータ分析に使うのか？

SQL専用ツールとの決定的な違い：**Devinはデータの完全な系譜（lineage）を理解できる。**

| 能力 | SQL専用ツール | Devin（AI Software Engineer） |
|------|--------------|------------------------------|
| データ探索 | マテリアライズドテーブルの結果のみ | プロダクトコード、計装イベント、ETLパイプライン、最終変換まで検索 |
| 文脈保持 | セッションごとにリセット | 過去のセッションから会社/プロダクト固有の知識を学習 |
| 自己検証 | 人間が実施 | SQLを実行して結果をライブデータで検証 |
| 非同期コラボ | 同期的なクエリ実行 | 反復的ワークフロー（クエリ→検証→可視化→議論） |
| 出力の検証可能性 | 結果のみ | 最終SQLクエリ+ダッシュボードリンク+可視化を提示 |

## アーキテクチャ: MCP + Knowledge

### MCP（Model Context Protocol）の役割

MCPはDevinと外部データサービス間のセキュアな標準ブリッジとして機能：

- **セキュアアクセス**: 認証情報を露出せずにデータウェアハウスに接続
- **スキーマ探索**: テーブル構造、リレーションシップ、データタイプをマッピング
- **クエリ実行**: 適切な権限でSQLを実行
- **結果処理**: エージェント最適化された形式で出力をフォーマット/可視化
- **自律的ツール選択**: DevinがどのMCPツールをいつ使うか自動的に判断。手動ワークフロー定義が不要

### 組み込みMCPサポート

Devinに事前設定されているMCPツール：

- **Google's MCP Toolbox for Databases** — 標準添付
- **対応データベース**: PostgreSQL, Firestore, Looker, SQL Server
- **Metabase MCP Server**（オープンソース）— 80+ツール（DB探索、ダッシュボード、カード、クエリ）
- **ロングテールDB**: 手動で認証情報ファイルをインジェクト（`Modify repo setup`）

## Knowledge Configuration — エージェントの「前提知識」設計

Devinのデータ分析精度を決定する最も重要な要素。チーム全体で共有されるコンテキストテンプレート：

### Knowledge設定の構成要素

1. **Purpose**: エージェントの役割定義（例: "Querying Redshift Data Warehouse"）
2. **Guidelines**: データアクセスの優先順位と探索手順
3. **Output Format**: 人間が検証可能な出力形式の強制
4. **Macro**: `!analytics` などのショートカットでチーム全体が即時invoke

### 設定テンプレートの重要パターン

```markdown
## Purpose:
クエリ対象とエージェントの役割を明文化

## Guidelines:
- 完全なDBスキーマを先に取得（`database://structure`）
- 分析リポジトリのREADME/docs.ymlを参照
- 疑わしい場合はanalyticsリポジトリのコードを読んで列の計算方法を確認
- **martモデルを優先**（int_/stg_プレフィックスなし）
- **analyticsスキーマを優先**（billing/rawスキーマより前）
- 不明な場合はユーザーに確認。使用するテーブルの候補を提示

## Output Format:
- 最終クエリを必ず結果と一緒に表示（人間が検証可能に）
- Metabase Playgroundリンクを生成（`get_metabase_playground_link`）
- 単一数値結果は目立つ形式で提示
- チャート/テーブルはmarkdown形式
```

## データ構造の前提条件

> "Having a legible and structured data setup is strongly recommended for using Devin as an AI data analyst. It's impossible for anyone, let alone an AI, to understand your data if it's not structured in a way that's easy to parse and understand."

**必須要件**:
- **Infrastructure as Code**: DBTでデータモデルとパイプラインをバージョン管理
- **事前マッピング**: データフロー、モデル、データベースを文書化
- **読み取り専用**: 本番DBはread-onlyユーザー認証情報に制限

## 実践的ワークフロー

```
ユーザー（Slack）→ "!analytics What's our conversion rate by industry?"
                        ↓
                   Devin（MCP経由でDB接続）
                        ↓
              スキーマ探索 → 適切なmartモデル特定
                        ↓
              SQL生成 → 実行 → 結果検証
                        ↓
              可視化生成 + 最終SQL提示 + Metabaseリンク
                        ↓
ユーザー ← 検証可能な回答（数値+チャート+SQL+リンク）
```

## Cognitionのデータ分析エージェント設計原則

1. **Software Engineer > SQL Tool**: コードベースの文脈理解があるエージェントの方が、テーブル結果だけを見る専用ツールより深い洞察を得られる
2. **Verifiable Outputs**: 最終SQLを必ず提示。人間が検証・再利用できる形式で出力
3. **Knowledge as Infrastructure**: マクロ付きKnowledge設定がチーム全体のアクセラレーター
4. **Self-Correction Loop**: エージェントが自分でクエリを実行して結果を検証（closing the agent loopのデータ分析版）
5. **Progressive Disclosure**: マートモデル → 中間モデル → 生データの優先順位で探索
6. **Async-First**: Slack経由のfire-and-forget。エージェントが24/7で処理

## 関連するCognition哲学との接続

- [[concepts/closing-agent-loop]] — Write→Catch→Fix→Mergeのループ。データ分析版: Query→Validate→Visualize→Report
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — MCPをコードAPIとして公開するパターン。データ分析ではSQL実行環境として機能
- [[concepts/cognition-devin-philosophy]] — 単一エージェントの文脈継続性。データ分析でも同じ原理（探索→分析→可視化を同一コンテキストで）
- [[concepts/harness-engineering/system-architecture/ai-memory-systems]] — Knowledge設定がエージェントの「ファイルベースメモリ」として機能

## ビジネスインパクト

| 指標 | 従来 | Devin |
|------|------|-------|
| 質問回答時間 | 数日〜数週間 | 数分 |
| チーム工数/月 | 150+時間 | 数分×質問数 |
| 知識の断片化 | 5チームに分散（Product Eng, Data Eng, DS, BI, Finance） | 一元化 |
| 出力の検証可能性 | 低（プロセスがブラックボックス） | 高（SQL+リンク付き） |

## DANA (Data Analyst Agent) — Devin版データ分析専用エージェント

Cognition社内では、Devinのデータ分析役割を **DANA (Data Analyst Agent)** として正式に製品化している。

### 特徴
- **アクセス方法**: Slackで `/dana` または `@Devin !dana` を打つだけで起動
- **対応DB**: Redshift, Snowflake, BigQuery
- **可視化**: Seabornでチャート生成、ダッシュボード構築
- **対象ユーザー**: 非エンジニアでも利用可能。「なぜ火曜日にサインアップが落ちた？」といったアドホック質問を、エンジニアを引き剥がさずに回答

### DANAとDevinの役割分担

```
@Devin       → ソフトウェアエンジニアリング全般（コード修正、PR、レビュー）
@Devin !dana → データ分析専用（クエリ、可視化、ダッシュボード）
```

これは **Agent Specialization** の実践例 — 同じエージェント基盤上で、役割ごとに異なるKnowledge・MCP・振る舞いを定義するパターン。

### 関連
- [[concepts/agent-patterns]] — エージェント特殊化パターンの実例
- [[concepts/closing-agent-loop]] — データ分析特化型の閉ループ

## End-to-End Bug Debugging — データ分析とエンジニアリングの融合

CognitionはDANAのデータ分析能力を、**バグトリアージとエンドツーエンド修正**にも拡張している。

### ワークフロー
1. **トリガー**: Linearの`Bug`ラベルがトリガー
2. **調査**: Datadog（ログ）+ read-only DBレプリカにアクセスして原因特定
3. **トレース**: 改変コミットをgit historyから特定
4. **修正**: コード修正 + 回帰テストを作成
5. **PR**: 自動でPRを開く

### 重要な接続

このワークフローは、データ分析エージェントとソフトウェアエンジニアリングエージェントの**統合**を示している：

```
データ分析（DANA）: なぜ数値がおかしい？ → コードレベルの原因特定
バグ修正（Devin）:      コード修正 + テスト追加
```

従来は別々のチーム（Data + Engineering）が担当していたワークフローを、単一エージェント基盤で完結させることで、**原因発見から修正までのリードタイムを劇的に短縮**している。

### 技術的基盤
- Datadog連携（MCP経由）
- Read-only DB replica（データ整合性検証）
- Git history walk（改変コミット特定）
- Playbook（バグトリアージ用のカスタムシステムプロンプト）
