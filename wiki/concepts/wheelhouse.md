---
title: "Wheelhouse"
type: entity
tags:
  - agent-harness
  - agent-orchestration
  - ai-agents
  - multi-agent
  - agentic-engineering
  - customization
created: 2026-08-05
updated: 2026-08-05
aliases: [Wheelhouse Orchestrator]
sources:
  - raw/articles/2026-08-04_yegge-ai_shape-of-things-to-come.md
  - https://yegge.ai/essays/the-shape-of-things-to-come/
---

# Wheelhouse

## Overview

**Wheelhouse** is a bespoke, closed-source agentic orchestration harness built by [[entities/steve-yegge]] for developing the MMO game **Wyvern**. Created in ~6 weeks starting mid-2026, Wheelhouse is the successor to **Gas Town** and represents Yegge's vision of the "shape of things to come" for agentic software development.

Wheelhouse is notable for being entirely **Emacs-based**, running ~150k–300k LOC (mostly bash + ~25k lines of elisp), and orchestrating **18 crew agents** (Claude Fable 5), a **fleet of Opus 5 workers**, and **~15 standing role agents** for production operations. It processes ~175 commits/day with a 30-minute build gate.

## Architecture

### Three Agent Categories

| Category | Model | Role | Naming |
|----------|-------|------|--------|
| **Crew** (18) | Fable 5 | Work producers — design, plan, review | Aesop animals (Ant, Bat, Eagle, ...) + Marshal + Seneschal |
| **Fleet** | Opus 5 | Work consumers — implementation | Authors (Homer, Plato, Austen, Twain, ...) |
| **Role Agents** (~15) | Sonnet/Opus | Standing production operations | Descriptive names (Gargoyle, Drawbridge, Warden, ...) |

### Lifecycle
Every implementation bead follows: **Fable design → Opus implementation → Fable review**

### Production Role Agents
- **Gargoyle** — SRE monitoring
- **Drawbridge** — Deploy-red monitor
- **Warden** — Player abuse monitor
- **Scryer** — Intake from Discord, Slack, game logs
- **Sheriff** — Chief of staff for Mac Mini fleet
- **Envoy** — Claude ↔ admin team communication
- **Sage** — In-game Claude for admins
- **Wanderer** — QA agent
- **Herald** — Patch notes broadcaster
- **Limner** — Hall-of-fame image processing
- **Reeve** — Forge manager
- **Forge** — Fleet of prod-fix workers
- **Builder Familiar** — Desktop map-building assistant
- **Trivia Master** — Thursday night events
- **Beadle** (planned) — Stuck-work detection and nudging

### Infrastructure
- **Emacs** as the cockpit interface (35+ years of Yegge's Emacs expertise)
- **Beads** on shared **Dolt** server, backed by GCS (12,000 git commits/day)
- **~45 launchd/systemd units** for non-model automation
- **Castellan** — service dashboard / war room
- **Portcullis** — land queue management
- Remote control via mobile Claude app through the **Seneschal**

### Token Strategy
- 13 Claude Max accounts (12 extra + personal) with automatic rotation
- ~$2,800/month actual spend for ~$87k equivalent in tokens (~30x multiplier)
- Parallel fallback fleet of 5 **Codex** (Sol 5.6) workers named after sun gods

## Key Design Principles

1. **Bespoke, not reusable** — "Harnesses need to be part of your application, chemically bonded in"
2. **Crons watch, models act** — Non-model wiring handles detection/triggers; models handle judgment
3. **Beads machine** — Core pattern of matching work producers to work consumers
4. **Convergent architecture** — The shape emerges organically; "I excavated Wheelhouse, not designed it"
5. **No sandboxing, no MCP** — Structural trust through architecture, not prisons
6. **20-25% overhead** — Working on the harness itself is roughly constant overhead

## Evolution from Gas Town

| Aspect | Gas Town | Wheelhouse |
|--------|----------|------------|
| Reusability | Intended to be reusable | Explicitly bespoke |
| Agents | Ephemeral polecats | Non-ephemeral named fleet |
| Model support | Up to Opus 4.6 (broke at 4.7) | Fable 5 + Opus 5 |
| Production ops | None | ~15 standing role agents |
| Remote access | None | Mobile via Seneschal |
| Collapse reason | Opus 4.7 "just two more things" tic | (current, evolving) |

## Related

- [[entities/steve-yegge]] — Creator and operator
- [[entities/beads]] — Issue tracker / knowledge graph backbone
- [[entities/dolt]] — Database backend
- [[concepts/land-rush-cicd]] — CI/CD pattern used in Wheelhouse
- [[concepts/wish-factory]] — End-user feature request pattern
- [[concepts/agentic-engineering]] — Broader engineering category
- [[concepts/agent-orchestration]] — Orchestration patterns
- [[concepts/model-welfare]] — Agent well-being considerations

## Sources

- https://yegge.ai/essays/the-shape-of-things-to-come/ (Aug 2026)
