---
source_url: https://merge.dev/blog/context-engineering-all
ingested: 2026-10-14
sha256: 2d79bc10bf6f41c7565a845706d44eede6be56c01431746621cd4c5627b2bee6
title: Context engineering from individual prompts to company-wide context
author: Merge (Vivek, Dhruv)
published: 2026-10-01
---

# Context engineering from individual prompts to company-wide context

Merge.dev blog, 2026-10-01, by Vivek and Dhruv. Extracted body of the post.

## Framing: "the harness is a context engine"

AI engineers now talk of "the harness" and "context engineering." Once you build enough
harnesses you notice they are all solving one problem: **context engineering**.

## Context engineering is a system design problem

- **Definition:** a system that takes every signal an agent might need (task, codebase,
  memories, feedback, the work of other agents) and turns it into **just enough tokenized
  state for one inference call**.
- If you define context only as "the prompt", the system is a single **context window with one
  ceiling**: the better you write the prompt, the higher that ceiling. Real systems add **other
  ceilings**, and you need a new engineering discipline to reach each:
  - **Task performance** (get better at the job itself).
  - **State management** — keep context fresh and uncorrupted as conversations lengthen.
  - **Context acquisition** — retrieve the right knowledge at the right time.
- **"You can't context-engineer your way out of a capability ceiling"** (cite arXiv:2604.21792).
  If a model can't do the task, no context trick fixes it. But if the model *can* do it and
  doesn't because the right knowledge wasn't there at the right time, context engineering is
  the whole game.

## Four stages of context maturity (a map, not a checklist)

1. **The Prompt** — knowledge lives in your head or in files; everything for the call is
   assembled by hand. Ceiling = how well one person can write a prompt.
2. **The Knowledge Base** — knowledge is retrieved from a store (files, codebase, embeddings,
   a memory tool). Ceiling = how well you curate and retrieve; context is only as good as
   retrieval quality.
3. **The Learning Loop** — the system is **tuned**: it evaluates what worked, feeds outcomes
   back, gets measurably better over time. Ceiling = how well you design the loop — signal
   quality, what gets learned, how fast it adapts.
4. **The Company-Wide Context Engine** — context becomes **organizational**: an agent can
   learn and apply what the company knows even if no single person did, drawing on
   **organizational memory**, work of other agents, and feedback from a shared environment.

## Organizational memory: four layers

- **Instructs** — the standing, always-on "how we do things" layer.
- **Skills** — how the work is actually done.
- **Malleable memory** — the layer of things currently being learned.
- **Semantic search** — everything else that doesn't fit the other three but might still help.

A company's context system should be understood by which of these it has, and **which of its
answers hold for reasons that survive the model it runs on**.

## Cross-links (wiki)

- context-engineering, memory, self-improving-agent-loop, context-architecture,
  harness-ontology, skill-issue.
