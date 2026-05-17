---
title: OpenClaw
type: entity
aliases: [openclaw, open-claw, peter-steinberger-openclaw]
created: 2026-04-15
updated: 2026-05-17
status: L2
sources:
  - https://github.com/NVIDIA/OpenClaw
  - https://build.nvidia.com/spark
  - https://nemoclawai.io/blog/getting-started-nemoclaw-dgx-spark/
  - https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html
  - https://blog.kilo.ai/p/hermes-vs-openclaw-when-to-reach
  - https://kilo.ai/openclaw/vs-hermes
  - https://docs.openclaw.ai/tools/acp-agents
  - https://snowan.gitbook.io/study-notes/ai-blogs/openclaw-memory-system-deep-dive
tags: [entity, framework, local-llm, open-source, agent-communication, agent-architecture, orchestration, memory-systems]
---

# OpenClaw

Open-source always-on AI assistant framework created by **Peter Steinberger** (former PSPDFKit CEO). Deploys autonomous agents that run continuously, self-evolve through interaction, and integrate with messaging platforms like Telegram. OpenClaw is the upstream project that **NemoClaw** wraps with enterprise-grade security.

## Core Philosophy

> *"With one command, anyone can run always-on, self-evolving agents anywhere."*

OpenClaw represents a shift from **session-bound** AI tools (Claude Code, ChatGPT conversations) to **persistent, always-on** agents that:
- Run continuously in the background
- Learn and adapt from interactions over time
- Operate across multiple messaging platforms
- Execute tasks autonomously within defined boundaries

## Architecture

```
OpenClaw Agent
  ├── TUI (Terminal UI)
  ├── Telegram Bot Integration
  ├── Local Model Support (Ollama, LM Studio)
  └── API Server
```

## Key Features

| Feature | Description |
|---------|-------------|
| **Always-on** | Runs 24/7 without manual session management |
| **Self-evolving** | Learns from interactions and adapts behavior |
| **Multi-platform** | Telegram, web dashboard, terminal, API |
| **Local inference** | Works with Ollama, LM Studio, llama.cpp |
| **Open source** | MIT-licensed, community-driven development |
| **Lightweight** | Designed for edge devices like DGX Spark |

## Integration with DGX Spark

OpenClaw is a **first-class citizen** on DGX Spark:

- Runs natively on arm64 architecture
- Leverages 128 GB unified memory for large models
- Integrates with LM Studio and Ollama for local inference
- Supports Telegram bot deployment for always-on access

### Quick Start on DGX Spark

```bash
# Install OpenClaw
# (via NemoClaw installer or standalone)
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash

# Launch the agent
openclaw agent --agent main --local -m "hello" --session-id test

# Or use the TUI
openclaw tui
```

## OpenClaw vs NemoClaw

| Aspect | OpenClaw (standalone) | NemoClaw (wrapped) |
|--------|----------------------|-------------------|
| **Security** | Direct host access | OpenShell sandbox |
| **Isolation** | None | Landlock + seccomp + netns |
| **Network** | Unrestricted | Policy-controlled |
| **Multi-tenant** | No | k3s-based pod isolation |
| **Inference** | Any provider | Routed through controlled backends |
| **Use case** | Personal experimentation | Enterprise deployment |

## Configuration

OpenClaw stores configuration in `~/.openclaw/openclaw.json`:

```json
{
  "gateway": {
    "auth": {
      "token": "<your-gateway-token>"
    }
  },
  "agent": {
    "name": "main",
    "model": "ollama/nemotron-3-super:120b",
    "platform": "telegram"
  }
}
```

### Web Dashboard

```
http://127.0.0.1:18789/#token=<your-gateway-token>
```

> ⚠️ **Important:** Use `127.0.0.1`, not `localhost` — the gateway requires an exact origin match.

## Telegram Integration

1. Create a bot token via `@BotFather` on Telegram (`/newbot`)
2. Configure the token in `openclaw.json`
3. Messages to the bot are forwarded to your agent
4. Agent responses are sent back to the user

## Core Architecture Patterns

OpenClaw のアーキテクチャは Hugo Bowne-Anderson + Ivan Leo の2026年2月ワークショップ "Building Your Own OpenClaw from Scratch" で Pure Python 再構築を通じて詳細に解説された。

### Hooks System（フックシステム）

エージェントのライフサイクルイベントに合成可能な副作用を追加：

```
on_model_response → Telegram送信 / Richターミナル出力
on_tool_call      → ビジュアルdiff表示 / ロギング
on_tool_result    → データベース記録 / 観測可能性
```

