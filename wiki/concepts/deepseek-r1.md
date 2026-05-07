---
title: DeepSeek-R1
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [model, reasoning, reinforcement-learning, grpo, distillation, chain-of-thought, benchmark, deepseek, nature]
sources:
  - raw/papers/2025-01-22_2501.12948_deepseek-r1.md
  - https://arxiv.org/abs/2501.12948
  - https://doi.org/10.1038/s41586-025-09422-z
---

# DeepSeek-R1

DeepSeek-R1は、**純粋な強化学習（RL）によってLLMの推論能力を引き出せる**ことを初めて大規模に実証した画期的モデル。DeepSeek-AI（中国）が2025年1月に発表。**Nature**（Vol. 645, pp. 633-638, 2025）に掲載された、数少ない産業界発のNature論文の一つ。人間がアノテーションしたChain-of-Thought（CoT）デモンストレーションなしに、自己検証・内省・「アハモーメント」などの高度な推論行動が**創発（emerge）**することを示した。

## モデルファミリー

DeepSeek-R1プロジェクトは3層のモデルファミリーを生み出した：

### DeepSeek-R1-Zero: 純粋RLからの推論創発

[[deepseek-v3|DeepSeek-V3-Base]]を起点に、**一切のSFT（Supervised Fine-Tuning）を行わず**、純粋なRLのみで訓練。

- **アルゴリズム**: [[grpo|GRPO（Group Relative Policy Optimization）]]
- **報酬**: ルールベースのみ（ニューラル報酬モデル不使用）
  - 正解報酬（Accuracy Rewards）: 数学の正解、コードのコンパイル結果など検証可能な指標
  - フォーマット報酬（Format Rewards）: 思考過程を `think` タグ内に配置
- **訓練コスト**: ~101K H800 GPU時間（約$202K）

**創発的行動**:
- 自己検証（self-verification）: 中間ステップの正しさを自発的にチェック
- 内省（reflection）: 矛盾を検出すると「待って、再評価しよう」と自律的に軌道修正
- 動的戦略適応: 行き詰まったアプローチを放棄し、別の解法を試行

> **「アハモーメント」（Aha Moment）**: 訓練中盤、モデルが自律的に「Wait, wait. Wait. That's an aha moment I can flag here. Let's reevaluate this step-by-step...」と出力。これはプログラムされた行動ではなく、RLの過程で**創発**した推論パターン。

**R1-Zeroの課題**:
- 言語混在（英語と中国語が混ざる）
- 可読性の低さ
- フォーマットの不安定さ

### DeepSeek-R1: マルチステージパイプライン

R1-Zeroの課題を解決するため、4段階の訓練パイプラインを設計：

```
Cold Start SFT → Reasoning RL → Rejection Sampling + SFT → General RL
```

| 段階 | 内容 | データ規模 |
|------|------|-----------|
| **1. Cold Start** | 数千の長文CoT例でSFT。可読性のある推論ベースラインを確立 | ~数千例 |
| **2. Reasoning RL** | 数学・コード・論理に焦点を当てた大規模RL（GRPO） | — |
| **3. Rejection Sampling + SFT** | 600K推論サンプル + 200K一般サンプル（計800K）でSFT | 800Kサンプル |
| **4. General RL** | 有用性・無害性のための最終RLアライメント（報酬モデル使用） | — |

**総訓練コスト**: R1-Zero ($202K) + R1 ($82K) = **約$294K**

### 蒸留モデル（Distilled Models）

DeepSeek-R1の出力を教師データとして、小型オープンソースモデルに推論能力を蒸留。

| 生徒モデル | AIME 2024 (Pass@1) | MATH-500 (Pass@1) |
|-----------|---------------------|---------------------|
| DeepSeek-R1-Distill-Qwen-1.5B | 28.9% | 83.9% |
| DeepSeek-R1-Distill-Qwen-7B | 55.5% | 92.8% |
| DeepSeek-R1-Distill-Llama-8B | 50.4% | 89.1% |
| **DeepSeek-R1-Distill-Llama-70B** | **70.0%** | **94.5%** |

> **衝撃的結果**: DeepSeek-R1-Distill-Llama-70Bは、AIME 2024・MATH-500で**GPT-4oやClaude-3.5-Sonnetを上回った**。また、蒸留Qwen-1.5B（僅か1.5Bパラメータ）がMATH-500で83.9%を達成 — これはGPT-4o (74.6%) や非推論特化の大規模モデルを凌駕する。

## ベンチマーク

### 推論ベンチマーク（OpenAI o1との比較）

