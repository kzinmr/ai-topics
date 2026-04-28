---
title: Process Supervision for AI Agent Runtimes
created: 2026-04-28
updated: 2026-04-28
type: concept
tags: [infrastructure, architecture, technique, reliability]
sources:
  - raw/articles/crawl-2026-04-28-process-supervision.md
---

# Process Supervision for AI Agent Runtimes

Process Supervision（プロセス監視）は、長時間実行されるエージェントプロセスのライフサイクル管理、障害検出・復旧、リソース監視を行う基盤技術。AIエージェントを本番運用するための**Harness Engineeringの前提概念**。

## 背景: なぜプロセス監視が重要か

AIエージェントは従来のマイクロサービスよりも複雑な障害モードを持つ：
- LLM呼び出しのタイムアウトやレイテンシスパイク
- 無限ループ（トークン消費爆発）
- 部分的なツール実行失敗からの状態不整合
- クラッシュ後のチェックポイント喪失

Harness Engineeringは「エージェントを実行する環境」を設計するが、その前提としてプロセスの死活監視と自動復旧の仕組みが不可欠となる。

## 主要概念

### 1. スーパーバイザーパターン

スーパーバイザーは管理対象プロセスのライフサイクルを監視するデーモン：

```
[マネージャー] → [スーパーバイザー] → [子プロセスA]
                                    → [子プロセスB]
                                    → [子プロセスC]
```

| 機能 | 説明 |
|------|------|
| **自動再起動** | クラッシュしたプロセスを即座に再起動 |
| **レート制限** | 再起動ループを防止（max_retries + backoff） |
| **通知** | 障害イベントを外部システムに伝達 |
| **Graceful Shutdown** | SIGTERM送信後、猶予期間を経てSIGKILL |

### 2. スーパーバイザーの状態機械

```
[作成] → [起動中] → [実行中] → [停止中] → [停止]
                   → [クラッシュ] → [起動中] (自動再起動)
                   → [クラッシュ] → [停止] (最大リトライ超過)
```

### 3. チェックポイントベースの耐久性

エージェントは各決定・ツール呼び出し後に状態を永続ストレージに書き込む：
- 実行状態（どのステップまで完了したか）
- ツール実行結果（再実行を避ける）
- エージェントメモリ/コンテキストの要約
- タイムスタンプ

**回復フロー:**
1. スーパーバイザーがプロセスクラッシュを検出
2. プロセスを再起動
3. エージェントが最後のチェックポイントから状態復元
4. 未完了のステップから処理再開（冪等性保証付き）

## AIエージェント向け実装アプローチ

| アプローチ | 説明 | 適切なユースケース |
|-----------|------|-----------------|
| **Dedicated (Temporal)** | Temporalのような耐久性ワークフローエンジン | ミッションクリティカル |
| **LLM Framework (LangGraph)** | LangGraphのチェックポイント機構 | LLMエコシステム内のチーム |
| **Agent Runtime (OmniDaemon)** | Agent Supervisorによるプロセス分離 + 自動再起動 | マルチエージェントシステム |
| **Custom (s6/supervisord)** | Unix process supervisor + カスタム起動スクリプト | 軽量・シンプルなユースケース |

### OmniDaemon: Agent Supervisorパターン

OmniDaemonは各エージェントを独立プロセスで実行し、Agent Supervisorがライフサイクルを管理:
- **Fault Isolation:** エージェントAのクラッシュがエージェントBに影響しない
- **Resource Safety:** 厳格なメモリ/CPU境界
- **Observability:** メトリクス、ログ、状態追跡のビルトイン
- **Reliability:** リトライ、DLQ（Dead Letter Queue）、ハートビート

```python
supervisor = await create_supervisor_from_directory(
    agent_name="my_agent",
    agent_dir="./my_agent",
    callback_function="agent.run"
)
```

## 回復パターン

| パターン | 説明 |
|---------|------|
| **Exponential Backoff** | 失敗間隔を倍増（1s → 2s → 4s → 8s） |
| **Circuit Breaker** | 連続失敗後に即時拒否、クールダウン後再開 |
| **Dead-Letter Queue** | 処理不能なイベントを別キューに隔離 |
| **Graceful Degradation** | 非クリティカルツールのスキップと継続 |

## エージェント固有の監視要件

従来のプロセス監視とは異なり、AIエージェントには以下が必要：
- **トークン消費監視:** 予算超過の検出と停止
- **ループ検出:** 同一ツールの繰り返し呼び出しパターン
- **レイテンシ異常検知:** LLM応答の異常な遅延や異常な長さ
- **コンテキスト消費チェック:** コンテキストウィンドウ溢れの事前検知

## 関連概念

- [[concepts/harness-engineering]] — 上位概念: Harness Engineeringの必須前提技術
- [[concepts/agent-sandboxing]] — プロセス分離とサンドボックスの関係
- [[concepts/closing-agent-loop]] — ループ検出とプロセス終了条件
- [[concepts/context-engineering]] — コンテキスト消費監視との連携
