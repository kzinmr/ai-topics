---
title: "Token-to-Outcome Attribution"
type: concept
created: 2026-06-01
updated: 2026-06-01
tags:
  - token-economics
  - enterprise-ai
  - cost-optimization
  - enterprise-saas
  - economics
  - ai-adoption
aliases: ["marginal token utility", "token-outcome-attribution", "AI ROI measurement"]
related:
  - concepts/token-economics
  - concepts/context-graphs
  - entities/jaya-gupta
sources:
  - raw/articles/2026-05-27_jayagup10_token-budget-wars.md
---

# Token-to-Outcome Attribution

**Token-to-outcome attribution** is the business layer that connects LLM inference spend to the work performed and the business outcome produced. It addresses the fundamental enterprise problem that a token bill is a stable unit of cost representing an unstable amount of work — a rising bill can mean real productivity or compute leaking into bad prompts, irrelevant context, and overpowered models.

## The Core Problem: Signal and Noise Share the Same Unit

As enterprises move from AI experimentation to AI infrastructure (seven-figure annual inference spend), a critical measurement gap emerges:

- **SaaS usage was a proxy for value**: More logins, more seats, more API calls = more value. This relationship held for decades.
- **AI breaks this**: Two enterprises with identical token bills can be running completely different operations — one converting inference into outcomes, the other paying for thrash that looks identical on the line item.
- **Technical variance produces material P&L swings**: Two runs of the same workflow on the same input can differ in token cost by 5-10x without anything visibly going wrong.

> "The signal and the noise share the same unit. AI usage tells you the meter is running. It doesn't tell you whether your company is cooking."

## Marginal Token Utility

**Marginal token utility** is the business value created by each additional dollar of inference. It is the number that matters at scale — and the number most companies cannot see.

Three structural obstacles make it hard to measure:

### 1. Retry Tails

If an agent completes a workflow correctly on the first pass with probability p, expected tokens per resolved workflow scale roughly as **T/p**, where T is the base cost. A drop in completion rate from 90% to 70% raises effective cost per resolution by about **28%**, not 20% — because failures compound. In enterprise workflows with messy inputs and exception handling, failure doesn't just reduce accuracy, it changes the economics.

### 2. Context Inflation

Inference cost scales roughly **O(n²)** in context length for attention-heavy operations. Doubling the context roughly quadruples the reasoning cost. Systems over-supply: retrieval pulls fifty documents when five would do, connectors dump entire email threads, agents carry stale conversation history. Everyone wants the model to have enough information, so the system over-supplies.

### 3. Routing

When teams don't know which model is good enough, they default to the strongest one. A basic classification task runs on the same frontier model used for complex reasoning. Across millions of calls, the difference between sending easy tasks to a smaller model and sending everything to the frontier model is often the difference between a manageable bill and a board-level problem.

## The Token Budget Wars

Jaya Gupta (@JayaGup10, May 2026) coined the term "Token Budget Wars" to describe the organizational dynamics emerging as inference becomes a metered resource:

- **AI spend competes with labor**: Most AI budget requests are one of three claims — replace outsourced labor, replace internal labor, or generate new revenue. The conversation is shifting from "cost per token" to **"cost per completed outcome"** (per resolved ticket, processed claim, reviewed contract, avoided hire, retained customer).
- **BPOs become the benchmark**: Business Process Outsourcing contracts are already priced in completed units, making them the easiest baseline for comparison. Internal labor is harder to benchmark because employees do many things and productivity gains show up as diffuse capacity, not eliminated headcount.
- **Software vs non-software divide**: Software companies experience token budget wars as a productivity measurement problem. Non-software enterprises (claims, underwriting, compliance reviews, supply chain) experience them as a transformation problem — the unit of work and the unit of cost don't speak the same language and don't sit inside the same organization.

## The Token-to-Outcome Attribution Layer

The missing infrastructure layer must answer three questions:
1. **What did the workflow actually cost?** Including retries and human corrections.
2. **Which parts of the agent trace mattered?** And which were thrashing?
3. **Did the work change the operating model?** Fewer tickets per agent, shorter claims cycles, smaller BPO line items, deferred hires.

The next step is outcome attribution in the **language of the business** — not "this workflow cost $2.13" but "this class of claims is cheaper with agents than BPO, except when the policy requires exception documents, in which case the retry tail destroys the economics."

## Decision Traces as Organizational Memory

AI agents create **decision traces** — every retrieval step, tool call, retry, escalation, human correction, and final decision becomes a durable record of how the organization actually decides. At first, companies capture these traces to justify spend. But once captured, they become more valuable than the cost report:

- Decision rationale is one of the most perishable assets in a company (lives in Slack threads, email chains, escalation calls, people's heads)
- People leave and processes change, but **agent traces persist**
- This connects directly to Gupta's earlier [[concepts/context-graphs|Context Graphs]] thesis — the structural advantage of capturing the "why" behind the "what"

## The Allocation Layer as Strategic Prize

If inference becomes a metered resource inside the customer's operating model, every dollar has to defend itself. The company that owns token-to-outcome attribution makes the allocation calls:
- Which workflows deserve more compute, which get capped
- Which get cheaper models, which stay human, which replace BPO
- Where AI spend goes inside the enterprise

Enterprises will not build this on their own. Gupta predicts they will buy it as a transformation — similar to how ERP, BI, and digital transformation arrived as "programs" with executive sponsorship and new infrastructure layers that became the source of truth.

## Related Concepts

- [[concepts/token-economics]] — The technical side: GPU costs, pricing, optimization layers
- [[concepts/context-graphs]] — The structural advantage of capturing decision traces
- [[entities/jaya-gupta]] — Author of the Token Budget Wars framework

## Sources

- [[raw/articles/2026-05-27_jayagup10_token-budget-wars]] — "Token Budget Wars" by Jaya Gupta (May 2026)