| Benchmark | DeepSeek-V3 | OpenAI o1-mini | **DeepSeek-R1** | OpenAI o1-1217 |
|-----------|-------------|----------------|-----------------|----------------|
| AIME 2024 (Pass@1) | 39.2 | 63.6 | **79.8** | 79.2 |
| MATH-500 (Pass@1) | 90.2 | 90.0 | **97.3** | 96.4 |
| GPQA Diamond (Pass@1) | 59.1 | 60.0 | **71.5** | 75.7 |
| Codeforces (Rating) | 1134 | 1820 | **2029** | 2061 |
| MMLU (EM) | 88.5 | 85.2 | **90.8** | 91.8 |
| SWE-bench Verified | — | — | **49.2** | 48.9 |

DeepSeek-R1は**AIME 2024、MATH-500、Codeforcesでo1-1217に匹敵または上回る**性能を達成。特にMATH-500の97.3%は当時のSOTA。

### 知識ベンチマーク

| Benchmark | DeepSeek-V3 | DeepSeek-R1 |
|-----------|-------------|-------------|
| MMLU | 88.5 | 90.8 |
| MMLU-Pro | 75.9 | 84.0 |
| GPQA Diamond | 59.1 | 71.5 |
| SimpleQA | 24.9 | 30.1 |

RLによる推論訓練が、知識タスクにおいても顕著な改善をもたらした。

## GRPO（Group Relative Policy Optimization）

詳細は [[grpo]] を参照。概要：

- **クリティックモデル不要**: PPOと異なり、ポリシーモデルと同サイズの価値関数モデルを必要としない → メモリ・計算資源を大幅節約
- **グループ相対アドバンテージ**: G個の出力をサンプリングし、グループ内の平均・標準偏差で正規化
- **ルールベース報酬**: ニューラル報酬モデルの「報酬ハッキング」問題を回避

$$A_i = \frac{r_i - \text{mean}(r_1, r_2, \dots, r_G)}{\text{std}(r_1, r_2, \dots, r_G)}$$

## 蒸留の意義

DeepSeek-R1の蒸留結果は、以下の重要な示唆を持つ：

1. **推論能力は蒸留可能**: 大規模モデルがRLで獲得した推論パターンは、SFTによって小型モデルに転移可能
2. **パラメータ数より訓練データの質**: 1.5Bの蒸留モデルが、はるかに大規模な非推論モデルを上回る → 推論データの質が決定的
3. **RL→SFTの非対称性**: RLで推論能力を「発見」し、SFTで「転移」する非対称パイプラインの有効性を実証

## 制限事項

| 制限 | 詳細 |
|------|------|
| **言語混在** | 非英語・非中国語クエリで英語と中国語が混ざる |
| **ツール非対応** | 検索エンジン・電卓など外部ツールをネイティブに扱えない |
| **Few-shot劣化** | Few-shotプロンプトで性能が**低下**する（zero-shotが最適） |
| **ソフトウェア工学未適用** | 大規模RLはSWEタスクに未適用（評価時間が長いため） |
| **プロンプト感受性** | 出力フォーマットの指定に敏感 |

## 歴史的意義

DeepSeek-R1は、Reasoningモデル発展史におけるマイルストーン論文として以下の意義を持つ：

1. **推論の創発を実証**: 「RLが推論能力を引き出せる」ことを671Bスケールで初めて示した
2. **Nature掲載**: 産業界のAI論文がNatureに掲載される希少な事例 → 学術的厳密さが認められた
3. **GRPOの導入**: PPOの計算ボトルネック（クリティックモデル）を解消する新しいRLアルゴリズム
4. **蒸留パラダイムの確立**: 「大規模RLで発見 → SFTで小型モデルに転移」の非対称パイプライン
5. **コスト効率**: $294Kでo1クラスの推論能力を達成 → 推論モデル開発の民主化
6. **アハモーメント**: AIの自律的行動創発の象徴的瞬間として広く引用

DeepSeek-R1の推論パターンは後に[[deepseek-v3|DeepSeek-V3]]にも蒸留され、V3のポストトレーニングにおいて重要な役割を果たした。

## 関連項目

- [[entities/deepseek]] — DeepSeek企業概要
- [[deepseek-v3]] — ベースモデル（R1の起点、後にR1推論を蒸留）
- [[grpo]] — Group Relative Policy Optimization（R1で導入されたRLアルゴリズム）
- [[reasoning]] — 推論能力全般
- [[chain-of-thought]] — Chain-of-Thought推論
- [[distillation]] — 知識蒸留技術
- [[reinforcement-learning]] — 強化学習
- [[openai-o1]] — 競合推論モデル
