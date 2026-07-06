---
title: OpenClaw
type: entity
aliases: [openclaw, open-claw, peter-steinberger-openclaw]
created: 2026-04-15
updated: 2026-05-28
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
  - raw/articles/2026-04-14_china-briefing_china-agentic-ai-openclaw-boom.md
  - raw/articles/2026-05-27_mem0-openclaw-hermes-agent-memory.md
  - https://x.com/i/article/2059652660022910976
tags:
  - entity
  - framework
  - local-llm
  - open-source
  - agent-communication
  - architecture
  - orchestration
  - memory-systems
  - china
  - agent-safety
  - mem0

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

OpenClaw's architecture was detailed through a Pure Python rebuild in the February 2026 workshop "Building Your Own OpenClaw from Scratch" by Hugo Bowne-Anderson + Ivan Leo.

### Hooks System

Composable side-effects added to agent lifecycle events:

```
on_model_response → Telegram send / Rich terminal output
on_tool_call      → Visual diff display / logging
on_tool_result    → Database recording / observability
```

The core loop **knows nothing about hooks** — it simply calls `emit()`. Telegram integration and logging can be added without a single line of change to the core loop.

### Memory System (File-First Hybrid Search Memory) [[comparisons/agent-memory-systems-comparison]]

OpenClaw adopts a Markdown-driven memory system with **files as the single source of truth**. It eschews vector DB dependency found in traditional RAG, featuring **hybrid search (BM25 + vector)** and **automatic embedding provider selection**.

Source: [[raw/articles/2026-01-25_snowan-gitbook_openclaw-memory-system-deep-dive]] (OpenClaw commit f99e3dd, Jan 2026)

#### Three-Layer Memory Structure

| Layer | Storage Location | Content | Load Condition |
|------|-----------------|---------|---------------|
| **Ephemeral (Daily Log)** | `memory/YYYY-MM-DD.md` | Append-only log of daily activities and decisions | Auto-loaded at session start: today + yesterday's logs |
| **Durable (Persistent Knowledge)** | `MEMORY.md` | Critical decisions, project conventions, long-term TODOs | **Private sessions only** — not shared in group contexts |
| **Session (Conversation History)** | `sessions/YYYY-MM-DD-<slug>.md` | Conversation transcripts with LLM-generated descriptive slugs | Previous conversation auto-saved at session start; full-text searchable |

#### Chunking Algorithm

Sliding window + overlap method:
- **Target**: ~400 tokens/chunk (~1600 chars)
- **Overlap**: 80 tokens (~320 chars) to prevent boundary context loss
- **Line-aware**: Accurate source attribution with line numbers
- **SHA-256 hash dedup**: Same content → cache hit → no re-embedding needed

#### Hybrid Search: BM25 + Vector

Weighted score fusion (default: **70% vector + 30% BM25**):

| Search Method | Strengths | Implementation |
|--------------|-----------|---------------|
| **Vector Search (Semantic Similarity)** | Concept matching ("gateway host" ≈ "machine running gateway") | SQLite + sqlite-vec extension / cosine similarity |
| **BM25 Search (Lexical Match)** | Exact tokens (error codes, function names, IDs) | SQLite FTS5 |

#### Automatic Embedding Provider Selection

**Local → OpenAI → Gemini** fallback chain:
1. **Local** (node-llama-cpp): embeddinggemma-300M (~600MB), privacy-focused, offline-capable, slow
2. **OpenAI** (text-embedding-3-small): 1536 dimensions, fast, 50% cost reduction via Batch API
3. **Gemini** (gemini-embedding-001): 768 dimensions, free tier available

#### Cache-First Embedding + Batch Optimization

- SHA-256 hash-based dedup: same paragraph appearing in multiple files → embed only once
- OpenAI Batch API: 50% cost reduction vs synchronous API
- Real example: 10,000 chunks → sync $0.20 → Batch $0.10 → 50% cache hit → $0.05

#### Pre-Compaction Flush [[concepts/context-engineering/context-compaction|Context Compaction]]

OpenClaw's most innovative memory feature. When a conversation approaches the context window limit, it triggers a **silent agent turn** to prompt writing to persistent memory **before** context compaction.

- At 200K context, triggers at ~80% usage
- Normally `NO_REPLY` (silent if nothing important to save)
- Only once per compaction cycle (spam prevention)
- Skipped in read-only sandbox mode

#### Session Index

- JSONL parsing to extract user/assistant messages
- Delta-based incremental indexing (100KB or 50-message threshold)
- Debounced background sync

#### Memory Search Tools

Two tools available to the agent:
- **`memory_search`**: Returns ~700 char snippets (with file path, line range, relevance score)
- **`memory_get`**: Reads a specific memory file with line-range filtering

