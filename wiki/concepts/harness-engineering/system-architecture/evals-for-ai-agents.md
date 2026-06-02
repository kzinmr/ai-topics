---
title: "Evals for AI Agents"
type: concept
aliases:
  - evals-for-ai-agents
  - agent-evaluation
  - demystifying-evals
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
  - evaluation
status: draft
sources:
  - "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"
  - "raw/articles/2026-01-09_anthropic_demystifying-evals-ai-agents.md"
---

# Evals for AI Agents

A systematic guide to evaluating AI agents, as proposed by Anthropic.

## Core Philosophy

> "The capabilities that make agents useful also make them difficult to evaluate. The strategies that work across deployments combine techniques to match the complexity of the systems they measure."

> "Writing evals is useful at any stage in the agent lifecycle. Early on, evals force product teams to specify what success means for the agent, while later they help uphold a consistent quality bar."

**The very properties that make agents useful also make them difficult to evaluate. Strategies that work across deployments combine techniques matched to the complexity of the systems they measure.**

## Basic Terminology

| Term | Definition |
|---|---|
| **Task** | A single test with defined inputs and success criteria |
| **Trial** | One execution of a task (run multiple times to account for model variance) |
| **Grader** | Logic that scores performance. May include multiple assertions |
| **Transcript/Trace** | Complete record of a trial including tool calls, reasoning, API messages |
| **Outcome** | The final environmental state (e.g., DB records), not the agent's verbal confirmation |
| **Eval Harness** | Infrastructure for end-to-end eval execution (concurrency, recording, scoring, aggregation) |
| **Agent Harness** | System that enables the model to function as an agent (orchestrating tools, returning results) |
| **Eval Suite** | Collection of tasks measuring specific capabilities/behaviors |

## Why Build Evals?

- **Prevent reactive debugging**: Stop teams from "flying blind" and guessing why changes broke things
- **Accelerate development**: Early evals enforce explicit success criteria. Later evals maintain quality standards
- **Speed up model adoption**: Teams with evals upgrade to new models in "days" rather than "weeks" of manual testing
- **Free baselines**: Automatically track latency, token usage, cost per task, error rates
- **High-bandwidth alignment**: Serve as a primary communication channel between product and research teams

## Grader Types and Scoring Strategies

| Type | Strengths | Weaknesses |
|---|---|---|
| **Code-based** | Fast, cheap, objective, reproducible, easy to debug | Brittle to valid variations, lacks nuance, unsuitable for subjective tasks |
| **Model-based (LLM)** | Flexible, scalable, captures nuance, handles open-ended/free-form output | Non-deterministic, expensive, requires human calibration |
| **Human** | Gold standard, aligns with expert judgment, calibrates LLM graders | Expensive, slow, hard to scale, requires SME access |

**Scoring approaches**: Weighted (combined thresholds), Binary (all must pass), Hybrid.

### Capability vs Regression Evals

- **Capability (quality)**: *"What can this agent do well?"* Start with low pass rates, target hard tasks, hill climb
- **Regression**: *"Can it still handle old tasks?"* Target ~100% pass rate, catch drift/regression
- **Evolution**: High pass-rate capability evals can "graduate" to the ongoing regression suite

## Agent-Specific Evaluation Approaches

| Agent Type | Key Strategy | Benchmarks/Tools |
|---|---|---|
| **Coding** | Deterministic graders (unit tests, static analysis) + transcript scoring for tool use/quality | SWE-bench Verified, Terminal-Bench |
| **Conversational** | Multi-dimensional scoring (state, turn count, tone) + LLM user simulation | τ-Bench, τ²-Bench |
| **Research** | Groundedness, coverage, source quality checks + frequent calibration of LLM rubrics against experts | BrowseComp |
| **Computer Use** | Real/sandboxed GUI environments + backend state validation (not just UI) | WebArena, OSWorld |

> **Computer Use insight**: Balance between DOM manipulation (fast, token-heavy) vs screenshots (slow, token-efficient). Should evaluate whether the agent selects the right tools per context.

## Handling Non-Determinism

Agent outputs vary per execution. Use these metrics based on product needs:

- **`pass@k`**: Probability of **≥1 success** in `k` trials. Best for tools where one working solution is enough.
- **`pass^k`**: Probability of **all `k` trials succeeding**. Best for customer-facing agents requiring consistency.
- *Divergence*: Identical at `k=1`. At `k=10`, `pass@k` → ~100%, `pass^k` → ~0%.

## Roadmap from Zero to One (Practical Steps)

1. **Start early**: 20-50 tasks from real failures are sufficient early on. Large effect sizes work with small samples
2. **Convert manual checks**: Use bug trackers, support queues, pre-release checks as initial tasks
3. **Clear task + reference solution**: If `pass@100 = 0%`, **the task/grader is broken**. Always provide a known-working reference
4. **Balance problem sets**: Test both positive and negative triggers to avoid one-sided optimization (e.g., over-searching vs under-searching)
5. **Isolate environments**: Clean state per trial. Prevent correlated failures from leftover files/cache
6. **Score outcomes, not paths**: Avoid rigid step checks. Allow creative solutions. Use partial credit for multi-component tasks
7. **Calibrate LLM judges**: Provide "unknown" escape hatches, use structured rubrics, score per dimension

## Eval Saturation

When evals reach 100% pass rates, they remain **useful for regression detection** but no longer provide **signals for improvement**. This is called **Eval Saturation**.

> "Large capability improvements manifest only as small score increases" (Anthropic)

**Countermeasures:**
- Continue saturated evals as regression suites
- Regularly add new capability evals to raise the "ceiling"
- "Graduate" evals to harder variants

## Creative Failures

When agents "fail" an eval, they may have actually discovered a better solution.

> Opus 4.5 failed a τ²-Bench flight booking problem by discovering a policy loophole, but actually produced a better solution for the user than the described eval intended. (Anthropic)

**Implication**: Rigid scoring logic may penalize creative problem-solving. Outcome-based grading and design that allows multiple correct answer patterns are important.

## Holistic Evaluation Framework (Swiss Cheese Model)

Anthropic recommends multiple layers of defense rather than a single eval:

| Layer | Role | Detects |
|---|---|---|
| **Automated Evals** | CI/CD auto-checks | Regression, capability gaps |
| **Production Monitoring** | Continuous monitoring in production | Distribution drift, real-world anomalies |
| **A/B Testing** | Compare old vs new agents | Relative performance differences |
| **Adversarial Testing** | Red teaming | Edge cases, security issues |
| **Human Evaluation** | Periodic expert review | Auto-eval calibration, nuance verification |
| **Feedback Loops** | Integrate user feedback | Real-world issues, eval improvement |

## Related Concepts

- [[concepts/harness-engineering]] — Top-level index
- [[concepts/building-effective-agents]] — Fundamental principles of agent building
- [[concepts/effective-harnesses-for-long-running-agents]] — Harnesses for long-running agents
- [[concepts/writing-tools-for-agents]] — Tool design for agents
