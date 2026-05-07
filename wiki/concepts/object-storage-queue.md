---
title: "Object Storage Queue Pattern"
tags:
  - concept
  - queue
  - object-storage
  - zero-disk
  - async-processing
  - architecture-pattern
created: 2026-05-07
updated: 2026-05-07
type: concept
related:
  - concepts/zero-disk-architecture
  - concepts/absurd-durable-execution
  - entities/turbopuffer
---

# Object Storage Queue Pattern

## 概要

**Object Storage Queue**は、Amazon S3 / GCSなどの**オブジェクトストレージをキューとして直接利用する**アーキテクチャパターン。turbopuffer社が自社のインデキシングジョブキューとして実装・公開した方式が代表例。

ゼロディスクアーキテクチャ（[[concepts/zero-disk-architecture]]）の一分野であり、状態を一切ローカルディスクに持たず、オブジェクトストレージのCAS（Compare-And-Set）能力を活用して分散キューを実現する。

> "Why are we so obsessed with building on object storage? Because it's simple, predictable, easy to be on-call for, and extremely scalable." — turbopuffer

---

## アーキテクチャ

### 5層の進化的設計

| 段階 | コンポーネント | 仕組み |
|:---|:---|:---|
| **1. Foundation** | 単一JSONファイル | キュー全体を1つの`queue.json`で表現。Pusherが読んで追記してCAS書き戻し。Workerが読んで進行中マークして書き戻し |
| **2. スループット** | Group Commit | リクエストをメモリバッファに集約し、1回のCAS書き込みでフラッシュ。RPS制限（GCS ~1 req/s）を回避 |
| **3. 競合解消** | Stateless Broker | 全クライアントに代わって単一のGroup Commitループを実行するステートレス仲介者。ACKは永続化完了後 |
| **4. HA** | Broker Failover | Brokerアドレスを`queue.json`内に記録。タイムアウト時に新Brokerが起動。CASにより一意性保証。旧Brokerは最初のCAS失敗で引退 |
| **5. 信頼性** | Job Heartbeats | Workerが定期的にハートビートを送信。タイムアウト超過でジョブを再クレーム可能 |

### データ構造

```json
{
  "broker": "10.0.0.42:3000",
  "jobs": ["◐(♥)", "◐(♥)", "○", "○", "○"]
}
```

- `○` = pending
- `◐` = in-progress
- `(♥)` = heartbeat（最終更新時刻）

---

## Zero Disk Architectureとの関係

[[concepts/zero-disk-architecture]]の最も純粋な実装例の1つ。

| Zero Diskの要件 | Object Storage Queueの実装 |
|:---|:---|
| 永続状態をすべてS3/GCSに | 全キュー状態 = 単一JSONファイル on S3/GCS |
| 計算ノードはステートレス | BrokerもWorkerも完全ステートレス |
| CASによる一貫性 | S3の条件付き書き込み（If-Match）で競合解決 |
| 耐久性 | S3/GCSの99.999999999%耐久性をそのまま活用 |
| インスタント起動/停止 | Brokerは初回CAS失敗で即引退。Workerはどこでも起動可能 |

### LCD Modelの適用

[[concepts/zero-disk-architecture]]のLCD Model（Latency vs Cost vs Durability）は、Object Storage Queueで以下のように調整される：

| 要素 | 選択 | トレードオフ |
|:---|:---|:---|
| **Latency** | Group Commitでバッファリング | 各リクエストに~200msの書き込みレイテンシ |
| **Cost** | 単一JSONファイル、最小限のAPIコール | S3のCAS書き込み1リクエストでNジョブ処理 |
| **Durability** | BrokerはS3永続化後にACK | 書き込み完了までリクエストは未承認 |

---

## Absurd（Postgres Queue）との比較

[[concepts/absurd-durable-execution]]が「Just Postgres」を掲げるのに対し、Object Storage Queueは「Just S3」に相当する。両者は「Just One Service」という精神を共有するが、トレードオフの性質が根本的に異なる。

