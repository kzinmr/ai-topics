---
title: "Bayesian Agent Orchestration"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [ai-agents, orchestration, rationality, research, human-in-the-loop]
sources: [raw/articles/2026-05-01_arxiv-bayesian-agent-orchestration.md]
---

# Bayesian Agent Orchestration

A position paper (arXiv:2605.00742, accepted at ICML 2026) arguing that the **control layer** of agentic AI systems — not the LLMs themselves — should be governed by Bayesian decision theory.

## Core Argument

Making individual LLMs explicitly Bayesian is computationally intensive and conceptually nontrivial. But the orchestration layer that manages which tools to call, which experts to consult, and when to escalate to humans is a natural fit for Bayesian principles.

## Three Bayesian Mechanisms

1. **Belief Maintenance**: The controller maintains a posterior distribution over task-relevant latent variables
2. **Belief Updating**: Human feedback is treated as probabilistic observation that refines the internal belief state, not just as commands
3. **Utility-Aware Action Selection**: Actions maximize expected utility given current beliefs

## Value of Information (VoI)

The controller only triggers a tool call or agent action when the expected information gain outweighs costs and risks. In high-stakes environments (e.g., financial transactions), the cost of a wrong action far exceeds the cost of asking for clarification — VoI naturally captures this asymmetry.

## Practical Impact

This addresses the "when to escalate to human" problem that plagues current agentic systems. Rather than hard-coded thresholds, the system maintains calibrated uncertainty and escalates when the expected value of human input exceeds the cost.

## Related Pages
- [[concepts/ai-agents]] — AI agent architectures
- [[concepts/agentic-engineering]] — Agentic software engineering
- [[concepts/human-in-the-loop]] — Human-in-the-loop patterns
