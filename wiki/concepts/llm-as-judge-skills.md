---
title: "LLM-as-Judge Skills"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [context-engineering, evaluation, coding-agents]
sources:
  - "[[raw/articles/2026-05-xx_github_llm-as-judge-skills]]"
related:
  - "[[concepts/context-engineering]]"
  - "[[concepts/evaluation]]"
  - "[[concepts/agent-skills]]"
---

# LLM-as-Judge Skills

[Murat Can Koylan](https://github.com/muratcankoylan) による **Agent-Skills-for-Context-Engineering**（15.5k stars）の一部。LLMの出力をLLM自身で評価するための再利用可能なスキルセット。

## 概要

LLM-as-Judgeは、モデルの出力品質を自動評価するパターン。Context Engineeringの観点から、評価ロジックをエージェントスキルとしてパッケージ化し、コーディングエージェント（Claude Code, Cursor, Codex）で再利用可能にする。

## レポジトリ構造

```
Agent-Skills-for-Context-Engineering/
├── examples/llm-as-judge-skills/
├── agents/        # エージェント定義
├── skills/        # 再利用可能スキル
├── prompts/       # 評価プロンプト
└── src/           # ソースコード
```

## 関連性

Context Engineering（コンテキストエンジニアリング）は、Anthropicが提唱する「プロンプトエンジニアリングの次」の概念。システムプロンプト、ツール定義、スキル、メモリなど、エージェントの全コンテキストを設計する工学分野。

## 参照

- [Agent-Skills-for-Context-Engineering — GitHub](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
- [Effective Context Engineering — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
