---
title: "Drew Breunig — Key Projects"
type: entity
parent: drew-breunig
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - methodology
  - open-source
sources: []
---

# Drew Breunig: Key Projects

Back to main profile: [[entities/drew-breunig]]

## Reporter (2014)

An award-winning iPhone app co-created with information designer Nicholas Felton. Reporter prompted users with quizzes throughout the day ("Where are you?", "What are you doing?", "Who are you with?") to collect personal data and generate visualizations. Unlike automatic tracking tools, Reporter emphasized intentional, meaningful data collection.

- Featured in The Verge, FlowingData, Washington Post
- Data exported as CSV/JSON — user-owned data philosophy
- Design based on Felton's Annual Reports tradition
- Breunig built the technical implementation; Felton designed the experience

See also: [[concepts/nicholas-felton]]

## StepList (2024)

A checklist and routine management application designed and built by Breunig. Inspired by Atul Gawande's "The Checklist Manifesto," StepList sits between simple to-do apps (Todoist) and complex project management tools (Jira).

- Create, perform, schedule, delegate, and share routines
- Unified desktop and mobile interface
- Free with optional $5/month premium plan
- Uses AI to pre-populate list icons and initial steps
- Built as a personal project that became a product

## whenwords (2024)

A software library distributed with **no code** — just a Markdown specification, YAML test suite, and prompt for coding agents. It implements a "relative time formatting" library (e.g., "3 days ago", "2 weeks from now") that agents can implement in any language.

- 1,200+ GitHub stars
- Demonstrated spec-driven development as a viable paradigm
- Generated implementations in Python, Ruby, Go, Rust, Elixir, PHP, Bash, Excel macros
- Noted by Andrej Karpathy as "mind-blowing"

## plumb (2026)

A proof-of-concept tool for managing the [[concepts/spec-driven-development|Spec-Driven Development Triangle]]. Plumb intercepts `git commit` via a pre-commit hook, analyzes staged changes and coding agent conversations, extracts decisions, and gates commits on human review.

- Keeps specs, tests, and code in sync
- 88 GitHub stars
- Built as a practical response to the challenges Breunig identified in SDD

## DSPy Integration Work

Breunig has been a significant contributor to the [[concepts/dspy|DSPy]] ecosystem, implementing RLM support and demonstrating practical applications:

- **dspy-monty-interpreter**: Drop-in code interpreter using Monty Python emulator for DSPy's RLM module
- **dspy-tutorial-deep-research**: Tutorial materials for DSPy
- Presented at Databricks Data + AI Summit 2025 on using DSPy for LLM pipeline optimization
- Demonstrated optimizing conflation programs across multiple models (Qwen 3 0.6B → 91% performance, Llama 3.2 1B → 95% performance)

## foggy-bot (2025–2026)

A personal weather website for Downtown San Francisco, demonstrating Breunig's approach to building lightweight, purpose-built tools with AI assistance.

## drskill (2026)

A CLI tool for debugging and auditing agent skill/MCP configurations. drskill analyzes how MCPs and Skills are triggered — globally or in a project — by examining traces. Key features:

- **Agent loadout debugging**: Inspect which skills and MCP servers are active for a given agent run
- **MCP & Skill auditing**: Trace how MCP tools and skills are invoked, identify unused or conflicting configurations
- **CI security for agent contexts**: Verify that agent contexts don't leak sensitive information or load unauthorized tools
- GitHub: [dbreunig/drskill](https://github.com/dbreunig/drskill)

Announced July 2026. Positioned as a developer tool for the growing ecosystem of [[concepts/agent-skills|agent skills]] and MCP-based architectures.

## DSPy / GEPA Ecosystem Contributions (2026)

- **skilled-proposer**: A GEPA proposer designed to reduce overfitting, with configurable parameters for tailoring proposer instructions to specific tasks. Built for the [[concepts/gepa|GEPA]] optimizer ecosystem. GitHub: [cmpnd-ai/skilled-proposer](https://github.com/cmpnd-ai/skilled-proposer)

## Overture Maps / GERS Work

As GERS Evangelist at [[concepts/overture-maps-foundation|Overture Maps Foundation]], Breunig:

- Advocates for the Global Entity Reference System as a geospatial data standard
- Demonstrates practical GERS usage (e.g., mapping Overture GERS IDs to US Census FIPS codes using DuckDB)
- Writes about the democratization of geospatial data through persistent identifiers
- Presents at GeoBuiz and other geospatial conferences

## See Also

- [[entities/drew-breunig--core-ideas|Core Ideas]]
- [[entities/drew-breunig--timeline|Timeline]]
- [[entities/drew-breunig--writings|Writings & Speaking]]
