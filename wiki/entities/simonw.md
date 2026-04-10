# Simon Willison (simonw)

**URL:** https://simonwillison.net/
**Blog:** Simon Willison's Weblog (simonwillison.net)
**GitHub:** @simonw
**Mastodon:** @simon@mastodon.social
**Twitter/X:** @simonw
**Bluesky:** @simonwillison.net
**Projects:** Datasette, LLM, sqlite-utils, llm-cli, cog, showboat, rodney, gisthost
**Location:** San Francisco, CA
**Flagship Creation:** Datasette — open-source tool for exploring and publishing data via SQLite

---

## Overview

Simon Willison is one of the most **prolific and influential voices** in the intersection of open-source software, data journalism, and artificial intelligence. He is the creator of **Datasette**, an open-source tool that transforms SQLite databases into searchable, browsable, publishable data portals. He is also the creator of **LLM**, a CLI tool for running large language models locally, and a constellation of Datasette plugins that have become the de facto toolkit for data-driven journalism and research.

Willison's blogging practice is itself an artifact worth studying. His weblog — updated nearly daily since 2002 — is a **living knowledge graph** of the tech industry. He publishes **TILs** (Today I Learned), release notes, research summaries, tool explorations, conference talk notes, and long-form essays, all tagged, dated, and cross-linked. In 2026, he added formal structure to the blog with TILs, releases, museums, tools, and research sections, making it one of the most organized and queryable personal knowledge bases on the internet.

His intellectual signature is **curiosity-driven pragmatism**: he tries things, documents what works, shares the failures, and builds tools from the patterns he discovers. In 2025-2026, his focus shifted heavily toward **agentic engineering** — the practice of using AI coding agents as collaborative partners in software development. He was an early and articulate advocate for this workflow, coining the term and writing extensively about patterns, anti-patterns, and economic incentives.

Willison's blog is **sponsored by WorkOS** ($10/month subscription for a monthly briefing email), making him one of the earliest examples of a successful individual creator sponsorship model in the tech writing space. His monthly briefings are widely read by engineers, researchers, and AI practitioners for their dense, accurate summarization of the month's LLM developments.

---

## Timeline

| Date | Event |
|------|-------|
| 2002 | Starts Simon Willison's Weblog (simonwillison.net) — one of the oldest continuously-running tech blogs |
| 2005 | Co-creates Django web framework (with Adrian Holovaty) at World Online |
| 2006 | Django open-sourced; becomes one of the most popular Python web frameworks |
| 2008 | Leaves World Online; becomes independent consultant/contractor |
| 2010s | Lanyrd (event discovery platform, acquired by Eventbrite); speaks at numerous conferences |
| 2017 | Launches Datasette — explore and publish data with SQLite |
| 2019 | Datasette ecosystem grows; sqlite-utils; datasette.io documentation site |
| 2020 | Launches `llm` project — CLI for running language models |
| 2021 | Datasette Cloud; plugin ecosystem expansion |
| 2022 | ChatGPT launch triggers intensive AI exploration; blog coverage intensifies |
| 2023 | LLM tool ecosystem: llm-gemini, llm-claude, prompt templates, embedding support |
| 2024 | Agentic engineering explorations; Claude API experiments; coding agent evaluations |
| Jan 2025 | "LLM predictions for 2026" shared with Oxide and Friends; gisthost.github.io launch |
| Feb 2025 | go-to-wheel (distributing Go binaries through PyPI); Pydantic's Monty in WASM; StrongDM AI team study |
| Feb 2025 | Showboat and Rodney launch — agent demo tools; Chartroom and datasette-showboat |
| Feb 2025 | Blog restructured: adds TILs, releases, museums, tools, research sections |
| Feb 2025 | "Writing about Agentic Engineering Patterns"; "I vibe coded my dream macOS presentation app" |
| Mar 2025 | Qwen exploration; clean-room relicensing question; "Perhaps not Boring Technology after all" |
| Mar 2025 | Pragmatic Summit fireside chat on agentic engineering; GPT-5.4 mini/nano ($52 for 76K photo descriptions) |
| Mar 2025 | OpenAI acquires Astral/uv/ruff/ty; HN user profiling; Starlette 1.0 with Claude skills |
| Mar 2025 | "Vibe coding SwiftUI apps is a lot of fun"; Mr. Chatterbox (Victorian-era ethically trained model) |
| Apr 2025 | "Agentic engineering: execution > generation" thesis; "Clinejection" attack chain analysis |
| Apr 2025 | datasette-graphql 3.0a1; datasette-llm 0.1a5; Axios supply chain attack analysis |
| Apr 2025 | Secret scanning CLI; datasette-ports; Gemma 4 API testing |
| Active through Apr 2026 | ~60+ blog posts in Q1 2026 alone; monthly briefing sponsorships; active Datasette/LLM development |

