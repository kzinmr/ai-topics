---
title: Agent Survival Benchmark
type: concept
created: 2026-04-16
updated: 2026-05-26
tags:
  - concept
  - evaluation
  - ai-agents
  - benchmark
related:
- evals-for-ai-agents
- multi-agent-autonomy-scale
- ai-agent-traps
sources: []
---

# Agent Survival Benchmark

An open-source benchmark for measuring LLM agent survival capability and performance under PvP (player-vs-player) pressure.

## Core Discovery

Published in April 2026, this benchmark provided a key insight: agent **aggressiveness does not predict victory**.

### Key Findings
- **Aggression ≠ Victory**: Highly aggressive agents do not necessarily win
- Survival/victory depends on other traits (adaptability, resource management, strategic patience)
- Suggests the limits of the conventional "faster, stronger" approach

## Benchmark Design

### PvP Pressure Testing
- Multiple agents interact in a competitive environment
- Measures survival rate, resource acquisition, and strategic success
- Evaluates a dimension distinct from traditional benchmarks (MMLU, HumanEval, etc.)

### Survival Metrics
- Agent survival duration
- Resource efficiency
- Strategic adaptability
- Interaction patterns with other agents

## Implications for Agent Development

### Beyond Raw Capability
- High capability does not equal real-world success
- Strategic intelligence, adaptability, and coordination ability are critical
- Survival benchmarks are essential for Dark Factory-level automation

### Agent Architecture Design
- Shifting from single-agent optimization to multi-agent coordination
- Testing in survival/competitive environments provides a better indicator of real-world performance
- A new form of red-teaming and adversarial testing

## Relation to Existing Frameworks

- **OSWorld**: Structured task success rate (~66%)
- **ARC-AGI**: Novel problem-solving ability (LLMs <1%)
- **Agent Survival**: Sustained operation and adaptation in competitive environments

This benchmark has the potential to shift the agent evaluation paradigm from capability measurement to survival and adaptation measurement.

## Sources

- [r/AI_Agents: I built an open-source benchmark for LLM agents under survival/PvP pressure](https://www.reddit.com/r/AI_Agents/comments/1sn1ahc/)
- OSWorld benchmark results
- ARC-AGI-3 results

## See Also

- [[concepts/_index]]
- [[concepts/vajra-background-agent]]
- [[concepts/ai-agent-memory-middleware]]
- [[concepts/single-agent-ceiling]]
- [[concepts/ai-agent-memory-two-camps]]
