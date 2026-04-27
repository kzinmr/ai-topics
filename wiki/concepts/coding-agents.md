---
title: "Coding Agents"
type: concept
aliases:
  - coding-agents
created: 2026-04-25
updated: 2026-04-27
tags:
  - concept
  - coding-agents
  - ai-agents
status: complete
description: "LLM-powered coding agents — tools, environments, and optimization patterns for agent-driven development."
---

# Coding Agents

LLM搭載のコード書きエージェント。Claude Code、OpenAI Codex、Cursor、GitHub Copilot、OpenClawなどが該当。

## 最適化: デベロッパ環境の設計

Eric Zakariasson (2026-04-27) による実践的ガイド:

エージェントに人間と同じ仕事をしてもらいたいなら、人間に1日目で与えるものを与えよ: マシン、認証情報、Slack、Linear、Notion、Datadog、GitHub org。

> "This also means that your job shifts. You're less the person writing every line and more the person building the system that tells agents what good and bad looks like. This is mostly the same work as building good developer experience for humans."

### 重要な視点
- エージェント環境の最適化は、人間向けのDX構築とほぼ同じ作業
- 開発者の役割は「すべての行を書く人」から「エージェントにとって善と悪がどう見えるかを定義する人」へ移行

参考: [Optimizing your dev environment for coding agents](../raw/articles/2041897427431563613_optimizing-your-dev-environment-for-coding-agents.md)

## 業界動向

### SpaceX × Cursor: $60B 買収オプション (2026-04)

SpaceXは2026年後半にCursorを**$600億で買収する権利**を取得。またはCursorに**$100億**を支払って協業する選択肢も保持。

**背景:**
- Cursorの独自モデルComposer 2はMoonshotのKimiベースでコミュニティの反応は冷ややか
- SpaceXのColossusクラスター（100万H100相当）へのアクセス獲得が真の目的
- Kevin Kwok分析: 「トップコーディングラボはモデルとプロダクトの両方を所有する必要がある。流通だけを持ちモデルを持たないのは賃貸契約。全てのデブツール企業はモデル企業になるか、モデルの機能になるか」

### OpenAI Workspace Agents (2026-04)

Codex搭載の共有エージェント。Business/Enterpriseプラン向け。Slack、Salesforce、Notion、Google Driveと統合。永続メモリとロールベースガバナンス搭載。

## 関連ページ
- [[concepts/harness-engineering]] — エージェント駆動開発の環境設計哲学
- [[concepts/agentic-engineering]] — 上位概念
- [[concepts/subagents]] — 並列エージェント委譲パターン
- [[concepts/cognitive-debt]] — コンテキスト管理の重要性
- [[entities/openai]] — OpenAI (Workspace Agents, Codex)
- [[entities/anthropic]] — Anthropic (Claude Code)
