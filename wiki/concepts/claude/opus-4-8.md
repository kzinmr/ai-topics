---
title: "Claude Opus 4.8"
type: concept
created: 2026-05-30
updated: 2026-06-08
tags:
  - concept
  - anthropic
  - model
  - coding-agents
  - orchestration
  - workflow
  - test-time-scaling
  - agent-communication
sources:
  - https://www.anthropic.com/news/claude-opus-4-8
  - raw/articles/simonwillison.net--2026-may-28-claude-opus-4-8--8d05463f.md
  - raw/articles/2026-06-07_kilocode_audit-claude-opus-4-8-vs-minimax-m3.md
---

# Claude Opus 4.8

**Claude Opus 4.8** is a frontier LLM released by **Anthropic on May 28, 2026**. It is the successor to [[concepts/claude-opus-4-7|Claude Opus 4.7]], delivering improvements across benchmarks and introducing three major platform features: **Dynamic Workflows**, **Effort Control**, and **Mid-conversation System Messages**.

## Release Information

- **Release date**: May 28, 2026
- **Predecessor**: Claude Opus 4.7 (April 16, 2026)
- **API model ID**: `claude-opus-4-8`
- **Availability**: Claude API, claude.ai, Claude Code, Cowork
- **Pricing**: Unchanged from Opus 4.7 — $5/M input tokens, $25/M output tokens
- **Fast mode**: $10/M input, $50/M output (now 3× cheaper than previous fast modes)
- **Fast mode speed**: 2.5× the speed of regular mode

## Key Capabilities

### Benchmark Performance

Opus 4.8 is described as "a modest but tangible improvement" over Opus 4.7. Notable results:

- **Super-Agent benchmark**: Only model to complete every case end-to-end, beating prior Opus models and [[concepts/gpt/gpt-5-5|GPT-5.5]] at parity on cost
- **CursorBench**: Exceeds prior Opus models across every effort level; more efficient tool calling (fewer steps for same intelligence)
- **Online-Mind2Web** (computer-use/browser-agent): 84% score — "meaningful jump" over Opus 4.7 and GPT-5.5
- **Legal Agent Benchmark**: Highest score recorded; first model to break 10% overall on the all-pass standard
- **Databricks Genie**: Step change in agentic reasoning; 61% cheaper token cost than Opus 4.7 for multimodal PDF/diagram reasoning

### Honesty and Self-Correction

A prominent improvement in Opus 4.8 is its **honesty** — the model is trained to avoid making unsupported claims. Early testers report it proactively flags issues with inputs and outputs, rather than leaving users to catch errors. This represents a shift toward models that are not just more capable, but more trustworthy collaborators.

## Three Major Platform Features

### 1. Dynamic Workflows (Claude Code)

A new feature (research preview) that allows Claude Code to tackle **codebase-scale problems** by:

- **Planning** the work upfront
- **Running hundreds of parallel subagents** in a single session
- **Verifying outputs** before reporting back to the user
- **Longer agent runs** — Opus 4.8 agents can run for extended durations compared to previous models

This enables migrations across hundreds of thousands of lines of code "from kickoff to merge, with the existing test suite as its bar." Available in Claude Code for Enterprise, Team, and Max plans.

**Significance**: This is a fundamental architectural shift from single-agent interaction to **multi-agent orchestration within a single session**. It parallels the [[entities/cognition|Cognition]] async agents architecture but operates within the Claude Code environment rather than as a standalone agent platform.

### 2. Effort Control (claude.ai and Cowork)

A new UI control alongside the model selector that lets users choose **how much effort** Claude puts into a response:

- **Higher effort**: Claude thinks more frequently and more deeply → better responses, higher token usage
- **Lower effort**: Claude responds faster → lower token usage, less rate limit consumption

This gives users direct control over the **compute-vs-quality tradeoff**, available on all plans.

**Significance**: Effort control operationalizes the concept of **test-time compute scaling** (related to [[concepts/reasoning|reasoning models]] and test-time scaling). Users can now explicitly dial up or down the amount of "thinking" the model does, rather than this being a fixed property of the model.

### 3. Mid-conversation System Messages (Messages API)

The Messages API now accepts **system entries inside the messages array**. This allows developers to:

- Update Claude's instructions **mid-task** without breaking the prompt cache
- Route updates **without going through a user turn**
- Dynamically adjust permissions, token budgets, or environment context as an agent runs

**Significance**: Previously, system prompts were fixed at session start. This change enables **dynamic agent reconfiguration** during long-running tasks — essential for [[concepts/agent-team-swarm/agent-orchestration|agent orchestration]] workflows where permissions or constraints need to change based on intermediate results.

## Code Audit Benchmark vs MiniMax M3 (June 2026)

[[entities/kilo|Kilo Code]] ran a controlled code-audit benchmark comparing Opus 4.8 at four reasoning levels against [[concepts/minimax-m3|MiniMax M3]] on a TypeScript webhook delivery service with 17 known issues ([source](https://x.com/kilocode/status/2063719228499542327)).

| Reasoning Level | Issues Found | Cost | Time |
|----------------|-------------|------|------|
| medium | 13/17 | $1.30 | 3m 53s |
| high | 13/17 | $1.93 | 4m 33s |
| xhigh | 15/17 | $2.03 | 7m 26s |
| max | 15/17 | $3.39 | 9m 24s |

**Key findings:**
- **xhigh was the sweet spot** — best coverage (15/17) at reasonable cost ($2.03)
- **max was not justified** — matched xhigh's count, cost 67% more, missed one finding xhigh caught
- **Reasoning level changed attention focus, not just depth** — medium/high caught async-in-sync-transaction (xhigh/max missed it); xhigh caught secret-returning endpoint (max missed it)
- **vs MiniMax M3** ($0.07, 13/17): M3 matched medium/high at ~1/18th the cost but trailed xhigh/max by 2 issues
- Effort Control (introduced with Opus 4.8) was central to this experiment's design

## Related

- [[concepts/claude-opus-4-7]] — predecessor model
- [[entities/anthropic]] — developer
- [[concepts/dynamic-workflows]] — new architectural pattern introduced with Opus 4.8
- [[concepts/claude/effort-control]] — user-controllable compute scaling
- [[entities/cognition]] — competitor's async agents architecture (similar concept, different implementation)
- [[concepts/gpt/gpt-5-5]] — competing model from OpenAI
