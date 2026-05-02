---
title: "LLM Security"
type: concept
created: 2026-04-25
updated: 2026-05-01
tags:
  - concept
  - security
  - agent-safety
  - evaluation
  - adversarial
status: L2
sources:
  - "raw/articles/simonwillison.net--2026-apr-30-gpt-55-cyber-capabilities.md"
  - "https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities"
---

# LLM Security

Security implications of frontier language models, including autonomous cyber-offensive capabilities, jailbreak resistance, and the dual-use nature of advanced coding and reasoning abilities.

## AISI Evaluation: GPT-5.5 Cyber Capabilities (April 2026)

The UK AI Security Institute (AISI) evaluated GPT-5.5 using a suite of 95 narrow tasks and complex "cyber ranges." It is one of the strongest models tested to date.

### Key Performance Metrics

| Test | GPT-5.5 | Claude Mythos | GPT-5.4 | Opus 4.7 |
|------|---------|---------------|---------|----------|
| **Expert-level Pass Rate** (CTF) | **71.4%** | 68.6% | 52.4% | 48.6% |
| **TLO (32-step) Solved** | 2/10 | Yes | — | — |
| **Cooling Tower (ICS)** | Failed | — | — | — |

### Capabilities Demonstrated

- Reverse engineering stripped binaries and firmware
- Heap/stack overflow exploitation
- Padding-oracle attacks
- Weaponizing synthetic vulnerabilities in open-source software
- Full corporate network simulation (TLO): reconnaissance → credential theft → lateral movement → CI/CD pivot

### `rust_vm` Challenge: Speed Comparison

A custom VM reverse-engineering task:
- **Human expert time**: ~12 hours
- **GPT-5.5 time**: 10 minutes 22 seconds
- **Cost**: $1.73

Key technical moments:
1. Autonomously diagnosed zeroed jump-table entries in PIE binaries and used `readelf -rW` to extract relocation-based handler addresses
2. Wrote ~100-line Python emulator; self-corrected register swap on interrupt mismatch
3. Recovered password-check logic (chained table lookups) and used SMT-style constraint solving

### Jailbreak Resistance

AISI red-teamers developed a **universal jailbreak in 6 hours** that elicited violative content across all malicious cyber queries, including multi-turn agentic settings. GPT-5.5's safeguards were bypassable in the research environment; subsequent OpenAI safeguard updates were unverified due to a configuration error in the AISI-provided version.

### Implications

| Signal | Meaning |
|--------|---------|
| **Second model to solve TLO** (after Mythos) | Broad industry trend, not single-model breakthrough |
| **Cyber capability as emergent** | Byproduct of general reasoning, coding, and long-horizon autonomy improvements |
| **Cost asymmetry** | $1.73 vs 12 human hours — 400× speedup for specialized tasks |
| **ICS failure** | Physical/OT domain reasoning still limited |

### Defensive Recommendations (AISI)

- Use these same frontier capabilities to harden systems via "Trusted Access Programmes"
- 43% of UK businesses suffered a breach in the past 12 months
- UK responded with £90m funding boost and the Cyber Security and Resilience Bill

## Evaluation Methodology

AISI uses a **ReAct agent scaffold** with Bash and Python tools inside a **Kali Linux container**. Performance on complex tasks (TLO) continues to scale with inference compute (token budget) without visible plateau — suggesting further capability improvements are possible with more compute.

## Related Concepts

- [[concepts/ai-safety]] — Broader safety landscape
- [[concepts/red-teaming]] — Adversarial evaluation
- [[concepts/jailbreaking]] — Prompt-based safety bypasses
- [[concepts/cybersecurity]] — Traditional security context
- [[concepts/llm-evaluation]] — Evaluation methodology

## Related Entities

- [[entities/aisi]] — UK AI Safety Institute
- [[openai]] — GPT-5.5 developer
- [[anthropic]] — Claude Mythos comparison point
