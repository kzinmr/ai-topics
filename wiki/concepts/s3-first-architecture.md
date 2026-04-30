---
title: S3-First Architecture
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [architecture, ai-agents, infrastructure]
sources: [raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md]
---

# S3-First Architecture

## Definition

**S3-First Architecture** is a data persistence pattern where object storage (Amazon S3 or compatible) serves as the **primary source of truth** for application state, rather than a traditional database. Databases are used secondarily — for indexing, listing, or search — while S3 holds the authoritative, versioned records.

## How It Works (Fintool Pattern)

1. **Write path:** Data is written to S3 as human-readable files (YAML, Markdown, JSON)
2. **Trigger:** S3 events fire Lambda functions that sync changes to PostgreSQL
3. **Read path:** Listing operations hit the database; single-item fresh reads go directly to S3
4. **Isolation:** Attribute-based access control (ABAC) with IAM policies (`${aws:PrincipalTag/S3Prefix}`) ensures tenant isolation

## Key Benefits

| Benefit | Description |
|---------|-------------|
| **Durability** | S3 provides 11 nines (99.999999999%) of data durability |
| **Free versioning** | S3 versioning provides automatic audit trails at no extra cost |
| **Human-readable** | Files are YAML/Markdown, making debugging trivial |
| **Auditability** | Every change is a versioned object with timestamp |
| **Tenant isolation** | IAM policies enforce per-user access boundaries |

## When to Use

- AI agents need persistent, versioned state (watchlists, memories, [[markdown-based-skills]])
- Multi-tenant systems where data isolation is critical
- Workflows where human readability and debugging matter
- Situations where the cost of a database exceeds the value of the data

## Related Concepts

- [[background-coding-agent]] — uses Modal snapshots for similar persistence goals
- [[modal-sandboxes]] — cloud execution environments that pair well with S3-first storage
- [[markdown-based-skills]] — skills stored as .md files in S3

## Sources

- Nicolas Bustamante (Fintool), "Lessons from Building AI Agents for Financial Services", LinkedIn, April 2026
