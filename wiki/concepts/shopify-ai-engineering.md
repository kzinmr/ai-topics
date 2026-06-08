---
title: "Shopify's AI-First Engineering"
created: 2026-05-20
updated: 2026-05-20
type: concept
tags:
  - shopify
  - ai-adoption
  - infrastructure
  - llm-proxy
  - claude-code
  - coding-agents
  - agentic-engineering
  - strategy-execution
  - strategy
  - leadership
  - product-management
  - optimization
  - developer-experience
  - career
  - education
  - company
  - mcp
  - multi-agent
sources: [raw/articles/2026-05-20_zodchiii_shopify-claude-code-setup.md, raw/articles/2026-05-20_pragmatic-engineer_farhan-thawar-shopify-ai.md, raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--32394213.md]
---

# Shopify's AI-First Engineering

[[entities/shopify|Shopify]] has emerged as a reference implementation for organizational [[ai-adoption]] at scale — 23,000 engineers, no token spending limits, and a target of 96% autonomous coding by Q3 2026. This page documents the architectural, cultural, and management practices that define Shopify's AI-first engineering approach, as described by [[entities/farhan-thawar|Farhan Thawar]] (VP Engineering) on The Pragmatic Engineer podcast and by external analysts.

## LLM Proxy Architecture

Rather than standardizing on a single AI tool, Shopify built an **internal LLM proxy** — a centralized gateway that routes every AI request through one infrastructure layer. Claude Code, GitHub Copilot, Cursor, and experimental tools (Devin, Gumloop) all flow through the same proxy.

This architecture provides:

- **Centralized cost control** — token usage tracked per engineer, team, and tool
- **Usage analytics** — which models are being used, for what tasks, with what results
- **Privacy protection** — sensitive data never leaves the controlled gateway
- **Model routing** — swap models without changing any engineer's workflow
- **Provider abstraction** — Anthropic, OpenAI, and others behind a single interface

The proxy embodies a key architectural principle: **standardize the infrastructure, not the tool**. Engineers can experiment with multiple AI tools while the organization maintains visibility and control at the proxy layer. This aligns with broader [[ai-infrastructure]] patterns where the control plane sits between tools and models.

## Tool Adoption Timeline

Shopify's AI tool adoption has been aggressive and early:

| Timeline | Tool / Event | Significance |
|---|---|---|
| **2021** | GitHub Copilot | First company outside GitHub to deploy Copilot — negotiated via direct email to GitHub's CEO, got 2 years free in exchange for feedback |
| **2022** | ChatGPT release | Continued Copilot expansion |
| **~2024** | Cursor | Deployed company-wide; notable that Cursor growth happened *outside* engineering — finance, sales, support teams using it for [[vibe-coding]] MCP servers |
| **2025** | Claude Code | Primary coding agent; [[concepts/claude-code|6 operational patterns]] emerged |
| **2025** | Devin, Gumloop | Experimental adoption, evaluating next-generation tools |
| **Nov 2024 – May 2025** | "Code Red" | 7-month tech debt elimination sprint (30-50% of engineering) |
| **Apr 2026** | Shopify MCP server | Open-sourced MCP server connecting Claude Code to Shopify APIs |
| **Q3 2026** | Target: 96% autonomous coding | 23,000 engineers working toward this deadline |

Key insight from the timeline: Shopify was experimenting with AI coding tools **before** ChatGPT made LLMs mainstream. Their 2021 Copilot deployment gave them a multi-year head start on organizational learning.

## Strategy:Execution Ratio Flip

The most significant philosophical shift at Shopify:

```
2024 workflow:
Strategy: 30% → Execution: 70%

2026 workflow:
Strategy: 70% → Execution: 30%
```

Because AI handles most coding, engineers now spend **70% of time on strategy**: mapping user flows, validating market demand, choosing the right architecture. Only 30% on execution. This represents an estimated ~20% productivity improvement — not from writing more code, but from **testing 10 approaches instead of 2**, faster prototyping, and higher-fidelity deliverables.

This is not just a ratio change — it's a redefinition of the engineer's role. The engineer becomes a **strategy-first decision-maker** who validates approaches through AI-generated prototypes rather than a line-by-line implementer. The agent handles *how*; the engineer focuses on *what* and *why*. This embodies the [[strategy-execution]] rebalancing that AI tools enable.

## No Token Spending Limits

Shopify has **zero cost limits** on AI token usage per engineer or team. This is unusual: most organizations impose budgets or quotas. Shopify's approach is the opposite:

