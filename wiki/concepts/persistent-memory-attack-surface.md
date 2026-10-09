---
title: "Persistent Memory Attack Surface in LLM Agents"
created: 2026-10-09
updated: 2026-10-09
type: concept
tags: [agent-security, prompt-injection, agent-memory, agent-safety, memory-systems, computer-use]
sources:
  - raw/papers/2026-08-28_2608.22797_memory-burns-threats-controls-persistent.md
related: [memory-integrity, cross-agent-memory-sharing, prompt-injection, agent-security-patterns, ai-control, ai-memory-systems]
confidence: medium
aliases: ["persistent memory attack surface", "When Memory Burns", "memory control surface", "MCS", "memory poisoning"]
---

# Persistent Memory Attack Surface in LLM Agents

Persistent memory turns agent experience into a durable asset — and a durable **attack
surface**. Unlike a one-off prompt injection that affects a single turn, a memory
vulnerability **persists across sessions and resurfaces whenever it is retrieved**, quietly
steering future behavior long after the injection. This is arguably the most under-defended
component of deployed agents in 2026.

## The Injection → Storage → Retrieval Framework

"When Memory Burns" (Su et al., 2026; arXiv:2608.22797) models the threat in three stages:

1. **Injection** — attacker content (a web page, email, tool output, another agent's shared
   memory) is coaxed into being written to long-term memory.
2. **Storage** — the content persists, becoming indistinguishable from legitimate experience.
3. **Retrieval** — on a later, unrelated task, the poisoned memory is retrieved and injected
   into context, influencing the agent's actions.

The crux: the malicious payload is *not in the current input*. By the time it acts, the
original untrusted source is gone, so conventional input-filtering guardrails never see it.

## Empirical Findings

Across **three agent frameworks, four attack strategies, three adversarial datasets, and nine
attack targets**, the vulnerability is **widespread and framework-agnostic**. No surveyed
framework is immune by default; the flaw lives in the *memory architecture*, not a particular
vendor's implementation.

## The Memory Control Surface (MCS)

The paper proposes six controls, evaluated in isolation and combination:

| # | Control | Defends at |
|---|---------|-----------|
| 1 | **Memory provenance** — record where each memory came from | injection / storage |
| 2 | **Retrieval-time validation** — re-check memories when recalled | retrieval |
| 3 | **Context isolation** — separate memory scopes by task/trust | storage |
| 4 | **Memory lifecycle management** — TTL, review, expiry | storage |
| 5 | **Memory access control** — who/what may read/write a memory | storage / retrieval |
| 6 | **Behavioral guardrails** — constrain what retrieved memory may cause | retrieval |

Key result: no single control suffices; defense-in-depth across the surface is required.
Provenance + retrieval-time validation are the highest-leverage pair, because they attack the
"poison looks legitimate" assumption directly.

## Relationship to the Rest of the Memory Story

This is the security twin of [[cross-agent-memory-sharing]] — sharing multiplies exactly this
risk across a fleet. It extends [[prompt-injection]] from *in-context* to *in-memory* attacks,
and gives concrete machinery (provenance, lifecycle, access control) to the abstract
concerns raised in [[memory-integrity]]. The MCS controls map cleanly onto
[[agent-security-patterns]] primitives (least-privilege, capability isolation).

## Open Questions

- Provenance is proposed but not fully specified — how do you verify a memory's *claimed*
  source cryptographically vs merely labeling it?
- Do guardrails (control 6) re-create the [[epistemic-transparency]] problem by needing to
  "explain" why a retrieved memory was rejected?
- What is the usability cost of lifecycle management (control 4) for agents that rely on
  long-lived genuine lessons?

## Related

- [[memory-integrity]] — the general integrity concern this operationalizes
- [[cross-agent-memory-sharing]] — sharing amplifies this surface
- [[prompt-injection]] — the in-context ancestor of this in-memory attack
- [[agent-security-patterns]] — reusable control primitives
- [[ai-control]] — broader attack/defense literature
