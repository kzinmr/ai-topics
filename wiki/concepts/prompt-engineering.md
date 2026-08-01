---
title: "Prompt Engineering"
type: concept
aliases:
  - prompt-engineering
  - prompting
  - end-of-prompting
created: 2026-04-25
updated: 2026-08-01
tags:
  - concept
  - prompting
  - agentic-engineering
  - agent-skills
  - computer-use
  - screen-recording
sources:
  - raw/newsletters/2026-07-31-the-end-of-prompting.md
  - https://thesignal.substack.com/p/the-end-of-prompting
---

# Prompt Engineering

**Prompt engineering** is the practice of crafting natural-language instructions ("prompts") to elicit desired outputs from LLM-based AI systems. Since ChatGPT's November 2022 launch made prompting mainstream, it has been the dominant human-AI interaction paradigm: *you get good output by being good at describing what you want.*

As of July 2026, that paradigm is being challenged by **demonstration-based interaction** — teaching AI by showing it a task once, rather than by writing instructions. Both OpenAI and Anthropic shipped "record a workflow" features within five weeks of each other, and AI-industry observers argue this marks the beginning of the end of prompting as the primary interface.

## The Paradigm Shift: From Description to Demonstration

### What a Prompt Leaves Out

A written prompt is a description of a task reconstructed from memory. It captures *what* the user thinks matters, but misses the tacit knowledge that lives in the doing:

- The **order** of operations
- The **pauses** and **corrections** made along the way
- The **reasoning** voiced at each fork in the road ("why I did it this way")

> "Working knowledge lives in the doing. Show, don't tell is how people have taught work for hundreds of years, and until last week, a written text instruction was the only thing you could give Claude." — Alex Banks, The Signal (Jul 31, 2026)

Skills built from written descriptions have therefore been "useful for basic input-output-driven tasks, but miss the mark on anything more complex."

### Record a Skill (Anthropic) & Record & Replay (OpenAI)

| | **Record & Replay** (OpenAI) | **Record a skill** (Anthropic) |
|---|---|---|
| **Release** | June 18, 2026 (Codex + ChatGPT desktop) | July 21, 2026 (Claude desktop, Cowork mode) |
| **What it records** | Screen, actions, window content | Screen, clicks, typing, **voice** |
| **Output** | Inspectable, editable skill | Slash command runnable from any chat |
| **Availability** | macOS only; excludes EEA, UK, Switzerland at launch | Gradual rollout; no published regional restriction (confirmed working in UK) |

The voice difference matters: OpenAI's recorder observes *actions* but not narration, while Anthropic's version listens. Per The Signal's analysis, "Clicks show what you do, but your commentary carries the context for why you did it."

**Kiana Ehsani** (Anthropic, acquired via Vercept) articulated the design philosophy behind the shift:

> "People should not have to write prompts! People should not have to think about what they can / can not delegate." — @ehsanik (Jul 21, 2026)

### Why Both Labs Converged

The recordings serve a dual purpose:

1. **User-facing**: They turn a one-time demonstration into a repeatable skill — the same uplift as Excel's macro recorder (available since the early 1990s).
2. **Lab-facing**: "For the labs building computer-use agents, demonstrations of real people doing real work are the most valuable training material there is — and these recorders turn their everyday users into a willing supply of it."

The pattern follows Atlassian's ~$975M acquisition of Loom (Oct 2023) — recording so others can watch how something gets done — taken one step further: the AI studies the recording and performs the task itself.

### First-Mover Reversal

Anthropic historically shipped interface ideas first (MCP Nov 2024 → OpenAI adopted Mar 2025; computer use Oct 2024 → Operator three months later; prompt caching Aug 2025; Projects and Artifacts before ChatGPT equivalents; Cowork → ChatGPT Work). The recorder is a notable exception: **OpenAI shipped Record & Replay 33 days before Anthropic's Record a skill** (June 18 vs July 21), though Anthropic's announcement drew ~11M views vs OpenAI's 4.6M.

## Counter-Arguments & Tensions

- **Handing labs your working methods**: Alex Karp has made "the strongest case against handing any AI lab your working methods" — recording your workflows means feeding proprietary process knowledge into a model owned by a lab.
- **Interface skepticism**: The article series acknowledges the open question of which tasks genuinely fit demonstration-based setup vs. which still require explicit instruction.
- **Prompts are not obsolete**: Prompt engineering remains the interface for one-off tasks, structured data extraction, and cases where no demonstration is available.

## Implications for the Wiki's Agentic Engineering Taxonomy

This development bridges [[concepts/agentic-engineering]] (how humans use agents — the shift from writing prompts to showing workflows) and [[concepts/agent-skills]] (skills as the durable artifact of demonstration). It also connects to [[concepts/computer-use]] (the substrate the recorders observe) and the screen-recording workflow tools (Loom, Excel macro recorder) that pioneered the pattern.

## Related Pages

- [[concepts/prompt-design]] — Prompt design, instruction fine-tuning, and system prompt engineering
- [[concepts/agentic-engineering]] — How humans work with agents
- [[concepts/agent-skills]] — Skills as repeatable agent capabilities
- [[concepts/computer-use]] — Computer-use agents as the substrate for recorded workflows
- [[concepts/prompt-caching]] — Prompt economics (adjacent to the price-war context of July 2026)
- [[entities/anthropic]] / [[entities/openai]] — The two labs racing on this interface
- [[concepts/resilient-prompt-engineering]] — Defensive prompt practices
- [[concepts/prompt-debt]] — Why written prompt collections degrade over time

## Open Questions

- Will demonstration-based skills replace prompt libraries as the primary knowledge artifact for AI users?
- How do recorded skills generalize across environments (desktop apps, web, CLI)?
- What are the privacy/competitive implications of labs collecting user workflow recordings at scale?
- Does voice narration become a first-class input modality for skill definition across all labs?
