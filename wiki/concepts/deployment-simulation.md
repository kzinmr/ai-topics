---
title: "Deployment Simulation"
type: concept
created: 2026-06-18
updated: 2026-06-18
tags:
  - ai-agents
  - evaluation
  - robotics
  - testing
  - benchmark
  - agent-design-patterns
sources:
  - raw/articles/2026-06-11_openai_deployment-simulation.md
  - raw/articles/2025-08-19_sierra_simulations-the-secret-behind-every-great-agent.md
  - https://openai.com/index/deployment-simulation/
  - https://sierra.ai/blog/simulations-the-secret-behind-every-great-agent
related:
  - concepts/ai-benchmarks/tau-bench
  - concepts/scenario-based-simulation
  - entities/sierra
  - entities/openai
  - comparisons/openai-vs-sierra-agent-simulation
---

# Deployment Simulation

**Deployment simulation** is a testing paradigm for AI agents where **simulated user-agent conversations** replace traditional scripted test cases. Unlike conventional software testing (same input → same output), AI agents produce non-deterministic outputs from identical inputs — making it impossible to verify correctness through static assertions alone. Instead, the agent is placed in realistic multi-turn scenarios with simulated users, and an independent **judge agent** evaluates whether the interaction achieved its goal.

## Why It Matters

Traditional software testing assumes determinism. AI agents break this assumption:

- **Same input, different outputs** — stochastic generation makes pass/fail assertions unreliable
- **Multi-turn complexity** — agent behavior degrades or shifts over extended conversations
- **Goal-oriented, not script-oriented** — the question isn't "did the agent follow instructions?" but "did the user accomplish their goal?"
- **Safety emerges over turns** — safety guardrails can erode through persistent or adversarial conversation patterns

## The Three-Actor Pattern

Both [[entities/openai|OpenAI]] and [[entities/sierra|Sierra]] converge on a three-actor architecture:

```
┌─────────┐     conversation      ┌─────────┐
│  User    │ ◄──────────────────► │  Agent   │
│ Simulator│                       │ (DUT)    │
└─────────┘                       └─────────┘
     │                                  │
     └──────────┐           ┌───────────┘
                ▼           ▼
            ┌─────────────────┐
            │  Judge / Evaluator │
            └─────────────────┘
```

1. **User Simulator** — generates realistic user utterances (varied languages, tones, tech literacy, edge cases)
2. **Agent (Device Under Test)** — the production-bound AI agent responding to the simulated user
3. **Judge / Evaluator** — independently grades the conversation on goal achievement, policy compliance, safety, and quality

## Two Implementations

### OpenAI: Research Framework (June 2026)

OpenAI's approach is a **research-oriented evaluation framework** with five scenario categories:

| Category | Focus |
|----------|-------|
| Task completion | Can the agent accomplish the user's goal? |
| Safety under pressure | Does safety hold when users are persistent/polite? |
| Ambiguity and correction | Can the agent handle vague or corrected requests? |
| Adversarial interaction | Does the agent resist manipulation attempts? |
| Domain expertise | Can the agent reason within specialized domains? |

Key contributions:
- **200+ scenario library** — reusable, categorized test scenarios
- **User simulator model** — calibrated against actual user behavior patterns
- **Multi-dimensional evaluation** — accuracy, safety, helpfulness, tool use scored independently
- **Findings on safety degradation** — safety weakens over multiple turns, not just at turn 1
- **Tool-use error compounding** — small tool-call errors cascade through multi-step workflows

### Sierra: Product Platform (August 2025 — ongoing)

Sierra's approach is a **product-integrated testing platform** embedded in Agent OS:

- **Automatic test generation** from SOPs, knowledge bases, coaching transcripts, and conversation flows
- **Persona diversity** — users who speak different languages, vary in tech comfort, adopt many tones
- **Judge agent** evaluates: goal achievement, SOP compliance, brand guidelines, accuracy
- **CI/CD integration** — simulations plug into GitHub Actions, gate releases like unit tests
- **CX team accessibility** — non-engineers can run and review simulations in Agent Studio
- **Scale**: customers run 35,000+ tests/day, achieving 90% resolution rates

## Key Insights Across Both Approaches

### Safety Erosion Over Turns

Both OpenAI and Sierra find that **multi-turn conversations expose vulnerabilities invisible in single-turn tests**. OpenAI's research specifically documents safety degradation in extended interactions — a finding with implications for all long-running agent deployments.

### The User Simulator Problem

The quality of deployment simulation depends entirely on how realistic the user simulator is. OpenAI calibrates their simulator against actual user behavior; Sierra generates personas from real business data (SOPs, coaching transcripts). Both approaches recognize that **abstract test cases are insufficient** — simulations must be grounded in real-world usage patterns.

### Judge-as-Agent

Both use an LLM-based judge to evaluate conversations — an instance of [[concepts/llm-as-judge|LLM-as-judge]] applied to agent evaluation. This introduces a meta-evaluation challenge: who judges the judge?

### From Testing to Continuous Validation

Sierra's CI/CD integration and OpenAI's benchmark suite both point toward a future where **agent validation is continuous, not one-time** — more like monitoring than testing.

## Relationship to Existing Concepts

| Existing Concept | Relationship |
|-----------------|--------------|
| [[concepts/ai-benchmarks/tau-bench\|τ-bench]] | Sierra's benchmark; deployment simulation is the product layer built on τ-bench's evaluation philosophy |
| [[concepts/scenario-based-simulation\|Scenario-Based Simulation]] | Palantir's enterprise decision-forking; different domain (operations vs. agent testing) but shares the "sandbox before commit" pattern |
| [[concepts/harness-engineering\|Harness Engineering]] | Deployment simulation is the user-interaction layer of agent harnesses |
| [[concepts/eval-loops\|Eval Loops]] | Deployment simulation operationalizes eval loops for conversational agents |
| [[concepts/ai-benchmarks/tau-bench\|τ-bench]] evaluation axes | Multi-turn dialogue + policy compliance + reliability = the axes that deployment simulation tests |

## Open Questions

- Can deployment simulation benchmarks be standardized across vendors, or will each platform maintain proprietary scenario libraries?
- How do you prevent **judge contamination** — where the judge model shares biases with the agent being tested?
- What is the relationship between deployment simulation and **online evaluation** (monitoring real conversations post-deployment)?
- Should user simulators be adversarial by default, or does that distort the evaluation toward robustness at the expense of helpfulness?

## Related

- [[comparisons/openai-vs-sierra-agent-simulation]] — Detailed comparison of the two approaches
- [[concepts/ai-benchmarks/tau-bench]] — Sierra's underlying evaluation benchmark
- [[concepts/scenario-based-simulation]] — Palantir's enterprise simulation pattern
- [[entities/sierra]] — Sierra (product platform)
- [[entities/openai]] — OpenAI (research framework)
- [[concepts/harness-engineering]] — Agent harness design patterns
