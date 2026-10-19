---
title: "Self-Hosted LLM Proxy as the Agent Observability Boundary"
type: concept
created: 2026-10-19
updated: 2026-10-19
tags:
  - llm-proxy
  - agent-observability
  - observability
  - agent-security
  - ai-gateway
  - vendor-lock-in
  - developer-tooling
confidence: medium
sources:
  - url: https://jrdsgl.com/if-you-dont-run-your-own-llm-proxy-how-the-fuck-do-you-even-know-whats-going-on/
    title: "If you don't run your own LLM proxy, how do you know what's going on?"
    date: 2026-10-18
  - url: https://news.ycombinator.com/item?id=50145507
    title: "HN discussion — self-run LLM proxy"
    date: 2026-10-18
  - raw/articles/2026-10-19_trending-hybrid-reasoning-killswitch-llmproxy.md
related:
  - concepts/ai-gateway
  - concepts/ai-observability
  - concepts/multi-agent-session-observability
  - concepts/provider-sealed-reasoning-blur
  - concepts/agent-safety
  - concepts/agent-security
---

# Self-Hosted LLM Proxy as the Agent Observability Boundary

> HN 2026-10-18, **203 pts / 149 comments**. The argument: if every request goes straight from your
> agent harness to a provider API, the *only* party with a complete record of what the agent actually
> sent and received is the provider.

## The claim

Agent behaviour is determined by the exact request payloads — system prompts, tool schemas, retrieved
context, mid-loop revisions. Without an intercepting layer between harness and provider, an operator
has:

- no ground truth for what the model was actually asked (harness-side prompt assembly is opaque, and
  providers may modify the request in flight — see [[concepts/provider-sealed-reasoning-blur]]),
- no independent cost/token record,
- no audit artefact for post-incident review,
- no way to detect prompt-injection-driven tool calls after the fact.

Running your own proxy makes the request/response pair the observable unit.

## Practical pattern from the HN thread

Two distinct implementations surfaced in discussion:

1. **Roll-your-own harness + proxy** (`voodooEntity`) — the proxy is a by-product of owning the harness:
   *"actual full observability of what it is doing and why it is doing what it is doing."*
2. **LiteLLM Proxy on own servers** (`hoppp`) — the two operational wins named were:
   - it **issues virtual keys**, so real provider API keys never enter the sandbox where the agent runs
     (a containment measure, not just an observability one — cf. [[concepts/agent-sandbox-patterns]]);
   - it **sees every request/response**, giving a full local transcript.

## The unresolved gap: subscription auth

The most-repeated practical objection (`stavros`): *"Can I use it with my Claude subscription?"*
OAuth-based consumer plans (Claude Pro/Max, ChatGPT plans) are not designed to be fronted by a
third-party proxy, and ToS handling is murky. This matters because a growing share of agent usage runs
on subscription auth precisely to avoid per-token API pricing — meaning the population least able to
instrument its traffic is the one most dependent on the provider's own logging.

## Position in the existing map

| Concern | Existing page | Relation |
|---|---|---|
| Gateway as routing/cost/governance layer | [[concepts/ai-gateway]] | This page is the *audit-first* justification for the same box; AI Gateway frames it as spend control and multi-model routing. |
| Trace/metric/eval stack | [[concepts/ai-observability]], [[concepts/active-observability]] | Those assume traces are already emitted; the proxy is where the raw trace is captured before any analysis layer. |
| Multi-agent session visibility | [[concepts/multi-agent-session-observability]] | Complementary — session-level vs request-level. |
| Provider-side opacity | [[concepts/provider-sealed-reasoning-blur]] | The sealing problem this page responds to. |

## Caveat

A proxy observes what the harness sends, not what the provider's serving stack does with it (server-side
prompt modification, tool injection, sealed reasoning). It closes the harness-side blind spot; it does not
make the provider transparent.

## Sources

- Article: https://jrdsgl.com/if-you-dont-run-your-own-llm-proxy-how-the-fuck-do-you-even-know-whats-going-on/
- HN: https://news.ycombinator.com/item?id=50145507
