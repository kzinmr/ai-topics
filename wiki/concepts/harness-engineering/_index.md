---
title: "Harness Engineering — Integrated Framework for AI Agent Environment Design"
type: concept
aliases:
  - harness-engineering
  - agent-harness
  - openai-harness
  - symphony-orchestrator
created: 2026-04-09
updated: 2026-04-19
tags:
  - concept
  - methodology
  - harness-engineering
  - ai-agents
  - orchestration
status: active
sources:
  - "https://openai.com/index/harness-engineering/"
  - "http://rywalker.com/research/symphony"
  - "https://www.youtube.com/watch?v=CeOXx-XTYek"
  - "https://www.engineering.fyi/article/harness-engineering-leveraging-codex-in-an-agent-first-world"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/"
---

# Harness Engineering — Integrated Framework

> **Definition:** Harness Engineering is an environment design philosophy for agent-driven development, based on the fundamental equation "Agent = Model + Harness." It focuses on designing environments ("harnesses") in which agents can autonomously write, test, and merge code.

Championed by Ryan Lopopolo (OpenAI), this is the **top-level concept** encompassing Simon Willison's Agentic Engineering, Anthropic's AI Agent Engineering, and Karpathy's Context Engineering.

## Concept Map

```
Harness Engineering (Top-level: Agent = Model + Harness)
│
├── agentic-engineering.md — Willison philosophy: development patterns where humans "leverage" agents
├── agentic-engineering-patterns.md — Willison practical guide: TDD, subagents, Cognitive Debt
│
├── agentic-workflows/ — Developer workflows (Agentic Engineering subpages, 23 files)
│   ├── _index.md
│   ├── agent-first-design.md
│   ├── agentic-manual-testing.md
│   ├── anti-patterns.md
│   ├── cli-first-development.md
│   ├── code-hoarding.md
│   ├── cognitive-debt.md
│   ├── compound-engineering-loop.md
│   ├── context-window-management.md
│   ├── first-run-the-tests.md
│   ├── hoard-things-you-know.md
│   ├── how-agents-work.md
│   ├── interactive-explanations.md
│   ├── karpathy-rl-agents.md
│   ├── linear-walkthroughs.md
│   ├── prompt-driven-development.md
│   ├── red-green-tdd.md
│   ├── rodney.md
│   ├── showboat.md
│   ├── subagents.md
│   ├── throw-away-draft-pattern.md
│   ├── using-git-with-agents.md
│   └── vibe-coding.md
│
├── system-architecture/ — System construction (AI Agent Engineering subpages, 19 files)
│   ├── _index.md
│   ├── advanced-tool-use.md
│   ├── agent-loop-orchestration.md
│   ├── agent-security-patterns.md
│   ├── agent-skills.md
│   ├── ai-memory-systems.md
│   ├── anthropic-memory-tool-cognition.md
│   ├── building-effective-agents.md
│   ├── claude-code-best-practices.md
│   ├── code-execution-with-mcp.md
│   ├── container-context.md
│   ├── context-anxiety.md
│   ├── context-compaction.md
│   ├── effective-harnesses-for-long-running-agents.md
│   ├── evals-for-ai-agents.md
│   ├── harness-design-long-running-apps.md
│   ├── infrastructure-noise.md
│   ├── multi-agent-research-system.md
│   └── writing-tools-for-agents.md
│
├── context-engineering.md — Context optimization (Karpathy + DSPy + Anthropic integrated version)
```

## Core Philosophy of Harness Engineering

### 1. Zero Human-Written Code
By intentionally not writing code, the agent is forced to perform end-to-end work. When the agent fails, the question becomes "what's missing?" — tools, context, structure.

### 2. Fast Build Loops (1-Minute Rule)
Limit inner loop build time to **within 1 minute**. Tokens are cheap, so keep the codebase in constant shape.

### 3. Agent-Legible Software
Software is written not just for humans but for models. Optimize codebases, workflows, and entire organizations for **agent readability**.

### 4. Humans Become the Bottleneck
The scarce resource shifts from tokens to **synchronous human attention**. The role changes from code review to system construction, observability, and context design.

## OpenAI Harness Experiment (Results)

| Metric | Value |
|--------|-------|
| Duration | 5 months |
| Human-written code | **0 lines** |
| Total codebase | >1,000,000 LOC |
| Merged PRs | Thousands |
| Token consumption | >1B tokens/day (~$2-3K/day) |
| Team size | Initially 3 |
| Models used | GPT-5.0 → 5.1 → 5.2 → 5.3 → 5.4 |

## Relationship to Agentic Engineering

| Dimension | Harness Engineering (Lopopolo) | Agentic Engineering (Willison) |
|-----------|-------------------------------|-------------------------------|
| Focus | Environment design, structure | Developer workflow, testing, quality |
| Human code | 0 lines (all agent) | Mixed (human makes final judgment) |
| Metrics | Throughput, PR count | Code quality, test coverage |
| Representative projects | Symphony, AGENTS.md | Datasette, LLM, Agentic Patterns Guide |
| Relationship | **Top-level concept** | **Subset (human utilization side)** |

> "The bottleneck in agent-first software development is usually not the agent's ability to write code. It's the quality of the environment the agent operates in." — Ryan Lopopolo

## Symphony: Issue-Tracker-Driven Orchestration