コアループはフックの存在を**一切知らない** — `emit()` を呼ぶだけ。Telegram連携もロギングも、コアループに1行も変更を加えずに追加できる。

### Memory System（ファイルファースト・ハイブリッド検索メモリ） [[concepts/agent-memory-systems-comparison]]

OpenClawは **ファイルを唯一の真実源（source of truth）** とするMarkdown駆動メモリシステムを採用。従来のRAGのようなベクトルDB依存を排し、**ハイブリッド検索（BM25 + ベクトル）** と **埋め込みプロバイダーの自動選択** を特徴とする。

出典: [[raw/articles/2026-01-25_snowan-gitbook_openclaw-memory-system-deep-dive]] (OpenClaw commit f99e3dd, Jan 2026)

#### メモリの3層構造

| 層 | 保存場所 | 内容 | 読み込み条件 |
|---|---|---|---|
| **Ephemeral（日次ログ）** | `memory/YYYY-MM-DD.md` | 日々の活動・判断の追記型ログ | 今日＋昨日のログをセッション開始時に自動読み込み |
| **Durable（永続知識）** | `MEMORY.md` | 重要な決定・プロジェクト規約・長期TODO | **プライベートセッションのみ** — グループコンテキストでは非公開 |
| **Session（会話履歴）** | `sessions/YYYY-MM-DD-<slug>.md` | LLM生成の説明的スラグ付き会話トランスクリプト | セッション開始時に前回会話を自動保存、全文検索可能 |

#### チャンキングアルゴリズム

スライディングウィンドウ + オーバーラップ方式:
- **ターゲット**: ~400トークン/チャンク（~1600文字）
- **オーバーラップ**: 80トークン（~320文字）で境界のコンテキスト切れを防止
- **行認識**: 行番号付きで正確なソース帰属が可能
- **SHA-256ハッシュによる重複排除**: 同一コンテンツ → キャッシュヒット → 再埋め込み不要

#### ハイブリッド検索: BM25 + ベクトル

重み付きスコア融合（デフォルト: **70% ベクトル + 30% BM25**）:

| 検索方式 | 得意分野 | 実装 |
|---|---|---|
| **ベクトル検索（意味的類似度）** | 概念マッチ（"gateway host" ≈ "machine running gateway"） | SQLite + sqlite-vec拡張 / コサイン類似度 |
| **BM25検索（語彙マッチ）** | 正確なトークン（エラーコード、関数名、ID） | SQLite FTS5 |

#### 埋め込みプロバイダー自動選択

**Local → OpenAI → Gemini** のフォールバックチェーン:
1. **Local** (node-llama-cpp): embeddinggemma-300M (~600MB)、プライバシー重視・オフライン可・低速
2. **OpenAI** (text-embedding-3-small): 1536次元、高速、Batch APIで50%コスト削減
3. **Gemini** (gemini-embedding-001): 768次元、無料枠あり

#### キャッシュファースト埋め込み + バッチ最適化

- SHA-256ハッシュベースの重複排除: 同一段落が複数ファイルに出現 → 1回だけ埋め込み
- OpenAI Batch API: 同期API比50%コスト削減
- 実例: 10,000チャンク → 同期$0.20 → Batch $0.10 → キャッシュ50%ヒットで$0.05

#### Pre-Compaction Flush（コンパクション前自動フラッシュ） [[concepts/context-compaction]]

OpenClawの最も革新的なメモリ機能。会話がコンテキストウィンドウ制限に近づくと、**サイレントなエージェントターン** を発動し、コンテキスト圧縮 **前** に永続メモリへの書き込みを促す。

- 200Kコンテキストの場合、約80%使用時に発動
- 通常は `NO_REPLY`（保存すべき重要事項がない場合は無言）
- コンパクションサイクルごとに1回のみ（スパム防止）
- Read-onlyサンドボックスモードではスキップ

#### セッションインデックス

- JSONL解析でユーザー/アシスタントメッセージを抽出
- デルタベースの増分インデックス（100KB or 50メッセージ閾値）
- デバウンス付きバックグラウンド同期

#### メモリ検索ツール

エージェントが利用できる2つのツール:
- **`memory_search`**: ~700文字のスニペットを返す（ファイルパス、行範囲、関連度スコア付き）
- **`memory_get`**: 特定のメモリファイルを行範囲フィルタ付きで読み取り

#### 実測パフォーマンス

- Local埋め込み: ~50 tokens/sec（M1 Mac, node-llama-cpp）
- OpenAI埋め込み: ~1000 tokens/sec（バッチ使用時）
- 検索レイテンシ: <100ms（10Kチャンク, ハイブリッド検索）
- インデックスサイズ: ~5KB / 1Kトークン（1536次元埋め込み）

