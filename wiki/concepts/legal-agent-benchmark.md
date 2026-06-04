---
title: "Legal Agent Benchmark (LAB)"
created: 2026-05-27
updated: 2026-05-27
type: concept
tags:
  - agent-evaluation
  - benchmark
  - ai-adoption
  - ai-agents
aliases:
  - LAB
  - Harvey Legal Agent Benchmark
related:
  - concepts/evals-for-ai-agents
  - concepts/ai-evaluation
  - concepts/jagged-intelligence
sources:
  - raw/articles/2026-05-26_harvey-ai-initial-results-legal-agent-benchmark.md
  - https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
  - https://github.com/harveyai/harvey-labs
---

# Legal Agent Benchmark (LAB)

**Legal Agent Benchmark (LAB)** is an open-source benchmark developed by [[entities/harvey|Harvey]] for evaluating AI agents on complex, long-horizon legal tasks. Released in May 2026, LAB uses an **all-pass standard** — a task passes only if *every* required rubric criterion passes — mirroring the strict review standards legal work demands. LAB also provides agent traces for **behavioral analysis**, making it one of the first domain-specific agent benchmarks to study not just *what* score an agent achieves but *how* it works.

## Key Design Principles

- **All-pass grading**: Expert-curated rubrics specify facts, conclusions, citations, structural requirements, and analytical moves. Every criterion must pass.
- **Multi-grader averaging**: Agent runs are graded multiple times across model families to prevent grader bias.
- **Behavioral traces**: Every run produces an action trace (Read → Search → Execute → Write → Validate → Edit), enabling analysis of agent decision patterns beyond raw scores.
- **Heterogeneous practice areas**: Tasks span corporate, regulatory, IP, tax, employment, healthcare, and more — reflecting the diversity of real legal work.

## Initial Results (May 2026)

Harvey baselined frontier models on a hold-out set mirroring the public LAB task distribution:

| Model | All-Pass Score |
|-------|---------------|
| Claude Opus 4.7 | **7.1%** |
| Claude Sonnet 4.6 | 5.4% |
| Claude Opus 4.6 | 4.2% |
| GPT-5.5 | 2.1% |
| Gemini 3.5 Flash | 0.8% |

**Key finding**: Under strict all-pass standards, frontier models complete **less than 10%** of legal tasks end-to-end. Legal work is far from saturated.

## Three Core Trends

### 1. Jagged Intelligence Across Practice Areas
No single model leads every practice area. Different models bring different priors:

- **GPT-5.5** leads in regulated and emerging-company groups (retrieval-heavy research)
- **Opus 4.7** leads in corporate transactions and funds (synthesis and analytical work)
- **Sonnet 4.6** leads in privacy, tax, and private-client work (structured comparison vs statutes)

This is a canonical example of **jagged intelligence**: the uneven profile of LLMs where some tasks work extremely well while others fail catastrophically in unpredictable ways.

### 2. Cost and Latency at the Frontier
Operating at the frontier of agent intelligence comes with steep costs:

| Model | Per-Task Cost | Per-Task Latency |
|-------|--------------|-----------------|
| Opus 4.7 | ~$50.90 | ~22 minutes |
| GPT-5.5 | ~3x cheaper | — |
| Gemini 3.5 Flash | — | ~6 minutes (~4x faster than Opus) |

Production agent deployments need high scores *inside a budget* — both dollar cost and wall-clock time.

### 3. Behavioral Analysis of Agent Traces

LAB's fixed action space has six actions: Read, Search, Execute, Write, Validate, Edit. By analyzing action sequences, Harvey identified emergent behaviors that correlate with outcomes:

| Behavior | All-Pass Impact |
|----------|----------------|
| **Verifying and revising** (close the revise-after-check loop) | **+1.5 points** |
| Post-draft validation (review step after drafting) | +0.8 points |
| Thorough research before drafting (>90% document coverage) | +0.4 points |
| Targeted retrieval (search during the run) | +0.3 points |
| Structured analysis (code/shell tools) | +0.3 points |
| Grounding drafts against the record | +0.3 points |
| Noisy tool fan-out (5+ parallel tool calls) | **-0.5 points** |
| Drafting without review (no validation or revision) | **-1.2 points** |

**Self-correction is the strongest positive signal.** These patterns resemble markers of strong associate work product: build context before drafting, check work before submitting, make substantive revisions after review, avoid excessive parallelism.

### Model-Specific Behavioral Priors

- **Opus 4.7**: Most visibly self-corrective — spends more trajectory on drafting, frequently re-checks, validates, and revises. Translates to higher scores on drafting tasks.
- **GPT-5.5**: Largest search segment — runs document search more heavily, covers wider breadth of documents. Translates to higher scores on research-focused tasks.

