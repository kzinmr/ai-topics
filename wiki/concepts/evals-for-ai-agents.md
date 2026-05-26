---
title: "Evals for AI Agents"
type: concept
created: 2026-04-25
updated: 2026-05-08
tags:
  - evaluation
  - architecture
  - methodology
  - testing
aliases:
  - demystifying-evals-for-ai-agents
  - agent evaluation
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_demystifying-evals-for-ai-agents.md
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
related:
  - building-effective-agents
  - swe-bench
  - ai-resistant-evaluations
  - infrastructure-noise-agent-evals
  - macro-evals-for-agentic-systems
---

# Evals for AI Agents

A systematic guide to AI agent evaluation by Anthropic. "Without evals, you can only react to production outages after the fact. With evals, problems become visible before they affect users."

## Basic Structure of Evaluation

| Concept | Definition |
|------|------|
| **Task** | A single test with defined input and success criteria |
| **Trial** | One attempt at one task. Run multiple times to account for model output variance |
| **Grader** | Logic that scores agent performance. Includes multiple assertions |
| **Transcript** | Complete record of outputs, tool calls, reasoning, and intermediate results |
| **Outcome** | Final state of the environment (whether the reservation exists in the DB, not whether the agent says "reservation completed") |
| **Evaluation harness** | Infrastructure for end-to-end evaluation execution |
| **Agent harness** (scaffold) | System that makes the model function as an agent. The evaluation target is "harness + model" |
| **Evaluation suite** | Set of tasks measuring specific capabilities or behaviors |

## Why Build Evaluations

- **Early stage**: Forces the product team to define what "success" looks like
- **At scale**: Without evals, it is "flying without instruments" — user complaints → manual reproduction → fix → no idea if anything else broke
- **New model adoption**: With evals → days to adjust evals/prompts and upgrade. Without evals → weeks of manual testing
- **Baseline & regression testing**: Track latency, token usage, cost/task with a static task bank

## Grading Methods

### 1. Code-based Grading
- Regex matching
- Static analysis (linter, type checking, AST comparison)
- Unit tests and integration tests
- **Advantages**: Fast and deterministic
- **Disadvantages**: Cannot capture partial correctness or creative solutions

### 2. LLM-as-Judge
- Model evaluates output quality
- Rubric-based (scoring across multiple dimensions)
- Pairwise comparison
- **Challenge**: Evaluator bias (prefers longer answers, overrates its own outputs)
- **Mitigation**: Evaluation with multiple models, regular calibration against humans

### 3. Human Evaluation
- Most reliable but high cost
- Conducted periodically for calibrating LLM evaluations
- Descript case: human scoring → LLM scoring (by product-team-defined criteria) → periodic human calibration

## Agent Evaluation Pitfalls

### 1. Overfitting to Evals
- Overfitting to specific task sets, failing out-of-distribution
- Mitigation: Regular task rotation and held-out sets

### 2. The Transcript-Outcome Gap
- The agent says "done" but there is no actual result
- Always evaluate on the final state of the environment (not the agent's words)

### 3. Creative Cheating
- Opus 4.5 found a policy loophole in the τ²-bench flight booking problem → flagged as "failure" in eval, but was the best solution for the user.
- Agents find creative solutions beyond the limits of static evaluations.

### 4. Non-Determinism
- Output varies even for the same task and same model.
- Multiple trials + statistical significance testing are essential.

## Practical Examples

- **Claude Code**: Rapid iteration on internal and external user feedback → added narrow evals for conciseness and file editing → expanded to complex behaviors like over-engineering
- **Descript**: Video editing agent. Evaluation designed along three axes: "don't break things, follow instructions, do it well." Manual → LLM scoring + periodic calibration.
- **Bolt AI**: Started building evals after widespread adoption. Built a system of static analysis + browser agent testing + LLM judge in 3 months.

## See Also

- [[concepts/building-effective-agents]] — Building effective agents (redirects to harness-engineering)
- [[concepts/swe-bench]] — SWE-bench coding benchmark
- [[concepts/ai-resistant-evaluations]] — AI-resistant evaluation design
- [[concepts/infrastructure-noise-agent-evals]] — Infrastructure noise in evals
- [[concepts/macro-evals-for-agentic-systems]] — Macro evals: population-level behavior pattern discovery (OpenAI × Slalom)
