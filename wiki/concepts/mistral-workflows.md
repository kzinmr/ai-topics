---
title: "Mistral Workflows"
type: concept
created: 2026-05-11
updated: 2026-05-11
tags:
  - orchestration
  - durable-execution
  - workflow
  - agents
aliases:
  - Mistral Workflows
  - Workflows (Mistral AI)
related:
  - concepts/agent-orchestration-frameworks
  - concepts/agentic-workflow-patterns
  - concepts/human-in-the-loop
  - entities/mistral-ai
  - entities/temporal
sources:
  - raw/articles/2026-05-10_mistral-ai_workflows.md
---

# Mistral Workflows

Mistral Workflows is **Mistral AI のエンタープライズAIオーケストレーションレイヤー**。2026年4月にパブリックプレビューとしてリリースされた。Temporalの永続的実行エンジンを基盤に、LLM呼び出し・ツール使用・外部API・人間の承認を含む複数ステップのAIプロセスを、クラッシュ・再起動・個別ステップの障害に耐えて本番実行するためのプラットフォーム。

**一言で**: ノートブックで動くAIデモではなく、ビジネスの現場で止まらないAIワークフローを実現する実行基盤。

## アーキテクチャ

### ハイブリッド展開モデル

Mistral Workflowsは**コントロールプレーンとデータプレーンの分離**を採用：

| 層 | 場所 | 役割 |
|---|------|------|
| **コントロールプレーン** | Mistral（または顧客のプライベートクラウド） | Temporalクラスタ、Workflows API、Studio UI — 状態・履歴・タスクディスパッチを管理 |
| **データプレーン** | 顧客環境（Kubernetes / VM / ローカル） | Workerプロセスが実際のコードを実行。LLM呼び出し・ツール実行・ビジネスロジックはすべて顧客のペリメーター内 |

WorkerはHelm chartでKubernetesにデプロイし、アウトバウンド接続でMistralのクラスタに接続する。オーケストレーターが顧客ネットワークにインバウンド接続することはない。

### Temporal基盤

