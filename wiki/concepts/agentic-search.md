---
title: Agentic Search
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [search, ai-agents, finance]
sources: [raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md]
---

# Agentic Search

> Agentic search combines SQL-based skill discovery with grep-like full-text search to load only relevant agent capabilities based on context.

## Definition

**Agentic Search** is a hybrid retrieval pattern for AI agents that avoids loading all skills/tools upfront. Instead, it:

1. **SQL Discovery**: Queries a structured skills database to find relevant capabilities based on the user's current context
2. **Agentic Grep/SQL Hybrid**: For unstructured content (e.g., SEC filings), performs targeted text search only when needed
3. **Lazy Loading**: Only injects relevant skills into the agent's context, avoiding token waste

## Key Design Principles

- **Context-Aware Retrieval**: Skills are loaded based on analysis of what the user is working on, not statically
- **Token Efficiency**: In financial domains where skills documents can be massive, loading everything upfront wastes context window
- **Hybrid Structured/Unstructured Search**: Combines SQL (for structured skill metadata) with full-text search (for document content)

## Use Case: SEC Filing Analysis

Fintool's agents need to answer questions about SEC filings (10-K, 10-Q, proxy statements). Instead of loading all 50+ analytical skills into context:

```
User asks: "What's the company's R&D spend trend?"
→ SQL query finds skills related to "financial metrics", "trend analysis"
→ Only those skills are loaded into context
→ Agent executes with focused capability set
```

## Related Concepts

- [[concepts/markdown-based-skills]] — Skills format used by agentic search
- [[concepts/s3-first-architecture]] — Where skills files are stored
- [[concepts/agent-harness]] — Agentic search is part of the harness layer
