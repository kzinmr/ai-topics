---
title: "REAL"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - web-development
sources:
  - https://github.com/agi-inc/REAL
  - https://realevals.xyz
related_concepts:
  - concepts/ai-benchmarks/webarena
  - concepts/ai-benchmarks/webgames
  - concepts/ai-benchmarks/online-mind2web
---

# REAL

**REAL** (Realistic Environment for Agent Learning) is a benchmark for evaluating autonomous agents on deterministic simulations of real websites. Developed by AGI Inc (GitHub: agi-inc/REAL), it powers realevals.xyz and addresses the flakiness problem of live-site web benchmarks by providing reproducible Next.js replicas of popular websites with deterministic behavior.

**GitHub**: [agi-inc/REAL](https://github.com/agi-inc/REAL) | **Website**: [realevals.xyz](https://realevals.xyz)

## What It Measures

- **Domain**: Web agent capabilities on realistic website interactions
- **Task type**: Multi-step web tasks requiring navigation, form interaction, and goal completion
- **Format**: Agents interact with deterministic Next.js replicas of popular websites (Amazon, Uber, LinkedIn, etc.) that reproduce real site behavior without live-site variability
- **Evaluation**: Combines a **reproducible LLM evaluator** with **state validators** — checking both the agent's process and the final website state
- **Key distinction**: Fixes the fundamental flakiness problem of live-site web benchmarks by providing deterministic, reproducible website simulations

## Data/Methodology

REAL comprises **112 tasks** on deterministic website replicas:

| Replica Site | Original | Task Types |
|-------------|----------|------------|
| E-commerce | Amazon | Product search, cart, checkout flows |
| Ride-sharing | Uber | Booking, scheduling, fare comparison |
| Professional | LinkedIn | Profile management, job search, networking |
| Others | Various | Diverse web interaction patterns |

**Methodology**:
1. Real websites are replicated as **deterministic Next.js applications**
2. The replicas reproduce realistic UI and interaction patterns without live-site variability
3. Each task has a deterministic initial state (no content drift)
4. Evaluation combines **LLM-based process evaluation** with **programmatic state validation**
5. Results are fully reproducible across evaluation runs

## Key Results

- **Scale**: 112 tasks across deterministic replicas of popular websites
- **Reproducibility breakthrough**: Deterministic simulations eliminate the flakiness of live-site evaluations where content can change between runs
- **Dual evaluation**: LLM evaluator for process quality + state validators for outcome verification
- **Open-source**: Publicly available on GitHub with active community

## Related Benchmarks

- [[concepts/ai-benchmarks/webarena|WebArena]] — Self-hosted sandboxed websites (812 tasks); REAL extends this approach with more realistic site replicas
- [[concepts/ai-benchmarks/webgames|WebGames]] — 50+ client-side browser challenges with verifiable pass/fail
- [[concepts/ai-benchmarks/online-mind2web|Online-Mind2Web]] — Live-website evaluation that REAL's deterministic approach aims to complement
- [[concepts/ai-benchmarks/webvoyager|WebVoyager]] — Live-website benchmark (643 tasks) that REAL's approach addresses the flakiness of

## Connections to Other Wiki Concepts

- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation Methodology]] — REAL demonstrates the deterministic simulation approach to solving reproducibility challenges in web agent evaluation
- [[concepts/ai-benchmarks/swe-bench|SWE-bench]] — Both use containerized/determinized environments for reproducible evaluation — SWE-bench with Docker containers, REAL with Next.js replicas
