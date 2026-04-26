---
title: "Harness Engineering"
type: concept
aliases:
  - harness-engineering
  - agent-harness
tags:
  - concept
  - harness-engineering
  - ai-agents
  - orchestration
  - openai
status: complete
description: "Agent = Model + Harness. Environment design philosophy for agent-driven development."
created: 2026-04-09
updated: 2026-04-24
sources:
  - "https://openai.com/index/harness-engineering/"
  - "http://latent.space/p/harness-eng"
  - "https://github.com/openai/symphony"
related:
  - "[[concepts/harness-engineering]]"
  - "[[concepts/agentic-engineering]]"
  - "[[concepts/context-engineering]]"
  - "[[concepts/symphony]]"
---

# Harness Engineering

> **Definition:** Harness Engineeringは「Agent = Model + Harness」を基本方程式とする、エージェント駆動開発の環境設計哲学。エージェントが自律的にコードを書き、テストし、マージできるような「環境（harness）」を設計することに焦点を当てる。

Ryan Lopopolo（OpenAI）が提唱し、Simon WillisonのAgentic Engineering、AnthropicのAI Agent Engineering、KarpathyのContext Engineeringを包含する**最上位概念**。

## 核心哲学

Harness Engineeringの4つの柱:

1. **Zero Human-Written Code** — 意図的にコードを書かないことで、エージェントにエンドツーエンドの作業を強制
2. **Fast Build Loops (1-Minute Rule)** — 内側ループのビルド時間を1分以内に制限
3. **Agent-Legible Software** — ソフトウェアは人間だけでなくモデルのために書かれる
4. **Humans Become the Bottleneck** — 希少なリソースはトークンから同期人間の注意へ移行

## OpenAI Harness Experiment

| メトリクス | 値 |
|------------|-----|
| 期間 | 5ヶ月 |
| 人間が書いたコード | **0行** |
| 総コードベース | >1,000,000 LOC |
| マージされたPR | 数千 |
| トークン消費 | >1B tokens/day (~$2-3K/day) |
| 使用モデル | GPT-5.0 → 5.4 |

## Symphony

[Symphony](https://github.com/openai/symphony)はHarness Engineeringの具現化。Issue-Tracker-Driven Orchestrationパターン:

> "Symphony shifts engineering from supervising coding agents to managing work — issues go in, PRs come out."

## AGENTS.md パターン

> "Treat your AGENTS.md as a table of contents (~100 lines) rather than a comprehensive encyclopedia."

詳細とサブ概念は [[concepts/harness-engineering]] を参照。

## See Also

- [[concepts/harness-engineering]] — 詳細フレームワーク
- [[concepts/agentic-engineering]] — Willisonのサブセット概念
- [[concepts/context-engineering]] — 横断技術コンポーネント
- [[concepts/symphony]] — OpenAIの実装
