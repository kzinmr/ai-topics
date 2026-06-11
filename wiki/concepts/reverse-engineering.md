---
title: "Reverse Engineering"
type: concept
aliases:
  - reverse-engineering
  - RE
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - reverse-engineering
  - security
  - methodology
status: complete
sources:
  - url: "https://github.com/pydantic/monty"
    title: "Monty Sandbox Security Model"
  - url: "https://pydantic.dev/articles/hack-monty"
    title: "Hack Monty Bounty Program"
---

# Reverse Engineering

**Reverse Engineering** is the process of analyzing existing systems or software to understand their structure, behavior, and design. In the AI context, it has broad applications including analyzing model internals, bypassing sandboxes, and inferring training data.

## Reverse Engineering in AI

### Model Analysis
- **Model extraction attacks**: Inferring model knowledge or weights through public APIs
- **Architecture estimation**: Inferring model structure from latency and response patterns
- **Prompt extraction**: Leaking system prompts through attacks
- **Membership inference**: Determining whether specific data was used in training

### Sandbox Evasion
- Security testing of AI agent code execution sandboxes (e.g., [[concepts/monty-sandbox]])
- **Hack Monty**: Pydantic ran a $5,000 bounty program
- Attempting container escape, filesystem access, and environment variable leaks

### Protocol Analysis
- Reverse engineering proprietary APIs
- Statistical analysis of model response patterns
- Inferring rate limits and load balancing

## Key Techniques

| Technique | Description | AI Application |
|-----------|------|----------------|
| **Static Analysis** | Static structural analysis of binaries/code | Analyzing model file formats |
| **Dynamic Analysis** | Observing runtime behavior | Analyzing API response patterns |
| **Fault Injection** | Intentionally triggering errors to observe behavior | Identifying sandbox boundaries |
| **Side-Channel Attacks** | Analyzing timing, power consumption, EM emissions | Estimating model size and structure |
| **Gray-Box Analysis** | Combining partial known information with observation | Discovering prompt injection vulnerabilities |

## Relationship with AI Security

Reverse engineering has two sides in AI security:
- **Offensive**: Finding model weaknesses, jailbreaks, prompt injection
- **Defensive**: Discovering and fixing vulnerabilities, red teaming, bug bounty programs

## Ethical Considerations

- **Terms of Service compliance**: Many AI services prohibit reverse engineering
- **Responsible disclosure**: Report discovered vulnerabilities appropriately
- **Educational context**: Use for security research and learning purposes

## Related Concepts

- [[concepts/monty-sandbox]] — Sandbox security model
- [[concepts/claude-code/claude-code-best-practices]] — Secure code execution
- [[concepts/agent-loop-orchestration]] — Agent security

## Sources

- [Monty Sandbox (Pydantic)](https://github.com/pydantic/monty)
- [Hack Monty Bounty Program](https://pydantic.dev/articles/hack-monty)
