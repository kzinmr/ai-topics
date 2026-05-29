---
title: Hilary Mason
type: entity
handle: "@hmason"
created: 2026-05-29
updated: 2026-05-29
tags:
  - person
  - ai-agents
  - agent-skills
  - agent-harness
  - entrepreneur
  - founder
  - ceo
  - ai-adoption
  - ai-product
  - youtube
  - blogger
sources:
  - raw/articles/2026-05-15_vanishing-gradients_show-us-your-agent-skills-ep2.md
---

# Hilary Mason (@hmason)

| | |
|---|---|
| **X** | [@hmason](https://x.com/hmason) |
| **Blog** | [hilarymason.com](https://hilarymason.com) |
| **GitHub** | — |
| **Role** | Co-Founder & CEO at Hidden Door; former Data Scientist in Residence at Accel Partners |
| **Known for** | Fast Forward Labs (acquired by Cloudera), HackNY co-founder, Chief Scientist at bitly, narrative AI/world-building at Hidden Door |
| **Bio** | Hilary Mason is a data scientist, entrepreneur, and AI product leader. She was the Chief Scientist at bitly, where she studied attention on the internet in realtime. She founded Fast Forward Labs, an applied machine learning research company acquired by Cloudera in 2017, where she then served as General Manager of Machine Learning. She was Data Scientist in Residence at Accel Partners, advising companies on data strategy. She co-founded HackNY, a non-profit connecting engineering students with NYC's startup community. In 2020, she co-founded Hidden Door, a narrative AI platform for social roleplaying games. |

## Overview

Hilary Mason is one of the most seasoned voices at the intersection of data science, machine learning, and product development. Her career spans from early internet-scale data analysis at bitly to applied ML research at Fast Forward Labs, and now to building a narrative AI gaming platform at Hidden Door. She brings a rare combination of technical depth, product intuition, and philosophical clarity to AI engineering — particularly around how agents can augment creative work rather than replace it.

Mason's background in both computer science and English literature gives her a distinctive perspective on AI. She argues that the machine is not itself creative — creativity comes from humans, and AI's role is to enable and amplify that creativity through structure, iteration, and constraint. At Hidden Door, this philosophy translates into a system where AI acts as a controllable "games master," decomposing storytelling into structured narrative beats while preserving the author's creative vision.

She has been working with language models since well before the ChatGPT moment, and her early advocacy helped many in the data community see the power of generative AI. Her public speaking and writing consistently emphasize the gap between "aspirationally very mid" AI output and the sharp, context-rich prompting needed to achieve greatness.

## Show Us Your (Agent) Skills Episode 2 (2026-05-15)

Hilary appeared on Episode 2 of *Show Us Your (Agent) Skills* to demonstrate how she uses AI agents for creative work at Hidden Door. Her segment spanned roughly 40 minutes (from 40:44 to approximately 1:18:35) and covered both product philosophy and practical agent workflow patterns.

### Core Philosophy: Bringing Science Back Into Engineering

Mason opened by invoking Richard Hamming's distinction between science and engineering:

> "In science, if you know what you're doing, stop. In engineering, if you don't know what you're doing, stop."

She argued that working with agents "is bringing the science back into the engineering and the engineering back into the science." The agent-driven workflow changes her relationship with writing tests, doing product experimentation, and rapid prototyping — making it economically viable to build something just to "develop an opinion about it."

### "Aspirationally Very Mid" — The Problem of Sameyness

Mason identified her core frustration with LLMs: they are "aspirationally very mid." They are biased, same-sy, and default to stereotypes:

> "If you ask it for a doctor, it's always going to give you a man, and it's going to have, you know, maybe an Indian name because it's racist. You're going to see a lot of repeats."

To get from mid to great, you need to bring sharp context and be extremely precise about what you want. She praised the [[entities/hermes-agent]] Superpowers plugin for bringing rigorous process and verification into agent workflows.

### Agentic Loops for Creative Work (Not Software)

Mason's key insight: agentic loops for creative work are fundamentally different from coding loops. The creative agentic loop is:

1. **Interview the creative** — Understand the narrative intent, characters, world rules
2. **Generate variations** — Produce multiple distinct narrative options
3. **Evaluate against editorial criteria** — Score each variation against predefined quality standards
4. **Iterate** — Compare to the baseline eval from the beginning and refine

This is the same structural pattern as coding agents (generate → evaluate → iterate), but applied to narrative rather than code. The evaluation criteria are editorial (character consistency, narrative coherence, emotional impact) rather than functional (tests pass, no bugs).

### Three Variations Pattern

A core Hidden Door design pattern: **always ask for 3+ distinct variations with different magnitudes of change and risk**. One variation is samey; three creates real choice. This mirrors Midjourney's four-image output pattern and aligns with recommendation systems' diversity principles — you sometimes want the top-K that spans the distribution, not just the single best.

### Hermes Agent Harness for Creative Workflows

Mason uses [[entities/hermes-agent]] as her primary agent harness for creative workflows:

- **Slash commands over auto-triggering**: Explicit invocation gives more control than automatic skill matching
- **Deep copy skills**: Skills that clone and adapt — she mentioned a deep copy skill that plays music and actually found a real bug in the process
- **"Gremlins"**: Cron-scheduled agents designed to generate deliberately bad ideas, surfacing edge cases and testing system robustness
- **Justfile orchestration**: Hidden Door heavily uses the Just command runner to orchestrate agent scripts, particularly for background story monitoring via LLM tasks

### CEO Workflow: Scatterbrained Schedule as a Feature

Mason described how agents fit her CEO schedule:

> "I'm a CEO. I have a million bad ideas. My schedule is often going this way and that way. And now I have the tools to set something moving... I can go do something else and I can come back and I can remember where I was and what I was doing without losing the whole thread."

Before agents, she had to block out 2.5 days a week with 4-hour uninterrupted sessions to make meaningful engineering progress. Now she can fit engineering work around meetings — a pattern that resonates with many executives and anyone with fragmented attention.

### Hidden Door Product Context

Hidden Door is a platform where fans roleplay in fictional worlds (books, movies, TV shows). The AI acts as a controllable "games master" that enforces world rules, character behavior, and narrative constraints. Key product principles:

- **The machine is not creative** — creativity comes from authors and narrative designers
- **Structured narrative beats** — stories are decomposed into beats with a database of tropes and world rules
- **Controllability over infinite generation** — players want shared moments to discuss, not infinite unique experiences
- **Author partnerships** — Hidden Door signs agreements with IP holders and collaborates on world adaptations

## Core Ideas

### Narrative AI as Constrained Generation

Mason's philosophy stands in contrast to the "infinite generation" approach common in AI gaming. At Hidden Door, AI doesn't generate freely — it operates within a structured system of narrative beats, world rules, and character constraints. The "world seed" is a ~100-line Python definition file mapping a fictional world into tropes, rules, and narrative patterns. The system checks every player action against world logic: "Is it easy, medium, or hard for this character in this situation? Are we trying to end the scene with a goal in mind?"

### Sharp Context as the Difference Between Great and Mid

The through-line of Mason's agent philosophy: precision in context engineering. "Aspirationally very mid" LLM output is the default. To get great results, you must bring sharp context — whether through structured prompts, evaluation rubrics, or the three-variations pattern. This applies equally to creative work and coding.

### Agents as Organizational Memory

Mason's "scatterbrained schedule" insight points to a broader theme: agents serve as external memory and context-preservation systems. They allow task-switching without the cognitive cost of reloading context. When she asked Claude to find embarrassing things in her transcripts, it returned: "Sometimes I ask 'What were we doing? Why are we here? What did I tell you to get this output?'" — which she found more revealing than embarrassing.

## Key Work

### Hidden Door (2020–present)
A narrative AI platform for social roleplaying games. Fans create characters and play stories in worlds from books, movies, and TV shows. The platform uses AI as a controllable "games master" with structured narrative beats, world rule enforcement, and author partnerships. Backed by Makers Fund, Northzone, Betaworks, and others.

### Fast Forward Labs (acquired by Cloudera, 2017)
An applied machine learning research and consulting startup that produced quarterly reports on emerging ML technologies and built prototypes for clients. Acquired by Cloudera, where Mason became General Manager of Machine Learning.

### Chief Scientist at bitly (2010–2014)
Led the data science team studying attention on the internet in realtime. Worked on spam classification, link analysis, and realtime data processing at internet scale.

### HackNY (co-founder)
A non-profit connecting talented engineering students with NYC's startup community through fellowships, hackathons, and mentorship.

## Related Concepts

- [[entities/hermes-agent]] — Mason's agent harness of choice for creative workflows, particularly slash commands, deep copy skills, and Gremlins
- [[concepts/creative-ai]] — Agentic loops for creative work vs. engineering work
- [[entities/bryan-bischof]] — Fellow Episode 2 guest; both emphasize generating multiple variations and packaging context with content

## Related People

- **Matt Brandwein** — Co-founder and CPO at Hidden Door
- **[[entities/tomasz-tunguz]]** — Fellow Episode 2 guest; General Partner at Theory Ventures
- **[[entities/eric-ma]]** — Fellow Episode 2 guest; Hilary praised Eric's Marimo Pair workflow as an example of bringing science back into engineering
