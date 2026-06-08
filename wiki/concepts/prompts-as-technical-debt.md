---
title: Prompts as Technical Debt
created: 2026-05-21
updated: 2026-05-21
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
sources: [raw/articles/seangoedecke.com--prompts-are-technical-debt-too--2bd50f80.md]
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
- "Switching tools or workflows is a form of prompting" — choosing [[claude-code]] over [[openai-codex-cli]], or adopting a [[ralph-loop]] pattern, is also a prompt-level decision

## Implications for AI Agent Engineering

### Keep Agent Setups Minimal
Goedecke recommends:
- Pick a third-party AI coding tool ([[claude-code]], [[openai-codex-cli]], [[cursor]], [[github-copilot]]) and leave it **as unconfigured as possible**
- Piggyback on the work of teams who evaluate and tweak prompts for each model release
- **Avoid MCP and skills unless absolutely necessary**, and keep them off by default

### AGENTS.md Discipline
When writing project prompt files:
- **Avoid behavior steering** — no "think step by step," "you are a skilled engineer," or "I'll tip you $200"
- **Limit to concrete, project-specific facts** about the codebase
- **Write prompts yourself** — don't let models auto-generate pages of barely-reviewed prompt text (same reason you wouldn't let them auto-generate pages of code)
- **Delete prompts when you can** — same instinct as deleting dead code

### Counterpoint: The Harness Engineering View
The [[agent-harness]] philosophy (notably articulated by [[garry-tan]] and practitioners of [[hermes-agent]]) takes the opposite view — that carefully engineered prompts, skills, and metaprompting are the key differentiator. See comparison at [[agent-harnesses]].

This tension between "minimal prompting" and "engineering the harness" is one of the central debates in AI agent engineering in 2026.

## Comparison to Code Technical Debt

| Aspect | Code Technical Debt | Prompt Technical Debt |
|---|---|---|
| Detection | Errors, slowdowns on change | Silent decay, no errors |
| Stability | Stable when untouched | Breaks with every model upgrade |
| Maintenance | Refactoring efforts | Requires re-tuning per model |
| Accumulation rate | Gradual | Rapid (new models every few months) |
| Best practice | Write as little as possible | Keep as unconfigured as possible |

## Related Concepts
- [[agent-harness]] — The opposing view: invest deeply in prompt engineering
- [[metaprompting]] — The broader practice of prompting systems that prompt
- [[agent-architecture-decomposition]] — How agent systems distribute prompting across components
- [[ralph-loop]] — A specific agent workflow pattern (a form of prompting)
- [[ai-agent-engineering]] — The engineering discipline around AI agents
- [[model-routing]] — Choosing which model to use (a prompt-level decision)

## Source
Based on Sean Goedecke's blog post "Prompts are technical debt too" (May 2026). See [[seangoedecke.com--prompts-are-technical-debt-too--2bd50f80]] for the full article.
