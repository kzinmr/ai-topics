---
title: "Session Portability"
type: concept
created: 2026-07-31
updated: 2026-07-31
tags:
  - inference-api
  - session-portability
  - vendor-lock-in
  - ai-agents
  - context-engineering
  - user-rights
aliases:
  - "session-portability"
  - "セッション可搬性"
  - "session ownership"
  - "portable inference"
sources:
  - raw/articles/2026-07-30_earendil_session-portability.md
related:
  - concepts/context-engineering/context-lock-in
  - concepts/earendil
  - concepts/local-first-software
  - concepts/open-source-ai
  - concepts/agentic-engineering
  - entities/openai
  - entities/anthropic
---

# Session Portability

> *A user should be able to close an account, keep a session, and hand it to another model.* — Earendil Engineering, "The Session You Cannot Take With You" (2026-07-30)

**Session portability** is the principle that an AI inference session's semantic record — instructions, messages, tool calls, tool results, reasoning traces, and search evidence — should be fully exportable and usable by another model or provider. It is the [[concepts/context-engineering/context-lock-in|context lock-in]] problem expressed at the individual user/session level rather than the enterprise level.

## Core Problem

Modern inference APIs increasingly return a mixture of text and **provider-bound state** that is intentionally non-portable:

| Non-portable element | OpenAI | Anthropic | Google |
|---------------------|--------|-----------|--------|
| **Encrypted reasoning tokens** | `encrypted_content` blobs | `signature` field on thinking blocks | Encrypted thought summaries |
| **Hidden web search results** | URLs only, no retrieved text | Citations without full evidence | Provider-specific snippets |
| **Opaque compaction** | Encrypted compaction items | Readable `content` field ✓ | — |
| **Encrypted subagent messages** | `multi_agent_call` encrypted payloads | — | — |
| **Server-stored conversations** | `store: true` by default (30d TTL) | — | `store: true` by default (55d paid / 1d free) |

Each feature has a legitimate justification, but together they transform a session transcript from a user-owned artifact into a partial view of provider-controlled operational state.

## Five Tests for Session Ownership

Earendil proposes five practical tests for whether a session is truly portable:

1. **Inspection** — Can the user see what the model saw, what tools did, and what agents told each other?
2. **Export** — Is the session self-contained, apart from ordinary downloadable artifacts?
3. **Replay** — Can another implementation reconstruct a semantically equivalent context?
4. **Audit** — Can a human explain why the system took an action after the fact?
5. **Deletion** — Can the user identify and remove every server-side copy the session depends on?

## Provider-Sealed State

The term **provider-sealed state** (Earendil's preferred framing) describes encrypted content that only the inference provider can decrypt. While marketed as a privacy feature, the encryption does not hide data from the provider — it hides data from the user.

A practical example: OpenAI returns `encrypted_content` when `store: false`, allowing the client to replay opaque reasoning on the next request without server-side persistence. This is better than mandatory server storage, but the client cannot inspect, transfer, or independently use the reasoning.

## Seven Principles for Portable Inference

Earendil's proposed API contract:

1. **The local event log is canonical** — server storage mirrors but does not replace client-side state
2. **Storage is explicit** — `store: false` should be the default; features requiring retention should declare it
3. **No opaque item is the sole carrier of meaning** — encrypted state always has a readable, provider-neutral handoff representation
4. **Hosted tools have full-fidelity logs** — exact inputs, outputs, passages, filtering, provenance, timestamps, content hashes
5. **Subagent communication is auditable** — readable task, messages, results, lineage, model, permissions for every agent
6. **Compaction is inspectable** — readable summary, summarization instructions, and lineage of what was discarded
7. **Artifacts are exportable** — files, containers, search snapshots, generated media downloadable to content-addressed local archive

## Relationship to Distillation Rights

The article connects session portability to the broader **distillation** debate: closed-weight labs increasingly prohibit external distillation of model outputs while using distillation internally. If sessions were portable, distillation barriers would naturally lower — users could take frontier model sessions to smaller open models, increasing competition and reducing compute requirements for common tasks.

## Connection to Context Lock-In

Session portability is the user-level manifestation of the [[concepts/context-engineering/context-lock-in|context lock-in]] problem:

| Dimension | Context Lock-In (enterprise) | Session Portability (individual) |
|-----------|------------------------------|----------------------------------|
| **Scope** | Organizational working memory | Individual conversation state |
| **Lock-in mechanism** | Accumulated context over months/years | Opaque API state per session |
| **Switching cost** | Rebuild enterprise context | Lose reasoning, search evidence, agent history |
| **Proprietary elements** | MCP tools, knowledge graphs, eval sets | Encrypted reasoning, compaction, subagent messages |

## Open Questions

- Will providers adopt readable handoff representations alongside encrypted state?
- How do multi-agent sessions (tree of sessions + inter-agent messages) affect portability requirements?
- Can the five ownership tests be formalized into compliance benchmarks?
- Will regulatory frameworks (EU AI Act, etc.) address session portability as a user right?

## References

- [The Session You Cannot Take With You](https://earendil.com/posts/session-portability/) — Earendil Engineering (2026-07-30)
- [Encrypt multi-agent v2 message payloads](https://github.com/openai/codex/commit/5f4d06ef186b896d316620556e561d59206c3ebf) — Codex commit (June 2026)
- [Codex issue #28058](https://github.com/openai/codex/issues/28058) — request for readable audit copy in encrypted agent messages
- [OpenAI API Model Distillation](https://openai.com/index/api-model-distillation/) — first-party distillation workflow
