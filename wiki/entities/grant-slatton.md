---
title: Grant Slatton
type: entity
created: 2026-04-27
updated: 2026-04-27
tags:
  - person
  - x-account
  - ai
  - aws
  - s3
  - row-zero
  - shardstore
  - formal-methods
  - spreadsheets
  - systems-engineering
  - rust
sources:
  - https://grantslatton.com/
  - https://x.com/GrantSlatton
  - https://www.linkedin.com/in/grant-slatton
  - https://dl.acm.org/doi/10.1145/3477132.3483540
---

# Grant Slatton (@GrantSlatton)

| | |
|---|---|
| **X/Twitter** | [@GrantSlatton](https://x.com/GrantSlatton) |
| **Blog** | [grantslatton.com](https://grantslatton.com/) |
| **Role** | Founding Engineer at Row Zero |
| **Formerly** | Senior Engineer, AWS S3 |
| **Location** | Seattle, WA |
| **Joined X** | April 2011 |
| **X Followers** | ~21K |

## Bio

Grant Slatton is a Seattle-based software engineer and systems thinker known for his work on high-performance distributed systems and his influential writing on AI tooling, organizational dynamics, and post-AI economics. He led the team that built **ShardStore** — the custom high-performance storage node at the heart of AWS S3, the world's largest cloud storage service — and is now a founding engineer at **Row Zero**, building what he describes as the world's fastest spreadsheet.

Slatton gained widespread public attention in March 2025 when his tweet showing an AI-generated Studio Ghibli-style portrait of his family went viral, sparking a global trend that became one of the defining internet moments surrounding OpenAI's upgraded image-generation tools. The post accumulated over 46 million views and 44,000 likes.

Outside of engineering, Slatton is an avid woodworker, trains Brazilian Jiu-Jitsu (BJJ), and maintains a prolific personal blog covering topics ranging from AI economics and bureaucratic theory to urbanism, programming language design, and Japanese travel.

## Career Timeline

| Period | Role | Organization | Key Contributions |
|---|---|---|---|
| ~2015–2020 | Senior Engineer, S3 | Amazon Web Services | Led the team that designed and built **ShardStore**, AWS S3's custom key-value storage node; co-authored SOSP 2021 paper on lightweight formal methods |
| 2020–present | Founding Engineer | Row Zero | Building the world's fastest spreadsheet for modern cloud data |

## Core Ideas & Thought Leadership

### AI Inflection Point ("The Curve is Bending")

Slatton's most widely discussed essay (April 2025) argues that AI models crossed a critical threshold in late 2024/early 2025 where their output became **professionally net-positive** for real development work. Key observations:

- **Inference spend escalation**: $100/yr (2023, GitHub Copilot) → $250/yr (2024, ChatGPT Plus) → ~$5,000/yr (2025, ChatGPT Pro + Claude Code)
- **o1-pro** was the first model he found *professionally useful* — capable of coding at the level of a junior engineer for single-file tasks
- Runs **parallel Claude Code sessions** (up to 3 instances simultaneously) treating each as a separate developer, merging via GitHub
- Measured a **~10% personal productivity gain** in Q1 2025 from AI tools
- Predicts code-writing agents will match college graduates in most software tasks by **end of 2026**
- Estimates companies will spend **$10K–$50K per developer per year** on AI inference by late 2025

### Technocapital (Post-AI Economics)

In this essay (February 2025), Slatton explores the implications of autonomous AI entities that operate as pure capital-maximizing agents:

- A "technocapital entity" is defined by its goal: harnessing more energy and matter to power intelligence, which in turn harnesses more energy and matter
- Such entities can be **unilaterally created** — a program with human-level AI given financial resources and a goal function
- Argues that humanity's role in such a future is bounded: all abundance is downstream of **capital ownership**, not labor
- Human labor, even if free, eventually becomes economically inferior to AI labor due to opportunity cost
- The end-state resembles an entity whose probes colonize star systems, converting matter into computation — with no meaningful role for humanity

### Bureaulogy (The Study of Bureaucracy)

A December 2024 essay analyzing why bureaucracies inevitably form in organizations and how to slow the process:

- **Dunbar's Number** (~150) — bureaucratic tendencies accelerate rapidly once organizations exceed this threshold
- **Upside-Downside Asymmetry** — losses hurt individual status 4× more than gains help it, causing risk-averse process creation
- **Selection Effects** — "When you create promotion checklists, you attract the kind of person who wants to follow a promotion checklist. Bureaucracy begets bureaucracy."
- Prescribes: minimizing headcount, aggressive firing of low-performers, **Directly Responsible Individual (DRI)** ownership model, and vibes-oriented promotion processes over checklists

### Sports vs Games (Aesthetic Distinction)

An essay (September 2024) distinguishing **sports** (rooted in fundamental human activities like running, fighting, climbing) from **games** (contrived, technique-specific). Proposes rule tweaks to combat sports to make them more realistic without losing their identity.

### Claude Code Workflows

Slatton is a prolific practitioner and advocate of Claude Code, writing a comprehensive guide (May 2025) on tips and tricks:

- **Context gathering workflow** using `ripgrep` to identify all types, functions, and modules before acting
- **CLAUDE.md adherence hack** — first line instructs Claude to echo back the file contents in every response
- **Caching context** in `claude/` directories for project-specific knowledge
- **Avoiding compaction** — breaking changes into pieces that fit within Claude's 200K token window
- **Meta-automation** — workflow files in `claude/workflows/` that Claude executes on command

## Projects

### ShardStore (AWS S3)

Slatton led the team that designed, built, and owned **ShardStore**, the custom high-performance key-value storage node at the center of AWS S3. ShardStore is a ~40,000 line Rust implementation that replaced the previous storage node generation.

**Key highlights:**
- Co-authored the SOSP 2021 paper *"Using Lightweight Formal Methods to Validate a Key-Value Storage Node in Amazon S3"* (ACM SIGOPS 28th Symposium on Operating Systems Principles)
- The paper reports on applying **lightweight formal methods** (model checking, conformance checking, crash consistency validation) to a production storage system under active development
- The approach prevented **16 issues from reaching production**, including subtle crash consistency and concurrency bugs
- Co-developed **Shuttle**, a concurrency checker library used to verify the filesystem's correctness
- The project is an influential case study in applying formal verification to real-world production systems

### Row Zero

Slatton is a founding engineer at **Row Zero**, a next-generation spreadsheet designed for modern cloud data workloads. The product positions itself as "the fastest spreadsheet in the world," targeting data-intensive users who have outgrown traditional spreadsheet tools.

**Key highlights:**
- Built for real-time collaboration on large cloud datasets
- Backend engineering team includes several former AWS S3/ShardStore colleagues
- Pairs with cloud data warehouses and data lakes
- Uses **lightweight property-based testing** for correctness verification

## X Activity Themes

Slatton's X presence (@GrantSlatton, joined April 2011, ~21K followers) spans several recurring themes:

### AI & Software Engineering
- Extensive hands-on coverage of **Claude Code** workflows, tips, and critiques
- Commentary on **AI coding agents**, parallel development, and the future of junior vs. senior developers
- Observations on AI inference pricing, model capability thresholds, and the Jevons paradox applied to AI compute
- Evaluation of models: o1-pro, Claude 3.7 Sonnet, DeepSeek R1, Gemini 2.5 Pro, Grok 3

### Viral AI Culture
- March 2025: Started the global **Ghibli-style AI image trend** with a family photo — became the face of the OpenAI image-generation explosion
- Post caption: *"tremendous alpha right now in sending your wife photos of y'all converted to studio ghibli anime"* — 44K likes, 46M+ views

### Systems & Infrastructure
- Deep technical takes on distributed systems, storage infrastructure, and Rust programming
- Meta-commentary on engineering culture, bureaucracy, and organizational design

### Urbanism & Travel
- Essays on urban design (e.g., "Road Width Extremism" — in favor of narrow roads)
- Frequent posts about Japan: language, travel experiences, and cultural observations

### Personal Interests
- Brazilian Jiu-Jitsu training and technique discussions
- Woodworking projects
- Corgi ownership and Seattle neighborhood walks with family

## Publications

| Year | Title | Venue | Role |
|---|---|---|---|
| 2021 | [Using Lightweight Formal Methods to Validate a Key-Value Storage Node in Amazon S3](https://dl.acm.org/doi/10.1145/3477132.3483540) | SOSP '21 | Co-author, lead engineer of ShardStore |

## Notable Blog Posts

| Date | Title | Topic |
|---|---|---|
| 2026-02-08 | [Every Man a Microservice — Contra Conway](https://grantslatton.com/every-man-a-microservice) | Software architecture, Conway's Law |
| 2026-01-31 | [Manufacturing as Maintenance](https://grantslatton.com/manufacturing-as-maintenance) | Engineering philosophy |
| 2025-05-19 | [LLM Memory — Some thoughts on implementations](https://grantslatton.com/llm-memory) | AI systems, memory architectures |
| 2025-05-11 | [Claude Code — Everything I know about how to use it, so far](https://grantslatton.com/claude-code) | AI coding agents |
| 2025-04-25 | [Solution-space Taste](https://grantslatton.com/solution-space-taste) | Software design aesthetics |
| 2025-04-05 | [The Curve is Bending](https://grantslatton.com/the-curve-is-bending) | AI inference costs, productivity |
| 2025-02-06 | [Technocapital](https://grantslatton.com/technocapital) | Post-AI economics |
| 2025-02-01 | [Writing a good design document](https://grantslatton.com/writing-a-good-design-document) | Engineering process |
| 2024-12-21 | [Bureaulogy](https://grantslatton.com/bureaulogy) | Organizational theory |
| 2024-10-19 | [Portals are Undertheorized](https://grantslatton.com/portals-are-undertheorized) | User experience, architecture |
| 2024-09-26 | [Sports vs Games](https://grantslatton.com/sports-vs-games) | Aesthetic philosophy |
| 2024-09-04 | [Lightweight property-based testing at Row Zero](https://grantslatton.com/lightweight-property-based-testing) | Software testing |
| 2024-09-01 | [Rust Macros: Zero to Hero](https://grantslatton.com/rust-macros-zero-to-hero) | Rust programming |
| 2024-08-17 | [Algorithms we develop software by](https://grantslatton.com/algorithms-we-develop-software-by) | Software methodology |
| 2024-07-01 | [Shuttle — A concurrency checker](https://grantslatton.com/shuttle) | Formal methods, concurrent systems |

## Related Entities

- [[entities/claude-code|Claude Code]] — AI coding agent Slatton extensively uses and writes about
- [[entities/boris-cherny|Boris Cherny]] — Creator of Claude Code
