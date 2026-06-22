---
title: Hermes Agent
created: 2026-05-14
updated: 2026-05-14
type: concept
tags:
  - ai-agents
  - nous-research
  - self-improving
  - memory-systems
  - architecture
  - harness-engineering
  - personal-ai
  - open-source
sources:
  - raw/articles/2026-05-13_akshaypachaar_hermes-agent-masterclass.md
  - https://hermes-agent.nousresearch.com/docs/
aliases: [nous-hermes, hermes-agent-framework]
---

# Hermes Agent

> **One-line pitch:** An open-source personal AI agent that gets better the longer you use it — self-evolving skills, three-tier memory, and GEPA optimization in a single framework. Crossed 90K+ GitHub stars in under two months (May 2026).

Hermes Agent, built by [[nous-research]], is a self-hosted personal AI agent that learns across sessions. It ships with a closed learning loop: the agent remembers context, writes its own reusable skills, prunes them in the background, and validates them offline through an evolutionary engine. No other open-source agent combines all three capabilities — not even [[openclaw]].

## Architecture

Everything flows through a **single `AIAgent` class** in `run_agent.py`. CLI, messaging gateway, batch runner, and IDE integration are all entry points into the same core agent, enabling true platform-agnostic operation.

The core loop is **ReAct-style and synchronous**: build system prompt → check if compression needed → make interruptible API call → execute tool calls → loop. Key architectural details:

| Concern | Implementation |
|---|---|
| **Turn cap** | Hard 90-turn limit per task; subagents share the budget, preventing runaway delegation chains |
| **Execution backends** | 6 environments: Local terminal, Docker, SSH, Modal, Daytona, Singularity — same code, config change |
| **Multi-model** | Translation layer routes any provider through one of three API formats (Claude, GPT, Gemini, local Ollama swappable via one command) |
| **System prompt** | Structured priority stack: SOUL.md → tool definitions → memory files → conversation history → user message |

## Identity Layer: SOUL.md

Before memory or skills load, the agent's identity is defined by `~/.hermes/SOUL.md`. It occupies **slot #1** in the system prompt and defines personality, tone, communication style, and hard limits. Hand-authored and static, it stays consistent across every project and session. If missing, Hermes falls back to a built-in default. SOUL.md is the **fixed frame**; memory and skills are the moving parts inside it.

## Three-Tier Memory System

Hermes does not have a single "memory" — it has three layers operating at different speeds and capacities:

### Tier 1: Markdown Files (always in context)
- **MEMORY.md** (2,200 chars max): Agent's notes about environment, project conventions, tool quirks, lessons learned
- **USER.md** (1,375 chars max): User profile — name, communication preferences, skill level, things to avoid
- Injected as a frozen snapshot at session start. Mid-session writes persist to disk immediately but appear in context next session.
- At ~80% capacity, the agent consolidates entries — merging related facts into denser, information-packed versions.

### Tier 2: SQLite Session Search (on-demand)
- Every CLI and messaging conversation stored in SQLite with **FTS5 full-text search**
- The agent can search weeks of past conversations, then summarize relevant findings via LLM
- Design tradeoff: Tier 1 is always in context but tiny; Tier 2 has unlimited capacity but requires active search + summarization

### Tier 3: External Memory Providers (pluggable)
- **8 pluggable providers** running alongside built-in memory (never replacing it); only one active at a time
- When active: automatic prefetch of relevant memories before each turn, sync after each response, extraction on session end

## Self-Evolving Skills

Skills are the agent's **procedural memory**: Markdown files with YAML frontmatter that encode *how* to do things, not just what it knows. See [[agent-skills]] for the broader concept.

**Progressive disclosure** keeps token costs low:
- **Level 0**: Names + descriptions only (~3K tokens for full catalog)
- **Level 1**: Full skill content loaded on demand
- **Level 2**: Drill into specific reference files within a skill

**Creation triggers** (autonomous via `skill_manage` tool):
- Complex task completion (5+ tool calls)
- Hitting errors/dead ends and finding the working path
- User correction of approach
- Discovery of a non-trivial workflow

The loop: agent encounters problem → solves through trial and error → saves approach as `SKILL.md` → next similar problem loads the proven procedure. Six `skill_manage` actions: create, patch (token-efficient targeted fix), edit (full rewrite), delete, write_file, remove_file.

### The Curator

Without maintenance, skills pile up — dozens of narrow, overlapping playbooks that waste tokens. The Curator is a **background maintenance system** that runs on inactivity check (7 days since last run + 2+ hours idle), spinning up a background agent fork with its own prompt cache.

**Two-phase operation:**
1. **Automatic transitions** (deterministic, no LLM): 30 days unused → stale; 90 days unused → archived
2. **LLM review** (up to 8 iterations): Forked agent surveys all agent-created skills; decides per-skill to keep, patch, consolidate, or archive

