---
title: "Pi 1.0 & Pi Durable release"
type: event
created: 2026-10-05
updated: 2026-10-05
date: 2026-10-01
tags:
  - announcement
  - durable-execution
  - coding-agent
  - open-source
  - agent-harness
sources:
  - raw/articles/earendil.com--pi-durable.md
  - https://earendil.com/posts/pi-durable/
  - https://x.com/badlogicgames/status/2107236034199126242
related:
  - entities/pi
  - concepts/earendil
  - concepts/absurd-durable-execution
  - concepts/durable-execution
---

# Pi 1.0 & Pi Durable release

On **2026-10-01**, Earendil and the Pi community shipped **Pi 1.0** — declaring the [[entities/pi|Pi]] coding agent a hardened foundation — together with a new experimental package, **Pi Durable**.

## What Pi Durable is

Pi Durable is **not** a replacement for the Pi coding agent. It is a **framework for building any agentic application** (coding agents included) aimed at *long-running, durable, malleable agents that can run anywhere*. It shares code (e.g. `pi-ai`) and principles — minimalism and malleability — with the Pi coding agent, and lets Earendil explore new harness designs without disrupting the coding agent; proven lessons flow back into Pi.

### Harness definition

Earendil defines a **harness** as *storage plus the machinery to run one or more LLM conversations in parallel*, providing the tools models call and the execution environments tools run in:

- **Conversation** — an interaction recorded as a transcript.
- **Agent** — the LLM plus its settings (thinking level) and callable tools.
- **Execution environment** — laptop, remote VM, or in-memory sandbox; chosen per conversation.
- **Task** — everything the harness runs (a model call or a tool execution) is a task.

The whole package (~15,000 lines excluding tests, ~150k tokens on GPT / ~250k on Claude worst-case) is built so the agent itself can read and understand it — storage backends alone are ~3,000 lines usually skippable.

## Key capabilities

- **Long runs anywhere** — targets "anywhere there is a JavaScript runtime." Ships memory, SQLite, and JSONL storage backends plus a conformance suite/benchmarks. SQLite/JSONL use no Node APIs, so with a small adapter they run on **Bun** or inside a **Cloudflare Durable Object**. Storage interface is small enough to implement over a KV store or Postgres. One process owns a storage at a time; other clients attach to it.
- **Bounded memory** — on SQLite the harness keeps only the working set (active transcripts, live tasks, pending submissions) in memory; compaction keeps active transcripts bounded by the context window, so even tens-of-thousands-of-message conversations fit.
- **Remote tools** — execution environments are pluggable, so the harness can run on one machine while its tools run on another; an `env` function builds the environment per tool call from the conversation's cwd.
- **Survives crashes** — the agent picks up where it left off after process death (laptop sleep, container redeploy, OOM).
- **Multi-surface, multi-human** — reached from different surfaces, supports multiple humans steering the same agents.

## Adoption signal

Creator [[entities/mario-zechner|Mario Zechner]] used Pi Durable in a phone-based app: *"everything except the LLM runs on my phone. pi durable is a library i use in this app which covers all the durable agent parts. the rest is the control plane and ui on top of it."* ([X, 2026-10-05](https://x.com/badlogicgames/status/2107236034199126242)) — demonstrating Pi Durable as a durable-agent **library** embedded under a thin control-plane/UI, with only inference off-device.

## Related

- [[concepts/earendil]] — the company shipping Pi/Pi Durable
- [[entities/pi]] — the coding agent Pi 1.0
- [[concepts/absurd-durable-execution]] — Earendil's Postgres-native durable execution framework
- [[concepts/durable-execution]] — the general concept

## Sources

- [Pi Durable | Earendil](https://earendil.com/posts/pi-durable/) (2026-10-01) — engineering announcement/tour. Raw: [[raw/articles/earendil.com--pi-durable]]
- [Mario Zechner on X](https://x.com/badlogicgames/status/2107236034199126242) (2026-10-05) — phone app using Pi Durable as the durable-agent library.
