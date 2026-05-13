---
title: OpenClaw
type: entity
aliases: [openclaw, open-claw, peter-steinberger-openclaw]
created: 2026-04-15
updated: 2026-04-15
status: L2
sources:
  - https://github.com/NVIDIA/OpenClaw
  - https://build.nvidia.com/spark
  - https://nemoclawai.io/blog/getting-started-nemoclaw-dgx-spark/
  - https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html
tags: [entity, framework, local-llm, open-source, agent-communication]
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

### Memory Compaction（Markdownメモリ圧縮）

ベクトルDBや埋め込みを使わないシンプルなアプローチ：

1. 会話が閾値（~8K tokens）を超えたら、別の LLM コールで要約
2. タイムスタンプ付き Markdown ファイルとして `memory/` に追記
3. エージェントは起動時・必要時にこのファイルを読み返す
4. 生の会話トレース（JSON）も SQLite に保存されるが、**主要な検索メカニズムは Markdown ファイル**

> *"People are so surprised that something simple like appending summaries to a markdown file works so well for memories."*

### Tool Factory & Self-Extension（ツールファクトリーと自己拡張）

ツールは `AgentTool` を継承した Pydantic クラスとして定義され、エージェント自身が新しいツールを書いて追加できる：

```
Agent reads agent_tools.py → writes new tool class → runtime detects via st_mtime → importlib.reload() → tool usable immediately
```

完全な解説は [[concepts/agents-that-build-themselves]] を参照。

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
- [[entities/telegram-managed-bots]]

- [[entities/nvidia-nemoclaw]] — NemoClaw secure wrapper for OpenClaw
- [[entities/peter-steinberger]] — OpenClaw creator
- [[entities/nvidia-dgx-spark]] — DGX Spark hardware platform
- [[concepts/local-llm/server-dgx-spark]] — Setup guide
- [[concepts/harness-engineering/system-architecture/agent-security-patterns]] — Security patterns

## References

- docs.openclaw.ai--pi-integration-architecture
- [[raw/articles/2026-02-24_openai_builders-unscripted-ep1-peter-steinberger]] — OpenAI Builders Unscripted interview with Peter Steinberger (Feb 2026)

## Media & Press

- **Builders Unscripted Ep. 1** (OpenAI, Feb 2026): Romain Huet interviews Peter Steinberger about OpenClaw's origin, building with Codex, and open source philosophy. [[raw/articles/2026-02-24_openai_builders-unscripted-ep1-peter-steinberger]]
