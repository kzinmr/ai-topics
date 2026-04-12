---
title: "AI Evals (評価)"
created: 2026-04-12
updated: 2026-04-12
type: concept
tags: [ai-evals, evaluation, quality-assurance, methodology]
aliases: ["AI Evaluations", "Evaluation Framework"]
sources:
  - raw/articles/lenny-podcast-why-ai-evals-are-the-hottest-new-skill-2025-09.md
---

# AI Evals (評価)

Systematic framework for evaluating AI/ML systems, particularly AI agents. Moves beyond subjective "vibes-based" assessment to measurable, reproducible quality checks.

## Core Methodology

AI evals follow a structured approach:

1. **Define the task** — What should the AI do?
2. **Collect real user traces** — How are actual users interacting with the system?
3. **Open coding** — Manually review 5-10 traces, categorize successes/failures
4. **Build taxonomy** — Create structured categories of failure modes
5. **Theoretical saturation** — Continue until no new categories emerge
6. **Automate** — Convert categories to measurable tests

## Types of Evals

### Code-based Evals
- **Strengths:** Deterministic, fast, cheap
- **Limitations:** Cannot evaluate open-ended outputs
- **Use case:** Structured tasks with clear pass/fail criteria

### LLM-as-Judge Evals
- **Strengths:** Can evaluate subjective, open-ended outputs
- **Limitations:** Slower, more expensive, less consistent
- **Use case:** Complex evaluations requiring nuanced judgment
- **Best practices:** Use multiple models, structured prompts, consistency checks

## Quality Metrics

- **Reproducibility** — Can the same test be run multiple times with same results?
- **Coverage** — Does the eval test all major failure modes?
- **Cost** — What is the computational cost of running the eval?
- **Speed** — How quickly can results be obtained?

## Implementation Patterns

1. **Benevolent dictator** — Single domain expert maintains taxonomy consistency
2. **Continuous improvement** — Update evals based on new failure modes
3. **User-centric** — Focus on actual user experience, not synthetic tests
4. **Incremental automation** — Start manual, automate progressively

## Related Concepts

- [[ai-agent-traps]] — AI agents commonly fail in predictable ways
- [[lm-evaluation-harness]] — Academic benchmarking framework
- [[functional-emotions-llms]] — Related to systematic evaluation approaches

## Sources

- Lenny's Podcast: "Why AI evals are the hottest new skill for product builders" with Shreya Shankar and Hamel Husain (Sept 25, 2025)
- [[raw/articles/lenny-podcast-why-ai-evals-are-the-hottest-new-skill-2025-09]]
