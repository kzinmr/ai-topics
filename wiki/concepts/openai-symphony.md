---
title: "OpenAI Symphony"
type: concept
created: 2026-04-13
updated: 2026-04-29
tags: [concept, agent-team-swarm, openai, orchestration, coding-agents]
related: [agent-team-swarm, harness-engineering, dark-factory-software-factory]
sources:
  - https://github.com/openai/symphony
  - https://github.com/openai/symphony/blob/main/SPEC.md
  - https://news.ycombinator.com/item?id=47252045
  - https://openai.com/index/open-source-codex-orchestration-symphony/
---

# OpenAI Symphony

**Source:** OpenAI Engineering Blog (2026-04-27) + GitHub (2026-02-26)
**Status:** Open-source spec with reference implementation
**Related:** [[concepts/agent-team-swarm]], [[concepts/harness-engineering]], [[concepts/dark-factory-software-factory]]

---

## Overview

OpenAI Symphonyは、**プロジェクトの作業を独立した自律的な実行ランに変換**し、チームがコーディングAgentを「監視」するのではなく「作業を管理」できるようにするサービス。

> Symphony turns project work into isolated, autonomous implementation runs, allowing teams to **manage work instead of supervising coding agents**.

Linear等の課題管理ボードを監視し、タスクごとにAgentをspawnして自動実行。AgentはCIステータス、PRレビューフィードバック、複雑度分析、ウォークスルー動画などの「Proof of Work」を提供し、承認されるとPRを安全にlandする。