### 比較マトリクス

| 軸 | Object Storage Queue (turbopuffer方式) | Absurd (Postgres方式) |
|:---|:---|:---|
| **ベース基盤** | S3 / GCS | PostgreSQL |
| **書き込みレイテンシ** | ~200ms（CAS PUT） | <10ms（SKIP LOCKED + INSERT） |
| **スループット** | Group Commitで数千〜数万 req/s | 数百〜数千 jobs/sec |
| **MVCC Bloat** | **なし**（オブジェクトストアにはMVCCがない） | **あり**（記事参照） |
| **一貫性モデル** | CAS（Compare-And-Set） | トランザクション + SKIP LOCKED |
| **スケール限界** | 事実上無制限（S3のスケール） | テーブルサイズ + VACUUMの制約 |
| **セルフホスト** | 不可能（S3/GCS依存） | 可能（Postgresのみ） |
| **キュー全体の可視性** | JSONファイルを読めば全部わかる | SQLクエリ |
| **運用の複雑性** | Broker層のHA設計が必要 | VACUUM / MVCC管理が必要 |
| **コスト（小規模）** | ~$0.02/GB + API呼び出し | 無料（既存Postgres） |
| **コスト（大規模）** | ほぼ一定（S3単価） | ストレージ + VACUUM I/Oで上昇 |

### 決定的な違い：MVCCの不在

最大の差異は**MVCCが存在しない**こと。PlanetScaleの記事が指摘したPostgres Queueの死亡スパイラル（デッドタプル蓄積 → ロック時間増加 → スループット低下）は、オブジェクトストレージベースのキューでは原理的に発生しない。

代わりにObject Storage Queueが抱えるリスク：

| リスク | 影響 | 緩和策 |
|:---|:---|:---|
| **高い書き込みレイテンシ** | 各PUTに~200ms | Group Commitでペイロードを増やす |
| **CAS競合** | 高競合下でリトライ頻発 | Brokerによる直列化 + Group Commit |
| **単一ファイルのサイズ限界** | JSONファイルが巨大化すると読み書きのレイテンシ増大 | 複数ファイル分割（未実装だが理論可能） |
| **Brokerの単一点** | Brokerが死ぬと新Broker選出まで停止 | タイムアウト検出 + 自動Failover |
| **オブジェクトストア依存** | GCSのRPS制限等のクラウド依存制約 | Group Commitで実質的に回避 |

---

## 実装パターンと応用

### 適用可能なユースケース

1. **高スループットなバッチジョブキュー** — インデキシング、エンコード、バッチ推論（turbopuffer本家のユースケース）
2. **ゼロディスク環境でのキュー** — Lambda + S3構成。状態を一切ローカルに置かない設計と親和性が高い
3. **簡易分散キュー** — PostgresやRedisを立てたくない小さなチーム。S3があれば動作する
4. **AI Agentのジョブディスパッチ** — AbsurdがPostgresベースなのに対し、こちらはクラウドネイティブなAgent間連携基盤として

### 非推奨なユースケース

1. **低レイテンシ（<50ms）必須** — CAS PUTの~200msの壁
2. **大量の小メッセージ** — 1メッセージごとにPUTするのはコスト効率が悪い
3. **厳密なトランザクション保証必須** — at-least-once semantics、CASベースの単一行一貫性

---

## 参考文献

- [How to Build a Distributed Queue in a Single JSON File on Object Storage](https://turbopuffer.com/blog/object-storage-queue) — turbopuffer ([[raw/articles/2026-05-07_object-storage-queue-turbopuffer]])
- [[concepts/zero-disk-architecture]] — ゼロディスクアーキテクチャ概念
- [[concepts/absurd-durable-execution]] — Postgres-Native Durable Execution（対照的なアプローチ）
- [[entities/turbopuffer]] — turbopuffer社（本パターンの実装者）
