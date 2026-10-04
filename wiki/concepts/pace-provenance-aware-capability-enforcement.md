---
title: "PACE — Provenance-Aware Capability Enforcement for Tool-Using Agents"
created: 2026-10-04
updated: 2026-10-04
type: concept
tags:
  - agent-security
  - tool-use
  - prompt-injection
  - supply-chain
  - formal-verification
  - agent-governance
aliases:
  - PACE
  - provenance-aware capability enforcement
sources:
  - raw/articles/arxiv-2610.01349-pace-provenance-aware-capability-enforcement-tool-agents.md
confidence: medium
related:
  - concepts/overact-proactive-over-authorization
  - concepts/capability-based-security
  - concepts/security-and-governance/agent-skill-supply-chain-attacks
  - concepts/agent-trace-integrity
---

# PACE — Provenance-Aware Capability Enforcement for Tool-Using Agents

**PACE** (Li et al., arXiv:2610.01349, Oct 1 2026) is an agent-security architecture whose core argument is that *admission-time* vetting is fundamentally insufficient. A safe artifact and a poisoned artifact can produce **identical admission evidence**, so no sound gate can distinguish them at load time. That leaves exactly one boundary a deployment can still act on: **the tool call itself, immediately before it executes.**

## The move: from gate-at-admission to gate-at-execution

Poisoned tool metadata, retrieved pages, memory entries, and reusable skills can all steer the next call (the cross-skill vector formalized in [[concepts/apex-adversarial-skill-chain-hijacking]]). PACE mediates **every tool call at execution time** via two mechanisms:

- **Path confinement** — proposes an executable *cut* of "represented influence paths," i.e. the information flows that could have reached this call. The final action must *preserve* the certified cut.
- **Capability & effect verification** — checks the call's schema-defined effects against **authority compiled from the authenticated request**. The effect is only allowed if the original request authorized it.

## Certified contract vs. evaluated configuration

PACE deliberately separates two notions that other defenses collapse:
- the **certified execution contract** (the provably-safe cut the confinement check enforces), and
- the **evaluated configuration** (the policy that can *restore* an authorized call after a proposed block, or apply a declared repair).

This gives a recoverable, auditable decision instead of a hard binary block — relevant to the "defense-induced capability collapse" problem, where over-strict defenses destroy benign reliability.

## Results

On **eight executable agent-security benchmarks × three target-model families**:
- **strictly lowest attack success in 62 of 79** eligible attack columns, ties in 14;
- full-benchmark native utility loses **at most 3 points** vs. the undefended agent;
- an ablation over **1167 paired cases** attributes most security gain to *effect verification*, and refusal control to *boundary adaptation*;
- a reduced-scale adaptive search succeeds on **0/30** out-of-authority targets against the defense.

The "≤3-point utility loss" is the headline because it is the number PACE shares with [[concepts/apex-adversarial-skill-chain-hijacking]]'s cautionary result — where the naive defense cost ~30 points of benign capability. PACE's contract/configuration separation is what buys back that capability.

## Relationship to OverAct

PACE and [[concepts/overact-proactive-over-authorization]] converge on the same insight from opposite directions: the tool-call boundary is the load-bearing one. OverAct measures the agent *self-initiating* over-scope access and mitigates it model-side (SelfAudit self-justification). PACE enforces authority system-side, independent of whether the over-reach was adversarial or self-initiated. Together they bracket the confidentiality risk in [[concepts/advanced-tool-use]].

## Open questions
- Compiling authority from "the authenticated request" requires a formal request-intent schema — how expressive before it becomes a new attack surface?
- Effect verification is bounded by the tool schema; tools with coarse effects ("run arbitrary code") may admit little static verification.
- Does path confinement's cost track context size, interacting with [[concepts/attention-bottleneck]]?

## Related
- [[concepts/capability-based-security]] — the least-privilege lineage PACE instantiates
- [[concepts/security-and-governance/agent-skill-supply-chain-attacks]] / [[concepts/apex-adversarial-skill-chain-hijacking]] — the admission-time gap PACE argues can't be closed
- [[concepts/agent-trace-integrity]] — post-hoc auditing; PACE is pre-execution prevention
- [[concepts/prompt-injection]] — the general class of influence PACE confines