#### Live System Prompt Design (vs Hermes' Frozen Memory)

OpenClaw takes the opposite approach to Hermes on when memory is visible. **MEMORY.md is re-injected fresh every turn** as part of the "Project Context → Workspace Files" block. Mid-session writes are visible immediately on the next turn.

**Trade-off:** Token overhead — maintainers report 20-30% of every turn's input is bootstrap files re-shipped each time. Large MEMORY.md files get fully injected even when `memory_search` and `memory_get` are available, creating redundancy.

Compared to Hermes: Hermes freezes memory at session start for prefix-cache optimization; OpenClaw re-injects for immediate visibility. Two coherent answers to the same design question: cache stability vs. freshness.

#### Dreaming: Three-Phase Memory Consolidation

OpenClaw's optional consolidation mechanism runs in the background with three phases (docs.openclaw.ai/concepts/memory):

| Phase | Function |
|-------|----------|
| **Light Sleep** | Ingest and stage short-term memories |
| **REM Sleep** | Reflect and extract patterns |
| **Deep Sleep** | Promote qualified memories to MEMORY.md |

Promotion is gated by three thresholds, all of which must pass: `minScore`, `minRecallCount` (memory recalled at least N times), and `minUniqueQueries` (triggered by at least N distinct search queries). A weighted scoring rule combines relevance, frequency, query diversity, recency, consolidation, and conceptual richness. Only memories that prove useful across multiple recalls get promoted.

#### Active Memory Mode

Optional blocking sub-agent that fires **before each reply** in interactive persistent sessions. Searches stored memory against the current message and injects relevant facts into context before the main turn begins. Recommended default: `recent` mode (current message + short conversation tail). Not active for headless tasks or one-shots.

#### Mem0 Plugin Integration

Mem0 for OpenClaw is the npm package `@mem0/openclaw-mem0`:
```bash
openclaw plugins install @mem0/openclaw-mem0
openclaw mem0 init --mode open-source
```

Adds eight memory tools replacing the native two-tool surface: `memory_search`, `memory_add`, `memory_list`, `memory_get`, `memory_update`, `memory_delete`, `memory_event_list`, `memory_event_status`.

Two modes:
- **Platform**: conversations sent to api.mem0.ai, requires `MEM0_API_KEY`
- **Open-Source**: no Mem0 API key; uses local LLM for extraction and embeddings

Default: skills mode (triage → recall → dream protocol). Per-user scoping via `userId`.

#### Measured Performance

- Local embedding: ~50 tokens/sec (M1 Mac, node-llama-cpp)
- OpenAI embedding: ~1000 tokens/sec (with batching)
- Search latency: <100ms (10K chunks, hybrid search)
- Index size: ~5KB / 1K tokens (1536-dim embeddings)

### Tool Factory & Self-Extension

Tools are defined as Pydantic classes inheriting `AgentTool`, and the agent itself can write and add new tools:

```
Agent reads agent_tools.py → writes new tool class → runtime detects via st_mtime → importlib.reload() → tool usable immediately
```

See [[concepts/agents-that-build-themselves]] for the full explanation.

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
- [[entities/openclaw]]
- [[comparisons/agent-memory-systems-comparison]] — OpenClaw/Claude Code/Codex memory system comparison
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

## China Adoption & Market Impact (2026)

In early 2026, OpenClaw spread virally in China, evolving from a developer community phenomenon into a nationwide movement involving cloud giants, local governments, and large enterprises. Details in [[concepts/china-openclaw-agentic-boom]].

### Structural Factors Enabling Adoption

1. **Cheapest API inference costs in the world**: Price competition between Alibaba, Baidu, ByteDance, MiniMax, etc. made high-frequency agent workflows economically viable for individuals and SMBs
2. **DeepSeek effect**: MoE, sparse attention, and MLA reduced compute requirements for frontier-level inference
3. **Inference-side demand shift**: China's daily AI token consumption grew from 100T → 140T tokens (late 2025 → March 2026, +40%)

### Simultaneous Response from Big 5 Cloud Providers

All 5 major providers (Alibaba Cloud, Tencent Cloud, ByteDance Volcano Engine, JD Cloud, Baidu Cloud) offered one-click OpenClaw deployment within days. Tencent launched QClaw (WeChat mini-program, 1.3 billion users), WorkBuddy, and ClawPro (enterprise). ByteDance launched an official China-hosted OpenClaw mirror on April 1, 2026.

### Government Support

