---
title: Fintool
created: 2026-04-30
updated: 2026-04-30
type: entity
tags: [company, ai-agents, financial-services]
sources: [raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md]
---

# Fintool

## Overview

**Fintool** is a financial services company that has built production AI agents for high-precision financial analysis tasks, including DCF valuations, SEC filing analysis, and earnings transcript processing. Their architecture emphasizes data quality, domain-specific skills, and reliable infrastructure over model capabilities.

## Key People

- **Nicolas Bustamante** — Primary technical voice on Fintool's AI agent architecture (LinkedIn author of the seminal architecture post, April 2026)

## Architecture

### Infrastructure Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Storage** | S3 (primary) | Human-readable YAML/Markdown files for user data |
| **Database** | PostgreSQL | Indexing and listing (synced from S3 via Lambda) |
| **Compute** | AWS Lambda | Event-driven processing, sandbox execution |
| **Orchestration** | [[durable-execution]] (Temporal) | Long-running task reliability |
| **Access Control** | AWS ABAC | Attribute-based isolation with IAM policies |
| **Real-time** | Redis Streams | Delta updates and streaming |

### Design Principles

1. **S3-First**: Object storage is the source of truth; databases are secondary indexes
2. **Pre-Warmed Sandboxes**: Environments warm up as users type, not after they submit
3. **Tenant Isolation**: `rm -rf /` risk mitigated via per-user isolated environments
4. **Skills as Files**: Non-engineers can update agent behavior via `.md` files
5. **Model Routing**: Simple queries → cheaper models (Haiku); complex valuations → premium models (Sonnet)

## Data Pipeline

```
SEC filings / transcripts / research
  → Normalization layer
    → Markdown (narrative), CSV/Tables (numbers), JSON (metadata)
      → Fiscal calendar mapping (10,000+ companies)
        → Low-confidence filtering (no garbage in)
          → Agent context injection
```

## Key Innovations

- **Fiscal Period Normalization**: Custom calendar for 10,000+ companies to handle varying fiscal year definitions
- **Shadowing Skill System**: `private > shared > public` priority for skill overrides
- **SQL Discovery for Skills**: Lazy-load only relevant skills to save tokens
- **AskUserQuestion Tool**: Agent pauses for human clarification on high-stakes decisions

## Philosophy

> "Your moat is not the model. Your moat is everything you build around it — financial data, domain-specific skills, reliable infrastructure, and trust."

> "The Model Will Eat Your Scaffolding." — Design skills to be easily updated or deleted as models improve.

## Related Entities

- [[entities/nicolas-bustamante]] — Technical leader at Fintool
- [[concepts/s3-first-architecture]] — Core architectural pattern
- [[concepts/markdown-based-skills]] — Skill definition system
- [[concepts/ask-user-question-pattern]] — Human-in-the-loop interaction

## Sources

- Nicolas Bustamante, "Lessons from Building AI Agents for Financial Services", LinkedIn, April 2026
