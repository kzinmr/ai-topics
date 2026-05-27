---
title: Galileo Eval Engineer
type: entity
created: 2026-05-27
updated: 2026-05-27
tags:
  - evaluation
  - coding-agents
  - claude-code
  - codex
  - agent-evaluation
  - agent-skills
  - observability
  - developer-tooling
sources:
  - raw/articles/2026-05-19_galileo_eval-engineer-for-claude-codex.md
  - https://github.com/Galileo-Agent-Labs/eval-engineer
  - https://galileo.ai/blog/introducing-eval-engineer-bringing-eval-expertise-to-claude-and-codex
related:
  - entities/pratik-bhavsar
  - concepts/infrastructure-noise-agent-evals
  - concepts/skill-architecture-patterns
  - concepts/agentic-ai-skills
  - concepts/process-reward-models-agent-eval
---

# Galileo Eval Engineer

**Eval Engineer** is an open-source skill bundle for [[entities/claude-code]] and [[OpenAI Codex]] that brings professional evaluation engineering practices into coding agent workflows. Created by **Galileo Agent Labs** (a division of Galileo AI, now part of Cisco), it was announced on May 19, 2026 by [[entities/pratik-bhavsar|Pratik Bhavsar]] and Paul Lacey.

| | |
|---|---|
| **Repository** | [Galileo-Agent-Labs/eval-engineer](https://github.com/Galileo-Agent-Labs/eval-engineer) |
| **License** | Open source |
| **Status** | Alpha (May 2026) |
| **Platform** | Claude Code, OpenAI Codex |
| **Install** | `uvx --from git+... eval-engineer install` |

## Overview

Eval Engineer bridges three contexts that most developers cannot hold simultaneously:

1. **Codebase knowledge** — how the app is built
2. **Galileo observability** — how the app behaves (traces, metrics, log streams)
3. **Eval expertise** — which evidence matters, how to turn failures into reusable eval cases, where fixes belong

It produces three artifacts per run: a **diagnosis**, a **bounded fix plan**, and a **verification plan** with exact commands to prove the fix worked.

> "Agent observability tells you what happened. Eval engineering tells you what to do next. Eval Engineer turns that workflow into executable skills inside the coding agent."

## Architecture

### Installation

Eval Engineer ships as a Python installer that writes repo-local skill files:

```
your-agent-repo/
  .galileo/
    config.yml            # editable files, verification commands, evidence paths
    current/              # active evidence + skill output
    sessions/             # append-only history
    eval-dataset/         # reusable eval cases
    learnings.md          # team knowledge
  .claude/skills/eval-*   # Claude Code command skills
  .agents/skills/eval-*   # Codex command skills
```

No Galileo credentials required at install time; credentials are only needed when skills fetch or write Galileo evidence.

### Command Surface

| Command | Purpose |
|---------|---------|
| `/eval-engineer` | Router: inspects working set and routes to the right specialist |
| `/eval-setup` | Prepares `.galileo/` working set, config, editable files, verification commands |
| `/eval-fetch` | Imports Galileo evidence (log-stream URL, trace ID, time window, exported packet) |
| `/eval-measure` | Checks whether metrics match the use case (fix measurement before fixing behavior) |
| `/eval-diagnose` | Root cause analysis from evidence → diagnosis.md + fix-plan.md + verification-plan.md |
| `/eval-cost` | Reduces tokens/latency/tool calls without quality regression |
| `/eval-audit` | Launch-readiness, safety, metric coverage, production-readiness review |

In Claude Code, invoke as slash commands (`/eval-diagnose`). In Codex, use `$eval-diagnose`.

## RCA Workflow

The canonical loop from "metric dropped" to "verified fix":

1. **Fetch**: `/eval-fetch` ingests Galileo log-stream evidence into a compact `debug-packet.json` (tens of KB, not a raw trace dump)
2. **Diagnose**: `/eval-diagnose` writes `diagnosis.md`, `fix-plan.md`, and `verification-plan.md`
3. **Apply & Verify**: Coding agent edits files within the bounds declared in `.galileo/config.yml`, runs local tests + Galileo canary comparison
4. **Ship**: PR with auditable artifacts

### Concrete Example

A production billing-support agent started routing billing disputes to general support (`tool_selection_quality`: 0.80 → 0.33). The fix loop:

- **Diagnosis**: Tool description ambiguity in `tools/descriptions.yml` — `escalate_to_support` description too broad, swallowing billing cases
- **Fix**: Tighten tool description + add routing rule to system prompt
- **Verify**: Local pytest + Galileo canary comparison → `tool_selection_quality` recovered to 0.83, no regression on adjacent categories
- **Artifact**: Candidate eval case proposed for human review

## Design Principles

### Loose Coupling to App, Tight Coupling to Workflow
The skill does not assume one framework, agent shape, metric, or folder layout. It defines the repeatable loop: read evidence → diagnose → propose bounded change → verify.

### Bounded by Design
Editable files declared in `.galileo/config.yml`. Skill prefers small changes to prompts, tool descriptions, routing rules, retrieval settings, and eval cases. Bigger decisions (changing models, adding tools, swapping frameworks) stay with the developer.

### Artifact-Driven
Every run leaves behind `diagnosis.md`, `fix-plan.md`, `verification-plan.md`, and before/after evidence packets. This makes agent reasoning auditable, transferable, and testable.

### Domain Knowledge Out of Core
Core skill handles the generic loop. Galileo-specific metrics, tokenomics, RAG, URL parsing, or OWASP knowledge lives in focused references and sub-skills.

## What It Is Not

- **Not a replacement for Galileo** — Galileo remains the system of record for traces, metrics, and scored evidence
- **Not a magic self-improving agent** — Human owns product decisions, merge decisions, and architecture changes
- **Not framework-specific** — Works across RAG apps, tool-calling agents, agentic workflows, and custom harnesses
- **Cannot make weak evals strong** — If traces are missing or metrics are wrong, `eval-measure` exists to fix measurement first

## Persona-Based Usage

| Persona | Primary Use |
|---------|-------------|
| **AI Engineer** | Development loop: `eval-diagnose` for quality, `eval-cost` for efficiency |
| **Researcher** | Compare behaviors across prompts, models, eval strategies; learn which eval design produces reliable signal |
| **FDE** | Field debugging accelerator: messy customer evidence → clear diagnosis + fix plan |
| **SRE** | Production RCA and regression response: classify whether issue is model behavior, tool failure, retrieval drift, latency, cost, or data quality |

## Customization

Primary customization via `.galileo/config.yml`: app type (RAG/agent/workflow/harness), editable files, off-limits files, verification commands, quality gates, risk profiles. Team knowledge in `.galileo/learnings.md`.
