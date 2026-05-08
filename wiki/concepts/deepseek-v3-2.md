---
title: DeepSeek-V3.2
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [model, mixture-of-experts, reasoning, sparse-attention, grpo, agent, synthetic-data, training, benchmark, deepseek]
sources:
  - raw/papers/2025-12-02_2512.02556_deepseek-v3.2-technical-report.md
  - https://arxiv.org/abs/2512.02556
---

# DeepSeek-V3.2

DeepSeek-V3.2は、**685Bパラメータ**の高効率推論モデル。DeepSeek-AIが2025年12月に発表。[[concepts/deepseek-v3|V3]]を進化させ、**DeepSeek Sparse Attention（DSA）**、**スケーラブルRL（GRPO）**、**大規模エージェントタスク合成**の3つの革新により、オープンソースと商用フロンティアモデル（GPT-5、Gemini-3.0-Pro）の性能ギャップを埋めることを狙った。ハイコンピュート版**V3.2-Speciale**はIMO 2025およびIOI 2025で金メダルを獲得。

## アーキテクチャ革新

### DeepSeek Sparse Attention (DSA)

標準的な自己注意の $O(L^2)$ 計算量を $O(Lk)$（$k$ は選択トークン数）に削減する新アテンション機構。

**Lightning Indexer**（高速インデクサ）:
- クエリトークン $h_t$ と過去トークン $h_s$ 間の**インデックススコア** $I_{t,s}$ を計算
- 計算式: $I_{t,s} = \sum_{j=1}^{H^I} w^I_{t,j} \cdot \text{ReLU}(q^I_{t,j} \cdot k^I_s)$
- ハードコードされたスパースパターンではなく、**どの過去トークンを保持するかを学習**する

**Fine-grained Token Selection**:
- インデクサスコアに基づきtop-k KVエントリのみを取得
- 長コンテキストシナリオ（最大128K）での推論コストを大幅削減
- 性能劣化なしに効率を実現

DSAは後継の[[concepts/deepseek-v4|V4]]（CSA: Compressed Sparse Attention）や [[glm-5-1|GLM-5.1]] にも採用され、オープンソースLLMの長コンテキスト効率化の標準手法となった。既存の技法との比較は[[attention-mechanism-variants]]を参照。

### スケーラブルRLフレームワーク（GRPO強化）

[[concepts/deepseek-r1|R1]]で導入された[[concepts/grpo|GRPO]]（Group Relative Policy Optimization）を3つの点で強化。ポストトレーニング予算は事前学習コストの**10%超**。

| 改良点 | 内容 | 効果 |
|--------|------|------|
| **Unbiased KL Estimate** | 系統的推定誤差を除去 | 安定した収束 |
| **Off-Policy Sequence Masking** | 大きな方策乖離を起こす負例シーケンスをマスク | 訓練安定性の向上 |
| **Keep Routing / Sampling Mask** | 推論・訓練フレームワーク間でMoEルーティングとサンプリングの一貫性を保証 | フレームワーク整合性 |

### 大規模エージェントタスク合成

モデルのツール使用能力を強化するため、**1,827の異なる環境**と**85,000の複雑なプロンプト**を生成するデータ合成パイプラインを開発。

**合成タスクの種類**:
- **Trip Planning**: 複数ステップの制約充足型計画問題
- **Code Agent**: コード実行を伴う複合タスク
- 特徴: 「解くのは難しいが検証は容易」（hard to solve, easy to verify）

**Thinking in Tool-Use（ツール使用時の思考管理）**:
- ツール対話中は推論トレース（`<tool_thinking>`）を保持
- 新しいユーザーメッセージ到着時にトレースを破棄しトークン節約
- コード実行の最大回数: 20回、可能な限り言語推論よりコード実行を優先

## モデルバリアント

| モデル | パラメータ | 特性 |
|--------|-----------|------|
| **V3.2（標準）** | 685B | 推論・エージェント両対応、GPT-5-High相当 |
| **V3.2-Speciale** | 685B（高計算量推論） | 長さ制約緩和、推論トークン増加、競技特化 |

## ベンチマーク性能

