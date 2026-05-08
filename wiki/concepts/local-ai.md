---
title: "Local AI Landscape — May 2026"
type: concept
aliases:
  - local-ai
  - local-ai-state-2026-05
  - local-llm-state
  - state-of-local-ai
created: 2026-04-25
updated: 2026-05-08
tags:
  - concept
  - local-ai
  - local-llm
  - hardware
  - inference
  - snapshot
status: enriched
sources:
  - "raw/articles/2026-05-07_x-andrewchen-local-ai-home-lab-state.md"
  - "https://x.com/andrewchen/status/2052449121982898315"
related:
  - "concepts/local-llm"
  - "concepts/local-llm-inference-hardware"
  - "concepts/local-llm-models-april-2026"
  - "concepts/mac-studio-local-ai"
  - "concepts/dgx-spark-local-llm-server"
  - "concepts/ollama"
  - "concepts/vllm"
  - "entities/andrew-chen"
  - "entities/nvidia-dgx-spark"
  - "entities/openclaw"
  - "entities/hermes-agent"
---

# Local AI Landscape — May 2026

> **Snapshot**: May 2026時点のローカルAI環境の全体像。Andrew Chen (a16z) のホームラボ構築体験をケーススタディとして、ハードウェア・モデル・ソフトウェアスタック・ユースケース・将来展望を俯瞰する。

## Discriminative Summary

**これは何か**: 個人が自宅やオフィスで自前のハードウェア上でLLMを実行する「ローカルAI」の現在地。クラウドAPI（GPT/Claude）を使わず、自前GPUや統合メモリマシンでオープンウェイトモデルを動かす実践の総体。ハードウェア選択・モデル品質・推論速度・ソフトウェアスタック・実際のユースケースまで含む。

**これは何でないか**: クラウドLLMの比較表ではない。データセンター/エンタープライズ推論の話ではない（それは[[concepts/vllm]]や[[concepts/sglang]]の領域）。モデル学習/ファインチューニングの話でもない（それは[[concepts/local-llm/model-distillation]]の領域）。

---

## 1. ハードウェアランドスケープ

2026年5月時点での主要なローカルAIハードウェア選択肢。Andrew Chenの実際の構成をベースに整理：

### 主要プラットフォーム比較

| プラットフォーム | メモリ | 帯域幅 | 扱えるモデルサイズ | 長所 | 短所 |
|-----------------|--------|--------|-------------------|------|------|
| **Mac Studio (M4/M5)** | 最大192GB統一 | ~800 GB/s | ~120B+ (4bit) | 大容量統一メモリ、高帯域幅 | **深刻な品不足**、メモリ容量削減の動き |
| **NVIDIA DGX Spark (GB10)** | 128GB統一 | 273 GB/s | ~120B (4bit), ~200B+ (fp4) | CUDAエコシステム、NVFP4対応 | 帯域幅が低め（tok/sは遅い） |
| **RTX 5090 eGPU** | 32GB VRAM | ~1.7 TB/s | ~30B (4bit) | 超高速推論 | 24-32GB上限、eGPUでの運用に問題多数 |
| **Strix Halo (Framework)** | ~64GB統一 | — | ~70B (4bit) | モジュラー、ノートPC級 | エコシステム未成熟 |
| **Mac Mini (M4 Pro)** | 最大64GB | ~270 GB/s | ~35B (4bit) | 手軽なエントリーポイント | 大規模モデルには非力 |
| **Gaming PC (RTX 4090)** | 24GB VRAM | ~1 TB/s | ~20B (4bit) | 既存資産を活用可能 | VRAM容量が最大の制約 |

### Andrew Chenのハードウェア遍歴

```
Mac Mini → NVIDIA DGX Spark → 5090 eGPU + gaming rig → Strix Halo Framework
```

- **Mac Studioの品不足**: 「BUT GOOD LUCK GETTING A MAC STUDIO!」— 2026年時点で入手困難。メモリ容量の削減も進行中
- **5090 eGPU**: 「lots of issues with it」— 運用上の問題が多く、安定運用は難しい
- **DGX Sparkの位置づけ**: 大容量メモリだが帯域幅は低め。tok/sでは劣るがCUDAエコシステムへのアクセスが決め手
- **Mac優位の理由**: 「Mac hardware stack (particularly Mac Studios) are really good since they have pretty high bandwidth and large amounts of unified memory」

