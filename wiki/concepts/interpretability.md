---
title: "Interpretability (LLM)"
type: concept
aliases:
  - mechanisitic interpretability
  - AI interpretability
created: 2026-05-08
updated: 2026-05-08
tags:
  - interpretability
  - model
  - agent-safety
  - steering
  - activation-engineering
related:
  - concepts/activation-steering
  - concepts/monosemanticity
  - concepts/rlhf
  - concepts/abliteration
  - entities/anthropic
  - entities/thariq-shihipar
sources:
  - raw/articles/thariq-shihipar-interpretability
  - https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
  - https://www.anthropic.com/news/golden-gate-claude
  - https://thesephist.com/posts/prism/
---

# Interpretability (LLM)

**Interpretability**とは、LLMの内部で「何が起きているか」を理解しようとする研究分野。モデルが「考えている」ことを可視化し、具体的な特徴（feature）や回路（circuit）として説明することを目指す。

> **一言で**: LLMのブラックボックスを開けて、中の歯車を見えるようにする営み。

## 背景：なぜ解釈可能性なのか

LLMの性能が指数関数的に向上するにつれて、「モデルがなぜその出力をしたのか」を説明できないことが、安全性と信頼性の最大のボトルネックになっている。プロンプトで望む出力を得られても、モデル内部で実際に何が起きているかは不明のまま。

[[concepts/scaling-hypothesis]]が示す通り、モデルが賢くなるほど人間が設計した「構造」が消えていき、内部の説明可能性は低下する。解釈可能性研究は、この**性能と制御性のトレードオフ**に正面から取り組む試みである。

## 主要なアプローチ

### Feature Extraction（特徴抽出）
LLMの内部表現（activation）を「特徴」に分解する。各特徴は特定の概念に対応する（例：「Golden Gate Bridge」「アラビア語」「詐欺メール」）。

- AnthropicのSparse Autoencoder（SAE）による特徴分解が代表的
- 数百万の特徴を抽出し、それぞれが何を表すかラベル付けする
- 同じ入力に対しては、同じ特徴が信頼性高く活性化する

### Circuit Analysis（回路解析）
複数の特徴がどう接続し、相互作用するかを追跡する。特定の能力（数学的推論、コード生成など）の背後にある「計算回路」を特定する。

### Activation Steering（活性化操作）→ [[concepts/activation-steering]]
特定の特徴の活性化強度を操作することで、モデルの振る舞いを制御する技術。解釈可能性の「理解する」側面から「制御する」側面への応用。

## ランドマーク

| 年 | 成果 | 意味 |
|----|------|------|
| 2023 | Anthropic, 「Toy Models of Superposition」 | 特徴が重ね合わさっていることを理論化 |
| 2024.3 | Anthropic, 「Scaling Monosemanticity」 | Claude 3 Sonnetから数百万の解釈可能な特徴を抽出 |
| 2024.5 | Golden Gate Claude | 特定の特徴を増幅するとClaudeがその「人格」になることを実証 |
| 2024.10 | Entropix（XJDR, 解説：Thariq Shihipar） | エントロピー/バレントロピーによる不確実性検出 |
| 2024.11 | Goodfire.ai | Llamaモデル向けの特徴操作ツール |
| 2025 | Abliteration (mlabonne) | RLHF拒否反応を特徴方向の削除で「無検閲化」 |

## 開発者にとっての意義

Thariq Shihiparは「Should Developers Care about Interpretability?」（2024.11）で、解釈可能性が単なる学術的興味ではなく実用的なエンジニアリングツールであることを以下の応用で示している：

1. **言葉で記述できないスタイルの制御**: 「70%親切、50%簡潔、80%プロフェッショナル」のようなニュアンス
2. **RLHFの副作用回避**: 推論時の選択的操作で、全ユーザー一律のRLHF後処理を回避
3. **ユーザー嗜好の永続的記憶**: 会話が長くなると失われる「簡潔に答えて」のような嗜好を特徴操作で保持
4. **安価で再現性のある分類**: スパム検出などを、別モデルを学習せずに特徴活性化パターンで実現

## 制約と課題

- **分布外への逸脱**: 特徴の過剰増幅はモデルを「言語のルールに従わない」状態にしうる（brain surgery vs プロンプトは「丁寧にお願いする」こと）
- **特徴ラベルの信頼性**: 人間＋機械によるラベリングは誤分類のリスクがある
- **回路の副作用**: ある特徴の操作が予期せぬ他の特徴・回路を活性化する可能性（RLHFと同様の問題）
- **広範な実用化は未達**: Anthropicの内部利用を除き、本格的なプロダクション活用事例は限定的

## 関連概念

- [[concepts/activation-steering]] — 特徴操作の具体的技術
- [[concepts/scaling-hypothesis]] — スケールと制御性のトレードオフ
- [[concepts/rlhf]] — 従来の制御手法。steeringはその補完/代替を目指す
- [[concepts/entropix]] — 不確実性検出による適応的サンプリング

## 参照

- [Scaling Monosemanticity (Anthropic, 2024)](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)
- [Golden Gate Claude (Anthropic, 2024)](https://www.anthropic.com/news/golden-gate-claude)
- [Prism: Steering text generation (Linus Lee)](https://thesephist.com/posts/prism/)
- [Should Developers Care about Interpretability? (Thariq Shihipar, 2024)](https://www.thariq.io/blog/interpretability/)
