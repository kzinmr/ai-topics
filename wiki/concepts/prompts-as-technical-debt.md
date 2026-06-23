---
title: Prompts as Technical Debt
created: 2026-05-21
updated: 2026-06-23
type: concept
tags:
  - prompting
  - technical-debt
  - ai-agent-engineering
  - agentic-engineering
  - metaprompting
  - harness-engineering
  - coding-agents
  - model
  - software-engineering
  - multi-llm
  - fighting-the-weights
  - dspy
  - gepa
sources:
  - raw/articles/seangoedecke.com--prompts-are-technical-debt-too--2bd50f80.md
  - raw/articles/2026-06-23_drew-breunig-prompt-debt.md
---

# Prompts as Technical Debt

The concept that **prompts are a form of technical debt** — possibly worse than code debt — was articulated by Sean Goedecke in May 2026. The argument extends the well-known adage "all code is technical debt" to the rapidly growing practice of maintaining project-specific prompt files (AGENTS.md, CLAUDE.md, skills, system prompts) for AI coding agents.

## The Core Argument

### Prompts Accumulate Like Code
Just as every line of code adds complexity and maintenance burden, prompt files grow alongside codebases:
- **AGENTS.md** and **CLAUDE.md** files at project root and subdirectories
- **Skills files** for agent harnesses
- **System prompts** for individual AI capabilities
- **Tool-specific prompts** for MCP servers and integrations

### Prompts Decay Silently (Worse Than Code)
Unlike code, where technical debt manifests as errors or slowdowns, prompts can become silently harmful:
- A prompt tuned for one model (e.g., GPT-5.4) may underperform on the next (GPT-5.5)
- Model upgrades can turn functional prompts into actively harmful ones without any visible error
- Engineers may not notice — they just conclude "the new model isn't as good"

### Model-Specific Fragility
Each new model release requires "re-learning how to hold the model." AI companies spend significant effort tweaking prompts for each model iteration. Individual engineers' bespoke prompt setups don't get the same attention:
- A prompt crafted in January may be harmful by February
- "Switching tools or workflows is a form of prompting" — choosing [[concepts/claude-code/claude-code]] over [[openai-codex-cli]], or adopting a [[ralph-loop]] pattern, is also a prompt-level decision

## Implications for AI Agent Engineering

### Keep Agent Setups Minimal
Goedecke recommends:
- Pick a third-party AI coding tool ([[concepts/claude-code/claude-code]], [[openai-codex-cli]], [[cursor]], [[github-copilot]]) and leave it **as unconfigured as possible**
- Piggyback on the work of teams who evaluate and tweak prompts for each model release
- **Avoid MCP and skills unless absolutely necessary**, and keep them off by default

### AGENTS.md Discipline
When writing project prompt files:
- **Avoid behavior steering** — no "think step by step," "you are a skilled engineer," or "I'll tip you $200"
- **Limit to concrete, project-specific facts** about the codebase
- **Write prompts yourself** — don't let models auto-generate pages of barely-reviewed prompt text (same reason you wouldn't let them auto-generate pages of code)
- **Delete prompts when you can** — same instinct as deleting dead code

### Counterpoint: The Harness Engineering View
The [[concepts/harness-engineering/agent-harness]] philosophy (notably articulated by [[garry-tan]] and practitioners of [[hermes-agent]]) takes the opposite view — that carefully engineered prompts, skills, and metaprompting are the key differentiator. See comparison at [[agent-harnesses]].

This tension between "minimal prompting" and "engineering the harness" is one of the central debates in AI agent engineering in 2026.

## Comparison to Code Technical Debt

| Aspect | Code Technical Debt | Prompt Technical Debt |
|---|---|---|
| Detection | Errors, slowdowns on change | Silent decay, no errors |
| Stability | Stable when untouched | Breaks with every model upgrade |
| Maintenance | Refactoring efforts | Requires re-tuning per model |
| Accumulation rate | Gradual | Rapid (new models every few months) |
| Best practice | Write as little as possible | Keep as unconfigured as possible |

## Drew Breunig's "Prompt Debt" Framework (June 2026)

In June 2026, [[entities/drew-breunig|Drew Breunig]] published "The Problem is Prompt Debt," extending the prompt-as-debt metaphor with a systematic analysis of **how** prompt debt accumulates, **why** it happens, and **how** to prevent it. His framework provides engineering depth beyond the initial observation:

### The Three-Stage Downward Spiral

Breunig describes prompt debt as a progressive condition that worsens in three distinct stages:

1. **Slowing Iteration**: Hot-fixes and edge-case instructions accumulate. Each new instruction risks regressing previous ones. Development cycles slow to a crawl.

2. **Team Incapacitation**: The prompt becomes a brittle thicket of conditions, all-caps threats, and repeated instructions — "impenetrable to colleagues." Templates evolve into labyrinths of conditional assembly logic.

3. **Model Lock-In**: Hot-fixes tailored to one model (e.g., GPT-4o) fail entirely on the next (e.g., GPT-5.4-mini). Teams forgo cheaper/faster models and ignore deprecation warnings. Datadog observed that GPT-4o remained the most-used model months after its launch, and Breunig reports that models of similar vintage can account for >50% of all inference calls.

