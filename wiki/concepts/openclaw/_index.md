---
title: "OpenClaw — Concepts Index"
type: concept
aliases:
  - openclaw-concepts
  - openclaw-index
  - open-claw-concepts
created: 2026-04-18
updated: 2026-04-19
tags:
  - concept
  - methodology
  - openclaw
  - ai-agents
status: active
sources: []
---

# OpenClaw — Concepts Aggregation

**OpenClaw** is an open-source persistent personal AI agent framework developed by Peter Steinberger (@steipete). It has recorded over 135,000 running instances and became the center of Anthropic's subscription restrictions. It is the upstream project for NVIDIA's NemoClaw.

## Core Philosophy ([[concepts/openclaw/philosophy]])

| Principle | Description |
|------|------|
| **Primitives First** | Provide guarantees, not defaults |
| **Always-On Agent** | Persistent autonomous operation, not session-bound |
| **Explicit > Implicit** | Routing rules are explicitly stated in system prompts |
| **Ship Beats Perfect** | Code is not read — it is "woven" (weave) |
| **Closed Loop Principle** | Self-validating structure: compile → run → test |
| **Local-First** | Local inference, local files, local MCP |

## Design Patterns

### Five-Tier Skill Precedence ([[concepts/openclaw/five-tier-precedence]])
```
1. Workspace skills     (highest priority)
2. User global skills
3. Managed skills
4. Bundled skills       (baseline only)
5. Extra skills         (lowest priority)
```
> "When something breaks, you can track it down with a single grep. No need to guess which skill triggered it."

### Anti-Bloat Policy
- Bundled skills are baseline only
- New skills go to ClawHub first
- Additions to core require "strong product or security reasons"
- Byte caps, candidate caps, symlink denial, verified file opens only

### AGENTS.md Optimization Pattern
Combining OpenClaw's TOOLS.md pattern with Vercel's AGENTS.md pattern:
> "In the task of selecting the right tool from ~50 CLI/APIs, OpenClaw's tool invocation accuracy was better than Hermes." — elvis

## Architecture Deep-Dive (May 2026)

- [[concepts/openclaw-architecture]] — Internal architecture details based on OpenClaw official docs (338 lines). Gateway-first design, WS protocol, embedded agent runtime, sandbox isolation, nodes, queueing, plugin system.
- [[concepts/hermes-agent-architecture]] — Internal architecture details based on Hermes Agent official docs (278 lines). AIAgent-centric design, prompt assembly, persistent state, tool runtime, subagent delegation.

## Architecture Comparison ([[concepts/openclaw/architecture-comparison]])

| Dimension | OpenClaw | Hermes Agent |
|------|----------|--------------|
| **Philosophy** | Primitives First, Linux/K8s | Batteries-included, Rails |
| **Skill Management** | Explicit, user-governed | Self-authoring |
| **Defaults** | Baseline only | 123+ bundled SKILL.md |
| **Debugging** | Single grep | Cross-skill investigation |
| **Growth Model** | Constrained (ClawHub) | Organic (Skill Explosion Problem) |

## Anthropic-OpenClaw Conflict ([[concepts/openclaw/anthropic-conflict]])

In April 2026, Anthropic excluded third-party agents from subscriptions. OpenClaw instances consumed $109.55/day (Opus) compared to $6/day for general developers. 135,000 instances running.

## Ecosystem Tools ([[concepts/openclaw/ecosystem-tools]])

| Tool | Description | Stars |
|--------|------|-------|
| **VibeTunnel** (vt.sh) | Turn any browser into a terminal | — |
| **CodexBar** | OpenAI Codex/Claude Code usage stats | 9.9k |
| **Peekaboo** | macOS CLI + MCP screenshots | 3.1k |
| **mcporter** | Expose MCP as CLI via TypeScript | 3.8k |
| **gogcli** | Google Suite CLI | 6.7k |
| **agent-rules** | Rules for Claude Code/Cursor | 5.7k |
| **tokentally** | LLM token/cost calculator | — |
| **Terminator MCP** | Return terminal output via MCP | — |

## Related Entities

| Entity | Description |
|-------------|------|
| [[entities/peter-steinberger]] | OpenClaw creator. Former PSPDFKit CEO. Developing personal agents at OpenAI |
| [[concepts/openclaw]] | OpenClaw framework details |
| [[entities/nvidia-nemoclaw]] | NVIDIA's enterprise OpenClaw wrapper |

## Product Positioning Framework

> *"OpenClaw had the audience. The mindshare, the GitHub stars... nanoclaw, nullclaw, picoclaw, zeroclaw. All trying to out-OpenClaw OpenClaw. None got Hermes's traction."* — elvis

Hermes's winning strategy: **Don't fight the category definer on their board — create a new game.**

## Decision Framework

| User Profile | Recommendation | Reason |
|---------------------|------|------|
| Wants to start fast | **Hermes** | Opinionated defaults = productive on Day One |
| Needs 100% control | **OpenClaw** | Legibility and scope control are paramount |
| Building custom agents | **Both** | Learn governance from OpenClaw, self-improvement from Hermes |

## Key Quotes

> *"With one command, anyone can run always-on, self-evolving agents anywhere."* — OpenClaw

> *"First they copy some popular features into their closed harness, then they lock out open source."* — Steinberger on Anthropic

> *"@steipete gave the world a new layer in the stack and put a claw in everyone's hand. That's foundational work."* — elvis

> *"You don't even need to use OpenClaw to benefit from OpenClaw — the patterns will show up in everything downstream for years."* — elvis

## See Also

- [[concepts/harness-engineering]] — Harness Engineering (cross-cutting concept)
- [[concepts/harness-engineering/agentic-workflows/interactive-explanations]] — Agentic Engineering Patterns
- [[concepts/local-first-software]] — Local-first software movement
- [[concepts/personal-superintelligence]] — Personal superintelligence
- [[concepts/open-source-ai-destruction]] — Open-source AI destruction debate
- [[comparisons/hermes-vs-openclaw-architecture]] — Detailed architecture comparison
- [[concepts/skill-architecture-patterns]] — Skill architecture comparative analysis
