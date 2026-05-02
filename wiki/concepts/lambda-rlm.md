---
title: "Lambda-RLM"
created: 2026-05-02
updated: 2026-05-02
type: concept
tags:
  - concept
  - rlm
  - harness-engineering
  - aec
  - agent-architecture
aliases:
  - Lambda Recursive Language Model
  - Lambda RLM
  - deterministic RLM pipeline
related:
  - [[concepts/rlm-recursive-language-models]]
  - [[concepts/recursive-language-models]]
  - [[concepts/harness-engineering]]
  - [[entities/theodoros-galanos]]
  - [[entities/the-harness-blog]]
sources:
  - https://theharness.blog/blog/recursive-by-design/
  - raw/articles/2026-05-02_the-harness-blog_recursive-by-design.md
---

# Lambda-RLM

**Lambda-RLM** is a deterministic pipeline architecture for Recursive Language Models, introduced by [[entities/theodoros-galanos|Theodoros Galanos]] in his blog post "Recursive by Design" (April 2026). Instead of letting the model decide how to decompose work in an open-ended REPL, Lambda-RLM computes the task structure upfront as a dependency tree — the "task is the plan" approach.

## Overview

Lambda-RLM is the third stage in an architectural evolution for engineering agent report generation, moving from an open-ended REPL (Stage 1) through context compaction (Stage 2) to a deterministic pipeline (Stage 3). It achieved **14x fewer tokens, 22x fewer input tokens, and +8.4% quality improvement** over the open REPL baseline.

Core insight: When task structure is deterministic and bounded, giving the model freedom to decide decomposition strategy wastes tokens on control code and planning rather than engineering reasoning.

## Architecture

Lambda-RLM replaces model-driven decomposition with a three-phase deterministic pipeline:

### Phase 1: Plan (0 LLM calls)
- Reads the template structure
- Measures source document sizes
- Computes a dependency tree of sections
- **No LLM calls** — pure algorithmic computation

### Phase 2: Extract + Review
- Pulls data from bounded chunks in dependency order
- Contract alignment check: compares extracted data against template requirements
- Flags gaps for re-extraction
- Uses `SUBCALL_LOG` so later extractions see what earlier ones found

### Phase 3: Generate
- Composes sections from extractions and dependencies
- Cross-section consistency checks (e.g., "Security" specs don't contradict "Electrical" specs)
- Discipline routing: routes specific sections to relevant discipline summaries

## Key Performance Metrics

| Metric | Open REPL | Lambda-RLM | Improvement |
|--------|-----------|------------|-------------|
| **Total Tokens** | 740K | 53K | **14x less** |
| **Input Tokens** | 732K | 33K | **22x less** |
| **API Calls** | 48 | 27 | **1.8x fewer** |
| **Cost Predictability** | Unknown | Exact Match | **Deterministic** |
| **Quality (Reward)** | 0.67 | 0.73 | **+8.4%** |

## Comparison with Standard RLM

| Aspect | Standard RLM | Lambda-RLM |
|--------|-------------|------------|
| **Decomposition** | Model decides (dynamic, open-ended) | Template-driven (deterministic, upfront) |
| **REPL usage** | Open-ended, full Python REPL | Bounded pipeline phases |
| **Context management** | Model writes code to slice/transform | Pre-computed dependency tree |
| **Coding tax** | High — model writes control code | Near zero — pipeline is pre-defined |
| **Best for** | Unbounded, exploratory tasks | Bounded, structure-known tasks |
| **Token efficiency** | Moderate | Extreme (14x) |

## Design Principles for Agent Consumers

Galanos derived several practitioner insights from the Lambda-RLM development:

- **Guessable APIs** — Agents hallucinate method names; use `__getattr__` with suggestion mappings (e.g., "Did you mean `CONTEXT(id)`?")
- **Internal Documentation** — Use a `HELP()` function inside the environment with return type annotations
- **Durable Memory** — Use scratchpad JSON that survives context compaction cycles
- **Visibility** — Maintain a `SUBCALL_LOG` so later LLM calls see prior extractions without re-processing
- **Parallelization** — Separate I/O-bound work (LLM calls) from state mutation (template filling)

## The Expert Feedback Loop

A key finding from Lambda-RLM development: technical benchmarks alone are insufficient. Domain experts reviewing the output identified:
- Terminology confusion ("fee proposals" vs "scope of works")
- Missing mandatory subsections
- Cross-section consistency violations
- Need for discipline routing (section-specific vs whole-document context)

This validates the [[concepts/harness-engineering]] principle that the highest-ROI activity is human-led error analysis of traces.

## Relationship to Other Concepts

- [[concepts/rlm-recursive-language-models]] — The general RLM framework; Lambda-RLM is a specific architectural variant
- [[concepts/recursive-language-models]] — Simpler RLM concept page
- [[concepts/harness-engineering]] — Broader framework; Lambda-RLM is a concrete implementation of harness-first agent design
- [[concepts/agent-architecture-decomposition]] — Three-layer framework; Lambda-RLM sits at the harness layer
- [[entities/theodoros-galanos]] — Creator and author
- [[entities/the-harness-blog]] — Publication venue

## Graph Structure Query

```
[lambda-rlm] ──author──→ [entity: theodoros-galanos]
[lambda-rlm] ──extends──→ [concept: rlm-recursive-language-models]
[lambda-rlm] ──contrasts──→ [concept: agent-architecture-decomposition] (open REPL variant)
[lambda-rlm] ──embodies──→ [concept: harness-engineering]
[lambda-rlm] ──teaches──→ [concept: agent-evaluation]
```

This concept was authored by [[entities/theodoros-galanos]], extends the general [[concepts/rlm-recursive-language-models|RLM framework]], contrasts with open-ended REPL architectures, and embodies the [[concepts/harness-engineering]] principle that agent reasoning architecture is itself a harness design choice.

## Sources

- ["Recursive by Design"](https://theharness.blog/blog/recursive-by-design/) — Theodoros Galanos, The Harness Blog (April 4, 2026)
