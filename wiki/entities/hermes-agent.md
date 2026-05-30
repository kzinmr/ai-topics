---
title: "Hermes Agent"
type: entity
aliases:
  - hermes-agent
  - nous-hermes
tags:
  - entity
  - ai-agents
  - open-source
  - nous-research
  - self-improving
status: complete
description: "Open-source self-hosted AI agent by Nous Research. Features persistent memory, self-improving skills, and always-on execution. Growing number of users migrating from OpenClaw."
created: 2026-04-27
updated: 2026-05-30
sources:
  - "https://x.com/i/article/2045080054917476451"
  - "raw/articles/2026-04-28_15-hermes-agent-features.md"
  - "https://x.com/i/article/2045935785661349956"
  - "raw/articles/2026-05-13_nvidia_rtx-ai-garage-hermes-agent-dgx-spark.md"
  - "raw/articles/2026-05-06_kilo_hermes-vs-openclaw-when-to-reach.md"
  - "raw/articles/2026-05-15_shann_hermes-agent-operator.md"
  - "raw/articles/2026-05-22_deeplearning-ai_hermes-vs-openclaw-newsletter.md"
  - "https://info.deeplearning.ai/hermes-vs.-openclaw-cybersecurity-alarms-ring-more-interactive-conversations-can-agents-do-human-work"
  - "raw/articles/2026-05-27_mem0-openclaw-hermes-agent-memory.md"
  - "raw/articles/2026-05-29_atal-upadhyay_hermes-harness-architecture.md"
related:
  - "[[concepts/harness-engineering]]"
  - "[[concepts/hermes-agent-use-cases]]"
  - "[[concepts/polymarket-trading-agents]]"
  - "[[concepts/nvidia-rtx-ai-garage]]"
  - "[[entities/openclaw]]"
  - "[[comparisons/hermes-vs-openclaw-architecture]]"
  - "[[entities/qwen]]"
  - "[[entities/nvidia-dgx-spark]]"
  - "[[nous-research]]"
---

# Hermes Agent

> **Definition:** Open-source self-hosted AI agent developed by Nous Research. Features a three-layer model: persistent memory, self-improving skills, and always-on execution.

## Basic Information
- **Developer:** Nous Research (known for YaRN, Nomos, Psyche model families)
- **Release Date:** February 25, 2026
- **License:** Open-source
- **Supported OS:** Linux, macOS, WSL2 (no native Windows support)

## Three-Layer Model

### Knowledge Layer
- Built-in memory, session search, LLM-Wiki skill
- Honcho integration (optional)
- The agent doesn't just answer — it accumulates knowledge over time

### Execution Layer
- Multi-agent profiles, child agents, tool system
- MCP support, persistent machine access
- Tasks can be decomposed, executed in parallel, and delegated

### Output Layer
- Cron jobs, gateway delivery (Telegram/Slack/Discord)
- Web UI, file output
- Results flow into real workflows, not trapped in chat windows

## Three Differentiators

### 1. Persistent Memory

Hermes's memory system is designed for **cache stability over immediate freshness**:

#### Memory Architecture

| Component | Location | Capacity | Role |
|-----------|----------|----------|------|
| **MEMORY.md** | `~/.hermes/memories/` | Hard cap: 2,200 chars | Agent's notes about the world (environment, conventions, experiences) |
| **USER.md** | `~/.hermes/memories/` | Hard cap: 1,375 chars | Agent's notes about the user (preferences, communication style) |
| **Session Search** | `~/.hermes/state.db` (FTS5) | SQLite | Cross-session conversation recall |

Total: ~3,575 characters (~1,300 tokens) travel into every system prompt. Entries separated by § (section sign, U+00A7).

#### Frozen System Prompt Design

Memory is captured **once at session start** and pinned as a frozen block in the system prompt. Changes written via the memory tool go to disk immediately but are NOT reflected in the current session — they appear at the next session start.

**Rationale: prefix caching.** Every major LLM provider caches the prompt prefix, so subsequent turns reuse those tokens at a fraction of the cost. As long as the system prompt doesn't change, the cache holds. Hermes trades intra-session memory freshness for cache-stable long sessions.

