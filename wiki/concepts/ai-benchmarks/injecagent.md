---
title: "InjecAgent"
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
  - "arXiv:2403.02691"
  - "ACL 2024"
related_concepts:
  - "[[prompt-injection]]"
  - "[[ai-agents]]"
  - "[[tool-use]]"
  - "[[agent-dojo]]"
---

# InjecAgent

InjecAgent is a benchmark for evaluating **indirect prompt injection (IPI)** vulnerabilities in tool-integrated LLM agents. Developed at UIUC and published at ACL 2024, it provides a systematic framework for testing how attackers can manipulate agent behavior through external tool outputs.

## What It Measures

InjecAgent specifically targets **indirect prompt injection** attacks where malicious instructions are embedded in data retrieved by tools rather than in the user's direct input. It evaluates:

- Agent susceptibility to IPI attacks via tool outputs
- Attack success rates across different tool types and attack strategies
- Defense effectiveness against indirect injections
- Impact of tool diversity on attack surface

## Data/Methodology

The benchmark comprises **1,054 IPI test cases** with extensive tool coverage:

- **17 user tools** and **62 attacker tools** providing diverse attack surfaces
- Attack scenarios where malicious instructions are embedded in web pages, documents, databases, and other external data sources
- **Multi-turn evaluation**: Tests attacks in realistic multi-step agent workflows
- **Success metrics**: Measures whether agents follow injected instructions vs. original user intent
- **Defense benchmarks**: Evaluates instruction hierarchy, input sanitization, and other mitigation strategies

## Key Results

- Tool-integrated agents are highly vulnerable to indirect prompt injection
- Attack success rates remain significant even with basic defenses applied
- The diversity of tool types creates a broad and difficult-to-secure attack surface
- Current LLMs struggle to distinguish between legitimate instructions and injected content in tool outputs

## Related Benchmarks

- [[agentdojo]] — Dynamic environment for prompt injection attack/defense evaluation
- [[agent-security-bench]] — Broader formalization of agent attack and defense strategies
- [[agentharm]] — Measures harmful agent task completion
- [[shade-arena]] — Evaluates hidden harmful behaviors and sabotage in agents

## Connections to Other Wiki Concepts

InjecAgent is a cornerstone benchmark for understanding **prompt-injection** in the context of **[[ai-agents]]** that use external tools. Unlike direct prompt injection, indirect injection through **tool-use** outputs represents a fundamentally harder security challenge because agents must process and act on external data. The benchmark has shaped research directions in agent security and influenced the development of more comprehensive evaluations like [[agent-security-bench]] and [[agentdojo]].
