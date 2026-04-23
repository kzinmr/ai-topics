---
title: Multi-Agents: What's Actually Working
category: other
status: active
---

# Multi-Agents: What's Actually Working
**Author:** Walden Yan (@walden_yan)
**Source:** https://cognition.ai/blog/multi-agents-whats-actually-working
**Published:** 2026-04-22 (X post), ~10 months after "Don't Build Multi-Agents"
**Summary:** Cognition deploys multi-agent systems that work in practice. Narrow class of patterns: multiple agents contribute intelligence while writes stay single-threaded. Three patterns: code-review-loop, smart-friend, manager-child delegation. Open problems are all communication.

## Key Patterns That Work

### 1. The Code-Review-Loop
- Devin (coding agent) + Devin Review (review agent)
- Catching average of 2 bugs per PR, 58% severe (logic errors, missing edge cases, security vulnerabilities)
- **Counterintuitive finding:** Works BEST when coding and review agents do NOT share context beforehand
- Clean context forces review agent to reason backward from implementation without spec
- Avoids "Context Rot" — models make less intelligent decisions at longer context lengths
- Shorter context → improved intelligence → increased detection of nuanced issues
- Communication bridge between agents is critical: Devin must use broader context to filter bugs from review
- Prevents: looping, disobeying user, out-of-scope work

### 2. Smart Friend Architecture
- Primary/smaller model (e.g., SWE-1.5 at 950 tok/sec) + smarter/expensive model as "smart friend" tool
- Primary model can call out to smart friend when task is tricky enough
- **Challenge 1:** Weaker model must know when it's at its limits
  - Solutions: encourage at least one call to evaluate trickiness, prompt-tune for calibration, domain-specific guidance
  - Context sharing: fork full context of primary model (80/20 solution)
  - Encourage broad questions ("what should I do?") rather than narrow ones
- **Challenge 2:** Smart friend must know how to talk back
  - Instruct primary model to investigate files it didn't look at
  - "Over-scoped" smart friend: suggest guidance based on agent trajectory even beyond the asked question
  - Generally leads to more interesting interactions
- **Reality check:** SWE-1.5 wasn't good enough as primary model — gap with Sonnet 4.5 too wide
- SWE-1.6 (Opus-4.5 level on SWE-bench) closes gap enough for pattern to pay off
- Works well across frontier models (Claude + GPT) — cross-frontier communication is capability routing, not difficulty escalation

### 3. Higher-Level Delegation (Manager → Child Agents)
- Live in Devin: manager Devin breaks larger task into pieces, spawns child Devins, coordinates through internal MCP
- Trained on small-scoped delegation defaults to being overly prescriptive when manager lacks deep codebase context
- Agents assume they share state with children when they don't
- Cross-agent communication (sub-agent messages to manager for siblings) doesn't happen by default — models not trained in environments requiring it
- Unstructured swarms (arbitrary agent networks negotiating) considered "mostly a distraction"
- Practical shape: map-reduce-and-manage (manager splits work, children execute, manager synthesizes and reports back)

## Core Principles (Evolved from "Don't Build Multi-Agents")

### Original Principles (10 months ago):
1. Share as much context as possible between agents
2. Actions carry implicit decisions that can conflict

### Current Principles:
- **Writes stay single-threaded** — additional agents contribute intelligence, not actions
- **Clean context leads to capability improvement** in generator-verifier loops
- **Clear communication and synthesis** with overall context is critical
- **Smart friend works when both models are strong** — asymmetric weaker primary is still an open training problem
- **Open problems are all communication problems:**
  - How does a weaker model learn when to escalate?
  - How does a child agent surface discoveries to siblings?
  - How do you transfer context between agents without drowning the receiver?

## What Changed in Last 10 Months
- Models more naturally "agentic" — understand tool use, context limits, how to distill context
- Agent usage exploded (~8x in enterprise segment over 6 months)
- **Push side:** Users experiment with more multi-agent setups (Devins managing Devins, coding agents iterating with review agents)
- **Pull side:** Explosion of costs → need for frontier capabilities at lower cost
- New Mythos class of larger, more capable models on horizon

## Cognition's Stance
> "Multi-agent systems work best today when writes stay single-threaded and the additional agents contribute intelligence rather than actions."

Building toward: intelligence injected at every stage of SDLC — planning, coding, review, testing, monitoring — not as swarm of autonomous actors, but as coordinated system that scales human taste.

## Sources
- [Multi-Agents: What's Actually Working](https://cognition.ai/blog/multi-agents-whats-actually-working) — Cognition Blog, 2026-04-22
- [Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents) — Cognition Blog, ~2025-06 (10 months prior)
- X post: https://x.com/walden_yan/status/... (@walden_yan, 4月22日)