## Agent Action Space

| Action | Description |
|--------|-------------|
| **Read** | Open a document from the matter file |
| **Search** | Query the matter for content across documents |
| **Execute** | Run analysis code over the matter or its outputs |
| **Write** | Produce or extend output in a deliverable |
| **Validate** | Run an explicit check of a draft against the instruction or the matter record |
| **Edit** | Modify the work product after a validation step |

## Future Directions

LAB will grow on three fronts:
1. **Benchmark expansion**: Richer task families, more practice areas, adjacent professional-service workflows beyond legal, longer-context matters. Partnership with Artificial Analysis for a regularly-updated leaderboard.
2. **Research program**: Studying how agents handle long-horizon tasks, domain knowledge transfer across sub-domains, and cost/latency optimization.
3. **Model provider collaboration**: Working with labs to understand what model-layer changes improve legal-agent performance.

## Graph Structure Query

```
[legal-agent-benchmark] ──author──→ [entity: harvey]
[legal-agent-benchmark] ──relates-to──→ [concept: evals-for-ai-agents]
[legal-agent-benchmark] ──embodies──→ [concept: jagged-intelligence]
[legal-agent-benchmark] ──extends──→ [concept: ai-evaluation]
[legal-agent-benchmark] ──relates-to──→ [concept: agent-observability]
[legal-agent-benchmark] ──contrasts──→ [concept: swe-bench]
```

This section informs graph queries: authored by [[entities/harvey]], relates to [[concepts/evals-for-ai-agents]] and [[concepts/ai-evaluation]], embodies the [[concepts/jagged-intelligence]] phenomenon, and contrasts with coding-focused benchmarks like [[concepts/swe-bench]].

## Related Concepts
- [[concepts/evals-for-ai-agents]] — Broader framework for agent evaluation
- [[concepts/ai-evaluation]] — AI model evaluation methodologies
- [[concepts/jagged-intelligence]] — Uneven LLM capability profiles
- [[concepts/swe-bench]] — Leading coding agent benchmark (contrasting domain)
- [[concepts/agent-observability]] — Observing agent behavior and traces

## Fireworks AI × Harvey Joint Results (June 2026)

Fireworks AI and Harvey jointly published June 2026 results on a 100-task slice of LAB, demonstrating two approaches to close the open-vs-closed performance gap.

### Hybrid Harness: Open-Source Worker + Frontier Advisor

A hybrid harness was built with GLM 5.1 as the worker and Claude Opus 4.7 as a callable advisor. The worker self-triggers the advisor on hard sub-tasks — a "frontier model as callable tool, not dependency" pattern.

| Configuration | All-Pass / 100 | Total Cost (100 tasks) |
|---|---|---|
| Claude Opus 4.7 (end-to-end) | 14 | $954 |
| GLM 5.1 (worker only) | 12 | $121 |
| GLM 5.1 + Opus 4.7 advisor | **18** | **$368** |
| Kimi K2.6 base | 11 | $75 |
| Kimi K2.6 + SFT | 15 | $84 |

- Advisor invoked 0.83x/task average (sparse-but-targeted use)
- vs Opus 4.7 alone: **+4 tasks all-pass, -$586**
- vs GLM 5.1 alone: **+6 tasks all-pass, +$246**

### Post-Training (SFT + RFT on Kimi K2.6)

**Supervised Fine-Tuning (SFT)**: LAB-passing trajectories used directly for SFT. No reward model needed.
- All-pass: 11 → 15 / 100 (+4 tasks)
- Mean score: 0.863 → 0.876

**Reinforcement Fine-Tuning (RFT)**: LAB evaluator used directly with per-criterion rewards.
- 46 rollout steps, mean score 0.863 → 0.886
- Jump from 0.864 to 0.882 between steps 43–44 (surpasses SFT checkpoint 0.876)

### Cost vs Quality Implications

- GLM 5.1: 0.8921 mean score at **$121** (1/8 of Opus 4.7's $954 for 0.911 mean)
- GPT-5.5: 0.892 mean score at **$560**
- Paradigm shift: from "use the smartest model on every query" to "use frontier quality only where it changes the answer, controlled open-source for the rest"

## Sources
- [Initial Results on Legal Agent Benchmark](https://x.com/i/article/2059284537503285248) — Harvey AI, May 2026
- [Introducing Harvey's Legal Agent Benchmark](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)
- [Harvey Labs GitHub](https://github.com/harveyai/harvey-labs)
- [Open Source Agents Frontier Advisors](https://fireworks.ai/blog/open-source-agents-frontier-advisors) — Fireworks AI × Harvey, June 2026
