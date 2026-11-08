---
title: "Earendil"
type: concept
aliases:
  - earendil
  - earendil-inc
created: 2026-04-25
updated: 2026-11-08
tags:
  - company
  - ai-infrastructure
  - coding-agent
  - durable-execution
  - inference-api
  - session-portability
  - open-source
sources:
  - https://earendil.com/
  - raw/articles/2026-07-30_earendil_session-portability.md
  - https://lucumr.pocoo.org/2026/1/27/earendil/
  - https://earendil.com/posts/announcement-reflection/
related:
  - entities/armin-ronacher
  - entities/pi
  - concepts/absurd-durable-execution
  - concepts/session-portability
---

# Earendil

**Earendil Inc.** is a technology company co-founded by [[entities/armin-ronacher|Armin Ronacher]] (creator of Flask/Sentry) and Colin. The company develops AI agent infrastructure and developer tooling, with a strong stance on user ownership and open systems.

## Products & Projects

- **[[entities/pi|Pi]]** — Open-source coding agent (`earendil-works/pi`), originally by Mario Zechner, now under Earendil
- **[[concepts/absurd-durable-execution|Absurd]]** — Postgres-native durable execution framework for AI agent loops (`earendil-works/absurd`)
- **Lefos** — Company product (lefos.com)
- **Works** — Open-source projects (github.com/earendil-works/)
- **Pi Durable** (Oct 1, 2026) — experimental package shipped with Pi 1.0; durable/malleable harness for long-running agentic applications. See [[events/pi-durable-1-0]] for the harness model (storage + machinery, conversations/tasks, pluggable storage & execution environments) and cross-device/multi-human capabilities.

## Values & Positions

Earendil has published notable essays articulating a user-rights perspective in the AI ecosystem:

### Session Portability (July 2026)

["The Session You Cannot Take With You"](https://earendil.com/posts/session-portability/) argues that inference APIs are creating a new form of lock-in through non-portable session state: encrypted reasoning tokens, hidden search results, opaque compaction, and encrypted subagent messages. The post proposes five tests for session ownership and seven principles for portable inference APIs.

Key positions:
- The local event log should be canonical, not server-stored IDs
- Encrypted state should always have a readable, provider-neutral handoff representation
- Hosted tools should provide full-fidelity logs, not just citations
- Distillation should be supported, not treated as an attack

### On Reasoning Opacity

The article highlights a growing asymmetry: all major labs hide raw chain-of-thought behind encryption, making reasoning traces non-portable across providers. Anthropic's thinking blocks are explicitly tied to specific models and should be stripped when switching models — even within Anthropic's own ecosystem.

### On Distillation

Earendil challenges the moral asymmetry of closed labs prohibiting external distillation while using it internally: "The broadest version of that principle conveniently allows learning to flow into closed models but not back out of them."

## Claude Code defections (Nov 2026)

Caleb Porzio's "Goodbye Claude, Hello Pi" (HN 367pts, 2026-11-08 — https://news.ycombinator.com/item?id=50410107) is a high-profile migration from Claude Code to Pi as the daily coding harness. Cited grievances: no `AGENTS.md` support until Anthropic's day-after announcement (CLAUDE.md/AGENTS.md dual-format friction), single-session IDE text-selection binding in VSCode, half-broken GUI slash commands, subagent output interleaving, and release churn — 244 Claude Code releases YTD, over 3/4 changing the system prompt or tool descriptions (2,900-token default Bash tool description). Framing: "CC feels like a product without a strong vision"; enterprise feature pace (dynamic workflows, agent teams, ultrareviews) burns tokens without serving individual developers. Raw: `raw/articles/2026-11-08_caleb-software_goodbye-claude-hello-pi.md`.

## Related Pages

- [[entities/armin-ronacher]] — Co-founder
- [[entities/pi]] — Coding agent
- [[concepts/absurd-durable-execution]] — Durable execution framework
- [[concepts/session-portability]] — Session portability concept (from Earendil's essay)
- [[concepts/context-engineering/context-lock-in]] — Related: enterprise-level context lock-in