### ハードウェアの詳細
- **DGX Spark**: → [[entities/nvidia-dgx-spark]], [[concepts/dgx-spark-local-llm-server]]
- **Mac Studio**: → [[concepts/mac-studio-local-ai]]
- **推論ハードウェア全般**: → [[concepts/local-llm-inference-hardware]]

---

## 2. モデルランドスケープ

### オープンウェイトモデルの「1年遅れ」テーゼ

> "The open weight models are all about a year behind..."
> — Andrew Chen, May 2026

Andrew Chenの核心的観察：

- **オープンウェイトモデルはSOTAクラウドLLMより約1年遅れ**
- 一般消費者が実際に自宅で動かせるのは最大~120Bパラメータモデル
  - GPT OSS 120B, Qwen 3.6 122B あたりが上限
- クラウドLLMと比較して **1/100のサイズ**、**30-50 tok/s**（vs クラウドの100+ tok/s）
- しかし改善は続いている — Qwen 3.6 27B Denseはすでに「かなり使える」

### 2027年への予測

> "...it seems remarkable to think that we might be able to run **Opus level local models in 2027**."

2026年に120B級で動く品質が1年前のクラウドLLM並みだとすると、2027年には現在のOpus級がローカルで動く可能性。これはハードウェア進化（メモリ帯域幅・容量の向上）とモデル効率化（量子化技術、MoEアーキテクチャ）の両面から現実味がある。

### 現在試せる主要モデル

| モデル | サイズ | タイプ | 備考 |
|--------|--------|--------|------|
| Qwen 3.6 27B | 27B | Dense | 「かなり使える」— Andrew Chen |
| Qwen 3.6 122B | 122B | MoE? | 消費者向け上限クラス |
| GPT OSS 120B | 120B | — | 上限クラス |
| Gemma 4 | 各種 | — | Googleの最新オープンモデル |
| 35B MoE | 35B | MoE | 高速モデルとして利用（LiteLLMでの振り分け対象） |

### 新型技術の検証場としてのローカルAI

- **TurboQuant**: 新しい量子化手法 — ローカルで直接試してパフォーマンス変化を確認できる
- **DFlash**: 新しい推論高速化技術 — 同様に自環境で検証可能

→ [[concepts/model-quantization-for-local-llms]], [[concepts/local-llm-models-april-2026]]

---

## 3. ソフトウェアスタック

Andrew Chenの実際のスタック：

```
ollama / LM Studio（気軽に試す）
    ↓
LiteLLM（ローカルLLMルーター — 複雑さに応じてクエリを振り分け）
    ↓
vLLM（本格的な推論サーバー）
```

### 二段階モデル戦略

| 用途 | モデル | 特性 |
|------|--------|------|
| 高速処理 | 35B MoE | 低レイテンシ、シンプルなタスク |
| 高品質処理 | 122B | 複雑な分析、深い推論が必要なタスク |

LiteLLMがクエリの複雑さに応じて適切なモデルに自動ルーティング。

### 主要ソフトウェア

| ソフトウェア | 役割 | 詳細 |
|-------------|------|------|
| **ollama** | 手軽なモデル実行 | → [[concepts/ollama]] |
| **LM Studio** | GUI付きモデル管理 | 初心者向け |
| **LiteLLM** | ローカルLLMルーター | OpenAI API互換、複数モデルの振り分け |
| **vLLM** | 高スループット推論サーバー | → [[concepts/vllm]], [[concepts/sglang]] |
| **llama.cpp** | CPU推論/GGUF量子化 | → [[concepts/llama-cpp]] |

### AIエージェントフレームワーク

Andrew Chenはホームラボで2つのエージェントフレームワークを併用：

- **OpenClaw** — Peter Steinberger開発の常駐型パーソナルAIアシスタント。→ [[entities/openclaw]], [[concepts/openclaw-architecture]]
- **Hermes Agent** — 常駐型AIエージェント。→ [[entities/hermes-agent]], [[comparisons/hermes-vs-openclaw-architecture]]

---

