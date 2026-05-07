---
title: "Predictive $\mathcal{V}$-Information"
aliases:
  - V-Information
  - Predictive V-Information
  - 予測的V-情報
  - Usable Information Under Computational Constraints
tags:
  - information-theory
  - representation-learning
  - fairness
  - structure-learning
  - theory
created: 2026-05-08
updated: 2026-05-08
sources:
  - "raw/papers/2020-02-25_2002.10689_predictive-v-information.md"
related:
  - "concepts/representation-learning"
  - "concepts/fairness"
---

# Predictive $\mathcal{V}$-Information

**Predictive $\mathcal{V}$-Information** は、観測者（observer）の計算能力やモデリング能力の制約を明示的に考慮した情報理論の枠組み。Shannon情報理論の変分拡張として、Yilun Xu, Shengjia Zhao, Jiaming Song, Russell Stewart, Stefano Ermon によって2020年に提案され、ICLR 2020で発表された[^1]。

## 概要

従来のShannon情報理論は、情報の**物理的な存在**を測る。これは観測者が無限の計算能力を持つことを前提としており、現実の機械学習システム（ニューラルネットワークなど）の振る舞いを説明するには不十分だった。

Predictive $\mathcal{V}$-Information は、観測者の能力を特定の関数族 $\mathcal{V}$ に制限することで、「その観測者にとってどの程度情報が**利用可能か**」を定量化する。

| 観点 | Shannon情報 | Predictive $\mathcal{V}$-Information |
|------|-------------|-------------------------------------|
| **観測者** | 全能（無限の計算能力） | 制約あり（関数族 $\mathcal{V}$） |
| **データ処理不等式(DPI)** | 常に成立（情報は生成されない） | **違反可能**（計算が利用可能な情報を生成する） |
| **対称性** | 対称（$I(X;Y) = I(Y;X)$） | 非対称（$I_{\mathcal{V}}(X \to Y) \neq I_{\mathcal{V}}(Y \to X)$） |
| **推定** | 高次元では困難 | PAC保証ありで信頼性高く推定可能 |
| **用途** | 通信の理論限界 | 実用的な機械学習と公平性 |

## 定義

### $\mathcal{V}$-Entropy（$\mathcal{V}$-エントロピー）
特定の関数族 $\mathcal{V}$ に属するモデルを使って、目的変数 $Y$ を予測する際の最小期待損失（不確実性）：

$$H_{\mathcal{V}}(Y) = \inf_{f \in \mathcal{V}} \mathbb{E}[L(f, Y)]$$

### Conditional $\mathcal{V}$-Entropy（条件付き$\mathcal{V}$-エントロピー）
入力 $X$ を観測した後、関数族 $\mathcal{V}$ のモデルを使って $Y$ を予測する際の残存不確実性：

$$H_{\mathcal{V}}(Y|X) = \inf_{f \in \mathcal{V}} \mathbb{E}[L(f(X), Y)]$$

### $\mathcal{V}$-Information（$\mathcal{V}$-情報量）
両者の差として定義される：

$$I_{\mathcal{V}}(X \to Y) = H_{\mathcal{V}}(Y) - H_{\mathcal{V}}(Y|X)$$

## 理論的意義

### DPI（データ処理不等式）の違反

Shannon理論では、データを処理する（変換する）ことで情報が増えることはない（$I(X;Y) \ge I(g(X);Y)$）。しかし $\mathcal{V}$-Information では、**計算によって利用可能な情報が増加する**：

$$I_{\mathcal{V}}(g(X) \to Y) \ge I_{\mathcal{V}}(X \to Y)$$

これは深層ニューラルネットワークが層を重ねるごとに、より線形分離可能で「使いやすい」特徴表現を抽出する現象を説明する。生データでは観測者 $\mathcal{V}$ が扱えなかった情報も、適切な変換 $g$ によって「利用可能」になる。

### PACスタイルの推定保証

Shannon相互情報量は高次元の連続変数に対して推定が非常に難しい。一方 $\mathcal{V}$-Information は観測者の関数族を制限することで、有限データからの信頼性の高い推定が可能になる。

### 既存指標の一般化

| 指標 | 特殊ケースとしての条件 |
|------|----------------------|
| **Shannon相互情報量** | $\mathcal{V}$ がすべての可測関数の集合 |
| **決定係数 $R^2$** | $\mathcal{V}$ が線形モデルの集合 |

## 応用

### 1. 構造学習（Structure Learning）

変数間の依存関係を学習する際に、特定のモデルクラスが実際に活用できる依存関係を特定できる。従来の相互情報量よりも現実的な因果グラフ構築が可能。

### 2. 公平な表現学習（Fair Representation Learning）

公平性の文脈では、表現 $Z$ が機密属性 $S$ についてどの程度の情報を持つかを最小化したい。$\mathcal{V}$-Information を用いれば、「特定の限定的な敵対者では抽出できない」という現実的な基準で公平性を保証できる。Shannon情報量では「全能の敵対者」を仮定するため過度に制約的になる。

### 3. 深層表現学習（Deep Representation Learning）

深層ネットワークの層が進むにつれて特徴がより「線形分離可能」になる現象を理論的に説明する。Shannon情報量では層を経るごとに一定または減少する情報が、$\mathcal{V}$-Information では増加する理由を定式化する。

## 関連概念との比較

| 概念 | 関係 |
|------|------|
| **Shannon情報理論** | 親理論。$\mathcal{V}$-Information はその変分拡張であり、$\mathcal{V}$ を全ての可測関数にするとShannon相互情報量に一致 |
| **決定係数 $R^2$** | $\mathcal{V}$-Information の特殊ケース（線形モデル族に制限） |
| **情報ボトルネック（IB）** | 関連するが別の手法。IBは圧縮と予測のトレードオフを扱い、$\mathcal{V}$-Information は観測者の制約に焦点 |
| **変分情報理論（Variational Information Theory）** | 広い枠組みの一部。$\mathcal{V}$-Information は変分下界を用いた情報量の実用的推定を提供 |

## 参考文献

[^1]: Xu et al., "A Theory of Usable Information Under Computational Constraints", ICLR 2020. https://arxiv.org/abs/2002.10689

## 関連項目

- [[concepts/representation-learning]] — 表現学習の理論的基盤として
