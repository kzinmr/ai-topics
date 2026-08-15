---
title: Agent Skill Supply-Chain Attacks
created: 2026-08-15
updated: 2026-08-15
type: concept
tags:
  - agent-security
  - agent-safety
  - security
  - vulnerability
  - supply-chain
  - prompt-injection
  - agent-skills
  - adversarial
  - benchmark
  - coding-agents
  - red-teaming
  - ai-agents
sources:
  - raw/papers/2026-08-05_2608.05223_malicious-skill-files-coding-agents.md
  - https://arxiv.org/abs/2608.05223
---

# Agent Skill Supply-Chain Attacks

A security vulnerability class in coding agents: malicious instructions and shell commands hidden inside the **agent skills interface** — the folders of instructions and scripts that agents load dynamically to specialize behavior. Documented systematically by Yang et al. (arXiv 2608.05223, August 2026).

## The attack

The skills interface widens the attack surface: a malicious skill file (a natural-language instruction or script) can smuggle a hidden shell command. Because agents load skills dynamically and act with delegated authority over connected systems, a single malicious skill can compromise the agent.

## Key findings (Yang et al. 2026)

- Synthesized **2,826 malicious skills** from 471 real-world shell commands using six LLMs across four families, mapped to **11 MITRE ATT&CK tactics** (released as a benchmark).
- Evaluation pipeline: run stratification, evidence anchoring, refusal veto, and deterministic declared-intent override, judged by a three-judge LLM-as-a-judge panel validated against a human gold standard (Cohen's kappa = 0.85).
- Across **5,629 completed runs** of two enterprise-grade agents: **Gemini CLI exploited in 95.5–96.1% of runs; Qwen Code in 71.6–74.0%** — nearly invariant to the generating model.
- **Explicit safety recognition occurred in only 1.99% of runs** — agents rarely flag the hidden instruction.

## Implication

Enterprises must assess and mitigate skill-interface risk before adopting coding agents. The paper positions this as a supply-chain problem analogous to [[concepts/ai-supply-chain-security|AI supply-chain security]] but operating at the *skill* layer rather than the dependency layer.

## Related

- [[concepts/agent-skills|Agent Skills]]
- [[concepts/ai-supply-chain-security|AI Supply Chain Security]]
- [[concepts/security-and-governance/agent-security-landscape-2026|Agent Security Landscape (2026)]]
- [[concepts/agent-security-patterns|Agent Security Patterns]]
- [[concepts/ai-agent-security|AI Agent Security]]
