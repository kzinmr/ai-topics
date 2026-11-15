---
title: "datasette-llm"
type: concept
created: 2026-05-06
updated: 2026-11-15
status: L1
tags:
  - tool
  - data-science
  - person
sources:
  - https://simonwillison.net/2026/May/5/datasette-llm/
  - raw/articles/simonwillison.net--2026-nov-14-datasette-llm--cbf5757f.md
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

## Release history

- **v0.1a7** (2026-05-05) — initial documented release: natural language → SQL via LLM providers.
- **v0.1a11** (2026-11-14) — adds support for **OpenAI-compatible endpoints**: Datasette can now use any LLM that speaks the OpenAI pseudo-standard web protocol. This unlocks fully local stacks — models served by **LM Studio**, **Ollama**, or **llama.cpp** (which just hit v1.0.0) — via a `plugins.datasette-llm.default_model` setting, e.g. `{"model": "lmstudio-qwen", "model_name": "qwen/qwen3.8-27b", "api_base": "http://localhost:1234/v1"}`, run through `uvx --with datasette-agent datasette ...` to get a Datasette Agent instance powered by a local model.

## Related

- [[entities/datasette]] — Core data exploration platform
- [[entities/llm]] — CLI tool for LLM access (provides provider abstraction)
- [[entities/simon-willison]] — Creator
- [[concepts/agentic-engineering]] — AI-assisted software development patterns

## Sources

- [datasette-llm 0.1a7 release notes](https://simonwillison.net/2026/May/5/datasette-llm/)
- [datasette-llm 0.1a11 — OpenAI-compatible endpoints](https://simonwillison.net/2026/Nov/14/datasette-llm/) (2026-11-14)
- [Datasette project](https://datasette.io/)

## References

- simonwillison.net--2026-may-5-datasette-llm--9b418a5a
- simonwillison.net--2026-nov-14-datasette-llm--cbf5757f
