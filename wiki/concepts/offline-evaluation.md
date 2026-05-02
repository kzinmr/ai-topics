---
title: "Offline Evaluation: Pre-Production Eval Pipelines for LLM Applications"
description: "Offline Evaluationは、本番環境にデプロイする前にLLMアプリケーションを体系的に評価するパイプライン。オフラインテスト、人間判定、プロダクションテレメトリの3層で構成。"
created: 2026-04-20
updated: 2026-04-20
type: concept
status: complete
depth_tracking:
 created: 2026-04-20
 target_depth: concept-level
tags:
  - evaluation
  - offline-testing
  - regression-testing
  - eval-pipeline
sources:
 - raw/articles/dspy-rlm-2026-04-20.md
 - raw/articles/llm-as-judge-scoring-bias-2026-04-20.md
related:
 - ai-evals
 - llm-as-judge
 - evaluation-flywheel
 - dspy
---

# Offline Evaluation: Pre-Production Eval Pipeline

**Offline Evaluation** は、プロダクション環境にデプロイする前にLLMアプリケーションを体系的に評価するパイプライン。「モデルvs製品」の区別非常重要。

## Model Evaluation vs Product Evaluation

| 評価タイプ | 焦点 | 目的 |
|-----------|------|------|
| **Model Evaluation** | ベースモデルの能力 | 健全性チェック（例: MMLU benchmark） |
| **Product Evaluation** | フルシステム（プロンプト、RAG、ツール、guardrails、UI） | **唯一重要な問い** |

> **重要な洞察:** 「このモデルは優れているか？」ではなく**「このシステムは正確に・安全かつ継続的にユーザーのタスクを解決するか？」**を問う。

## Three-Layer Evaluation Stack

### Layer 1: Offline Tests
- **実行タイミング:** 開発中・PR時に自動実行
- **目的:** 回帰検出、快速なフィードバック
- **ツール:** pytest, beartest, deepset haystack evaluation
- **メトリクス:** BLEU, ROUGE, exact match, regex match

### Layer 2: Human Judgment
- **実行タイミング:** リリース前・_major変更時
- **目的:** 品質保証、ニュアンス評価
- **方法:** の専門家/ユーザーの評価チーム
- **盲点:** 主観的、遅い、スケーラビリティ問題

### Layer 3: Production Telemetry
- **実行タイミング:** デプロイ後継続
- **目的:** 実際の性能監視、アラート
- **メトリクス:** error rate, latency, user feedback, task success rate

## Offline Test Design

### テストの種類

| テスト種類 | 説明 | 例 |
|-----------|------|-----|
| **Unit tests** | 単一コンポーネント | Signatureの出力フォーマット |
| **Integration tests** | コンポーネント間連携 | RAGパイプラインのretrieval→answer |
| **Regression tests** | 既存機能の壊出し | 新バージョンで以前合格のテスト |
| **Adversarial tests** | 敵対的入力への耐性 | インジェクション攻撃、プロンプト回避 |
| **Edge case tests** | 境界条件 | 空コンテキスト、例外入力 |

### テストデータの作り方

```
Golden dataset (20-50 examples) の推奨構成:
├── Happy path (40%) — 标准的な成功ケース
├── Edge cases (30%) — 境界条件、例外処理
├── Adversarial (20%) — インジェクション、強制終了
└── Ambiguous (10%) — 複数正当回答が存在する場合
```

### Evaluation Metrics Pyramid

```
        /\
       /  \     Correctness (exact match, regex)
      /----\    ------------
     /      \   Groundedness (attribution to retrieved docs)
    /--------\  ------------
   /          \ Style & Coherence (fluency, consistency)
  /------------\ ------------
 /              \ Task Success (did it solve the user's problem?)
```

## Lexical Metrics (for Regression Testing)

### BLEU/ROUGE
| Pros | Cons |
|------|------|
| 高速、一貫性 | 意味・ニュアンスをMiss |
| 参照ベースのタスクに有用 | 絶対的品質評価には不向き |
| 回帰テスト向き |  |

> **用途:** 同じ回答を生成し続けているかの確認（回帰）。品質向上の測定には不向き。

### LLM-based Metrics (for Quality Assessment)
| Pros | Cons |
|------|------|
| 意味を捕捉 | 遅い、場合により主観的 |
| 人間評価との相関が高い | プロンプト依存 |
| 新しいアプローチの評価に有用 |  |

## Integration with CI/CD

```yaml
# .github/workflows/eval.yml (概念例)
- name: Run Offline Evals
  run: |
    pytest tests/eval/ \
      --metrics=exact_match,groundedness,llm_judge \
      --golden-dataset=tests/eval/golden.jsonl \
      --fail-on-regression
```

## Offline Eval Pipeline Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Evaluation Pipeline                    │
├─────────────────────────────────────────────────────────┤
│  ┌──────────┐    ┌───────────┐    ┌────────────────┐   │
│  │ Test     │───►│ Metric    │───►│ Aggregation    │   │
│  │ Cases    │    │ Compute   │    │ & Reporting    │   │
│  └──────────┘    └───────────┘    └────────────────┘   │
│       │               │                   │             │
│       ▼               ▼                   ▼             │
│  ┌──────────┐    ┌───────────┐    ┌────────────────┐   │
│  │ Golden   │    │ LLM-as-   │    │ Regression     │   │
│  │ Dataset  │    │ Judge     │    │ Comparison     │   │
│  └──────────┘    └───────────┘    └────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Relationship to LLM-as-Judge

LLM-as-Judgeはoffline evaluationの**メトリクス計算層**で重要な役割を果たす：

| レイヤー | LLM-as-Judgeの役割 |
|---------|-------------------|
| Unit/Integration tests | 固定的評価（BLEU/ROUGE等）で十分 |
| Quality assessment | LLM-as-Judgeが必要（主観的判断） |
| Regression comparison | 前バージョンとの差分検出 |

## Best Practices

1. **Define metrics before building** — 何を測定するか明確にしてから開発開始
2. **Start with golden dataset** — 20-50の代表的なテストケースを作成
3. **Test at multiple levels** — unit/integration/e2e组合せる
4. **Automate regression detection** — PRごとに自動実行
5. **Correlate with human judgment** — offline metricsが人間評価と合っているか検証
6. **Iterate on metrics** — 実際の失敗パターンからメトリクスを改良

## See Also

- [[concepts/ai-evals]] — AI評価全般
- [[concepts/llm-as-judge]] — LLM-as-Judgeの詳細なバイアス分析
- [[concepts/evaluation-flywheel]] — 評価の継続的改善サイクル
- [[concepts/dspy]] — DSPyでのeval統合