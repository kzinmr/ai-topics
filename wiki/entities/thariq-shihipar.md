---
title: Thariq Shihipar
type: entity
handle: "@trq212"
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - ai
  - startups
  - tech
  - anthropic
  - claude-code
  - agents
  - mit-media-lab
  - yc
  - interpretability
sources: []
---


# Thariq Shihipar (@trq212)

| | |
|---|---|
| **X** | [@trq212](https://x.com/trq212) |
| **Blog** | [thariq.io](https://www.thariq.io) |
| **GitHub** | [tshihpar](https://github.com/tshihpar) |
| **Role** | Member of Technical Staff @ Anthropic (Claude Code team); Founder @ Multiverse |
| **Known for** | Claude Agent SDK architecture, "Skills" system design, agent harness engineering, interpretability research, YC-backed startups |
| **Bio** | Engineer and serial entrepreneur currently on the Claude Code team at Anthropic. Previously founded Multiverse (YC W20, raised $17M), sold a SaaS startup (Edgeout.gg → blitz.gg), co-founded Pubpub.org (non-profit academic publishing), and studied at the MIT Media Lab. Writes thoughtfully about AI interpretability, agent architecture, spirituality, and the craft of building. |

## Overview

Thariq Shihipar occupies a unique position in the AI engineering world — he is simultaneously a **core builder of production AI systems** (Claude Code at Anthropic) and a **reflective practitioner** who writes deeply about the philosophical and spiritual dimensions of technology. This combination of deep technical chops and introspective analysis makes his blog one of the most distinctive in the AI space.

At Anthropic, Shihipar is a Member of Technical Staff on the **Claude Code** team and was a key architect of the **Claude Agent SDK** (formerly Claude Code SDK). His January 2026 workshop on the Claude Agent SDK — "Learn to use Anthropic's Claude Agent SDK for AI-powered development workflows" — attracted nearly 100,000 views on YouTube and has been described by developers as "the Agent builder's bible." In this workshop, he built an agent harness from scratch, implementing the core Agent Loop (Context → Thought → Action → Observation), integrating the Bash tool for general computer use, and demonstrating context engineering via the filesystem.

His work on **Skills** — Anthropic's modular mechanism for extending Claude's capabilities — has been particularly influential. A February 2026 article, "Lessons from Building Claude Code: How We Use Skills," went viral with over 6 million views and 15,000 likes on X. The article detailed how Anthropic's team uses Skills as modular "smart folders" containing scripts, knowledge bases, and documentation to make Claude behave like a specialized professional assistant.

Before Anthropic, Shihipar's entrepreneurial track record includes:
- **Multiverse** (YC W20) — A gaming company that raised $17M and scaled to over a million users, going viral on TikTok
- **Edgeout.gg** — A bootstrapped gaming analytics platform sold to blitz.gg
- **Quick Edit** — AI copyediting with great UX
- **Sherpa** — An AI email assistant that prioritizes emails based on contacts and goals
- **Pubpub.org** — A non-profit academic publishing platform (co-founded)
- **LatentLit** — A tool for creating and sharing LLM-powered AI agents
- **Chime** — An undergrad startup

He also holds a graduate degree from the **MIT Media Lab**, where he explored the intersection of technology, creativity, and human-computer interaction.

## Core Ideas

### The Harness Concept

Shihipar's work on the Claude Agent SDK is grounded in the idea that **agents need more than just a model** — they need a "harness" containing:

- **Tools**: Capabilities the agent can invoke (Bash, file operations, web browsing)
- **Prompts**: Behavioral constraints and instructions
- **File System**: Durable state and context engineering surface (`CLAUDE.md`)
- **Skills**: Modular capability packages
- **Sub-agents**: Delegated agents for specialized tasks
- **Memory**: Cross-session state and learning

> *"Agents build their own context, like decide their own trajectories, are working very very autonomously."*

This framing aligns closely with [[varun-trivedy]]'s "Agent = Model + Harness" equation and [[philipp-schmid]]'s analysis of agent harnesses as the key infrastructure layer for 2026.

### The Power of the Bash Tool

One of Shihipar's key technical insights is that the **Bash tool** is often the most powerful tool for agent workflows:

> *"The Bash tool is the ultimate API — it gives agents general-purpose access to the computer, rather than being limited to specific pre-built integrations."*

This insight has influenced how the Claude Agent SDK is designed — prioritizing general-purpose computer access over domain-specific tool integrations.

### Context Engineering via Filesystem

Shihipar introduced the concept of **Context Engineering** — using the filesystem as the primary medium for maintaining agent state across long-running tasks:

- `CLAUDE.md` files ground future actions with persistent context
- The filesystem serves as a shared workspace between humans and agents
- Git provides versioning, rollback, and branching capabilities
- Skills can be stored as files and discovered dynamically

> *"One of the key insights we had building Claude Code is that people were using it for non-coding tasks. The filesystem turned out to be the universal interface."*

### Interpretability and Steering

In "Should Developers Care about Interpretability?" (Nov 2024), Shihipar made the case that interpretability is not just an academic concern but a practical engineering tool:

- Understanding *how* models make decisions enables better prompt engineering
- Steering techniques (modifying model behavior without retraining) are becoming production-ready
- Developers who understand model internals will have a significant advantage in building reliable AI systems

### Entropix and Uncertainty Detection

In "Detecting when LLMs are Uncertain" (Oct 2024), Shihipar provided an accessible deep-dive into **Entropix**, a technique developed by XJDR for improving reasoning through adaptive sampling:

- **Entropy** measures how spread out the model's predictions are
- **Varentropy** measures the "shape" of uncertainty
- Different uncertainty states suggest different actions (branching, thinking tokens, standard sampling)
- Inference-time techniques are accessible to open-source hackers without huge budgets

### Spiritual Technology

Shihipar's blog extends beyond pure technical content into deeply personal reflections on spirituality, intention, and character development:

- **"Spiritual Technology"** — On systematized ways of improving character and soul, inspired by Ghazali
- **"Intention"** — On the nature of intention, accountability, and why he writes publicly about spirituality
- **"I can think. I can wait. I can fast."** — On not needing anything, and the freedom that comes from wanting less
- **"Clay and Light"** — On the two modes of being — driven by desire or moved by something inexplicable

## Key Work

### Claude Agent SDK Workshop (Jan 2026)

A comprehensive 1h53m workshop that became one of the most-viewed technical tutorials on AI agent development:
- Built an agent harness from scratch live on camera
- Implemented the core Agent Loop (Context → Thought → Action → Observation)
- Demonstrated context engineering via the filesystem
- Showed how the Bash tool enables general-purpose computer use
- Explained the evolution from LLM features to LLM agents

### "Lessons from Building Claude Code: How We Use Skills" (Feb 2026)

A viral article (6M+ views, 15K+ likes on X) detailing:
- 9 real-world application scenarios for Skills
- High-level design principles for modular AI capabilities
- Common pitfalls and how to avoid them
- How Skills became the most flexible and shareable AI tooling mechanism at Anthropic

### Multiverse (YC W20)

A Y Combinator-backed gaming company that:
- Raised $17M in funding
- Scaled to over 1 million users
- Went viral on TikTok
- Ran for 5 years before transitioning

### Entropix Analysis (Oct 2024)

An accessible explanation of XJDR's uncertainty detection technique:
- Mapped entropy and varentropy combinations to specific sampling actions
- Compared branching (MCTS) vs. thinking tokens approaches
- Argued for inference-time optimization as a low-budget path to improved reasoning

### Other Notable Projects

| Project | Description |
|---------|-------------|
| **LatentLit** | Tool for creating and sharing LLM-powered AI agents |
| **Sherpa** | AI email assistant that prioritizes based on contacts and goals |
| **Quick Edit** | AI copyediting with great UX |
| **AI Worldbuilding** | Experiment in AI-aided world building for RPGs |
| **Edgeout.gg** | Bootstrapped gaming analytics (sold to blitz.gg) |
| **Pubpub.org** | Non-profit academic publishing platform (co-founded) |
| **LLM-Powered Sorting with TrueSkill** | Sorting large datasets using LLMs and TrueSkill ranking |

## Blog / Recent Posts

| Date | Title | Theme |
|------|-------|-------|
| 2026-03-28 | ✦ Clay and Light | Spiritual — Two modes of being: driven by desire or moved by inexplicability |
| 2026-02-22 | A Lovely Autumn Night | Reflection — How ambition changes shape from climbing towers to caring for people |
| 2026-02-14 | The Thing | Courage — We're all bottlenecked by courage; being smart rarely helps |
| 2026-01-20 | I can think. I can wait. I can fast. | Minimalism — Freedom from wanting less |
| 2026-01-16 | Strangers & Travelers | Connection — Being a stranger in the world and changing without changing yourself |
| 2025-12-06 | Spiritual Technology | Character — Systematized ways of improving character, inspired by Ghazali |
| 2025-12-06 | Intention | Purpose — Nature of intention, accountability, public writing on spirituality |
| 2025-11-17 | LLM-Powered Sorting with TrueSkill | Technical — Sorting large datasets using LLMs and TrueSkill ranking |
| 2025-11-04 | Should Developers Care about Interpretability? | Technical — Breakdown of interpretability and steering, why it matters |
| 2025-10-24 | AI & Product Strategy Consulting through Multiverse Inc. | Business — Consulting services for AI product development |
| 2024-11-04 | Detecting when LLMs are Uncertain (Entropix) | Technical — Accessible deep-dive into Entropix reasoning techniques |
| 2024-10-11 | Crypto ELI5 | Education — Explaining cryptocurrency intuition through a "toy crypto" currency |
| 2024-10-11 | How Modding Games Changed My Life | Personal — The impact of game modding on creative development |

## Related People

- **[[varun-trivedy]]** — Both work on agent harness engineering; Trivedy's "Agent = Model + Harness" framework parallels Shihipar's SDK architecture
- **[[philipp-schmid]]** — Both write about agent infrastructure; Schmid's "2026 will be around Agent Harnesses" aligns with Shihipar's Claude Agent SDK work
- **[[entities/florian-brand.md]]** — Both interested in interpretability and understanding how AI systems work under the hood

## X Activity Themes

Shihipar's X activity (@trq212) typically covers:

1. **Claude Code & Agent SDK** — Technical deep-dives into agent architecture, Skills design, and harness engineering
2. **Interpretability research** — Accessible explanations of how LLMs work internally and why developers should care
3. **Startup lessons** — Reflections on building, scaling, and selling companies; practical advice for founders
4. **Spiritual and philosophical content** — Thoughtful posts on intention, character development, and the meaning of technology in human life
5. **AI product strategy** — Insights on building AI products that users actually want, drawing from extensive startup experience
6. **Community engagement** — Active participation in AI developer communities, workshop presentations, and knowledge sharing
