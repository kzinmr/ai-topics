---
title: "Akira (@realmcore_) / Random Labs"
type: entity
created: 2026-04-13
updated: 2026-05-25
tags:
  - person
  - coding-agents
  - rlm
  - multi-agent
  - startup
  - ycombinator
aliases:
  - realmcore_
  - Random Labs
  - Akira (Random Labs)
sources:
  - https://www.ycombinator.com/companies/random-labs
  - https://randomlabs.ai/about
  - https://venturebeat.com/orchestration/y-combinator-backed-random-labs-launches-slate-v1-claiming-the-first-swarm
  - https://xarticl.es/articles/we-built-rlm-for-coding-and-it-fcking-rocks-swarm-native-agents-are-here-to-stay
---

# Akira (@realmcore_) — Random Labs / Slate

**Akira** (@realmcore_) is a co-founder of **Random Labs** (YC S24), creators of **Slate** — the industry's first "swarm-native" autonomous coding agent. Slate uses a novel **Thread Weaving** architecture for parallel, long-horizon engineering tasks.

## Overview

Akira is part of the founding team at Random Labs, a Y Combinator-backed (S24) startup based in San Francisco that builds AI coding agents for long-running, complex engineering tasks. Random Labs was founded in 2024 and is building Slate as an open-source-first coding agent designed to work alongside developers for hours on hard problems.

The company's mission is to create general software agents and interfaces that allow engineers to maximally leverage them, bridging the global engineering shortage by positioning Slate as a collaborative tool for the "next 20 million engineers."

## Slate: Swarm-Native Coding Agent

Slate was launched in open beta in early 2026, with V1 released in March 2026. It is described as the first "swarm-native" agentic coding platform — orchestrating multiple specialized AI models in parallel rather than running a single agent sequentially.

### Key Architectural Innovations

**Thread Weaving**: Slate's core architecture runs a central orchestrator thread that dispatches parallel worker threads using a TypeScript-based DSL. Each worker handles a bounded sub-task (editing a file, running tests, researching documentation). Workers return compressed "episodes" (successful tool calls, conclusions) rather than full execution transcripts, while the orchestrator weaves these into a coherent task state.

**Episodic Memory**: Slate retains only the tool calls that contribute to its success, using a rolling compression system that enabled single sessions as long as 2 days during V0 beta.

**Dynamic Pruning Algorithm**: Maintains context in large codebases while scaling output to enterprise complexity.

**Model-Agnostic Routing**: Dynamically routes tasks across Claude, Codex, GLM, and other models based on task type.

### Performance

- Internal testing: passed two-thirds of tests on Terminal Bench 2.0's `make-mips-interpreter` task (where Opus 4.6 succeeds <20% in standard harnesses)
- Published case study: ported a Python library to TypeScript for ~$58 in credits

### Key Philosophy

> "The bottleneck in AI agents isn't intelligence. It's memory management." — Random Labs co-founder

The team's core insight: the differentiating factor in AI coding tools is shifting from model capabilities to **agent infrastructure** — memory management, context routing, execution environments, error recovery, and human-in-the-loop interfaces.

## RLM (Reinforcement Learning for Models) Advocacy

Akira and the Random Labs team are strong advocates of **RLM for coding**, arguing that reinforcement learning directly applied to coding agents produces significantly better results than prompt engineering or fine-tuning alone. This positions Slate as a testbed for RL-based coding agent training.

## Related Entities

- [[entities/scott-wu]] — Fellow coding agent builder (Devin/Cognition)
- [[entities/pi]] — Another coding agent (pi-dev / Mario Zechner)
- [[entities/openai-codex]] — Model used in Slate's multi-model orchestration

## Related Concepts

- [[concepts/swarm-agents]] — Slate's foundational architecture concept
- [[concepts/rlm]] — Reinforcement Learning for Models; core to Slate's approach
- [[concepts/agent-memory]] — Episodic memory and compression in Slate
- [[concepts/agent-orchestration]] — Thread Weaving as multi-agent orchestration pattern
- [[concepts/coding-agents]] — Slate as a coding agent implementation

## Company: Random Labs

| Detail | Value |
|--------|-------|
| **Founded** | 2024 |
| **Accelerator** | Y Combinator S24 |
| **Location** | San Francisco, CA |
| **Product** | Slate (swarm-native coding agent) |
| **Install** | `npm i -g @randomlabs/slate` |
| **Website** | [randomlabs.ai](https://randomlabs.ai) |
| **Contact** | team [@] randomlabs.ai |

## Sources

- [Y Combinator Profile: Random Labs](https://www.ycombinator.com/companies/random-labs)
- [VentureBeat: Random Labs launches Slate V1](https://venturebeat.com/orchestration/y-combinator-backed-random-labs-launches-slate-v1-claiming-the-first-swarm)
- [Xarticl.es: We built RLM for coding (by @realmcore_)](https://xarticl.es/articles/we-built-rlm-for-coding-and-it-fcking-rocks-swarm-native-agents-are-here-to-stay)
- [Random Labs About](https://randomlabs.ai/about)
- [FyI Combinator: Random Labs](https://fyicombinator.com/company/random-labs)
- [Seedwire: Slate V1 Memory Analysis](https://seedwire.co/news/rando-labs-unleashes-slate-v1-the-dawn-of-swarm-native-coding-agents)
