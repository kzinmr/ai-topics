# Inside OpenAI's In-House Data Agent

**Source:** https://openai.com/index/inside-our-in-house-data-agent/
**Authors:** Bonnie Xu, Aravind Suresh, Emma Tang
**Date:** 2026-01-29
**Tags:** openai, data-agent, gpt-5.2, data-analysis, internal-tool

---

## Summary

OpenAI built a bespoke, internal-only AI data agent to explore and reason over their massive data platform (600+ petabytes, 70k+ datasets). Powered by GPT-5.2, it uses the same tools available to external developers: Codex, Evals API, and Embeddings API.

## Key Challenges

- **Discovery Fatigue:** Finding the right table among 70k+ datasets
- **Semantic Ambiguity:** Overlapping fields with different inclusion criteria
- **Technical Complexity:** 180+ line SQL prone to M:N joins, filter pushdown errors
- **Scale:** 3,500+ internal users, 600+ PB data platform

## Architecture: Six Layers of Context

1. **Table Usage:** Metadata (schemas) + lineage (upstream/downstream)
2. **Human Annotations:** Curated descriptions from domain experts
3. **Codex Enrichment:** Derives code-level definitions from Spark/Python pipelines
4. **Institutional Knowledge:** Slack, Google Docs, Notion ingestion
5. **Memory:** Saves corrections and non-obvious constraints
6. **Runtime Context:** Live queries to validate schemas in real-time

## Operational Principles

- **Closed-Loop Reasoning:** Self-evaluates progress, retries on errors
- **Multi-Interface Access:** Slack, web UI, IDEs, Codex CLI (via MCP), ChatGPT
- **Teammate Model:** Iterative exploration, not one-shot answers
- **Pass-Through Security:** Inherits user's existing permissions

## Key Lessons

1. **Less is More:** Too many redundant tools confused the agent
2. **Guide the Goal, Not the Path:** Highly prescriptive prompting degraded results
3. **Meaning Lives in Code:** Pipeline logic captures assumptions and business intent not found in SQL or metadata

## Evaluation

Uses the Evals API with "golden" SQL query pairs — compares both SQL and resulting data, not naive string matching.

## Related

- [[concepts/data-analysis-agents]] — Umbrella concept for AI data analysis agents
- [[concepts/poor-mans-continuous-learning]] — Knowledge-based continuous improvement (golden queries, memory layers)