- **Celebrate engineers who spend more** — investigate what high-spending engineers are doing, because it's probably high-value work
- **Push engineers to use expensive models** — O1 Pro, O3 Pro, Claude Max, not defaults
- **CTO Mikey's stance**: "If you don't pay personally for O1 Pro or Gemini Ultra, you are crazy"

The philosophy: penny-pinching on AI tools is counterproductive when the productivity gains outweigh the costs. This is [[cost-optimization]] through *removing* constraints rather than adding them — trusting that engineers will use expensive models when the task warrants it.

## 1,000 Interns Program

Shopify scaled its intern program from ~25 per term to **1,000 interns** (~350 per term, roughly 10% of engineering). The strategic hypothesis:

- **Interns are "AI reflexive"** — they grew up with LLMs as native tools, not learned behaviors
- **Interns change internal culture** — they bring AI-first workflows that senior engineers adopt
- **"The secret weapon"** — Farhan Thawar: "You always learn more from the interns" than they learn from the company
- **Internship may become the only entry-level path** into Shopify engineering

This is a deliberate [[career]] and [[education]] strategy: using early-career talent not just for capacity but as a **culture-change vector**. Interns demonstrate what's possible with AI-native workflows, pulling the organization forward rather than being trained into old patterns.

## GSD: Internal Project Management

Shopify built its own project management tool called **GSD** (Get Stuff Done) instead of using Jira or Linear. The philosophy: "first you make the tool, then the tool makes you."

GSD integrates AI deeply:
- **Auto-generated weekly project updates** from PRs + Slack conversations
- **Engineering manager dashboards**: focus time, meeting load, AI adoption rates
- **AI-native tracking**: the tool understands what engineers are actually doing, not just what they report

This reflects a broader [[developer-experience]] principle: tools shape behavior. By building their own PM tool, Shopify could optimize it for AI-augmented workflows rather than retrofitting AI onto a tool designed for pre-AI workflows.

## Tangle, Tangent, and SimGym — AI Infrastructure Triad

Under CTO [[entities/mikhail-parakhin|Mikhail Parakhin]], Shopify has developed three complementary AI infrastructure systems that go beyond the LLM proxy:

### Tangle — Reproducible ML & Data Workflows

**Tangle** is Shopify's reproducible ML and data workflow engine. It differs from traditional tools like Airflow:
- **Content-addressed caching** — creates network effects across teams; if one team computes something, others benefit
- Makes ML and data workflows reproducible, collaborative, and production-ready from the start
- More than just orchestration — it's a **collaboration layer** for data science
- Enables sharing of intermediate results, features, and model artifacts across the organization

### Tangent — Auto-Research Loop

**Tangent** is Shopify's automated research system:
- Optimizes **search, themes, prompt compression, storage**, and more
- Is becoming a **democratizing tool for PMs and domain experts**, not just ML engineers
- Represents **AutoML finally feeling real in the LLM era** — the system can explore solution spaces and find better configurations without human intervention
- Still has limitations — auto-research falls short in areas requiring deep domain expertise
- When Tangent discovers better configurations, Tangle makes those results shareable across teams

### SimGym — Customer Simulation

**SimGym** is Shopify's customer simulation platform:
- Simulates **merchant and buyer trajectories** using real historical behavior data
- Runs **counterfactuals** to evaluate interventions (discounts, campaigns, notifications)
- Evolved from comparing A/B variants to **telling merchants what to change on a single live storefront** to raise conversions
- Is expensive to run (multimodal models, browser farms, serving and distillation costs)
- Becomes much more powerful when combined with Tangle and Tangent
- Key insight from Parakhin: **simulated customers only work if you have real historical behavior data** — Shopify's commerce data provides a defensible moat
- Category-level behavior varies dramatically across commerce verticals
- Ideas like **Chinese Restaurant Processes** are showing up again in practice for modeling merchant/buyer trajectories

### How the Three Systems Interact

```
Tangent (Auto-Research) ──optimizes──→ Product Configurations
                                              │
Tangle (Reproducible Workflows) ──shares──→ Research Results
                                              │
SimGym (Customer Simulation) ──validates──→ Counterfactual Outcomes
```

Together, these three systems represent a **closed-loop AI infrastructure**: Tangent discovers better solutions, Tangle makes them reproducible and shareable, and SimGym validates them against simulated customer behavior. This is qualitatively different from the LLM proxy — the proxy manages AI tool access, while Tangle/Tangent/SimGym actively use AI to improve the product.

