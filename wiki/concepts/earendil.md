---
title: "Earendil"
type: concept
aliases:
  - earendil
  - earendil-inc
created: 2026-04-25
updated: 2026-07-31
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

## Related Pages

- [[entities/armin-ronacher]] — Co-founder
- [[entities/pi]] — Coding agent
- [[concepts/absurd-durable-execution]] — Durable execution framework
- [[concepts/session-portability]] — Session portability concept (from Earendil's essay)
- [[concepts/context-engineering/context-lock-in]] — Related: enterprise-level context lock-in
