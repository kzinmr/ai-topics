---
title: datasette-llm-limits
type: entity
created: 2026-05-16
updated: 2026-05-16
tags:
  - tool
  - model
  - optimization
sources:
  - raw/articles/simonwillison.net--2026-may-15-datasette-llm-limits--c4c541c4.md
---

# datasette-llm-limits

**datasette-llm-limits** is a Datasette plugin released in May 2026 that provides **spending controls** for the [datasette-llm](https://datasette.io/plugins/datasette-llm) LLM interaction plugin.

## Overview

The plugin enables Datasette administrators to set **token and cost limits** on LLM API usage through their Datasette instance. This addresses the concern that when LLM access is exposed via a web interface, users may run expensive queries without realizing the cost implications.

## Features

- **Token limits**: Cap the maximum number of tokens per request
- **Cost tracking**: Monitor spending across LLM API calls
- **Budget controls**: Prevent runaway API usage from expensive queries
- **Admin controls**: Datasette instance owners configure limits globally

## Context

This plugin is part of Simon Willison's broader **datasette-llm** ecosystem:
- [datasette-llm](https://datasette.io/plugins/datasette-llm) — LLM integration for Datasette (query your data with natural language)
- [datasette-llm-limits](https://datasette.io/plugins/datasette-llm-limits) — Spending controls for the above
- Both plugins are open-source and available on [PyPI](https://pypi.org/project/datasette-llm-limits/)

## Related

- [[entities/simon-willison]] — Creator of Datasette and datasette-llm plugins
- [[entities/datasette]] — SQLite-powered data exploration tool
- [[concepts/llm-cost-management]] — Managing token and API costs in LLM applications
