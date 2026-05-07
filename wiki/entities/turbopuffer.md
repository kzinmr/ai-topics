---
title: "turbopuffer"
tags: [entity, service, vector-database, search, object-storage]
created: 2026-05-07
updated: 2026-05-07
team:
  - name: Simon Hørup Eskildsen
    role: Co-founder & CEO
    background: Former Shopify
  - name: Justine
    role: Co-founder & CTO
    background: Former Shopify
  - name: Nathan VanBenschoten
    role: Chief Architect
    focus: Vector search, SPFresh, RaBitQ, ANN v3
  - name: Adrien Grand
    role: Engineer
    focus: BM25, MAXSCORE, full-text search
  - name: Morgan Gallant
    role: Engineer
    focus: Full-text search, inverted indexes, recall monitoring
  - name: Nikhil Benesch
    role: Engineer
    focus: LSM tree, infrastructure
  - name: Xavier Denis
    role: Engineer
    focus: Rust performance, SIMD optimization
  - name: Bojan Serafimov
    role: Engineer
    focus: Native filtered vector search
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
|| **ベクトルインデックス** | SPFresh（セントロイドベースANN）— v3ではRaBitQ量子化＋AVX-512対応 |
| **全文検索インデックス** | カスタムLSM Tree on Object Storage |
| **API** | REST（JSON） |
| **ライセンス** | プロプライエタリ（マネージドサービス） |
| **設立** | 不明（〜2024?） |

### パフォーマンス（v1ベンチマーク）

| シナリオ | レイテンシ |
|:---|:---|
| Cold Query（1M vectors, 3GB） | 444ms p90 |
| Warm Query（同） | **10ms** p90 |
| Cold Query（1M docs BM25, 300MB） | 285ms p90 |
| Warm Query（同） | **18ms** p90 |
| WAL書き込み（500kB） | 285ms p50 |

### パフォーマンス（ANN v3 — 2026年5月）

| 構成 | レイテンシ（p99） | Recall@10 | QPS/ノード |
|:---|:---:|:---:|:---:|
| **100B vectors, ANN v3** | **200ms** | >90% | ~100K |
| 10B vectors, ANN v3 | ~50ms | >95% | ~100K |
| 1B vectors, ANN v3 | ~20ms | >97% | ~100K |
| 1M vectors（v1 ベースライン） | ~10ms（warm） | ベースライン | ~1K |

**ANN v3の技術革新:**
- **RaBitQ二値量子化**: 768次元f32ベクトルを16-32x圧縮、距離計算をXOR+popcountに変換
- **AVX-512 VPOPCNTDQ**: 1サイクルで512比較、f32ドット積比32xの演算密度
- **SPFresh階層化**: 100x分岐係数の階層クラスタリング
- **ランダムシャーディング**: ストレージ最適化VM間で線形スケーリング

### ネイティブフィルタリング（Native Filtering）

2025年1月導入。SPFreshクラスタリングベースのインデックスでフィルタリングをネイティブ統合。

| 方式 | フィルタ付きRecall | レイテンシ | スケーラビリティ |
|:---|:---:|:---:|:---:|
| **Pre-filter** | 100% | O(n) — 遅い | 悪い |
| **Post-filter** | 0-60%（選択率依存） | 高速 | 良い |
| **Native（turbopuffer）** | **>90%** | **高速** | **良い** |

**2層インデックス:**
1. **クラスタレベル**: `(attribute_value, cluster_id)` → ビットマップ — 高速ビットマップ演算
2. **行レベル**: `(cluster_id, vector_id)` → ベクトル — フィルタ通過クラスタ内のみANN

### 継続的Recall測定

2024年9月導入。**実生産クエリの1%をサンプリング**し、recall@10を継続監視。