[Symphony](https://github.com/openai/symphony) is the embodiment of Harness Engineering:

> "Symphony shifts engineering from supervising coding agents to managing work — issues go in, PRs come out."

### How It Works
1. **Linear polling** — Periodically fetch eligible issues
2. **Workspace isolation** — Create independent environments per issue
3. **Agent launch** — Codex agent processes the issue
4. **Auto PR creation** — Submit PR after testing/review
5. **WORKFLOW.md** — Policy file in the repo controlling agent behavior

## AGENTS.md Pattern

> "Treat your AGENTS.md as a table of contents (~100 lines) rather than a comprehensive encyclopedia. A monolithic instruction file crowds out task context."

### Design Principles
1. **Small entry point** — ~100 line AGENTS.md functions as a table of contents
2. **Details in `docs/` directory** — Structured documentation for agents to reference
3. **Progressive Disclosure** — Don't give everything at once; provide pointers to needed information

## Relationship to Context Engineering

Context Engineering is a **cross-cutting technical component** of Harness Engineering:
- Harness = Environment design for "what to show the agent and what to hide"
- Context Engineering = Within that, specifically "context window optimization" techniques

Karpathy's definition:
> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step."

Details: [[concepts/context-engineering|Context Engineering]]

## Key Commentary

### Brett Taylor (OpenAI Chairman) Response
> "Software dependencies are going away — they can just be vendored."

Ryan agrees: internalizing dependencies (even 1K-10K LOC) is feasible. Agents can review and modify internalized code with lower friction than upstream patching.

### On Agent Self-Improvement
- Capture all agent trajectories → run daily agent loop → extract team-wide learning → reflect in repository
- "Everybody benefits from everybody else's behavior for free"

### On Model Trajectory
- Each model release (5.0 → 5.4) significantly expanded capability ceilings
- "Don't bet against the model" — build robust systems for rapidly improving capabilities

## Redefining the Human Role

| Traditional Engineer | Harness Engineering Engineer |
|---------------------|------------------------------|
| Write code | Design environment, specify intent, build feedback loops |
| Review PRs | Validate artifacts, define acceptance criteria |
| Write tests | Design test strategy, agents implement |
| Solve problems | Prioritize problems, delegate to agents |

> "When an agent struggles, it's a signal that something is missing: identify the tool, guardrail, or documentation, and have the agent write the fix itself."

## Derived Design Patterns

### CLI Design for Agents
- Agents prefer CLI over GUI
- Token-efficient CLIs suppress verbose output (show failures only)
- Patch tools to be agent-friendly (e.g., `--silent` mode, structured output)

### Agent Self-Improvement Loop
- Capture all agent trajectories → run daily agent loop → extract team-wide learning → reflect in repository
- "Everybody benefits from everybody else's behavior for free"

### Dependency Vendoring (Brett Taylor)
- "Software dependencies can disappear — they can be vendored"
- Internalizing dependencies (even 1K-10K LOC) is feasible
- Agents can review and modify internalized code with lower friction than upstream patching

## Comparison with Other AI Engineering Leaders

| Dimension | Harness Eng (Lopopolo) | Agentic Eng (Willison) | Loopy Era (Karpathy) |
|-----------|----------------------|----------------------|---------------------|
| Focus | Environment design, structure | Testing, quality | Autonomous loops, experimentation |
| Human code | 0 lines | Mixed | Nearly 0 lines |
| Metrics | Throughput | Code quality | Experiment count |
| Representative projects | Symphony | Datasette, LLM | AutoResearch |

## Related Concepts

### Sub-Concepts Under Harness
- [[concepts/harness-engineering/agentic-workflows/interactive-explanations]] — Developer workflow details (Willison, Sankalp, Steipete patterns)
- [[concepts/harness-engineering/system-architecture/container-context]] — System construction patterns (Anthropic, OpenAI Responses API)
- [[concepts/context-engineering|Context Engineering]] — Context optimization techniques (Karpathy + DSPy + Anthropic)

### Cross-References
- [[concepts/karpathy-loop]] — Karpathy's autonomous experimental design loop
- [[concepts/skill-architecture-patterns]] — Skill self-improvement vs. management patterns
- [[concepts/harness-engineering/system-architecture/context-compaction]] — Context compaction mechanisms
- [[concepts/harness-engineering/system-architecture/context-anxiety]] — Claude Sonnet 4.5's context anxiety phenomenon
- [[concepts/mismanaged-geniuses-hypothesis]] — Frontier LMs underutilized by suboptimal scaffolding

## Sources
- [[concepts/agentic-engineering]] — Simon Willison's Agentic Engineering philosophy
- [[concepts/harness-engineering/agentic-engineering-patterns]] — Simon Willison's practical pattern guide
- [[concepts/harness-engineering/agentic-workflows/interactive-explanations]] — Developer workflow details (Willison, Sankalp, Steipete patterns)
- [[concepts/harness-engineering/system-architecture/container-context]] — System construction patterns (Anthropic, OpenAI Responses API)
- Ryan Lopopolo, OpenAI Harness Engineering
- Anthropic: Building Effective Agents, Context Engineering
- OpenAI Cookbook: Context Engineering Patterns

---

*Page restructured: 2026-04-19 | Agentic/AI Agent Engineering integrated under Harness | Context Engineering pending integration*
