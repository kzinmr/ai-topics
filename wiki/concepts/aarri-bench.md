---
title: "AARRI-Bench (Act As a Real Research Intern)"
type: concept
created: 2026-06-16
updated: 2026-06-16
tags:
  - benchmark
  - evaluation
  - lab
  - training
sources:
  - https://arxiv.org/abs/2606.07462
  - raw/newsletters/2026-06-15-import-ai-461-alignment-is-not-on-track-frontiercode-and-synthetic-research-inte.md
related:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/frontiercode
  - concepts/synthetic-data
  - concepts/ai-evals
  - concepts/recursive-self-improvement
---

# AARRI-Bench (Act As a Real Research Intern)

**AARRI-Bench** is a benchmark suite for evaluating frontier LLMs and agentic harnesses in the **research lifecycle** — not just coding, but the full spectrum of activities a human research intern performs. Introduced in arXiv:2606.07462 (Wang et al., June 2026).

## Core Thesis

As foundation models advance and agent scaffolding becomes increasingly sophisticated, agents have demonstrated remarkable proficiency in complex, long-horizon coding tasks and even autonomous experiment execution. Despite their evolution from research assistants into autonomous research agents, these systems still exhibit significant limitations in **field sensitivity**, **research ethics**, and **nuanced scientific judgment**. Consequently, frontier agents remain unable to fully replace human researchers.

AARRI-Bench is designed to measure this gap: not "can the model code?" but "can the model act as a competent research intern?"

## Benchmark Structure

### 82 Manually Crafted Tasks

Unlike scraped benchmarks, AARRI-Bench tasks are hand-curated to test real research competencies.

### Four Evaluation Categories

| Category | What It Tests | Examples |
|----------|--------------|----------|
| **Context** | Field awareness, literature familiarity | Knowing what's been done, understanding research landscape |
| **Mindset** | Self-awareness, autonomy, research judgment | Knowing when you don't know, prioritizing experiments |
| **Hands-on** | Technical proficiency | Implementing experiments, running evaluations |
| **Interaction** | Tool use + human collaboration | Communicating results, integrating feedback |

### Three Difficulty Tiers

| Tier | Name | Description |
|------|------|-------------|
| **S1** | Adaptation | Modifying existing approaches to new contexts |
| **S2** | Integration | Combining multiple techniques for a research goal |
| **S3** | Innovation | Proposing novel approaches to open problems |

## Key Findings

### Synthetic Research Interns

The benchmark reveals that current frontier models, even when wrapped in agentic harnesses, perform well on technical execution (S1) but struggle significantly on research judgment and field awareness (S3).

### Ethical Reasoning Tasks

AARRI-Bench includes specific tasks for:
- **Fabricated data identification**: Detecting when research data has been artificially generated or manipulated
- **Paper injection attack detection**: Identifying when adversarial papers have been inserted into the literature to bias model outputs
- **Research ethics scenarios**: Evaluating whether the agent makes ethically sound decisions in ambiguous research situations

### Performance Results

| System | Score | Notes |
|--------|-------|-------|
| **Claude Opus 4.7 + Mini-SWE-Agent** | 68.3% | Best agentic combination |
| Claude Opus 4.7 (standalone) | — | Lower without agent scaffolding |
| Mini-SWE-Agent (standalone) | — | Lower without frontier model |

The 68.3% ceiling on the best system indicates significant room for improvement — a human research intern would be expected to perform substantially higher on many of these tasks, particularly those requiring field awareness and ethical judgment.

## Significance

AARRI-Bench is important because it:

1. **Shifts the evaluation axis** from "can the model produce code/reports?" to "can the model perform the cognitive work of a research intern?"
2. **Captures the judgment gap** — the difference between technical competence and research maturity
3. **Provides ethical benchmarks** — specifically testing for vulnerability to data fabrication and literature poisoning attacks
4. **Complements coding benchmarks** — alongside FrontierCode (which tests mergeability), AARRI-Bench tests research lifecycle competency

## Related Benchmarks

- [[concepts/ai-benchmarks/frontiercode]] — Tests code mergeability, not just correctness
- [[concepts/ai-benchmarks/swe-bench]] — Tests issue resolution via test passing
- [[concepts/ai-benchmarks/agent-arena]] — Causal evaluation of agent performance
- [[concepts/synthetic-data]] — Synthetic data generation and evaluation

## Sources

- [arXiv:2606.07462 — Act As a Real Researcher](https://arxiv.org/abs/2606.07462) (Wang et al., June 2026)
- [Import AI 461](https://importai.substack.com/p/import-ai-461-alignment-is-not-on) (Jack Clark, June 15, 2026)
