---
title: "Meta-Meta-Prompting"
aliases: ["Fat Skills Fat Code Thin Harness", "Personal AI OS", "Compound AI System"]
type: concept
created: 2026-05-11
updated: 2026-07-10
tags:
  - agentic-engineering
  - harness-engineering
  - personal-ai
  - workflow
  - multi-agent
  - architecture
related:
  - concepts/harness-engineering
  - concepts/agent-sandboxing
sources:
  - raw/articles/2026-05-09_garrytan_meta-meta-prompting.md
---

# Meta-Meta-Prompting

**Meta-Meta-Prompting** is an AI agent design philosophy proposed by Garry Tan (YC CEO). Rather than writing prompts directly to AI, it is an approach to build a **skill system** and **knowledge graph** that allows the AI to write its own prompts, enabling the entire system to grow compoundingly.

> "I hardly write prompts to AI anymore. What really matters is the skill system." — Garry Tan

## Why "Meta-Meta"?

1. **Level 1: Prompt** — Humans write instructions for AI
2. **Level 2: Meta-Prompt** — AI generates its own prompts (system prompts, chain-of-thought, etc.)
3. **Level 3: Meta-Meta-Prompt** — AI autonomously decides 'when and which skill to use', 'which model to route to', and 'where to integrate results in the knowledge base'

At Level 3, humans no longer write individual prompts. Instead, they build reusable skills that the AI autonomously combines and executes.

## Fat Skills, Fat Code, Thin Harness

Architecture pattern for realizing Meta-Meta-Prompting:

```
┌─────────────────────────────────────────────────┐
│                  Thin Harness                     │
│  ┌─────────────────────────────────────────┐    │
│  │          Router / Orchestrator            │    │
│  │  (OpenClaw, Hermes Agent, Claude Code)   │    │
│  └─────────────────────────────────────────┘    │
│                      │                            │
│         ┌────────────┼────────────┐              │
│         ▼            ▼            ▼              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │  Skill A  │ │  Skill B  │ │  Skill C  │  ...  │
│  │ (meeting) │ │ (enrich)  │ │ (triage)  │        │
│  └──────────┘ └──────────┘ └──────────┘        │
│         │            │            │              │
│         ▼            ▼            ▼              │
│  ┌─────────────────────────────────────────┐    │
│  │            Fat Code / Knowledge           │    │
│  │    (100K pages structured knowledge base)   │    │
│  └─────────────────────────────────────────┘    │
└─────────────────────────────────────────────────┘
```

| Layer | Role | Features |
|----|------|------|
| **Thin Harness** | Routing & orchestration | Lightweight, swappable, general-purpose |
| **Fat Skills** | Reusable workflow modules | Independently testable, composable, accumulates |
| **Fat Code** | Accumulated knowledge, data, and logic | Structured pages per person, company, meeting, book, article |

### Thin Harness Principles

- The harness is only responsible for routing 'which model to use' and 'which skill to call'
- It does not hold business logic or knowledge
- Swappable (Fat Skills survive transitions from Claude Code to Hermes Agent to OpenClaw)

### Fat Skills Principles

- Each skill is **independently testable**
- Skills are **composable** (meeting-ingestion → enrich → investor-update-ingest)
- Once created, skills **accumulate permanently**
- **Skillify** — A meta-skill that auto-converts recurring patterns into skills

## Compound Effect

The greatest value of Meta-Meta-Prompting lies in its **compounding nature**:

```
Week 1:  5 skills,  1,000 pages → Basic meeting summaries
Week 4:  20 skills, 5,000 pages → Begins understanding relationships between people
Week 12: 60 skills, 30,000 pages → Cross-connects past meetings with new books
Week 24: 100+ skills, 100,000 pages → Enables advanced synthesis like Book Mirror
```

- Every book, every meeting, and every skill improvement **accumulates without decay**
- The knowledge base functions as a 'neural system' (dynamic connections, updates, reasoning) rather than a 'file cabinet' (static storage)
- The only AI architecture where **the entire system gets smarter over time**

## Implementation Patterns

### 1. Automatic Knowledge Graph Updates

```yaml
After meeting:
  - Generate transcript
  - Create summary
  - Update person pages (reflect latest statements and interests)
  - Update company pages
  - Update timeline
  - Update open threads
  - Update relationship context
```

### 2. Multi-Model Routing

| Task Type | Model | Reason |
|-----------|--------|------|
| Precision work | Claude Opus 4.7 | Accuracy first |
| Recall & extraction | GPT-5.5 | Search & summarization |
| Creative work | DeepSeek V4-Pro | Divergent thinking |
| Fast inference | Groq + Llama | Latency minimization |
| Routing decisions | OpenClaw / Hermes Agent | Harness layer |

### 3. Skillify — Auto-Skill Creation

```
Human: "skillify this"
System:
  1. Analyze recent operation patterns
  2. Extract reusable workflow
  3. Generate skill file
  4. Register in resolver routing system
  5. Make available for all future workflows
```

## Correspondence with Hermes Agent

Garry Tan's architecture deeply corresponds to Hermes Agent's design:

| Meta-Meta-Prompting | Hermes Agent |
|---------------------|--------------|
| Thin Harness | Hermes Agent core runtime |
| Fat Skills | Skill system (`skill_manage`) |
| Skillify | Auto skill generation (`skill_manage(action='create')`) |
| Knowledge Graph | wiki (structured knowledge base) |
| Multi-model routing | Multi-provider support |
| 100+ skills | All available skills |
| ~100K pages | wiki entity and concept pages |

## References

- Garry Tan. "Meta-Meta-Prompting: The Secret to Making AI Agents Work" (2026-05-09). X Article. [[raw/articles/2026-05-09_garrytan_meta-meta-prompting]]
- Garry Tan. "Fat Skills, Fat Code, Thin Harness" (preceding article in series). [[entities/garry-tan]]
- YC Lightcone Podcast. "Tokenmaxxing: How Top Builders Use AI To Do The Work Of 400 Engineers" (2026-05-08)

