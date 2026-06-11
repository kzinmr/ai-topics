---
title: "peoplereadmes"
created: 2026-05-17
updated: 2026-05-17
type: concept
tags:
  - agent-skills
  - context-engineering
  - evaluation
  - open-source
  - ai-agents
sources:
  - https://github.com/muratcankoylan/peoplereadmes
  - https://raw.githubusercontent.com/muratcankoylan/peoplereadmes/main/README.md
related:
  - riley-walz
  - muratcan-koylan
  - agent-skills
  - context-engineering
---

# peoplereadmes

**peoplereadmes** is an open-source framework by [[muratcan-koylan|Muratcan Koylan]] for creating structured "persona context systems" — research artifacts that help humans and AI agents understand how exceptional technical builders operate. It is explicitly NOT a celebrity chatbot or impersonation project. The goal is to extract transferable knowledge from observable professional patterns.

The first persona package is `personas/riley-walz/`, modeling the public professional patterns of [[riley-walz]].

## Core Premise

Most "persona" systems are shallow: they collect biographical facts, summarize tone, and ask an LLM to imitate a person. peoplereadmes takes a fundamentally different approach — it treats **observable professional patterns** as the unit of study, not the person.

The useful output is not a clone of a person, but a **structured model of how they work**:
- How they notice opportunities
- How they choose projects
- How they compress complex ideas into public artifacts
- How they use tools, APIs, data, hardware, or interfaces
- How they launch, explain, and archive work
- Which risks and ethical boundaries repeat

## Pipeline

```
public evidence → source map → project analysis → tacit-knowledge extraction → technical model → prompt system → eval rubric → reusable context package
```

### 1. Public Evidence
Collection of all publicly available material: projects, interviews, talks, social media posts, code repositories, and media coverage. Only public, verifiable sources are used.

### 2. Source Map
Organization of evidence into a structured map connecting claims to their sources. Each claim is linked to specific research runs and source tiers (primary, secondary, tertiary).

### 3. Project Analysis
Systematic examination of multiple projects to identify recurring patterns, technical defaults, and decision-making heuristics. For Riley Walz, this surfaced the "public data seam → thin interface → sharp hook → institutional reaction → methodology archive" pattern.

### 4. Tacit-Knowledge Extraction
Surfacing knowledge that the subject demonstrates in practice but may not have explicitly articulated — technical instincts, taste judgments, framing strategies, and risk assessment patterns.

### 5. Technical Model
A structured representation of the subject's technical approach: preferred tools, API usage patterns, data handling defaults, launch strategies, and documentation habits. Machine-readable where possible (JSON schemas, heuristics catalog).

### 6. Prompt System
Agent prompts that instruct LLMs on how to use the context without impersonating the person. Includes system prompts for standard use, deep-context prompts for detailed analysis, and explicit safety boundaries.

### 7. Eval Rubric
Evaluation rubrics that test whether generated outputs are:
- **Faithful** — grounded in evidence, not fabricated
- **Useful** — actionable for creative or technical work
- **Safe** — within defined ethical boundaries
- **Evidence-bound** — claims linked back to sources

### 8. Reusable Context Package
The final deliverable: a self-contained directory that can be loaded by humans or AI agents to understand how a particular builder operates. Designed to be version-controlled, shareable, and composable.

## What It Is NOT

The repo explicitly prohibits:
- Speaking as another person
- Claiming endorsement, affiliation, or access to private thoughts
- Inferring private psychology, relationships, or communications
- Building doxxing, harassment, or credential misuse workflows
- Treating "publicly accessible" as automatic ethical permission

Every persona package preserves the **difference between evidence, interpretation, and generated inspiration**.

## Repository Structure

```
personas/
  riley-walz/
    README.md              — Package overview and load order
    context/
      context-pack.md      — Compact default context for agent use
      brain-model.md       — Long-form professional pattern model
      idea-engine.md       — Idea discovery and project selection
      taste-and-voice.md   — Taste, framing, naming, likes/dislikes
      technical-playbook.md — Technical defaults summary
      advanced-technical-intelligence.md — API/data-seam instincts
      safety-boundaries.md — Hard boundaries
    data/
      projects.json         — Project catalog
      heuristics.json       — Machine-readable heuristics
      technical-ability-model.json — Structured ability analysis
      quote-bank.json       — Direct public quotes
      evidence-map.json     — Claims-to-sources mapping
    prompts/
      system-prompt.md      — Standard agent prompt
      deep-context-system.md — Full deep-context prompt
    evals/
      rubric.md             — Output quality evaluation
      brain-model-rubric.md — Brain model evaluation
    research/
      deep-dive/            — Raw deep research outputs
schemas/
  persona.schema.json       — Formal schema for persona packages
agents/
  project-navigator-agent.md — Agent for navigating project data
```

## Why This Approach Matters

The peoplereadmes framework addresses a gap in how the AI community studies creative and technical excellence:

1. **Beyond biography**: Traditional profiles capture who someone is and what they've done. peoplereadmes captures **how** they do it — the repeatable patterns, heuristics, and technical instincts.

2. **Agent-native format**: The output is designed to be consumed by AI agents, not just humans. Machine-readable data files, structured prompts, and eval rubrics make the knowledge actionable.

3. **Safety by design**: By focusing on observable professional patterns rather than personality simulation, the framework avoids the ethical pitfalls of persona cloning while still extracting useful knowledge.

4. **Cumulative knowledge**: Each persona package adds to a growing library of structured knowledge about how exceptional builders operate — patterns that can be compared, contrasted, and synthesized.

## Relationship to Agent Skills

peoplereadmes is a natural extension of Koylan's work on [[concepts/agent-skills|Agent Skills for Context Engineering]]. While Agent Skills provides reusable operational patterns for AI agents, peoplereadmes provides reusable **creative and technical patterns** extracted from studying exceptional builders. Both share the same underlying philosophy: structured, filesystem-based knowledge that both humans and agents can use.

## Current Status

As of May 2026, peoplereadmes is in early development with one complete persona package (Riley Walz). The framework, schemas, and evaluation methodology are designed to scale to additional subjects.

## Related Pages

- [[riley-walz]] — First peoplereadmes persona study subject
- [[muratcan-koylan]] — Creator of the peoplereadmes framework
- [[concepts/agent-skills]] — Koylan's broader Agent Skills framework (15.6k stars)
- [[concepts/context-engineering|Context Engineering]] — The discipline that underpins both Agent Skills and peoplereadmes
- [[concepts/evaluation/llm-as-judge-skills]] — Koylan's evaluation skills used in peoplereadmes eval rubrics

## Sources

- [peoplereadmes GitHub repository](https://github.com/muratcankoylan/peoplereadmes)
- [peoplereadmes README (raw)](https://raw.githubusercontent.com/muratcankoylan/peoplereadmes/main/README.md)
- [muratcankoylan.com](https://muratcankoylan.com)
- [muratcankoylan.com/for-agents](https://muratcankoylan.com/for-agents)
