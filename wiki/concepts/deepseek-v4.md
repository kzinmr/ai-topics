---
title: DeepSeek-V4
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [model, mixture-of-experts, long-context, hybrid-attention, fp4, speculative-decoding, agent, training, benchmark, deepseek]
sources:
  - raw/papers/2026-04-xx_deepseek-v4-technical-report.md
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf
---

# DeepSeek-V4

DeepSeek-V4は、**100万トークン（1M）コンテキスト**の超高効率処理を実現したMixture-of-Experts（MoE）モデルシリーズ。DeepSeek-AIが2026年4月に発表。[[deepseek-v3|V3]]アーキテクチャを基盤に、**Hybrid Attention、Manifold-Constrained Hyper-Connections（mHC）、Muon Optimizer**など複数の革新的技術を導入し、1Mコンテキストでの推論コストをV3.2比で**3.7〜10倍削減**。

## モデルラインナップ

| モデル | 総パラメータ | 活性化パラメータ | コンテキスト | ライセンス |
|--------|-------------|-----------------|-------------|-----------|
| **V4-Pro** | 1.6T | 49B | 1M tokens | MIT |
| **V4-Flash** | 284B | 13B | 1M tokens | MIT |
| **V4-Pro-Max** | 1.6T+ | 49B+ (reasoning) | 1M tokens | MIT |

## アーキテクチャ革新

### Hybrid Attention: 3層のハイブリッドアテンション

従来の自己注意機構は系列長に対して二次計算量 $O(n^2)$ を持つ。1Mコンテキストではこれが致命的なボトルネックとなる。V4は3つの補完的アテンションをインターリーブしてこの問題を解決：

| レイヤー | 方式 | 圧縮率 | アテンション | 役割 |
|---------|------|--------|-------------|------|
| **CSA** (Compressed Sparse Attention) | KVキャッシュ圧縮 + Top-k疎Attention | m=4 | DeepSeek Sparse Attention (DSA) | 長距離依存の効率的捕捉 |
| **HCA** (Heavily Compressed Attention) | 超圧縮（最大128x）+ 密Attention | m'=最大128 | Dense | グローバルコンテキストの粗粒度把握 |
| **SWA** (Sliding Window Attention) | 局所ウィンドウ | 窓サイズ=128 | Dense | 局所的な細粒度依存関係の保存 |

**アーキテクチャ上の特徴**:
- CSAはクエリが圧縮KVの上位kエントリのみに注目 → 計算量を大幅削減
- HCAは極端な圧縮によりグローバルな文脈を低コストで保持
- SWAは局所パターン（隣接トークン間の文法・構文など）を逃さない
- 3層の出力はゲーティング機構で統合（詳細は非公開）

### Manifold-Constrained Hyper-Connections (mHC)

従来の残差結合（Residual Connection）を拡張し、残差マッピングを**二重確率行列（doubly stochastic matrices）**の多様体上に制約。

$$x_{l+1} = x_l + f_\theta(x_l) \quad \rightarrow \quad x_{l+1} = M(x_l) \cdot f_\theta(x_l)$$

ここで $M(x_l)$ は二重確率行列（各行・各列の和が1、全要素 ≥ 0）。

- **スペクトルノルム ≤ 1**: 順伝播・逆伝播の数値的安定性が飛躍的に向上
- **効果**: 1Mコンテキストのような超深層・長系列での勾配消失/爆発を抑制
- V3の補助損失なし負荷分散と同様、訓練安定性を損なわずにモデル深度を拡張可能

### Muon Optimizer

大部分のモジュールでAdamWを**Muon**に置換。

- **Hybrid Newton-Schulz Iterations**: 直交化のための数値手法。行列の直交性を反復的に改善
- **効果**: AdamW比で収束が高速化、訓練安定性が向上
- **適用範囲**: Attention投影行列、MLP重みなど主要モジュール。MoEルーティングなど一部はAdamWを継続使用

## 訓練インフラ

### データセット

**32T+トークン**の多様な高品質データで事前学習。V3（14.8T）の2倍以上のデータ規模。

### 訓練安定化技術

**Anticipatory Routing（予測的ルーティング）**:
- MoEのルーティング更新をバックボーン更新から分離
- ルーティングインデックスを履歴パラメータ $\theta_{t-\Delta t}$ で計算
- **目的**: ルーティングの急激な変化による損失スパイクを防止
- V3の「ゼロロールバック」安定性をさらに強化

**SwiGLU Clamping**:
- SwiGLU活性化関数の線形成分を $[-10, 10]$ にクランプ
- 活性化の極端な外れ値を抑制し、FP8/FP4低精度訓練の安定性を確保

### MegaMoE: 細粒度Expert Parallelism

V4の最大のシステム革新の一つ。

- **通信と計算の融合**: all-to-all通信を単一のパイプライン化カーネルに統合
- **帯域効率**: 「1 GBpsのインターコネクト帯域が6.1 TFLOP/sの計算を隠蔽するのに十分」
- H800 GPUのインターコネクト制約（~400 GBps NVLink）を最大限活用

### TileLang DSL

カスタムカーネル開発のためのドメイン特化言語。

| 機能 | 効果 |
|------|------|
| **Host Codegen** | CPU側オーケストレーションのオーバーヘッドを数百μs → <1μsに削減 |
| **Deterministic Kernels** | 非決定的atomic操作を回避し、訓練と推論でビット単位の再現性を保証 |
| **Fused Kernels** | 複数操作を単一カーネルに融合し、HBM読み書きを最小化 |

## 効率性: V3.2との比較（1Mコンテキスト時）

