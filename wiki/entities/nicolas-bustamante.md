---
title: Nicolas Bustamante
created: 2026-04-30
updated: 2026-04-30
type: entity
tags: [person, ai-agents, financial-services]
sources: [raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md]
---

# Nicolas Bustamante

## Overview

**Nicolas Bustamante** is a technical leader at [[entities/fintool]] who has shared detailed architectural insights on building production AI agents for financial services. His LinkedIn article (April 2026) is one of the most comprehensive public accounts of AI agent infrastructure in a regulated, high-precision domain.

## Key Contributions

### AI Agent Architecture in Financial Services

Bustamante articulated several foundational patterns:

1. **S3-First Architecture**: Using object storage as the primary data source, with databases as secondary indexes
2. **Markdown-Based Skills**: Allowing non-engineers to encode financial methodologies as `.md` files
3. **Pre-Warmed Sandboxes**: Eliminating latency by warming up execution environments proactively
4. **AskUserQuestion Tool**: Agent-initiated human clarification for high-stakes decisions
5. **"The Model Will Eat Your Scaffolding"**: Designing for model obsolescence as capabilities improve

### Moat Philosophy

> "Your moat is not the model. Your moat is everything you build around it — financial data, domain-specific skills, reliable infrastructure, and trust."

This perspective positions infrastructure and data quality as the real competitive advantage, not the underlying LLM.

## Technical Stack (as described by Bustamante)

- AWS (S3, Lambda, ABAC)
- PostgreSQL (secondary index)
- Temporal (durable execution)
- Redis Streams (real-time updates)
- Braintrust (evaluation framework)
- Claude (Sonnet for complex tasks, Haiku for simple queries)

## Related Entities

- [[entities/fintool]] — Company where Bustamante works
- [[concepts/s3-first-architecture]] — Architecture pattern he pioneered
- [[concepts/markdown-based-skills]] — Skill system he designed

## Sources

- Nicolas Bustamante, "Lessons from Building AI Agents for Financial Services", LinkedIn, April 2026
