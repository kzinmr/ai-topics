# Datasette Agent
**Source**: https://datasette.io/blog/2026/datasette-agent/
**Author**: Simon Willison
**Date**: 2026-06-12
**Saved**: 2026-06-16

---

I've been experimenting with AI-powered interfaces to Datasette for a while now, and today I'm releasing **Datasette Agent** — a plugin that gives Datasette a conversational AI assistant capable of exploring and analyzing your data using natural language.

## The core idea

Datasette has always been about making data *explorable*. You can browse tables, run SQL queries, and drill into individual records. But there's a gap between "I have a question about this data" and "I know the right SQL to answer it." Datasette Agent bridges that gap.

You type a question in plain English — "Which users signed up last month?" or "What's the average response time by endpoint?" — and the agent translates it into SQL, runs it against your database, and presents the results in a conversational format.

## How it works

Under the hood, Datasette Agent uses a combination of techniques:

1. **Schema introspection:** When you ask a question, the agent first examines the database schema — table names, column types, foreign keys, indexes — to understand what data is available.
2. **LLM-powered SQL generation:** The schema context and your question are sent to a language model (supporting OpenAI, Anthropic, and local models via Ollama) which generates a candidate SQL query.
3. **Sandboxed execution:** The generated SQL is executed in a read-only transaction with configurable query timeout and row limits. The agent never writes to the database.
4. **Iterative refinement:** If the query fails or returns unexpected results, the agent can attempt to fix the query and try again, up to a configurable number of retries.
5. **Result interpretation:** The raw results are passed back to the LLM, which generates a natural language summary with the key findings.

## Key features

This first release includes:

- **Chat interface** — a new `/agent` page in Datasette that provides a chat UI for asking questions about your data.
- **API endpoint** — a `POST /-/agent/ask` JSON API for programmatic access.
- **Query history** — every generated SQL query and its results are logged to a `_agent_queries` table, so you can audit what the agent did.
- **Multi-model support** — configure any OpenAI-compatible API, Anthropic Claude, or a local Ollama instance.
- **Safety guardrails** — read-only execution, row limits, query timeouts, and an optional approval step where the agent shows you the SQL before running it.
- **DuckDB support** — works with both SQLite databases (Datasette's native format) and attached DuckDB databases via the `datasette-duckdb` plugin.

## Installation

```
pip install datasette-agent
datasette mydb.db --install datasette-agent
```

Then set your LLM API key as an environment variable:

```
export OPENAI_API_KEY=sk-...
# or
export ANTHROPIC_API_KEY=sk-ant-...
```

Navigate to `/agent` on your Datasette instance and start asking questions.

## Why now?

Language models have gotten good enough — and cheap enough — that this kind of tool is genuinely useful rather than a demo. The latest generation of models can reliably generate correct SQL for complex queries, including joins, aggregations, window functions, and CTEs. The cost per query is fractions of a cent.

I also think there's something powerful about combining a **structured data exploration tool** with a **conversational interface**. Datasette gives you the browseable tables, the faceting, the filtering, the visualizations. The agent gives you a fast way to ask and answer questions without needing to write SQL yourself. They complement each other.

## Future plans

- **Visualization suggestions** — when the agent returns results, suggest appropriate chart types and generate inline visualizations.
- **Follow-up context** — maintain conversation context so you can ask follow-up questions like "now break that down by region."
- **Custom instructions** — let database administrators provide domain-specific context (what columns mean, data quality notes, business logic) that the agent can use.
- **Collaborative exploration** — share agent conversations with teammates so they can see the path of analysis.

## Try it out

Datasette Agent is open source (Apache 2.0) and available on PyPI today. The code is at [github.com/simonw/datasette-agent](https://github.com/simonw/datasette-agent).
