---
title: "Agent Patterns"
type: concept
created: 2026-04-30
updated: 2026-05-06
tags:
  - concept
  - ai-agents
  - agentic-engineering
  - multi-agent
  - subagent-patterns
status: complete
description: "Patterns and practices for building and deploying AI agents — harnesses, workflows, and multi-agent orchestration."
---

# Agent Patterns

AI Agentのアーキテクチャパターン、ハル設計、ワークフロー。

## 概要

AI Agentのパターンは多岐にわたる：単一エージェントのパターンから、サブエージェント、メタエージェント、長期実行エージェント、およびマルチエージェント協調まで。

## Subagent Patterns (Philipp Schmid, May 2026)

Philipp Schmidの4つのサブエージェントパターンは、メインエージェントがサブエージェントを制御するレベルに基づいて分類される：

### 1. Inline Tool — サブエージェントを関数呼び出しとして
最もシンプルなパターン。メインエージェントが `call_agent` ツールを呼び出し、サブエージェントをスポーンして結果をツールレスポンスとして返す。同期的（ブロッキング）または非同期的（agent_id を返す）の2種類。
- **用途**: リサーチ参照、コードレビュー、テスト生成
- **限界**: 中間フォローアップ不可

### 2. Fan-Out — スポーンして待機
メインエージェントが複数タスクを発行し、収集タイミングを制御。`spawn_agent`（即時ID返却）と `wait_agent`（ブロッキング）の2ツールで構成。
- **強み**: サブエージェントの並列実行中にメインエージェントも作業可能
- **限界**: タイミング設計が重要（即 `wait_agent` すると並列効果が消える）

### 3. Agent Pool — 永続的メッセージング
サブエージェントが長期生存・ステートフル・対話可能。メインは `spawn_agent`, `send_message`, `wait_agent`, `list_agents`, `kill_agent` の豊富なツールセットでコーディネータ役に。
- **強み**: サブエージェントが会話履歴を保持、フィードバックを受け取って修正可能
- **用途**: Researcherがデータを探し、Writerがそのデータを使って記事を書くようなマルチステップワークフロー

### 4. Teams — エージェント間直接通信
メインエージェントはハイレベルなスーパーバイザー。チームをセットアップした後は、サブエージェント同士が `send_message` で直接通信。
- **強み**: メインエージェントのコンテキストをクリーンに保つ
- **限界**: エージェントループのリスク（AがBを待ち、BがAを待つ）。全ロールにフロンティアモデルが必要

| パターン | ツール | メインの役割 | 寿命 |
|---------|--------|------------|------|
| Inline Tool | `call_agent` | Caller | 単一タスク |
| Fan-Out | `spawn`, `wait` | Dispatcher | 単一タスク |
| Agent Pool | `spawn`, `send`, `wait`, `list`, `kill` | Coordinator | マルチターン |
| Teams | 全て＋cross-agent `send` | Supervisor | 永続的 |

### 実装ガイドライン
1. **まずはInline Toolから始める** — ほとんどのマルチエージェント需要は単一タスク呼び出しで十分
2. **モデル選択**: パターン1・2は小型モデルでも可。パターン3はマルチエージェント状態追跡対応モデルが必要。パターン4は全ロールにフロンティアモデルが必要（GPT-4o, Claude 3.5 Sonnet）
3. **結果収集**: フレームワークがツールを提供するが、オーケストレーションはモデルが制御する。開発者はモデルが `wait_agent` / `kill_agent` を適切に呼ぶことを保証する必要がある
4. **将来設計**: 今日4体の連携タスクが明日は1体の高性能モデルで解ける可能性。柔軟に設計する

