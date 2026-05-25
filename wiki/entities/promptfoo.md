---
title: "Promptfoo"
type: entity
created: 2026-05-25
updated: 2026-05-25
tags:
  - promptfoo
  - evaluation
  - agent-evaluation
  - tool
  - testing
sources:
  - https://www.promptfoo.dev/
  - raw/articles/2026-05-19_openai_macro-evals-for-agentic-systems.md
related:
  - macro-evals-for-agentic-systems
  - evals-for-ai-agents
status: stub
---

# Promptfoo

オープンソースの LLM / AI エージェント評価フレームワーク。エージェントレベルの lower-level eval に使用される。

## 概要

- **用途**: LLM出力・エージェント動作のルーブリックベース評価
- **ライセンス**: MIT（オープンソース）
- **Web**: [promptfoo.dev](https://www.promptfoo.dev/)

## 主要機能

- **OpenAI Agents プロバイダー**: OpenAI Agents SDK で構築されたエージェントシステムの評価をネイティブサポート
- **チャット会話評価**: マルチターン会話のグレーディング
- **ルーブリック定義**: カスタム評価基準の設定
- **CI/CD 統合**: 評価の自動化パイプライン組み込み

## OpenAI Macro Evals での使用

[[macro-evals-for-agentic-systems]] Cookbook では、5 つの lower-level ルーブリック（`final_decision_quality`, `policy_compliance_correctness`, `routing_specialist_activation`, `market_drift_awareness`, `review_appropriateness`）を Promptfoo で実装し、1000 件の合成トレースに対して pass/fail を生成。これらの lower-level シグナルが BERTopic スタイルのマクロ発見パイプラインへの入力となる。

## See Also

- [[concepts/macro-evals-for-agentic-systems]]
- [[concepts/evals-for-ai-agents]]
- [[comparisons/evals-skills]]
