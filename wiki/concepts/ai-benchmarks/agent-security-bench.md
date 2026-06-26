---
title: "Agent Security Bench (ASB)"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - safety
  - agent-security
  - ai-agents
sources:
  - "ICLR 2025"
related_concepts:
  - "[[agent-security]]"
  - "[[ai-agents]]"
  - "[[prompt-injection]]"
  - "[[adversarial-testing]]"
---

# Agent Security Bench (ASB)

Agent Security Bench (ASB) is a comprehensive benchmark published at ICLR 2025 that formalizes the evaluation of **attacks and defenses** in LLM-based agents. It provides a systematic framework covering multiple attack vectors and defense mechanisms across diverse agent scenarios.

## What It Measures

ASB evaluates the security posture of LLM agents across a formalized taxonomy of attack types:

- **Direct Prompt Injection (DPI)**: Attacks through user-facing inputs
- **Indirect Prompt Injection (IPI)**: Attacks through external data and tool outputs
- **Plan-of-thought backdoors**: Subtle manipulation of agent reasoning chains
- Defense effectiveness against each attack category
- Cross-scenario generalization of attack and defense strategies

## Data/Methodology

The benchmark spans **10 scenarios** with over **400 tools**, providing extensive coverage:

- **Formalized attack taxonomy**: DPI, IPI, and plan-of-thought backdoor categories
- **10 diverse agent scenarios**: Covering real-world agent use cases
- **400+ tools**: Extensive tool integration for realistic evaluation
- **Standardized metrics**: Comparable evaluation across models and defense strategies
- **Defense benchmarking**: Systematic testing of instruction hierarchy, filtering, and monitoring approaches

## Key Results

- No single defense mechanism is effective across all attack categories
- Plan-of-thought backdoors represent a particularly challenging attack vector
- Defense effectiveness varies significantly across agent scenarios
- Current agents show inconsistent security properties across different tool environments

## Related Benchmarks

- [[agentdojo]] — Dynamic prompt injection attack/defense evaluation
- [[injecagent]] — Focused IPI benchmarking for tool-integrated agents
- [[agentharm]] — Harmful task completion measurement
- [[shade-arena]] — Sabotage and monitoring evaluation

## Connections to Other Wiki Concepts

ASB provides the most formalized framework for **agent-security** evaluation among current benchmarks. Its taxonomy of DPI, IPI, and plan-of-thought backdoors structures the threat landscape for **[[ai-agents]]** research. The benchmark builds on insights from [[agentdojo]] (prompt injection), [[injecagent]] (indirect injection), and [[shade-arena]] (sabotage) to create a unified evaluation framework. Its formalization of **adversarial-testing** methodologies has become a reference point for subsequent agent security research.