| ベンチマーク | GPT-5 High | Gemini-3.0 Pro | DeepSeek-V3.2 | **V3.2-Speciale** |
|-------------|:----------:|:--------------:|:-------------:|:-----------------:|
| **AIME 2025** | 94.6% | 95.0% | 93.1% | **96.0%** |
| **HMMT Feb 2025** | 88.3% | 97.5% | 92.5% | **99.2%** |
| **GPQA Diamond** | 85.7% | **91.9%** | 82.4% | 85.7% |
| **Codeforces (Rating)** | 2537 | **2708** | 2386 | 2701 |
| **SWE-bench Verified** | 74.9% | 76.2% | 73.1% | — |

### 競技プログラミングでの成果（Speciale）

| 大会 | 結果 |
|------|------|
| **IMO 2025**（国際数学オリンピック） | 🥇 金メダル |
| **IOI 2025**（国際情報オリンピック） | 🥇 金メダル |
| **ICPC World Finals 2025** | 🥈 世界2位 |

## サーチ・長コンテキストにおけるコンテキスト管理

検索エージェントの長コンテキストボトルネック対処として、3つの戦略を実装：

| 戦略 | 動作 | 効率 |
|------|------|------|
| **Summary** | オーバーフローした軌跡を要約 | 中程度 |
| **Discard-75%** | 最古の75%のツール履歴を破棄 | 高い |
| **Discard-all** | 現在のゴールを保持しつつコンテキストをリセット | **最も効率的・スケーラブル** |

## 限界と今後の課題

1. **世界知識**: 総訓練FLOPsが少ないため、プロプライエタリモデルに依然として劣後
2. **トークン効率**: Gemini-3.0-Proと同等の品質を得るにはより長い生成軌跡（多くのトークン）が必要
3. **インテリジェンス密度（Intelligence Density）**: 推論チェーンの「密度」最適化が将来課題 — レイテンシとコストの削減

## DeepSeek進化における位置づけ

```
V3 (Dec 2024)         671B MoE、FP8訓練、DualPipe — GPT-4o級を$5.6Mで達成
    ↓
V3.2 (Dec 2025)       685B、DSA + GRPO強化 + エージェント合成 — GPT-5/Gemini-3.0-Proに迫る
    ↓
V4 (Apr 2026)         1.6T Pro / 284B Flash、1Mコンテキスト、Hybrid Attention — 完全フロンティア
```

V3.2の位置づけは、**V3の効率アーキテクチャを基盤に、DSAによる推論効率化とスケーラブルRLによる推論能力強化を加えた過渡的マイルストーン**。V4で実現した1MコンテキストやmHC、Muon Optimizerほどのアーキテクチャ飛躍はないが、DSAとエージェントタスク合成は後継モデルに継承された重要な技術的貢献。

## 歴史的意義

1. **DSAの確立**: 学習可能なスパースアテンションが実用的な長コンテキスト効率化手法として検証され、V4、GLM-5.1など後続モデルに波及
2. **オープンソース競争力の証明**: GPT-5/Gemini-3.0-Pro世代の商用フロンティアに対し、オープンウェイトモデルが肉薄できることを実証
3. **エージェント能力の合成データスケーリング**: 1,827環境・85Kプロンプトの合成パイプラインが、実タスク性能への転移可能性を示した
4. **競技AIのマイルストーン**: IMO・IOI金メダルは、AIの数学・アルゴリズム推論能力の到達点を示す

## 関連項目

- [[entities/deepseek]] — DeepSeek企業概要
- [[concepts/deepseek-v3]] — 前世代（V3アーキテクチャ）
- [[concepts/deepseek-v4]] — 後継モデル（1Mコンテキスト、Hybrid Attention）
- [[concepts/deepseek-r1]] — 推論特化モデル（GRPOの原点）
- [[concepts/grpo]] — Group Relative Policy Optimization
- [[attention-mechanism-variants]] — DSAを含むアテンション技法の比較
- [[glm-5-1]] — DSAを採用した後続モデル
- [[agent-training]] — エージェントタスク合成の文脈
- [[concepts/speculative-decoding]] — 推論効率化技術
- [[concepts/mixture-of-experts]] — MoEアーキテクチャ
