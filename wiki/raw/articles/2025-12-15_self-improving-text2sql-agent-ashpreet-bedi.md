# Self-Improving Text-to-SQL Agent: Dynamic Context & Continuous Learning

**Source:** https://www.ashpreetbedi.com/sql-agent
**Author:** Ashpreet Bedi
**Date:** 2025-12-15
**Tags:** text-to-sql, continuous-learning, knowledge-base, agent-architecture, sql-agent

---

## Summary

A framework for building a Text-to-SQL agent that uses a "poor man's continuous learning" loop — instead of retraining models, the system improves by updating a structured knowledge base with successful queries and tribal knowledge.

## Key Concepts

### Dynamic Context
The agent retrieves relevant knowledge at query time: table schemas, common join keys, metric definitions, and specific rules (e.g., "Use `TO_DATE` for date filters").

### "Poor Man's Continuous Learning"
A pragmatic learning loop that avoids updating model weights:
> "Every good query becomes future context. Every mistake becomes a rule. Every clarification becomes shared knowledge."

- **Stability:** Keeps online path stable while allowing controlled improvements
- **Transparency:** Knowledge base can be manually audited and corrected

## Architecture

1. **Online Path (Text-to-SQL Agent):** Retrieves context via hybrid search, augments input with rules, generates/validates/executes SQL
2. **Offline Path (Continuous Learning):** Captures successful runs, updates KB with user approval, optional regression harness

## Knowledge Base Design

Three categories:
1. **Table Information:** Schemas, metadata, column rules
2. **Sample Queries:** Common patterns and KPI logic
3. **Business Semantics:** Organizational terminology → database structures

## Tech Stack
- FastAPI, PostgreSQL (sessions, memory, knowledge)
- OpenAI (primary), Anthropic (optional)
- Docker & Railway

## Related
- BigQuery Conversational Analytics "Golden Queries"
- dbt Semantic Layer (ontology-driven approach)
- LPE-SQL (Continual Learning for Text-to-SQL, ICLR 2025)