### Tool Factory & Self-Extension（ツールファクトリーと自己拡張）

ツールは `AgentTool` を継承した Pydantic クラスとして定義され、エージェント自身が新しいツールを書いて追加できる：

```
Agent reads agent_tools.py → writes new tool class → runtime detects via st_mtime → importlib.reload() → tool usable immediately
```

完全な解説は [[concepts/agents-that-build-themselves]] を参照。

## Orchestration Capabilities

OpenClaw is fundamentally a **gateway-first architecture** — the Gateway serves as the single control plane for routing, sessions, and channel connections. This design makes it naturally suited as an **orchestrator** in multi-agent architectures. The Kilo blog analysis (Brendan O'Leary, May 2026) and community consensus confirm OpenClaw's role as orchestrator when paired with execution specialists like Hermes Agent.

### Core Orchestration Mechanisms

| Mechanism | Description |
|-----------|-------------|
| **Multi-agent routing** | Isolated agent instances with separate workspaces, models, and personas through one Gateway |
| **ACP sub-agent spawning** | `sessions_spawn({ runtime: "acp" })` launches external harnesses (Claude Code, Codex, Gemini CLI, Pi, Hermes Agent) as interchangeable execution backends |
| **Sub-agent lifecycle** | `/acp spawn`, `/acp steer`, `/acp cancel`, `/acp close`, `/acp status` — full orchestration control |
| **Cron scheduling** | Built-in deterministic job scheduling for repeatable coordination |
| **Webhook triggers** | External event-driven agent activation |
| **Agent-to-agent communication** | Session tools for inter-agent messaging |
| **Completion announce channel** | Parent-owned ACP sessions with structured result channel back to parent |

### Hub-and-Spoke Architecture

> "OpenClaw is not a chatbot wrapper around an API for AI models. It's an **operating system for AI agents**. OpenClaw treats AI as an infrastructure problem: sessions, memory, tool sandboxing, access control, and orchestration." — [OpenClaw Architecture Overview](https://ppaolo.substack.com/p/openclaw-system-architecture-overview)

### Orchestrator + Execution Specialist Pattern

A growing architecture pattern (~20% of users in Kilo Reddit analysis) treats OpenClaw as **orchestrator** (planning, decomposition, multi-step coordination, scheduling) and Hermes Agent as **execution specialist** (fast, repeatable task loops). They communicate via the **Agent Client Protocol (ACP)** — a standardized protocol akin to LSP for code editors.

See [[comparisons/hermes-vs-openclaw-architecture]] for the full comparison.

## Lifecycle Management

| Operation | Command |
|-----------|---------|
| Start agent | `openclaw agent --agent main --local -m "hello"` |
| Launch TUI | `openclaw tui` |
| Check status | `openclaw status` |
| View logs | `openclaw logs --follow` |

## Playbooks Available on DGX Spark

| Playbook | Duration | Description |
|----------|----------|-------------|
| **OpenClaw Local Deployment** | 4w | Full setup with LM Studio/Ollama |
| **NemoClaw + Telegram** | 30 min | Bot integration with local inference |
| **Multi-Agent Chatbot** | 1 hr | Multiple agents coordination |

## Related
- [[concepts/openclaw]]
- [[concepts/agent-memory-systems-comparison]] — OpenClaw/Claude Code/Codex メモリシステム比較
- [[entities/telegram-managed-bots]]

- [[entities/nvidia-nemoclaw]] — NemoClaw secure wrapper for OpenClaw
- [[entities/peter-steinberger]] — OpenClaw creator
- [[entities/nvidia-dgx-spark]] — DGX Spark hardware platform
- [[concepts/local-llm/server-dgx-spark]] — Setup guide
- [[concepts/harness-engineering/system-architecture/agent-security-patterns]] — Security patterns
- [[concepts/self-evolving-agents]] — Self-evolving agents taxonomy (OpenClaw = Level 4: Architectural Evolution)
- [[concepts/agents-that-build-themselves]] — Hugo+Ivan workshop: self-extending agents in Pure Python

## References

- docs.openclaw.ai--pi-integration-architecture
- [[raw/articles/2026-02-24_openai_builders-unscripted-ep1-peter-steinberger]] — OpenAI Builders Unscripted interview with Peter Steinberger (Feb 2026)

## Media & Press

- **Builders Unscripted Ep. 1** (OpenAI, Feb 2026): Romain Huet interviews Peter Steinberger about OpenClaw's origin, building with Codex, and open source philosophy. [[raw/articles/2026-02-24_openai_builders-unscripted-ep1-peter-steinberger]]