**Trade-off:** A user who mentions mid-session switching from npm to pnpm will have that fact written to MEMORY.md immediately, but the agent won't use pnpm until the next session.

#### Memory Tool API

Single tool with three actions: `add` (append, rejects exact duplicates), `replace` (substring-match on existing entry), `remove` (substring-match delete). No entry IDs, no UUIDs — the model addresses past entries by quoting a unique substring. Designed as a constrained API surface to make the model think carefully about what it writes.

#### Auto-Compaction: None

When MEMORY.md hits the 2,200-char hard cap, the next write **fails with an error**. The agent must consolidate by hand. No silent garbage collection, no LRU, no sliding window. The design assumes the model can be trusted to manage 3,575 characters directly.

#### Mem0 Integration

Mem0 is one of eight external memory providers. Activation: `hermes memory setup`. Writes `memory.provider: mem0` into config. Exposes three tools: `mem0_profile`, `mem0_search`, `mem0_conclude`. After each turn, user/assistant exchange ships to Mem0 in a background thread — slow/failed calls never block the conversation. Circuit breaker: 2-minute pause after 5 consecutive failures.

In Hermes, Mem0 fixes the 3,575-char ceiling and adds semantic search to replace substring-match retrieval.

### 2. Self-Improving Skills
- After completing complex tasks (5+ tool calls), skills are automatically created
- Procedures, pitfalls, and verification steps captured as structured markdown files
- On similar tasks, the skill is loaded for fast, accurate execution
- Stored as readable/writable markdown files in `~/.hermes/skills/`

**Curator System** (DeepLearning.AI May 2026):
- Background archiving of skills unused for 90+ days
- LLM determines keep / merge / archive for each skill
- Mechanism to mitigate skill explosion (though not fully preventive. See [[comparisons/hermes-vs-openclaw-architecture|architecture comparison]])

### Agentic Loop (DeepLearning.AI May 2026)
Hermes' internal loop:
1. **Prompt Assembly** — personality (SOUL.md) + instructions + tools + skills + memory + conversation history
2. **Summarization** — compress old messages when exceeding context window
3. **LLM Send** — send assembled prompt to model
4. **Dispatch** — execute tool call / skill execution / user response
5. **Loop** — repeat until final response

This loop contrasts with OpenClaw's Gateway-driven approach. Hermes is agent-centric, OpenClaw is gateway-centric. → [[comparisons/hermes-vs-openclaw]]

### 3. Always-On Execution
- Runs 24/7 on a server
- Connects to Telegram, Discord, Slack, WhatsApp, Signal, Email, 15+ platforms via single gateway
- Natural-language cron ("scan these GitHub repos every morning and summarize")
- Runs unattended

## Comparison with OpenClaw

| Feature | OpenClaw | Hermes |
|---------|----------|--------|
| Learning Loop | static (manual skill install) | closed loop (~15 tool calls to generate skill) |
| Memory | Manual setup / third-party dependency | Built-in bounded curated memory |
| Self-improvement | None | Yes (gets smarter with use) |
| Platform Integration | 50+ (broad) | 15+ (all major) |
| Security | Standard | Strong |
| Token Efficiency | **High** (loads only needed tools) | **Lower** (loads all bundled skills 123+, higher cost) |

## Milestones (May 2026)

- **150,000 GitHub Stars**: Achieved in under 3 months (as of May 19, 2026). Confirmed in Shann's (@shannhk) article
- **Most Used Agent on OpenRouter**: #1 globally in OpenRouter app usage stats (May 2026 week 2). Highest global token usage among all models and frameworks
- **NVIDIA RTX AI Garage Endorsement**: Featured as the central agent framework in NVIDIA's RTX AI Garage program on the official NVIDIA blog (2026-05-13)
- **123 Bundled Skills**: 123 skills included at shipping. Covering GitHub PRs, Obsidian, Google Workspace, Linear, Notion, Typefully, Perplexity, Deep Research, etc.
- **6 Deployment Targets**: Local, Docker, SSH, Daytona, Singularity, Modal
- **20+ Messaging Surfaces**: Telegram, Discord, Slack, Email, Voice, CLI

