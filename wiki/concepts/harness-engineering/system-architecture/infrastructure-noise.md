---
title: "Quantifying Infrastructure Noise in Agentic Coding Evals"
aliases:
  - infrastructure-noise
  - agentic-eval-noise
  - benchmark-infrastructure
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-architecture
  - harness-engineering
  - anthropic
  - evals
status: draft
sources:
  - "https://www.anthropic.com/engineering/infrastructure-noise"
---

# Quantifying Infrastructure Noise in Agentic Coding Evals

エージェント型コーディングベンチマークにおいて、インフラ設定のみがスコアに与える影響を定量化した調査。

## 核心洞察

> "Infrastructure configuration alone can swing agentic coding benchmark scores by up to 6 percentage points—often exceeding the narrow margins separating top models on public leaderboards."

> "An agent that writes lean, efficient code very fast will do well under tight constraints. An agent that brute-forces solutions with heavyweight tools will do well under generous ones. Both are legitimate things to test, but collapsing them into a single score without specifying the configuration makes the differences—and real-world generalizability—hard to interpret."

**インフラ設定だけでベンチマークスコアが最大6ポイント変動。これは主要モデル間の差を超える。**

## 実験結果

### Terminal-Bench 2.0（6設定: `1x`厳格 → アンキャップド）

| メトリクス | 1x | 3x | uncapped |
|-----------|-----|-----|----------|
| インフラエラー率 | 5.8% | 2.1% | 0.5% |
| 成功率変動 | - | p=0.40（有意差なし） | +6pp (p<0.01) |

- `1x → 3x`: 一過性のOOMキルを吸収するだけで、タスクを容易にはしない
- `3x → uncapped`: 成功率が約4ppジャンプ。インフラエラーは1.6ppのみ減少。**インフラが新しい解決経路を可能にする**

### SWE-bench Crossover（RAM最大`5x`ベースライン）

- 同じ単調増加だが、規模は小さい: **`1x`に対して`5x`で+1.54pp**
- SWE-benchタスクは一般的にリソース集約度が低いため、期待される結果

## インフラが測定を変える方法

| リソースバンド | 評価への影響 | 測定しているもの |
|:---|:---|:---|
| **≤ `3x` ヘッドルーム** | インフラ信頼性を修正（一過性のスパイク） | スコアを人工的に inflated せずに評価を安定化 |
| **> `3x` ヘッドルーム** | 新しい解決経路を積極的に可能にする | 寛容なリソースを活用するエージェントに報酬 |

### 戦略バイアスの例（`bn-fit-modify`）
- **寛容な制限**: エージェントが`pandas`、`networkx`、`scikit-learn`をインストール → 成功
- **厳しい制限**: ポッドがインストール中にOOM。軽量な戦略（標準ライブラリ数学実装）のみ成功

> 異なるモデルはデフォルトで異なるアプローチを取る。リソース設定は、どのデフォルトが成功するかを決定し、「モデル能力」と「インフラ許容度」を混同させる。

## その他の隠れた変数

- 時間制限、クラスターヘルス、ハードウェア仕様、同時実行レベル、送信帯域幅
- **APIレイテンシ/時間帯**: パスレートがトラフィックパターンとインシデントに応じて変動
- **重要**: モデル能力とインフラ動作の境界は、単一のベンチマークスコアが示すものより曖昧

## ベンチマーク解釈への影響

> "A few-point lead might signal a real capability gap—or it might just be a bigger VM."

- **リーダーボード懐論**: `<3pp`の差は、評価設定が文書化され一致していない限り慎重に扱うべき
- 単純な二項信頼区間はすでに`1〜2pp`をカバー。インフラコンファウンダーが上に重なる
- ラボにとって: リソース割り当ては測定された能力に直接影響。再現性には標準化が重要

## 実践的提言

1. **デュアルパラメータを指定**: 評価設定は保証された割り当てとハードキル制限の両方を定義する必要がある
2. **バンドをキャリブレーション**: 床/天井スコアが統計的ノイズ内に収まるように ceiling を設定
3. **方法論を報告**: 正確なリソース倍率と施行戦略を公開
4. **インフラを第一級変数として扱う**: プロンプトフォーマットやサンプリング温度と同じ厳密さでリソース設定を文書化・制御

## 関連概念

- [[_index]] — 上位インデックス
- [[evals-skills]] — 評価スキル
- [[harness-design-long-running-apps]] — ハーネス設計
- [[ai-evals]] — AI評価の概念
