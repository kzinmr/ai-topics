---
title: ARC-AGI-2 Benchmark
type: concept
created: 2026-04-24
updated: 2026-04-24
tags: [concept, benchmark, agi-research, abstraction]
aliases: [arc-agii-2, arc-prize-2]
sources: []
---

# ARC-AGI-2 Benchmark

**ARC-AGI-2** (Abstraction and Reasoning Corpus, 2nd iteration) is an AI benchmark developed by the ARC Prize Foundation that tests systems' ability to infer abstract transformation rules from grid-based demonstrations and apply them to novel inputs.

## Overview

ARC-AGI-2 presents systems with input-output grid demonstrations and asks them to infer the underlying transformation rule and apply it to new examples. Unlike conventional ML benchmarks that test pattern recognition on training data, ARC-AGI-2 tests genuine abstract reasoning and few-shot generalization.

## Architecture

- **Grid-based input-output pairs**: Systems receive demonstrations showing how to transform input grids to output grids
- **Rule inference**: Systems must identify the abstract transformation rule
- **Generalization**: The rule must apply to entirely novel input grids not seen during training

## Performance in Frontier Models

Gemini 3 Deep Think achieved **45.1%** on ARC-AGI-2 with code execution enabled. This places it among the leading models on this benchmark, which has historically been difficult for even the most capable models.

| Model | Score | Notes |
|-------|-------|-------|
| Gemini 3 Deep Think | 45.1% | With code execution |
| [Previous models] | Lower | Without code execution or different approaches |

## Significance
1. **Abstract pattern recognition**: Beyond surface-level visual patterns
2. **Rule generalization**: Applying learned rules to novel contexts
3. **Few-shot learning**: Learning from very limited examples
4. **Compositionality**: Combining simple operations into complex transformations

## Relation to AGI Research

ARC-AGI-2 was designed as a proxy for measuring progress toward artificial general intelligence. Success on this benchmark requires reasoning capabilities that go beyond statistical pattern matching — it demands a form of causal and structural understanding.

## Resources

- [ARC Prize Foundation](https://arcprize.org/) — Official ARC benchmark
- [Epoch AI](https://epoch.ai/) — Benchmarking and tracking AGI progress


## Benchmarking Ecosystem Updates (2026-04)

### Epoch AI Benchmarking Hub
ARC-AGI-2 is now featured on Epoch AI's Benchmarking Hub, providing centralized tracking of abstract reasoning benchmarks across the AI research landscape. This increases visibility and enables cross-benchmark comparisons.

### WeirdML v2
Håvard Tveit Ihle's WeirdML benchmark received a v2 update, adding a new dimension to abstract reasoning evaluation. METR is providing API cost support for participants, reducing the economic barrier to experimentation.

## Related

- [[gemini]] — Gemini 3 Deep Think performance
- [[ai-evals]] — AI evaluation benchmarks overview
- [[llm-evaluation-harness]] — Evaluation framework details
- [[agent-survival-benchmark]] — Other agent-focused benchmarks

## Sources

- [Epoch AI: ARC-AGI-2](https://substack.com/redirect/034037b3-c281-49ed-8de1-9ea5821ed9ef) (2026-04-20)

## See Also

- [[concepts/_index]]
