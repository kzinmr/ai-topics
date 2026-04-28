---
title: pi (Coding Agent)
type: entity
handle: "@badlogicgames"
created: 2026-04-28
updated: 2026-04-28
tags:
  - entity
  - tool
  - coding-agent
  - harness
  - open-source
  - typescript
related:
  - mario-zechner
  - claude-code
  - coding-agents
  - gemma-4
  - lmstudio
sources:
  - https://patloeber.com/gemma-4-pi-agent/
  - https://github.com/badlogic/pi-mono
---

# pi (Coding Agent)

Minimal coding agent by **Mario Zechner** designed for local, token-efficient coding workflows. Pi strips away bloat to maximize token efficiency — a 4-tool core (`read`, `write`, `edit`, `bash`) that deliberately avoids the feature creep of tools like Claude Code and Cursor.

## Key Facts

| | |
|---|---|
| **Creator** | Mario Zechner (@badlogicgames) |
| **GitHub** | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) |
| **NPM** | `@mariozechner/pi-coding-agent` |
| **Architecture** | 4-package monorepo |
| **Tools** | `read`, `write`, `edit`, `bash` (default) |
| **Model support** | Multi-provider (OpenAI, Anthropic, Google, self-hosted) |
| **Session commands** | `/compact`, `/new`, `/tree`, `/fork` |
| **Execution** | YOLO by default (no confirmation for bash) |

## Core Design

### 4-Tool Philosophy
Pi ships with exactly 4 tools: `read`, `write`, `edit`, `bash`. This minimalism is intentional — fewer tools mean less context overhead, more token efficiency for local models, and simpler reasoning paths.

### Session Commands
- `/compact` → Summarizes older messages to free context
- `/new` → Fresh session
- `/tree` → Navigate session history
- `/fork` → Branch from a past message without losing history

### Skill System
On-demand Markdown-based capability packages. Invoke via `/skill:name` or auto-discovery. Notable community skills include `liteparse` (doc parsing for image-only models), `frontend-slides`, `grill-me` (idea iteration).

## Gemma 4 Integration (patloeber.com, 2026-04)

The article at patloeber.com documents running pi with **Gemma 4 26B A4B** via LM Studio:

- **Model:** Gemma 4 26B A4B (MoE) — 26B total params, only 4B activate per token
- **Provider:** LM Studio at `http://localhost:1234/v1`
- **VRAM:** ~18GB for Q4_K_M (all 26B must be loaded despite MoE routing)
- **Context:** Up to 256K tokens; recommended 128K if VRAM allows
- **Install:** `npm install -g @mariozechner/pi-coding-agent`
- **Config:** Point `~/.pi/agent/models.json` to LM Studio's base URL

Key architectural note: *"Even though the model only activates 4B parameters per token, all 26B parameters must be loaded into memory for fast routing. That's why VRAM requirements are closer to a dense 26B model."*

## Context vs. VRAM Tradeoff

| Use Case | Context | Additional VRAM |
|----------|---------|-----------------|
| Small edits | 16K | ~1 GB |
| Standard coding | 64K | ~4 GB |
| Multi-file refactors | 128K | ~8 GB |
| Full repo context | 256K | ~16 GB |

The article emphasizes the tradeoff between context size and VRAM overhead. Coding agents accumulate heavy session context, making larger contexts highly beneficial for multi-file refactors and full repo understanding.

## Execution Mode

Pi runs **YOLO by default** — executes bash commands without confirmation. Fast but risky. Alternatives: `permission-gate` for prompt confirmation, or `cco`/`sandbox` for containerized safety.

## Extensions (TypeScript modules)

Custom tools, commands, UI, permissions, and sub-agents can be added via TypeScript extensions. Load via `--extension` flag or auto-discovery in `~/.pi/agent/extensions/`. Key trade-off: default YOLO execution prioritizes speed; enable `permission-gate` or sandboxing for production/local reliability.

## Skills Deep Dive

On-demand Markdown-based capability packages following the [Agent Skills standard](https://agentskills.io). Installed via git at user or project level:

- **User-level:** `git clone ... ~/.pi/agent/skills/`
- **Project-level:** `git clone ... .pi/skills/`

Notable community skills include `liteparse` (doc parsing for image-only models), `frontend-slides`, `grill-me` (idea iteration), `gemini-skills`. Invoke via `/skill:name` or auto-discovery.

## Sources

- Patrick Loeber, "How to run a local coding agent with Gemma 4 and Pi," patloeber.com (Apr 2026)
- [GitHub repository](https://github.com/badlogic/pi-mono)
