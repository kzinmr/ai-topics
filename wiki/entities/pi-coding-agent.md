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

## Podcast: Syntax #976 (Feb 2026)

The Syntax.fm episode "Pi - The AI Harness That Powers OpenClaw" (with Armin Ronacher and Mario Zechner, hosts Wes Bos & Scott Tolinski) provides the most comprehensive public discussion of Pi's design philosophy and architecture.

### Pi's Core Definition

> *"Pi is a while loop that calls an LLM with four tools. The LLM gives back tool calls or not, and that's it. It tries to be minimal because it turns out that the current generation of LLMs are really good at just reading, writing, editing files, and calling bash."* — **Mario Zechner**

### "Bash is All You Need"

The podcast's central thesis: modern LLMs (especially Claude 3.7/Sonnet) are extensively trained on bash commands and shell usage. Rather than building complex agent frameworks with custom tools for every scenario, Pi provides a minimal environment where the agent can write its own scripts. This makes Pi the underlying technology for **OpenClaw** (Cloudbot/Moltbot).

### Steering Queue

Pi includes a unique **steering queue** mechanism — users can send messages to the agent *while* it is executing a long-running task to correct its course mid-execution. This addresses the "agent drift" problem where an agent goes in the wrong direction and the user has to wait for the session to finish before correcting.

### Self-Modifying Skills (Hot Reloading)

A key Pi innovation: the agent can write new tools or modify existing skills during a session, and Pi loads them immediately without restart:

> *"My browser skill changes effectively every three days because there is a new cookie banner I have to dismiss... it can fix itself because it has everything within its control."* — **Armin Ronacher**

### MCP Critique vs Pi Approach

The podcast critiques MCP on two grounds:
1. **Not composable** — Data must pass through the LLM's context window to move between tools, which is wasteful and leads to context exhaustion
2. **Rigid** — MCP servers often require a full agent restart to update

Pi's alternative: let the agent write and modify its own scripts locally. Instead of loading a massive database into context, the agent writes a script (e.g., `jq`) to filter data locally and only returns relevant bits to the LLM.

### Prompt Injection Concerns

The podcast addresses prompt injection as an unresolved problem for autonomous agents. If an agent has tools to search the web and read local files, a malicious website can include hidden exfiltration instructions. The theoretical "Camel Paper" fix (two LLMs: one for policy, one for data) often breaks utility. Current conclusion: no foolproof way to separate user instruction from malicious data in the same context window.

### "Code Is Truth" Memory Philosophy

Mario argues against complex RAG/embedding systems for coding. His approach: give the agent a simple map of the folder structure and let it read files as needed. **"Code is truth."**

### MAM: Master of Mischief

Mario's personal Slack bot that uses `jq` on a JSONL log of all channel history to provide "infinite memory" — a practical demonstration of Pi's philosophy applied to chatbot memory.

## Sources

- Patrick Loeber, "How to run a local coding agent with Gemma 4 and Pi," patloeber.com (Apr 2026)
- [GitHub repository](https://github.com/badlogic/pi-mono)
- Syntax.fm #976 — "Pi - The AI Harness That Powers OpenClaw" (Feb 4, 2026)
  - [Transcript](https://syntax.fm/show/976/pi-the-ai-harness-that-powers-openclaw-w-armin-ronacher-and-mario-zechner/transcript)
  - Raw: raw/articles/2026-02-04_pi-syntax-fm-podcast.md

## See Also

- [[gemma-4]] — Open-weight MoE model commonly used with pi for local coding agents.
- [[mario-zechner]] — Creator of pi coding agent.
- [[claude-code]] — Anthropic's coding agent that pi positions as an alternative to.
- [[coding-agents]] — AI agents for software engineering tasks and tooling.
- [[lmstudio]] — Local inference server used to run models with pi.
- [[openclaw]] — Open-source agent framework built on top of Pi.
