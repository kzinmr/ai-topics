# Deployment Simulation — OpenAI

> Source: https://openai.com/index/deployment-simulation/
> Published: 2026-06-11

## Overview

OpenAI published a research framework for evaluating AI models in realistic, multi-turn scenarios that approximate actual deployment conditions. Traditional evaluations measure capabilities in isolation, but real-world deployment involves extended conversations, tool use, and unexpected user behaviors.

## The Framework

Three components:

1. **Scenario design** — Realistic user scenarios with personas and follow-up behaviors
2. **Simulation engine** — A separate "user simulator" model calibrated against actual user behavior
3. **Evaluation suite** — Multi-dimensional evaluation (accuracy, safety, helpfulness, tool use, etc.)

## Scenario Categories

Five categories:
- Task completion
- Safety under pressure
- Ambiguity and correction
- Adversarial interaction
- Domain expertise

## Key Findings

- **Safety degradation over multiple turns** — safety guardrails weaken in extended conversations
- **Tool-use error compounding** — small errors in tool calls cascade through multi-step workflows
- **Helpfulness-safety tension** — polite/persistent interactions can erode safety boundaries
- **Extended conversations improve uncertainty calibration** — models become better calibrated over longer interactions
- **Emergent planning behaviors** — complex tasks reveal planning capabilities not visible in single-turn evals

## Release Artifacts

- Scenario library (200+ scenarios)
- User simulator
- Evaluation suite
- Benchmark results
- Interactive tool
