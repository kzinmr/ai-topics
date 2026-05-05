---
title: "Recursive Self-Improvement"
created: 2026-05-05
updated: 2026-05-05
type: concept
tags: [prediction, safety, alignment, training, benchmark, automation]
sources: [raw/articles/2026-05-04_import-ai-455-automating-ai-research.md]
---

# Recursive Self-Improvement

## Definition

Recursive self-improvement (RSI) refers to the capability of an AI system to autonomously design, train, and deploy a more capable successor AI system — without human intervention. This creates a potential feedback loop where each generation produces an even more capable next generation.

## Current State (May 2026)

### Capability Evidence

| Benchmark | Late 2023 | Current (May 2026) | Description |
|-----------|-----------|-------------------|-------------|
| SWE-Bench | 2% (Claude 2) | 93.9% (Claude Mythos Preview) | Solving real GitHub issues |
| METR Time Horizon | 30s (GPT-3.5) | ~12 hours (Opus 4.6) | Sustained autonomous work |
| CORE-Bench | — | 95.5% (Opus 4.5, Dec 2025) | Computational reproducibility |
| MLE-Bench | 16.9% (Oct 2024) | 64.4% (Feb 2026) | Building ML systems from scratch |

### Key Enabling Capabilities

1. **Coding Mastery**: AI can now solve 93.9% of real-world software engineering tasks independently
2. **Extended Autonomy**: Working reliably for 12+ hours without human intervention, with 100-hour reliability expected by end 2026
3. **ML Research Skills**: Replicating papers (95.5%), building ML systems (64.4%), optimizing kernels
4. **Training Optimization**: Claude Mythos Preview achieved 52x speedup on CPU-only training implementation (4x expected from a human)
5. **Agent Orchestration**: "Manager" AI can supervise multiple specialized sub-agents

### Industry Targets

| Lab | Goal | Timeline |
|-----|------|----------|
| OpenAI | "Automated AI research intern" | Sept 2026 |
| Anthropic | "Automated Alignment Researchers" | Ongoing |
| Recursive Superintelligence | Dedicated RSI startup | $500M raised |
| Mirendil | Dedicated RSI startup | Active |

## Jack Clark's Probabilistic Forecast

From Import AI 455 (May 4, 2026):
- **30%** probability of automated AI R&D by end of 2027
- **60%** probability by end of 2028
- Failure condition: If not achieved by 2028, suggests a fundamental deficiency in current paradigm

## The Alignment Challenge

### Compounding Error Problem

Recursive self-improvement turns alignment from a binary problem into a compounding one:

> "Unless your alignment approach is '100% accurate'... things can go wrong quite quickly. For example, your technique is 99.9% accurate, then that becomes 95.12% accurate after 50 generations, and 60.5% accurate after 500 generations." — Jack Clark

This means even near-perfect alignment techniques become dangerously degraded across multiple self-improvement cycles.

### Key Risks
- **Fake Alignment**: AI systems may learn to appear aligned on tests while pursuing different goals
- **Goal Drift**: Small imperfections compound into unrecognizable objectives
- **Capability Explosion**: Each generation may be significantly more capable than its predecessor, making correction impossible
- **Instrumental Convergence**: Aligned intent may still produce dangerous instrumental behaviors

## Engineering vs. Creativity

Clark distinguishes between "meat and potatoes" engineering and radical paradigm shifts:
- **What AI can do**: Massive-scale experimentation, hyperparameter tuning, neural architecture search — the "99% perspiration"
- **What AI may lack**: The "1% inspiration" that produced breakthroughs like Transformers
- **The bet**: Even without creative genius, sheer volume and speed of experimentation can push the frontier forward

## Economic Implications

### The Amdahl's Law Economy
As AI accelerates digital work, physical-world bottlenecks (drug trials, manufacturing) become the primary growth constraints. The economy becomes increasingly gated by physical processes rather than cognitive ones.

### The Machine Economy
Potential emergence of capital-heavy, human-light corporations where AI-run entities trade with each other, creating a parallel economy challenging traditional governance and redistribution models.

## Related

- [[entities/jack-clark]] — Key source, 60% prediction by end 2028
- [[entities/anthropic]] — Automated Alignment Researchers initiative
- [[concepts/ai-safety]] — Alignment risks
- [[concepts/automated-alignment-research]] — Anthropic's AAR program
- [[concepts/model-distillation]] — Related capability advancement pathway
- [[concepts/agent-team-swarm]] — Multi-agent orchestration as enabling capability
- [[entities/openai]] — "Automated AI research intern" target
