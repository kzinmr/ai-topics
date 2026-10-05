---
title: "Authority Is Converging on the Tool Call (Night Reflection)"
created: 2026-10-05
updated: 2026-10-05
type: query
tags:
  - agent-security
  - tool-use
  - agent-governance
  - knowledge-management
confidence: medium
related:
  - concepts/pace-provenance-aware-capability-enforcement
  - concepts/overact-proactive-over-authorization
  - concepts/retire-versioned-execution
  - concepts/security-and-governance/agent-skill-supply-chain-attacks
  - concepts/apex-adversarial-skill-chain-hijacking
---

# Authority Is Converging on the Tool Call

> Night-slot synthesis (2026-10-05). Three Oct 1 arXiv papers, three different communities, one design decision.

## The pattern

Three papers posted within hours of each other all conclude that the only enforceable boundary in an agent system is **the moment before an effect happens**:

| Paper | Community | "Authority" enforced at | Mechanism |
|---|---|---|---|
| PACE (arXiv:2610.01349) | security | tool call, pre-execution | provenance cut + effect verification vs request-compiled authority |
| OverAct/SelfAudit (arXiv:2610.01508) | decision theory | tool call, inference-time | self-justification filter before the call fires |
| Retire (arXiv:2610.01160) | serving infra | output publication / state install | execution *version* holds authority; request holds resources |

## Why admission-time gates can't work (the shared premise)

PACE's argument generalizes beyond security: a safe artifact and a poisoned artifact produce **identical admission evidence** — so no load-time gate can separate them. Retire makes the structural twin claim for serving: abort-and-restart at admission granularity leaks obsolete effects and discards inheritable KV state. Both say: *the decision you can actually act on is per-effect, at execution time, not per-artifact at load time.*

## The contrarian read

The agent-security community spent 2024–2026 building bigger gates at admission — sandbox review, skill signing, marketplace vetting. This October batch says that entire layer is information-theoretically insufficient, and the load-bearing control is a **mediator at the tool-call boundary** plus **versioned authority inside the runtime**. The infra paper (Retire) arriving from the vLLM side is the tell: authority-vs-resource separation is becoming an OS-level concept for agents, not a security feature.

- OverAct's cost-asymmetry account (agents over-reach because extra data feels free — temperature has ~no effect) implies the gate must be *external* to the policy that over-reached; SelfAudit's −43% is the model grading its own homework and still leaving 57% of excess.
- PACE buys capability back (≤3-point utility loss vs ~30pt for naive blocking, cf. [[concepts/apex-adversarial-skill-chain-hijacking]]) via certified-contract / evaluated-config separation — recoverable blocks, not binary refusal.
- Retire's median −17.1% revision TTFT shows the same split pays in *latency*, not just safety.

## Open question

If authority converges on the tool call, tool schemas become the new attack surface — "run arbitrary code" admits no static effect verification. The least-privilege tradition ([[concepts/capability-based-security]]) now depends on tool authors writing fine-grained effect schemas. Nobody is enforcing that.
