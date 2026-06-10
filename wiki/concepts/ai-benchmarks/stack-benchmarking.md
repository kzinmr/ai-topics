---
title: "Stack Benchmarking (Ramp)"
created: 2026-06-04
updated: 2026-06-04
type: concept
tags:
  - benchmark
  - evaluation
  - ai-agents
  - memory-systems
  - fintech
  - model
sources:
  - raw/articles/2026-06-04_ramp_stack-benchmarking.md
  - https://builders.ramp.com/post/stack-benchmarking
---

# Stack Benchmarking

Ramp's methodology for building a **domain-specific agent benchmark** to guide the development of **Ramp Stack**, their agentic accounting assistant. Published June 2026 on the Ramp Builders engineering blog by Ryan Stevens.

## Overview

Ramp developed a custom accounting benchmark to evaluate frontier AI models on real-world accounting tasks. The benchmark was used to drive decisions about model selection, agent architecture, and skill composition for Ramp Stack — an AI agent designed to automate accounting workflows.

## Key Research Areas

### Domain-Specific Benchmarking
Unlike general-purpose benchmarks (MMLU, HumanEval, SWE-bench), Ramp built a benchmark specifically for **accounting domain tasks**. This represents a growing trend of companies building proprietary, domain-specific evaluation suites rather than relying solely on public benchmarks.

Key considerations:
- **Task authenticity** — Tasks reflect actual accounting workflows, not synthetic problems
- **Domain coverage** — Benchmarks span multiple accounting sub-domains
- **Graded difficulty** — Tasks range from simple classification to complex multi-step workflows

### Frontier Model Evaluation
The benchmark was used to evaluate frontier AI models (likely including GPT-4 class and above) on accounting-specific tasks. This is part of a broader industry pattern of evaluating frontier models on domain-specific tasks beyond general reasoning benchmarks.

### Skill Ablation
A central finding involved **skill ablation studies** — systematically removing or disabling specific agent capabilities to measure their contribution to overall performance. This helps identify:
- **Critical skills** — Capabilities without which performance collapses
- **Optional skills** — Capabilities that help but aren't essential
- **Negative skills** — Capabilities that may actually degrade performance in certain contexts

### Memory Architecture
The benchmark explored how different **memory architectures** affect agent performance on accounting tasks:
- Short-term vs. long-term memory
- Structured vs. unstructured memory
- Shared memory across agent components
- Memory retrieval strategies

## Industry Significance

Ramp's approach exemplifies a growing pattern in enterprise AI deployment:

1. **Build, don't just evaluate** — Benchmarks are built as development tools, not just evaluation tools
2. **Domain depth over breadth** — Deep domain-specific benchmarks > broad general benchmarks for production use
3. **Skill ablation as methodology** — Systematic capability testing reveals what matters vs. what's hype
4. **Memory matters** — Agent memory architecture is a first-class concern, not an afterthought

## Related Concepts

- [[concepts/agent-evaluation]] — General agent evaluation methodologies
- [[concepts/eval-loops]] — Evaluation loop patterns for agents
- [[concepts/benchmark-framing]] — How benchmarks shape AI development
- [[concepts/memory-systems]] — Agent memory architecture
- [[concepts/outcome-based-pricing]] — Ramp-related pricing model for AI agents
- [[entities/ramp]] — Ramp entity page

## Open Questions

- What specific models were evaluated and with what quantitative results?
- How does accounting domain benchmarking differ from other domains (legal, medical, coding)?
- What skill ablation results were found — which capabilities matter most?
- How does Ramp Stack's architecture compare to other agentic accounting approaches?
