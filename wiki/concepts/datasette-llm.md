---
title: "datasette-llm"
type: concept
created: 2026-05-06
updated: 2026-05-06
status: L1
tags:
  - llm-tools
  - datasette
  - data-analysis
  - simon-willison
sources:
  - https://simonwillison.net/2026/May/5/datasette-llm/
---

# datasette-llm 0.1a7

**datasette-llm** is a Datasette plugin by [[entities/simon-willison]] (released May 5, 2026, v0.1a7) that enables natural language querying of SQLite databases through LLM APIs directly within Datasette's web interface.

## Core Features

- **Natural language to SQL translation**: Users can type queries in plain English and get SQL results back
- **Integrated into Datasette UI**: Works as a first-class Datasette plugin, appearing alongside existing query interfaces
- **Multi-provider support**: Works with any LLM provider supported by Simon's [[entities/llm]] CLI tool
- **Alpha stage**: Currently at v0.1a7, indicating active development and API instability

## Architecture

The plugin integrates with Datasette's existing plugin system and uses the LLM library's provider abstraction layer. It sits between Datasette's web UI and the LLM API, translating natural language prompts into SQL queries and displaying results.

## Significance

This represents the continuing convergence of **data tools and LLM interfaces**. Simon Willison's ecosystem (Datasette + LLM CLI + plugins) is becoming a full-stack toolkit for AI-assisted data exploration. The pattern — small, composable plugins that add AI capabilities to existing data infrastructure — mirrors the broader "agentic tooling" trend where LLMs augment rather than replace existing workflows.

## Related

- [[entities/datasette]] — Core data exploration platform
- [[entities/llm]] — CLI tool for LLM access (provides provider abstraction)
- [[entities/simon-willison]] — Creator
- [[concepts/agentic-engineering]] — AI-assisted software development patterns

## Sources

- [datasette-llm 0.1a7 release notes](https://simonwillison.net/2026/May/5/datasette-llm/)
- [Datasette project](https://datasette.io/)

## References

- simonwillison.net--2026-may-5-datasette-llm--9b418a5a
