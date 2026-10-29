---
title: "Sierra Compliance Console (regulated outreach controls for long-horizon agents)"
type: concept
created: 2026-10-29
updated: 2026-10-29
tags:
  - ai-agents
  - long-horizon
  - enterprise-agents
  - agent-governance
  - proactive
  - agent-platform
  - product
  - platform
  - policy
  - partnership
sources:
  - raw/articles/2026-10-28_sierra-compliance-console.md
related:
  - concepts/long-horizon-agents
  - entities/sierra
  - concepts/microsoft-agent-governance-toolkit
  - concepts/a2a-agent-protocol
  - entities/bret-taylor
---

# Sierra Compliance Console

**Compliance Console** (Sierra, announced 2026-10-28) is the first widely-visible product that treats **outbound-contact law as an agent-runtime control plane** rather than as a policy document. It ships inside Sierra's [[concepts/long-horizon-agents|long-horizon]] Horizon platform and enforces per-jurisdiction communication rules on the agent's *actions* — disclosures, contact windows, holidays, frequency caps, opt-outs — with a dashboard that reports how many outbound messages/calls were **allowed, deferred, blocked, or held for review**.

^[[raw/articles/2026-10-28_sierra-compliance-console.md]]

## The trigger: agent horizon crossed the regulatory horizon

Sierra's own framing is the most interesting part of the post: *"In the last six months agents have reached a tipping point. They've moved from mostly reactive, one-and-done support conversations to interactions that can last weeks or months and drive growth."* The named use cases — originating a loan, collecting a late payment, chasing a quote, renewing an insurance policy — all involve **proactive** outreach across phone, SMS, and email to the same person over days or months.

Each of those touches is individually regulated, and the rules are **locale-specific**: who may be contacted, when, how often, and what they must be told. This is the classic telemarketing/communications-law domain (TCPA-style consent, calling-hour, disclosure and frequency rules in the US; PECR/ePrivacy and national opt-out regimes in the EU, with country-specific blackout days). Historically these were enforced by a dialer/campaign tool with a compliance officer configuring it. Once an agent autonomously decides *when* and *how often* to reach out, the compliance logic has to move inside the agent loop.

## Controls exposed

| Control | What the agent is constrained to | Configurable axis |
|---------|----------------------------------|-------------------|
| **Disclosures** | Identify itself; announce call recording | Per channel: call opener, SMS opt-out explanation, email unsubscribe link |
| **Contact windows** | Only reach out during allowed hours | Based on **recipient's** local time; default cited as 8AM–9PM in most locales; custom days, or split windows |
| **Holiday exclusions** | Hold outreach on legally restricted days | Per country/region — examples given: Spain's National Day, France's Bastille Day, Australia's ANZAC Day |
| **Frequency limits** | Cap contacts per person | Company-configurable; separate limits for **marketing vs transactional** outreach |
| **Opt-outs** | Honor every opt-out request | Channel-agnostic — STOP by SMS *or stated verbally on a call*; saved and fully accessible to the company |
| **Dashboards** | Audit trail | In Insights: allowed / deferred / blocked / held-for-review counts, plus opt-outs |

Two design details carry most of the engineering weight:

1. **Recipient-local time, not agent time or company time.** For an agent running in a datacenter contacting customers across timezones, the clock that matters is the one at the callee's address. This is the same "the constraint belongs to the principal, not the executor" problem that shows up in agent identity/authorization work ([[concepts/a2a-agent-protocol]]).
2. **Voice opt-out parity with SMS opt-out.** Recognizing and persisting an opt-out stated in natural language during a phone call — rather than only handling the deterministic `STOP` keyword — means the compliance state machine depends on ASR/NLU output. That is a reliability-critical path with a legal penalty attached, which is exactly where agent teams most need hard verification.

## Where this fits in the agent-stack trend

Compliance Console is best read as a data point in the **hardening of the agent action boundary**, alongside sandboxing and trace-integrity work:

- [[concepts/sandbox]] / [[comparisons/agent-sandboxing]] — constrain *what code* an agent may run; Compliance Console constrains *whom an agent may contact, and when*. Same architectural role (a policy enforcement point on the action), different regulated domain.
- [[concepts/agent-trace-integrity]] — "allowed / deferred / blocked / held for review" is precisely the kind of decision log whose provenance matters if a regulator or plaintiff later asks why a contact happened.
- [[concepts/agent-skills]] / [[concepts/skill-constellations-github-supply-chain]] — the mirror-image risk: an injected instruction that causes an agent to *skip* the disclosure step or re-contact an opted-out customer is a compliance violation with legal exposure, not just a wrong answer.
- [[entities/sierra]]'s tau-bench lineage ([[concepts/ai-benchmarks/tau-bench]], [[concepts/ai-benchmarks/tau-knowledge]]) — Sierra has consistently built evals for exactly the domains it products, so a Compliance-Console-shaped benchmark (does the agent refuse an out-of-window contact?) is a plausible follow-on.

## Assessment / open questions

- Vendor announcement post; **no numbers** are given (no coverage of which jurisdictions are pre-configured, no statement on whether rules are maintained as curated content or customer-authored, no evidence on enforcement latency or false-permit rate). `confidence: medium` on the claims themselves.
- The hard part is not the enforcement primitive, it's **rule currency**: telecom and marketing-contact law changes constantly and is enforced per-state and per-country. Who authors and updates the rule set, and what happens on lag, determines whether this is a control plane or a liability-reduction story.
- No mention of whether the controls are bypassable by an agent that composes outreach across channels (e.g. email to circumvent an SMS frequency cap) — cross-channel budget sharing is the obvious first gap to probe.

## Related

- [[concepts/long-horizon-agents]] — Sierra's own Horizon positioning (July 2026) that this product extends
- [[entities/sierra]], [[entities/bret-taylor]]
- [[concepts/microsoft-agent-governance-toolkit]] — oversight/permission layer for autonomous actors
