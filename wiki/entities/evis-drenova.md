---
title: Evis Drenova
type: entity
created: 2026-05-08
updated: 2026-05-08
status: L2
tags:
  - person
  - coding-agents
  - search
  - infrastructure
  - benchmark
sources:
  - "raw/articles/2026-05-06_entire-improving-agentic-search-in-coding-agents]]"
aliases: ['@evisdrenova']
---


# Evis Drenova

Evis Drenova is a software engineer and researcher at [Entire](https://entire.io), focusing on AI agent observability and agentic code search infrastructure.

## Notable Work

### Agentic Code Search Study (May 2026)

Authored "How We Improved Agentic Search," a public benchmark study that analyzed 1,983 real coding-agent checkpoints to understand how agents search codebases. Key contributions:

- **Quantified agent search behavior**: Showed 48.8% of all coding-agent tool calls are search-related (file reads, grep, bash fallback)
- **Disproved the "faster search = better agents" hypothesis**: Demonstrated that even a 9× search speedup (fff: 14.7ms → 1.7ms) only improved end-to-end runtime by 1.6%, because tool execution represents <1% of total agent wall clock
- **Built pgr**: An open-source Rust MCP search tool that prioritizes definitions-first, path-aware ranking — improving first-query Hit@1 from 26% to 34% (implementation prompts: 14.3% → 42.9%)
- **Developed benchmark methodology**: Three-layer benchmark stack (speed, broad mixed-workload, offline retrieval) for evaluating search interventions in agent loops

## Affiliation

- Entire (entire.io) — AI agent observability infrastructure
- GitHub: [entireio/pgr](https://github.com/entireio/pgr), [entireio/cli](https://github.com/entireio/cli)

## See Also

- [[entities/entire]] — Company
- [[concepts/pgr]] — The agentic search tool
