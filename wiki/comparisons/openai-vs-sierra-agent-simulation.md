---
title: "OpenAI vs Sierra: Agent Simulation Approaches"
type: comparison
created: 2026-06-18
updated: 2026-06-18
tags:
  - ai-agents
  - agent-evaluation
  - simulation
  - evaluation
  - comparison
sources:
  - raw/articles/2026-06-11_openai_deployment-simulation.md
  - raw/articles/2025-08-19_sierra_simulations-the-secret-behind-every-great-agent.md
  - https://openai.com/index/deployment-simulation/
  - https://sierra.ai/blog/simulations-the-secret-behind-every-great-agent
related:
  - concepts/deployment-simulation
  - entities/openai
  - entities/sierra
  - concepts/ai-benchmarks/tau-bench
---

# OpenAI vs Sierra: Agent Simulation Approaches

Both [[entities/openai|OpenAI]] and [[entities/sierra|Sierra]] independently arrived at the same core insight: **AI agents need simulated conversations, not scripted tests, to validate deployment readiness.** This page compares their approaches.

## Summary Table

| Dimension | OpenAI (June 2026) | Sierra (August 2025 — ongoing) |
|-----------|-------------------|-------------------------------|
| **Type** | Research framework + benchmark suite | Product platform (Agent OS) |
| **Audience** | Researchers, model developers | Enterprise CX teams, developers |
| **User Simulator** | Dedicated model calibrated on real user behavior | Auto-generated personas from SOPs, knowledge bases, coaching transcripts |
| **Scenario Source** | 200+ curated scenarios across 5 categories | Auto-generated from business data |
| **Judge** | Multi-dimensional evaluation suite | Independent judge agent (goal, SOP, brand, accuracy) |
| **Integration** | Standalone benchmark, interactive tool | CI/CD (GitHub Actions, CLI), Agent Studio UI |
| **Key Finding** | Safety degradation over turns; tool-use error compounding | 35K+ tests/day; 90% resolution, 4.5/5.0 CSAT |
| **Openness** | Open-sources scenario library + simulator | Platform-integrated, not separately available |

## Shared Architecture: Agent + User + Judge

Both converge on the same three-actor pattern, though terminology differs:

| Role | OpenAI Term | Sierra Term |
|------|-------------|-------------|
| The system being tested | Model / Agent | Agent |
| Fake human conversational partner | User simulator | Simulated user / Persona |
| Independent grader | Evaluation suite | Judge agent |

This convergence suggests the pattern is **fundamental to agent evaluation**, not vendor-specific.

## Approach Differences

### Research vs. Product

OpenAI frames deployment simulation as a **research contribution** — a methodology + benchmark for the community. The output is a scenario library, a simulator model, and evaluation metrics that anyone can use.

Sierra frames it as a **product feature** — simulations are built into Agent OS and tightly integrated with agent development workflows. The value is in the automation and CI/CD integration, not the research methodology.

### Scenario Generation

**OpenAI**: Curated, hand-designed scenarios across 5 categories (task completion, safety, ambiguity, adversarial, domain expertise). Quality over quantity — 200+ scenarios designed to probe specific failure modes.

**Sierra**: Auto-generated from business data (SOPs, knowledge bases, coaching transcripts, conversation flows). Quantity + relevance — scenarios grounded in actual customer interactions, not abstract test cases.

This reflects different philosophies:
- OpenAI: **top-down** — researchers design scenarios to test known failure categories
- Sierra: **bottom-up** — the system derives scenarios from real business context

### Evaluation Focus

**OpenAI** evaluates across **research dimensions**: accuracy, safety, helpfulness, tool use. The emphasis is on understanding model capabilities and failure modes.

**Sierra** evaluates across **business dimensions**: goal achievement, SOP compliance, brand guidelines, response quality. The emphasis is on production readiness and customer satisfaction.

### Scale and Velocity

OpenAI's framework is designed for **periodic benchmarking** — run the suite, analyze results, improve the model.

Sierra's platform enables **continuous validation** — 35,000+ tests/day, integrated into every deployment pipeline. This is closer to unit testing than benchmarking.

## What OpenAI Found That Sierra Didn't (Explicitly) Document

OpenAI's research surfaced specific **multi-turn failure modes** that have broad implications:

1. **Safety degradation over turns** — safety guardrails weaken in extended conversations, not just at turn 1
2. **Tool-use error compounding** — small errors in tool calls cascade through multi-step workflows
3. **Helpfulness-safety tension** — polite/persistent users can erode safety boundaries
4. **Emergent planning** — complex tasks reveal planning behaviors invisible in single-turn evals

These findings complement Sierra's product-focused metrics (resolution rate, CSAT) with **mechanistic insights** about *why* agents fail.

## What Sierra Found That OpenAI Didn't (Explicitly) Document

Sierra's product deployment surfaced practical insights about **operationalizing** simulations:

1. **Non-engineer accessibility** — CX teams can run and review simulations without engineering support
2. **Automatic scenario generation** — the overhead of manual test creation is the primary blocker to adoption
3. **CI/CD gating** — simulations as release gates (like unit tests) is the key to preventing regressions
4. **Business grounding** — abstract test cases don't capture real customer behavior; scenarios must come from actual business data

## Synthesis: Complementary Perspectives

The two approaches are **complementary, not competing**:

- OpenAI provides the **research foundation** — why simulations work, what they reveal, how to design them
- Sierra provides the **product implementation** — how to make simulations accessible, automated, and continuous

Together, they suggest a maturity model for agent simulation:

```
Level 0: No testing beyond manual review
Level 1: Scripted test cases (deterministic assertions)
Level 2: Simulated conversations with curated scenarios (OpenAI-style)
Level 3: Auto-generated simulations from business data (Sierra-style)
Level 4: Continuous simulation integrated into CI/CD with automated gating
```

## Open Questions

- Will OpenAI's scenario library become a community standard, or will vendor-specific libraries dominate?
- Can Sierra's auto-generation approach be applied to non-CX domains (coding agents, research agents)?
- How do you validate the judge? Both approaches assume the judge is reliable, but judge reliability is itself untested.
- What's the relationship between deployment simulation and **online monitoring** of real conversations?

## Related

- [[concepts/deployment-simulation]] — The overarching concept
- [[concepts/ai-benchmarks/tau-bench]] — Sierra's underlying benchmark
- [[entities/openai]] — OpenAI
- [[entities/sierra]] — Sierra