## 4. パフォーマンス特性 — トレードオフの理解

ローカルAIをチューニングする過程で自然と身につく概念群：

| 概念 | 内容 | ローカルでの制約 |
|------|------|-----------------|
| **Context Window** | 一度に処理できるトークン数 | メモリ容量に直結 |
| **KV Cache** | 過去トークンのキー・バリューキャッシュ | メモリ使用量の主要因 |
| **Memory Usage** | モデル重み + KVキャッシュ + アクティベーション | ハードウェアの物理上限 |
| **Memory Bandwidth** | GB/s単位のデータ転送速度 | DGX Sparkは273 GB/s（比較的低い） |
| **Parameter Size** | モデルのパラメータ数 | 消費者向け上限 ~120B |
| **TTFT** (Time To First Token) | 初回トークン生成までの時間 | プロンプト処理速度に依存 |
| **Tokens/s** | 生成速度 | 30-50 tok/s（ローカル）vs 100+ tok/s（クラウド） |

> "as you tune your setup for maxing out tokens/s to make it as usable and responsive, you get a much better sense for all the tradeoffs"

---

## 5. 主要ユースケース

Andrew Chenの実践から明らかになった「ローカルAIのスイートスポット」：

### 非同期バッチ処理
- 個人メール全量の取り込みと要約
- ブログ記事の月次Markdown化と検索可能化
- Googleデータの構造化
- ブックマークした全記事の要約
- 登録YouTubeチャンネルの要約

### 特性
> "the sweetspot has been low-ish priority, asynch, and where the problem doesn't require SOTA"

- **低優先度 + 非同期** — 即時応答が不要なタスク
- **SOTA不要** — 100点満点の出力を求めない
- **大量データ処理** — クラウドAPIだとコストが嵩む処理
- **プライバシー重視** — 個人データをクラウドに送りたくない

### クラウド代替としての経済性
> "You could argue that this is a lot of effort and $ for something that could probably be covered by my monthly GPT/Claude subscription. And that's true! But the learning is the point :)"

---

## 6. スタートガイド

Andrew Chenのおすすめエントリーパス：

1. **すでにあるものから始める**
   - Mac M5ラップトップ、またはGPU搭載ゲーミングPC
   - 常時稼働に設定し、OpenClawジョブを向ける

2. **専用ハードウェアに投資するなら**
   - DGX Spark — 大規模モデルを試すのに最適（CUDAエコシステム）
   - Strix Haloシステム — モジュラーで将来性あり
   - GPUラックを組む道も（上級者向け）

3. **ソフトウェアから始める**
   - ollama → まずは気軽にモデルをダウンロードして試す
   - 慣れてきたらLiteLLM + vLLMスタックへ

---

## 7. 関連ページ

### コンセプト
- [[concepts/local-llm]] — ローカルLLM総論
- [[concepts/local-llm-inference-hardware]] — 推論ハードウェア詳細
- [[concepts/local-llm-models-april-2026]] — モデル別ベンチマーク
- [[concepts/mac-studio-local-ai]] — Mac Studio推論環境
- [[concepts/dgx-spark-local-llm-server]] — DGX Spark推論サーバー構築
- [[concepts/local-llm-server-setup-on-dgx-spark]] — DGX Sparkセットアップ手順
- [[concepts/ollama]] — Ollamaランナー
- [[concepts/vllm]] — vLLM推論サーバー
- [[concepts/model-quantization-for-local-llms]] — 量子化技術
- [[concepts/local-first-computing]] — ローカルファースト思想

### エンティティ
- [[entities/andrew-chen]] — 本スナップショットの原典
- [[entities/nvidia-dgx-spark]] — GB10プラットフォーム詳細
- [[entities/gemma-4]] — Gemma 4
- [[entities/qwen3-6-plus]] — Qwen 3.6
- [[entities/openclaw]] — OpenClawエージェント
- [[entities/hermes-agent]] — Hermes Agent
- [[entities/nvidia]] — NVIDIA

### 比較
- [[comparisons/hermes-vs-openclaw-architecture]] — エージェントアーキテクチャ比較

### 生記事
- [[raw/articles/2026-05-07_x-andrewchen-local-ai-home-lab-state]] — Andrew Chenのフルポスト
