---
title: Personal Software
type: concept
aliases: [just-in-time-software, bespoke-software, one-user-software]
created: 2026-06-05
updated: 2026-06-05
tags:
  - ai-agents
  - agent-skills
  - personal-software
  - software-engineering
  - mcp
  - ai-automation
  - agent-design-patterns
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - raw/transcripts/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
---

# Personal Software

Software built for **one user's workflow**, made newly cheap by AI coding agents. The point is not that everyone should use these tools — it's that agents make this kind of bespoke software economically viable for the first time.

## Definition

> *"Custom software or just-in-time software... I don't know if my way would work for anyone else."* — [[entities/jeremiah-lowin|Jeremiah Lowin]], Show Us Your Agent Skills Ep. 1

Personal software is:
- Built for a single user's specific workflow
- Edited the way that user wants to edit it
- In the vocabulary that user uses
- Not intended for general distribution

## Why Now

Before AI agents, building bespoke software for one person was almost never worth the engineering effort. Agents change the economics:

- **Development cost drops** — An agent can build a working tool in hours, not weeks
- **Maintenance becomes the skill** — The user edits skills and memory, not source code
- **MCP enables composability** — Tools can be wired together without traditional backend infrastructure

> *"This is not an interactive UI. This is read only... I interact with this entirely over an API or an MCP server, talking to it from any agent I want that can connect to it."* — Jeremiah Lowin on Cardboard

## Examples

### Cardboard (Jeremiah Lowin)

Custom slide software that lays out talks as **acts → beats → slides**. Read-only UI driven entirely via MCP from OpenClaw voice memos. Built in days.

> *"Purely for me, like no one else should use it."*

**Design insight**: Read-only UIs need no form validation, no edit conflicts, no permissions model. The expensive parts live in the agent layer.

### Wes McKinney's Local Tooling

- **Middleman** — Local GitHub replacement with activity pinned to top of PRs
- **Kata** — Local issue tracker
- **Agents View** — Session search across hundreds of agent sessions

> *"GitHub is in leagues with big scroll. They just really want you to have to scroll to the bottom of a pull request with like 100 comments."*

### Randy Olson's Data-Viz Skill

Encodes his personal taste: which data sources to prefer, which chart variants to try, which mistakes to reject, Tuftean evaluation criteria. The artifact and the stack underneath it are both shaped by the same one user.

## The Stack Is Personal Too

> *"So you have your harness, you have OpenClaw, you have Pi, whatever you Claude, whatever you want to use as your base substrate, and then the way people pile on functionality features, customize it, skills, is deeply personal."* — Jeremiah Lowin

The choice of substrate, memory system, and tool composition is itself personal. OpenClaw fits Jeremiah because he's customized its memory layer. The artifact and the stack underneath it are both shaped by the same one user.

## Related Concepts

- [[concepts/agentic-engineering]] — The discipline that makes personal software viable
- [[concepts/generator-evaluator-pattern]] — Skills encode personal taste and judgment
- [[concepts/personal-ai]] — Broader category of AI assistants customized per user
- [[concepts/harness-engineering]] — The infrastructure layer under personal software

## Related Entities

- [[entities/jeremiah-lowin]] — Primary advocate (Cardboard, Prefab, OpenClaw skills)
- [[entities/wes-mckinney]] — Local-first tooling (Middleman, Kata, Agents View)
- [[entities/randy-olson]] — Data-viz skill encoding personal taste
- [[entities/fastmcp]] — Enables MCP-based personal software
- [[entities/openclaw]] — Memory substrate for personal software

## References

- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)

## Log

- **2026-06-05**: Initial concept page created.