内部では[Temporal](https://temporal.io/)の永続的実行エンジン（Netflix/Stripe/Salesforceと同じ基盤）を使用。MistralはTemporalをAIワークロード向けに拡張し、ストリーミング、ペイロードハンドリング、マルチテナンシー、OpenTelemetryベースの可観測性を追加している。

## 中核機能

### 1. Durable Execution（永続的実行）

すべてのステップがイベント履歴に記録される。プロセスがクラッシュ・タイムアウト・Worker再起動しても、**別のWorkerが履歴を再生し、最後に完了したステップから再開**する。

- 通常のアプリケーションコードでは、ネットワークタイムアウトで複数ステップのプロセスが中途半端に終わる
- Workflowsでは、数分〜数時間〜数ヶ月にわたる長期実行プロセスが生存する
- 開発者はリカバリロジックではなく**ビジネスロジック**に集中できる

### 2. Human-in-the-Loop（承認ワークフロー）

`wait_for_input()` の1行で、ワークフローを承認待ちで一時停止できる：

```python
approval = workflow.wait_for_input("Review required")
```

- ワークフローは一時停止し、計算リソースを消費しない
- レビュアーに通知が送られ、Le Chat / Webhook / APIのいずれかから応答可能
- レビュアーが応答すると、中断した正確なポイントから再開
- 全実行履歴がStudioに記録され、監査可能

### 3. Observability（可観測性）

- すべての分岐・リトライ・状態変更がStudioに記録
- OpenTelemetryネイティブ対応（追加設定不要）
- 数ヶ月後の意思決定調査にも対応可能な完全なタイムライン
- 各ルーティング判断・モデル呼び出し・承認ステップをドリルダウン可能

### 4. AI Primitives

ワークフロー内で直接使えるAI特化プリミティブ：
- **Agent loop**: エージェントの反復実行（観察→思考→行動ループ）
- **LLM streaming**: トークンストリーミングをクライアントに中継
- **Mistral API統合**: 追加の統合コードなしでモデルを呼び出し
- **Tool use**: 外部API・データベース・ファイル操作のアクティビティ化

### 5. マルチサーフェストリガー

1つのワークフローを3つの経路から起動可能：

| トリガー方法 | 対象ユーザー |
|-------------|------------|
| **Mistral API** (`POST /v1/workflows/{name}/execute`) | 開発者・外部システム |
| **Mistral AI Studio** | 運用チーム（入力フォーム自動生成＋ライブ実行タイムライン） |
| **Le Chat** | ビジネスユーザー（アシスタントとして会話内でワークフローを起動） |

## Python SDK

開発者はPythonでワークフローをコードとして記述。SDK v3.0がパブリックプレビューと同時に公開。

**中核概念**: ワークフロー（決定論的オーケストレーション）とアクティビティ（副作用を伴う外部処理）の分離：

- **Workflow**: ステップの調整・状態保持・分岐・待機・次のアクション決定（決定論的）
- **Activity**: LLM呼び出し・HTTPリクエスト・DB書き込み・ファイル読み取り・ツール実行（副作用）

SDKはデコレータと1行設定でリトライポリシー・トレーシング・タイムアウト・レート制限を処理する。

## 実運用ユースケース

### 貨物リリース自動化（CMA-CGM等）

- 税関申告・危険物分類・安全検査・規制チェックを複数管轄にまたがって自動化
- タイムアウト生存・人間レビューの中間停止・障害時の正確な原因特定が必要
- `wait_for_input()` で人間の承認を待機し、再開時に正確に継続

### ドキュメントコンプライアンス（KYC審査）

- 本人確認書類抽出 → 制裁リスト/PEP DB照合 → 管轄横断の規制要件クロスリファレンス → 構造化リスク評価
- 従来は1ケースあたり数時間のアナリスト作業 → 数分に短縮
- Studioが全ステップを構造化タイムラインとして表示、OpenTelemetryトレースで詳細までドリルダウン可能

### カスタマーサポート振り分け

- 返金・技術問題・請求紛争・アカウントエスカレーションの自動分類・ルーティング
- 誤分類時の修正可能性（correctability）が重要要件
- 各ルーティング判断がStudioで可視化・追跡可能。分類が間違っていた場合、チームがワークフローレベルで修正

## 利用判断基準

### 使うべきケース

- クラッシュ・再起動に耐える必要がある複数ステップのLLMパイプライン
- 数時間〜数日にわたる承認待ちを含むHuman-in-the-loopプロセス
- スケジュール実行または1回限りの定期AIタスク
- ハンドオフと共有状態を持つマルチエージェントオーケストレーション
- 現在キュー・ステートマシン・リトライコードで構築しているもの全般

### 不要なケース

- オーケストレーション不要の単一LLMエンドポイント呼び出し → 通常のSDK呼び出しで十分

## 競合・関連技術との違い

- **[[concepts/agent-orchestration-frameworks]]** (LangGraph, CrewAI等) — これらはエージェント間の調整に焦点。Mistral Workflowsは永続的実行・Human-in-the-loop・エンタープライズ監査を基盤として提供し、その上でエージェントも動かせる。
- **[[concepts/agentic-workflow-patterns]]** — Anthropicの5パターン（Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer）は設計パターン。Mistral Workflowsはそれらを実装する**実行基盤**。
- **Temporal単体** — Mistral WorkflowsはTemporalの上にAI特化の拡張（ストリーミング、ペイロード、マルチテナンシー、OpenTelemetry、Le Chat統合）を追加したマネージドレイヤー。
- **AWS Step Functions / Azure Durable Functions** — 汎用ワークフローエンジン。Mistral WorkflowsはAIプリミティブ（エージェントループ、LLMストリーミング、モデル呼び出し）をネイティブ統合している点が差別化。

## 採用企業（パブリックプレビュー時点）

ASML, ABANCA, CMA-CGM, France Travail, La Banque Postale, Moeve