- **ターゲット**: 90-95% recall@10
- **検出**: インデックス劣化を数分以内に検知
- **主張**: 実生産環境での継続的recall監視を実装した最初の検索エンジン

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
|| 2024-09-04 | Morgan Gallantが「Continuous Recall Measurement」公開 — 実生産環境での1%クエリサンプリングによるrecall@10継続測定を導入（[[raw/articles/2024-09-04_turbopuffer-continuous-recall]]） |
|| 2025-01-21 | Bojan Serafimovが「Native Filtering」公開 — SPFreshクラスタリングベースのフィルタリング手法（[[raw/articles/2025-01-21_turbopuffer-native-filtering]]） |
|| 2025-09 | Jason Liuがアーキテクチャ解説「TurboPuffer: Object Storage-First Vector Database Architecture」を公開 |
|| 2025-11 | turbopuffer製品ローンチ — S3/GCSネイティブな検索エンジン |
|| 2026-01-07 | Adrien Grandが「BM25 Scaling Surprises」公開 — クエリ長とレイテンシの冪乗則モデル（[[raw/articles/2026-01-07_turbopuffer-bm25-scaling]]） |
|| 2026-01-14 | Morgan Gallant & Adrien Grandが「FTS v2 Postings」公開 — 固定サイズブロック分割による9.9xインデックス圧縮（[[raw/articles/2026-01-14_turbopuffer-fts-v2-postings]]） |
|| 2026-01-14 | Adrien Grand & Morgan Gallantが「Vectorized MAXSCORE over WAND」公開 — MAXSCORE動的プルーニングへの移行理由（[[raw/articles/2026-01-14_turbopuffer-fts-v2-maxscore]]） |
|| 2026-02-03 | Adrien Grand・Morgan Gallant・Nikhil Beneschが「FTS v2」発表 — 20x高速全文検索、10x小さい転置インデックス（[[raw/articles/2026-02-03_turbopuffer-fts-v2]]） |
|| 2026-03-05 | 正式ブログ公開 — 「turbopuffer: fast search on object storage」でアーキテクチャとコストメリットを詳述 |
|| 2026-03-08 | Xavier Denisが「Rust Zero-Cost Abstractions vs SIMD」公開 — バッチイテレータによる220ms→47ms高速化（[[raw/articles/2026-03-08_turbopuffer-rust-zero-cost-simd]]） |
|| 2026-04 | Rank by Attribute機能リリース（Adrien Grand） — BM25＋数値属性の複合ランキング（[[concepts/turbopuffer-rank-by-attribute]]） |
|| 2026-05-05 | Nathan VanBenschotenが「ANN v3」公開 — RaBitQ量子化＋AVX-512 VPOPCNTDQによる100Bベクトル200ms p99検索（[[raw/articles/2026-05-05_turbopuffer-ann-v3]]） |
|| 2026-05-07 | Object Storage Queueブログ公開 — 自社インデキシングキューをオブジェクトストレージで再構築した事例（[[concepts/object-storage-queue]]） |

---

## 全文検索（FTS v2）

turbopufferは2026年2月に**FTS v2**をリリース。20倍高速な全文検索と10倍小さい転置インデックスを実現した。

### 固定サイズブロック分割

v1では文書クラスタ単位で可変サイズのブロックに分割していたが、v2では**~256ポスティングの固定サイズブロック**を使用。

| 方式 | ブロックサイズ | 圧縮率 | スキップ精度 |
|:---|:---:|:---:|:---:|
| **v1（クラスタベース）** | 可変（42〜1,204） | 低い | 悪い |
| **v2（固定サイズ）** | 〜256 | 高い（9.9x削減） | 良い |

**N=256の理由**:
1. **圧縮効率**: デルタ符号化+ビットパッキングに十分な密度
2. **スキップ性能**: MAXSCOREプルーニングの最小単位として最適
3. **オーバーヘッドバランス**: ブロックメタデータ（〜32B）が1.6%に

### MAXSCORE動的プルーニング

WAND（Weak-AND）から**MAXSCORE**に移行。特にLLM生成クエリ（長文・多トークン）で効果を発揮。

| アルゴリズム | アプローチ | 長クエリ(50+語)の性能 |
|:---|:---|:---:|
| **WAND** | 文書中心（pivot管理のオーバーヘッド大） | 1.0x（ベースライン） |
| **Block-MAXSCORE** | 用語中心（必須語が候補発見、全語がスコアリング） | **2.5x** |

「必須語が候補を見つけ、全語がスコアする」— 固定サイズブロックと組み合わせることで、1ブロック処理（256ポスティング）がL1キャッシュに収まり、SIMD処理との親和性が高い。

### Quickwitビットパッキング

Quickwitのビットパッキングライブラリを採用し、**741M postings/sec**の展開スループットを達成。

| 方式 | 展開スループット |
|:---|:---:|
| **Quickwit bitpacking** | 741M postings/s |
| VByte（ベースライン） | 200M postings/s |
| Simple-8b | 400M postings/s |

### word_v3 トークナイザー

- NFKC正規化
- 数字・英数字混合の改良処理
- ロケール対応のケースフォールディング
- 効率的な前方一致クエリ

### インデックスサイズ（MSMARCOデータセット）

| コンポーネント | FTS v1 | FTS v2 | 削減率 |
|:---|:---:|:---:|:---:|
| **Doc IDs** | 25.7 GiB | 2.62 GiB | 9.8x |
| **Term Frequencies** | 12.2 GiB | 1.12 GiB | 10.9x |
| **Positions** | 13.7 GiB | 1.48 GiB | 9.3x |
| **Total** | **51.6 GiB** | **5.22 GiB** | **9.9x** |

