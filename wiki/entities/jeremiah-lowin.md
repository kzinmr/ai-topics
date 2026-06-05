---
title: Jeremiah Lowin
type: entity
aliases: [jeremiahlowin, jlowin]
created: 2026-06-05
updated: 2026-06-05
status: L2
tags:
  - person
  - ai-agents
  - agent-skills
  - memory-systems
  - personal-software
  - mcp
  - open-source
  - prefect
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
---

# Jeremiah Lowin

**Founder and CEO of Prefect, core maintainer of FastMCP, builder of personal software with AI agents.** Jeremiah is a practitioner who uses AI agents as a "second brain," feeding context through voice memos into an editable memory substrate (OpenClaw) and building bespoke tools for his own workflow.

## Quick Facts

| | |
|---|---|
| **X/Twitter** | [@jeremiahlowin](https://x.com/jeremiahlowin) |
| **GitHub** | [jlowin](https://github.com/jlowin) |
| **Role** | Founder/CEO, [Prefect](https://prefect.io) |
| **Notable projects** | FastMCP (core maintainer), Cardboard, Prefab, OpenClaw skills |

## Workflow Philosophy

### Agent as Second Brain

Jeremiah's central practice is **pouring information into agents and extracting it when needed**. He starts each workday with a voice memo — recorded during his commute or at his desk — talking through what he's thinking, what he wants to do, and what's on the horizon. The transcript drops into OpenClaw's memory substrate, where agents read from it asynchronously.

> *"That's what I really love, is just pouring information in and then working to get it out."* — Show Us Your Agent Skills, Ep. 1

The leverage comes from **feeding context for weeks or months before the moment you need an answer**:

> *"There's a talk I'm giving in three weeks for PyData London, so I can feed in something tonight, close it, don't worry about it, talk to the agent about 1,000 other things, and then I can come back and we can actually pick right up because of the memory substrate there."*

### Three Daily States

1. **Morning** — Voice memo recorded during commute or at home. Talk through the day. Drop into OpenClaw.
2. **Through the day** — Agents work in background, reading from the same memory layer.
3. **When you come back** — Threads pick up via memory substrate; conversations resume where they left off.

### Editable Memory as Key Criterion

Jeremiah chose OpenClaw specifically because he can **reach into the agent's memory and change what it remembers**:

> *"This is one of the reasons that I use an OpenClaw, for example, so that I can go muck around with its memory, in a way that works for me."*

If the operator can't edit what the agent remembers, the second brain is the vendor's, not theirs.

### Separate Tools for Thinking vs. Coding

- **OpenClaw** — main personal interface for thinking, planning, and accumulated context
- **Claude Desktop / Codex Desktop** — for writing code

> *"I use OpenClaw as my main personal interface because of how I've customized its memory. When I'm working on code, I use Claude Desktop and Codex Desktop, which I migrated to from the CLIs mostly because of how much better it is at managing parallel sessions."*

## Agent Skills Design

### Anatomy of a Skill

A skill is a markdown file with two pieces of frontmatter: **name** (used to invoke it) and **description** (always visible to the agent). The body is hidden until the agent decides to invoke the skill — this **progressive disclosure** is the key mechanism.

> *"Skills are shockingly simple for how effective they are. They have two front matter: a name, that's really important, that's how you invoke it; and a description. And the description is always going to be seen by the agent."*

### Key Skills

| Skill | Purpose |
|-------|---------|
| **ship-it** | Polite note telling Claude that "ship it" means *open a pull request*, not merge |
| **explain** | Referenced by every other skill; produces a guided tour (conceptual model → formal behavior → what changed → future work), explicitly bans line-level diff narration |
| **skill-creator** | Meta-skill for creating new skills |
| **github-reply** | Uses explain as a building block for responding to PRs |

> *"This skill has become my workhorse. It is referenced in every other skill I have."* — on `explain`

### Skills vs. MCPs

> *"Skills are awesome ways to steer behavior. They go into the agent's brain in the exact same way that a message from you does... MCPs are great ways to distribute business logic from a central place."*

## Personal Software Projects

### Cardboard
Custom slide software that lays out talks as **acts → beats → slides** with a fixed colour scheme for speaker notes. The screen is read-only by design — Jeremiah interacts entirely via API or MCP server from any agent.

> *"Purely for me, like no one else should use it."*

### Prefab
Python front-end framework for MCP apps, no backend required. Spun out of FastMCP. For building dashboards rather than one-off tools.

> *"I desperately wanted to create MCP apps in Python, and that meant I needed a Python front-end framework that didn't require a backend."*

## FastMCP

Jeremiah is the **core maintainer of FastMCP**, a Python framework for building MCP servers. He manages the volume of open-source contributions by running 10+ agents in parallel:

> *"Code is so cheap and it's just kind of getting lobbed over. There's this real imbalance as a maintainer."*

## Related People

| Person | Connection |
|--------|-----------|
| **[[entities/wes-mckinney\|Wes McKinney]]** | Fellow guest on Show Us Your Agent Skills Ep. 1 |
| **[[entities/randy-olson\|Randy Olson]]** | Fellow guest; generator-evaluator pattern |
| **[[entities/hugo-bowne-anderson\|Hugo Bowne-Anderson]]** | Host of Show Us Your Agent Skills |
| **Peter Steinberger** | OpenClaw creator (Jeremiah's memory substrate) |

## See Also

- [[entities/wes-mckinney]]
- [[entities/randy-olson]]
- [[entities/openclaw]]
- [[entities/fastmcp]]
- [[concepts/personal-software]]
- [[concepts/generator-evaluator-pattern]]

## References

- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)
- Show Us Your Agent Skills, Episode 1 (May 2026)

## Log

- **2026-06-05**: Initial entity page created from "The Agentic Software Factory" article.
