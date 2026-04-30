---
title: "Agent Engineering Guide 2026: What to Learn, Build, and Skip"
created: 2026-04-30
updated: 2026-04-30
type: concept
tags:
  - agent-engineering
  - career-development
  - context-engineering
  - tool-design
  - evals
  - harness-engineering
  - mcp
  - orchestration
aliases:
  - agent engineering filter
  - 2026 agent guide
  - what to learn in AI agents
related:
  - [[concepts/context-engineering]]
  - [[concepts/harness-engineering]]
  - [[concepts/prompt-caching]]
  - [[concepts/evals-for-ai-agents]]
  - [[concepts/mcp]]
  - [[concepts/agent-sandboxing]]
  - [[concepts/agent-memory]]
  - [[entities/claude-code]]
sources:
  - raw/articles/2026-04-30_x--what-to-learn-build-skip-ai-agents.md
  - https://x.com/i/article/2049548305408131349
---

# Agent Engineering Guide 2026: What to Learn, Build, and Skip

A comprehensive practitioner's guide to navigating the AI agent landscape in 2026. Published as an X native article (30K chars), this captures the converging wisdom of production agent engineers on what compounds vs. what's noise. It is the most complete articulation of [[entities/andrej-karpathy|Karpathy]]'s filter applied at scale.

**The core thesis**: The field moves under everyone equally. Knowing this week's framework API surface doesn't compound. Understanding primitives—context engineering, tool design, the orchestrator-subagent pattern, eval discipline, harness mindset, MCP—does. The credential is the artifact you ship.

## The Five-Part Filter

Before adopting any new launch, run it through these five tests:

| # | Test | What to Ask |
|---|------|-------------|
| 1 | **Will this matter in two years?** | Wrappers die fast; primitives (protocols, memory patterns, sandboxing approaches) survive. |
| 2 | **Has someone you respect built on it and written honestly about it?** | Postmortems > launch announcements. "We tried X in production and here's what broke" > "X is 10x better." |
| 3 | **Does adopting it require throwing away existing tracing, retries, config, auth?** | If yes, it's a framework trying to be a platform (90% mortality rate). Good primitives slot in. |
| 4 | **What does it cost to skip this for six months?** | For most launches: nothing. The winning version will be clearer. This test lets you skip 90% of launches without anxiety. |
| 5 | **Can you measure whether it actually helps your agents?** | Teams without evals run on vibes and ship regressions. Teams with evals let data decide. |

**The meta-skill**: The willingness to be uncool about what you don't pick up. The framework that goes viral on HN this week will have cheerleaders for 14 days. Six months later, half are unmaintained. The people who didn't engage saved their attention for things that survived the test of being boring after the hype passed.

## What to Learn (Compounds Forever)

These are the primitives that survive model swaps, framework swaps, and paradigm shifts.

### Context Engineering

The most important rename of the last two years: "prompt engineering" → "context engineering." The model is no longer something you craft a clever instruction for. It's something you assemble a working context for at every step: system instructions, tool schemas, retrieved documents, prior tool outputs, scratchpad state, compressed history. **Context is state.** Every token of irrelevant noise costs reasoning quality.

**Context rot** is a real production failure: by step eight of a ten-step task, the original goal can be buried under tool output. Teams that ship reliable agents actively summarize, compress, prune, version tool descriptions, cache static parts, and refuse to cache dynamic parts.

See also: [[concepts/context-engineering]], [[concepts/prompt-caching]], [[concepts/context-rot]]

### Tool Design

Tools are where agents meet your business. Five to ten well-named tools beat twenty mediocre ones. Tool names should read like English verb phrases. Descriptions should include when to use AND when not to. Error messages should be feedback the model can act on: "Max tokens 500 exceeded, try summarizing first" beats "Error: 400 Bad Request" by an enormous margin. One team reported a 40% reduction in retry loops after rewriting error messages alone.

See also: [[concepts/writing-effective-tools-for-ai-agents]]

### The Orchestrator-Subagent Pattern

The multi-agent debate of 2024–2025 ended with a synthesis: naïve multi-agent (shared state, parallel writes) fails catastrophically. Single-agent loops scale further than expected. **The one multi-agent shape that works in production**: an orchestrator agent delegates narrowly-scoped read-only tasks to isolated subagents, then synthesizes. Subagents get small, focused contexts. They cannot mutate shared state. The orchestrator owns the writes.