### BM25スケーリングモデル

Adrien Grandが発見したBM25の逆説的性質：**トークン数増加がレイテンシ低下につながる場合がある**。

$$f(n) = C \cdot n^K$$

| クエリ長 | K値（スケーリング指数） | 挙動 |
|:---|:---:|:---|
| 短い（1-5語） | K=0.35 | 強く劣線形 |
| 中程度（5-20語） | K=0.65 | 中程度の劣線形 |
| 長い（20-100+語） | K=0.92 | ほぼ線形 |

必須語（高IDF）は候補選択を駆動し、非必須語（低IDF）はMAXSCOREで効率的にスキップされる。

---

## チーム

| 名前 | 役割 | 担当/経歴 |
|:---|:---|:---|
| **Simon Hørup Eskildsen** | Co-founder & CEO | 元Shopify |
| **Justine** | Co-founder & CTO | 元Shopify |
| **Nathan VanBenschoten** | Chief Architect | ベクトル検索、SPFresh、RaBitQ、ANN v3 |
| **Adrien Grand** | Engineer | BM25、MAXSCORE、全文検索 |
| **Morgan Gallant** | Engineer | 全文検索、転置インデックス、recall監視 |
| **Nikhil Benesch** | Engineer | LSM Tree、インフラ基盤 |
| **Xavier Denis** | Engineer | Rustパフォーマンス、SIMD最適化 |
| **Bojan Serafimov** | Engineer | Native Filtered Vector Search |

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

### turbopuffer公式ブログ
- [turbopuffer: Fast Search on Object Storage](https://turbopuffer.com/blog/turbopuffer) — 正式発表ブログ（[[raw/articles/2026-05-07_turbopuffer-fast-search-object-storage]]）
- [How to Build a Distributed Queue in a Single JSON File](https://turbopuffer.com/blog/object-storage-queue) — キュー実装ブログ（[[raw/articles/2026-05-07_object-storage-queue-turbopuffer]]）
- [ANN v3: 100B Vector Search at 200ms p99](https://turbopuffer.com/blog/ann-v3) — RaBitQ量子化+AVX-512による第3世代ANN（[[raw/articles/2026-05-05_turbopuffer-ann-v3]]）
- [Rust Zero-Cost Abstractions vs SIMD](https://turbopuffer.com/blog/zero-cost) — バッチイテレータによる4.7x高速化（[[raw/articles/2026-03-08_turbopuffer-rust-zero-cost-simd]]）
- [FTS v2: 20x Faster Full-Text Search](https://turbopuffer.com/blog/fts-v2) — 第2世代全文検索（[[raw/articles/2026-02-03_turbopuffer-fts-v2]]）
- [FTS v2 Postings: Building Better Inverted Indexes](https://turbopuffer.com/blog/fts-v2-postings) — 固定サイズブロックと9.9x圧縮（[[raw/articles/2026-01-14_turbopuffer-fts-v2-postings]]）
- [Vectorized MAXSCORE over WAND](https://turbopuffer.com/blog/fts-v2-maxscore) — 動的プルーニングの選定理由（[[raw/articles/2026-01-14_turbopuffer-fts-v2-maxscore]]）
- [BM25 Scaling Surprises](https://turbopuffer.com/blog/bm25-latency-musings) — クエリ長とレイテンシの冪乗則（[[raw/articles/2026-01-07_turbopuffer-bm25-scaling]]）
- [Native Filtering](https://turbopuffer.com/blog/native-filtering) — クラスタリングベースのフィルタ検索（[[raw/articles/2025-01-21_turbopuffer-native-filtering]]）
- [Continuous Recall Measurement](https://turbopuffer.com/blog/continuous-recall) — 実生産環境でのrecall@10監視（[[raw/articles/2024-09-04_turbopuffer-continuous-recall]]）

### 公式ドキュメント
- [Architectureドキュメント](https://turbopuffer.com/docs/architecture)
- [Concepts: Cache Hierarchy, LSM, SPFresh](https://turbopuffer.com/docs/concepts)
- [Tradeoffs](https://turbopuffer.com/docs/tradeoffs)

### 第三者による分析
- [TurboPuffer: Object Storage-First Vector Database Architecture](https://jxnl.co/writing/2025/09/11/turbopuffer-object-storage-first-vector-database-architecture/) — Jason Liuによる技術解説
- [turbopuffer — Why Now Tech Primer](https://whynowtech.substack.com/p/turbopuffer) — Alex Mackenzieによる詳細分析
