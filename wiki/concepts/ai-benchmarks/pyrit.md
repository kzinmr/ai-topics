---
title: PyRIT (Python Risk Identification Tool)
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - evaluation
  - safety
  - agent-safety
sources:
  - https://github.com/Azure/PyRIT
related_concepts:
  - safety
  - red-teaming
  - prompt-injection
---

# PyRIT (Python Risk Identification Tool)

PyRIT is a Python-based tool developed by Microsoft's AI Red Team for identifying security risks in generative AI systems. Unlike benchmarks that score model performance, PyRIT is an active testing tool that probes AI systems for vulnerabilities through multi-turn adversarial attacks, providing 70+ converters for diverse attack strategies.

## What It Measures

PyRIT is a tool (not a benchmark) designed to identify and assess:

- **Security vulnerabilities**: Weaknesses in generative AI systems that could be exploited by malicious actors
- **Jailbreak susceptibility**: How easily models can be manipulated to bypass safety guardrails
- **Prompt injection resilience**: Resistance to [[prompt-injection]] attacks that manipulate model behavior
- **Multi-turn attack surfaces**: Vulnerabilities that only emerge through extended adversarial conversations
- **Content policy violations**: Cases where models generate harmful, biased, or policy-violating content under adversarial conditions
- **System prompt leakage**: Whether internal instructions or system prompts can be extracted

## Data/Methodology

PyRIT provides a comprehensive red-teaming toolkit:

- **70+ converters**: A library of attack transformation strategies that can be combined and chained
- **Multi-turn attacks**: Support for sophisticated adversarial conversations that build up to exploitation over multiple exchanges
- **Automated red-teaming**: Programmatic generation and execution of adversarial prompts
- **Extensible architecture**: Plugin system for adding custom attack strategies and target models
- **Orchestrator pattern**: High-level orchestration of complex attack flows across multiple targets
- **Microsoft AI Red Team**: Developed and maintained by Microsoft's dedicated AI security team with real-world red-teaming experience

## Key Results

- PyRIT has been used internally by Microsoft's AI Red Team to test Azure AI services and other Microsoft AI products
- The tool has identified numerous vulnerabilities across different generative AI systems
- Multi-turn attack strategies prove significantly more effective than single-turn attempts
- The 70+ converter library covers a wide range of attack vectors including [[prompt-injection]], jailbreaking, and content manipulation
- PyRIT has been open-sourced to enable the broader security community to conduct systematic red-teaming of AI systems

## Related Tools and Concepts

- [[prompt-injection]] — One of the primary attack categories that PyRIT tests for
- AI safety and alignment research
- Red-teaming methodologies for generative AI
- Other AI safety evaluation tools and frameworks

## Connections to Other Wiki Concepts

PyRIT represents the security-focused side of AI [[evaluation]], complementing performance-focused benchmarks. While benchmarks like those aggregated in [[hal-leaderboard]] measure what agents *can* do, PyRIT measures what they *shouldn't* be able to do. Its focus on [[prompt-injection]] and multi-turn adversarial attacks connects to broader safety concerns in [[ai-agents]] deployment. PyRIT's approach of active probing rather than passive scoring represents a different philosophy from traditional benchmarks — it's a tool for finding failures rather than measuring successes.