### Harness Engineering: "Same Model, Better Results"

A key feature explicitly mentioned in the NVIDIA blog: **consistently superior results from Hermes when comparing the same model across different frameworks**. This is because Hermes functions not as a thin wrapper but as an active orchestration layer. → [[concepts/harness-engineering]]

### NVIDIA DGX Spark Integration

The DGX Spark is positioned as the ideal hardware for Hermes Agent:
- **128GB unified memory** for running 120B-class MoE models 24/7
- **Qwen 3.6 35B** (120B-class intelligence in 20GB memory) recommended on DGX Spark
- **Hermes DGX Spark Playbook**: Official NVIDIA setup guide available
- Always-on agent design aligns with DGX Spark's 24/7 operation

→ [[entities/nvidia-dgx-spark]], [[concepts/nvidia-rtx-ai-garage]]

## Real-World Usage Examples (Reddit/X/YouTube Survey)

1. **📞 Pre-call client research** — Auto-enriched dossier before meetings (saves 20-30 minutes)
2. **✉️ Meeting-note to follow-up** — Convert rough notes to polished follow-ups, write TODOs to Obsidian
3. **🎧 Weekly podcast digest** — 10hr→2hr highlights reel via Voxtral + Mistral Large 3 pipeline
4. **📬 Daily news briefings** — Cron delivery from $5 VPS + GitHub student plan + Gemini + Ollama
5. **⚙️ Content-ops pipeline** — Blog creation, cold emails, YC/X/Reddit lead scraping
6. **💬 24/7 personal assistant** — Across Telegram/WhatsApp channels, persistent memory
7. **🛡️ Agent watchdog** — Hermes as 2-hour cron monitoring for OpenClaw, fault detection → auto-recovery (within 15 seconds)

## 15 Features Deep Dive (April 2026)
The article "15 Hermes Agent features you've never touched" (2791 bookmarks, 913 likes, 350K impressions) covers advanced features including:
- Web search and content extraction capabilities
- Cron job automation for recurring tasks
- Skill-based procedural memory system
- Entity and concept wiki management
- Multi-agent orchestration patterns
- Filesystem and terminal integration

## Execution Specialist Role (Dual-Agent Architecture)

Hermes Agent is increasingly used as an **execution specialist** in a dual-agent architecture where OpenClaw serves as the orchestrator and Hermes handles fast, repeatable task execution. They communicate via the **Agent Client Protocol (ACP)**.

