---
title: "Online-Mind2Web"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - web-development
sources:
  - https://arxiv.org/abs/2504.01382
related_concepts:
  - concepts/ai-benchmarks/mind2web-2
  - concepts/ai-benchmarks/webarena
  - concepts/ai-benchmarks/real-benchmark
---

# Online-Mind2Web

**Online-Mind2Web** is a benchmark that challenges optimistic web agent results by assessing the true current state of web agent capabilities. Introduced by Xue et al. from the OSU NLP Group (arXiv 2504.01382), it evaluates 300 realistic tasks on 136 live websites using an LLM-as-a-Judge auto-grader (~85% human agreement). The benchmark exposes overstated progress claims by comparing sophisticated web agents against simple baselines on live websites.

**Paper**: [arXiv 2504.01382](https://arxiv.org/abs/2504.01382)

## What It Measures

- **Domain**: Real-world web agent capabilities on live websites
- **Task type**: Realistic web tasks performed on live (non-sandboxed) websites
- **Format**: 300 tasks distributed across 136 real-world websites, testing agents under production conditions
- **Evaluation**: **LLM-as-a-Judge** auto-grader with ~85% human agreement — evaluates whether the agent's final web state achieves the task goal
- **Key distinction**: Explicitly designed to challenge optimistic benchmark results — shows that progress on sandboxed benchmarks may not transfer to live-web performance

## Data/Methodology

Online-Mind2Web comprises **300 tasks** on **136 live websites**:

**Design Philosophy**:
- Tasks are performed on live production websites (not sandboxed replicas)
- The benchmark was created specifically to test whether sandboxed benchmark progress transfers to real-world performance
- Includes comparison against simple baselines to contextualize agent performance

**Methodology**:
1. Tasks are defined on 136 real-world websites spanning diverse domains
2. Agents must interact with live websites where content may change
3. An **LLM-as-a-Judge** evaluates task completion:
   - ~85% agreement with human annotators
   - Handles the inherent ambiguity of live-web evaluation
4. Results are compared against simple baseline strategies
5. The comparison reveals whether complex agents genuinely outperform simple approaches on live websites

## Key Results

- **Scale**: 300 tasks across 136 live websites
- **Reality check**: Exposes that progress on sandboxed benchmarks (like WebArena) may be overstated when evaluated on live websites
- **Baseline comparison**: Shows that sophisticated web agents don't always significantly outperform simpler approaches in live-web settings
- **LLM judge calibration**: ~85% human agreement establishes reasonable automated evaluation reliability

## Related Benchmarks

- [[concepts/ai-benchmarks/mind2web-2|Mind2Web 2]] — Companion benchmark by the same OSU NLP Group using Agent-as-a-Judge for agentic search evaluation
- [[concepts/ai-benchmarks/webarena|WebArena]] — Sandbox-based web agent benchmark (812 tasks); Online-Mind2Web tests whether WebArena-style progress transfers to live sites
- [[concepts/ai-benchmarks/real-benchmark|REAL]] — Deterministic website simulations; Online-Mind2Web's live-site approach contrasts with REAL's reproducibility-focused design
- [[concepts/ai-benchmarks/webvoyager|WebVoyager]] — Another live-website benchmark (643 tasks on 15 sites) with multimodal evaluation

## Connections to Other Wiki Concepts

- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation Methodology]] — Online-Mind2Web demonstrates the importance of evaluating agents in realistic (live) conditions rather than only in sandboxed environments
- [[concepts/ai-benchmarks/swe-bench|SWE-bench]] — Both face the tension between controlled evaluation and real-world validity; SWE-bench uses fixed codebases while Online-Mind2Web uses live websites to capture real-world complexity
