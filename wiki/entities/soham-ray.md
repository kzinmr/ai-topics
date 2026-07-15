---
title: "Soham Ray"
created: 2026-07-15
updated: 2026-07-15
type: entity
tags:
  - person
  - ai-researcher
  - evaluation
  - agent-evaluation
aliases:
  - "@sohmray"
  - sohmray
sources:
  - raw/articles/2026-07-14_sohmray_icml-2026-research-trends.md
  - https://x.com/sohmray
related:
  - entities/sierra
  - entities/shreya-shankar
  - concepts/ai-benchmarks/tau-bench
  - concepts/ai-benchmarks/tau-squared-bench
  - concepts/ai-benchmarks/tau-knowledge
  - concepts/ai-benchmarks/tau-voice
---

# Soham Ray

**Soham Ray** (@sohmray) is a researcher at **[[entities/sierra|Sierra]]** working on AI agent evaluation. He co-authored and presented the tau-bench family of benchmarks (tau-bench, tau2-bench, tau-Knowledge, tau-Voice) at ICML 2026, where tau2-bench received an **oral presentation** — one of 168 orals in the top 0.7% of ~24,000 submissions.

## Overview

Soham Ray joined Sierra as a researcher focusing on **agent evaluation and benchmarking**. His work on the tau-bench suite represents one of the most significant contributions to practical agent evaluation frameworks, spanning conversation, knowledge work, voice interaction, and multi-step tool use.

At ICML 2026 in Seoul, he presented three tau-bench papers alongside coauthors **Ola Zytek**, **Ben Shi**, **Pedram Razavi**, and **Victor Barres**. The tau2-bench paper received an oral presentation, placing it among the most impactful submissions at the conference.

## Key Contributions

### tau-bench Suite (2025–2026)

The tau-bench family of benchmarks evaluates AI agents on realistic, multi-step tasks:

- **tau-bench** — Core conversational agent benchmark for customer service scenarios
- **tau2-bench** — Extended multi-step agent evaluation; ICML 2026 **oral** (top 0.7%)
- **tau-Knowledge** — Knowledge-grounded agent evaluation with ~195K token knowledge base across 698 documents
- **tau-Voice** — Voice interaction agent evaluation

The benchmarks have been adopted by researchers worldwide and were cited in ICML 2026 invited talks and papers.

### ICML 2026 Research Trends Article (July 2026)

Ray published a widely-read analysis of ICML 2026 research trends on X Articles, identifying several key themes:

1. **Automated research is accelerating** — AI research scientists, Google's End-to-End AI Scientist and MARS auto-research agent, though the field is still early
2. **"Everything is a factory"** — Cheaper code is driving more elaborate data generation and LLM-judge pipelines
3. **Research taste is the open question** — LLMs possess vast world knowledge but struggle with the experiential judgment that guides research direction (InnoEval is an early quantification attempt)
4. **Weight shifting to evaluation** — Arvind Narayanan's talk framed evaluation as the bottleneck; figuring out *what* to evaluate is the hardest part
5. **Benchmark saturation crisis** — ~50% of 60 benchmarks show saturation; "Benchmarking at the Edge of Comprehension" tackles post-human evaluation; contamination-resistant design
6. **LLM judges maturing** — REAL calibrates judges as reward scorers; Rubric Curriculum RL evolves rubrics during training
7. **Synthetic data quality continuously improving** — "Less is Enough" matches 300K samples with 2K targeted synthetic; Simula pitches agentic generation
8. **Memory is what personalizes agents** — Learning to Share, MemEvolve, Persona2Web, MCP-Persona; memory also becomes an attack surface

## Professional Background

- **2025–present**: Researcher, Sierra (agent evaluation, tau-bench)
- **X/Twitter**: [@sohmray](https://x.com/sohmray) — joined September 2016

## Cross-References

- [[entities/sierra]] — Employer; the tau-bench benchmarks are Sierra's primary research contribution
- [[entities/shreya-shankar]] — Collaborator on tau-bench; co-author of tau-bench papers
- [[concepts/ai-benchmarks/tau-bench]] — Core conversational agent benchmark
- [[concepts/ai-benchmarks/tau-squared-bench]] — Extended multi-step evaluation (ICML 2026 oral)
- [[concepts/ai-benchmarks/tau-knowledge]] — Knowledge-grounded evaluation
- [[concepts/ai-benchmarks/tau-voice]] — Voice interaction evaluation

## Sources

- [X Article: "Research Trends at ICML 2026"](https://x.com/i/article/2077127538808356864) — July 14, 2026
- [X/Twitter Profile](https://x.com/sohmray)
- [ICML 2026 — tau2-bench Oral](https://icml.cc/virtual/2026/oral/71031)
