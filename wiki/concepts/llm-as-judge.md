---
title: "LLM-as-Judge: Evaluation Frameworks, Best Practices & Bias Types"
description: "LLM-as-JudgeはLLMを使用してLLM出力を評価するパラダイム。3つのバイアス类型（ルーブリック順序、スコアID、参照解答）と7つのベストプラクティスを整理。高リスク評価にはGPT-4oクラスが必要。"
created: 2026-04-20
updated: 2026-04-20
type: concept
status: complete
depth_tracking:
 created: 2026-04-20
 target_depth: concept-level
tags: [llm-evaluation, ai-evals, bias-mitigation, rubric-design]
sources:
 - raw/articles/llm-as-judge-scoring-bias-2026-04-20.md
 - raw/articles/dspy-rlm-2026-04-20.md
related:
 - ai-evals
 - evaluation-flywheel
 - offline-evaluation
 - dspy
---

# LLM-as-Judge: Evaluation Frameworks & Bias Mitigation

**LLM-as-Judge** は、LLMを使用してLLM出力を評価するパラダイム。比較評価（pairwise）よりも**スコアリング評価（absolute scoring）**が産業用途では実用的だが、3種類のバイアスに影響される。

## Three Scoring Biases (Li et al., 2025)

### 1. Rubric Order Bias（ルーブリック順序バイアス）

スコアの説明順序が判断に影響する：

| 順序タイプ | 効果 |
|-----------|------|
| Ascending-Numeric (1→5) | conventional — モデルは中央値に集まる傾向 |
| Descending-Numeric (5→1) | **より正確** — 人間の評価との整合性が高い |
| Random-Numeric | **最も悪い** — 論理的整合性が崩れ |

> **発見:** 上から下にスコアが下がるDescending順が、上げたスコアほど詳細説明つける構造と一致するため、より論理的。

### 2. Score ID Bias（スコアIDバイアス）

同じ値を異なる記号的表現で書くと評価が変わる：

| 記号的表現 | 効果 |
|-----------|------|
| Arabic numerals (1,2,3,4,5) | conventional — GPT-4oで中程度の精度 |
| Letter-grades (E,D,C,B,A) | **DeepSeek-V3-671Bで精度向上** |
| Roman numerals (i,ii,iii,iv,v) | **GPT-4oで精度向上** |

### 3. Reference Answer Score Bias（参照解答バイアス）

参照解答に特定のスコアを添付すると評価が歪む——**最も危险的**：

| 参照スコア | 影響 |
|-----------|------|
| Ref-5 (満点) | **最も安定、最も正確** |
| Ref-1 to Ref-4 | 不安定、歪み大 |

> **実験結果:** GPT-4oでRef-5参照使用時、Flip Rate 45.54% — ほぼ半数のスコアが扰乱される

## Model Robustness差异

| モデル | Flip Rate (最大) | MAD (最大) | 推奨シナリオ |
|--------|-----------------|------------|-------------|
| GPT-4o | <25% | <0.3 | 高リスク評価 |
| DeepSeek-V3-671B | 中程度 | 中程度 | 中リスク評価 |
| Qwen3-8B | **46.22%** | **0.5296** | 低リスク評価のみ |

## 7 Best Practices for LLM-as-Judge

### 1. Ditch the 1-10 Scale
- 離散的な小さなスケール（2-5段階）を 선호
- 1-10は粒度が細すぎて不安定

### 2. Start with Human Labels
- 評価を真空状態で始めない
- 人間の基底値（ground truth）でバリデーション

### 3. Choose Judge Model Carefully
- **高リスク評価:** GPT-4o classを使用
- 小さいモデルは低リスク評価のみ

### 4. Write Explicit Rubrics
- 曖昧さのない明確な基準
- 各スコアレベルの具体的条件

### 5. Prefer Decision-Based Checks
- DAG/QAG (Question-Answer Generation) がfree-form scoringより安定
- バイナリ判定 > 5段階スケール > 10段階スケール

### 6. Use Ensembles
- 複数のJudgeで多数決/平均
- 単一Judgeより頑健

### 7. Validate Against Human Baselines
- 展開前に人間の評価と照合
- バイアス補正プロシージャを適用

## Evaluation Framework Types

### A. Multiple-Choice Benchmarks
| Pros | Cons |
|------|------|
| 高速、能力比較に有用 | 自由回答には不向き |
| トレンド把握に有用 | 推論チェーンを測定しない |
| 実行が容易 | 実世界タスク成功を測定しない |

### B. Verifiers (Programmatic Grading)
- 客観的検証可能な回答（数学、コード、構造化出力）に適する
- 中間ステップも評価可能
- **欠点:** verifier構築に多大な工数

### C. Human Preference Leaderboards
| Pros | Cons |
|------|------|
| スタイル偏好を捕捉 | が高コスト |
| 有用性を測定 | 正しさを直接測定しない |
| 安全性を暗黙的に測定 | 迭代サイクルが遅い |

### D. LLM-as-Judge（今回分析対象）
| Pros | Cons |
|------|------|
| スケールしやすい | Judgeの質に依存 |
| 柔軟なルーブリック設計 | ルーブリック設計が重要 |

## Bias Mitigation Summary

| テクニック | 推奨度 | 効果 |
|-----------|--------|------|
| Descending rubric order | ★★★ | 精度向上 |
| Roman numerals (for GPT-4o) | ★★★ | 精度向上 |
| Letter grades (for DeepSeek) | ★★★ | 精度向上 |
| Full-mark reference answers | ★★★ | 安定性向上 |
| Random rubric order | ★ | 非推奨 |
| Low-scored references | ★ | 非推奨 |
| Stronger judge model | ★★★ | 基本的には常に使用 |

## Integration with DSPy

DSPyの文脈では、LLM-as-Judgeはteleprompterのmetricsとして使用される：

```python
import dspy

# LLM-as-judge metricの定義
class JudgeQuality(dspy.Signature):
    """Evaluate response quality on criteria."""
    response = dspy.InputField()
    score = dspy.OutputField(desc="1-5 rating")

judge = dspy.Predict(JudgeQuality)

# メトリクスとして使用
def quality_metric(example, pred, trace=None):
    result = judge(response=pred.response)
    return int(result.score) >= 4
```

## See Also

- [[concepts/ai-evals]] — 評価全般の概念ページ
- [[concepts/evaluation-flywheel]] — 評価の反復的改善サイクル
- [[concepts/offline-evaluation]] — プロダクション前評価パイプライン
- [[concepts/dspy]] — DSPyでの評価統合
- [[comparisons/eval-tools-comparison]] — 評価ツール比較