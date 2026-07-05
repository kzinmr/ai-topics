---
title: "mary"
handle: "@howdymary"
type: entity
created: 2026-05-25
updated: 2026-05-25
tags:
  - person
  - meta-harness
  - ai-agents
  - agent-runtime
  - benchmark-optimization
  - coding-agents
  - open-source
aliases: ["howdymary", "mary"]
sources:
  - https://x.com/howdymary
  - https://github.com/howdymary
  - https://hermesatlas.com/projects/howdymary/hermes-agent-metaharness
  - raw/articles/2026-04-07_howdymary_meta-harness-hermes.md
---

# mary (@howdymary)

| | |
|---|---|
| **X** | [@howdymary](https://x.com/howdymary) — 18.4K followers |
| **GitHub** | [howdymary](https://github.com/howdymary) |
| **Role** | Data @marketmotionxyz |
| **Background** | Previously Galaxy, Brookings, Schwarzman Scholars, Columbia |
| **Known for** | hermes-agent-metaharness, applying Meta-Harness to Hermes Agent |
| **Side projects** | @jobanxiety |

## Overview

mary (@howdymary) is a data scientist/engineer at **marketmotionxyz** who built the first practical implementation of a **Meta-Harness** for the **Hermes Agent** ecosystem. With a background spanning Galaxy (crypto), Brookings Institution, Schwarzman Scholars, and Columbia, she brings a cross-disciplinary perspective to AI agent engineering.

Her open-source project `hermes-agent-metaharness` (78 stars) is a standalone outer-loop optimization framework that applies the Stanford/MIT Meta-Harness concept to Nous Research's Hermes Agent, treating it as an execution backend and searching for optimal harness configurations on verifiable coding benchmarks.

## Core Ideas

### The OS/Brain Architecture Model

mary's key conceptual contribution is a clean framing of agent systems:

> "Hermes is an agent runtime (operating system) around a model (the brain). Meta harnesses are a way to improve the operating system, not the brain itself."

This **OS/Brain separation** has important implications:
- **Don't retrain the model** — improve the runtime code instead
- **Harness = OS layer**: system prompts, tool definitions, context collection/retrieval, completion logic
- **Model = Brain**: the frozen LLM that processes inputs and generates outputs
- **Meta harness = OS optimization**: an outer loop that searches for better OS configurations

### Research-Safe Meta-Harness Design

Her implementation is intentionally conservative and research-oriented:

| Principle | Implementation |
|-----------|---------------|
| **Target verifiable benchmarks** | TBLite, TB2 (not production chat) |
| **Don't rewrite core** | Deterministic wrapper candidates around a seed |
| **Stable execution backend** | Hermes treated as fixed backend, not self-modified |
| **Filesystem as feedback** | Archive parsing, baseline reuse, frontier tracking |
| **Conservative mutations** | Structured, deterministic candidate generation |

### Architecture Pattern: Inner/Outer Loop

```
hermes-agent (inner runtime)          hermes-agent-metaharness (outer loop)
├── candidate protocol                ├── candidate evaluation & comparison
├── TB2/TBLite integration           ├── archive analysis
├── loop hooks                       ├── baseline helpers
├── per-task archive writing         ├── frontier management
                                     └── mutation & search
```

This separation keeps the agent runtime stable while the meta-harness experiments with different harness configurations.

## Key Work

### hermes-agent-metaharness (2026)
- **Stars**: 78 | **License**: MIT | **Language**: Python
- Standalone outer-loop optimization framework for Hermes Agent
- Directly inspired by Stanford/MIT Meta-Harness paper (arXiv 2603.28052)
- Capabilities: TBLite/TB2 benchmark orchestration, archive parsing, paired evaluation, frontier tracking, deterministic wrapper-mutation search

### Other Projects
- **autopredict**: Market trading agents (7 stars)
- **codex-prpprd-devfleet**: Development fleet management
- **peptide-daily**: Bioinformatics project
- **fast-browser**: Browser automation utility
- **shenzhen**: Hardware/embedded project
- Contributions to: browser-use, Open-Higgsfield-AI, paper2code

## GitHub Repositories

| Repository | Stars | Description |
|-----------|-------|-------------|
| [hermes-agent-metaharness](https://github.com/howdymary/hermes-agent-metaharness) | 78 | Meta-Harness for Hermes Agent |
| [autopredict](https://github.com/howdymary/autopredict) | 7 | Market trading agents |
| [fast-browser](https://github.com/howdymary/fast-browser) | — | Browser automation |
| [peptide-daily](https://github.com/howdymary/peptide-daily) | — | Bioinformatics |

## X Activity Themes

- AI agent engineering and benchmark optimization
- Hermes Agent ecosystem and tooling
- Meta-harness patterns and practical implementations
- Coding benchmarks (TBLite, TerminalBench)
- Open-source AI infrastructure

## Related Entities

- [[entities/deedydas]] — Originated the popular meta-harness framing she built upon
- [[entities/nous-research]] — Creators of Hermes Agent
- [[concepts/meta-harness]] — The concept implemented in hermes-agent-metaharness
- [[concepts/harness-engineering]] — Broader discipline of agent execution environment design

## See Also

- [[concepts/meta-harness]]
- [[concepts/harness-design-long-running-apps]]
- [[entities/hermes-agent]]
- [[concepts/autoresearch]]
- [[entities/deedydas]]
