---
title: "Service-as-Software"
created: 2026-05-04
updated: 2026-05-04
tags:
  - concept
  - ai-business-model
  - saas
  - venture-capital
  - ai-economics
aliases:
  - "Services: The New Software"
  - "Service as Software"
  - SaS
  - "Autopilot business model"
related:
  - [[entities/julien-bek]]
  - [[entities/sequoia-capital]]
  - [[concepts/harness-engineering]]
  - [[concepts/agent-harness]]
sources:
  - raw/articles/2026-03-05_sequoia-services-the-new-software.md
  - https://sequoiacap.com/article/services-the-new-software/
description: "AI business model where companies sell completed outcomes (the work itself) rather than productivity tools. For every $1 spent on software, $6 is spent on services — service-as-software captures the larger budget by replacing outsourced intelligence tasks."
---

# Service-as-Software

**Service-as-Software (SaS)** is an AI business model paradigm articulated by Sequoia Capital partner [[entities/julien-bek|Julien Bek]] in March 2026. It argues that the next generation of trillion-dollar companies will sell AI-executed **outcomes** (completed work) rather than AI-powered **tools** (software). This shifts the addressable market from software budgets to labor/services budgets — a 6x expansion.

## Summary

Traditional SaaS sells software seats to professionals (e.g., a CRM for salespeople). Service-as-Software sells the completed work itself (e.g., "your sales pipeline is managed"). The AI doesn't assist the knowledge worker — it *is* the knowledge worker, with human oversight for judgement-intensive exceptions.

The thesis builds on the observation that AI has crossed a threshold: **intelligence** tasks (rules-based, procedural, testing) are now automatable, while **judgement** tasks (taste, instinct, strategy) remain human. As AI systems accumulate proprietary data, the boundary shifts — today's judgement becomes tomorrow's intelligence.

## Key Framework

### Copilot vs. Autopilot

| Dimension | Copilot (SaaS) | Autopilot (SaS) |
|-----------|---------------|-----------------|
| **Customer** | The professional (lawyer, accountant) | The end-buyer (CFO, company) |
| **Value** | Makes the professional more productive | Delivers the final outcome |
| **Budget** | Software/tool budget | Labor/services budget (6x larger) |
| **Responsibility** | Human takes responsibility | AI/service provider takes responsibility |

### Intelligence vs. Judgement

- **Intelligence**: Complex rules, debugging, testing, translation, form-filling. AI has crossed this threshold.
- **Judgement**: Experience, taste, instinct, strategic decisions (e.g., which feature to build). Still human domain — but the boundary is shrinking.

> "Writing code is mostly *intelligence*. Knowing what to build next is *judgement*."

## The Outsourcing Wedge

The most effective market entry strategy targets tasks that are **already outsourced**:

1. **Acceptance** — The company already pays external providers for this work
2. **Budget** — There's a clear line item to substitute
3. **Frictionless** — Replacing an outsourcing contract is a "vendor swap"; replacing internal headcount is a "reorg"

> "The outsourced task is the wedge. The insourced work is the long-term TAM."

## Opportunity Map

| Vertical | TAM | Intelligence Ratio | Key Players |
|----------|-----|-------------------|-------------|
| Insurance Brokerage | $140-200B | High (form-filling, carrier shopping) | WithCoverage, Harper |
| Accounting & Audit | $50-80B | High (340K accountants lost in 5 years) | Rillet, Basis |
| Healthcare Revenue Cycle | $50-80B | Pure intelligence (notes→ICD-10 codes) | Anterior |
| Claims Adjusting | $50-80B | High (aging workforce) | Pace, Strala |
| IT Managed Services | $100B+ | High (SMBs already outsource) | Edra, Serval |
| Recruitment & Staffing | $200B+ | High (screening, outreach) | Juicebox, Mercor |
| Supply Chain/Procurement | $200B+ | Medium-High (long-tail suppliers) | Magentic, Tacto |
| Legal Transactional | $20-25B | High (NDAs, filings) | Harvey, Crosby |
| Management Consulting | $300-400B | Low-Medium (judgement-heavy) | (disaggregating) |

## Relationship to Harness Engineering

Service-as-Software and [[concepts/harness-engineering|Harness Engineering]] are parallel concepts applied to different domains:

| Aspect | Harness Engineering | Service-as-Software |
|--------|-------------------|---------------------|
| **Domain** | Software engineering | Business models |
| **Core claim** | The harness (infrastructure around LLM) determines reliability more than the model | The outcome (completed work) captures more value than the tool |
| **Key figure** | Hamel Husain, Atal Upadhyay | Julien Bek, Sequoia Capital |
| **Budget shift** | From model selection → infrastructure investment | From software spend (1x) → labor spend (6x) |

Both share a structural insight: the layer surrounding the core capability (model or tool) is where the defensible value lies.

## The Innovator's Dilemma

Incumbent "Copilot" companies from 2025 face a structural challenge transitioning to "Autopilot" models: selling the work directly cuts their professional customers out of the loop. This creates an opening for **pure-play autopilot startups** targeting the larger labor budget from day one.

## Related Concepts

- [[entities/julien-bek]] — Author of the thesis
- [[entities/sequoia-capital]] — Firm behind the thesis
- [[concepts/harness-engineering]] — Parallel concept in software engineering
- [[concepts/agent-harness]] — The technical architecture that enables service-as-software

## Sources

- [Services: The New Software — Sequoia Capital (Mar 2026)](https://sequoiacap.com/article/services-the-new-software/)
- [Fortune: Are services the new software? (Apr 2026)](https://fortune.com/2026/04/21/services-are-the-new-software-sequoia-venture-capital-julien-bek-ai-native-eye-on-ai/)
- [Forbes: Sequoia Says AI Will Kill Software Tools (Apr 2026)](https://www.forbes.com/sites/josipamajic/2026/04/01/sequoia-says-ai-will-kill-software-tools-by-becoming-the-work/)