Source: [Philipp Schmid — How Agents Manage Other Agents: Four Subagent Patterns in 2026](https://www.philschmid.de/subagent-patterns-2026)

## Raw Articles

- [2025286163641118915_The-File-System-Is-the-New-Database-Personal-OS-for-AI-Agents](2025286163641118915_The-File-System-Is-the-New-Database-Personal-OS-for-AI-Agents.md)
- [2026-04-25-agent-product-design-chinese](2026-04-25-agent-product-design-chinese.md)
- [2026-04-25-agentcraft-rts-agent-orchestration](2026-04-25-agentcraft-rts-agent-orchestration.md)
- [2026-04-27_2045080054917476451_Hermes-Agent-Polymarket-Self-Learning-Weather-Trading-Bot](2026-04-27_2045080054917476451_Hermes-Agent-Polymarket-Self-Learning-Weather-Trading-Bot.md)
- [2026-04-27_2045935785661349956_Hermes-Agent-What-People-Are-Actually-Using-It-For](2026-04-27_2045935785661349956_Hermes-Agent-What-People-Are-Actually-Using-It-For.md)
- [2026-04-27_2046277232537256002_The-Runtime-Behind-Production-Deep-Agents](2026-04-27_2046277232537256002_The-Runtime-Behind-Production-Deep-Agents.md)
- [2026-04-28_x-article-15-hermes-agent-features](2026-04-28_x-article-15-hermes-agent-features.md)
- [2026-04-28_x-article-connecting-agents-to-decisions-palantir](2026-04-28_x-article-connecting-agents-to-decisions-palantir.md)
- [2026-2013-effective-harnesses-for-long-running-agents](2026-2013-effective-harnesses-for-long-running-agents.md)
- [2026-2026-devin-use-cases---agent-workflows-cookbook](2026-2026-devin-use-cases---agent-workflows-cookbook.md)
- [2026-2035-agent-skills-overview---agentskills.io](2026-2035-agent-skills-overview---agentskills.io.md)
- [2026-designing-for-agents](2026-designing-for-agents.md)
- [2041927992986009773_Launching-Claude-Managed-Agents](2041927992986009773_Launching-Claude-Managed-Agents.md)
- [2042539396638085339_What-Hermes-Agent-Can-Do-for-You](2042539396638085339_What-Hermes-Agent-Can-Do-for-You.md)
- [2047720067107033525_Memory-in-Claude-Managed-Agents](2047720067107033525_Memory-in-Claude-Managed-Agents.md)
- [agent-sandbox-architecture-2026-02-25](agent-sandbox-architecture-2026-02-25.md)
- [crawl-2026-04-23-building-effective-ai-agents](crawl-2026-04-23-building-effective-ai-agents.md)
- [hyperbo.la--w-agents-agents-agents--79613a0d](hyperbo.la--w-agents-agents-agents--79613a0d.md)
- [jason-liu-sandboxes-agents-sdk-2026-04](jason-liu-sandboxes-agents-sdk-2026-04.md)
- [lucumr.pocoo.org--2026-2-9-a-language-for-agents--77a0e78a](lucumr.pocoo.org--2026-2-9-a-language-for-agents--77a0e78a.md)
- [martinalderson.com--posts-ai-agents-are-starting-to-eat-saas--37d8652e](martinalderson.com--posts-ai-agents-are-starting-to-eat-saas--37d8652e.md)
- [martinalderson.com--posts-excel-agents-could-unlock-1t-in-economic-value--2fb910d0](martinalderson.com--posts-excel-agents-could-unlock-1t-in-economic-value--2fb910d0.md)
- [martinalderson.com--posts-travel-agents-developers--03e9ba7f](martinalderson.com--posts-travel-agents-developers--03e9ba7f.md)
- [martinalderson.com--posts-using-agents-and-wine-to-move-off-windows--85a78b28](martinalderson.com--posts-using-agents-and-wine-to-move-off-windows--85a78b28.md)
- [martinalderson.com--posts-why-im-building-my-own-clis-for-agents--08080178](martinalderson.com--posts-why-im-building-my-own-clis-for-agents--08080178.md)
- [milksandmatcha-0xsero-single-agent-ceiling-2026](milksandmatcha-0xsero-single-agent-ceiling-2026.md)
- [nesbitt.io--2026-04-08-package-security-problems-for-ai-agents-html--cec0229c](nesbitt.io--2026-04-08-package-security-problems-for-ai-agents-html--cec0229c.md)
- [nesbitt.io--2026-04-09-package-security-defenses-for-ai-agents-html--aa01c0e5](nesbitt.io--2026-04-09-package-security-defenses-for-ai-agents-html--aa01c0e5.md)
- [open.substack.com--pub-importai-p-import-ai-453-breaking-ai-agents--80eac51f](open.substack.com--pub-importai-p-import-ai-453-breaking-ai-agents--80eac51f.md)
- [open.substack.com--pub-nlpnews-p-ai-agents-weekly-claude-managed-agents--883aac03](open.substack.com--pub-nlpnews-p-ai-agents-weekly-claude-managed-agents--883aac03.md)
- [seangoedecke.com--programming-with-ai-agents-as-theory-building--b672de74](seangoedecke.com--programming-with-ai-agents-as-theory-building--b672de74.md)
- [two-ways-to-sandbox-agents-2026-02-25](two-ways-to-sandbox-agents-2026-02-25.md)
- [workos-fga-authorization-ai-agents-2026-04-13](workos-fga-authorization-ai-agents-2026-04-13.md)
