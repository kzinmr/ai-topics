---
title: "RAO (Recursive Agent Optimization)"
type: concept
aliases: ["Recursive Agent Optimization", "RAO"]
created: 2026-05-11
updated: 2026-05-11
status: L2
tags:
  - ai-agents
  - reinforcement-learning
  - inference
  - optimization
  - multi-agent
  - training
sources:
  - "[[papers/2026-05-07_2605.06639_recursive-agent-optimization]]"
  - "[[articles/2026-05-08_x-thread_apurva-gandhi-rao-recursive-agent-optimization]]"
related:
  - "[[concepts/recursive-language-models]]"
  - "[[concepts/rlm-recursive-language-models]]"
  - "[[concepts/grpo]]"
  - "[[entities/apurva-gandhi]]"
---

# RAO (Recursive Agent Optimization)

**RAO (Recursive Agent Optimization)** は、LLMエージェントが自身のコピーを再帰的に spawn し、サブタスクを委譲・調整する能力を end-to-end の強化学習で訓練する手法。CMU と Amazon AGI Labs の共同研究（2026年5月）。

## 概要

既存のマルチエージェント・再帰的エージェントシステムの多くは、事前学習済みモデルに推論時の scaffold（ラッパー）を被せたものに過ぎなかった。RAO はこの発想を逆転させ、**モデル自体を再帰的推論のために訓練する**。

RAO が訓練する「再帰的エージェント」は：
- サブエージェントを spawn し、タスクの一部を委譲できる
- 委譲されたサブエージェント自身もさらに委譲できる（深い再帰）
- 独立したサブタスクは**並列実行**可能
- 同じ単一ポリシーが実行ツリーの全ノードで動作する

## コアメカニズム

### 実行ツリー（Execution Tree）

RAO rollout は動的に生成される再帰的な実行ツリーを生成する。各ノードは1つのエージェントインスタンスに対応し、以下のサイクルを実行する：

```
Root Agent (depth=0)
├── Sub-Agent A (depth=1)
│   └── Sub-Agent A1 (depth=2)
└── Sub-Agent B (depth=1) ← Aと並列実行可能
```

### 訓練目的関数

RAO の訓練目的関数は、再帰的 rollout ツリーの**異なるレベルからサンプリングされたタスク**によるマルチタスク目的関数と見なせる。深いレベルのタスクは親タスクよりも簡単な部分問題になる傾向があり、自然なカリキュラム学習が生じる。

### クレジット割り当て（Credit Assignment）

RAO は再帰的 rollout 構造を活用し、サブタスク軌跡ごとに**構造化された密なクレジット割り当て**を提供する：
- 環境フィードバックが利用可能な場合はそれを報酬として使用
- 利用できない場合は **LLM-judge proxy** で報酬を生成
- 各ノードのエージェントは、自身のサブタスク成功と、ルートタスクへのグローバルな貢献の両方で報酬を受け取る

## 実験結果

### 主要ベンチマーク
| 指標 | 結果 |
|------|------|
| モデル | Qwen3-4B-Instruct |
| 訓練ステップ数 | **75 steps** |
| タスク | Deep Research |
| 単一エージェントベースライン比 | **+16% SR** (Success Rate) |

### 汎化能力
- モデルのコンテキストウィンドウを超えるタスクにスケール可能
- 訓練時よりも**はるかに難しいタスク**に汎化
- 問題の難易度に応じて**適応的に推論計算量を調整**（難しい問題ほど深い再帰深度に到達）

### 効率性
- 単一エージェントと比較して wall-clock time を削減（並列実行の効果）
- 訓練効率の向上（密なクレジット割り当てによる）

## RLM との関係

RAO のエージェントハーネス実装は Zhang et al. (2025) の **Recursive Language Models (RLMs)** に類似しているが、以下の重要な違いがある：

| 側面 | RLM (Zhang 2025) | RAO (Gandhi 2026) |
|------|-----------------|-------------------|
| 再帰深度 | depth=1 が限界 (Wang 2026) | depth > 1 で positive results |
| 並列実行 | 逐次的 | **非同期並列実行**をサポート |
| 訓練対象 | 言語モデル層の再帰 | エージェントの委譲・調整行動 |

## Sub-Agent / Agent Harness との関係

RAO は、Claude Code, Codex CLI, OpenCode などが sub-agent を推論時 scaffold として使う手法に対して、**モデル自体をその使い方のために訓練する**アプローチを提供する。Harness Effect（同じモデルでも harness によって 5-40pp の性能差が出る現象）の文脈では、RAO は harness の使い方そのものをモデルに学習させることで、このギャップを埋める可能性がある。

## プロジェクト情報

- **論文**: [arXiv:2605.06639](https://arxiv.org/abs/2605.06639)
- **プロジェクトページ**: https://apga.github.io/RAO
- **コード**: 近日公開予定
- **著者**: Apurva Gandhi, Satyaki Chakraborty, Xiangjun Wang, Aviral Kumar, Graham Neubig

## 今後の展望

- RAO で訓練されたモデルが実際の agent harness（Claude Code, Codex CLI 等）でどの程度のハーネス効果を示すかの評価
- より大規模なモデル（Qwen3-4B → 32B/72B）でのスケーリング
- 実世界タスク（SWE-bench, TheAgentCompany）での評価
- 深い再帰深度での安定性と制御
