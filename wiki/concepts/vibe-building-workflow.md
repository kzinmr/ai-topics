---
title: "Vibe Building — Mollick's Five-Step Agentic Workflow"
created: 2026-09-23
updated: 2026-09-23
type: concept
tags:
  - agent-workflows
  - vibe-coding
  - methodology
  - emerging
sources:
  - raw/articles/rescue-raiders.netlify.app--rr-revisited--9a3d67be.md
related:
  - concepts/agent-generated-software
  - concepts/vibe-coding
  - concepts/agentic-coding
  - concepts/loop-engineering
  - entities/ethan-mollick
confidence: high
---

# Vibe Building — Mollick's Five-Step Agentic Workflow

Ethan Mollick's practical workflow for producing substantial results from frontier coding agents (Claude Fable-class) without becoming a professional engineer. Distilled from his work on the [[concepts/agent-generated-software]] examples (Rescue Raiders remake, lecture slide generators, education games): "a little process goes a *long* way when working with agents."

## The five steps

1. **Vibe-plan first** — before touching a coding agent, have ChatGPT/Claude/Gemini draft the spec: what you are making, features, constraints, and **how success is measured**. Skip this and you burn a lot of tokens on a tool that does the wrong job.
2. **Version control from minute one** — a GitHub repo even for solo work: versioning, change history, and rollback when the agent's work breaks something.
3. **Run the agent in a sandbox** — Claude Code / Codex running on your machine can delete data or leak secrets. A dev container (Google's **Zed**, Perplexity's **Macros** both good; cloud alternatives **Sponsor Bit** and **GitHub Codespaces**) means a blown sandbox costs nothing.
4. **Ask how to test** — make the agent itself explain how its work can be tested, *then actually run the tests*. This is the concrete instance of "verify, don't just eyeball."
5. **Close the loop** — test, find problems, hand findings back to the agent, iterate until the loop converges.

## Why it matters

The steps are cheap (minutes) but convert agentic coding from a slot machine into a repeatable process — the same "generate + critic + test loop" that made Valve's *Peaks* and the Rescue Raiders remake work, at individual scale. Pairs with [[concepts/loop-engineering]] as the single-practitioner version.

## See Also

- [[entities/ethan-mollick]] — source of the workflow
- [[concepts/agent-generated-software]] — what the workflow produces
- [[concepts/vibe-coding]] — practice this disciplines
- [[concepts/loop-engineering]] — related loop discipline

## Sources

- [[raw/articles/rescue-raiders.netlify.app--rr-revisited--9a3d67be.md]] — One person, a frontier AI agent, and 1987 abandonware (Mollick, Sep 23 2026; includes the five-step workflow)
