---
title: "Position: agentic AI orchestration should be Bayes-consistent"
source: arXiv (2605.00742)
date: 2026-05-01
venue: ICML 2026
url: https://arxiv.org/abs/2605.00742
tags: [ai-agents, orchestration, bayesian, decision-theory, research, icml]
---

# Position: agentic AI orchestration should be Bayes-consistent

**arXiv:2605.00742** — Accepted for publication at ICML 2026

## Abstract

LLMs excel at predictive tasks and complex reasoning tasks, but many high-value deployments rely on decisions under uncertainty — which tool to call, which expert to consult, or how many resources to invest. While the usefulness and feasibility of Bayesian approaches remain unclear for LLM inference, this position paper argues that the control layer of an agentic AI system (that orchestrates LLMs and tools) is a clear case where Bayesian principles should shine.

Bayesian decision theory provides a framework for agentic systems that can:
1. Maintain beliefs over task-relevant latent quantities
2. Update these beliefs from observed agentic and human-AI interactions
3. Choose actions based on expected utility

Making LLMs themselves explicitly Bayesian belief-updating engines remains computationally intensive. In contrast, coherent decision-making requires Bayesian principles at the **orchestration level** of the agentic system, not necessarily within the LLM agent parameters.

## Key Concepts

- **Value of Information (VoI)**: Only trigger a tool call or agent action when expected information gain outweighs costs and risks
- **Human feedback as probabilistic observation**: Human input refines the system's internal belief state, not just commands
- **Calibrated uncertainty**: The orchestration layer maintains a posterior distribution over task-relevant latent variables
- **Utility-aware policies**: Actions are chosen to maximize expected utility given current beliefs

## Practical Significance

This is especially critical in high-stakes environments where the cost of a wrong action (e.g., unauthorized financial transaction) is significantly higher than the cost of asking for clarification. The framework naturally handles the "when to escalate to human" problem that plagues current agentic systems.
