---
title: "Harness Engineering"
created: 2026-04-09
updated: 2026-04-09
tags: [concept, ai-agents, tooling, emerging]
aliases: ["harness-eng", "agent harness"]
---

# Harness Engineering

Engineering methodology focused on building systems and structures around AI coding agents to maximize autonomous productivity, coined and popularized by Ryan Lopopolo at OpenAI.

## Core Philosophy

> "Move over, [[context-engineering]]. Now it's time for Harness Engineering and the age of the [[token-billionaires]]." — swyx

Harness engineering shifts the focus from writing code yourself to building the **structure, context, and systems** that enable AI agents to write, review, and merge code autonomously.

## Key Principles

### 1. Zero Human-Written Code
- Deliberately refuse to write code; force the agent to do the job end-to-end
- When the agent fails, ask "what capability, context, or structure is missing?" rather than fixing it manually
- Build smaller building blocks that the agent can reassemble

### 2. Fast Build Loops (1-Minute Rule)
- Inner loop build time capped at **1 minute**
- Retool build systems continuously to keep agents productive
- Build time discipline acts as a "ratchet" — tokens are cheap, so constantly garden the codebase

### 3. Agent-Legible Software
- Software must be written for the model as much as for the engineer
- Optimize entire codebase, workflow, and organization around **agent legibility** instead of human habit
- Encode engineering taste and non-functional requirements into context the agent can use

### 4. Humans Become the Bottleneck
- The scarce resource shifts from tokens to **synchronous human attention**
- Move from reviewing code directly → building systems, observability, and context that let agents review, fix, and merge autonomously
- Post-merge review becomes informational rather than gatekeeping

## What Agents Own (Full SDLC)

| Area | Examples |
|------|----------|
| Product code & tests | Core application logic |
| CI configuration & release tooling | Build pipelines |
| Internal DevRel tools | Debugging utilities |
| Documentation | Specs, runbooks |
| Eval & harness review | Quality gates |
| Scripts managing the repo | Automation |
| Production dashboards | Grafana JSON, alert definitions |
| Definition files | Config, infrastructure |

## Skills & Context Encoding

### Small Skill Files Over Massive Prompts
- ~6 core skills (not hundreds)
- Short overall table of contents (~100 lines)
- Skills determine when to use tools, not every call

### Quality Score & Tech Tracker
- Markdown tables as hooks for agents to review business logic
- Agents assess against documented guardrails and propose follow-up work
- Durable encoding of "what good looks like"

### Spec-Driven Development
- Instead of predefined scaffolds → reasoning-model-led workflows
- The harness becomes the box; the model chooses how to proceed
- See [[ghost-libraries]] for the "ghost library" pattern

## Results (OpenAI Internal Experiment)

| Metric | Value |
|--------|-------|
| Duration | 5 months |
| Human-written code | **0 lines** |
| Total codebase | >1,000,000 LOC |
| PRs merged | Thousands |
| Token spend | >1B tokens/day (~$2-3K/day) |
| Team size | 3 people initially |
| Model generations used | GPT-5.0 → 5.1 → 5.2 → 5.3 → 5.4 |

## On-Code is Disposable
- Worktrees and merge conflicts matter less when agents can resolve them
- Fully delegate the PR lifecycle
- If output is bad, trash it and restart — no emotional attachment to authored code

## Symphony Orchestration

See [[symphony-orchestration]] for details on OpenAI's internal Elixir-based multi-agent system that grew out of harness engineering principles.

## Key Commentary

### Brett Taylor (OpenAI Chairman) Response
> "Software dependencies are going away — they can just be vendored."

Ryan agreed: internalizing dependencies (even 1K-10K LOC) is feasible. Agents can deep-review and change internalized code with lower friction than upstream patching.

### On Agent Self-Improvement
- Slurp up all agent trajectories → run daily agent loops → extract team-wide learnings → reflect back into the repository
- "Everybody benefits from everybody else's behavior for free"

### On CLI Design for Agents
- Agents prefer CLI over GUI
- Token-efficient CLIs should suppress verbose output (only show failures)
- Patch tools to be agent-friendly (e.g., `--silent` mode, structured output)

### On Model Trajectory
- Each model release (5.0 → 5.4) significantly expanded capability ceiling
- What was impossible at 5.0 became trivial at 5.4
- "Don't bet against the model" — build systems robust to rapid capability improvements

## Sources
- [[raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--197ff517]] (swyx, 2026-04-10)
- [[raw/articles/substack.com--app-link-post--4e59bb76]] (swyx podcast transcript, 2026-04-10)
- Ryan Lopopolo's original harness engineering essay

## Related
- [[symphony-orchestration]]
- [[openai-frontier]]
- [[ryan-lopopolo]]
- [[ghost-libraries]]
- [[token-billionaires]]
- [[codex]]
- [[context-engineering]]
