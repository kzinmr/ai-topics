---
title: "LLM Training Coherence Evolution"
created: 2026-04-17
updated: 2026-04-17
tags: [concept, training, coherence, gpt2, fineweb]
aliases: ["llm training evolution", "coherence checkpoints", "training visualization"]
related:
  - concepts/reasoning-models
  - entities/andrej-karpathy
  - concepts/decoder-only-gpt
---

# LLMトレーニングにおけるコヒーレンスの進化

## 概要

LLMのトレーニング過程で、モデルがどのように「意味のあるテキスト生成」を獲得するかを追跡した実験。Karpathyの2015年RNN実験を現代のGPT-2アーキテクチャで再現し、57チェックポイントにわたるコヒーレンスの進化を可視化した。

## Giles Thomasの実験（2026-04）

**参照:** [How an LLM becomes more coherent as we train it](https://www.gilesthomas.com/2026/04/how-an-llm-becomes-more-coherent-over-training)

### トレーニング設定
- **モデル:** 163Mパラメータ（GPT-2スタイル）
- **データセット:** Hugging Face `FineWeb`（Webスクレイピングテキスト）
- **総トークン数:** ~3.2Bトークン（~12.8 GiB）
- **バッチ設定:** 96シーケンス × 1,024トークン = 98,304トークン/ステップ
- **総ステップ数:** 33,164
- **チェックポイント:** 57回（2日間で保存）
- **生成プロンプト:** `"Every effort moves you"` + 20トークン（temperature=1.0）

### コヒーレンスの進化（主要チェックポイント）

| ステップ | トークン数 | 特徴 | 例 |
|----------|-----------|------|-----|
| Pre-training | 0 | 単語は認識可能だが意味なし | `youhhhh esoteric Suns 1896ricia enormous` |
| 617 | ~60M | トークン頻度・基本構文を学習 | `you and to was, in the, a, The your of- and` |
| 1234 | ~120M | 意味の兆し、まだ破綻 | `you'll take the rest of the mainstay in all of his team` |
| 2468 | ~240M | **最初の真のコヒーレンス** | `you to a different country. For all the most part...` |
| 9255 | ~1.03B | 高度にコヒーレントだがデータセットバイアス強い | `you forward and it is important to make sure that your clients are satisfied` |
| 14191 | ~1.4B | 構造化フォーマット（箇条書き）を学習 | リスト形式での出力開始 |
| 24680-26531 | ~2.4B | 繰り返しループ・陳腐化（小モデル特有） | `complexity and complexity` |
| 27765 | ~2.7B | ドキュメントメタデータ生成を試行 | `Hip Hop: The New York Times, April 23, 2017` |
| 28382 | ~2.8B | 強い構文制御（`however`等の接続詞を正しく使用） | `you, however, towards a better future` |
| 33164 | 3.2B | 最終：コヒーレントだが注意喚起的 | `you, and you're rewarded, but not to your potential` |

### 主要知見

1. **構文学習は急速**: トレーニングの1/3程度で妥当なテキスト生成が可能に。ロス曲線は初期に急降下（構文学習の大部分は早期に完了）
2. **Plausible ≠ Correct**: 早中期のコヒーレンスは流暢だが事実誤認や陳腐化を含む。完全なトレーニングは現実へのグラウンディングに必須
3. **トークンvs文字アーキテクチャ**: Karpathyの2015年RNN実験（文字ベース）と異なり、トークンベースLLMは最初から認識可能な単語から始まり、早期コヒーレンスを加速
4. **小モデルの特性**: 繰り返しループ、フォーマット実験、データセットバイアスは統計パターン学習の自然な副産物
5. **創発的「意識」は統計的**: 初期の特定フレーズ出現はランダムなトークン衝突であり、原始的な政治的意識等ではない

## KarpathyのRNN実験との比較

Giles Thomasの実験はKarpathyの2015年RNNトレーニング進化実験を現代LLMで再実装したもの。主な違い：

| 次元 | Karpathy RNN (2015) | Giles LLM (2026) |
|------|---------------------|------------------|
| アーキテクチャ | 文字ベースRNN | トークンベースGPT-2 |
| 初期状態 | 純粋なノイズ | 認識可能な単語 |
| コヒーレンス獲得 | 段階的 | 急速（早期に構造学習） |
| データセット | シェイクスピア | FineWeb（Webテキスト） |

## 意義

この実験はLLMの「内部世界モデル」がトレーニングを通じてどのように形成されるかを可視化する稀有な例。特に以下の点で重要：

- **教育価値**: LLMが「どのように」学習するかを直感的に理解可能
- **モデル評価**: 小モデルの限界（繰り返しループ、データセットバイアス）を特定
- **トレーニングダイナミクス**: 構文学習→意味学習→現実グラウンディングの3段階を明確化
- **スケーリング法則**: コヒーレンスの質的変化はトレーニング量の関数として予測可能

## 関連

- [[concepts/reasoning-models]] — 推論能力の進化
- [[entities/andrej-karpathy]] — オリジナルRNN実験
- [[concepts/decoder-only-gpt]] — GPT-2アーキテクチャ
- [[concepts/illusion-of-thinking]] — コヒーレンスと思考の区別

## ソース

- Giles Thomas, ["How an LLM becomes more coherent as we train it"](https://www.gilesthomas.com/2026/04/how-an-llm-becomes-more-coherent-over-training), 2026-04-17
- Andrej Karpathy, ["The Unreasonable Effectiveness of Recurrent Neural Networks"](https://karpathy.github.io/2015/05/21/rnn-effectiveness/), 2015-05-21
