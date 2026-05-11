---
title: "Serving DeepSeek-V4: Inference Systems Perspective"
type: concept
created: 2026-05-10
updated: 2026-05-10
tags:
  - deepseek
  - inference
  - kv-cache
  - model
  - quantization
sources:
  - https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem
  - raw/articles/together.ai--blog-serving-deepseek-v4-why-million-token-context-is-an-inf--c1510b3a.md
---

# Serving DeepSeek-V4: Inference Systems Perspective

DeepSeek-V4の100万トークンコンテキストは、単なるモデルアーキテクチャの革新ではなく、**推論システム全体の問題**として捉える必要がある。Together AIがNVIDIA HGX B200上での早期Bring-up作業を通じて得た知見をまとめる。

## Core Insight: Architecture Changes Everything Downstream

V4のHybrid Attention設計（CSA + HCA + SWA）は、従来の「単一のKVキャッシュレイアウト」の前提を根本から崩す。同じモデルでも、ワークロードの性質によって最適なサービングプロファイルが異なる。

## KV Cache Pressure: The Token Axis Revolution

### The Cache Formula

```
KV cache ∝ layers × tokens × kv_heads × head_dim × bytes
```

長文コンテキスト推論では、KVキャッシュがサービングに二重の打撃を与える：
1. **同時実行数の制限** — 各リクエストがメモリを占有
2. **スループット低下** — デコード時に毎ステップ、保存されたコンテキストを読み取る必要がある

### V4の革新: Token Axis Compression

V4は**トークン軸を圧縮**することでこの問題に直接アプローチする。従来の最適化とは異なる次元を攻撃：

| 技術 | 圧縮する次元 |
|------|-------------|
| Group Query Attention (GQA) | KV heads |
| Multi-Head Latent Attention (MLA) | Head dimension |
| FP8/MXFP4/NVFP4 | Bytes per element |
| DeepSeek-V3.2 Sparse Attention | Read amount at decode |
| **DeepSeek-V4** | **Token count itself** |

## The Three Cache Types: A Serving Nightmare

V4は単一のキャッシュではなく、**3種類の異なるKVキャッシュレイアウト**を同時に管理する必要がある：

### 1. Compressed Sparse Attention (CSA)
- **ストライド**: 4（各圧縮エントリが8トークンの近傍を要約）
- **選択**: クエリが上位128の圧縮エントリを選択
- **役割**: 選択された領域への細粒度スパースパス
- **キャッシュ特性**: 比較的コンパクト、効率的に保存可能

### 2. Heavily Compressed Attention (HCA)
- **ストライド**: 128（1Mコンテキスト → 約8Kエントリ）
- **選択**: 全エントリに対して密にアテンション（8Kは十分小さい）
- **役割**: 全文脈の粗粒度グローバル読み取り
- **キャッシュ特性**: 最もコンパクト、HCAは密にアテンション可能

### 3. Sliding Window Attention (SWA)
- **ウィンドウ**: 約128トークン
- **選択**: 最近のコンテキストを正確に保持
- **役割**: 局所的な細粒度依存関係の保存
- **キャッシュ特性**: 最も高コスト、正確なローカル状態のため保存が重い

### The Cache Policy Challenge

V4の真の課題は、これら3種類のキャッシュを**同時に管理**すること：
- 異なるサイズ、異なる寿命、異なる読み取りパターン
- CSA/HCA圧縮器は未圧縮のテール状態も使用する
- エンジンはページのeviction、prefix reuse、batchingをすべて考慮する必要がある

## Prefix Caching: From Simple Rule to Storage Policy

V4以前のprefix cachingは単純だった：「共有prefix = 共有KV」。V4では「**どのキャッシュを共有するか？**」という問題に変わる。

### Three SWA Strategies

| 戦略 | メリット | デメリット |
|------|---------|-----------|
| **Full SWA Cache Store** | 単純なprefix reuse、再計算不要 | 高いキャッシュフットプリント |
| **Periodic SWA Checkpoints** | ストレージ効率向上 | Kトークンごとの再計算コスト |
| **Recompute SWA on Hit** | 最もストレージ効率的 | 128トークン × 61レイヤー = 約8Kトークンの再計算 |

**Togetherの現在の選択**: 戦略1（Full SWA Cache）を採用中。prefix reuseを単純に保ち、残りのサービングパスが成熟するまで再計算の複雑さを回避。

### The Cache Policy Trade-off

V4はprefix cachingを**ポリシー決定**に変える：
- CSAとHCAを保存する
- SWAの扱いを決定する
- 各タイプを独自のコストでevictする

## Performance is Regime-Dependent

V4の性能はワークロードの**レジーム**によって大きく異なる：

### Long-Context, Decode-Heavy Workloads ✅
- KVキャッシュがボトルネック → V4の圧縮が直接効く
- コーディングエージェント、リサーチエージェント、長文要約
- **早期にメリットが現れる**

### Short-Context, Prefill-Heavy Workloads ⚠️
- CSAのtop-k選択、HCAの圧縮読み取り、SWAが成熟した密アテンションカーネルのパスを外れる
- MXFP4（MoE重み）とNVFP4（Blackwell）の性能特性が異なる
- **カーネル成熟度に依存**

