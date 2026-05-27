---
title: "Garry Tan"
aliases: ["@garrytan"]
type: person
x_handle: garrytan
x_id: "11768582"
created: 2026-05-11
tags:
  - personal-ai
  - agentic-engineering
  - harness-engineering
  - ai-agents
  - workflow
roles:
  - President & CEO, Y Combinator (2023–present)
  - Co-founder, Initialized Capital (2015–2023)
  - Partner, Y Combinator (2011–2015)
  - Co-founder, Posterous (2008–2012)
  - Early employee, Palantir Technologies
education:
  - BS Computer Systems Engineering, Stanford University
related:
  - entities/openclaw
  - entities/hermes-agent
  - concepts/meta-meta-prompting
  - concepts/harness-engineering
sources:
  - raw/articles/2026-05-09_garrytan_meta-meta-prompting.md
  - https://en.wikipedia.org/wiki/Garry_Tan
  - https://www.ycombinator.com/people
---
---
---

# Garry Tan

Garry Tan (@garrytan) is the President & CEO of Y Combinator. A venture capitalist with an engineering and design background, he is known for advocating **Personal AI OS** and **Meta-Meta-Prompting** in the AI agent era.

## Career

| Period | Role |
|------|------|
| 2005–2008 | Microsoft → Palantir Technologies (10th employee, designer & engineering manager) |
| 2008–2012 | Co-founded Posterous (YC S08, acquired by Twitter for $20M in 2012) |
| 2011–2015 | Y Combinator Partner (built Bookface & Demo Day sites) |
| 2013– | Co-founded Posthaven |
| 2015–2023 | Co-founded Initialized Capital, Managing Partner |
| 2023–present | Y Combinator President & CEO |

## As an AI Builder

Tan emphasizes being an active builder despite being a VC, known as a **CEO who codes late into the night**.

### G Stack

An AI agent system he personally developed beyond YC's scope. Built on Claude Code, it has the following capabilities:

- `/office-hours` — Skill simulating YC's founder evaluation process
- AI engineering team from product scoping to deployment
- Structured processes, defined roles, rigorous review

### Meta-Meta-Prompting Framework (May 2026)

An AI agent design philosophy advocated in a long-form X Article published on May 9, 2026. See [[concepts/meta-meta-prompting]] for details.

**Core Thesis**:
- The era of writing prompts for AI is over; it's time to build **skill systems**
- **Fat Skills, Fat Code, Thin Harness** — Keep harness thin, skills and knowledge thick
- Models are the engine; true value lies in knowledge, workflows, and data
- Personally operating 100+ AI skills and an ~100,000-page knowledge base
- **Skillify** — A meta-skill that automatically skillifies recurring workflows

### Preceding Article: "Fat Skills, Fat Code, Thin Harness"

An article preceding Meta-Meta-Prompting that explains the basic principles of harness architecture.

### Multi-Model Strategy

| Model | Use |
|--------|------|
| Claude Opus 4.7 | Precision work |
| GPT-5.5 | Recall & extraction |
| DeepSeek V4-Pro | Creative work |
| Groq + Llama | Fast inference |
| OpenClaw + Hermes Agent | Routing |

### Key Skills

- `meeting-ingestion` — Automatic meeting capture & structuring
- `media-ingest` — Media content ingestion
- `enrich` — Existing knowledge base enrichment
- `perplexity-research` — Research investigation
- `investor-update-ingest` — Investor update processing
- `email-triage` — Automatic email sorting
- `calendar-check` — Calendar management
- `Skillify` — meta-skill (automatic workflow skillification)

## Relationship with Hermes Agent

Garry Tan's system **uses OpenClaw and Hermes Agent as the routing layer**. His "Fat Skills, Fat Code, Thin Harness" architecture corresponds to Hermes Agent's design philosophy as follows:

| Tan's Concept | Hermes Agent Implementation |
|-----------|----------------------|
| Thin Harness | Core runtime |
| Fat Skills | Skill system |
| Skillify | `skill_manage(action='create')` |
| Knowledge Graph | wiki |
| Multi-model routing | Multi-provider support |

## Reference Links

- X: [@garrytan](https://x.com/garrytan)
- Y Combinator: [ycombinator.com](https://www.ycombinator.com/)
- Wikipedia: [Garry Tan](https://en.wikipedia.org/wiki/Garry_Tan)
- YouTube: [Garry Tan](https://www.youtube.com/@garrytan) — Educational startup strategy content
