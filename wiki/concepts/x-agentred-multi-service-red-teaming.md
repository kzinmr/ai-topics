---
title: "X-AgentRed — Red-Teaming Personal Agents Across Services"
created: 2026-10-12
updated: 2026-10-12
type: concept
tags: [red-teaming, agent-security, tool-use, ai-agents, agent-communication]
sources: [raw/papers/2026-10-09_2610.13886_x-agentred-multi-service-red-teaming.md]
confidence: high
related: [concepts/security-and-governance/agentic-security, concepts/prompt-injection, concepts/agent-tooling]
---

# X-AgentRed — Red-Teaming Personal Agents Across Services

Personal agents now chain tools across many web services and apps. Harm rarely comes from a
single malicious tool — it **accumulates and interacts across services** as the agent fulfills a
*benign* user request. Jung et al. (arXiv:2610.13886, Oct 2026) propose **X-AgentRed**, a
self-evolving red-teaming framework that finds these *compositional* failures by searching a
graph of tool dependencies rather than asking an LLM to imagine them.

## The gap it attacks

Existing red-teaming either (a) prompts an LLM to spot harmful paths from a task/environment
description, or (b) decomposes a human-specified harmful goal into benign-looking action
combinations. Both are **biased toward patterns seen in training**, so they favor familiar tool
combinations and under-explore genuinely novel cross-service interactions.

## Method

- Model each tool by its **effects, potential harms, and execution preconditions**.
- Build a **directed graph** capturing how one tool's effects can satisfy another tool's
  preconditions — i.e. how a chain of individually-legitimate calls composes into a harmful
  outcome.
- Sample "recipes" (paths) from the graph and instantiate them as realistic scenarios.
- **Execution feedback drives self-improvement**: diversify harmful paths via tool substitution,
  and refine preconditions at *blocked* steps of unsuccessful paths so further execution becomes
  possible.

## Results

Across four frontier agentic models, X-AgentRed achieves **1.77×** the harmful-path rate of STAC
and explores a more diverse tool set, yielding **2.99×** the tool coverage on average.

## Why it matters

This is the red-teaming analogue of [[concepts/skill-co-installation-conflict]] and the compositional-security
theme: the danger is an emergent property of the *tool graph*, invisible when auditing tools one
at a time. Because generation is training-biased, *discovering* cross-service paths by
construction + execution (rather than *imagining* them) is the real contribution. It connects to
[[concepts/security-and-governance/agentic-security]] and to prompt-injection / tool-abuse work —
the difference is X-AgentRed optimizes for path *novelty and coverage*, not for a single attack
payload.

## Related

- [[concepts/security-and-governance/agentic-security]]
- [[concepts/prompt-injection]]
- [[concepts/tool-orchestration]]
- [[concepts/skill-co-installation-conflict]]
