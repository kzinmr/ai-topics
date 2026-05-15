---
title: "Hermes Agent vs OpenClaw"
created: 2026-05-14
updated: 2026-05-14
type: comparison
tags: [comparison, hermes-agent, openclaw, ai-agents, agent-architecture, agent-harness, open-source, personal-ai]
sources:
  - raw/articles/2026-05-13_akshaypachaar_hermes-agent-masterclass.md
  - raw/articles/2026-05-06_kilo_hermes-vs-openclaw-when-to-reach.md
  - https://blog.kilo.ai/p/hermes-vs-openclaw-when-to-reach
  - https://kilo.ai/openclaw/vs-hermes
  - https://github.com/nousresearch/hermes-agent
  - https://github.com/openclaw/openclaw
  - https://docs.openclaw.ai
  - https://hermes-agent.nousresearch.com
---

# Hermes Agent vs OpenClaw

> **"Hermes packages a gateway around a learning agent. OpenClaw packages an agent around a messaging gateway."** — Brendan O'Leary, [Kilo Blog](https://blog.kilo.ai/p/hermes-vs-openclaw-when-to-reach) (May 2026)

Both are the closest open-source persistent AI agents. Both are MIT-licensed, messaging-friendly, and self-hosted. But that one architectural inversion drives nearly every practical tradeoff between them.

## Comparison Table

| Dimension | Hermes Agent | OpenClaw |
|---|---|---|
| **Architecture Philosophy** | **Agent-first.** Learning runtime at the core (`AIAgent` class). Gateway added around it. "Batteries included" — Rails approach. | **Gateway-first.** Messaging infrastructure at the core (long-lived Gateway daemon). Agent wrapped around it. "Primitives first" — Linux/Kubernetes approach. |
| **Memory System** | **Three-tier:** (1) Bounded MEMORY.md + USER.md injected as frozen snapshot; (2) SQLite/FTS5 searchable session archive + `session_search`; (3) External memory providers (plugin). | **File-based bootstrap + vector retrieval:** MEMORY.md, SOUL.md, AGENTS.md, USER.md load at session start; daily notes (`memory/YYYY-MM-DD.md`); LanceDB semantic search via `memory_search`. |
| **Skill/Learning System** | **Self-authoring.** Agent auto-creates SKILL.md from task patterns. Post-task procedural capture. Patch-in-place improvement from errors. [[gepa|GEPA]] offline evolutionary optimizer. Curator prunes stale skills. | **Governed + marketplace.** Five-tier precedence system. Explicit user intention required for creation. ClawHub marketplace: 13,700+ community skills. Byte caps, candidate caps, symlink rejection prevent rot. |
| **Identity Layer** | **SOUL.md** — slot #1 in system prompt, before memory/skills. Hand-authored, static, consistent across all sessions and profiles. | **SOUL.md** — bootstrap file loaded at session start. Personality guide with communication style. Can be overridden per-agent via `systemPromptOverrides`. |
| **Execution Backends** | **7 sandbox backends:** local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox. Serverless backends (Modal/Daytona) hibernate when idle. | **CLI backends + sandbox modes:** claude-cli, codex-cli, gemini-cli, Pi via ACP. Sandbox modes: off, non-main, all. Elevated escape hatch for trusted operations. |
| **Model Support** | **Translation layer** routes any provider through 3 API formats. 300+ models via Tool Gateway. Claude, GPT, Gemini, Ollama, OpenRouter, DeepSeek, and more. | **Provider-agnostic.** Anthropic (Opus/Sonnet), OpenAI (GPT-4o/5.5), Google Gemini, OpenRouter, Moonshot, MiniMax, Ollama (local). CLI backends for codex-cli, gemini-cli, Pi. |
| **Messaging Platforms** | **7 platforms:** Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI. Cross-platform conversation continuity. Voice memo transcription. | **11+ platforms:** Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, WebChat. All through one Gateway process. |
| **Scheduling** | Natural-language cron via gateway. Scheduled reports, backups, briefings. | **Deterministic cron** (`jobs.json`). Webhooks. Gmail Pub/Sub. One-shot and recurring. Background task records. Gateway-owned lifecycle. |
| **GitHub Stars / Community** | **~150k stars** (May 2026). Grew from 90k in ~2 months. Built by [[nous-research|Nous Research]]. Active Discord. Smaller but fast-growing ecosystem. | **~372k stars** (May 2026). Created by Peter Steinberger (steipete). 13,700+ community skills on ClawHub. Larger, more mature community. |

## Architecture at a Glance

```
Hermes:   [Messaging Platforms] → Gateway → [AIAgent Core: SOUL → Memory → Skills → GEPA] → Sandboxes
OpenClaw: [Messaging Platforms] → [Gateway Core: Sessions, Routing, Cron, Channels] → Agent Runtime → CLI Backends
```

**Hermes** optimizes for the agent becoming more capable over time — self-improving skills, compounding memory, GEPA optimization. **OpenClaw** optimizes for a persistent assistant reachable from anywhere — 11+ channels, deterministic scheduling, multi-agent routing through a single control plane.

## Verdict

**Choose Hermes** when you want an agent that improves at your workflows over time, need flexible sandbox backends (especially Modal for cloud execution), or are doing research-style work with subagent delegation and rollback safety. The learning loop compounds.

**Choose OpenClaw** when you need to message your assistant from everywhere (11+ platforms), require deterministic cron scheduling, multi-agent orchestration, or access to the largest skill ecosystem (13,700+). The gateway is prod-grade infrastructure.

**Choose both** for complex setups: OpenClaw as orchestrator (planning, scheduling, multi-channel routing) + Hermes as execution specialist (fast, repeatable loops with learning). They communicate via the Agent Client Protocol (ACP).

Neither approach is wrong. Hermes bets on learning. OpenClaw bets on infrastructure. The right choice depends on whether you optimize for a smarter agent or a more connected one.

## Related

- [[hermes-agent]] — Hermes Agent platform deep-dive
- [[nous-research]] — Nous Research, creators of Hermes Agent
- [[gepa]] — GEPA: evolutionary skill optimizer behind Hermes's learning loop
- [[hermes-vs-openclaw-architecture]] — Deeper architecture comparison (source-code level)