## Liquid AI and Non-Transformer Architecture

Shopify has deployed **[[entities/liquid-ai|Liquid AI]]** models in production for:
- **Low-latency query understanding** — real-time search processing
- **Large-scale catalog workloads** — millions of product entries
- **Sidekick Pulse tasks** — AI assistant infrastructure

CTO Mikhail Parakhin describes Liquid as "the first genuinely competitive non-transformer architecture" he has used in practice. The deployment signals Shopify's willingness to adopt non-Transformer architectures when they demonstrate clear efficiency advantages. Key question: can Liquid scale to frontier-level (100B+ parameters) with enough compute? If yes, Shopify would adopt it broadly.

## Coding Interviews for Directors and Above

Shopify added mandatory [[code-review|coding interviews]] for **all engineering director and VP hires**. Candidates pair-program with Farhan Thawar; AI tools are allowed and encouraged.

- **"If they don't use a co-pilot, they usually get creamed by someone who does"** — Farhan Thawar
- Tests ability to **discern good AI-generated code from bad**
- Evaluates whether leaders can effectively **orchestrate AI tools** rather than just manage people

This is a significant [[leadership]] signal: Shopify believes that in an AI-first organization, even senior leaders must be technically capable of working with AI coding agents. The interview tests not raw coding but **AI-augmented engineering judgment**.

## Parallel Agents and Critique Loops

Shopify's engineers deploy Claude Code in two complementary modes:

**Parallel agents** — multiple Claude Code instances working simultaneously on different parts of the codebase. One refactors auth, another writes tests, a third updates docs. The engineer reviews and merges outputs. This shifts the engineer's role from writing code to **orchestrating intelligent systems** ([[multi-agent]] pattern).

**Extended critique loops** — for complex architectural decisions, a single agent runs through propose→critique→revise→critique→finalize cycles, forcing Claude to argue with itself. This produces dramatically better results than single-pass prompting.

Both patterns are documented in detail at [[concepts/claude-code]].

## Safe Autonomy with Guardrails

Shopify's [[agent-safety|permission-based guardrail system]] creates a bounded autonomy zone:

- **Allow**: read, write (Edit), test, lint, git status/diff/add/commit
- **Deny**: git push, deploy, database drops (`db:drop`), secret access (`.env` files), destructive operations (`rm -rf`)
- **Default mode**: acceptEdits — agents can edit without constant human approval

Agents can work freely within the sandbox; humans stay in the loop for anything irreversible (push, deploy, data destruction). This pattern is a production reference for safe [[ai-agent-engineering]] at scale.

## Engineering Culture

Shopify's AI-first culture is driven by several reinforcing practices:

- **Role modeling** — leaders must code and share their AI workflows publicly (internal prompt library, hackathon participation)
- **"Hire smart people and pair with them on problems"** — not "get out of their way." Farhan spent 1 hour pairing with an Anthropic applied AI engineer to learn Claude Code internals
- **"No one has it figured out"** — explicit acknowledgment that the entire industry is learning simultaneously
- **Internal AI memo** — CEO [[entities/tobi-lutke|Tobi Lütke]] distributed an internal document setting AI expectations, establishing top-down commitment
- **No swim lanes** — "We don't try to put people into roles where you only think about product or only think about engineering. We're curious problem solvers."

## Key Numbers

| Metric | Value |
|---|---|
| Engineers | 23,000 |
| Target autonomous coding | 96% by Q3 2026 |
| Estimated productivity gain | ~20% (from exploring 10x more approaches) |
| Interns | 1,000 (vs 25/term previously, ~10% of engineering) |
| "Code Red" duration | 7 months (Nov 2024 – May 2025) |
| AI tools in use | Claude Code, Copilot, Cursor, Devin (experimental), Gumloop (experimental) |
| Token spending policy | No limits per engineer/team |

## See Also

- [[concepts/claude-code]] — Claude Code as a coding agent: patterns and guardrails
- [[entities/shopify]] — Shopify entity overview
- [[entities/claude-code]] — Claude Code entity overview
- [[entities/farhan-thawar]] — Farhan Thawar (VP Engineering, Shopify)
- [[entities/tobi-lutke]] — Tobi Lütke (CEO, Shopify)
- [[entities/anthropic]] — Anthropic
- [[concepts/agentic-design-patterns]] — Agentic design patterns
- [[entities/coding-agents]] — Coding agents ecosystem overview
