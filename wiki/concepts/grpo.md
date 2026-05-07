---
title: GRPO (Group Relative Policy Optimization)
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [reinforcement-learning, grpo, reasoning, training, alignment, deepseek]
sources:
  - raw/papers/2025-01-22_2501.12948_deepseek-r1.md
  - https://arxiv.org/abs/2501.12948
---

# GRPO (Group Relative Policy Optimization)

GRPOは、[[deepseek-r1|DeepSeek-R1]]で導入された強化学習アルゴリズム。**PPO（Proximal Policy Optimization）の最大の計算ボトルネックであったクリティックモデル（価値関数）を不要にした**ことが最大の革新。

## 背景: PPOの問題点

従来のRLHFで標準的に使われるPPOは、以下の4つのモデルを必要とする：

1. **ポリシーモデル**（Policy Model）: 訓練対象
2. **リファレンスモデル**（Reference Model）: KL制約用
3. **報酬モデル**（Reward Model）: スコアリング用
4. **クリティックモデル**（Critic/Value Model）: アドバンテージ推定用 ← **これがボトルネック**

クリティックモデルはポリシーモデルと**同サイズ**である必要があり、実質的に訓練時のメモリ消費が2倍になる。671BパラメータのDeepSeek-V3クラスでは、これが実用的な障壁となっていた。

## GRPOの仕組み

### コアアイデア

クリティックモデルによる価値推定の代わりに、**同じ入力から生成した複数出力のグループ内相対比較**でアドバンテージを計算する。

### アドバンテージ計算式

各クエリ $q$ に対して、旧ポリシー $\pi_{\theta_{old}}$ から $G$ 個の出力 $\{o_1, o_2, \dots, o_G\}$ をサンプリングし、各出力の報酬 $\{r_1, r_2, \dots, r_G\}$ を計算：

$$A_i = \frac{r_i - \text{mean}(r_1, r_2, \dots, r_G)}{\text{std}(r_1, r_2, \dots, r_G)}$$

- $A_i > 0$: グループ平均より優れた出力 → 強化学習
- $A_i < 0$: グループ平均より劣る出力 → 抑制
- **グループサイズ G** は重要なハイパーパラメータ（DeepSeek-R1では大きなG値を使用）

### GRPOの目的関数

$$\mathcal{J}_{GRPO}(\theta) = \mathbb{E}\left[ \min\left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)} A_i, \ \text{clip}\left(\frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)}, 1-\epsilon, 1+\epsilon\right) A_i \right) - \beta \cdot \mathbb{D}_{KL}(\pi_\theta \| \pi_{ref}) \right]$$

- **Clipping**: PPOと同様、確率比を $[1-\epsilon, 1+\epsilon]$ にクリップし過度な更新を防止
- **KL正則化**: リファレンスモデルからの逸脱をペナルティ（$\beta$ で強度調整）

## ルールベース報酬設計

DeepSeek-R1でのGRPO実装の重要な特徴は、**ニューラル報酬モデルではなくルールベースの報酬**を使用したこと：

| 報酬タイプ | 内容 | 目的 |
|-----------|------|------|
| **正解報酬（Accuracy Rewards）** | 数学：最終解答のLeetCodeスタイル検証、コード：コンパイル＋テスト通過 | 正しい推論結果を強化 |
| **フォーマット報酬（Format Rewards）** | 思考過程が `<think>...</think>` タグ内に適切に配置されているか | 構造化された推論フォーマットを強制 |

**ニューラル報酬モデル不使用の理由**: 報酬ハッキング（reward hacking）の防止。ニューラル報酬モデルは「表面上は良質だが実際は不正解」な出力に高スコアを与える可能性がある。ルールベースなら検証可能な正解に対してのみ報酬を与えるため、この問題が生じない。

## PPOとの比較

| 側面 | PPO | GRPO |
|------|-----|------|
| クリティックモデル | **必要**（ポリシーと同サイズ） | **不要** |
| メモリ消費 | ポリシーの~2倍 | ポリシーのみ |
| アドバンテージ推定 | 価値関数（学習必要） | グループ内相対比較（計算のみ） |
| 報酬モデル | 通常ニューラル | ルールベース推奨 |
| バイアス | 価値関数の近似誤差 | グループサイズに依存 |
| スケーラビリティ | 大規模モデルでボトルネック | 大規模モデルに適する |

## 適用事例

### DeepSeek-R1 / R1-Zero

- **R1-Zero**: 全訓練をGRPO + ルールベース報酬のみで実施。推論能力の創発を達成
- **R1（Stage 2: Reasoning RL）**: 数学・コード・論理タスクにGRPOを適用
- **R1（Stage 4: General RL）**: 有用性・無害性アライメントにもGRPOを使用（この段階では報酬モデル併用）

訓練コスト: R1-ZeroのGRPO訓練は101K H800 GPU時間（$202K）で完了。

### DeepSeek-V3 ポストトレーニング

[[deepseek-v3|DeepSeek-V3]]のポストトレーニングでもGRPOが使用され、R1から蒸留された推論パターンの最適化に貢献。

## GRPOの現代的意義

1. **計算効率**: クリティックモデル不要により、大規模モデルのRL訓練の敷居を大幅に下げた
2. **推論創発**: 純粋RLによる推論能力の自律的出現を可能にした鍵技術
3. **スケーラビリティ**: モデルサイズが増大するほどPPOとの差が開く → 将来の超大規模モデル訓練での標準となる可能性
4. **実装の簡潔さ**: クリティックモデルの学習・管理が不要で、訓練パイプラインが単純化

## 制限と今後の課題

- **グループサイズGへの依存**: Gが小さいと推定の分散が大きくなる。Gが大きいとサンプリングコストが増加
- **ルールベース報酬の適用範囲**: 数学・コードなど検証可能なドメインに限定。創造的タスクではニューラル報酬モデルが必要
- **理論的保証**: PPOほどの理論的解析がまだ進んでいない

## 関連項目

- [[deepseek-r1]] — GRPOが導入された原論文
- [[deepseek-v3]] — GRPOをポストトレーニングに採用
- [[reinforcement-learning]] — 強化学習全般
- [[rlhf]] — RLHF（Reinforcement Learning from Human Feedback）
- [[ppo]] — Proximal Policy Optimization（GRPOの前身）
- [[reasoning]] — 推論能力
