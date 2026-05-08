---
title: "Claude Think Tool"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - claude
  - tool-use
  - agent-architecture
  - reasoning
  - evaluation
aliases:
  - think tool
  - Claude think tool
  - stop-and-think tool
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_claude-think-tool.md
  - https://www.anthropic.com/engineering/claude-think-tool
related:
  - claude-code
  - agent-skills
  - advanced-tool-use
---

# Claude Think Tool

Claudeの「think」ツールは、複雑なタスク中に構造化された思考のための専用スペースを提供するツール。長いツール呼び出しチェーンや複数ステップの会話で、Claudeが外部情報を処理し、次のアクションの前に立ち止まって考えることを可能にする。

## Extended Thinking との違い

| | Think Tool | Extended Thinking |
|---|---|---|
| **タイミング** | レスポンス生成**中**（ツール呼び出しの合間） | レスポンス生成**前** |
| **対象** | 外部情報（ツール結果）の処理 | クエリ単体からの深い推論 |
| **推論の深さ** | 新しい情報に焦点を絞った軽量推論 | 包括的で深い事前検討 |
| **適した用途** | 複雑なツールチェーン、ポリシー重視環境 | コーディング、数学、物理（非ツール） |

## 実装

```json
{
  "name": "think",
  "description": "Use the tool to think about something...",
  "input_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "A thought to think about."
      }
    },
    "required": ["thought"]
  }
}
```

τ-Benchの標準環境の一部として組み込まれている。

## ベンチマーク結果 (τ-Bench)

**評価指標**: pass^k（全k回の独立試行が成功する確率をタスク間で平均）— 一貫性と信頼性を測定。

### Airline Domain (Claude 3.7 Sonnet)

| 設定 | pass^1 | pass^2 | pass^3 |
|------|--------|--------|--------|
| Baseline | 0.332 | 0.206 | - |
| Extended Thinking | 0.412 | 0.290 | 0.232 |
| Think Tool | 0.404 | 0.254 | 0.186 |
| **Think Tool + Optimized Prompt** | **0.584** | **0.444** | **0.384** |

- Think tool + 最適化プロンプトで **baseline比 +54%** の改善
- 単独でも Extended Thinking と同等の性能

### Retail Domain

- Think tool単独: 0.812 vs Baseline 0.783

## 推奨ユースケース

- **複雑なツール呼び出し**: 長いツールチェーンで各結果を分析する必要がある場合
- **ポリシー重視環境**: 詳細なガイドラインに従う一貫性が求められる場面（カスタマーサービス等）
- **逐次的意思決定**: 各ステップが前のステップに依存し、ミスがコスト高な場面

## 現状

2025年12月時点で、AnthropicはExtended Thinkingの改善により、ほとんどのケースでthink toolよりもExtended Thinkingの使用を推奨している。ただし、ツール結果の逐次処理が必要なケースではthink toolに優位性が残る。

## See Also

- [[claude-code]] — Claude Code agent harness
- [[agent-skills]] — Equipping agents with skills
- [[advanced-tool-use]] — Advanced tool use patterns
- [[effective-harnesses-for-long-running-agents]] — Long-running agent harnesses
