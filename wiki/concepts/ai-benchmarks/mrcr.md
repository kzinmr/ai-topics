---
title: "MRCR (Multi-Round Coreference Resolution)"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - long-context
  - reasoning
aliases:
  - mrcr
  - multi-round-coreference-resolution
status: active
sources:
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related:
  - "[[concepts/ai-benchmarks-and-evals]]"
  - "[[concepts/context-engineering]]"
---

# MRCR (Multi-Round Coreference Resolution)

> **Part 6 of @xeophon's 18-part AI Benchmarks & Evals series.** A long-context evaluation benchmark that improves on the Needle-in-a-Haystack (NIAH) pattern by using multiple needles and requiring coreference resolution across conversation rounds.

## Overview

MRCR (Multi-Round Coreference Resolution) tests how well LLMs can retrieve and reason over information distributed across long contexts. It advances beyond the popular Needle-in-a-Haystack (NIAH) test by introducing **multiple retrieval targets** and **coreference resolution** — requiring models to not just find a single fact but to track entities and relationships across extended conversations.

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Long-context information retrieval and reasoning |
| **Task type** | Multi-needle retrieval with coreference resolution |
| **Key innovation** | Multiple needles (vs single needle in NIAH) |
| **Context length** | Tests across various context lengths (8K–128K+ tokens) |
| **Evaluation** | Accuracy of retrieved/reasoned answers |

## How It Improves on NIAH

| Dimension | Needle-in-a-Haystack (NIAH) | MRCR |
|-----------|---------------------------|------|
| **Needles** | Single fact hidden in context | Multiple facts/entities |
| **Task** | Find and retrieve one piece of information | Track entities across rounds, resolve coreferences |
| **Difficulty** | Simple retrieval | Multi-step retrieval + reasoning |
| **Real-world fidelity** | Low (single-needle is artificial) | Higher (multi-entity tracking mirrors real use) |

## @xeophon's Key Insight

> "Multiple needles. Improvements over NIAH." — @xeophon, Part 6

Xeophon highlights MRCR as a more realistic alternative to NIAH-style tests. While NIAH became popular for its visual heatmaps, it tests only the simplest possible retrieval scenario. MRCR's multi-needle design better reflects real-world long-context use cases (multi-document analysis, long conversation tracking, etc.).

## Strengths

- **More realistic than NIAH**: Multi-needle design reflects actual long-context usage patterns
- **Coreference resolution**: Tests entity tracking, not just fact retrieval
- **Scalable difficulty**: Can vary number of needles and context length independently
- **Better discrimination**: Models that "pass" NIAH may still fail MRCR at the same context length

## Weaknesses

- **Less well-known**: Not as widely adopted as NIAH or other mainstream benchmarks
- **Still synthetic**: Generated conversation-like text, not real documents
- **Limited public data**: Less publicly available infrastructure than NIAH

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[concepts/context-engineering]] — Context engineering and management
- [[concepts/hle]] — HLE (expert-level reasoning)

## Sources

1. @xeophon, "AI Benchmarks & Evals Series, Part 6: MRCR," May 6, 2025.
