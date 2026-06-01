---
title: "Token Budget Wars"
type: x_article
date: 2026-05-27
author: Jaya Gupta
author_handle: "@JayaGup10"
x_article_id: "2059783769712943104"
tweet_id: "2059784669382791653"
getxapi: false
source_fallback: false
url: "https://x.com/i/article/2059783769712943104"
tags: [x-article, token-economics, enterprise-ai, ai-adoption, cost-optimization]
---

# Token Budget Wars

**Author**: Jaya Gupta (@JayaGup10), Foundation Capital
**Published**: May 27, 2026

Enterprise AI has moved from adoption to allocation.

The new currency at the top of the company is your ability to quantify your AI ROI. Every function is being asked the same question: what did you produce, and what did it cost? For the last 2 years, the CEO woke up to Jim Cramer on CNBC, watched competitors announce productivity gains, and told the company to use AI. The follow up question - show me the value - is what is creating pressure now.

Claude shipped in November 2025, after most 2026 annual budgets were locked. By Q1, enterprises were running multiples ahead of plan. Inference stopped being a line item to experiment with and became a recurring operating cost. That brought out a new question: where is AI actually creating value?

This is a hard question to answer because token utility is not quantified. The bill can't tell you whether the spend replaced labor, generated revenue, reduced risk, accelerated a workflow, or was just a bunch of engineers tokenmaxxing on the leaderboard. At a few hundred thousand dollars of spend, it still feels like experimentation. Past a certain point, call it seven figures, it turns into infrastructure. The technical variance starts producing material P&L swings: two runs of the same workflow on the same input can differ in token cost by 5-10x without anything visibly going wrong. At an experimental scale that variance is quite pricy, but when it's at infrastructure scale it's a number the CFO has to explain to the CEO.

Call that marginal token utility: the business value created by each additional dollar of inference. It's the number that matters at scale, and the number most companies cannot see.

The question in board rooms is changing from "is AI useful?" to "where is AI actually creating leverage?" And that is why the token budget wars are really about the allocation of tokens.

## The fight for ownership

The fight for ownership of tokens is getting charged so fast because it's running into a thirty-year executive instinct that big teams equal big jobs and scope and power because the visible marker of a senior executive's success was the size of the team they ran (directs, skip-levels, people in the org).

However, when intelligence becomes the scarce resource, the new marker is how much of it you're orchestrating.

AI spend is really competing with labor.

Most AI budget requests are one of three claims: replace outsourced labor, replace internal labor, or generate new revenue.

A person has a salary. A BPO contract has a price per ticket, claim, invoice, or review. Humans understand these units of measure, but inference is more since the cost of a completed task depends on how the system behaves along the way. A claim that requires three retries, human correction, and a frontier model may be more expensive than the outsourced labor it was supposed to replace, which is why the conversation is moving to what is the cost of a completed outcome? Cost per resolved ticket, processed claim, reviewed contract, completed invoice, avoided hire, retained customer, or dollar of revenue moved.

Executives have realized that BPOs are the easiest place benchmark because the work is already priced in completed units. Internal labor is much harder to compare against AI because employees do many things everyday, productivity gains show up as avoided hiring or diffuse capacity, and managers resist reducing headcount on the basis of partial automation. BPO gives the business teams a measurable baseline.

## Why this is different from SaaS

SaaS trained companies to treat usage as a proxy for value.

AI breaks that. The same workflow can consume radically different amounts of inference depending on the prompt, retrieved context, model selected, tools called, retries, and whether the agent gets stuck. The unit on the invoice — a token — is stable, while the amount of work it represents is not.

So more precisely: the signal and the noise share the same unit. A rising token bill can mean real work is getting done, but it can also mean compute is leaking into bad prompts, irrelevant context, unnecessary tool calls, redundant reasoning, and overpowered models. Two enterprises with identical token bills can be running completely different operations underneath, one converting inference into outcomes, the other paying for thrash that looks identical on the line item.

SaaS usage told you the software had been adopted. AI usage tells you the meter is running. It doesn't tell you whether your company is cooking.

