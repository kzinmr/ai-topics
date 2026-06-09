---
title: "Building Towards Self-Driving Codebases with Long-Running, Asynchronous Agents — Aman Sanger (Cursor) at NVIDIA GTC 2026"
created: 2026-04-12
author: Aman Sanger (@aman_sanger)
source: YouTube
url: https://www.youtube.com/watch?v=2Fp3jIrFTMo
type: talk
duration: "37:48"
tags: [coding-agents, async-agents, multi-agent, cursor, self-driving-codebases, cloud-agents, agentic-engineering, nvidia, gtc-2026]
---

# Talk Overview

Aman Sanger, co-founder and CTO of Cursor, presents at NVIDIA GTC 2026 on the evolution of AI coding — from autocomplete to synchronous agents to async cloud agents, culminating in the vision of "self-driving codebases" where agents autonomously build, fix, and maintain software with minimal human intervention.

## Three Eras of AI Coding

### Era 1: Autocomplete (2021–2023)
- Tab-complete / IntelliSense-level predictions
- Models predicted next few minutes of edits based on recent editor context
- Cursor launched during this era

### Era 2: Synchronous Coding Agents (2024–present)
- Models became capable of generating whole features from natural language instructions
- 2025 was "the year coding agents completely took off"
- By end of 2025, the vast majority of code in Cursor came from agents rather than tab completions
- Agent requests surpassed tab accepts — remarkable because every keystroke can trigger tab, yet users submitted more full prompts

### Era 3: Async Agents (emerging)
- Agents need their own cloud environments — can't run tens of agents on local machines
- Must be able to test work (computer use, running tests) which is resource-intensive
- Agents should have the full suite of developer tools

## Cursor Cloud Agent

- Runs agents in VMs with full desktop access
- Agents can use the computer to test features visually
- 30% of Cursor's merged PRs come from cloud agents (as of Feb 2026)
- Example: video rendering refactor (React → Rust, 25x faster, 8-hour agent run)
- Example: 10,000-line PR for network policy controls in sandbox processes

## Artifacts: Reviewing Agent Outputs

The key insight for making cloud agents tractable: **review artifacts, not code**.

- **Video artifacts**: Agent records a video of the fully functioning feature after implementing it. Engineer reviews the video to verify correctness before looking at code. If it's wrong, reprompt without reading code.
- **Research reports**: For ML experiments, agents produce research reports summarizing findings — far easier to grok than code diffs.
- **Architecture diagrams / plans**: Potential artifacts for backend/infra work.
- **Overtesting**: Agents can run tests that aren't checked into the codebase — disposable verification artifacts.

The "Artifacts" release internally caused a major uptick in cloud agent adoption.

## Train Time vs Test Time

Core technical insight: RL-trained agents perform well when test tasks match training distribution.

- Single agent running for tens of millions of tokens → falls apart (outside training distribution)
- **Multi-agent solves this**: each subtask is simpler, well within training distribution
- Outer planner runs for hundreds of thousands of tokens, not millions
- Sub-agents handle the detailed work

## Multi-Agent Architecture

- **Planner + sub-planners + workers** (recursive hierarchy)
- Model specialization by capability:
  - **OpenAI models**: strongest at high-level planning and orchestration
  - **Gemini / Anthropic models**: stronger at computer use and multi-modal understanding
  - **Anthropic models**: better at creating UIs
- Cloud agents use OpenAI as planner, other models for computer use and visual verification
- Simpler sub-agent tasks can use faster, cheaper models with same quality

### Weaknesses
- Outer agent still hits limits at very long task durations
- Models not yet excellent at orchestrating agents — RL training benefits workers more than orchestrators
- "Model UX" — models must learn to produce useful, reviewable artifacts (not just code)

## Self-Driving Codebases (Terminal State)

Two components:

### 1. Self-Healing and Fixing
- **Automations**: Triggered by events (issue tracker, on-call pages)
  - Every issue → agent proposes a fix
  - Every page at 2am → agent investigates, proposes solution (single click to fix)
  - Goal: agents as primary on-call, humans as secondary escalation
- **Training monitoring**: Agents run every few steps during training, check logs/weights/biases, flag potential failures before runs crash
- **Code review + security**: Agents find PRs with vulnerabilities that would have shipped

### 2. Building Full Projects
- Browser project: 1-week agent run, billions of tokens, tens of thousands of dollars
  - Rendering engine, JavaScript sandbox, full browser complexity
  - Produced a working (but not production-ready) browser
- Harness: recursive planner → sub-planners → workers
- Multimodal: different models for planning vs. computer use vs. UI

## The Role of the Engineer

- **Spec writing**: Engineers will focus on detailed, verifiable specs (implementation plan + evaluation suite)
- **Taste**: Product taste, UX decisions — hardest for models to learn
- **Architecture**: Infrastructure and code design decisions
- **"Don't lose to slop"**: Maintain quality standards, don't let velocity override taste
- **Holding more in your head**: Instead of deep code details, engineers hold the entire codebase at a higher abstraction level
- **Attention to detail shifts**: Same skill, different focus — product decisions, architectural review, artifact evaluation

## Cursor's Vision: R&D Cloud

- Old clouds = "cost of goods sold cloud" (infrastructure to deliver products)
- Cursor = "R&D cloud" helping enterprises build more ambitious software
- Scaling engineering 3x in 2026 — not cutting headcount despite AI productivity gains
- Want to tackle more ambitious things, compound excellent engineers with excellent tools

## Q&A Highlights

- **Education**: Education adapts extremely slowly. Organizations should allow AI use because "that's not what things will look like in the real world." Understanding code details still matters today but will matter less.
- **Taste**: "Don't lose to slop." Taste matters in product UX AND architecture/infra. Don't let velocity override design thinking.
- **Code review**: Models will get much better at code review (humans don't enjoy it, models can excel). Need better RL training for review specifically.
- **Interview process**: Final stage is 1-2 day onsite project using Cursor/agents. Scope has increased as agents improved. Tests agency, architecture decisions, product taste.
- **Legacy codebases**: Agents should actively improve codebases during off-peak hours — clean up tech debt, gnarly code. For understanding, spend more compute scaling up multi-agent approach.
- **Enterprise software proliferation**: More bottlenecked by quality of ideas than implementation ability. More startups, more products from existing companies.
- **Future engineer skills**: Holding lots in your head still valuable (but at higher abstraction — entire codebase, not just a function). Attention to detail shifts to product/architecture decisions.

## Connection to Wiki Concepts

- [[concepts/async-coding-agents]] — Core topic: async agents in cloud environments
- [[concepts/multi-agent]] — Planner/sub-planner/worker hierarchy as key architecture
- [[concepts/self-driving-codebases]] — Vision of autonomous codebase maintenance
- [[concepts/context-engineering]] — Spec writing as the new core engineering skill
- [[entities/aman-sanger]] — Speaker
- [[entities/cursor]] — Company
