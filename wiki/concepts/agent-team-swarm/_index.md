---
title: "Agent Team / Swarm"
tags: [concept, ai-agents, llm, evaluations, rag]
created: 2026-04-24
updated: 2026-04-24
---

# Agent Team / Swarm

**Agent Team (Swarm)** は、単一のAI Agentがタスクを遂行するのではなく、複数のAgentが協調・分担して複雑なワークフローを自律的に実行するアーキテクチャパターン。

従来の **Harness Engineering**（1つのAgent + ツール環境）を、複数のBrainとHandsにスケールアップしたもの。

## Taxonomy: Agent Team関連概念の整理

| 概念 | 提唱者/実装 | 焦点 | レベル |
|---|---|---|---|
| **Agentic Engineering** | Simon Willison他 | AI Agentを活用したソフトウェア開発手法全般 | レベル1: 個人開発者のワークフロー |
| **Harness Engineering** | Anthropic, Ryan Lopopolo | Agentの実行環境・ツール統合・ガードレール | レベル2: 単一Agentのインフラ |
| **Managed Agents** | Anthropic | AgentのBrain/Hands/Sessionを分離したプラットフォーム | レベル3: エンタープライズ基盤 |
| **Agent Team / Swarm** | OpenAI Symphony他 | 複数Agentの協調・オーケストレーション | レベル4: チームレベル自律化 |
| **Dark Factory** | Dan Shapiro, StrongDM | 人間がコードを一切書かず・レビューもしない完全自律 | レベル5: 完全自動化 |

## Dan Shapiroの「5レベル」モデル

Simon Willisonが紹介したDan Shapiroの分類:

1. **Level 1: Spicy Autocomplete** — GitHub Copilotの初期版、コード補完
2. **Level 2: Chat-assisted** — ChatGPTに聞いてコピペ
3. **Level 3: Agent-assisted** — Claude Code/Codexがタスクを実行
4. **Level 4: The Engineering Team** — 仕様と計画を立て、Agentが実装。人間はマネージャー役
5. **Level 5: Dark Factory** — Fanucの無人工場の如く、人間が不要な完全自律開発

StrongDMはこのLevel 5を実践し、Anthropic Managed AgentsとOpenAI SymphonyはLevel 4→5への架け橋となっている。

## 主要実装

### Anthropic Managed Agents
- **Brain（Claude + harness） / Hands（sandbox） / Session（event log）**を完全分離
- Multi-Agent Coordination（リサーチプレビュー）: Agentが他のAgentをspawn可能
- Self-Evaluation（リサーチプレビュー）: 成功基準を定義し自律的に評価・改善
- 詳細: [[concepts/anthropic-managed-agents]]

### OpenAI Symphony
- Linear等のタスクボードを監視し、Agentチームをspawnして実行
- SPEC.mdを提供 → 任意の言語で実装可能（参照実装はElixir）
- Coding Agentを「管理」するのではなく「仕事を管理」するパラダイム
- Ryan LopopoloがOpenAI Frontierで開発。3-5 PR/日 → 75 PR/週の実績
- 詳細: [[concepts/openai-symphony]], [[ryan-lopopolo]]

### StrongDM Attractor / Dark Factory
- 非インタラクティブ開発: 仕様 + シナリオ → Agentがコード作成 → テスト → 収束
- 人間はコードを一切見ない・レビューしない
- Digital Twin Universe: 依存サービスをAgentでクローン
- 詳細: [[concepts/dark-factory-software-factory]]

## 2026 Production Architecture Patterns

### The Four Proven Patterns
1. **Hierarchical (Orchestrator-Worker)** — Central manager decomposes tasks, delegates to specialized workers
2. **Peer-to-Peer (Collaborative)** — Agents communicate directly, negotiating without a central manager
3. **Pipeline (Sequential)** — Linear sequence where one agent's output is the next's input
4. **Event-Driven (Reactive)** — Agents subscribe to event bus and activate on triggers

### Communication Protocols
Three protocols competing to become the standard:
- **MCP** — Agent-to-tool communication (mature, widely adopted)
- **A2A** — Dynamic discovery + enterprise governance between autonomous agents (Google + IBM/Linux Foundation, 2025 merger)

Decision: MCP for tools, A2A for cross-org and governance.

### Critical Failure Modes
- **Infinite Delegation:** Agent A → B → A loop. Solution: depth limit (3-5)
- **Context Poisoning:** One agent's error amplified downstream. Solution: validation agents at junctions
- **Cost Explosion:** p99 costs 10-20x average. Solution: hard token/dollar limits per task

### The Shared Memory Problem
Centralized state store with **optimistic concurrency control** (e.g., Redis Lua scripts for atomic check-and-set).

## 関連概念

- [[concepts/harness-engineering]] — 単一Agentの実行環境設計（基礎）
- [[concepts/multi-agent-autonomy-scale]] — 256Agentスケールの自律協調研究
- [[concepts/harness-engineering/agentic-engineering-patterns]] — Agentic Engineeringのパターン集
- [[ryan-lopopolo]] — Symphonyの作者、Harness Engineering提唱者
- [[concepts/agent-communication-protocols]] — MCP/A2A/ACP プロトコル比較
- [[concepts/agentic-conflict-resolution]] — 複数Agent間の競合検出・解決
- [[concepts/zero-trust-agentic-ai]] — Agentのセキュリティ基盤
