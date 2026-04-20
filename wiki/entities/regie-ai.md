---
title: "Regie.ai"
description: "AI-native sales engagement platform replacing Outreach/Salesloft — designed for mixed teams where the agent is a first-class actor with prospecting, outreach, follow-ups, routing, and human escalation capabilities"
tags: [company, startup, regie-ai, sales, sales-engagement, agent-automation]
status: skeleton
related:
  - "[[concepts/context-graph]]"  # Regie builds decision traces for sales workflows
  - "[[concepts/harness-engineering]]"  # Agent orchestration for sales engagement
status: skeleton
created: 2026-04-20
---

# Regie.ai

> TODO: Research company blog, product, and technical depth to build L3 page.

## Profile

- **Type:** AI Agent Startup (Sales Engagement)
- **Website:** [regie.ai](https://www.regie.ai/)
- **Focus:** AI-native sales engagement platform replacing Outreach/Salesloft
- **Positioning:** Designed for a mixed team where the agent is a first-class actor

## Role in Foundation Capital's Framework

Regie.ai exemplifies **Path 1** (Replace Existing Systems of Record from Day One):

> "Regie has chosen to build an AI-native sales engagement platform to replace legacy platforms like Outreach/Salesloft, which were designed for humans executing sequences across a fragmented toolchain."

Key characteristics:
- **AI-native architecture** — Agents are first-class actors, not human assistants with AI assists
- **Agent capabilities:** prospect, generate outreach, run follow-ups, handle routing, escalate to humans
- **Event-sourced state** — Every decision (who to contact, what message, when to escalate) is recorded as a trace
- **Policy capture native** — Sales engagement policies (contact frequency, message templates, escalation rules) built into the architecture

## Why Sales Engagement Is a Strong Fit

Sales workflows have high exception density:

1. **Deal desk decisions** — Discount approvals, custom terms, competitor responses all require exceptions to standard playbooks
2. **Follow-up timing** — When to follow up depends on prospect behavior, deal stage, and historical precedent
3. **Routing decisions** — Which rep should handle which deal based on capacity, expertise, and relationship history
4. **Escalation triggers** — When to escalate to senior sales or pre-sales based on deal size, technical complexity, or competitive situation

These decision traces compound into a context graph that enables increasingly automated sales engagement.

## Relationship to Context Graphs

Regie's architecture naturally captures decision traces for sales workflows:

- Every outreach decision is recorded with context (prospect profile, deal stage, competitive situation)
- Exception approvals (discounts, custom terms) are tracked with who approved and why
- Follow-up patterns and their outcomes become searchable precedent
- Routing decisions build a library of optimal assignments

The context graph becomes a competitive moat: the more deals processed, the smarter the routing and outreach decisions.

## TODO

- [ ] Research funding history and investors
- [ ] Find technical blog posts or documentation on AI-native architecture
- [ ] Understand how they handle CRM integration (Salesforce)
- [ ] Check for case studies or customer testimonials
- [ ] Research how agents and humans collaborate in their model
- [ ] Remove skeleton status after enrichment