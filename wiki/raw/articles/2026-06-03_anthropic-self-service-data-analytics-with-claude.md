---
title: "How Anthropic Enables Self-Service Data Analytics with Claude"
author: Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry
date: 2026-06-03
source_url: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
type: blog-post
tags:
  - data-science
  - ai-agents
  - anthropic
  - claude-code
  - enterprise-ai
  - analytics
---

# How Anthropic Enables Self-Service Data Analytics with Claude

> Source: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
> Date: June 3, 2026
> Authors: Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry (Anthropic Data Science & Data Engineering)

## Summary

Anthropic automates **95% of business analytics queries** via Claude with **~95% accuracy in aggregate**. The article describes their agentic analytics stack and best practices for self-service business insights using Claude Code.

## Key Insight: Data Is Not Software

LLMs' generative abilities are a double-edged sword. Coding is an open-ended solution space that rewards creativity, with documentation and tests as natural guardrails. In contrast, analytics use cases often have **a single correct answer using a single correct source** with no deterministic way of proving correctness.

The central problem: **mapping a user's question to specific and up-to-date entities in the data model and knowing the correct way of working with them**. If this mapping is solved, SQL generation becomes trivial.

## Three Failure Modes

1. **Concept <> Entity Ambiguity**: With hundreds of viable options in a data model, the agent can't choose the correct fields (e.g., "active users" — what actions? include fraud? what lookback window?)
2. **Data Staleness**: Data sources, business definitions, and schemas change constantly; agent knowledge goes stale
3. **Retrieval Failure**: The right information exists in the data model but the agent doesn't find it due to vast search space

## Agentic Analytics Stack

### Layer 1: Data Foundations
- Dimensional modeling, shift-left testing, freshness/completeness checks
- **Canonical datasets**: Curate a small set of single source-of-truth datasets, aggressively deprecate near-duplicates
- **Enforce standards**: Via tooling (agent routed to canonical first), CI (changes bypassing fail review), and mandate
- **Colocate artifacts**: All data code (modeling, semantic layer, reference docs, dashboards) in single repo with CI cross-layer integrity checks
- **Metadata as first-class product**: Column descriptions, metric definitions, grain docs, lineage, ownership

### Layer 2: Sources of Truth (in descending trust order)
1. **Semantic Layer**: Compiled metric/dimension definitions. Agent structurally required to use first. LLM auto-generation of metric definitions was net-negative — "generate documentation with Claude, but have humans own definitions"
2. **Lineage & Transformation Graph**: When semantic layer doesn't cover, lineage lets agent reason about upstream models
3. **Query Corpus**: Historical SQL. In practice, raw retrieval of thousands of prior queries moved accuracy by <1 point. Distill into structured reference docs instead
4. **Business Context**: Company knowledge graph (docs, roadmaps, decision logs, org structure) for resolving ambient references

### Layer 3: Skills (Procedural Knowledge)
- Without skills: **21% accuracy** on evals. With skills: **consistently above 95%**, regularly ~99% in certain domains
- **Pairwise skills**: Knowledge skill (thin router loading domain details on demand) + Unbook skill (process: clarify → find sources → query → adversarial review)
- **Reference docs** written for LLM retrieval: table grain/scope/exclusions, gotchas, routing triggers
- **Skill maintenance as first-class citizen**: Co-located in same repo as transforms. ~90% of data-model PRs include skill change
- **Consistent cross-surface experience**: Same skill → same answer in Slack, IDE, dashboard, standalone sessions

### Layer 4: Validation
- **Offline evals**: Dashboard-based (auto-generated + human validated) + Long-tail (Claude generates plausible questions) + Correction harvesting
- **Ablation techniques**: Most useful was negative — raw SQL corpus access moved accuracy <1 point despite 80% of answers being present. Bottleneck was structure, not access
- **Adversarial review**: +6% accuracy, +32% tokens, +72% latency
- **Provenance footer**: Source tier, freshness, owner on every response
- **Active correction harvesting**: Scheduled agent scans for correction language, drafts fixes, opens PRs

## Getting Started (Minimum Viable)
1. A handful of canonical datasets
2. A few dozen offline evals
3. A thin knowledge skill

## Appendix: Skill File Skeleton

The article includes a detailed skill file skeleton with sections:
- Semantic Layer (REQUIRED first step)
- Part 1: MUST KNOW (Business Context, Entity Disambiguation, Data Integrity)
- Part 2: HOW TO DO (Technical Execution, Analysis Best Practices, Adversarial SQL Review)
- Part 3: DATA REFERENCES & RESOURCES (Knowledge Base Navigation, Troubleshooting)

## Significance

This is Anthropic's first public documentation of how they use Claude Code internally for data analytics at scale. It establishes a third major pattern for AI data analysis agents alongside OpenAI's internal agent and Cognition's DANA.