This architecture pattern is validated by:
- **Kilo blog analysis** (Brendan O'Leary, May 2026): "OpenClaw as orchestrator (planning, decomposition, multi-step coordination, scheduling) and Hermes as execution specialist (fast, repeatable task loops)"
- **Kilo Reddit analysis** (1,300+ comments): ~20% of users run both tools together with this pattern
- **popularaitools.ai**: "Hermes is significantly faster than OpenClaw on the same model and more lightweight"

### Why Hermes as Execution Specialist

| Strength | Mechanism |
|----------|-----------|
| **Speed** | "Noticeably faster" than OpenClaw on same model — lightweight agent loop |
| **Learning loop** | Self-improving skills get faster/more accurate on repeatable task types |
| **Sandbox backends** | 5 isolated environments (Local, Docker, SSH, Singularity, Modal) |
| **Subagent delegation** | `delegate_task` spawns child agents with isolated contexts for parallel work |
| **Checkpoint/rollback** | Filesystem snapshots before file operations; `/rollback` on failure |
| **execute_code sandbox** | Mechanical pipelines separated from reasoning-heavy subagent delegation |

### ACP Communication

Hermes communicates with OpenClaw via ACP (Agent Client Protocol), the open standard for agent-to-agent communication. OpenClaw spawns Hermes as an ACP session via `sessions_spawn({ runtime: "acp", agentId: "hermes" })`, treating Hermes as an interchangeable execution backend.

**Key limitation:** Hermes's self-evaluation always passes, so external validation is needed. The dual-agent architecture mitigates this — OpenClaw (orchestrator) validates Hermes (executor) output quality.

See [[comparisons/hermes-vs-openclaw-architecture]] for the full comparison.

## Shann's 4-Level Fleet Operation Model (May 2026)

Shann (@shannhk), AI marketer at Espressio and practitioner running Hermes agents in production, published a multi-agent operations guide ([How to Become a Hermes Agent Operator](https://x.com/i/article/2055317817658900480), 2026-05-15).

### 3 Core Components
- **Brain** — `~/.hermes/memories/` contains MEMORY.md (business facts) and USER.md (user preferences). Injected at every session start. Cross-session search via SQLite+FTS5
- **Personality** — Tone defined in `soul.md`. Can assign different personalities (concise, sarcastic, direct, formal, etc.) to 6 agents from one foundation
- **Skillset** — 123 pre-built skills + self-improvement loop. Agents auto-generate new skills as they work

### 4-Level Setup Model

| Level | Configuration | Use Case |
|-------|--------------|----------|
| **Level 1** | Single agent + Control Room | Personal assistant, initial setup |
| **Level 2** | Multi-specialist (direct dialogue) | Role separation, credential scope division |
| **Level 3** | Orchestrator + Specialists + Task Bus | Cross-department workflows, delegation and integration |
| **Level 4** | Level 3 + Cron automation | Weekly SEO reports, server health checks, fully autonomous operation |

### Control Room Pattern
```
/root/vps-agents/          → Control plane (docs, rules, runbooks)
                             No raw secrets stored here

/srv/<agent-name>/data/    → Live runtime (secrets, memory, skills, sessions, cron)
                             Actual instance of each Hermes agent
```

### SEO Agent 21-Step Pipeline (Production Case Study)

Entire process runs in one Docker container. Three sub-agents switch contexts per phase:

| Phase | Steps | Content |
|-------|-------|---------|
| Research + Ideate | 01-07 | Keyword seed → SERP snapshot → competitor extraction → intent analysis → content gap → internal/external validation |
| Production | 08-15 | Angle brief → visual strategy → outline → draft → image generation → flowchart → QA |
| Distribution | 16-21 | Publish prep → schema → internal links → syndication → analytics → monitoring |

### Prototype → Production Methodology

```
Prototype (on Hermes) → 2-3 real-world tests → Fine-tune in dedicated Workspace → Deploy to VPS + Cron
```

Shann: "You can't write a production agent from scratch. You have to grow it. Hermes accelerates that growth."

### Rails vs Linux Framing
Shann's philosophical contrast between Hermes and OpenClaw:
- **Hermes = Rails**: Opinionated defaults, batteries included, agent makes more decisions
- **OpenClaw = Linux**: Primitives, guarantees, explicit control, agent only does what it's told

### Model Operations Strategy
- **Claude Opus 4.7**: Creative work (copywriting, voice, hook generation)
- **Codex (GPT 5.5)**: Structured work (coding, planning, multi-step workflows, browser automation)
- Both used together. Model switching per agent/task via Tool Gateway

→ [[entities/shannhk]], [[concepts/hermes-agent-use-cases]]

## Atal Upadhyay's 9-Part Harness Architecture Analysis (May 2026)

Independent analyst Atal Upadhyay (@atal) published a detailed architectural review mapping Hermes against a nine-part harness framework. The analysis concluded Hermes is "one of the best open-source harnesses in the ecosystem" and confirmed implementations across all nine dimensions:

### Nine-Part Model Assessment

| Component | Hermes Implementation |
|-----------|----------------------|
| **Outer iteration loop** | Provider abstraction — same runtime drives chat-completions, Anthropic Messages, Codex Responses, out-of-process Codex, and Bedrock. Transport adapters normalize tool-call formats. "Much better than Claude Code" for multi-model support |
| **Context management & compression** | Full compression path with auxiliary model summarization. Head/tail protected by token budget. Summary budget scales at ~20% of compressed content (2K-12K range). Old tool outputs pruned before summarization |
| **Skills & tools management** | Registration and exposure are **separate concerns**. Tools register into central registry; toolset layer decides what model sees per run. Scoped by platform/scenario. Narrowable for delegated runs |
| **Subagent management** | Child runs get own task ID, terminal context, structured return. Dangerous commands default to deny. Recursion depth capped. **Gap:** no durable, externally steerable child-run plane |
| **Session persistence & recovery** | SQLite with FTS5 search + WAL journaling. Sessions track source tags, parent-child lineage for compression splits. CLI, messaging platforms, and cron jobs attach to same session plane |
| **System prompt assembly** | Three-tier explicit composition: **stable** (SOUL.md, tool guidance, skills index), **context** (AGENTS.md, CLAUDE.md, .cursorrules with injection scanning), **volatile** (memory snapshots, user profile, timestamp) |
| **Lifecycle hooks** | Two surfaces: plugin hooks (inside harness process, block/rewrite/pass) and filesystem-driven gateway hooks (shell/Python scripts on gateway startup, agent step, etc.) |
| **Permission & safety layer** | Approval gates, scoped permissions per profile, deny-by-default for delegated contexts |
| **Built-in pre-packaged skills** | 123 bundled skills covering GitHub, Google Workspace, Linear, Notion, etc. |

### Beyond the Framework: Three Unique Subsystems

1. **Messaging Gateway** — Broad platform adapter surface (Telegram, Discord, Slack, WhatsApp) routing through shared session model. Compared to OpenClaw's successful UI pattern for long-running agent interaction.
2. **Profile System** — Each profile is an isolated agent root. Two profiles on the same machine behave as completely different agents from state and footprint perspective.
3. **Cron as First-Class Subsystem** — Jobs are durable, gated by same permissions as interactive sessions, delivered through gateway paths, isolated per profile. "Forces unattended operation concerns into the main architecture rather than leaving them as peripheral scripts."

### Compression Lineage — Unique Architectural Detail

On compression, Hermes closes the current SQLite session row, creates a **child session seeded by the summary**, rotates the session ID, and records parent-child lineage. Plugin context engines and memory providers are notified. Long conversations produce a lineage chain instead of one repeatedly rewritten transcript — described as "pretty unique relative to other harness architectures we've reviewed."

### Recommended Next Step: First-Class Orchestration

The analysis identifies the most natural next architectural step: promoting child runs to first-class control-plane objects with run IDs, explicit lifecycle management, external steering, and cleanup semantics that survive parent completion. Hermes already has the substrate (session infrastructure, gateway routing) — the gap is vs. OpenClaw's agent orchestration layer.

→ [[concepts/harness-engineering]], [[comparisons/hermes-vs-openclaw-architecture]], [[entities/openclaw]]

## Sources
- [Hermes Harness Architecture](https://x.com/i/article/2060381072148537344) (2026-05-29, Atal Upadhyay/@atal, X article) — 9-part harness model analysis, unique compression lineage, orchestration gap identification
- [Hermes Agent: What People Are Actually Using It For](https://x.com/i/article/2045935785661349956) (2026-04-26, X article) — usage patterns from Reddit/X/YouTube
- [Hermes Agent + Polymarket - weather trading guide](https://x.com/i/article/2045080054917476451) (2026-04-25, X article) — installation + Polymarket trading
- [How to Become a Hermes Agent Operator](https://x.com/i/article/2055317817658900480) (2026-05-15, Shann/@shannhk, X article) — 4-level fleet operation model, SEO agent 21-step pipeline, prototype-to-production methodology

## References

- 2026-1-month-with-hermes
- hermes-architecture-analysis-kazuki-inamura

- 2026-04-27_2045080054917476451_Hermes-Agent-Polymarket-Self-Learning-Weather-Trading-Bot
- 2026-04-27_2045935785661349956_Hermes-Agent-What-People-Are-Actually-Using-It-For
- 2026-04-28_x-article-15-hermes-agent-features
- 2042539396638085339_What-Hermes-Agent-Can-Do-for-You
