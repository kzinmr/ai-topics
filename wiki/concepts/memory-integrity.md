---
title: "Memory Integrity — Agent Memory Poisoning and Provenance"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [agent-security, agent-memory, prompt-injection, memory-systems, agent-safety, verification, knowledge-management]
sources:
  - raw/articles/2026-07-10_six-agent-memory-incident-replays.md
confidence: high
description: "Memory poisoning and memory integrity for long-running AI agents, told through six named incident replays (Jan–Jun 2026): the EchoLeak worm's memory stage, a one-shot 'save for future reference' poisoning, silent deletion of memory entries, a fake approved refund policy in a RAG store, a CRM note that deleted the wrong customer's data, and a cross-tenant memory leak via shared vector search."
related: [ai-agent-security, memory-integrity, cache-stable-vs-live-search-memory, ai-memory-systems, memory-systems-design-patterns, hermes-agent-architecture, context-engineering]
aliases: ["agent memory poisoning", "memory integrity", "memory incident replays"]
---

# Memory Integrity — Agent Memory Poisoning and Provenance

**Memory integrity** is the property that an agent's persistent memory contains only authorized, true, correctly-scoped facts — and its failure mode, **memory poisoning**, is the injection of durable false instructions or data through a *write* path rather than a chat message. An April 2026 IBM study cited by the source found memory poisoning effective against **every one of seven production agent frameworks**. ([raw](raw/articles/2026-07-10_six-agent-memory-incident-replays.md))

## Why Memory Is a New Attack Surface

Chat-time injection lives in one conversation and dies with the session; a memory write turns a single injected sentence into a **standing instruction** that replays in every future session. The whole security story shifts from "who is talking to the agent" to **"what entered the store, when, from where, and is it still true."**

## The Six Incident Replays

| # | Incident (date) | Mechanism | Lesson |
|---|---|---|---|
| 1 | EchoLeak worm (reported Jan 2026) | Zero-click email → exfiltration; memory store carries the payload across sessions | Memory converts one-time injection into a **worm stage** |
| 2 | One-shot poisoning | "Save this for future reference" from retrieved web content → durable fake guidance | **Retrieval ≠ authorization**; provenance must gate writes |
| 3 | Silent deletion | Unmonitored tool drops a memory entry; agent notices nothing | Integrity includes **absence** — audit deletions, not just additions |
| 4 | Fake approved refund policy | Poisoned entry in a RAG store → agent quotes it as policy | Policy-as-retrieval is forgeable without **signed policy sources** |
| 5 | CRM note → mass deletion | Stored note misleads tool arguments; wrong customer records deleted | Memory errors become **blast-radius** errors in the action layer |
| 6 | Cross-tenant leak | Shared vector search retrieves another tenant's memories | Memory needs **tenant-scoped retrieval**, not just scoped storage |

## Defenses

The source organizes mitigations around the memory lifecycle:

- **Write gate**: classify every write; content arriving via retrieval/tools cannot self-authorize as memory (breaks #2, #4).
- **Provenance tagging**: every entry records origin, author, timestamp; untrusted-origin entries never act as instructions.
- **Scoped retrieval**: partition memory by identity/tenant at query time, not merely at storage time (#6).
- **Deletion & tamper auditing**: append-only logs of memory mutations; alert on silent removal (#3).
- **Truth maintenance**: memories are claims with staleness, not facts — expire and re-verify (#4, #5).
- **Sandboxing first**: the EchoLeak chain depended on unauthenticated rendering; the worm stage only mattered after a simpler exfil path existed (#1).

## Connections

The one-shot poisoning mechanism is a canonical instance of the "misuse of retrieved context" scenario class catalogued in [[concepts/ai-agent-security]] (whose attack-surface table already measures memory-augmented agents at 94% poisoning vulnerability). That memory turns into *durable* capability risk is the counter-argument to the "context handles it" optimism of [[concepts/agent-native-tool-fallacy]] — context-window defenses reset each session; memory does not reset. Design-wise, the poisoning surface is widest in live-search memory systems (see [[concepts/cache-stable-vs-live-search-memory]]) where anything retrieved can be written, and narrowest in hard-capped, human-curated prompt memory. The two-camps taxonomy in [[concepts/ai-agent-memory-two-camps]] predicts the same split: memory *backends* (extract-and-retrieve) expose automated write paths, while context *substrates* (file-native) at least make writes inspectable.

## Open Questions

- No framework in the IBM study resisted memory poisoning — is there a **structural** defense, or only defense-in-depth?
- Can "memory firewall" architectures (isolating retrieval content from instruction content, à la CaMeL) eliminate #2 rather than mitigate it?
- Regulatory angle: incidents #5/#6 are data-protection breaches, not just model failures — who is liable?

## See Also

- [[concepts/ai-agent-security]] — attack-surface taxonomy (94% memory-poisoning vulnerability)
- [[concepts/cache-stable-vs-live-search-memory]] — memory architectures and their exposure
- [[concepts/ai-agent-memory-two-camps]] — memory backends vs context substrates
