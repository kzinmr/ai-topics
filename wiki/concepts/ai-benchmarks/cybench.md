---
title: "Cybench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - safety
  - cybersecurity
  - ai-agents
sources:
  - "arXiv:2408.08926"
related_concepts:
  - "[[cybersecurity]]"
  - "[[ai-agents]]"
  - "[[safety-evaluation]]"
  - "[[coding-agents]]"
---

# Cybench

Cybench is a framework for evaluating the **cybersecurity capabilities and risks** of language models. It provides structured challenges that test whether LLMs can identify, exploit, and defend against security vulnerabilities in realistic scenarios.

## What It Measures

Cybench evaluates LLM capabilities in cybersecurity contexts:

- **Vulnerability identification**: Ability to discover security flaws in code and systems
- **Exploit generation**: Capability to create working exploits for identified vulnerabilities
- **Defense strategies**: Proficiency at recommending and implementing security mitigations
- **Risk assessment**: Understanding of threat landscapes and attack surfaces
- **CTF-style challenges**: Problem-solving in capture-the-flag cybersecurity scenarios

## Data/Methodology

The benchmark framework includes:

- **Curated cybersecurity challenges**: Covering web security, binary exploitation, cryptography, forensics, and reverse engineering
- **Graduated difficulty levels**: From basic vulnerability identification to advanced exploit chains
- **Automated evaluation**: Verifiable flag-based scoring for objective assessment
- **Risk-focused analysis**: Evaluation of dual-use potential of LLM cybersecurity capabilities
- **Real-world grounding**: Challenges derived from realistic security scenarios

## Key Results

- Frontier LLMs show rapidly improving cybersecurity capabilities
- Models can solve many medium-difficulty CTF challenges autonomously
- Cybersecurity capabilities represent a significant dual-use concern
- Current models still struggle with multi-step, creative exploit chains

## Related Benchmarks

- [[decodingtrust]] — Broader trustworthiness evaluation including security dimensions
- [[agentdojo]] — Agent security through prompt injection evaluation
- [[agent-security-bench]] — Comprehensive agent attack/defense evaluation
- [[agentharm]] — Harmful capability assessment including cyber threats

## Connections to Other Wiki Concepts

Cybench sits at the intersection of **cybersecurity** and AI evaluation, addressing growing concerns about LLM-enabled cyber capabilities. It connects to the **[[coding-agents]]** domain by testing whether code-generating models can both create and exploit security vulnerabilities. The benchmark's dual-use focus relates to broader **safety-evaluation** concerns addressed by [[decodingtrust]] and [[agentharm]], while its practical challenge format informs how **[[ai-agents]]** might be deployed (or misused) in security contexts.
