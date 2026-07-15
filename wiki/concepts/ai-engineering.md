---
title: "AI Engineering"
type: concept
created: 2026-04-25
updated: 2026-07-15
tags:
  - ai-agents
  - ai-software-engineering
  - event
sources:
  - raw/newsletters/2026-07-14-5-trends-that-defined-ai-engineering-at-world-s-fair-2026.md
status: complete
---

# AI Engineering

## Overview

AI engineering has matured dramatically from the 'prompt engineering' era of 2023 to a full-fledged engineering discipline by 2026. The term was coined by [[entities/swyx]] in June 2023 to describe a new kind of developer emerging from the LLM revolution. By 2026, the AI Engineer World's Fair showed the field concentrating on building reliable systems, orchestrating agents, managing context, evaluating outputs, and integrating AI into production software.

## Five Trends Defining AI Engineering in 2026

### 1. From Agent Autonomy to Harness Engineering

[[entities/lilian-weng]]'s essays illustrate this shift. Her influential 2023 article 'LLM Powered Autonomous Agents' described agent anatomy in terms of planning, memory and tool use — with AutoGPT and BabyAGI as exemplars. Her 2026 essay 'Harness Engineering for Self-Improvement' argues the system surrounding the model — the harness managing workflows, context, permissions, evaluation, persistent state and continuous improvement — has become equally important. At AIEWF 2026, AutoGPT was barely mentioned; the conversation focused on Claude Code, Codex, Gemini CLI, Cursor, Warp and the infrastructure for dependable production agents.

### 2. Loop Engineering

The dominant design pattern at AIEWF 2026 was the **inner/outer loop** separation:

- **Inner loop**: The primary system interacting with users and performing work, largely autonomous
- **Outer loop**: Human oversight, feedback signals, evals, and strategic direction

[[entities/addy-osmani]]: 'Agents can run much more of the inner execution loop, but that outer loop is still engineering.' [[entities/peter-steinberger]] (OpenClaw creator): 'The agent runs the inner execution loop; I set the direction and I make decisions in the outer loop.' Roland Gavrilescu (Introspection CEO): 'You can think of the system as having an inner loop and an outer loop.'

Dex Horthy (HumanLayer) cautioned that 'the hype is outrunning the discipline' — control loops work in systems like Kubernetes because they're deterministic, unlike LLM agent loops.

### 3. Forward Deployed Engineers and Software Factories

Enterprises are adopting AI through **Forward Deployed Engineers (FDEs)** who work directly with organizations to implement AI capabilities. [[entities/natalie-meurer]] (Sierra): 'Every enterprise we work with wants to know how it can maintain everything its agentic ecosystem is capable of doing.'

[[entities/pauline-brunet]] (Cursor): FDEs deploy cloud agents, long-running agents, automations, and applications built on the Cursor SDK — ensuring strict ROI so clients don't 'turn things off when we leave.'

**Software factories**: Long-running agents working throughout the entire software lifecycle. [[entities/zach-lloyd]] (Warp CEO) explains organizations must 'choose your repositories, the parts of the software lifecycle you want to automate, and the points where humans should be brought into the loop.' Warp's platform 'Oz' implements this model.

[[entities/andrew-qu]] (Vercel): 'Agents are not as predictable as web applications. The infrastructure can look similar, but the interaction, interface and outputs are much more dynamic.' Vercel released 'eve' as an agent framework comparable to Next.js.

### 4. Context Engineering

[[entities/prukalpa-sankar]] (Atlan) introduced 'context engineering' as a discipline: understanding 'how context flows from your business systems into a shared company brain, then out to agents, copilots, and apps through MCP, APIs, and retrieval.' Enterprise adoption remains concentrated among early adopters — finding 'the right champions inside an organization' is a key challenge for FDEs.

### 5. Skill Engineering

[[entities/anthropic]] popularized 'agent skills' for Claude in October 2025. [[entities/addy-osmani]]: skills 'encode the workflows, quality gates, and best practices that senior engineers use when building software.'

Philipp Schmid (Google DeepMind): 'Agents are just files. We write markdown files to extend capabilities.' Skills reduce the need for orchestration code previously written in Python.

[[entities/paul-bakaus]] created Impeccable, an open-source design skills system, and advocates for 'skill engineering' as a discipline. He warns that most skills and models 'converge in one direction — if everybody uses the same skill everything ends up looking the same.'

Matt Pocock warns of 'skills hell' — comparable to framework hell — advising fewer and smaller skills with more thought into structure.

Y Combinator president [[entities/garry-tan]]: 'The AI native companies that I see inside YC encode all of that as skills, written procedures that their agents execute.'

Tyler Brown: 'Autonomy without structure creates as much slop as leverage. Each time there's a new model release, it's as if you have a kid that grows from middle school to high school. You have to change the curriculum.'

## Key Takeaways

- Complete agent autonomy is neither reliable nor desirable at scale — agents augment engineers, not replace them
- The field has moved from 'can agents work?' to 'how do we build reliable systems around them?'
- Agent-native interfaces (agents as files, Markdown-based skills, declarative workflows) are replacing traditional orchestration code
- The human engineer's role is the outer loop: setting direction, evaluating outputs, and maintaining skills
- AI engineering describes where software engineering is heading, not just a new job title

## Related Pages

- [[events/ai-engineer-worlds-fair-2026]]
- [[concepts/ai-agent-engineering]]
- [[concepts/agentic-engineering]]
- [[concepts/harness-engineering]]
- [[entities/swyx]]
- [[entities/richard-macmanus]]
- [[concepts/coding-agents]]
