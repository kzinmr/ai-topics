---
type: x_article
x_article_title: "Forward Deployed Engineering 101"
x_article_author: "Varick / vasuman (@vasuman)"
source_url: https://x.com/i/article/2057172544277606401
date: 2026-05-20
getxapi: false
tags:
  - forward-deployed-engineering
  - applied-ai
  - career
  - varick
---

# Forward Deployed Engineering 101

By the end of this article, you should understand why Anthropic, OpenAI, Google, and other AI companies are looking for FDEs, and how you can capitalize on this demand.

## Why do AI companies need FDEs

If you believe intelligence is becoming commoditized, it then follows that the only competitive edge is how and where you use it. There is no competitive advantage in intelligence alone. Therefore, determining how and where companies use it becomes the most important role — that is the role of a forward deployed engineer.

Businesses hire an Applied AI company (like Varick) that deploys FDEs to help them get the most out of the technology. This gives them access to a team that has already done large-scale AI transformations that make clients move much faster than their competitors.

The FDE is a highly skilled engineer who can understand the customer's problems very deeply, write code into a code base they've potentially never seen before, and communicate the business impact to a non-technical decision maker to close the deal. This is a million-dollar hire.

## What the role requires

Being an FDE requires you to be on-site with a customer. The term FDE originated from Palantir, and they took being on-site very seriously. In 2010, they worked with the Special Forces group in Afghanistan — the Special Forces would go on the mission in the day, get feedback, and route it to the FDEs who would ship code during the night.

## About the role — Three phases: Audit, Evals, and Deployment

### Audit
On-site with a client, mapping processes/workflows in different teams within the company. Key decisions:
- **Rule-based but variable inputs → agent**: If a workflow can be distilled into rules but the inputs vary (email, PDF, scanned image), and the work involves calling tools
- **Predictable rules + predictable inputs → code**: Code is faster and cheaper
- **Pattern recognition + domain expertise → manual**: Don't over-automate

Look for high-volume automations. Don't overuse AI — most automation tasks can be done with a series of tool calls and just one call to an LLM as an orchestrating layer.

### Evals
If a customer is spending millions on an AI deployment, they need to know it's working. A good eval:
1. **Trace the human's steps** and grade the AI on each one
2. **Start small with great examples** of the intended outcome, then measure everything against them

Evals prove value to the customer — a good agent evaluation is what an executive needs to trust the agent will provide ROI.

### Deployment
- **Avoid large-scale data migrations**: Build APIs over existing data layers (SharePoint or databases) and place a model on top as an orchestrator
- **Create an execution environment**: A sandbox directly in the company's infra to test the agent safely
- **Start slow**: Take a small workflow, get it to work, then layer on additional capabilities
- **Start with the smallest unit of autonomy**; only then give it the capability to take action

## How to become an FDE in 30 days

Three backgrounds find the most success: Consultants, Product Managers, and Software Engineers.

### Consultants/PMs
Build a high-quality portfolio:
- A production-ready AI agent that can execute an entire process
- A RAG pipeline built on custom dataset
- An eval framework scoring agent outputs
- An MCP connecting LLM to legacy software

### Software Engineers
Build similar projects, but explain every component: tech stack, results, iterations, business outcomes. Most importantly, have a reason for building those agents — what was the pain point?

### 30-day outline
- **Checkpoint 1 (7 days)**: Agent loop, tool calls, guardrails, context window vs external memory, audit trail
- **Checkpoint 2 (14 days)**: Structured outputs, demo to prod, checkpointing
- **Checkpoint 3 (21 days)**: Retry logic, cost optimization, golden dataset, multi-agent pipelines
- **Checkpoint 4 (Final week)**: Review, communicate everything out loud, tie to business metrics

## TLDR
- The FDE is the most in-demand role in tech right now
- Three phases: audit, evals, deployment
- Portfolio + ability to speak about it are deciding factors
- Lack of communication ability is a deal-breaker
- Know when AI isn't the answer — this builds trust and ROI
- Varick is hiring: https://www.varickagents.com/careers