### Fighting the Weights

A core mechanism driving prompt debt: when desired behavior contradicts model training, prompt authors must **fight the weights** with repeated instructions, stern warnings, and all-caps demands. Breunig documents concrete examples:

- **ChatGPT's image prompt**: Instructed the LLM eight times to NOT reply when an image was returned — because training pushed the model to always continue the conversation
- **Claude Code**: Tells Opus seven times to return multiple tool calls in a single response
- **Anthropic Fable**: Restates one copyright rule six times in its leaked system prompt

Each repetition increases brittleness and regression risk with every edit. These fixes are model-specific — they break when the model changes, because "models are not cleanly versioned software. They have different weights that produce different behaviors."

### Two Prevention Principles

Breunig argues that the solution comes from the coding agent community (the "outliers on the jagged frontier"), who have developed two principles:

**Principle 1: Specify with Measurements, Not Prose.** Replace natural language specifications with hard edges: evaluations, metrics, and typed specifications. These are legible, shared artifacts that enable collaboration. The best engineers now spend more time on tests — not as a safety net, but as "the thing that lets the model cook."

**Principle 2: Stop Writing the Prompt by Hand.** Once metrics can score candidates, the prompt becomes something to search for, not craft. The surface area of possible words and structures is too vast for human hours. Systems like [[concepts/dspy|DSPy]] and [[concepts/gepa|GEPA (Genetic-Pareto Prompt Evolution)]] automate this search, holding prompts accountable to measurements.

### The Engineering Maturation Parallel

Breunig draws a historical analogy: every mature engineering discipline eventually stops doing by hand what it once took pride in doing by hand:

| Discipline | Manual Era → Automated |
|---|---|
| Programming | Assembly → Compilers |
| Databases | Hand-tuned queries → Query planners |
| Memory | Manual management → GC |
| **Prompts** | Hand-crafted prompts → Algorithmic prompt search |

### Goedecke vs. Breunig: Complementary Perspectives

| Dimension | Goedecke (May 2026) | Breunig (June 2026) |
|---|---|---|
| **Core metaphor** | Prompts ARE technical debt (like code debt) | Prompt Debt is a progressive condition with stages |
| **Root cause** | Prompts decay silently with model upgrades | Fighting the weights + natural language imprecision |
| **Primary symptom** | Model-specific fragility | Three-stage spiral: slowdown → team incapacitation → lock-in |
| **Solution** | Minimal prompting, piggyback on tool teams | Measurements over prose + algorithmic prompt search (DSPy/GEPA) |
| **Philosophy** | Defensive: avoid accumulating prompt complexity | Proactive: replace prompt-writing entirely with search |
| **Key tools** | Unconfigured tools, delete prompts | DSPy, GEPA, evaluation suites |

## Extended Comparison: Three Views on Prompt Debt

| Aspect | Code Technical Debt | Goedecke Prompt Debt | Breunig Prompt Debt |
|---|---|---|---|
| Detection | Errors, slowdowns | Silent decay | Spiral symptoms (slowdown, team pain, lock-in) |
| Mechanism | Entropy in codebase | Model upgrade breaks prompts | Fighting the weights creates repeated instructions |
| Stability | Stable when untouched | Breaks with every model upgrade | Model-specific hot-fixes prevent portability |
| Accumulation | Gradual | Rapid (new model cadence) | Progressive (each fix adds brittleness) |
| Fix strategy | Refactor, delete dead code | Keep minimal, piggyback | Replace prompts with eval-driven search |
| End state | Maintainable code | Thin prompt layer | Portable, model-agnostic systems |

## Related Concepts
- [[entities/drew-breunig]] — Author of "The Problem is Prompt Debt," introduced fighting-the-weights and algorithmic prompt search
- [[concepts/dspy|DSPy]] — Framework for algorithmic prompt optimization cited as a prompt-debt solution
- [[concepts/gepa|GEPA (Genetic-Pareto Prompt Evolution)]] — Evolutionary prompt optimizer cited as a prompt-debt solution
- [[concepts/harness-engineering/agent-harness]] — The opposing view: invest deeply in prompt engineering
- [[metaprompting]] — The broader practice of prompting systems that prompt
- [[concepts/harness-engineering/agent-architecture-decomposition]] — How agent systems distribute prompting across components
- [[ralph-loop]] — A specific agent workflow pattern (a form of prompting)
- [[ai-agent-engineering]] — The engineering discipline around AI agents
- [[concepts/coding-agents/model-routing]] — Choosing which model to use (a prompt-level decision)

## Sources

- **Sean Goedecke**, "Prompts are technical debt too" (May 2026) — Original framing. See [[seangoedecke.com--prompts-are-technical-debt-too--2bd50f80]]
- **Drew Breunig**, "The Problem is Prompt Debt" (June 2026) — Extended framework with three-stage spiral, fighting the weights, and algorithmic prompt search. See [[raw/articles/2026-06-23_drew-breunig-prompt-debt]]
