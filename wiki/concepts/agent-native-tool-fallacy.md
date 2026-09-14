---
title: "The Agent-Native Tool Fallacy"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [concept, agent-tooling, agent-harness, tool-use, ai-agents, software-engineering, prediction, anti-pattern]
sources:
  - raw/articles/seangoedecke.com--dont-build-tools-for-ai-agents--cbc5138d.md
confidence: medium
description: "Sean Goedecke's argument that 'build X for AI agents' products mostly fail: agent-good tools converge on human-good tools, existing tools hold a training-data moat, and agent ergonomics are unknown and shifting fast. Positioning for agents means API-over-UI margin work, not product redesign."
related: [writing-effective-tools-for-ai-agents, better-models-worse-tools, harness-engineering, agentic-engineering, ai-slop, tool-use, agent-harness-design]
aliases: ["don't build tools for AI agents", "agent-native tool fallacy"]
---

# The Agent-Native Tool Fallacy

**The agent-native tool fallacy** is the name for the widely-repeated claim that software should be redesigned from the ground up for AI agents rather than human users. Sean Goedecke (ex-Slack ML engineer) argues in ["Don't build tools for AI agents"](https://seangoedecke.com/dont-build-tools-for-ai-agents/) (September 2026) that most "X for AI agents" products will fail, for three structural reasons. ([raw](raw/articles/seangoedecke.com--dont-build-tools-for-ai-agents--cbc5138d.md))

## The Three Arguments

1. **Agent-good ≈ human-good.** Agents use computers the way human engineers do — text entry, API calls, reading text/images. A hypothetical redesign of Jira "for agents" would look almost identical to Jira. Goedecke's humanoid-robot analogy: because robots are shaped for the human world, human tools suit them, creating a self-reinforcing cycle — build humanoid robots so they use human tools, so build human tools. Human-like agents are "pound-for-pound more useful in our current world."

2. **Training data is a moat for incumbent tools.** If a new agent-native tool is 20% better for agents than the incumbent human tool, but the agent's familiarity with the incumbent is worth more than 20%, the agent should still use the incumbent. Agents carry billions of tokens of knowledge about existing languages, libraries, and idioms — which is why Goedecke is suspicious of agent-specific programming languages.

3. **Agent ergonomics are unknown *and* shifting.** "Just-so stories" (e.g., agents prefer statically-typed languages for tight feedback loops) don't survive measurement; plausible arguments exist in both directions (Golang compiles fast vs. Golang boilerplate clogs context). The ground shifts under builders: context-size minimization was a primary worry one year, and by 2026 [[concepts/context-compaction|compaction]] is good enough to re-compact a 272k window almost unlimited times.

## What To Do Instead (the marginal version)

Goedecke's concession: expose plain-text/Markdown views, build a functional API, ship MCP servers or CLIs. But these are *marginal* improvements — "building for AI agents" currently just means "prioritizing the API over the UI" — and even that may not be durable: as GPT-6-Astra's computer-use capability improves, the gap between tools-for-AIs and tools-for-humans closes.

Note the counterexample within the same period: agents may use existing tools *more* than their human owners (Goedecke's own agents use Datadog far more than he does, via speed + parallelism). Agent-heavy *usage* of human tools does not imply agent-native *design* is the answer.

## Tensions With Existing Wiki Positions

This page sits in genuine tension with the harness/tooling literature:

- [[concepts/writing-effective-tools-for-ai-agents]] (Anthropic-derived guidance) and [[concepts/mu-tools-for-agents]] treat tool-surface redesign for agents as high-leverage. Goedecke's claim (1) doesn't deny tools *matter* — it denies that *greenfield agent-only products* outcompete incumbents. Anthropic-style guidance is about making *your existing product* legible at the margin, which is exactly Goedecke's concession list.
- [[concepts/better-models-worse-tools]] (Ronacher) shows agent-oriented tool schemas can *regress* model performance — supporting claim (3): we do not yet know which agent tool ergonomics actually help, andSchema-level guesses can be wrong even for frontier models.
- [[concepts/harness-engineering]] reframes the same territory: the winning layer so far is the *harness around general-purpose tools* (bash, editor, browser) rather than bespoke agent-native apps — consistent with Goedecke, since harnesses compose existing human tools.

Confidence is `medium`: a single practitioner's argument, plausible but untested against the counter-industry of "agent-native infrastructure" startups. Filed as a thesis with its conditions, not settled fact.

## Key Takeaways

- The burden for an agent-native tool is *not* "better for agents" but "better for agents **by more than** the incumbent's training-data familiarity advantage."
- Ergonomic knowledge about agents decays fast (context-size anxieties → compaction era within ~a year); bet on interfaces that survive model turnover: plain text, APIs, CLIs, MCP.
- Improving an existing product's agent legibility ≠ redesigning products for agents. The first is durable advice; the second is mostly a doomed category.

## See Also

- [[concepts/writing-effective-tools-for-ai-agents]] — the standard prescriptive guidance Goedecke's argument bounds
- [[concepts/better-models-worse-tools]] — empirical case that agent tool ergonomics are not yet understood
- [[concepts/harness-engineering]] — the layer that actually absorbs "agent ergonomics" in practice
- [[entities/seangoedecke-com]] — author
- [[concepts/ai-slop]] — same author's adjacent thesis on AI-generated quality decay
