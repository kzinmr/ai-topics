---
title: "turbopuffer"
tags: [entity, service, vector-database, search, object-storage]
created: 2026-05-07
updated: 2026-05-07
type: entity
related:
  - concepts/zero-disk-architecture
  - concepts/object-storage-queue
  - concepts/turbopuffer-rank-by-attribute
  - concepts/absurd-durable-execution
---

# turbopuffer

## 概要

**turbopuffer**は、オブジェクトストレージ（S3/GCS/Azure Blob）を唯一の永続レイヤーとして構築された、ベクトル検索＋全文検索エンジン。従来のベクトルデータベースと異なり、データのプライマリストアがオブジェクトストレージであり、SSD/RAMはキャッシュとしてのみ機能する。この「Object-Storage-Native」アーキテクチャにより、従来比**6–100倍のコスト削減**と99.99%のアップタイムを実現。

**公式サイト:** https://turbopuffer.com/
**GitHub:** なし（プロプライエタリ）

---

## プロダクト詳細

### 基本スペック

| 項目 | 値 |
|:---|:---|
| **種類** | マネージド検索エンジン（ベクトル + BM25全文検索 + 集計） |
| **プライマリストレージ** | S3 / GCS / Azure Blob（ソースオブトゥルース） |
| **キャッシュ** | NVMe SSD + メモリの階層キャッシュ |
| **ベクトルインデックス** | SPFresh（セントロイドベースANN） |
| **全文検索インデックス** | カスタムLSM Tree on Object Storage |
| **API** | REST（JSON） |
| **ライセンス** | プロプライエタリ（マネージドサービス） |
| **設立** | 不明（〜2024?） |

### パフォーマンス

| シナリオ | レイテンシ |
|:---|:---|
| Cold Query（1M vectors, 3GB） | 444ms p90 |
| Warm Query（同） | **10ms** p90 |
| Cold Query（1M docs BM25, 300MB） | 285ms p90 |
| Warm Query（同） | **18ms** p90 |
| WAL書き込み（500kB） | 285ms p50 |

### コスト比較（TB/月）

| アーキテクチャ | コスト |
|:---|:---:|
| RAM + 3x SSD（従来型） | $3,600 |
| 3x SSDのみ | $600 |
| **turbopuffer（S3 + SSD Cache）** | **$70** |
| Raw S3 | $20 |

---

## アーキテクチャ

### Object-Storage-Native LSM

![turbopuffer architecture diagram showing client → API → Memory/SSD Cache → Object Storage (S3)](/docs/architecture)

- **全永続状態はオブジェクトストレージ上** — 計算ノードは完全ステートレス
- **WAL（Write-Ahead Log）** — 書き込みはまずWALに追記され、非同期でLSM Treeにマージ。WALもオブジェクトストレージ上
- **LSM Tree on S3** — ほとんどの実装がローカルディスク用に設計されている中、turbopufferは最初からS3上で動作するLSMを独自実装
- **クエリプランニング** — オブジェクトストレージへのラウンドトリップを最大3回に制限
- **SPFresh** — セントロイドベースの近似最近傍探索。グラフベース（HNSW/DiskANN）よりオブジェクトストレージとの親和性が高い。ラウンドトリップ数と書き込み増幅を最小化

### キャッシュ階層（Pufferfish Effect）

```
Cold (Object Storage)  →  Warm (NVMe SSD)  →  Hot (RAM)
      ~500ms                  ~数十ms              <10ms
```

「Pufferfish Effect」 — 検索されるほどデータがキャッシュに巻き上がり（inflate）、高速化する。使われないデータはコールドストレージに留まりコストを圧縮。

### 一貫性モデル

| モード | レイテンシ | 特性 |
|:---|:---|:---|
| **Strong Consistency（デフォルト）** | ~10msフロア | GET IF-NOT-MATCHで最新を確認。書き込み後すぐに読み取り可能 |
| **Eventual Consistency** | <10ms | キャッシュのみ。書き込み後しばらく古いデータが見える可能性 |

