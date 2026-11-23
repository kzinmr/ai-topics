---
title: "Reverse Engineering"
type: concept
aliases:
  - reverse-engineering
  - RE
created: 2026-04-25
updated: 2026-11-23
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
  - raw/articles/2026-11-18_slowchronicle.com_llm-assisted-reverse-engineering.md
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

## Recent Developments

- **Nov 2026 — LLM-assisted reverse engineering practitioner workflow**: ioma8 (20-year hardware/software hacker, Slow Chronicle) documented a production RE workflow where AI compresses "years each" of manual work. Stack: [[entities/deepseek]] DeepSeek v4.1 Flash via a DeepSeek harness (occasional Codex w/ Luna/Terra), Ghidra + MCP bridge, radare2/kuna. Key techniques: point the agent at the binary with dedicated agent skills; force continuous Markdown documentation of findings (survives compaction/handoff); agent-driven debugging with breakpoints, log probes/injection, computer-use or API-controllable emulators for external access; deliberate re-approach prompting (e.g., "follow strings instead of xrefs"); reading the full trace to spot narrow paths. Two reusable skills stand out: a **Ghidra-decompile skill** (22 scripts + GhidraMCP version-mismatch fix) and **hypothesis-debugging** — a scientific-method loop (hypothesis → definitive experiment → recorded result in a CSV) that stops agents circling in guess-mode. Rust for implementations because the strict compiler gives agents a brutal feedback loop. Raw: raw/articles/2026-11-18_slowchronicle.com_llm-assisted-reverse-engineering.md (HN 223 pts).
- **Oct 2026 — Anthropic blocks video-game reverse engineering**: Users reported Claude refusing video-game recreation/cloning and generic reverse-engineering tasks (Mashable, GameDeveloper, Tom's Hardware; HN 149/124 pts), part of a broader usage-policy enforcement wave that also blocked training-internals topics. The lab-encoding-of-publisher-friendly-restrictions question and its false-positive pattern are analyzed in [[concepts/frontier-model-usage-policy-enforcement-2026-10]].

## Related Concepts

- [[concepts/monty-sandbox]] — Sandbox security model
- [[concepts/claude-code/claude-code-best-practices]] — Secure code execution
- [[concepts/agent-loop-orchestration]] — Agent security
- [[concepts/agent-skills]] — Skill packs (e.g., ghidra-decompile, hypothesis-debugging) as the leverage point in agentic RE
- [[concepts/mcp]] — Ghidra MCP bridge tooling for agents

## Sources

- [Monty Sandbox (Pydantic)](https://github.com/pydantic/monty)
- [Hack Monty Bounty Program](https://pydantic.dev/articles/hack-monty)
- [LLM assisted reverse engineering (Slow Chronicle, Nov 18 2026)](https://www.slowchronicle.com/posts/llm-assisted-reverse-engineering)
