---
title: "Multi-Agents: What's Actually Working"
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [multi-agent, agentic-engineering, agent-team-swarm, context-window-management, code-review]
sources:
  - raw/articles/2026-04-22-multi-agents-whats-actually-working.md
related:
  - concepts/multi-agent-autonomy-scale.md
  - concepts/agent-team-swarm.md
  - concepts/back-of-house-multi-agent-patterns.md
  - concepts/cognition-devin-philosophy.md
  - concepts/context-window-management.md
---

# Multi-Agents: What's Actually Working

## Overview

Cognition's April 2026 blog post "Multi-Agents: What's Actually Working" by Walden Yan represents a significant evolution from their June 2025 stance "Don't Build Multi-Agents." The core finding: **multi-agent systems work best when writes stay single-threaded and additional agents contribute intelligence rather than actions.**

## Three Working Patterns

### 1. The Code-Review-Loop
- **Architecture:** Devin (coding agent) + Devin Review (review agent)
- **Performance:** Catches average 2 bugs per PR, 58% severe (logic errors, missing edge cases, security vulnerabilities)
- **Counterintuitive finding:** Works BEST when coding and review agents do NOT share context beforehand
  - Clean context forces review agent to reason backward from implementation without spec
  - Avoids "Context Rot" — models make less intelligent decisions at longer context lengths
  - Shorter context → improved intelligence → increased detection of nuanced issues
- **Communication bridge critical:** Devin must use broader context to filter bugs from review
- **Prevents:** looping, disobeying user, out-of-scope work

### 2. Smart Friend Architecture
- **Primary/smaller model** (e.g., SWE-1.5 at 950 tok/sec) + **smarter/expensive model** as "smart friend" tool
- **Primary model can call out** to smart friend when task is tricky enough
- **Challenge 1:** Weaker model must know when it's at its limits
  - Solutions: encourage at least one call to evaluate trickiness, prompt-tune for calibration, domain-specific guidance
  - Context sharing: fork full context of primary model (80/20 solution)
  - Encourage broad questions ("what should I do?") rather than narrow ones
- **Challenge 2:** Smart friend must know how to talk back
  - Instruct primary model to investigate files it didn't look at
  - "Over-scoped" smart friend: suggest guidance based on agent trajectory even beyond the asked question
- **Reality check:** SWE-1.5 wasn't good enough as primary model — gap with Sonnet 4.5 too wide
  - SWE-1.6 (Opus-4.5 level on SWE-bench) closes gap enough for pattern to pay off
- **Works well across frontier models** (Claude + GPT) — cross-frontier communication is capability routing, not difficulty escalation

### 3. Higher-Level Delegation (Manager → Child Agents)
- **Live in Devin:** manager Devin breaks larger task into pieces, spawns child Devins, coordinates through internal MCP
- **Trained on small-scoped delegation** defaults to being overly prescriptive when manager lacks deep codebase context
- **Agents assume they share state** with children when they don't
- **Cross-agent communication** (sub-agent messages to manager for siblings) doesn't happen by default — models not trained in environments requiring it
- **Unstructured swarms** (arbitrary agent networks negotiating) considered "mostly a distraction"
- **Practical shape:** map-reduce-and-manage (manager splits work, children execute, manager synthesizes and reports back)

## Core Principles Evolution

### Original Principles (June 2025 - "Don't Build Multi-Agents"):
1. Share as much context as possible between agents
2. Actions carry implicit decisions that can conflict

### Current Principles (April 2026):
- **Writes stay single-threaded** — additional agents contribute intelligence, not actions
- **Clean context leads to capability improvement** in generator-verifier loops
- **Clear communication and synthesis** with overall context is critical
- **Smart friend works when both models are strong** — asymmetric weaker primary is still an open training problem
- **Open problems are all communication problems:**
  - How does a weaker model learn when to escalate?
  - How does a child agent surface discoveries to siblings?
  - How do you transfer context between agents without drowning the receiver?

## What Changed in 10 Months
- Models more naturally "agentic" — understand tool use, context limits, how to distill context
- Agent usage exploded (~8x in enterprise segment over 6 months)
- **Push side:** Users experiment with more multi-agent setups (Devins managing Devins, coding agents iterating with review agents)
- **Pull side:** Explosion of costs → need for frontier capabilities at lower cost
- New Mythos class of larger, more capable models on horizon

## Cognition's Stance
> "Multi-agent systems work best today when writes stay single-threaded and the additional agents contribute intelligence rather than actions."

Building toward: intelligence injected at every stage of SDLC — planning, coding, review, testing, monitoring — not as swarm of autonomous actors, but as coordinated system that scales human taste.

## Relation to Existing Wiki Concepts

### Multi-Agent Autonomy Scale (5-Level Model)
Cognition's patterns map to the existing 5-level model:
- **Code-Review-Loop** → L3 Agent-Assisted (human-in-the-loop review)
- **Smart Friend** → L2 Chat-Assisted (weaker model + stronger advisor)
- **Manager → Child** → L4 Engineering Team (orchestrated delegation)

### Open Problems
The communication challenges identified by Cognition align with:
- [[concepts/context-window-management]] — how to distill context without loss
- [[concepts/agent-team-swarm]] — coordination patterns for multi-agent systems
- [[concepts/multi-agent-consensus-patterns]] — how agents reach agreement

## Sources
- [Multi-Agents: What's Actually Working](https://cognition.ai/blog/multi-agents-whats-actually-working) — Cognition Blog, 2026-04-22
- [Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents) — Cognition Blog, ~2025-06 (10 months prior)
- X post: https://x.com/walden_yan/status/... (@walden_yan, 4月22日)