This is how Anthropic's research system works, how Claude Code's subagents work, and what Spring AI and most production frameworks now standardize. Default to single-agent. Reach for orchestrator-subagent only when the single agent hits context window pressure, latency from sequential tool calls, or task heterogeneity.

### Evals and Golden Datasets

Every team that ships reliable agents has evals. Every team that doesn't, doesn't. The single highest-leverage habit in the field. **Build a labeled regression set on day one, before you scale anything.** Harvest production traces, label failures, use LLM-as-judge for subjective parts, exact-match for the rest. Run the suite before any prompt, model, or tool change.

> Spotify's judge layer vetoes ~25% of agent outputs before they ship. Without it, one in four bad results would reach users.

The mental model: **an eval is a unit test that holds the agent honest while everything else changes underneath it.**

See also: [[concepts/evals-for-ai-agents]], [[concepts/evaluation-flywheel]], [[concepts/llm-as-judge]]

### File-System-as-State and the Think-Act-Observe Loop

For any agent doing real multi-step work, the durable architecture is: think → act → observe → repeat. The file system (or structured store) as the source of truth. Every action logged and replayable. Claude Code, Cursor, Devin, Aider, OpenHands, goose—all converged on this.

**The model is stateless. The harness has to be stateful.** The harness does more work than the model in any production agent worth its compute bill. The model picks the next action. The harness validates it, runs it in a sandbox, captures output, decides what to feed back, decides when to stop, decides when to checkpoint, decides when to spawn a subagent.

**Harness > model, always.** Swap the model for a different one of similar quality and a good harness still ships. Swap the harness for a worse one and the best model still produces an agent that randomly forgets what it was doing.

See also: [[concepts/harness-engineering]]

### MCP, Conceptually

Don't just learn how to call MCP servers. Learn the model: clean separation between agent capabilities, tools, and resources, with extensible auth and transport. Once you understand it, every other "agent integration framework" looks like a worse version of MCP. The Linux Foundation stewards it. Every major model provider backs it.

See also: [[concepts/mcp]]

### Sandboxing as a Primitive

Every production coding agent runs in a sandbox. Every browser agent has been hit by indirect prompt injection. Treat sandboxing as primitive infrastructure, not a feature you add when a customer asks. Process isolation, network egress controls, secret scoping, auth boundaries between agent and tool.

See also: [[concepts/agent-sandboxing]], [[concepts/agent-sandbox-patterns]]

## What to Build With (April 2026 Picks)

| Category | Pick | Notes |
|----------|------|-------|
| **Orchestration** | LangGraph | Production default, ~1/3 of large companies. Typed state, conditional edges, durable workflows. Verbose but the verbosity matches real production control needs. |
| **Orchestration (TypeScript)** | Mastra | Cleanest mental model in TS ecosystem. |
| **Orchestration (Pydantic-native)** | Pydantic AI | Hit v1.0 late 2025, real momentum. |
| **Protocol Layer** | MCP | Full stop. Build tool integrations as MCP servers. |
| **Memory (personalization)** | Mem0 | Chat-style user preferences. |
| **Memory (conversational)** | Zep | Production systems with evolving state and entity tracking. |
| **Memory (long-running)** | Letta | Agents maintaining coherence across days/weeks. |
| **Observability/Evals** | Langfuse (OSS), LangSmith, Braintrust | Both tracing AND evals. Don't ship without both. |
| **Runtime/Sandbox** | E2B (code), Browserbase (browser), Modal (bursts) | Never run unsandboxed code execution. |
| **Models (cost-performance)** | Claude Sonnet 4.6, GPT-5.5, Gemini 3, DeepSeek-V3.2/Qwen 3.6 for narrow tasks | Treat models as swappable. Re-evaluate quarterly. |

## What to Skip (The Karpathy Filter Applied)

### Frameworks to Skip
- **AutoGen/AG2**: Microsoft moved to community maintenance, releases stalled.
- **CrewAI**: Engineers building real systems have moved off it. Demos easily, doesn't scale.
- **Microsoft Semantic Kernel**: Not where the ecosystem is heading (unless locked into MS enterprise stack).
- **DSPy**: Niche. Philosophical merit, not a general agent framework. Don't pick it as one.

