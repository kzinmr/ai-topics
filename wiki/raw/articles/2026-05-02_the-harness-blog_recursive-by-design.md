# Recursive by Design: Building Engineering Agents

**Source:** <https://theharness.blog/blog/recursive-by-design/>
**Author:** Theodoros Galanos
**Date:** 2026-05-02 (scraped)
**Archive:** raw/articles/2026-05-02_the-harness-blog_recursive-by-design.md

---
## Summary

The article argues that **agent reasoning architecture is itself a harness design choice** — not separate from it. The author describes three stages of evolution: from an open-ended REPL (high variance, 740K tokens), through context compaction (cost reduction but not root cause), to **Lambda-RLM** (deterministic pipeline, 53K tokens, 14x less, +8.4% quality).

Key thesis: "The agent's reasoning architecture is itself a harness design choice. Agent design and harness design are the same problem."

## Core Concepts

### Recursive Language Model (RLM)
- Context is a variable in the REPL, not tokens in the window
- State persists across turns; variables act as memory
- Code can invoke LLMs inside loops, enabling O(n) or O(n^2) work over large inputs

### Lambda-RLM Architecture (Three-Stage Pipeline)
1. **Plan** — Reads template, measures sources, computes decomposition (0 LLM calls)
2. **Extract + Review** — Pulls data from bounded chunks in dependency order; contract alignment check
3. **Generate** — Composes sections from extractions and dependencies

### Key Metrics
| Metric | Open REPL | Lambda-RLM | Improvement |
|--------|-----------|------------|-------------|
| Total Tokens | 740K | 53K | **14x less** |
| Input Tokens | 732K | 33K | **22x less** |
| API Calls | 48 | 27 | **1.8x fewer** |
| Quality (Reward) | 0.67 | 0.73 | **+8.4%** |

## Practitioner Lessons
- **Guessable APIs** — Use `__getattr__` with suggestion mappings for LLM consumers
- **Durable Memory** — Scratchpad JSON survives context compaction
- **Visibility** — `SUBCALL_LOG` so later calls see prior extractions
- **Expert Feedback Loop** — Domain experts fixed terminology, missing sections, cross-section consistency

## Related
- [[concepts/harness-engineering]]
- [[concepts/recursive-language-model]]
- [[entities/theodoros-galanos]]
- [[entities/the-harness-blog]]
- `aec-bench` — Benchmarking tool for agent architectures

## Sources
- <https://theharness.blog/blog/recursive-by-design/>
