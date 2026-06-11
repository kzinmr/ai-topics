---
title: Agent Productivity and Cognitive Effects
created: 2026-06-01
updated: 2026-06-01
type: concept
tags:
  - concept
  - coding-agents
  - agent-ergonomics
  - psychology
  - mental-health
  - developer-tooling
sources:
  - raw/articles/simonwillison.net--2026-may-31-the-solution-might-be-cancelling-my-ai-subscript--a94e18e9.md
---

# Agent Productivity and Cognitive Effects

## Overview

The impact of AI coding agents on personal productivity is complex and varies dramatically across individuals. While agents can accelerate development 10-100x on specific tasks, they also introduce new failure modes — particularly for neurodivergent users — around project proliferation, attention fragmentation, and unsustainable reward cycles.

## The "Project Proliferation Syndrome"

David Wilson (May 2026) describes a pattern common among heavy AI agent users:

> "I didn't mean to build most of these things. Usually the Claude session started with something like 'write a quick script for X', and one hour later the result is not a quick script for X."

Wilson listed 16+ projects spun up with AI tooling, none of which were maintained. The core dynamic: AI agents lower the activation energy from "idea" to "working project with tests and docs" to under an hour, creating an unsustainable rate of project creation.

> "Even if the code is rock solid, there's a limit to how many projects like that I can sensibly care for — and if they're instantly abandoned, what value was there from creating them in the first place?" — Simon Willison

## The "Thermonuclear ADHD Amplifier"

David Wilson's metaphor captures a widely-reported experience:

> "This technology is horrific for attention. It's a thermonuclear ADHD amplifier and I have seen the same effect in every single one of my adult friends. Folk running 3 screens simultaneously working on totally unrelated 'projects' they have little hope of maintaining."

The cheap reward cycle — minimal input + minimal friction → finished project → dopamine — creates a feedback loop that's particularly problematic for users prone to hyperfocus or novelty-seeking.

## The ADHD Spectrum: Opposite Reactions

The Hacker News thread on Wilson's post revealed a stark split among users with ADHD:

### Agents as Catastrophic

> "A tool producing a cheap reward with minimal input and no friction can only be a liability, and achieving that realisation is probably the only real contribution of AI to date." — David Wilson

### Agents as Liberating

> "For me (also ADHD) it's kind of the opposite. I'm finishing side projects for the first time ever because I can actually get them working before I get bored of them."

> "I used to listen to intense EDM while working. Now I sit in silence and talk to my agents. I maintain inbox zero. I absorb and comment across all relevant projects, even outside my team. I literally feel like I have a support team for the first time."

> "For those of us prone to hyperfocus, working with AI can provide the kinds of stimulation we crave. I can hardly remember a time when I've felt more engaged with my work, more productive, and more badass."

## The Discipline Question

Both Wilson and Willison converge on a single critical skill: **discipline**. Wilson's conclusion:

> "I have no idea how to manage AI at present except by curtailing use."

Willison's response:

> "I'm hopeful that the critical skill to develop here is discipline. That's not great news for me: I've been trying to figure that one out for decades!"

## Implications for Agent Design

This tension suggests several design principles for coding agents:

1. **Friction-injection** — Agents should introduce intentional friction for high-cost actions (creating new projects, spawning new repositories)
2. **Project lifecycle awareness** — Agents could help users close abandoned projects rather than only spawning new ones
3. **Attention management** — Session limits, focus modes, and completion-first workflows
4. **Individual differences** — The same tool that destroys focus for one user enables it for another — personalization matters

## Related Concepts

- [[vibe-coding]] — The paradigm of describing code rather than writing it
- [[agentic-engineering]] — Disciplined use of AI agents for software development
- [[ai-agent-architecture]] — How agent architecture affects user experience
- [[concepts/harness-engineering/agent-ergonomics]] — Human factors in agent interaction design

## Open Questions

- Can agent design (rather than use curtailment) solve the project proliferation problem?
- Are the positive ADHD experiences a stable pattern or an early novelty effect?
- What's the optimal level of friction for different user types?