---

## 沿革

| 日付 | イベント |
|:---|:---|
| 〜2024 | Simon Hørup Eskildsen（元Shopify）とJustine（CTO、元Shopify）が創業 |
| 2025-09 | Jason Liuがアーキテクチャ解説「TurboPuffer: Object Storage-First Vector Database Architecture」を公開 |
| 2025-11 | turbopuffer製品ローンチ — S3/GCSネイティブな検索エンジン |
| 2026-03 | 正式ブログ公開 — 「turbopuffer: fast search on object storage」でアーキテクチャとコストメリットを詳述 |
| 2026-04 | Rank by Attribute機能リリース（Adrien Grand） — BM25＋数値属性の複合ランキング（[[concepts/turbopuffer-rank-by-attribute]]） |
| 2026-05 | Object Storage Queueブログ公開 — 自社インデキシングキューをオブジェクトストレージで再構築した事例（[[concepts/object-storage-queue]]） |

---

## 主要顧客

| 顧客 | ユースケース | 効果 |
|:---|:---|:---|
| **Cursor** | コードベース検索（数十億ベクトル） | 95%コスト削減、Eval 23.5%改善 |
| **Notion AI** | セマンティック検索 / RAG | ベクトル検索の大規模運用 |
| **Linear** | Issue検索 | 全文検索 + セマンティック検索 |
| **Superhuman** | メール検索 | 高速全文検索 |
| **Readwise** | ハイライト検索 | 全文検索 |
| **Suno** | 音楽生成関連検索 | — |

### 現在のスケール

- 3.5T+ ドキュメントホスティング
- 10M+ writes/s
- 25k+ queries/s
- 99.99% uptime since launch

---

## Zero Disk Architectureとの関係

turbopufferは、[[concepts/zero-disk-architecture]]を実践する最も代表的な商用プロダクトの1つ。

- **オブジェクトストレージ唯一依存**: 「No Dependencies」— クリティカルパスにオブジェクトストレージ以外のステートフル依存なし
- **ステートレス計算ノード**: Rust製バイナリがS3バケットから直接namespaceを読み込む。ノード故障 → 別ノード即座に引き継ぎ
- **究極の耐久性**: S3の99.999999999%耐久性をそのまま利用。Shopify時代の「pager fatigue」から学んだ設計哲学

> "The fewer stateful dependencies, the more nines of uptime." — Simon Hørup Eskildsen

---

## 関連ページ

- [[concepts/object-storage-queue]] — turbopufferが実装したオブジェクトストレージ上のキュー実装パターン
- [[concepts/turbopuffer-rank-by-attribute]] — BM25＋数値属性の複合ランキング機能
- [[concepts/zero-disk-architecture]] — ゼロディスクアーキテクチャ概念（turbopufferはその商用実装の代表例）
- [[concepts/absurd-durable-execution]] — Postgres-Native Durable Execution（対照的な「Just One Service」アプローチ）

## 参考文献

- [turbopuffer: Fast Search on Object Storage](https://turbopuffer.com/blog/turbopuffer) — 正式発表ブログ（[[raw/articles/2026-05-07_turbopuffer-fast-search-object-storage]]）
- [How to Build a Distributed Queue in a Single JSON File](https://turbopuffer.com/blog/object-storage-queue) — キュー実装ブログ
- [Architectureドキュメント](https://turbopuffer.com/docs/architecture)
- [Concepts: Cache Hierarchy, LSM, SPFresh](https://turbopuffer.com/docs/concepts)
- [Tradeoffs](https://turbopuffer.com/docs/tradeoffs)
- [TurboPuffer: Object Storage-First Vector Database Architecture](https://jxnl.co/writing/2025/09/11/turbopuffer-object-storage-first-vector-database-architecture/) — Jason Liuによる技術解説
- [turbopuffer — Why Now Tech Primer](https://whynowtech.substack.com/p/turbopuffer) — Alex Mackenzieによる詳細分析