- Shenzhen Longgang District: Up to RMB 10 million (~$1.4M) subsidies for One-Person Companies (OPCs) using AI agents
- Wuxi City: Up to RMB 5 million (~$730K) for OpenClaw-powered robotics
- MIIT: Developing national standards for AI agents

### Security Exposure

- CNCERT: ~23,000 users' assets exposed to the public internet
- Asia Tech Lens: 135,000+ exposed instances, of which 42,000+ had authentication bypass (February 2026)
- 13% of skills on ClawHub/skills.sh had critical vulnerabilities (Snyk survey)

### Service Marketplace

Installation and setup services ranging from RMB 50–700 ($7–100) appeared on Taobao/Xianyu. Free installation events at Baidu Beijing HQ and Tencent Shenzhen office drew hundreds to thousands of attendees.

## Media & Press

- **Builders Unscripted Ep. 1** (OpenAI, Feb 2026): Romain Huet interviews Peter Steinberger about OpenClaw's origin, building with Codex, and open source philosophy. [[raw/articles/2026-02-24_openai_builders-unscripted-ep1-peter-steinberger]]
- **China Briefing** (Apr 2026): Giulia Interesse reports on the OpenClaw viral adoption in China — cloud wars, government subsidies, security risks. [[raw/articles/2026-04-14_china-briefing_china-agentic-ai-openclaw-boom]] → [[concepts/china-openclaw-agentic-boom]]

## Summary
OpenClaw (originally "Clawdbot") is an open-source, always-on AI assistant framework created by Peter Steinberger (former PSPDFKit CEO). It deploys autonomous agents that run continuously on a user's machine, self-evolve through interaction, and integrate deeply with the local environment via shell access, file system operations, and MCP server integration. OpenClaw represents the "always-on agent" paradigm — an AI that persists across sessions rather than being invoked statelessly per query.


## Key Ideas
- **Always-On Architecture**: Unlike stateless chat interfaces, OpenClaw agents run as persistent daemon processes that maintain session state, memory, and context across interactions
- **Self-Evolving Capabilities**: Agents can modify their own configuration, install new tools, and extend their capabilities based on user needs and observed patterns
- **Local-First Design**: All agent execution happens on the user's machine, providing low latency, privacy, and the ability to interact with local files, terminals, and applications
- **Tool-Augmented**: OpenClaw agents can execute shell commands, edit files, browse the web, use MCP servers, and interact with local applications — far beyond simple text generation
- **NVIDIA NemoClaw Integration**: NVIDIA's enterprise-hardened distribution of OpenClaw adds secure sandboxing, GPU acceleration, and enterprise governance features
- **Gateway + Orchestrator Architecture**: OpenClaw employs a two-component architecture — a Gateway (self-hosted bridge connecting to LLM APIs) and an Orchestrator (the agent runtime that manages tool execution, memory, and session lifecycle)


## Terminology
- **Gateway**: The self-hosted bridge component that manages LLM API connections, routing requests through configurable providers (OpenAI, Anthropic, local models, etc.)
- **Orchestrator**: The agent runtime that manages tool execution, memory persistence, session lifecycle, and the agent's core loop
- **NemoClaw**: NVIDIA's enterprise distribution of OpenClaw, adding sandboxed execution via Firecracker microVMs, GPU-accelerated inference, and audit logging
- **MCP Server Integration**: OpenClaw agents can connect to Model Context Protocol (MCP) servers, giving them access to standardized external tool ecosystems
- **Always-On Persistence**: The agent maintains a rolling window of conversation history, file system state, and learned behaviors across machine restarts


## Examples/Applications
- **Personal Assistant**: An OpenClaw agent running 24/7 on a developer's machine, managing email triage, calendar scheduling, and file organization
- **Development Copilot**: Agent integrated with local dev environment, managing git operations, running tests, and assisting with code reviews
- **Research Assistant**: Always-on agent monitoring RSS feeds, summarizing articles, and maintaining a personal knowledge base
- **Home Automation Hub**: OpenClaw connected to local IoT devices and MCP servers, managing home automation through natural language


## Related Concepts
- [[concepts/agent-harness-primitives]]
- [[concepts/security-and-governance/agent-sandboxing]]
- [[entities/hermes-agent]]
- [[entities/peter-steinberger]]
- [[entities/nvidia-nemoclaw]]


## Sources
- [OpenClaw GitHub Repository](https://github.com/OpenClaw/OpenClaw)
- [OpenClaw Demystified: The AI Agent That Runs on Your Machine | O. Wulveryck](https://blog.owulveryck.info/2025/10/11/openclaw-demystify-the-ai-agent-that-runs-on-your-machine.html)
- [NVIDIA NemoClaw: Enterprise AI Agent Development Framework](https://developer.nvidia.com/nemoclaw)