| 指標 | V4-Pro vs V3.2 | V4-Flash vs V3.2 |
|------|---------------|-----------------|
| **トークンあたりFLOPs** | 27%（**3.7x削減**） | 10%（**10x削減**） |
| **KVキャッシュサイズ** | 10%（**10x削減**） | 7%（**14x削減**） |

> 1MコンテキストでV4-ProのFLOPsはV3.2の約1/4、KVキャッシュは1/10。これはHybrid AttentionとmHCの相乗効果による。

## ポストトレーニング

### 2段階パイプライン

```
Specialist Training → On-Policy Distillation (OPD)
```

**Stage 1: Specialist Training（専門家訓練）**
- 数学・コード・エージェントの各ドメインで個別の専門家モデルを訓練
- 手法: SFT + [[grpo|GRPO]]
- 各専門家は特定ドメインで極限まで最適化

**Stage 2: On-Policy Distillation (OPD)**
- 複数の教師専門家の**全語彙ロジット分布**から単一の生徒モデルが学習
- 従来の蒸留（離散出力のみ）より情報損失が少ない
- 複数ドメインの能力を単一モデルに統合

### エージェント機能

**Interleaved Thinking（インターリーブド推論）**:
- V3.2まで：推論トレースはツール呼び出し境界でリセット
- V4：ユーザーメッセージ境界を越えて推論トレースを保持・継続
- 複数ツール呼び出しを含む複雑なエージェントタスクで性能向上

**Quick Instruction**:
- `<|action|>` や `<|query|>` の特殊トークンで補助タスク（Web検索意図検出など）を処理
- 別の小型モデルを必要としない → レイテンシ削減

### FP4 QAT（量子化アウェア訓練）

| 適用箇所 | 目的 |
|---------|------|
| MoEエキスパート重み | メモリトラフィック削減（FP16比75%減） |
| CSAインデクサーパス | インデックス計算の高速化 |

FP4はFP8のさらに半分のビット幅。ただし活性化はFP8/BF16を維持し、重みのみFP4化するハイブリッド戦略。

## ベンチマーク

### 推論・コーディング

| Benchmark | V4-Pro-Max | 比較対象 |
|-----------|-----------|---------|
| **Codeforces** | **3206 rating**（人間23位相当） | — |
| Code Agents (内部R&D) | 67% pass rate | Claude Opus 4.5: 70% |
| 数学・推論 | GPT-5.2, Gemini-3.0-Proに匹敵以上 | — |

### 知識・言語

| Benchmark | V4-Pro-Max | 比較 |
|-----------|-----------|------|
| SimpleQA | 57.9% | オープンモデル最高 |
| Chinese-SimpleQA | 84.4% | — |
| 中国語機能作文 | 62.7% win rate | vs Gemini-3.1-Pro |

### 実タスク

| タスク | V4-Pro-Max | 比較 |
|--------|-----------|------|
| 高度専門職30タスク | **63% non-loss rate** | vs Claude Opus 4.6 |
| 長文コンテキスト | Gemini-3.1-Pro超え | 学術ベンチマーク |

## V3からの進化サマリー

| 次元 | DeepSeek-V3 (Dec 2024) | DeepSeek-V4 (Apr 2026) |
|------|----------------------|----------------------|
| **最大パラメータ** | 671B / 37B active | 1.6T / 49B active |
| **コンテキスト** | 128K | **1M** |
| **アテンション** | MLA | **Hybrid Attention (CSA+HCA+SWA)** |
| **残差結合** | 標準Residual | **mHC (多様体制約)** |
| **Optimizer** | AdamW | **Muon (+ AdamW一部)** |
| **データ規模** | 14.8T tokens | **32T+ tokens** |
| **訓練安定化** | Aux-Loss-Free | Anticipatory Routing + SwiGLU Clamping |
| **Expert Parallelism** | 標準 | **MegaMoE** |
| **カーネル開発** | CUDA手書き | **TileLang DSL** |
| **ポストトレーニング** | SFT + GRPO + R1蒸留 | **Specialist Training + OPD** |
| **量子化** | FP8 | **FP4 QAT (重みのみ)** |
| **エージェント** | — | Interleaved Thinking, Quick Instruction |
| **コード** | Codeforces 1134 | **Codeforces 3206** |

## 歴史的意義

DeepSeek-V4は以下の点でマイルストーン的成果：

1. **1Mコンテキストの実用化**: Hybrid Attentionにより、100万トークン長の処理を実用的なコストで実現
2. **効率革命**: V3.2比でFLOPs 3.7-10x削減、KVキャッシュ10-14x削減 → 長文推論の経済性を根本から変革
3. **mHC**: 残差結合に多様体制約を導入する新しい正則化パラダイム
4. **MegaMoE + TileLang**: ハードウェア限界を克服するシステムソフトウェア革新
5. **On-Policy Distillation**: 複数専門家の全ロジット分布から学習する新しい蒸留パラダイム
6. **Agent-Native Design**: Interleaved Thinking、Quick Instruction — 最初からエージェント用途を想定した初のDeepSeekモデル

## 関連項目

- [[entities/deepseek]] — DeepSeek企業概要
- [[deepseek-v3]] — 前世代アーキテクチャ
- [[deepseek-r1]] — 推論特化モデル（GRPOの起源）
- [[grpo]] — ポストトレーニングで使用されるRLアルゴリズム
- [[mixture-of-experts]] — MoEアーキテクチャ一般
- [[long-context]] — 長文コンテキスト処理技術
- [[speculative-decoding]] — 投機的デコーディング
- [[fp4]] — 4ビット量子化
- [[tilelang]] — カーネル開発DSL
- [[inference]] — 推論効率化技術
