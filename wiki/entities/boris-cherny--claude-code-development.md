---
title: "Boris Cherny — Claude Code Development Story"
type: entity
parent: boris-cherny
created: 2026-04-28
updated: 2026-08-03
tags:
  - person
  - anthropic
  - model
  - coding-agents
  - opus-5
  - prompt-injection
sources:
  - raw/articles/ycrootaccess.com--p-boris-cherny-building-claude-code--f3769a9e.md
---

# Boris Cherny: Claude Code Development Story

Back to main profile: [[entities/boris-cherny]]

## Origins (Sep 2024 – Nov 2024)

Claude Code began when Boris joined Anthropic in September 2024 and started prototyping with the Claude 3.6 model. His first prototype was a **command-line tool to identify and change music via AppleScript** — this evolved into the core of Claude Code. The prototyping drew from an earlier Anthropic research project called **Clide**, which influenced Boris's approach despite its inefficiencies (slow startup times, heavy indexing requirements).

By November 2024, an internal dogfooding-ready version was released:
- **20% of Anthropic's engineering team** adopted it on day one
- **50% adoption by day five**
- Rapid iterative refinement through constant internal feedback

The tool reached **general availability in May 2025**, after which the team expanded to around 10 engineers by July 2025.

## Key Development Challenges

- **Filesystem access**: Adding tools for reading, writing, and running batch commands while preventing unintended file deletions through a robust permissions system with static analysis
- **Minimizing business logic**: Letting the AI model operate as "raw" as possible — deleting portions of the system prompt as models improved
- **Local vs virtualized execution**: Opting for local execution for simplicity, balancing performance and safety
- **High-velocity prototyping**: Boris built ~20 prototypes for features like todo lists over two days, testing 5-10 ideas daily with AI agents
- **60-100 internal releases per day** — bottom-up feature building based on individual team needs

## Team & Collaboration

- **Sid Bidasaria** (joined Nov 2024) — rapid iterations and subagent development, completed key features in just three days through experimental approaches
- **Cat Wu** (founding product manager) — researched AI agent usage, provided feedback that expanded the tool's scope
- **Dogfooding culture**: 70-80% of technical staff used Claude Code daily, generating constant input via internal channels

## Startup School 2026 Interview (Aug 2026)

At YC Startup School 2026, Boris discussed the Opus 5 release and Claude Code's evolution. Key insights:

### Opus 5 Capabilities
- **Extended autonomous runs**: Opus 5 can run for days, weeks, or months continuously — no scaffolding needed
- **Prompt injection resistance**: Combined with a mechanistic interpretability-based classifier (from Crysola's neuron-level detection work) and auto mode classifier, Opus 5 cannot be prompt-injected. This has been effective since Opus 4.7/4.8
- **80% system prompt deletion**: The Claude Code team deleted 80% of the system prompt for Opus 5 — the model now infers behaviors that previously required explicit instructions

### Product Overhang & Unhobbling
Boris introduced the concept of **product overhang**: models have capabilities that current products fail to elicit. Claude Code itself was born from unhobbling Sonnet 3.5 — moving from single-line autocomplete to full file writes. The key advice:
- Give models slightly harder tasks than you think they can do
- Provide verification mechanisms, not micro-instructions
- Let models "cook" with high-level goals + guardrails + exit criteria

### Dynamic Workflows & Agent Orchestration
Claude Code's **dynamic workflows** enable orchestrating thousands of agents via an "algebra for agents" (sequential, parallel, fan-out patterns). Example: Bun's Zig→Rust rewrite ran for 11 days with thousands of agents, replacing 1+ year of engineering work. This represents a new form of **test-time compute scaling**.

### Self-Maintaining Codebases
Anthropic runs ~20-30 daily routines across all Claude Code codebases: dead code cleanup, shipping experiments, writing/deleting tests, and an "abstraction police" that unifies nearly-duplicated abstractions. Hundreds to thousands of agents run daily.

### Prompt Engineering Evolution
Boris argues prompt engineering is evolving toward **empirical model elicitation** — the skill is figuring out how to give Claude a hard task and letting it verify its own work. "Don't listen to LinkedIn influencers" — the approach is scientific: try, observe failure, adjust.

### Coding Is (Almost) Solved
Caveat: solved for Boris's kind of coding. Deep systems code, distributed systems, and pixel-level UI verification remain challenging. But for an increasing fraction of work, agents write 100% of code.

Source: [[raw/articles/ycrootaccess.com--p-boris-cherny-building-claude-code--f3769a9e]]

## See Also

- [[entities/boris-cherny--core-ideas|Core Ideas & Philosophy]]
- [[entities/boris-cherny--key-work|Key Work & Impact]]
