---
title: "Activation Steering (Feature Steering)"
type: concept
aliases:
  - feature steering
  - activation engineering
  - representation engineering
created: 2026-05-08
updated: 2026-05-08
tags:
  - interpretability
  - steering
  - llm
  - inference
  - safety
  - rlhf-alternative
related:
  - concepts/interpretability
  - concepts/monosemanticity
  - concepts/rlhf
  - concepts/abliteration
  - concepts/entropix
  - entities/thariq-shihipar
  - entities/anthropic
sources:
  - raw/articles/thariq-shihipar-interpretability
  - https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
  - https://www.anthropic.com/news/golden-gate-claude
  - https://thesephist.com/posts/prism/
---

# Activation Steering（Feature Steering）

**Activation Steering**とは、LLMの推論時に特定の内部特徴（feature）の活性化強度を操作することで、モデルの振る舞いを直接制御する技術。特徴の「増幅（amplify）」と「抑制（suppress）」によって、プロンプトでは達成できない粒度の制御を可能にする。

> **Thariq Shihiparの比喩**: Steering is like brain surgery; prompting is like asking politely.（Steeringは脳外科手術、プロンプトは丁寧にお願いすること）

## 仕組み

```
[入力] → [通常のforward pass] → [特徴Aの活性化を検出]
                                      ↓
                              [特徴Aを2xに増幅 / 特徴Bを0xに抑制]
                                      ↓
                              [介入されたactivation] → [出力]
```

1. **特徴抽出**: Sparse Autoencoder（SAE）で内部表現をdisentangleし、数百万の解釈可能な特徴に分解する（AnthropicのScaling Monosemanticity, 2024）
2. **特徴の特定**: 操作したい振る舞いに対応する特徴を見つける（例：「詐欺メール」特徴、「簡潔さ」特徴）
3. **介入（Intervention）**: 特徴のactivationに係数（clamping factor）を掛けて増幅/抑制する
4. **推論継続**: 介入後のactivationで生成を続行する

## 主な応用

### 1. スタイル・ペルソナ制御
プロンプトで「親切で簡潔に」と指示するのではなく、「親切さ特徴を70%、簡潔さ特徴を50%」のように連続値で制御。言葉で記述しきれないニュアンスを実現。

- **Goodfire.ai**: Llamaモデル向けの特徴操作ツール。検出された特徴に基づいてsteeringを行う
- **Prism (Linus Lee)**: テキスト埋め込み分類器を学習させてテキスト生成をsteering

### 2. RLHFの補完・代替
RLHFは全ユーザー一律のpost-training処理だが、steeringは**推論時に開発者ごとの選択的操作**が可能。

| 次元 | RLHF | Activation Steering |
|------|------|---------------------|
| タイミング | Post-training（固定） | 推論時（動的） |
| 粒度 | モデル全体 | 特徴単位 |
| 副作用 | false refusals, quality degradation | 特徴過剰増幅による分布外出力 |
| 制御権 | モデル提供者 | API開発者 |

### 3. ユーザー嗜好の永続化
会話中の「簡潔に答えて」という嗜好はcontext windowから外れると失われる。steeringなら簡潔さ特徴を永続的に増幅することで、会話の長さに関係なく嗜好を保持できる。

### 4. 安価な分類器
スパム検出などの分類を、別モデルを学習せずに実現。スパム/非スパムメール群で活性化する特徴のパターン差分を調べ、「スパム特徴セット」を構築することで推論時の分類器として機能。

## Golden Gate Claude（Anthropic, 2024）

最も有名な実証例。Golden Gate Bridge特徴のclamping factorを極端に上げると、Claudeは自分がGolden Gate Bridgeであるかのように振る舞い始めた。

このデモが示した重要な洞察：
- 特徴は実際にモデルの振る舞いを因果的に制御している（相関ではなく因果）
- 過剰な増幅はモデルを「分布外」に追いやる — テキストの一貫性が崩れる
- 「正しい」増幅の度合いを見つけることが実用化の鍵

## 実用上の課題

### 分布外（OOD）問題
特徴を強く増幅しすぎると、モデルは学習分布から外れ、非文法的・支離滅裂な出力を生成する。これは単なる「Golden Gate Bridgeの話をしすぎる」という問題を超えて、**言語そのもののルールに従わなくなる**問題。

### 特徴ラベルの不完全性
数百万の特徴に対して人間＋機械でラベルを付与するため、誤分類や誤解のリスクがある。Shihiparは「特徴リストを見て、ラベルに同意できないことがある」と指摘。

### 回路の予期せぬ活性化
特徴は孤立しているわけではなく、他の特徴と「回路（circuit）」を形成している。ある特徴の操作が予期せぬ連鎖反応を起こす可能性があり、これはRLHFの副作用と本質的に同じ問題。

### 未検証のスケーラビリティ
Anthropicの内部利用を除けば、広範なプロダクション環境での実績はまだない。大規模展開時の振る舞いは未知数。

## Abliteration — 拒否反応の除去

Activation Steeringの特定の応用として、**Abliteration**（mlabonne, 2024）はRLHFで埋め込まれた拒否反応（refusal）を特徴方向の操作で「無検閲化」する：

1. 拒否応答を引き起こすテキスト群と、通常応答のテキスト群で活性化パターンを比較
2. 「拒否方向（refusal direction）」を特定
3. その方向の成分を活性化から差し引く
4. → モデルは拒否しなくなる（が、RLHFの他の恩恵も一部失う可能性あり）

## 開発上の位置づけ

Activation Steeringは、LLM APIの次の進化を示唆する。2024年まではプロンプト＋RAGが開発者の主な制御手段だったが、steeringの成熟により、開発者は**モデル内部への直接的な制御インターフェース**を得る可能性がある。

Shihiparは「次世代のモデルAPIは、より強力になるがより複雑にもなる。プロンプトとRAGだけでは望む出力を得られなくなる」と予測する。

## 関連概念

- [[concepts/interpretability]] — 解釈可能性全般。Steeringはその応用面
- [[concepts/rlhf]] — 従来の制御手法。Steeringの補完対象
- [[concepts/entropix]] — 不確実性検出。Steeringと同様に推論時介入の一種
- [[concepts/scaling-hypothesis]] — スケールによる制御性の低下。Steeringはその対策

## 参照

- [Scaling Monosemanticity (Anthropic, May 2024)](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)
- [Golden Gate Claude (Anthropic, 2024)](https://www.anthropic.com/news/golden-gate-claude)
- [Prism: Steering text generation (Linus Lee)](https://thesephist.com/posts/prism/)
- [Abliteration: uncensoring LLMs (mlabonne, 2024)](https://huggingface.co/blog/mlabonne/abliteration)
- [Goodfire.ai — feature steering for Llama](https://goodfire.ai)
