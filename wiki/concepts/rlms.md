---
title: "RLMs: Recursive Language Models"
description: "RLMs（再帰的言語モデル）は、LLMが自身のコンテキストを再帰的に読み書きすることで推論時に自己最適化を行うパラダイム。DSPyとは異なり訓練データ不要で、10M+トークンコンテキスト處理が可能。"
created: 2026-04-20
updated: 2026-04-20
type: concept
status: emerging
depth_tracking:
 created: 2026-04-20
 target_depth: concept-level
tags:
  - llm-architecture
  - inference
  - self-optimization
  - context-management
sources:
 - raw/articles/rlms-recursive-language-models-2026-04-20.md
 - raw/articles/gepa-iclr2026-2026-04-20.md
related:
 - dspy
 - gepa
 - context-engineering
 - inference-time-scaling
---

# Recursive Language Models (RLMs)

**RLMs** (Recursive Language Models) は、LLMが自身のコンテキストを**再帰的に読み書き**することで推論時に自己最適化を行う新しいパラダイム。Alex L. Zhang, Tim Kraska, Omar Khattabによる2025年のpreprintで提案。

## Core Concept

従来のLLM usage:
- コンテキストは**固定**（プロンプト構築時に決定）
- 推論中にコンテキストは変化しない
- 最適化は**コンパイル時**（DSPy等）または**訓練時**

RLMs:
- LLMが**自身の生成した中間出力を読み取る**
- 計算された表現をコンテキストに**書き込む**
- **自己フィードバックループ**を通じて出力を再帰的に改善

## The RLM Mechanism

RLMsは**Python風のコード**を生成・実行することで動作：

```python
# RLMが生成するコード（概念図）
context = read_context()           # これまでの全コンテキストにアクセス
new_repr = compute(context)        # モデルが処理・表現を生成
write_context(new_repr)            # 次ステップのために書き戻し
continue_generation()              # 再帰的に継続
```

**従来のtool-useとの区别:** RLMは外部APIを呼ぶのではなく、**自身の処理コンテキスト自体を変更する**。

## Key Properties

| Property | 説明 |
|----------|------|
| **Optimization timing** | 推論時（训练データ不要） |
| **Context management** | 動的再帰的アクセス |
| **Control主体** | LM itself（コード生成 통해自己制御） |
| **Data requirements** | なし（ゼロショット） |
| **Replayerability** | 低（推論時の非決定性） |
| **Context scale** | 10M+ トークン处理可能 |

## DSPy vs RLMs: Fundamental Distinction

| 次元 | DSPy | RLMs |
|------|------|------|
| **最適化タイミング** | コンパイル時（訓練データ必要） | 推論時（ゼロショット） |
| **コンテキスト管理** | 固定プロンプト＋デモンストレーション埋め込み | 動的再帰的アクセス |
| **制御主体** | 外部Teleprompter | LM itself（コード生成） |
| **データ要件** | 10-50+ 訓練例 | なし |
| **再計算可能性** | **高い**（コンパイル結果は決定論的） | 低（推論時非決定性） |
| **適用シナリオ** | 反復的パイプライン（QA, RAG, 分類） | 長文コンテキスト（10M+）、深層推論 |
| **コンテキスト上限** | プロンプトサイズ制約 | 再帰で突破了可能 |

## Shared Philosophy

DSPyもRLMsも以下の原則を共有する：

> **"Language Model is the module, not the product."** (Khattab)

ただし最適化へのアプローチが異なる：

| | DSPy | RLMs |
|--|------|------|
| LMの捉え方 | **学習可能な関数** (like neural network) | **再帰的プロセッサ** (like Turing machine) |
| 最適化方法 | 訓練データでプロンプトをコンパイル | 推論時にコンテキストを自己操作 |

## When to Use RLMs vs DSPy

**Use RLMs when:**
- 訓練データが利用できない
- 深層的な多段推論が必要
- コンテキストが非常に長い（10M+ tokens）
- ゼロショット適応が欲しい
- 実行時に動的に最適化したい

**Use DSPy when:**
- 訓練データがある（10-50+ examples）
- タスクが反復的（同じパターンを繰り返す）
- 再現性が重要
- コスト-品質トレードオフを最適化したい

## Relationship to GEPA

GEPAとRLMsはKhattab研究の補完的な方向性：

| | GEPA | RLMs |
|--|------|------|
| **タイミング** | コンパイル時 | 推論時 |
| **方法** | 遺伝的アルゴリズム（世代を跨ぐ） | 再帰的自己最適化（実行中） |
| **最適化対象** | プロンプト文本体 | コンテキスト表現 |
| **サンプル効率** | 高い（GRPO比35x） | 最高（ゼロショット） |

**将来の統合可能性:** GEPAで初期プロンプトを最適化し、RLMsで実行時に動的改良を行う——というハイブリッドアプローチが考えられる。

## Research Pipeline (Khattab Group 2025-2026)

```
DSPy (宣言的プログラミング)
  ├── GEPA (遺伝的プロンプト最適化) → ICLR 2026 Oral
  ├── RLMs (再帰的コンテキスト処理) → Preprint 2025
  └── Multi-module GRPO (RL + プロンプト最適化統合)
       │
       └──► 未来の統合: GEPA-initialized + RLM dynamic refinement
```

## Open Questions

1. RLMsの非決定性をどのように制御するか
2. 再帰深度と性能の관계（何处で収益逓減するか）
3. GEPAとRLMsの統合方法
4. 長コンテキストにおけるmemory footprint管理

## See Also

- [[concepts/dspy]] — RLMsと比較される宣言的LMプログラミングフレームワーク
- [[concepts/gepa]] — Khattabの別研究方向（コンパイル時最適化）
- [[concepts/context-engineering]] — コンテキスト管理全般
-  — 推論時スケーリングの別の視点