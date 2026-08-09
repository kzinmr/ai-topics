---
title: "AI Adoption Barbell Distribution"
created: 2026-08-09
updated: 2026-08-09
type: concept
tags:
  - concept
  - ai-adoption
  - enterprise-ai
  - enterprise-agents
  - metrics
  - ai-economics
  - career-strategy
  - strategy
  - consulting
  - fde
sources:
  - raw/articles/2026-08-07_varick_ai-adoption-is-a-myth.md
---

# AI Adoption Barbell Distribution

The **AI adoption barbell distribution** is a framework describing how enterprise AI usage concentrates at extremes: a small cadre of power users at one end, a vast majority of non-users at the other, and a thin middle of mediocre adopters. Coined by [[entities/vasuman]] (CEO of [[entities/varick-agents]]) in August 2026, the barbell explains why broad "adoption" metrics consistently fail to translate into organizational productivity gains.

## Summary

Across organizations of 50 to 5,000 people, AI adoption follows a consistent **10-70-20 split**: 5-10% power users, ~70% non-users, and ~20% mediocre users. This distribution is structural, not transitional — it persists regardless of rollout quality, training investment, or tool sophistication. Every new AI capability release raises the skill floor and widens the gap between frontier users and the majority. The implication: enterprise AI strategy must stop treating adoption as a yes/no question and instead design for this barbell explicitly, routing work through background agents for the 70% while amplifying and sharing the skills of the top 10%.

## The Barbell Distribution

The barbell pattern emerged from [[entities/varick-agents]]' work with "the largest companies on the planet" implementing AI agents and strategy. The distribution is remarkably stable:

| Segment | Share | Behavior |
|---------|-------|----------|
| **Power users** | 5–10% | Daily use, skill files, connectors, agent orchestration. Evangelists who tinker with AI outside work. |
| **Mediocre users** | ~20% | Use AI a few times per day, poorly. Extract a fraction of the value power users get. |
| **Non-users** | ~70% | Opened ChatGPT maybe 4 times in 2 years. Used an outdated model once and dismissed AI entirely. |

The distribution holds across orgs from 50 to 5,000 people. A Claude Cowork rollout described by one operations leader produced precisely this split — and despite the dashboard showing "adoption," nothing got faster. **Both were true simultaneously.**

A perfect rollout does not fix this. Even an eight-figure enterprise license commitment yields the same barbell. The claim that "these are just companies doing it poorly" is false: the barbell is structural.

## Adoption Metrics Are Binary, Skill Is a Spectrum

Enterprise adoption tracking collapses a full skill spectrum into yes/no questions:

- "Did this person log in this month?"
- "Did this person send at least 5 prompts per day?"

This produces the paradox captured by McKinsey's 2025 survey: **88% of organizations use AI in at least one business function, but only 6% see more than 5% EBIT impact.** MIT NANDA's GenAI Divide report found that 5% of integrated pilots extract millions in value while 95% show no measurable P&L impact.

The metric that actually matters — **how skillful is each person at using AI, and what is their ROI per token used?** — is almost never tracked.

### Using It vs. Using It Well

Using AI and using it well are separate skills. Power users develop craft:

- Knowing when to clear context
- Converting repeated patterns into skill files rather than retyping prompts
- Distinguishing the 15% of work that needs model judgment from the 85% that needs deterministic code
- **Reading a diff properly before accepting it**

The gap between a "slop-cannon" user (paste Jira text, hit submit, skim, merge) and a refined power user (flag code locations, constrain scope, skill-file guardrails, review diffs, catch stray changes) is enormous — and at least half of any organization will never close it.

## Token Concentration

Token consumption mirrors the barbell. In one enterprise rollout, **10% of users burned 90% of tokens.** If the other 90% used AI the way the top decile does, costs would 10x — turning an $10M commitment into $100M. This concentration is both a cost-control mechanism and a signal of where real work is happening. See also [[concepts/enterprise-ai-cost-management]].

## Incentive Misalignment

The barbell persists because every stakeholder's incentives reinforce it:

- **AI vendors** build for frontier users (the loudest, most flattering, highest-spend cohort). Every feature release raises the skill floor, widening the chasm.
- **Frontier users** have no reason to close the gap — their leverage IS the chasm. They work 70% faster or do the work of 3 people. If everyone catches up, they lose their edge.
- **Enterprises** are seduced by "prompt training" programs that address only 10% of the problem. The other 90% — understanding which workflows should never touch a model vs. which should be fully automated — is company-specific and requires on-site work to determine.

"Train your employees how to prompt" sells easily but solves little. The frontier-users-and-vendors feedback loop keeps tightening while the 70% remain untouched.

## The Solution Framework

[[entities/vasuman]] proposes a four-part approach:

### 1. Train Diagnostically, Not Remedially

Training is necessary — but its purpose is **diagnostic**: to identify who is capable of reaching the frontier vs. who is not. Some employees are interested in AI but lack time and leverage to go deep. Training surfaces ability and comfort level across the org.

### 2. Publish Power-User Skills with Ranking Incentives

Give power users a shared database where every skill they build gets posted, ranked, and installed by others. Ranking provides the incentive: power users will trade their edge for status within the organization. This is the only mechanism observed to turn one person's breakthrough into something sharable. However, even with full distribution, ~50% of people will never use a skill.

### 3. Background AI for Everyone Else

For the 70%, work must get done without them changing how they work. **Put the AI in the background** — build agents into existing systems of record (Salesforce, NetSuite, Dynamics) so repetitive processes run autonomously. Humans become approvers, rejecters, and editors of agent output rather than prompt-writers.

> **People are not in the market for a tool that helps them get the work done. They just want the work done.**

### 4. Change the Reporting Metric

Stop reporting "adoption" to the board. Report what share of work is **manual vs. hybrid vs. fully automated**. This is the only reporting framework that maps to real organizational outcomes. See also [[concepts/ai-benchmarks/ram-relative-adoption-metric]].

## Related Concepts

- [[concepts/enterprise-agents]] — Building agents for enterprise systems of record
- [[concepts/forward-deployed-engineering]] — The on-site, company-specific work required to identify automatable workflows
- [[concepts/ai-adoption-failures-and-enterprise-psychosis]] — The psychological and organizational barriers to AI adoption
- [[concepts/enterprise-ai-scaling-patterns]] — Patterns for scaling AI across large organizations
- [[concepts/ai-services-joint-ventures]] — Service-delivery models for enterprise AI
- [[concepts/ai-benchmarks/ram-relative-adoption-metric]] — Relative Adoption Metric as an alternative to binary adoption tracking
- [[concepts/enterprise-ai-cost-management]] — Token economics and cost control in enterprise AI rollouts
- [[entities/vasuman]] — CEO of Varick Agents, author of the barbell thesis
- [[entities/varick-agents]] — Enterprise AI agent consultancy
