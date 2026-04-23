---
title: Build the Harness, Not the Code: Staff/Principal Engineer's Guide to AI-Agent Systems
category: other
status: active
---

# Build the Harness, Not the Code: Staff/Principal Engineer's Guide to AI-Agent Systems

**Source:** Vitthal Mirji  
**Date:** February 2026  
**URL:** https://vitthalmirji.com/2026/02/build-the-harness-not-the-code-a-staff/principal-engineers-guide-to-ai-agent-systems/  
**Crawled:** 2026-04-23  

## 🔑 Core Thesis & Key Facts
> *"A team at OpenAI shipped a production product with **zero lines of manually-written code**... They estimate they built this in about 1/10th the time it would have taken to write the code by hand."*

- **Scale & Velocity:** 1M lines in 5 months. Started with 3 engineers, grew to 7. Averaged **3.5 PRs/person/day**. Throughput *increased* as team scaled.
- **Operating Principle:** `humans steer, agents execute`. Focus on environment design, scaffolding, and compounding returns, not implementation speed.
- **Heuristic:** `anything that helps humans ship better software faster usually helps agents do the same.`
- **Mindset Shift:** `AI doesn't erase engineering fundamentals; it magnifies them. Strong systems get stronger. Fragile systems fail faster.`

## 📖 3 Core Harness Lessons

### 🔹 Lesson 1: Give Agents a Map, Not a Manual
Giant instruction files fail due to context scarcity, instant rot, and verification difficulty.
> *"Adding an auto-generated AGENTS.md summary reduced task success by roughly 2-3 percentage points while increasing token cost by about 20-30%."*

| Ecosystem | Index File | Structure | Enforcement |
|-----------|------------|-----------|-------------|
| **OpenAI** | `AGENTS.md` (~100 lines) | `docs/` with design-docs, exec-plans, references | CI linters, doc-gardening agent |
| **Claude** | `CLAUDE.md` (50-120 lines) | `.claude/` (agents, hooks, skills) + `docs/` | Lifecycle hooks (15 events) |

> *"If it's a suggestion, use CLAUDE.md. If it's a requirement, use hooks."*

### 🔹 Lesson 2: Automate Cleanup, or Drown in It
> *"OpenAI's team spent every Friday - 20% of their week - cleaning up 'AI slop.'"*
- **Golden Principles:** 5-10 mechanical rules. Favor "boring", composable tech.
- **Prescriptive Errors:** Lint failures must tell the agent *how* to fix them.
- **Claude Hook Enforcement Example:** Runs after every file write — blocks raw console.log, auto-formats, runs eslint --fix.

### 🔹 Lesson 3: Context is Infrastructure, Not Documentation
> *"From the agent's point of view, anything it can't access in-context while running effectively doesn't exist."*
- Push decisions from chat/Slack to repo-local, versioned artifacts.
- **App Legibility:** Per-worktree instances, ephemeral observability, artifacts for state tracking.
- Agents routinely run single tasks for **upwards of six hours**.

## ⚙️ Operational Primitives & 10 Tips
**Primitives:** `Skills` (HOW) → `Shell/MCP` (DO) → `Compaction` (CONTINUITY)

| Tip | Focus | Action |
|-----|-------|--------|
| 1-5 | Skill Design | Write routing logic descriptions, add negative examples, embed templates, design for long runs, explicit invocation |
| 6-10 | Security/Networking | Treat skills+networking as high-risk, standard artifact handoffs, two-layer allowlists, secure credential injection |

- **Production Impact:** Glean's Salesforce skill improved eval accuracy from **73% → 85%** and reduced **time-to-first-token by 18.1%**.

## 🪜 11-Step Autonomy Ladder
1. Validate codebase state → 2. Reproduce bug → 3. Record evidence → 4. Implement fix → 5. Validate fix → 6. Record verification → 7. Open PR → 8. Review → 9. Test → 10. Merge → 11. Monitor

## 🏗️ Architecture Enforcement
- **Strict Boundaries:** Dependencies flow left-to-right only (Types → Config → Repo → Service → Runtime → UI). Cross-cutting concerns enter via `*Providers*` only.
- **Philosophy:** `enforce boundaries centrally, allow autonomy locally.`