---

## Core Ideas

### Agentic Engineering: Execution Over Generation

Willison's most significant contribution to AI discourse in 2025-2026 is the concept of **agentic engineering** — using AI coding agents (Claude Code, Cursor, Codex) not just as autocomplete tools but as **collaborative partners** that can execute, test, and iterate on code. His central thesis:

> *"The defining trait of coding agents is their ability to run code. Never assume AI output works until executed and verified."*

He documented this extensively in a Lenny Rachitsky podcast appearance ("An AI state of the union: We've passed the inflection point, dark factories are coming, and automation timelines"), a Pragmatic Summit fireside chat, and numerous blog posts. His approach is characterized by:

- **Prototype-driven iteration** — start with concrete prototypes, not abstract designs
- **Disciplined architecture reviews** — humans remain essential for high-level design
- **Execution-first verification** — AI generates, human validates

### AI's Design Blind Spot

Willison (via Lalit Maganti's work on `syntaqlite`) articulated a crucial limitation of current AI systems:

> *"When I was working on something where I didn't even know what I wanted, AI was somewhere between unhelpful and harmful... Implementation has a right answer, at least at a local level: the code compiles, the tests pass, the output matches what you asked for. Design doesn't. We're still arguing about OOP decades after it first took off."*

This insight distinguishes his analysis from both AI hype and AI skepticism — he sees AI as **powerful but categorically limited**, excelling at concrete, verifiable tasks while struggling with open-ended architectural decisions.

### Vibe Coding

Willison embraced and documented **vibe coding** — the practice of iteratively building software through natural language interaction with AI agents. His "I vibe coded my dream macOS presentation app" and "Vibe coding SwiftUI apps is a lot of fun" posts showed genuine enthusiasm tempered by clear-eyed assessment:

- SwiftUI + AI is productive because the framework is declarative and well-documented
- The output quality depends heavily on the specificity of the prompt
- It works best for self-contained projects with clear acceptance criteria

### Datasette and the SQLite Renaissance

Willison has been a central figure in the **SQLite renaissance** — the rediscovery of SQLite as a general-purpose data platform, not just an embedded database. Datasette turns any SQLite database into a **queryable, browsable, API-accessible data portal**. His 2025-2026 work expanded this ecosystem:

- **datasette-graphql 3.0a1** — automatic GraphQL API generation from SQLite schemas
- **datasette-llm** — LLM integration for Datasette plugins
- **datasette-enrichments-llm** — AI-powered data enrichment pipelines
- **datasette-ports** — discovery of running Datasette instances
- **datasette-showboat** — agent demonstration tools
- **Chartroom** — visualization plugin

### The "Clinejection" Attack Chain

In April 2025, Willison documented a critical vulnerability where a malicious GitHub issue title was used as a **prompt injection vector** against Claude Code's GitHub Actions integration. The attack chain involved:

1. Malicious issue title injected into `anthropics/claude-code-action@v1`
2. Prompt tricked Claude into running `npm install` with a malicious package
3. Cache poisoning via stuffed GitHub Actions caches
4. Stolen NPM publishing secrets → compromised release

This analysis demonstrated Willison's ability to **translate technical vulnerabilities into actionable lessons** for the broader developer community.

### Supply Chain Security and AI

Willison's coverage of the **Axios npm supply chain attack** (April 2026) traced it to individually targeted social engineering against a maintainer. His thesis: as AI generates more vulnerability reports (Linux/cURL/HAProxy maintainers now receive 5-10 high-quality AI reports/day, up from 2-3/week), the **human element remains the weakest link**.

### "Something Is Afoot in the Land of Qwen"

In March 2025, Willison wrote about Alibaba's Qwen model family with notable concern about **high-profile team departures** raising sustainability questions. This reflects his broader pattern of tracking not just technical capabilities but the **organizational and economic forces** shaping AI development.

---

## Key Quotes

> *"The defining trait of coding agents is their ability to run code. Never assume AI output works until executed and verified."*

> *"Implementation has a right answer, at least at a local level: the code compiles, the tests pass, the output matches what you asked for. Design doesn't."*

> *"Markets will not reward slop in coding, in the long-term."* — citing Soohoon Choi

> *"The challenge with AI in open source security has transitioned from an AI slop tsunami into more of a... plain security report tsunami. Less slop but lots of reports."* — citing Greg Kroah-Hartman

> *"Substantial amounts of high-impact vulnerability research (maybe even most of it) will happen simply by pointing an agent at a source tree and typing 'find me zero days'."* — citing Thomas Ptacek

> *"Vibe coding SwiftUI apps is a lot of fun."*

---

## Recent Themes (2024–2026)

- **Agentic engineering patterns:** Execution-first workflows, prototype-driven iteration, human-in-the-loop architecture
- **Vibe coding:** Building production software through natural language interaction with AI agents
- **Datasette ecosystem expansion:** GraphQL, LLM integration, port discovery, visualization tools
- **LLM tooling:** `llm` CLI, plugin system, local model experimentation, embedding pipelines
- **Supply chain security:** Axios attack analysis, Clinejection prompt injection, AI-generated vulnerability reports
- **SQLite as a platform:** Bytecode exploration, query planner statistics, schema analysis tools
- **AI economics:** GPT-5.4 mini/nano cost analysis ($52 for 76K photo descriptions), model comparison
- **Open-source sustainability:** Model team departures (Qwen), clean-room relicensing debates, maintainer access programs
- **Blog as knowledge infrastructure:** Restructuring with TILs, releases, museums, tools, research sections
- **Monthly briefing sponsorships:** Creator economy model — $10/month for curated LLM digest

---

## Related

- [[Datasette]] — Open-source data exploration and publishing via SQLite
- [[LLM Tooling]] — CLI tools, plugins, and APIs for running language models
- [[Agentic Engineering]] — AI coding agents as collaborative development partners
- [[SQLite Renaissance]] — SQLite as a general-purpose data platform
- [[Supply Chain Security]] — Open-source package vulnerabilities and social engineering attacks
- [[Vibe Coding]] — Iterative software development via natural language AI interaction
- [[Open Source Sustainability]] — Model team dynamics, maintainer access, relicensing
- [[Knowledge Management]] — Blog as structured knowledge graph, TILs, cross-linking

---

## Influence

- **Django co-creator** — one of the most popular Python web frameworks (2005)
- **Datasette** — transformed SQLite into a general-purpose data platform; active plugin ecosystem
- **LLM CLI** — popular tool for running language models locally; extensible plugin architecture
- **Agentic engineering advocate** — early and articulate voice on AI coding workflows
- **Blog since 2002** — one of the oldest continuously-running tech blogs; ~2,000+ posts
- **Conference speaker** — DjangoCon, PyCon, LLM Summit, Pragmatic Summit, Oxide and Friends
- **Monthly briefing sponsor** — pioneering individual creator sponsorship model ($10/month)
- **GitHub:** ~50K+ stars across projects; active contributor to Python, SQLite, and AI ecosystems
- **Security research** — documented Clinejection attack chain, Axios supply chain analysis, CSP sandboxing research
- **Go-to-wheel** — enabled distributing Go binaries through PyPI

---

## Sources

- simonwillison.net — Simon Willison's Weblog (2002–present)
- "LLM predictions for 2026" shared with Oxide and Friends (Jan 2026)
- "Writing about Agentic Engineering Patterns" (Feb 2026)
- "I vibe coded my dream macOS presentation app" (Feb 2026)
- "Perhaps not Boring Technology after all" (Mar 2026)
- "Vibe coding SwiftUI apps is a lot of fun" (Mar 2026)
- "Highlights from my conversation about agentic engineering on Lenny's Podcast" (Apr 2026)
- "The Axios supply chain attack used individually targeted social engineering" (Apr 2026)
- Release: datasette-graphql 3.0a1 (Apr 2026)
- Datasette plugin ecosystem (datasette.io)
- LLM CLI (github.com/simonw/llm)
- GitHub: @simonw