### Patterns to Skip
- **Autonomous agent pitches** (AutoGPT/BabyAGI lineage): Dead in product form. The honest framing is "agentic engineering": supervised, bounded, evaluated.
- **Agent app stores/marketplaces**: Promised since 2023, never delivered enterprise traction.
- **SWE-bench leaderboard chasing**: Nearly every public benchmark can be gamed without solving the underlying task.
- **Naïve parallel multi-agent architectures**: Five agents chatting over shared memory falls apart in production.
- **Standalone code-writing agents as architecture**: Interesting research, not a production-default pattern yet.
- **Horizontal "build any agent" enterprise platforms**: Buy-versus-build still favors narrow agents.
- **Per-seat SaaS pricing for agent products**: Market moved to outcome and usage-based.

### The Weekly Habit
Reserve 30 minutes on Friday: read Anthropic's engineering blog, Simon Willison's notes, Latent Space. Skim one or two postmortems. Skip everything else for the week.

## How to Actually Move

1. **Pick one outcome that already matters.** Not a moonshot. Something measurable your business already cares about. The agent succeeds when that outcome moves. This becomes your eval target.
2. **Set up tracing and evals before you ship anything.** Fifty labeled examples is enough to start. The cost of building this later is ~10x.
3. **Start with a single-agent loop.** LangGraph or Pydantic AI. Claude Sonnet 4.6 or GPT-5. Three to seven tools. File system or DB as state. Ship to a small audience. Watch traces.
4. **Treat the agent as a product, not a project.** Failures are your roadmap. Build the regression set from real production traces.
5. **Add scope only when you've earned it.** Subagents when context is the bottleneck. Memory frameworks when the window can't hold what you need. Computer use when APIs aren't there.
6. **Pick boring infrastructure.** MCP for tools. E2B/Browserbase for sandboxes. Postgres for state. Your existing auth/observability stack.
7. **Watch unit economics from day one.** Per-action costs, cache hit rates, retry-loop costs. Agents look cheap in PoC and explode at 100x scale.
8. **Re-evaluate models quarterly, not weekly.** Lock in for a quarter. Run evals at quarter-end and switch if data says to.

## Signal vs. Noise Detection

**Signal**: A respected engineering team writes a postmortem with numbers. It's a primitive (protocol, pattern, infra). It interoperates. The pitch describes a failure mode it solves. It's been around long enough to have a "what didn't work" blog post.

**Noise**: Demo videos with no production case studies after 30 days. Benchmark leaps too clean to be real. Pitches using "autonomous," "agent OS," or "build any agent." Frameworks whose docs assume you'll throw away existing infra. Star counts rising without commits/releases/contributors.

## What's Worth Watching (Next Two Quarters)

- **Replit Agent 4's parallel forking model** — First serious attempt at parallel agents that doesn't trip over shared state.
- **Outcome-based pricing maturity** — Sierra and Harvey validate it inside narrow verticals. Does it generalize?
- **Skills as a packaging layer** — AGENTS.md proliferation suggests emerging way to package agent capabilities.
- **Claude Code's April 2026 quality regression** — 47% regression caught by users before internal monitoring. Drives industry-wide investment in better online evals.
- **Voice as default support surface** — Sierra's voice channel surpassed text in late 2025. Latency/interruption/real-time tool use become first-order.
- **Open-model agent capability closing the gap** — DeepSeek-V3.2, Qwen 3.6. Cost-performance for narrow agent tasks shifting.

## The Unconventional Bet

The conventional path was: pick a stack, master it for years, climb a ladder. That worked when the stack was stable for a decade. The stack now changes every quarter. The people winning stopped optimizing for stack mastery and started optimizing for taste, primitives, and ship velocity. They build small things in public. They learn by shipping. They get pulled into rooms by what they've already made. **The credential is the artifact.**

The skill you actually need to develop is not "agents." It's the discipline of figuring out which work compounds in a field where the surface keeps changing. Context engineering compounds. Tool design compounds. The orchestrator-subagent pattern compounds. Eval discipline compounds. The harness mindset compounds. Knowing the API of the framework that launched on Tuesday does not.

> "Build things. Put them on the internet. The era rewards people who make the thing more than people who can describe the thing."

## Sources

- [What to Learn, Build, and Skip in AI Agents (2026)](https://x.com/i/article/2049548305408131349) — X native article, 30K chars. Original source for this concept page.
- Andrej Karpathy's filter (the five-part test is an elaborated version of Karpathy's "90% of what AI twitter tells you to learn will be dead in 6 months")
- Anthropic. ["Effective Context Engineering for AI Agents"](https://www.anthropic.com/engineering/effective-context-engineering)
- Cognition. ["Don't Build Multi-Agents"](https://cognition.ai/blog/dont-build-multi-agents)
- Claude Code postmortem (April 2026): 47% performance regression caught by user community before internal monitoring.
