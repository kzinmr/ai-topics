---
title: Drew Breunig
created: 2026-04-10
updated: 2026-04-10
source: blog
tags:
  - person
  - ai
  - context-engineering
  - geospatial
  - quantified-self
  - blog
---


# Drew Breunig

| | |
|---|---|
| **Blog** | [dbreunig.com](https://www.dbreunig.com/) |
| **X/Twitter** | [@dbreunig](https://x.com/dbreunig) |
| **Mastodon** | [@dbreunig@note.computer](https://note.computer/@dbreunig) |
| **GitHub** | [dbreunig](https://github.com/dbreunig) |
| **LinkedIn** | [drewbreunig](https://linkedin.com/in/drewbreunig) |
| **Location** | Alameda, CA |

## Overview

Drew Breunig is a writer, developer, and strategist working at the intersection of cultural anthropology, computer science, and media. He is one of the most prominent early voices on **context engineering** — the discipline of systematically managing LLM context windows — and a leading commentator on **spec-driven development**, **coding agents**, and **Recursive Language Models (RLMs)**. He currently works as a GERS Evangelist with the [Overture Maps Foundation](https://overturemaps.org) and is associated with [cmpnd-ai](https://www.cmpnd.ai).

Breunig's career spans advertising, location intelligence, geospatial data, and AI. He co-founded **Reporter** (2014), an award-winning quantified-self app with Nicholas Felton, and built **StepList** (2024), a routine management application. His 2024–2025 writings on context engineering, particularly "How Long Contexts Fail" and "Why Context Engineering Matters," positioned him as a key thinker in the emerging field of LLM application architecture. He speaks regularly at conferences including Databricks Data + AI Summit, O'Reilly's Context Engineering Superstream, and the ACM Conference on AI and Agentic Systems.

His blog at dbreunig.com, active since 2010, covers AI, geospatial technology, media, culture, and software development with a distinctive voice that blends anthropological insight with technical depth.

## Timeline

| Date | Event |
|------|-------|
| 2002–2006 | BA in Cultural Anthropology, UC Santa Cruz |
| 2006–2008 | Account Planner at Plan B — developed brand strategies for IBM, P&G, Clorox, Diageo |
| 2008–2012 | Director of Technology at Annalect Group (Omnicom Media Group) — designed strategies for EA, Boost Mobile, HP |
| 2010 | Begins writing at dbreunig.com, exploring the intersection of technology and culture |
| 2012–2019 | SVP Strategy at PlaceIQ — led strategy and data science for location intelligence |
| 2013 | Co-develops Reporter app with Nicholas Felton (released 2014) |
| 2014 | Reporter launches — award-winning quantified-self app for iPhone |
| 2014–2016 | Writes extensively on media measurement, advertising technology, and data ethics |
| 2016–2019 | EVP Strategy at PlaceIQ — ran strategy, data science, and client projects |
| 2019 | PlaceIQ acquired by Precisely |
| 2022–2025 | VP Strategy at Precisely — designed strategy for data integrity software; led Overture Maps collaboration |
| 2023 | Begins writing intensively about AI, LLMs, and prompt engineering |
| 2024 | "A Plea for Sober AI" — early call against AI hype |
| 2024 | "The 3 AI Use Cases: Gods, Interns, and Cogs" — influential AI taxonomy |
| 2024 | "Towards Standardizing Place" — advocacy for Overture's GERS |
| 2024 | Launches StepList, a checklist/routine management app |
| 2024 | Releases `whenwords` — a no-code software library for spec-driven development |
| 2025 | "How Long Contexts Fail" — seminal article on context management |
| 2025 | "How to Fix Your Context" — follow-up with practical mitigation strategies |
| 2025 | "Why Context Engineering Matters" — Databricks Data + AI Summit presentation |
| 2025 | O'Reilly Context Engineering Superstream speaker |
| 2025 | Announces editing "The Context Engineering Handbook" |
| 2025 | Speaks at MLOps Community's "Coding Agents" conference on Spec-Driven Development |
| 2025 | Releases `plumb` — tool for keeping spec/tests/code in sync |
| 2026 | GERS Evangelist at Overture Maps Foundation |
| 2026 | "Two Beliefs About Coding Agents" — influential analysis of AI coding impact |
| 2026 | "The 2nd Phase of Agentic Development" — on reimaginings vs. clones |
| 2026 | "How Claude Code Builds a System Prompt" — deep analysis of coding agent internals |

## Core Ideas

### Context Engineering as a Discipline

Breunig is perhaps best known for coining and popularizing the term **"context engineering"** to describe the systematic management of LLM context windows. His work emerged in mid-2025, coinciding with Andrej Karpathy's similar articulation of the concept. Breunig argued that as context windows grew from 4K to 1M+ tokens, simply stuffing more information into prompts was counterproductive — it introduced new failure modes that required dedicated engineering discipline.

His framework identifies four primary context failures:

- **Context Poisoning**: When a hallucination or error enters the context and is repeatedly referenced, compounding over time. The Gemini 2.5 team documented this when their agent playing Pokémon would hallucinate and then repeatedly reference its own error.
- **Context Distraction**: When the context overwhelms the model's training, causing it to focus on provided information at the expense of its general knowledge. Databricks research showed Llama 3.1 405B correctness began falling around 32K tokens.
- **Context Confusion**: When irrelevant or contradictory information in the context leads to degraded responses. A quantized Llama 3.1 8B model failed with 46 tools but succeeded with 19.
- **Context Clash**: When tool descriptions or instructions contradict the rest of the prompt, creating internal confusion.

His mitigation framework includes six tactics:

| Tactic | Description |
|--------|-------------|
| **RAG** | Selectively adding relevant information to context |
| **Tool Loadout** | Choosing only relevant tool definitions |
| **Context Quarantine** | Isolating contexts in dedicated threads |
| **Context Pruning** | Removing irrelevant information |
| **Context Summarization** | Condensing accrued context |
| **Context Offloading** | Storing information outside the context window |

> "Programming the LLM to, as Karpathy says, 'pack the context windows just right' — smartly deploying tools, information, and regular context maintenance — is the job of the agent designer."

### The 3 AI Use Cases: Gods, Interns, and Cogs

In October 2024, Breunig proposed a taxonomy for understanding AI applications that cut through the hype:

- **Gods**: Models used for their creative and generative capabilities — writing, brainstorming, ideation. The model is the product.
- **Interns**: Models used to augment human work — coding assistants, research aides. The human is still in the loop.
- **Cogs**: Models used for automated, repetitive tasks — classification, extraction, routing. The model is a component in a larger system.

This framework helped practitioners reason about which AI approaches fit their actual needs rather than chasing every new capability.

### Sober AI and Quiet AI

Breunig has been a consistent voice for measured, practical AI adoption. In "A Plea for Sober AI" (May 2024), he argued:

> "The hype is so loud we can't appreciate the magic."

He advocates for "quiet AI" — AI features that work invisibly to improve user experience rather than demanding attention through chatbots and interfaces. In "In Pursuit of Quiet AI Features" (February 2024), he explored how the best AI implementations enhance existing workflows without changing them fundamentally.

His "Be Better, Not Smaller" essay (July 2024) argued against the trend of building smaller, dumber models:

> "Most AI products are making a familiar mistake."

### Spec-Driven Development and the SDD Triangle

Breunig is a pioneer of **Spec-Driven Development (SDD)** — using coding agents to implement software from detailed text specifications and test suites, without writing code directly. His `whenwords` project (late 2024) was a landmark demonstration: a software library distributed as a Markdown specification and YAML test suite, with no code at all. Developers could feed the spec to any coding agent and get a working implementation in their language of choice.

From this experience, he developed the **Spec-Driven Development Triangle**:

```
        Spec
       /    \
      /      \
    Tests -- Code
```

The triangle represents a feedback loop where:
- The **spec** defines what tests need to pass and what code should do
- The **tests** validate both the spec's requirements and the code's behavior
- The **code** is the implementation, but also reveals gaps in both spec and tests

> "Spec-driven development is a feedback loop, not a straight line. As each node moves forward, our job — and our tooling's job — is to keep the other two in sync."

He built `plumb` (2026) as a proof-of-concept tool to manage this triangle, intercepting git commits to analyze changes and ensure specs and tests stay synchronized with code.

### Recursive Language Models (RLMs)

Breunig is an advocate for **Recursive Language Models**, a pattern developed by Alex Zhang and Omar Khattab that gives LLMs a REPL environment to explore, analyze, and reason over large contexts. He implemented RLM support in DSPy and documented extensive use cases.

The key insight: RLMs maintain two distinct context pools — tokenized context (what fills the window) and external context (what the model can explore). This allows reasoning over contexts far larger than any single window, and importantly, RLMs generate traces that reveal their reasoning process.

> "If you run them on the same task several times, you're generating emergent agent discovery patterns."

### The Two Beliefs About Coding Agents

In February 2026, Breunig articulated two observations from watching the AI coding ecosystem mature:

1. **Most talented developers don't appreciate the impact of their intuitive knowledge on coding agents.** When luminaries share amazing results, they're bringing years of architectural intuition that the agent leverages. The same agent given to a junior developer would produce different results.

2. **Most work people share are incredible personal tools, but not capital-P Products.** The last 10% of product development — testing, support, marketing, distribution — remains the hard part. "Code today is free, as in puppies."

### Agentic Development: Clones → Reimaginings

In April 2026, Breunig identified a shift in open-source AI coding projects:

- **Phase 1 (Clones/Ports)**: Using agents to reimplement existing software (Anthropic's C compiler, Vercel's bash emulator). Low-hanging fruit because existing test suites provide ground truth.
- **Phase 2 (Reimaginings)**: Attacking old problems with modern tactics, unconstrained by legacy architecture. Cheng Lou's Pretext (text layout library) and Cloudflare's EmDash (CMS spiritual successor to WordPress).

> "Coding agents make reimagining practical because the cost to perform them is so, so much lower. Code is cheap. We can take more shots, more often, to counter the embedded standards."

### The Software Crisis Revisited

At the MLOps Community conference (March 2026), Breunig drew a historical parallel:

> "Being overwhelmed by the volume of code isn't a new problem. It's what birthed software engineering. The initial Software Crisis was our inability to manage complex codebases new computers allowed. Our current Software Crisis is our inability to manage complex codebases new models allow. Our problem used to be that we couldn't hold an entire codebase in our head. Now we can't even read our entire codebase."

He characterized the current moment as: "Waterfall volume at the cadence of agile. And even that undersells it: it's waterfall times ~two at the cadence of agile times ~seven."

### Geospatial Standardization and GERS

Breunig has been a leading advocate for the **Global Entity Reference System (GERS)**, a persistent identifier system developed by the Overture Maps Foundation. His "Towards Standardizing Place" essay argued that coordinate reference systems (like WGS 84) standardize locations but not places — buildings, businesses, parks, and other entities that people actually interact with.

GERS assigns a stable 128-bit, 32-character ID to every entity in Overture's dataset, enabling simple column joins across disparate geospatial datasets without complex spatial operations. Breunig argues this could dramatically expand the geospatial market by making it accessible to data analysts who aren't GIS specialists.

> "Standardizing location with WGS 84 hasn't proven sufficient. Every organization can benefit from geospatial intelligence, but the cost and complexity of onboarding geo data is prohibitive."

### Anthropological Lens on Technology

Breunig's background in cultural anthropology shapes his approach to technology analysis. He consistently examines how systems shape human behavior and culture, rather than treating technology as purely technical. His early writings (2010–2016) explored how Facebook Timeline, Chat Roulette, and Google Glass were changing social dynamics, and how algorithms might be affecting rather than merely reflecting human behavior.

> "Do Algorithms Find Depression or Cause Depression?" (2016) — examining whether crowdsourced workers' depression in ML training data was discovered or induced by the work itself.

## Key Projects

### Reporter (2014)

An award-winning iPhone app co-created with information designer Nicholas Felton. Reporter prompted users with quizzes throughout the day ("Where are you?", "What are you doing?", "Who are you with?") to collect personal data and generate visualizations. Unlike automatic tracking tools, Reporter emphasized intentional, meaningful data collection.

- Featured in The Verge, FlowingData, Washington Post
- Data exported as CSV/JSON — user-owned data philosophy
- Design based on Felton's Annual Reports tradition
- Breunig built the technical implementation; Felton designed the experience

### StepList (2024)

A checklist and routine management application designed and built by Breunig. Inspired by Atul Gawande's "The Checklist Manifesto," StepList sits between simple to-do apps (Todoist) and complex project management tools (Jira).

- Create, perform, schedule, delegate, and share routines
- Unified desktop and mobile interface
- Free with optional $5/month premium plan
- Uses AI to pre-populate list icons and initial steps
- Built as a personal project that became a product

### whenwords (2024)

A software library distributed with **no code** — just a Markdown specification, YAML test suite, and prompt for coding agents. It implements a "relative time formatting" library (e.g., "3 days ago", "2 weeks from now") that agents can implement in any language.

- 1,200+ GitHub stars
- Demonstrated spec-driven development as a viable paradigm
- Generated implementations in Python, Ruby, Go, Rust, Elixir, PHP, Bash, Excel macros
- Noted by Andrej Karpathy as "mind-blowing"

### plumb (2026)

A proof-of-concept tool for managing the Spec-Driven Development Triangle. Plumb intercepts `git commit` via a pre-commit hook, analyzes staged changes and coding agent conversations, extracts decisions, and gates commits on human review.

- Keeps specs, tests, and code in sync
- 88 GitHub stars
- Built as a practical response to the challenges Breunig identified in SDD

### DSPy Integration Work

Breunig has been a significant contributor to the DSPy ecosystem, implementing RLM support and demonstrating practical applications:

- **dspy-monty-interpreter**: Drop-in code interpreter using Monty Python emulator for DSPy's RLM module
- **dspy-tutorial-deep-research**: Tutorial materials for DSPy
- Presented at Databricks Data + AI Summit 2025 on using DSPy for LLM pipeline optimization
- Demonstrated optimizing conflation programs across multiple models (Qwen 3 0.6B → 91% performance, Llama 3.2 1B → 95% performance)

### foggy-bot (2025–2026)

A personal weather website for Downtown San Francisco, demonstrating Breunig's approach to building lightweight, purpose-built tools with AI assistance.

### Overture Maps / GERS Work

As GERS Evangelist at Overture Maps Foundation, Breunig:
- Advocates for the Global Entity Reference System as a geospatial data standard
- Demonstrates practical GERS usage (e.g., mapping Overture GERS IDs to US Census FIPS codes using DuckDB)
- Writes about the democratization of geospatial data through persistent identifiers
- Presents at GeoBuiz and other geospatial conferences

## Writing Themes and Evolution

### Early Period (2010–2016): Culture and Media

Breunig's early writing focused on how technology shapes culture and media:

- "The 5 Blows to the Human Ego" (2013)
- "Google Glass is Just Like the Segway – and Similarly Doomed" (2013)
- "Spectacles are the Anti-Glass" (2016)
- "Do Algorithms Find Depression or Cause Depression?" (2016)
- "A Community Camera Manifesto" (2016)
- "How the iPhone Led to Today's Internet Outage" (2016) — explaining DDoS problems

### Middle Period (2016–2022): Location Intelligence and Data

- "The Business Implications of Machine Learning" (2016)
- "Brands Are Finding Their Way With Location Data" (2016) — CMS Wire
- "Why Media Metrics Matter" (2022) — pinned Medium article

### AI Period (2023–Present): LLMs, Agents, and Engineering

Since ChatGPT's launch, Breunig's writing shifted intensely toward AI:

- **Prompt Engineering & Context**: "Prompt Engineering at the End of the Universe" (2024), "The Prompt Foreman" (2025), "Let the Model Write the Prompt" (2025)
- **AI Products & Strategy**: "The 3 AI Use Cases" (2024), "Be Better, Not Smaller" (2024), "What Remains After an AI Collapse?" (2024)
- **Agent Development**: "Enterprise Agents Have a Reliability Problem" (2025), "Two Beliefs About Coding Agents" (2026), "The 2nd Phase of Agentic Development" (2026)
- **RLMs & DSPy**: "The Potential of RLMs" (2026), "Pipelines & Prompt Optimization with DSPy" (2024)
- **Geospatial**: "Towards Standardizing Place" (2024), "DuckDB is Probably the Most Important Geospatial Software of the Last Decade" (2025)

## Speaking Engagements

- **Databricks Data + AI Summit 2025**: "Let the Model Write the Prompt — Why Applications & Pipelines Should Use DSPy"
- **Databricks Data + AI Summit 2026**: Featured speaker
- **O'Reilly Context Engineering Superstream (Feb 2026)**: "Context Fails and Fixes"
- **MLOps Community "Coding Agents" Conference (Mar 2026)**: "Learnings from a No-Code Library: Keeping the Spec Driven Development Triangle in Sync"
- **Dev Writers Meetup (Swyx)**: "Finding the Right Word"
- **GeoBuiz**: Multiple presentations on GERS and location intelligence

## Key Quotes

> "The hype is so loud we can't appreciate the magic." — A Plea for Sober AI (2024)

> "Most AI products are making a familiar mistake." — Be Better, Not Smaller (2024)

> "Code today is free, as in puppies." — Two Beliefs About Coding Agents (2026)

> "Being overwhelmed by the volume of code isn't a new problem. It's what birthed software engineering." — Spec-Driven Development talk (2026)

> "Agentic engineering enables waterfall volume at the cadence of agile. And even that undersells it: it's waterfall times ~two at the cadence of agile times ~seven." — Spec-Driven Development talk (2026)

> "There will be better strategies, optimizations, and models tomorrow. Don't be dependent on any one." — On DSPy philosophy (2025)

> "Programming the LLM to, as Karpathy says, 'pack the context windows just right' — smartly deploying tools, information, and regular context maintenance — is the job of the agent designer." — How to Fix Your Context (2025)

> "Standardizing location with WGS 84 hasn't proven sufficient. Every organization can benefit from geospatial intelligence." — Towards Standardizing Place (2024)

> "If you want to know where the future is being made, look for where language is being invented and lawyers are congregating." — Prompts vs. Context (2025), quoting Stewart Brand

> "We don't own your data, but we try to show it to you in new ways." — On Reporter's philosophy (2014)

## Technical Approach

Breunig's technical work is characterized by:

- **Practical experimentation over theory**: He builds working prototypes (plumb, whenwords, foggy-bot) to explore ideas rather than writing abstract papers.
- **Open source and accessibility**: All his projects are freely available, and he advocates for accessible geospatial data.
- **DuckDB as a primary tool**: He's a vocal DuckDB advocate, using it for geospatial joins, data exploration, and demonstrating accessible analytics.
- **DSPy for LLM applications**: He champions DSPy's philosophy of decoupling tasks from specific models and prompts.
- **Small, focused tools**: Following the "be better, not smaller" philosophy, he builds tools that do one thing well rather than platforms that do everything poorly.
- **Jekyll-powered blog**: His blog runs on Jekyll, deployed on Vercel, with a focus on clean, accessible writing.

## Related

- [[Nicholas Felton]] — Co-founder of Reporter; information designer known for Annual Reports
- [[Overture Maps Foundation]] — Open geospatial data project; Breunig is GERS Evangelist
- [[DSPy]] — Stanford NLP's framework for LLM applications; Breunig is a significant contributor
- [[Context Engineering]] — Discipline Breunig helped name and define
- [[Spec-Driven Development]] — Development paradigm Breunig pioneered with `whenwords`
- [[Recursive Language Models]] — Pattern Breunig implemented in DSPy and advocates
- [[PlaceIQ]] → [[Precisely]] — Location intelligence companies where Breunig worked
- [[Useful Sensors]] — Company Breunig advises on positioning and strategy
- [[cmpnd-ai]] — Company Breunig is associated with

## Sources

- **Blog**: [dbreunig.com](https://www.dbreunig.com/) — Primary source, active since 2010
- **Writing Archive**: [dbreunig.com/writing.html](https://www.dbreunig.com/writing.html) — Complete list of posts
- **GitHub**: [github.com/dbreunig](https://github.com/dbreunig) — 49 public repos, joined 2009
- **LinkedIn**: [linkedin.com/in/drewbreunig](https://linkedin.com/in/drewbreunig) — Career history
- **Mastodon**: [@dbreunig@note.computer](https://note.computer/@dbreunig)
- **Medium**: [medium.com/@dbreunig](https://medium.com/@dbreunig) — 1.2K followers
- **The Verge**: Reporter app coverage (February 2014)
- **FlowingData**: Reporter app review (February 2014)
- **CMS Wire**: "Brands Are Finding Their Way With Location Data" (February 2016)
- **CARTO Blog**: "GERSifying Overture Places" (September 2025) — features Breunig's GERS work
- **cmpnd.ai Blog**: "RLMs in DSPy" — co-authored technical deep dive
- **Databricks Data + AI Summit**: 2025 and 2026 speaking engagements
- **O'Reilly Context Engineering Superstream**: February 2026 presentation
- **MLOps Community**: March 2026 "Coding Agents" conference presentation
- **YouTube**: Video recordings of Breunig's conference talks available
