---
title: "Production AI Agents"
type: concept
created: 2026-07-25
updated: 2026-07-25
tags:
  - ai-agents
  - agentic-engineering
  - production-ml
  - evaluation
  - methodology
  - healthcare
related:
  - [[entities/hugo-bowne-anderson]]
  - [[concepts/ai-agent-engineering]]
  - [[concepts/agentic-engineering]]
  - [[concepts/harness-engineering]]
sources:
  - raw/newsletters/2026-07-25-four-months-inside-a-production-ai-agent-what-real-users-changed.md
---

# Production AI Agents

> *"If anyone says they can swap a model and know with no manual review that it'll be better, they're lying."*
> — William Horton, on the reality of production model evaluation

## Overview

Production AI agents are AI systems deployed to real users in enterprise settings — handling live traffic, subject to reliability and safety requirements, and continuously evaluated against business outcomes. Unlike prototypes or demos, production agents must contend with unpredictable user behavior, edge cases that evade guardrails, and the constant pressure of model churn as LLM providers release new versions.

The difference between a demo agent and a production agent is not just scale — it is the presence of **structured evaluation systems**, **guardrails**, **monitoring**, and **iterative improvement** based on real usage data. The production experience consistently reveals that user behavior diverges sharply from what builders expect, making evaluation-driven development not just useful but essential.

## The Maven Assistant Case Study

Maven Clinic, a digital health platform serving women's and family health, deployed a production AI agent called **Maven Assistant** to handle member conversations at scale. The following insights come from a July 2026 interview on the **Vanishing Gradients** podcast between Hugo Bowne-Anderson and **William Horton** (Maven's AI/ML team lead), covering the first four months of production operation.

### Rollout

- **100% user rollout**: Every Maven member received access to the AI agent, not a phased or percentage-based deployment.
- **Weekly conversation volume grew 10x** over the four-month period, indicating rapid user adoption and engagement.
- The team invested heavily in provider search and appointment booking flows — the high-complexity, high-value interactions they expected users to need most.

### Unexpected Usage Patterns

The most striking finding was a **mismatch between what the team built for and what users actually needed**:

- **50-60% of all conversations** were basic health questions — not the complex provider or appointment tasks the team had prioritized.
- Users treated Maven Assistant as a **general health Q&A tool**, effectively using it as a triage-layer before engaging with the provider system.
- This pattern was stable over time — it wasn't an early-adopter novelty that faded.

> **Lesson**: The production agent revealed genuine user needs that no amount of pre-launch research or persona-building could have predicted. The team had to reorient their development roadmap around the actual usage distribution.

### Evaluation System

Maven's evaluation infrastructure was one of the most sophisticated documented in production AI:

- **1,000+ deterministic tool-use test scenarios** covering the core interaction paths
- **LLM-as-judge evaluations** using multiple judge models with cross-validation
- **Synthetic negatives** — deliberately crafted failure cases to test guardrail robustness
- **Manual review** by subject matter experts (clinicians) for high-stakes outputs
- The evaluation harness was the **central operating system for iteration** — every model swap, prompt change, or tool modification was gated by this system

### Guardrail Failures

Real production operation revealed subtle and counterintuitive guardrail failure modes:

- **Emergency guardrail failure**: The agent told an ER patient to *"go to the ER"* — which sounds correct, but the guardrail was designed to detect emergency keywords and escalate, not to answer. The failure was that the guardrail *fired correctly* but produced guidance indistinguishable from the agent's normal operating mode.
- **Zendesk content leakage**: The agent pulled knowledge base articles from Zendesk written for customer support staff, not patients — telling users to *"open the app"* or *"contact support"* instead of answering their actual question.
- These failures were **not detectable from synthetic or canned test data** — only real user traffic revealed them.

### Model Switching

Over the four-month period, Maven shifted its model strategy:

- **Initial choice**: Gemini Flash 2.5 was the initial deployment model.
- **Migration direction**: The team moved **toward OpenAI models**, with significant evaluation work on GPT-5.6, and new models codenamed **Terra** and **Fable**.
- **Evaluation impact**: Each model swap required running the full 1,000+ test suite plus manual review — no evaluation short-circuit was possible.
- **William Horton's key quote**: *"If anyone says they can swap a model and know with no manual review that it'll be better, they're lying."*

### Open-Weight Model Economics

The interview also explored the economics of self-hosted open-weight models:

- A smaller self-hosted model still requires an **always-on GPU**, infrastructure provisioning, and ongoing engineering attention.
- The total cost of ownership (GPU compute + infra + ops labor) often **exceeds API-based models** when engineering time is factored in.
- Open-weight models remain attractive for **data sovereignty** and **privacy** reasons, but the economic argument is not straightforward.

## Key Lessons

### 1. Build for Discovery, Not Assumption

The single most important lesson from Maven Assistant: **you cannot predict what users will actually do with an AI agent.** 50-60% of usage fell into a category the team had not prioritized. Production AI agents should be built with instrumentation and rapid feedback loops from day one — treat user behavior as a discovery process, not a validation of assumptions.

### 2. Evaluation Is Non-Negotiable and Never Automatic

Model switching is not a drop-in replacement — every model change requires comprehensive re-evaluation. The 1,000+ test suite, LLM judges, synthetic negatives, and manual review are not optional overhead; they are the cost of operating a production AI system that people depend on. No automated evaluation pipeline can fully replace human review for production safety.

### 3. Guardrails Need Real-World Testing

Canned test cases will not catch the failure modes that emerge in production. The ER triage and Zendesk content failures are examples of guardrails that worked correctly in testing but produced wrong outputs in real use. Guardrails must be tested against **live traffic patterns** and continuously refined.

### 4. Architecture Should Follow Usage Patterns

The Maven team's key architectural lesson: **provider search and appointment booking should be one agent**. The separation between these functions created friction in the user experience. Model experiments should **start before the original model choice hardens** into the system architecture — waiting until you're locked in makes switching more costly.

### 5. Open-Weight Economics Are Nuanced

Self-hosting is not automatically cheaper. The always-on infrastructure cost and engineering attention required for a smaller model can exceed API costs. The decision should be driven by **privacy requirements and data sovereignty**, not assumed cost savings.

## Related Concepts

- **[[concepts/ai-agent-engineering]]** — Broader principles for building reliable AI agents
- **[[concepts/agentic-engineering]]** — Engineering practices for agentic systems
- **[[concepts/harness-engineering]]** — The evaluation harness as the operating system for AI development
- **[[entities/hugo-bowne-anderson]]** — Vanishing Gradients host who conducted the Maven Assistant interview
- **[[concepts/guardrails]]** — Safety mechanisms for production AI agents
- **[[concepts/ai-evals]]** — Evaluation methodologies for AI systems
