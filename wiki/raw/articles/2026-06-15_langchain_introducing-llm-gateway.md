---
title: "How We Made Coding Agent Spend Predictable"
date: 2026-06-15
source: X Article
source_url: https://x.com/i/article/2066552183152373760
canonical_url: https://www.langchain.com/blog/introducing-llm-gateway
authors: ["LangChain Engineering"]
tags: [llm-observability, cost-management, coding-agents, langsmith]
status: FULL
---

# How We Made Coding Agent Spend Predictable

**LangSmith LLM Gateway** is currently in private beta.

For the last few years, AI usage was easy to ignore in a budget. At LangChain, model usage was largely confined to a few teams, usage was predictable, and monthly bills were manageable.

However, in the last year that stopped being true with a few things happening at once:
- AI usage went from a few teams to the whole company
- The best models got more expensive
- Agents got powerful enough to easily fire off dozens of model calls to finish a single task

As a result, AI spend became harder to understand and harder to control in real time.

The sharpest version of this showed up in engineering. One developer using coding agents heavily could generate thousands of dollars in weekly spend before anyone noticed. Our leadership needed a way to see spend as it was happening, set limits by team and user, and prevent accidental runaway usage without blocking productive work.

## Implementing an LLM Gateway

With cost tracking in mind, we built LangSmith LLM Gateway straight into the product we use every day. The immediate goal was simple: prevent accidental runaway spend by coding agents to bring peace of mind to both the VP of Engineering and Head of Finance.

In LangSmith LLM Gateway, budgets can be set across several dimensions:
- Organization-wide
- Workspace
- User
- API key

We have default budgets that every employee can hit on monthly, weekly, daily, and hourly windows, with the ability to set exceptions for people working on projects that need higher usage.

We applied the Gateway everywhere in the company where it was possible to do so centrally: coding agents through Claude Code, Codex, or LangChain Deep Agents. Every eligible coding agent call at the company runs through the LLM Gateway, giving our engineering leadership a bird's eye view of company-wide spend to the minute. And we made sure it was easy to implement, orchestrating it centrally through our MDM so each user wouldn't have to process the setup themselves.

> "The upside of Gateway is that there is more certainty with centralized control that I won't open my dashboard and see a surprise multi-thousand dollar bill. I have visibility into limits and spend with a central shutoff/control point." - Alex Lunev, VP of Engineering, LangChain

## Connecting Cost Controls to the Rest of the LangSmith Stack

Gateway is most useful when cost data is connected to the rest of the AI system.

Because LangSmith LLM Gateway is part of LangSmith, spend controls are connected to the systems we already use to manage AI applications. Gateway runs can be traced, attributed to users or keys, and analyzed alongside production data.

That means cost data is not limited to a monthly bill. We can connect spend to specific agents, model calls, traces, and failure modes. We can also use existing LangSmith controls for OAuth, model management, and user management, instead of rebuilding those workflows around a standalone proxy.

This also makes Gateway data more actionable. When a coding agent spends more than expected, we can inspect the trace, understand what happened, and use evaluations and observability data to improve the underlying agent behavior.

## What our internal rollout taught us and how it shaped the product

Running the Gateway on ourselves first surfaced the gap between how billing and routing look on paper and how they behave live. Three lessons that shaped where we invested next:

1. **Model pricing is more complex than a static table.** A lookup table goes stale quickly, so accurate cost accounting has to absorb caching, token-tier nuances and frequent provider prices changes. This pushed us to treat model pricing as a system than a constant: we're auditing our calculation logic and building in a more rigorous update path in order to maintain trustworthy costs.

2. **Not every client routes cleanly through Gateway, and support varies by app and by how it is managed.** In our rollout, Cursor only exposed base-url swap as a per-user setting covering only Chat, and not something that we could push through our MDM across the platform. Claude Desktop could only be passed through the gateway as a managed config, but turning it on shifted the app into a local agent in place of standard Chat (and the capability is early in development). Rather than wait on provider support, this shaped our approach to measure the delta of what gateway captures versus what the rest of our enterprise provider settings capture (i.e. monthly Claude plans) in order to have spend accounted for even when traffic can't flow through Gateway directly.

3. **Hard limits need a workflow around them.** A cap with no runway just blocks work. Engineers told us that they want early warning well before they hit a limit and a fast, auditable way to raise it. That feedback turned limits from static guardrails into a workflow: we're adding tiered alerting ahead of a threshold and exploring a paper-trailed budget-increase request flow so spend controls protect the business without getting in the way.

Dogfooding turned abstract edge cases into concrete product priorities including price accuracy, graceful handling of clients who can't route through Gateway, and managing limits on spend.

## The result

Since rolling out LangSmith LLM Gateway internally, our LLM costs have stayed within budget.

The bigger change is that spend is no longer something we only understand at the end of the month. Engineering leaders can see usage as it happens, set limits at the right level, and give teams the flexibility to use coding agents without creating surprise bills.

LangSmith LLM Gateway is currently in private beta. Sign up here to request access.