## Why marginal token utility is hard to see

Three things:

1. **Retry tails**. If an agent completes a workflow correctly on the first pass with probability p, expected tokens per resolved workflow scale roughly as T/p, where T is the base cost. A drop in completion rate from 90% to 70% raises effective cost per resolution by about 28%, not 20%, because the failures compound.

2. **Context inflation**. Inference cost scales roughly O(n²) in context length for attention-heavy operations, so doubling the context roughly quadruples the reasoning cost. Everyone wants the model to have enough information, so the system over-supplies retrieval pulls fifty documents when five would do, connectors dump entire email threads, agents carry stale conversation history.

3. **Routing**. When teams don't know which model is good enough, they default to the strongest one. A basic classification task runs on the same model used for complex reasoning. Across millions of calls, the difference between sending easy tasks to a smaller model and sending everything to the frontier model is often the difference between a manageable bill and a board-level problem.

## Software vs non-software enterprises

Non-software industries will feel this pain in the form of a transformation. Software companies will see them first because the work being optimized is already instrumented. Engineering has PRs, commits, deploys, incidents, cycle time, MTTR and these tie into product.

Non-software enterprises will feel the problem more deeply because the work is operational. Think claims, underwriting, support cases, compliance reviews, supply chain exceptions, payment disputes. These workflows were historically measured in labor, cycle time, SLA adherence, and error rates, and need to be right under audit, not just right on average. The unit of work and the unit of cost don't speak the same language, and they don't sit inside the same organization.

I believe that software companies will experience the token budget wars as a productivity measurement problem which tracks to all of the "AI layoffs" that have happened whereas non-software enterprises will experience them as a transformation problem.

## The missing layer: token-to-outcome attribution

It needs a conversion layer that connects inference spend to the work performed and the business outcome produced. That layer has to answer three questions: what did the workflow actually cost, including retries and corrections? Which parts of the agent trace mattered, and which were thrashing? Did the work change the operating model: fewer tickets per agent, shorter claims cycles, smaller BPO line items, deferred hires?

The next layer is outcome attribution in the language of the business, not just "this workflow cost $2.13," but "this class of claims is cheaper with agents than BPO, except when the policy requires exception documents, in which case the retry tail destroys the economics."

## Measurement becomes memory

To connect a token to an outcome, the enterprise has to capture what happened in between: what the agent saw, what it retrieved, which tools it called, what it ignored, where it retried, when a human overrode it, which exception applied, which precedent mattered, and why one path worked while another failed. The measurement layer has to record decision traces, which is something enterprises have never really had.

Decision rationale is one of the most perishable assets in a company because it lives in Slack threads, email chains, escalation calls, and people's heads but the thing is those people leave and processes change.

AI changes that because agents create traces. Every retrieval step, tool call, retry, escalation, human correction, and final decision becomes part of the path from context to action to outcome. At first, companies will capture these traces to justify spend. But once captured, the traces become more valuable than the cost report because they become a durable record of how the organization actually decides (context graph).

## The allocation layer is the prize

If inference becomes a metered resource inside the customer's operating model, every dollar has to defend itself. Which vendors can show when tokens convert into outcomes, when they don't, and why?

Enterprises will not figure this out on their own. They will buy it as a transformation. The Fortune 500 has run this playbook before: buckle up, hire McKinsey, hire every Palantir alum on the market, and drive the change top-down from the CEO. Token-to-outcome attribution will arrive in a similar way ERP, BI, and digital transformation did: as a "program" with executive sponsorship and a piece of infrastructure underneath it that becomes the new source of truth.

The company that owns token-to-outcome attribution makes the allocation calls, which workflows deserve more compute, which get capped, which get cheaper models, which stay human, which replace BPO. And once you make those calls, you control where AI spend goes inside the enterprise and get to have the trust to allocate.

The first phase of enterprise AI proved that models could do work and the next phase will decide how much of that work is worth it. As Charlie Munger put it: show me the incentive and I will show you the outcome.