### The Regime Split

> V4の長文コンテキストの利点は早期に現れる。短文コンテキストの性能はカーネルのbring-upとprefill最適化に依存する。

これは新しいアーキテクチャでは典型的：最初の実装は正しさを確立し、次のイテレーションでハードウェア効率のギャップを埋める。

## Practical Capacity Gains: Real Numbers

Togetherの早期bring-upでの発見：

- **Full-SWA実装**のper-token KVフットプリント: 約3.8KB（V3パスの3.4KBより高い）
- **SWAキャッシュポリシー最適化**後: 1つのHGX B200ノードで約1.2Mトークン → **3.7Mトークン**に容量増加
- **変更は最小限**: SWA状態のスマートな保存のみ

> V4のアーキテクチャは長文コンテキスト効率の**機会**を作るが、実現された容量は推論エンジンが異なるキャッシュタイプをどのように保存、再計算、evictするかに依存する。

## Workload-Specific Endpoint Profiles

同じV4モデルでも、ワークロードごとに最適なサービングプロファイルが異なる：

| ワークロード | 最適プロファイル | 主要指標 |
|-------------|-----------------|---------|
| **Long-Context Agents** | 大きなTP、バッチ有効、prefix reuse | コスト/完了タスク |
| **Coding Agents (Repo-wide)** | キャッシュティアリング、SWA再計算ポリシー | prefix hit rate, cache tier latency |
| **Short Chat** | 小さいTP、最小バッチ遅延、短文最適化カーネル | Time-to-first-token, p99レイテンシ |
| **RL Rollouts** | 長文エージェントと類似 | コスト/trajectories, experiments/バジェット |

## Benchmarking V4: What to Measure

V4への移行前に測定すべき4つの要素：

1. **Context-length regime** — 実際のコンテキスト長で性能を測定
2. **Prefix reuse** — 共有prefixのキャッシュhit率
3. **Cache policy** — SWAのfull-store vs recompute-on-hitのトレードオフ
4. **Endpoint profile** — ワークロード固有のプロファイルでの性能

### Key Insight for Agent Developers

> For long-context agents, measure cache hit rate, decode throughput, and **cost per completed task**. Time-to-first-token captures only part of the picture.

従来の「トークンあたりのコスト」ではなく、「**完了したtrajectoriesあたりのコスト**」が重要になる。

## V4 Architecture Summary: Serving Impact

| アーキテクチャ要素 | サービングへの影響 |
|-------------------|-------------------|
| **CSA** (stride 4) | コンパクト、効率的なprefix caching可能 |
| **HCA** (stride 128) | 最もコンパクト、1M→8Kに圧縮 |
| **SWA** (window 128) | 高コスト、ポリシー決定が必要 |
| **mHC** | 訓練安定性、推論への直接的影響なし |
| **Muon Optimizer** | 訓練効率、推論への直接的影響なし |
| **MXFP4 QAT** | カーネル選択に影響、BlackwellでNVFP4と異なる |

## Comparison: V4 vs V3.2 Cache Footprint

| 指標 | V3.2 | V4 | 改善 |
|------|------|-----|------|
| **KVキャッシュ (1Mコンテキスト)** | 非現実的 | 3.7Mトークン/ノード | 14x容量増 |
| **Per-token footprint** | 3.4KB (dense) | 3.8KB (SWA full) / ~0.5KB (HCA) | ポリシー依存 |
| **Prefix caching** | 単一レイアウト | 3種類のキャッシュ | 複雑化 |
| **Decode throughput** | KVバウンド | 圧縮により改善 | レジーム依存 |

## Implications for AI Agent Infrastructure

V4のアーキテクチャは、AIエージェントのインフラ設計に重要な示唆を与える：

1. **Coding Agents**: 共有リポジトリの状態をprefix cacheとして再利用可能に
2. **Research Agents**: 長文ドキュメントのコンテキストを効率的に保持
3. **Multi-Agent Systems**: 異なるエージェントタイプに異なるendpointプロファイルが必要
4. **Cost Models**: トークンあたりではなく、完了タスクあたりのコスト最適化へ

## Key Quotes

> "V4 turns million-token context into a serving-systems problem."

> "The same weights need different serving profiles."

> "Developers should benchmark V4 in their actual regime. A 1M-context coding agent and a short-context chat assistant exercise different parts of the serving stack."

> "For mixed traffic, expect tradeoffs. One endpoint can serve mixed workloads, but a profile-specific endpoint will usually perform better once the workload shape is clear."

## Related

- [[concepts/deepseek-v4]] — V4のアーキテクチャ詳細（Hybrid Attention, mHC, Muon, MegaMoE）
- [[concepts/inference]] — 推論最適化の一般論
- [[concepts/kv-cache]] — KVキャッシュの基礎
- [[concepts/prefix-caching]] — Prefix cachingの仕組み
- [[entities/together-ai]] — Together AIのサービングプラットフォーム
- [[entities/nvidia]] — NVIDIA Blackwell GPU（HGX B200）
