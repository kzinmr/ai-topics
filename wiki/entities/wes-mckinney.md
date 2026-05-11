---
title: Wes McKinney
type: entity
aliases: [wesm, wesmckinn]
created: 2026-05-11
updated: 2026-05-11
status: L2
sources: [https://wesmckinney.com/, https://en.wikipedia.org/wiki/Wes_McKinney, https://wesmckinney.com/about/, https://x.com/wesmckinn, https://github.com/wesm, raw/articles/2026-01-20_wesmckinney_agent-ergonomics.md]
tags: [person, blogger, open-source, data-science]
---

# Wes McKinney

pandas creator, Apache Arrow co-creator, and open-source data infrastructure pioneer. Principal Architect at [Posit](https://posit.co) (formerly RStudio). Author of *Python for Data Analysis*. Angel investor via [Composed Ventures](https://composed.vc).

Recently deeply immersed in agentic engineering, building projects across Python, Go, Rust, and Swift — all via coding agents.

## Core Ideas

### Agent Ergonomics（2026）

> "Human ergonomics in programming languages matters much less now."

McKinney argues that AI coding agents shift the optimal language choice away from human-friendly languages (Python) toward languages optimized for the agentic loop: fast compile-test cycles, painless distribution, and lean runtime characteristics.

**Key tenets**:

1. **Compile-test cycles dominate**: Agents compile-and-test 10-100x more often than humans. Python's slower test cycles and interpreter overhead become punishing at agent scale.
2. **Distribution is essential**: Self-contained, dependency-free binaries (Go/Rust) are the right modality for tools in the agentic loop.
3. **Human ergonomics is secondary**: When code is primarily authored by agents, readability and simplicity matter less than iteration speed.
4. **Go has an edge over Rust**: Ultrafast compile times for release builds give Go a substantial advantage in agentic iteration loops.
5. **Python won't die**: The data science/ML ecosystem moat (NumPy, pandas, PyTorch) ensures Python's continued role, but the "Python part" of the stack will thin as lower layers are re-engineered.

### The Four-Layer Stack

McKinney proposes separating the data/AI stack into layers by durable value:

1. **Compute, IO, compiler kernels**: CUDA, MLIR, JAX/XLA, Apache Arrow — where the long-term value lives
2. **Database and caching**: Ideally with ADBC zero-serialization connectivity
3. **Language bindings and orchestration**: Python wrappers that expose lower-layer capabilities
4. **Application/agent interfaces**: The thinnest layer, sits on top

Long-term value resides in layers 1-2, not 3-4.

### roborev & Agentic Tooling

Built [roborev](https://github.com/wesm/roborev) — a continuous background code review system written in Go. Key motivations:
- Agents' commits are full of bugs and imperfections
- McKinney is "definitely less effective manually reviewing languages I never used pre-AI"
- Automated code review as a force multiplier for agentic engineering

Other agentic projects: [moneyflow](https://moneyflow.dev/) (Python TUI accounting), [agent-session-viewer](https://github.com/wesm/agent-session-viewer) (Python session history), [agentsview](https://github.com/wesm/agentsview) (fast local session viewer), [msgvault](https://github.com/wesm/msgvault) (email/chat archive).

## Professional Background

- **2007**: BS Mathematics, MIT
- **2007-2010**: Quant researcher at AQR Capital Management — migrated research to Python, started pandas (April 2008)
- **2010-2011**: PhD program in Statistics at Duke University (leave)
- **2012**: Authored *Python for Data Analysis* (O'Reilly, 3 editions)
- **2013-2014**: Co-founded DataPad (acquired by Cloudera)
- **2014-2016**: Cloudera engineering team — created Ibis
- **2016-2018**: Two Sigma Investments — Apache Arrow development
- **2018-2021**: Founded Ursa Labs (with RStudio/Posit + Two Sigma)
- **2021-2023**: Co-founder/CTO of Voltron Data ($110M raised)
- **2023-present**: Principal Architect at Posit, host of *The Test Set* podcast

## Key Projects

| Project | Role | Language |
|---------|------|----------|
| [pandas](https://pandas.pydata.org) | Creator, BDFL | Python |
| [Apache Arrow](https://arrow.apache.org) | Co-creator, PMC | C++/multi |
| [Apache Parquet](https://parquet.apache.org) | PMC member | C++ |
| [Ibis](https://ibis-project.org) | Creator | Python |
| [roborev](https://github.com/wesm/roborev) | Creator | Go |
| [msgvault](https://github.com/wesm/msgvault) | Creator | — |
| [agentsview](https://github.com/wesm/agentsview) | Creator | — |

## Links

- Website: [wesmckinney.com](https://wesmckinney.com/)
- X/Twitter: [@wesmckinn](https://x.com/wesmckinn)
- GitHub: [wesm](https://github.com/wesm)
- LinkedIn: [wesmckinn](https://linkedin.com/in/wesmckinn)
- Book: [Python for Data Analysis](https://wesmckinney.com/book)
- Angel fund: [Composed Ventures](https://composed.vc)

## Related Concepts

- [[concepts/agent-ergonomics]] — Programming language design principles for AI coding agents
- [[concepts/harness-engineering/agentic-engineering]] — Professional use of coding agents
- [[concepts/vibe-coding-vs-agentic-engineering]] — Vibe coding vs agentic engineering distinction
