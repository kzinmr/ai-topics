---
title: "Data Aggregation Is Not a Moat"
source: "https://leehanchung.github.io/blogs/2026/05/10/data-aggregation-is-not-a-moat/"
author: "Hanchung Lee (Han Lee)"
date: 2026-05-10
type: article
tags: [data-moat, ai-agents, data-business, aggregation, web-scraping, semantic-web]
---

# Data Aggregation Is Not a Moat

> "Most 'data moats' are not that. They are collections of public, semi-public, or non-exclusive data wrapped in operational competence. Their defensibility came from the cost of aggregation, not from ownership of the underlying facts. When the aggregation cost collapses, the moat collapses with it."

## The Old Data Moat: Operational Burden

Traditional data businesses sold **the operational burden** of collecting, cleaning, storing, analyzing, and packaging data. The moat was that every step was annoying and expensive — licenses, anti-bot systems, parsing messy HTML, cleaning noisy records, normalizing schemas.

## How AI Agents Collapse the Moat

AI agents compress the cost structure of data aggregation. Instead of writing brittle crawler code against fixed page structures, a user can describe the workflow in plain language. Agents choose sources, navigate browsers, use logged-in sessions, read pages semantically, clean noise, summarize results, and package output. The pipeline shifts from a maintained software system to an on-demand user workflow.

This revives the 1990s Semantic Web / web-agent idea, but without requiring perfect semantic markup — AI agents route around the failure of standards by interpreting messy human-facing interfaces directly.

## What Still Matters vs. What Doesn't

| Still Defensible (Real Moat) | Collapsing (False Moat) |
|------------------------------|------------------------|
| Unique first-party transactions | Public/semi-public collections |
| Exclusive rights / regulated records | Non-exclusive data wrapped in operational competence |
| Private telemetry | Any dataset reproducible on-demand by an agent |
| High-quality feedback loops unavailable to others | Static databases, dashboards, monitoring services |

> "If a motivated user can ask an agent to recreate a useful slice of the dataset on demand, the static database becomes less valuable."

## Value Shifts Upward

**Old defensible layer:** "We collected the data."

**New defensible layer:**
- Trust
- Provenance
- Permissioning
- Workflow integration
- Evaluation
- Compliance
- AI/ML models and systems built on top of the data

> "The important question is no longer: who has the biggest pile of aggregated data? It is: who can produce a decision-quality answer that is current, verified, auditable, and integrated into the user's work?"

## Case Study: OpenAI and Anthropic

Both companies operate separate crawlers for search (`OAI-SearchBot`), user-directed browsing (`ChatGPT-User`), and model training (`GPTBot`, `ClaudeBot`). Their full value chain goes: ingest → clean → filter → transform → evaluate → post-train → compress into model weights → expose through products, APIs, coding agents, search, enterprise workflows, developer platforms.

**Input:** public, licensed, and user-provided data  
**Output:** intelligence-as-a-service  
**Key insight:** The model captures far more economic value than the raw dataset ever could.

## Conclusion

> "The old business sold a maintained pile of gathered data. The new workflow gives the user an agent that gathers, reasons, and acts when the need appears. Dataset as product is being compressed into an on-demand workflow that turns raw information into action."

**Actionable takeaway:** Focus defensibility on trust, integration, and the models/workflows built on top of data — not on the mere act of aggregation.
