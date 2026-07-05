---
title: "AgentDojo"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - safety
  - agent-safety
  - ai-agents
sources:
  - "arXiv:2406.13352"
  - "NeurIPS 2024 Datasets and Benchmarks"
related_concepts:
  - "[[concepts/prompt-injection]]"
  - "[[concepts/ai-agents]]"
  - "[[adversarial-testing]]"
  - "[[agent-security-bench]]"
---

# AgentDojo

AgentDojo is a dynamic evaluation environment for benchmarking prompt injection attacks and defenses in LLM agents. Developed by ETH Zurich and published as a NeurIPS 2024 Datasets and Benchmarks track paper, it provides a comprehensive testbed for assessing agent robustness against adversarial inputs.

## What It Measures

AgentDojo evaluates how susceptible LLM agents are to **prompt injection attacks** and how effective various defense mechanisms are at mitigating them. It specifically tests:

- Agent resilience to direct and indirect prompt injections
- Task completion rates under adversarial conditions
- Defense effectiveness across diverse attack vectors
- Trade-offs between utility and security in defended agents

## Data/Methodology

The benchmark comprises **97 tasks** across multiple application domains, with **629 security test cases** designed to probe different attack surfaces. Key methodological features include:

- **Dynamic environment**: Tasks and attacks are generated dynamically rather than using static templates, reducing overfitting risk
- **Multi-domain coverage**: Tasks span web browsing, file management, coding, and other agent-use scenarios
- **Red-teaming framework**: Systematic attack generation paired with defense evaluation
- **Utility-aware metrics**: Measures both security (attack success rate) and utility (task completion on benign inputs)

## Key Results

- Many popular LLM agents show significant vulnerability to prompt injection attacks
- Simple defenses (e.g., instruction hierarchy, input filtering) provide partial but incomplete protection
- There is a consistent trade-off between agent utility and security robustness
- Current state-of-the-art agents remain vulnerable to sophisticated injection strategies

## Related Benchmarks

- [[agentharm]] — Measures agent harmfulness through malicious task completion
- [[injecagent]] — Focuses specifically on indirect prompt injection in tool-integrated agents
- [[agent-security-bench]] — Formalizes broader attack/defense taxonomy for LLM agents
- [[shade-arena]] — Evaluates sabotage and hidden harmful behaviors in agents

## Connections to Other Wiki Concepts

AgentDojo connects to the broader landscape of **[[concepts/ai-agents]]** evaluation by addressing one of the most critical security concerns: adversarial manipulation of agent behavior. Its focus on **prompt-injection** makes it a key resource for understanding how malicious inputs can override system instructions. The benchmark's dynamic methodology influenced subsequent works on **[[adversarial-testing]]** and contributed to the development of defense frameworks studied in [[agent-security-bench]].
