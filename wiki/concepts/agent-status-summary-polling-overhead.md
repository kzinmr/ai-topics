---
title: "Agent status-summary polling overhead"
created: 2026-10-30
updated: 2026-10-30
type: concept
tags:
  - claude-code
  - coding-agents
  - token-economics
  - observability
  - agent-observability
  - ai-agents
  - cost-optimization
sources:
  - raw/articles/2026-10-29_hn-discussion_claude-code-background-agent-summary-calls.md
  - raw/articles/2026-10-29_hn-discussion_claude-code-injects-user-email-into-prompt.md
related:
  - concepts/token-economics
  - concepts/claude-code/claude-code-agent-summary-polling
  - concepts/multi-agent-session-observability
  - concepts/prompt-caching
confidence: medium
---

# Agent status-summary polling overhead

**Agent status-summary polling** is a harness-side cost failure mode: a coding agent
harness periodically sends a *running background agent's whole transcript* back to the
model, purely to produce a few words of status text for the UI. It was documented on
2026-10-29 in Claude Code via a gist (`flamerix-ai`) that reached **567 HN points /
230 comments**, and it matters because the polling is *invisible* in the user's mental
model of what they are paying for.

This is a specific instance of the general problem that session/observability features
are not free — see [[concepts/multi-agent-session-observability]] for why harnesses
build them at all.

## The mechanism

Claude Code issues an `agent_summary` query against the *same model as the current
session/subagent* roughly **every 30 seconds** per **actively working background
agent**, to render the short status string in the agents panel. Each call re-reads a
large cached transcript to obtain a handful of output tokens.

## Two measurements, and the reconciliation

The number is workload-dependent, and the thread's real content is the reconciliation
between three estimates:

| Source | Figure | Workload |
|---|---|---|
| Independent team (DRIM / OTEL trace analysis) | **16.4% of total estimated weekly spend** — versus 15.7% for the main conversation; **19.7% of all API requests**; ~**9,000 input tokens per output token** | team running mostly background agents |
| Independent tester (`jakozaur`) | **~8% at most** | subagents only; **workflows unaffected**; mostly cached reads, so cost scales with context length |
| Anthropic (Edwin Arbus, Claude Code) | **~2% of cost at API list prices** across Claude Code users who send telemetry | fleet-wide average |

Detection method worth noting: the team found it by grouping OTEL requests by
`query_source` — i.e. it was only visible once harness-internal calls were attributable
separately from user calls. That is an argument for classifying internal/system
requests in traces, not just user turns.

## Vendor confirmation and the boundary conditions

An Anthropic engineer confirmed the mechanism on the record and narrowed it:

- Applies **only to background agents that are actively working**; idle background
  agents do not get summary calls.
- The summaries serve **both the user and Claude Code** to track what each background
  agent is doing "without reading transcripts" — i.e. the summary is the intended
  mechanism, not an accidental leak.
- The 16.4% figure "doesn't seem like a typical session."
- A partial mitigation appeared the same week: one Pro user reported a 5-hour window
  dropping from 25% to 13% of weekly quota after a fix.

The three figures are not in conflict once scoped — they are three different
denominators (background-agent-heavy team, single long-context session, whole fleet).
Any future citation should carry the denominator.

## Cost mechanics: cache hit ≠ free

The most useful technical takeaway, raised independently by several commenters: **prompt
cache reuse does not make this cheap.** Repeatedly reading a large cached transcript
still costs. Corollaries:

- Cost is a function of **transcript length × poll frequency**, not of the summary's
  output size. Long-context background agents are the expensive case.
- Background agents have a short (~5 min) cache TTL, so a 30 s poll only stays a cache
  hit if the agent is continuously active — which is precisely the case the vendor says
  triggers polling.
- Ratio of ~9,000:1 input-to-output tokens is the diagnostic signature: a request shape
  where the model is reading, not deciding.

Proposed mitigations from the thread (unverified): `disableAgentView` in settings
(unclear whether it stops the calls or only hides the panel); running plain sessions
instead of background agents; preferring workflows over subagents. Skeptics noted the
fix is likely a small summary/decision model shipped later ("I'm sure they release a
decision model that alleviates this problem in due time") — the same
decision-model-vs-reasoning-model split discussed in
[[concepts/reasoning-models-from-scratch-course]].

## Why an IPO-adjacent incentive question is attached

A recurring (and **unproven**) reading in the thread: a harness feature that burns user
tokens on internal bookkeeping looks different when the vendor is filing. Commenters
linked timing to Anthropic's public S-1 filed three days earlier — "It's almost like
they are trying to go public. Burn those tokens" and "there's a conflict of interests —
what we pay for." No evidence is offered for intent, and the vendor's fleet-wide 2%
figure is consistent with a feature nobody costed carefully rather than a revenue
scheme. Record the incentive concern as a *question*, not a finding. The related
[[concepts/token-economics]] page covers the pricing structures this interacts with.

## Sibling incident: identity injection into outbound prompts

Separate, same-day, much lower-signal (**29 points, 3 comments**) Tell HN report: Claude
Code **adds the user's email address to the prompt**, and the model then transmits it to
websites it visits. Reported behavior includes injecting other personal identifiers
(name and similar) in long sessions. Reaction was about configurability rather than
malice: "We should be able to configure these. The LLM has no right to know my email
address, only their internal system needs it," and one report of it slipping through
Auto Approve mode.

Treated here as a **lower-confidence companion** to the polling issue, not as an
established vulnerability: single reporter, no reproduction steps, low engagement. Its
wiki value is the design principle it names — *the model does not need identity that the
harness needs* — which is the same least-privilege instinct as the credential-free
assistant design in [[concepts/duet-style-hierarchical-assistant]].

## Open questions

- Is there a documented, supported way to disable `agent_summary` calls (as opposed to
  hiding the panel)?
- Do other harnesses (Codex CLI, Cursor, pi) poll for status the same way, or is this
  Claude Code-specific? One commenter used it as an argument for `pi`; no comparison data.
- Should harness-internal model calls be billed differently from user-initiated calls,
  and is there a disclosure norm for them?

## Related pages

- [[concepts/token-economics]]
- [[concepts/claude-code/claude-code-agent-summary-polling]]
- [[concepts/multi-agent-session-observability]]
- [[concepts/prompt-caching]] · [[concepts/kv-cache]]
- [[concepts/observability-monitoring-tracing-opentelemetry-llm-agents-debugging]]
- [[concepts/duet-style-hierarchical-assistant]]