**Safety constraints:** Never touches bundled or hub-installed skills; never auto-deletes (worst outcome is archival to `~/.hermes/skills/.archive/`); pre-pass tar.gz snapshot of entire skills directory enables one-command rollback. Pinned skills (`hermes curator pin <skill>`) are protected from archival but still patchable.

## GEPA Integration

The in-agent learning loop has a known weakness: the agent tends toward self-congratulation, overwriting manual customizations with worse versions. [[gepa]] (Genetic-Pareto Prompt Evolution, ICLR 2026 Oral) addresses this as an **offline optimization pipeline** in a companion repository (`NousResearch/hermes-agent-self-evolution`).

**Pipeline:** Read current skill → generate evaluation dataset (synthetic test cases via Claude Opus, real SQLite session history, or hand-curated golden sets) → run GEPA optimizer (read execution traces → understand failure points → generate candidate variants) → evaluate via LLM-as-judge scoring with rubrics → constraint gates (100% test suite pass, <15KB, caching compatibility, semantic drift guard) → best variant goes out as a **PR** (never a direct commit).

**Cost:** ~$2–10 per optimization run. No GPU required — everything through API calls. Effective when you hit a wall without wanting to invest in full fine-tuning (RL/GRPO).

## Profiles: Multi-Agent Isolation

Hermes supports multiple fully isolated agents via **profiles**. Each profile has its own config, memory, skills, sessions, and SOUL.md — sharing nothing by default. The `--clone` flag copies the default profile's config and `.env` as a starting point. Common patterns: programmer (routing execution through Claude Code), designer (trained on visual style references), researcher (daily digest cron job). Each profile can have its own Telegram bot.

## Cron Scheduler: Plain English Jobs

Hermes ships with a built-in scheduler. The gateway daemon ticks every 60 seconds, runs due jobs in isolated agent sessions, and delivers output to any messaging platform. **Jobs are described in plain English** — no cron expressions needed. Syntax examples: `/cron add 30m "Remind me to check the build"`, `/cron add "every 2h" "Check server status"`, `/cron add "0 9 * * 1-5" "..."` for precise control. Jobs can chain output via `context_from` flag, and skills can be attached via `--skill`. Jobs survive restarts (`~/.hermes/cron/jobs.json`).

## Comparison with OpenClaw

[[openclaw]] is the closest open-source comparison — both are persistent, messaging-friendly agents — but they make opposite architectural choices. A clean framing from the Kilo blog: **"Hermes packages a gateway around a learning agent. OpenClaw packages an agent around a messaging gateway."**

| Dimension | Hermes Agent | OpenClaw |
|---|---|---|
| **Learning loop** | Closed loop (autonomous skill creation) | Static (manual skill installation) |
| **Memory** | Built-in bounded curated memory (3 tiers) | Manual setup / third-party dependent |
| **Self-improvement** | Yes — gets better with use | No |
| **Platform integrations** | 15+ (major platforms) | 50+ (broad coverage) |
| **Architecture focus** | Gateway around a learning agent | Agent around a messaging gateway |
| **Execution speed** | Noticeably faster on same model (lightweight loop) | Heavier runtime |

In production, the two are increasingly used together: OpenClaw as orchestrator (planning, coordination, scheduling) and Hermes as execution specialist (fast, repeatable task loops), communicating via ACP (Agent Client Protocol).

See [[comparisons/hermes-vs-openclaw-architecture]] for a full side-by-side analysis.

## Key Facts

- **Developer:** [[nous-research]]
- **Released:** February 25, 2026
- **License:** Open-source (MIT)
- **Stars:** 140K+ (May 2026)
- **Skills Hub:** 687 skills across 18 categories (87 built-in, 79 optional, 16 from Anthropic, 505 from LobeHub)
- **Most Used Agent on OpenRouter** (May 2026)
- **Endorsed by NVIDIA RTX AI Garage** as a central agent framework
- **Configuration:** `~/.hermes/config.yaml` (non-secret), `~/.hermes/.env` (secrets), `~/.hermes/state.db` (SQLite/WAL/FTS5)

## See Also

- [[entities/hermes-agent]] — Entity page with milestones and usage patterns
- [[concepts/harness-engineering/agent-harness]] — The broader class of infrastructure Hermes belongs to
- [[concepts/gepa]] — The offline optimization pipeline
- [[concepts/agent-skills]] — Reusable procedural memory for agents
- [[entities/akshay-pachaar]] — Author of the masterclass source article
- [[comparisons/hermes-vs-openclaw-architecture]] — Full architecture comparison
- [[concepts/nvidia-rtx-ai-garage]] — NVIDIA's endorsement and DGX Spark integration