**GitHub:** [openai/symphony](https://github.com/openai/symphony) — 14,707 stars, Apache 2.0

---

## Core Architecture

### System Components (SPEC.md)

| コンポーネント | 役割 |
|---|---|
| **Workflow Loader** | リポジトリ内の`WORKFLOW.md`からYAML設定 + プロンプトを読み込み |
| **Config Layer** | ワークフロー設定の型付きゲッター |
| **Orchestrator** | ポーリングループ、課題の適格性判定、同時実行数制御、リトライ、整合性チェック |
| **Workspace Manager** | 課題IDを隔離されたワークスペースパスにマップ |
| **Agent Runner** | ワークスペース作成 → 課題+ワークフローからプロンプト構築 → Agent実行 |
| **Logging** | 構造化ランタイムログの出力 |

### 重要な境界定義

```
Symphony = スケジューラー/ランナー + トラッカーリーダー
≠ Agentの実装自体（Codex/Claude Code等と統合）
```

---

## WORKFLOW.md: リポジトリ所有の契約

Symphonyの中核革新は、**エージェントの振る舞いをリポジトリ内の`WORKFLOW.md`で定義**すること。

```yaml
---
tracker:
  kind: linear
  project_slug: "your-project"
  active_states: [Todo, "In Progress", Merging, Rework]
  terminal_states: [Closed, Cancelled, Done]
polling:
  interval_ms: 5000
workspace:
  root: ~/code/symphony-workspaces
agent:
  max_concurrent_agents: 10
  max_turns: 20
codex:
  command: codex --config model_reasoning_effort=xhigh
  approval_policy: never
  thread_sandbox: workspace-write
---
You are working on a Linear ticket {{ issue.identifier }}
...
```

### Prompt Template (Liquid)
- 課題のタイトル、説明、ステータスを注入
- リトライ時の継続コンテキストを含む
- 「Proof of Work」の基準を明文化

---

## Agent Runner Protocol

1. **Isolated Workspace:** 課題ごとに独立したディレクトリ（パス封じ込み付き）
2. **Coding Agent統合:** Codex/Claude Code等をstdio app-serverモードで実行
3. **永続Workpad:** Linearチケットにコメント作为進捗追跡の信頼できる情報源
4. **自動リトライ:** 失敗時は再スケジューリング（最大試行回数設定可能）
5. **ステータス遷移:** 品質基準を満たした時のみチケットステータスを更新

---

## Design Philosophy

> "Symphony works best in codebases that have adopted **harness engineering**. Symphony is the next step — moving from managing coding agents to managing work that needs to get done."

- **仕様駆動**: 人間は仕様とワークフローを定義し、Agentが実装
- **Proof of Work重視**: コードそのものではなく、CI/テスト/レビュー結果で品質を証明
- **非監視型**: Agentの作業を見守るのではなく、成果物だけを検収
- **リポジトリ所有**: ワークフロー定義をコードと一緒にバージョン管理

---

## Ecosystem

### 公式実装
- **Elixir reference implementation** (openai/symphony/elixir/) — Apache 2.0

### コミュニティ実装
- **Symphony Go** (vnovick/symphony-go) — Go実装 + Live Kanban Dashboard
- 多数のフォークと移植が進行中

### HNでの議論

- **MarkMarine**: 自身のAttractor forkを評価。「Symphonyはharnessを提供しないため、Attractorのgraph orchestrationは補完的。property testing, fault injection, fuzzing + digital twinでテスト層を構築している」
- **bigwheels**: 「Attractor公開1ヶ月で数百のOSS実装が出現」。コミュニティの関心の高さを示す
- **exclipy**: 「SPEC.mdはinscrutable agent slop。状態機械に言及しながら説明がない」。ドキュメントの具体性不足を批判
- **hrpnk**: 「言語非依存の仕様が本当にそんなに簡単か？」。SPEC.mdの移植性への懐疑

---

## Comparison: Symphony vs Anthropic Managed Agents

| 観点 | OpenAI Symphony | Anthropic Managed Agents |
|---|---|---|
| **焦点** | 作業のオーケストレーション | Agentインフラのマネージド化 |
| **スコープ** | タスクボード → Agent spawn → 成果検収 | Agentライフサイクル全体（Brain/Hands/Session） |
| **設定** | WORKFLOW.md（リポジトリ所有） | Claude Console + API（プラットフォーム所有） |
| **Agent** | 外部Agent（Codex等）を統合 | Claude Agentをネイティブ提供 |
| **Multi-Agent** | 同時実行数制御 + 隔離ワークスペース | Agent spawn + Self-Evaluationループ |
| **Philosophy** | "Manage work, not agents" | "Decouple brain from hands" |

両者は補完的：Symphonyは「どのAgentがどのタスクをいつ実行するか」を管理し、Managed Agentsは「個々のAgentをどう安全に・効率的に動かすか」を提供する。

---

## Related

- [[concepts/agent-team-swarm]] — 複数Agent協調の上位概念
- [[concepts/harness-engineering]] — Symphonyが前提とする開発プラクティス
- [[concepts/dark-factory-software-factory]] — 完全自律開発への次のステップ
- [[concepts/anthropic-managed-agents]] — 競合のマネージドAgentプラットフォーム
- [[concepts/multi-agent-autonomy-scale]] — 大規模Agent協調の研究
- [[ryan-lopopolo]] — Symphonyの作者、Harness Engineering提唱者。OpenAI Frontierで1M LOCのagent-only実験を主導

---

## OpenAI Engineering Blog Update (Apr 2026)

OpenAI published an [engineering blog post](https://openai.com/index/open-source-codex-orchestration-symphony/) detailing the results and lessons from deploying Symphony internally.

### Key Results
- **500% increase in landed PRs** within three weeks of Symphony adoption on some teams
- Human attention was the bottleneck — engineers could only manage 3–5 agent sessions before context switching became painful
- Symphony turned issue trackers (Linear) into a **control plane** for autonomous coding agents

### The Economic Shift
When implementation cost drops to near zero, engineering behavior changes fundamentally:
- **Speculative Tasks:** Engineers explore refactors and test hypotheses freely, discarding results that don't work
- **Broadened Access:** Product managers and designers can file feature requests directly — agents provide video walkthroughs as "review packets"
- **From Interaction to Orchestration:** The paradigm shifted from micromanaging agent sessions to an "always-on" orchestrator that pulls work from the task tracker

### Codex App Server Mode
Symphony uses a headless JSON-RPC API (`Codex App Server`) with dynamic tool calls:
- Functions like `linear_graphql` are exposed to agents without exposing raw API tokens
- Full session handshake protocol: `initialize → thread/start → turn/start`

### Lessons Learned
1. **Loss of Nudging:** Moving to ticket-level work means humans can't "steer" agents mid-flight
2. **System Hardening over Manual Fixing:** Instead of fixing agent mistakes, add skills to the harness (e2e tests, Chrome DevTools access) so agents self-correct
3. **Objectives over Transitions:** Treating agents as rigid state machine nodes failed; giving agents *objectives* and tools and "letting them cook" works better

---

## OSS Pipeline: Issue → Agent → PR → Human Review (Apr 2026)

AINews (Apr 28, 2026) reports that Symphony has evolved into a full **open-source development pipeline**:

- **Issue → Agent → PR → Human Review**: Symphony now orchestrates a complete development workflow where:
  - Issues from Linear/GitHub are automatically picked up by agents
  - Agents work in isolated workspaces with defined prompts
  - PRs are submitted with full context and proof of work
  - Humans only review final output, not supervise process
- **Open Source**: The pipeline is available as an Apache 2.0 project on GitHub
- **Community Adoption**: Multiple implementations emerging (Go, Elixir, Python)
- **Significance**: This represents the transition from L3 (Agent-Assisted) to L4 (Engineering Team) in the 5-level autonomy model

This OSS pipeline is the practical realization of Symphony's "manage work, not agents" philosophy.

---

## Sources

- [OpenAI Symphony GitHub](https://github.com/openai/symphony)
- [SPEC.md](https://github.com/openai/symphony/blob/main/SPEC.md)
- [HN Discussion: OpenAI Symphony](https://news.ycombinator.com/item?id=47252045)
