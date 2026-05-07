# AI Data Analysis Agents

> **AI agents designed for data exploration, querying, and analysis — bridging natural language questions to data-driven insights.**

Data analysis agents represent a distinct category of AI agent, optimized for the data analysis workflow: data discovery → schema understanding → query generation → execution → verification → visualization → reporting. Unlike general-purpose coding agents, they emphasize **data lineage understanding**, **semantic grounding**, and **verifiable outputs**.

## The Core Challenge

Data analysis agents face unique challenges compared to general coding agents:

1. **Discovery at Scale**: Finding the right table among thousands or tens of thousands of datasets
2. **Semantic Ambiguity**: Same column names may mean different things in different contexts (logged-in vs logged-out users)
3. **Tribal Knowledge**: Business logic encoded in pipeline code, not in SQL metadata
4. **Verification**: Queries that run successfully can still return semantically wrong results
5. **Multi-step Reasoning**: Data questions often require chaining queries (explore → pattern → question → refine)

## Two Major Approaches

Two dominant patterns have emerged in 2025-2026:

### Approach A: Internal Bespoke Agent (OpenAI Pattern)

OpenAI built an internal data agent for their 600+ PB, 70k+ dataset platform, powered by GPT-5.2. The key insight: **data meaning lives in pipeline code, not in SQL metadata**.

**Six layers of grounding context:**
1. **Table Usage** — schema metadata + lineage
2. **Human Annotations** — domain expert descriptions
3. **Codex Enrichment** — code-level definitions from Spark/Python pipelines
4. **Institutional Knowledge** — Slack, G Docs, Notion ingestion
5. **Memory** — persistent corrections and constraints
6. **Runtime Context** — live schema validation queries

**Operational philosophy:** "The Teammate Model" — iterative exploration with proactive clarification, not one-shot answers.

### Approach B: Software Engineer as Data Analyst (Cognition/Devin Pattern)

Cognition's philosophy is that **an AI software engineer makes a better data analyst than a SQL-only tool**, because it understands the full data lineage (code → ETL → warehouse → dashboard).

**Key differentiator:** Devin can search product code to see how a column is computed or how an event is instrumented — bridging the gap between codebase logic and database results.

**DANA (Data Analyst Agent):** A specialized Devin persona activated via `/dana` or `@Devin !dana` in Slack, equipped with MCP database connectors (Redshift, Snowflake, BigQuery) and Knowledge configurations.

## Common Architectural Patterns

Despite different implementations, successful data analysis agents share:

### 1. Multi-Layer Context Grounding
Both OpenAI and Cognition use layered context retrieval, mirroring how a human analyst works:
- **Schema layer**: Table names, columns, types, relationships
- **Code layer**: How data is computed/transformed in pipelines
- **Business layer**: Metric definitions, tribal knowledge, naming conventions
- **Memory layer**: Corrections and learnings from past sessions

### 2. Knowledge Base / Memory
- **OpenAI**: Saves corrections and non-obvious constraints to improve future baseline performance
- **Cognition**: Uses Knowledge configurations with macros (`!analytics`) for team-wide shared context
- **BQ Golden Queries**: Curated exemplar queries as semantic grounding
- See [[concepts/poor-mans-continuous-learning]] for the unifying pattern

### 3. Verification Loop
Both systems emphasize verifiable outputs:
- OpenAI: Exposes reasoning process, links to raw data
- Cognition: Forces output format to include final query + Metabase playground link
- The agent isn't trusted — only the **verifiable evidence it produces** is trusted

### 4. MCP / Protocol-Based Tool Access
Both use standardized protocols for database connectivity:
- OpenAI: Codex MCP integration
- Cognition: MCP Marketplace with Google's MCP Toolbox for Databases + open-source Metabase MCP

## Comparison: Key Systems

| Aspect | OpenAI Internal Agent | Cognition DANA / Devin |
|--------|---------------------|----------------------|
| **Model** | GPT-5.2 | Multiple models (via Devin harness) |
| **Data Scale** | 600+ PB, 70k+ datasets | Enterprise DW (Redshift/Snowflake/BQ) |
| **Code Awareness** | Codex pipeline code crawling | Full codebase search + git history |
| **Knowledge Capture** | Memory + institutional ingestion | Knowledge configs + macros |
| **Verification** | Evals API golden SQL pairs | Final SQL + Metabase playground link |
| **Interfaces** | Slack, Web, IDE, Codex CLI, ChatGPT | Slack, Web, CLI, API, Linear |
| **Approach** | Bespoke internal tool | Productized agent with MCP |
| **Key Insight** | "Meaning lives in code" | "Software Engineer > SQL Tool" |

## Relationship to DWH Semantic Layers

Data analysis agents sit **one abstraction level above** the semantic layer approaches discussed in [[concepts/poor-mans-continuous-learning]]:

```
Semantic Layer (dbt, BQ Graph)  →  "What queries are valid?"
Golden Queries (BQ)              →  "What queries have worked before?"
Data Analysis Agents             →  "What question is the user really asking?"
```

The agent uses the semantic layer and golden queries as tools/context — it doesn't replace them. OpenAI's "six layers" explicitly include schema metadata and golden patterns. Cognition's Knowledge configurations recommend preferring "mart" models (semantic layer outputs) over raw staging tables.

## End-to-End: From Data Question to Code Fix

The most advanced capability demonstrated is the fusion of data analysis with **engineering debugging** (Cognition's end-to-end bug triage):

```
1. "Why did signups drop Tuesday?" (data question)
   → DANA queries warehouse, identifies anomaly
2. Which commit caused the regression? (engineering question)
   → Devin searches git history, traces to breaking change
3. Fix it and add a test (code question)
   → Devin writes fix, creates PR with regression test
```

This eliminates the traditional handoff between data teams and engineering teams — a single agent traces the full path from data anomaly to code root cause to fix.

## Related Wiki Pages

- [[concepts/cognition-ai-data-analyst]] — Detailed Cognition/Devin data analyst architecture
- [[concepts/poor-mans-continuous-learning]] — Knowledge-based continuous improvement pattern
- [[concepts/closing-agent-loop]] — Write→Catch→Fix→Merge cycle (data analysis variant)
- [[concepts/mcp]] — Model Context Protocol (tool access standardization)
- [[entities/ashpreet-bedi]] — Dash self-learning data agent, PMCL originator
- [[raw/articles/2026-01-29_openai-in-house-data-agent]] — OpenAI in-house data agent article
