---
title: Josh Barrow
type: entity
created: 2026-06-15
updated: 2026-06-15
tags:
  - person
  - search
aliases:
  - jbarrow
  - jbarrowai
  - Josh Barrow
sources:
  - https://jbarrow.ai/
  - https://jbarrow.ai/field_notes/obliq-bench/
  - raw/articles/2026-06-12_jbarrow_searching-fast-and-slow.md
---

# Josh Barrow (@jbarrowai)

**Josh Barrow** is an AI researcher and writer focused on information retrieval, search system design, and the intersection of IR with agentic systems. He maintains a personal site at [jbarrow.ai](https://jbarrow.ai/) with field notes on search research.

## Overview

Barrow is known for his practical analysis of search architecture and retrieval paradigms. In June 2026, he published "Searching, Fast and Slow" — revisiting the 2013 Slow Search paper through the lens of agentic retrieval.

## Key Contributions

### "Searching, Fast and Slow" (June 2026)

Barrow analyzed the competing philosophies in agentic retrieval:
- **Latency doesn't matter** — agents are patient; per-query latency is irrelevant
- **Agents are more sensitive to latency** — agents issue more queries, so throughput matters

He resolved this tension by distinguishing per-query latency from whole-task throughput. His key argument: the IR community should do **more slow search research** because agents are "the perfect slow searchers" — infinitely patient and cheaper to run if given better results.

### Obliq-Bench

Created [Obliq-Bench](https://jbarrow.ai/field_notes/obliq-bench/), a benchmark for evaluating oblique/indirect query resolution — the kind of search that agents perform when working through multi-step reasoning problems.

## Related Concepts

- [[concepts/slow-search]] — Barrow's primary thesis area
- [[concepts/agentic-retrieval]] — Context for his analysis
- [[concepts/hornet]] — Referenced in his discussion of throughput-focused retrieval

## Sources

- [jbarrow.ai](https://jbarrow.ai/) — Personal site
- [Obliq-Bench](https://jbarrow.ai/field_notes/obliq-bench/) — Field notes
- [[raw/articles/2026-06-12_jbarrow_searching-fast-and-slow]] — "Searching, Fast and Slow" article
