---
title: Agreement is a Bug
type: concept
created: 2026-04-27
updated: 2026-04-27
status: L2
sources: [https://x.com/nyk_builderz/status/2041091619848634661, https://x.com/nyk_builderz/status/2037870116059201828, https://x.com/nyk_builderz/status/2038519372541730819]
tags:
  - anthropic
  - multi-agent
  - disagreement
  - subagents
  - architecture-evaluation
  - diversity-of-perspective
aliases: [structured-disagreement, claude-code-subagent-disagreement]
---

# Agreement is a Bug

NYK Builderz (@nyk_builderz) が2026年3月に公開した、**Claude Codeサブエージェントの「構造化された不一致」フレームワーク**。

## Core Thesis

> 「合意はバグである」

40以上のアーキテクチャ・戦略判断をClaude Codeでテストした結果、**最大の失敗は「間違った答え」ではなく「単一視点からの盲点」**であった。

## The Problem with Single-Agent AI

単一エージェントでの判断には根本的な制限がある:

1. **システムバイアス**: システムプロンプトが分析の方向性を固定する
2. **盲点の集中**: 一つのモデル/プロンプトは必ず特定の盲点を持つ
3. **合意のIllusion**: エージェントが合意するのは「正しいから」ではなく「同じ視点だから」

## The Solution: Structured Disagreement

11のClaude Codeサブエージェントを並列起動し、**合意する前に強制的に不一致を生成**:

| 要素 | 説明 |
|------|------|
| **11 Perspectives** | 歴史的な思想家/設計者にモデル化された異なる視点 |
| **Independent System Prompts** | 各エージェントが固有のシステムプロンプトを持つ |
| **Declared Blind Spots** | 各エージェントの盲点を事前に宣言 |
| **6 Deliberate Polarities** | 意図的な極性（対立軸）の設定 |
| **Parallel Subagents** | 独立したコンテキストとターミナルセッションで並列実行 |

## Key Insight

> 「 breakthrough wasn't a better prompt. It was a structured disagreement. 」

プロンプトを改善しても解決しない問題は、**多様性の欠如**から来る。構造化された不一致を通じて、盲点を発見し、判断の質を向上させる。

## Relationship to Multi-Agent Patterns

このアプローチは、従来の「多エージェント協調」の発想を逆転させる:

- **従来**: 複数のエージェントが合意して結論を出す
- **NYKのフレームワーク**: 複数のエージェントが**不同意合**して、合意に達する前に盲点を洗い出す

これは[[back-of-house-multi-agent-patterns]]の「Back of House」パターンとは異なり、**意思決定の品質**に焦点を当てた異なるアプローチ。

## Related Concepts

- [[back-of-house-multi-agent-patterns]] — マルチエージェントワークフロー
- [[multi-agent-orchestration-patterns]] — 複数エージェントのオーケストレーション
- [[subagents]] — サブエージェントのパターン
- [[excessive-agency]] — エージェントの自律性の限界
