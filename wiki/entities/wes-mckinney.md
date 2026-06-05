---
title: Wes McKinney
type: entity
aliases: [wesm, wesmckinn]
created: 2026-05-14
updated: 2026-06-05
status: L2
tags:
  - person
  - ai-agents
  - agent-skills
  - coding-agents
  - developer-tooling
  - harness-engineering
  - open-source
sources:
  - raw/articles/2026-05-12_hugobowne_agentic-engineering-verification.md
  - transcripts/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - https://wesmckinney.com/
  - https://en.wikipedia.org/wiki/Wes_McKinney
  - https://posit.co/blog/the-prolific-output-of-wes-mckinney-in-the-age-of-agentic-engineering
---

# Wes McKinney

**Creator of pandas, Apache Arrow, and Ibis. Principal Architect at Posit. Angel investor (Composed Ventures). Leading figure in agentic engineering.**

## Quick Facts

| | |
|---|---|
| **X/Twitter** | [@wesmckinn](https://x.com/wesmckinn) (~59K followers) |
| **GitHub** | [wesm](https://github.com/wesm) |
| **Website** | [wesmckinney.com](https://wesmckinney.com) |
| **Role** | Principal Architect at [Posit](https://posit.co) |
| **Location** | Nashville, TN |
| **Education** | BS Mathematics, MIT (2007); PhD Statistics, Duke (leave 2011) |
| **Known for** | pandas, Apache Arrow, Apache Parquet, Ibis, Python for Data Analysis |
| **Recent focus** | Agentic engineering: RoboRev, Agents View, Middleman, Kata, spicytakes.org |

## Bio

Wes McKinney is an American software developer, entrepreneur, and open-source pioneer. He created **pandas** in 2008 while working as a quant researcher at AQR Capital Management, open-sourcing it in 2009 — a move that helped establish Python as the dominant language for data science. He is also co-creator of **Apache Arrow**, a cross-language columnar memory format, and creator of **Ibis**, a portable Python dataframe API. He authored the definitive reference *Python for Data Analysis* (O'Reilly, 3 editions as of 2022).

He co-founded **DataPad** (acquired by Cloudera, 2014), founded **Ursa Labs** (with Posit, 2018), co-founded **Voltron Data** ($110M raised, 2021), and now serves as Principal Architect at **Posit** (since 2023), where he contributes to **Positron**, a next-generation data science IDE built on VS Code. He is a Member of The Apache Software Foundation, a PMC member for Apache Parquet, and GP at **Composed Ventures**, his angel investment fund.

Since late 2025, McKinney has emerged as one of the most visible practitioners of **agentic engineering** — developing software primarily through AI coding agents rather than direct code authorship. He has shipped five AI-centric open-source projects in rapid succession, written in Python, Go, Rust, and Swift — languages he had minimal prior experience with. His work has been described by Posit colleagues as "several lifetimes of distinguished work" unfolding in real time.

## Philosophy: Agentic Engineering

### "I almost don't read code now"

McKinney's core thesis is that the role of the human developer is shifting from **writing and reading code** to **directing agents and architecting verification systems**. His mantra:

> "I almost don't read code now. My approach with Roborev is it's like my code reader. The mantra is: Roborev reads every line of code that is generated. It gets read multiple times. And so, whenever I push up a pull request, the branch gets re-reviewed. And so by the time I'm merging a pull request into a repository, the code has all been read by agents four or five times minimum. I look at the code in terms of structural detail: does it look right?"
> — *Show Us Your Agent Skills*, Episode 1 (May 2026)

### Adversarial Agent Review

McKinney advocates for **adversarial multi-agent review** — using a different agent/capability profile than the one that wrote the code:

- AI coding agents write code quickly but produce "fundamentally buggy code" that "has to be really rigorously reviewed by other agents"
- The agent that wrote the code is less likely to spot its own bugs
- He has run over **3,000 automated reviews** in a matter of weeks
- His workflow: Claude Code writes → Codex/GPT-5.5 reviews → fixes flow back into the authoring session

### Agent Ergonomics (2026)

McKinney argues that AI coding agents fundamentally change which programming languages are optimal:

> "Human ergonomics in programming languages matters much less now."

**Key tenets**:
1. **Compile-test cycles dominate** — agents compile-and-test 10-100x more often than humans. Python's slower test cycles become punishing at agent scale.
2. **Distribution is essential** — self-contained static binaries (Go, Rust) are the right modality for agentic tools
3. **Human readability is secondary** — when code is authored by agents, simplicity matters less than iteration speed
4. **Go has an edge over Rust** — ultrafast compile times give Go a substantial advantage in agentic loops
5. **Python won't die** — the data science/ML ecosystem moat ensures Python's continued role, but the "Python part" of the stack will thin

### The Four-Layer Stack

McKinney proposes separating the data/AI stack into layers by durable value:

1. **Compute, IO, compiler kernels** — CUDA, MLIR, JAX/XLA, Apache Arrow (where long-term value lives)
2. **Database and caching** — ideally with ADBC zero-serialization connectivity
3. **Language bindings and orchestration** — thin Python wrappers
4. **Application/agent interfaces** — the thinnest layer, sits on top

Long-term value resides in layers 1-2, not 3-4.

### "The Mythical Agent Month"

McKinney's essay draws on Fred Brooks' 1975 classic *The Mythical Man-Month*:

> "With coding agents, we are writing code faster than ever. But hands on keyboards was never the bottleneck."

He warns that agents excel at building **software facades** but struggle with the ~9x harder work of turning prototypes into robust, maintainable products. The bottleneck shifts from code production to verification, architecture, and quality assurance.

### Vibe Coding vs. Agentic Engineering

McKinney draws a sharp distinction:
- **Vibe coding**: accepting agent output uncritically, shipping without rigorous review
- **Agentic engineering**: systematic multi-agent review, adversarial verification, continuous automated QA

> "I still care about code quality, how fast my test suite runs, how fast the code runs, the long-term sustainability, the growth of the code base. I think a lot of vibe-coded software will simply rot."

## Current Projects (Agentic Era)

### RoboRev
[roborev.io](https://roborev.io/) | [GitHub](https://github.com/roborev-dev/roborev) | Written in **Go**

A continuous background code review daemon that reviews every commit as it happens. Installs as a post-commit hook, runs reviews in the background, and surfaces issues in seconds rather than hours.

- **55+ releases**, version 0.26.0+
- Supports multiple agents: **Codex, Claude Code, Gemini, Copilot**, and others
- Commands: `roborev fix` (auto-fix issues), `roborev refine` (iterative branch refinement), `roborev analyze refactor` (per-file refactoring analysis)
- Interactive terminal interface
- Has an engaged community of contributors
- McKinney calls it "essential to managing the poor code quality of agents in rapidly expanding agentic code bases"
- Uses **GPT-5.5** as the strongest reviewer

### Agents View
[agentsview.io](https://www.agentsview.io/) | [GitHub](https://github.com/wesm/agentsview)

A fast local session viewer/database for Claude, Codex, and Gemini. Stores and indexes agent sessions so developers can review past interactions, track decisions, and audit agent behavior.

### Middleman
[GitHub](https://github.com/wesm/middleman)

A local GitHub dashboard — an alternative interface to GitHub that gives McKinney a unified view of issues, PRs, and CI status across all his projects. Built for his own workflow.

### Kata

A local issue tracker, built after Beads "destroyed some of my Git repositories, very annoyingly" (ep-1 @ 13:25). Part of McKinney's local-first toolchain replacing GitHub's web-based workflow.

### The Automated Software Factory

McKinney describes his ambition to scale agentic engineering into a full software factory:

> *"I'm thinking about ideas for how I could turn this into more of an automated software factory and build even more software, but the trouble is that I'm bandwidth limited in terms of my ability to make decisions throughout the day. And so I feel like I'm already in all these spec interviews, like I'm already at my decision-making bandwidth. Like I can't make any more decisions."* — *Show Us Your Agent Skills*, Ep. 1

The bottleneck is no longer code generation or even line-by-line code review — it's the builder's **structural decision-making capacity** throughout the day.

### msgvault
[msgvault.io](https://msgvault.io) | [GitHub](https://github.com/wesm/msgvault) | **DuckDB-powered**

A tool to archive and search a lifetime of email and chat. Features a terminal UI and MCP server. Built with agentic engineering ("not vibe-coded — hardcore agentic engineering"), with RoboRev doing continuous review throughout development.

### spicytakes.org
[spicytakes.org](https://spicytakes.org)

A content engine that scrapes and summarizes tech blogs, grades quotes by "spiciness," and presents curated highlights. Built entirely with coding agents.

- **1M+ lines of code generated agentically in 6 months**
- Covers 22+ authors and 31,000+ quotes
- 93 posts, 679 quotes spanning 2010-2026
- Started as a way to "liberate" the content from McKinney's 114+ conference talks and podcast appearances
- Expands to multiple blogs (a "franchise" model)
- McKinney calls it his primary example of large-scale agentic software development

## Skills Framework

McKinney builds his agent skills using the **Superpowers** framework created by **Jesse Vincent** ([@obra](https://github.com/obra), [GitHub](https://github.com/obra/superpowers)). Superpowers provides a structured way to define agent behaviors with:

- **Front matter** — metadata and configuration
- **Progressive disclosure** — skills reveal complexity only when needed
- **Thin drivers** — minimal wrappers that call tools, not fat abstractions

This aligns with McKinney's broader philosophy: the **harness** should be minimal, and the **skills** should encode the specific behaviors and judgments that make agents effective. He has described his agentic stack as a "software factory" of parallel agents, each guided by specific skills.

## Professional Timeline

| Year | Event |
|------|-------|
| 2007 | BS Mathematics, MIT |
| 2007-2010 | Quant researcher at AQR Capital Management; started pandas (April 2008) |
| 2009 | Open-sourced pandas |
| 2010-2011 | PhD program in Statistics, Duke University (leave of absence) |
| 2012 | Published *Python for Data Analysis* (O'Reilly, 1st ed.) |
| 2013-2014 | Co-founded DataPad (acquired by Cloudera, 2014) |
| 2014-2016 | Cloudera engineering; created Ibis |
| 2016-2018 | Two Sigma Investments; Apache Arrow development |
| 2018-2021 | Founded Ursa Labs (with Posit + Two Sigma) |
| 2021-2023 | Co-founder/CTO of Voltron Data ($110M raised) |
| 2023-present | Principal Architect at Posit; host of *The Test Set* podcast |
| 2025-2026 | Emerged as leading agentic engineering practitioner; shipped RoboRev, Agents View, Middleman, spicytakes.org, msgvault |

## Key Projects

| Project | Role | Language | Description |
|---------|------|----------|-------------|
| [pandas](https://pandas.pydata.org) | Creator, BDFL | Python | Industry-standard data analysis library |
| [Apache Arrow](https://arrow.apache.org) | Co-creator, PMC | C++/multi | Cross-language columnar memory format |
| [Apache Parquet](https://parquet.apache.org) | PMC member | C++ | Columnar storage format |
| [Ibis](https://ibis-project.org) | Creator | Python | Portable dataframe API for any backend |
| [Positron](https://positron.posit.co) | Contributor | TypeScript | Next-gen data science IDE on VS Code |
| [RoboRev](https://roborev.io) | Creator | Go | Continuous background code review daemon |
| [msgvault](https://msgvault.io) | Creator | Go | Email/chat archive with DuckDB |
| [Agents View](https://agentsview.io) | Creator | — | Local agent session viewer |
| [Middleman](https://github.com/wesm/middleman) | Creator | — | Local GitHub dashboard |
| [spicytakes.org](https://spicytakes.org) | Creator | Python/Go | AI-powered blog aggregation |
| *Python for Data Analysis* | Author | — | Definitive O'Reilly reference (3 editions) |

## Key Quotes

> "I almost don't read code now. Roborev reads every line of code that is generated. It gets read multiple times." — *Show Us Your Agent Skills* (May 2026)

> "If you're just committing and shipping the code that's coming out of Opus 4.6, that code is a bunch of hot garbage. It has to be really rigorously reviewed by other agents and different capability profiles." — *Joe Reis Podcast* (Apr 2026)

> "The whole reason to use Python is that it's easy to read and write. So if I'm not reading or writing the code, what's the point?" — *Joe Reis Podcast* (Apr 2026)

> "I put off learning Rust just long enough that I never have to learn it." — *Joe Reis Podcast* (Apr 2026)

> "I still care about code quality, how fast my test suite runs, how fast the code runs, the long-term sustainability, the growth of the code base. I think a lot of vibe-coded software will simply rot." — *The Test Set* (Apr 2026)

> "Do you like being able to close the laptop now? No, and that's becoming a bit of a problem. When I close the laptop, I feel guilty. I'm like — the computer could be doing things right now." — *The Test Set* (Apr 2026)

> "Pandas wasn't designed like a database. It probably should have been, but I didn't know what I was doing whenever I started the project." — *Data Renegades* (Mar 2026)

## Related Concepts

- [[concepts/agent-ergonomics]] — Language design principles for AI coding agents
- [[concepts/harness-engineering]] — Minimal harness architecture for agentic tools
- [[concepts/agentic-engineering]] — Professional discipline of developing software with coding agents
- [[concepts/vibe-coding]] — Uncritical acceptance of agent output (antithesis to McKinney's approach)

## Related Entities

- [[entities/roborev]] — McKinney's continuous code review daemon
- [[entities/agents-view]] — Agent session database
- [[entities/middleman]] — Local GitHub dashboard
- [[entities/superpowers]] — Jesse Vincent's skills framework used by McKinney
- [[entities/posit]] — McKinney's employer, formerly RStudio
- [[entities/jeremiah-lowin]] — Fellow guest on *Show Us Your Agent Skills*, Prefect founder
- [[entities/randy-olson]] — Fellow guest, Good Eye Labs CTO
- [[entities/jesse-vincent]] — Creator of Superpowers skills framework
- [[entities/hugo-bowne-anderson]] — Host of *Show Us Your Agent Skills*, Vanishing Gradients

## Links

- Website: [wesmckinney.com](https://wesmckinney.com)
- X/Twitter: [@wesmckinn](https://x.com/wesmckinn)
- GitHub: [wesm](https://github.com/wesm)
- LinkedIn: [wesmckinn](https://linkedin.com/in/wesmckinn)
- Book: [Python for Data Analysis](https://wesmckinney.com/book) (free online)
- Angel fund: [Composed Ventures](https://composed.vc)
- spicytakes.org: [https://spicytakes.org](https://spicytakes.org)
- RoboRev: [https://roborev.io](https://roborev.io)
- Agents View: [https://agentsview.io](https://agentsview.io)
- msgvault: [https://msgvault.io](https://msgvault.io)
- Superpowers: [https://github.com/obra/superpowers](https://github.com/obra/superpowers)

## See Also

- [[entities/roborev]]
- [[entities/superpowers]]
- [[entities/show-us-your-agent-skills]]
- [[concepts/generator-evaluator-pattern]]
- [[concepts/personal-software]]

## Log

- **2026-06-05**: Enriched with details from "The Agentic Software Factory" article. Updated Kata description, added "Automated Software Factory" section with quotes, added See Also links for new entities/concepts.
- **2026-05-14**: Initial entity page creation (L2 depth).
