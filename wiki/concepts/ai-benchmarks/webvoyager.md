---
title: "WebVoyager"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - multimodal
  - web-development
sources:
  - https://arxiv.org/abs/2401.13919
related_concepts:
  - concepts/ai-benchmarks/webarena
  - concepts/ai-benchmarks/visualwebarena
  - concepts/ai-benchmarks/browsecomp
---

# WebVoyager

**WebVoyager** is a benchmark and end-to-end web agent built with large multimodal models. Introduced by He et al. from Tencent AI Lab (arXiv 2401.13919), it tests agent navigation across 15 live real-world websites with 643 tasks. WebVoyager is notable for being an early, widely-cited example of using a multimodal LLM (GPT-4V) as an automatic judge for evaluating live-web agent trajectories.

**Paper**: [arXiv 2401.13919](https://arxiv.org/abs/2401.13919)

## What It Measures

- **Domain**: End-to-end web navigation using multimodal models
- **Task type**: Real-world web tasks requiring visual understanding and multi-step navigation
- **Format**: Agents must navigate across 15 live (non-sandboxed) real-world websites to complete tasks, processing both visual screenshots and HTML content
- **Evaluation**: GPT-4V-based automatic judge evaluates whether the agent's final trajectory achieves the task goal — an early multimodal LLM-as-judge protocol for web agents
- **Key distinction**: Operates on live real-world websites rather than sandboxed replicas, testing agents in production-like conditions

## Data/Methodology

WebVoyager comprises **643 tasks** across **15 live real-world websites** spanning diverse domains:

**Website Coverage**:
- Covers e-commerce, search engines, travel booking, news, and other common web domains
- All websites are live production sites (not self-hosted replicas)
- Tasks require multi-step navigation chains across multiple pages

**Methodology**:
1. Agents receive natural language task descriptions
2. Agents observe screenshots of current web pages and issue actions (click, type, scroll)
3. Navigation proceeds through iterative observation-action cycles
4. A **GPT-4V automatic judge** evaluates the final trajectory for task completion
5. The multimodal judge can assess both visual state and task outcome

## Key Results

- **Scale**: 643 tasks across 15 live real-world websites
- **Multimodal evaluation pioneer**: One of the earliest benchmarks to use a multimodal LLM (GPT-4V) as an automatic judge for agent trajectory evaluation
- **Live website testing**: Unlike sandboxed benchmarks, WebVoyager tests agents against production websites where content may change
- **End-to-end evaluation**: Tests the complete agent pipeline from visual perception to action execution to goal achievement

## Related Benchmarks

- [[concepts/ai-benchmarks/webarena|WebArena]] — Sandbox-based web agent benchmark (812 tasks) with URL-based state verification
- [[concepts/ai-benchmarks/visualwebarena|VisualWebArena]] — Multimodal extension of WebArena with 910 visually-grounded tasks
- [[concepts/ai-benchmarks/browsecomp|BrowseComp]] — OpenAI's benchmark for deep-research browsing (1,266 questions)
- [[concepts/ai-benchmarks/online-mind2web|Online-Mind2Web]] — Another live-website evaluation challenging optimistic benchmark results

## Connections to Other Wiki Concepts

- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation Methodology]] — WebVoyager pioneered the multimodal LLM-as-judge approach for evaluating agent trajectories on live websites
- [[concepts/ai-benchmarks/real-benchmark|REAL]] — Both address the challenge of evaluating web agents on realistic websites, but REAL uses deterministic simulations while WebVoyager uses live sites
