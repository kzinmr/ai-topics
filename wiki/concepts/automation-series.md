---
title: "Antoine Buteau's Automation Series"
slug: automation-series
type: concept
aliases:
  - automation-series-antoine-buteau
  - buteau-automation-series
created: 2026-05-02
updated: 2026-05-02
tags:
  - concept
  - automation
  - architecture
  - workflow-design
  - deterministic
  - probabilistic
  - ai-automation
  - human-in-the-loop
status: complete
sources:
  - raw/articles/2026-05-02_antoine-buteau_automation-series-1.md
  - raw/articles/2026-05-02_antoine-buteau_automation-series-2.md
  - raw/articles/2026-05-02_antoine-buteau_automation-series-3.md
  - raw/articles/2026-05-02_antoine-buteau_automation-series-4.md
  - raw/articles/2026-05-02_antoine-buteau_automation-series-5-hitl.md
  - raw/articles/2026-05-02_antoine-buteau_automation-series-6-state.md
  - raw/articles/2026-05-02_antoine-buteau_automation-series-7.md
  - raw/articles/2026-05-02_antoine-buteau_automation-series-8.md
  - raw/articles/2026-05-02_antoine-buteau_automation-series-9.md
  - raw/articles/2026-05-02_antoine-buteau_automation-series-10.md
---

# Antoine Buteau's Automation Series

> **A 10-part series on automation architecture by Antoine Buteau.** The series establishes a comprehensive framework for building safe, reliable, and scalable automation by treating automation not as a single capability but as a deliberate architectural discipline spanning deterministic code, probabilistic AI, and accountable human judgment.

## Overview

Antoine Buteau's Automation Series provides a complete methodology for designing production automation systems. The core thesis across all 10 parts is that **effective automation architecture requires separating workflows into deterministic, probabilistic, and accountable components** — and deliberately assigning each responsibility to the right actor (code, model, or human).

The series progresses from foundational classification (Part 1) through deep dives into deterministic workflows (Part 2), AI automation (Part 3), boundary design (Part 4), human-in-the-loop patterns (Part 5), state management (Part 6), observability (Part 7), bounded agents (Part 8), failure modes and security (Part 9), and culminates in a practical architecture worksheet (Part 10).

## Series Parts

| # | Title | Focus Area | Core Thesis |
|---|---|---|---|
| 1 | [Automation Is Not One Thing](#part-1-automation-is-not-one-thing) | Classification & Framing | The fastest way to build bad automation is to treat it as a single category. |
| 2 | [Deterministic Workflows](#part-2-deterministic-workflows) | Reliability & Code | When reliability matters more than intelligence — use deterministic logic wherever possible. |
| 3 | [AI Automation](#part-3-ai-automation) | Probabilistic AI | AI should be a narrow, bounded step within a larger workflow, not the entire system. |
| 4 | [The Automation Boundary](#part-4-the-automation-boundary) | Code vs Model vs Human | Without an intentional boundary map, responsibilities are assigned "by accident." |
| 5 | [Human-in-the-Loop](#part-5-human-in-the-loop-is-a-design-pattern) | Review & Feedback | HITL is a deliberate design pattern, not a failure — it enables safe consequential automation. |
| 6 | [State, Idempotency, Retries, and Queues](#part-6-state-idempotency-retries-and-queues) | Infrastructure | Unglamorous backend components prevent failures, duplicates, and data corruption. |
| 7 | [Observability, Auditability, and Replay](#part-7-observability-auditability-and-replay) | Monitoring & Debugging | If you cannot explain what your automation did, you have a liability, not automation. |
| 8 | [Agents Inside Bounded Workflows](#part-8-agents-inside-bounded-workflows) | AI Agents | Agents are constrained operators within defined workflows, not autonomous digital employees. |
| 9 | [Failure Modes, Security, and Blast Radius](#part-9-failure-modes-security-and-blast-radius) | Risk & Safety | Design for failure containment, not perfect prevention. |
| 10 | [The Automation Architecture Worksheet](#part-10-the-automation-architecture-worksheet) | Practical Tool | The point of automation architecture is to make better decisions before the workflow is in production. |

## Key Insights

| Insight | Description |
|---|---|
| **Three Kinds of Work** | All automation work falls into deterministic (code), probabilistic (AI/model), or accountable (human) categories. |
| **Code Dispatches, AI Executes, Human Gates** | Deterministic logic should serve as a router that calls AI only when ambiguity is the primary task, with human gates for high-consequence decisions. |
| **Risk & Reversibility Matrix** | Score every action by impact and reversibility to determine the appropriate level of automation and human oversight. |
| **Confidence-Driven Action** | Confidence scores must drive specific behaviors (auto-proceed, exception queue, human review) or they are "decorative." |
| **Selective HITL** | Human review should be targeted (high-risk/low-confidence only), explainable, and operationally owned with a feedback loop. |
| **Idempotency Is Non-Negotiable** | Every operation must be safe to run multiple times. If you cannot answer "What happens if this runs twice?" you are not ready to launch. |
| **Observability Beyond Logging** | Must capture inputs, outputs, AI specifics, logic results, HITL decisions, and support replay — not just raw logs. |
| **Bounded Agents** | Agents need narrow missions, scoped tools, defined stop conditions, structured success criteria, and clear handoffs. |
| **Least Privilege & Blast Radius** | Automation should operate with the absolute minimum permissions. Build with failure containment from the start. |
| **Staged Autonomy** | Progress through Shadow → Draft → Assisted → Full Automation stages, earning autonomy through demonstrated reliability. |
| **Every Intervention Is Training Data** | Human review decisions feed back into evaluation loops, gold sets, and prompt improvements. |
| **Eight-Step Architecture Worksheet** | A practical tool for designing automation: Workflow → Boundary Map → Risk Score → Model Jobs → Gates & State → Observability → Security → Launch Strategy. |

---

## Part 1: Automation Is Not One Thing

**Core Thesis:** The fastest way to build bad automation is to treat it as a single category. Effective automation architecture requires separating workflows into deterministic, probabilistic, and accountable components.

The series opens by reframing the fundamental question teams should ask. Instead of "Can we automate this?" — which is too vague — teams should ask: **"Which parts of this workflow should be deterministic, which parts can be probabilistic, and where do we need human judgment?"**

**The Three Kinds of Work:**
- **Deterministic:** Same input always produces same output. Tools: Code, rules, schemas, APIs, tests.
- **Probabilistic:** Messy inputs with ambiguity. Tools: AI/LLMs with strict contracts.
- **Accountable:** High-consequence decisions requiring ownership. Tools: Human gates or strict control models.

The article introduces the **Automation Classification Matrix**, which separates work types (Exact rule, Data movement, Text classification, Information extraction, Drafting, Recommendation, Irreversible action) by owner (Code/Model/Human), AI usage, and controls.

> **The Operator's Rule:** Before launching, ask: What must be deterministic? Where does ambiguity exist? What is reversible? Where do we need a human gate? Who owns it after launch?

---

## Part 2: Deterministic Workflows

**Core Thesis:** "AI is expensive ambiguity machinery. Do not spend it on work that needs exactness."

This part establishes that deterministic workflows are the foundation of reliable automation. They are reliable, cost-effective, and accountable. The key architectural pattern is using **deterministic logic as a dispatcher** that routes to AI only when ambiguity is the primary task.

A critical concept introduced is **data contracts** — which prevent "prose leakage" from AI outputs into structured databases. By enforcing schemas and types at boundary points, teams ensure that probabilistic outputs don't corrupt deterministic systems.

**The Operator's Rule (3-step hierarchy):**
1. If a decision can be expressed as code, write code.
2. If the input is ambiguous, use AI as a bounded step.
3. If the consequence is serious, add a human gate.

---

## Part 3: AI Automation

**Core Thesis:** AI should be a **narrow, bounded step** within a larger workflow — not the entire system.

This part defines six AI job patterns: **Classify, Extract, Draft, Summarize, Route, and Recommend** — each with strict input/output contracts and gates.

**Confidence Scores** must be operationalized: High confidence + low risk = auto-proceed. Low confidence = exception queue. High confidence + irreversible action = human approval. Without driving specific actions, confidence scores are "decorative."

**Evaluation Loops** are essential for production AI automation:
- Gold sets (50-200 examples) for regression testing
- Sampled review (5-10%) for ongoing quality
- Drift checks to detect degradation
- Failure taxonomies for systematic improvement

> **The Operator's Rule:** "Use AI where ambiguity is the job. Do not use AI to replace state management, permissions, retries, audit logs, policy enforcement, or ownership."

---

## Part 4: The Automation Boundary

**Core Thesis:** Without an intentional boundary map, responsibilities are assigned "by accident."

This part introduces **The Boundary Map**, a deliberate design that assigns ownership across three actors:

| Actor | Owns | Examples |
|---|---|---|
| **Code** | Exactness | Required fields, permission checks, policy thresholds, idempotency, retries |
| **Models** | Ambiguity | Classification, extraction, sentiment — with fixed contracts and output schemas |
| **Humans** | Accountability | Low-confidence outputs, irreversible actions, sensitive communications |

The **Risk and Reversibility Decision Framework** scores actions by impact and reversibility:
- Low risk + easy reversal → auto with logs
- High risk + hard reversal → human owns decision

> **The Operator's Rule:** "If you cannot say which decisions belong to code, model, and human, you are not designing automation. You are distributing risk randomly."

---

## Part 5: Human-in-the-Loop Is a Design Pattern

**Core Thesis:** Human review is not a failure — it's a deliberate design pattern that enables automation to handle consequential work safely.

**Good HITL Design** is selective (high-risk/low-confidence only), explainable to the reviewer, and operationally owned with a feedback loop. **Bad HITL Design** requires approval on every item, gives reviewers no context, and has no feedback loop.

**Strategic Review Triggers:** Low confidence, high stakes, compliance requirements, technical failures, novelty (unseen cases), and quality control sampling.

**The Feedback Loop** is critical: every human intervention becomes operational training data. The recommended weekly review ritual: analyze cases → identify top failures → add to gold set → adjust prompts → run regression tests.

> **The Operator's Rule:** "If 95% of reviewed items are approved unchanged, raise the threshold carefully or narrow the review trigger."

---

## Part 6: State, Idempotency, Retries, and Queues

**Core Thesis:** While AI handles "intelligence," unglamorous backend components prevent failures, duplicates, and data corruption.

**Key Infrastructure Concepts:**
1. **Durable State:** Workflows must remember progress in durable storage, not chat transcripts.
2. **Idempotency:** The same operation executed multiple times must have the same effect as once. Use idempotency keys.
3. **Retries:** Only for temporary failures (timeouts, rate limits). Never retry logical failures.
4. **Queues:** Absorb bursts, manage rate limits, and provide dead-letter storage for failed items.

**State Transition Flow:**
```
RECEIVED → VALIDATED → MODEL_REQUESTED → MODEL_COMPLETED → GATE_DECIDED → ACTION_COMPLETED
                ↘              ↘                    ↘               ↘
            EXCEPTION      MODEL_FAILED         EXCEPTION      HUMAN_REVIEW
```

> **The Operator's Rule:** "If you cannot answer 'What happens if this runs twice?' you are not ready to launch. If you cannot answer 'Where is this item in the workflow?' you are not ready to scale."

---

## Part 7: Observability, Auditability, and Replay

**Core Thesis:** "If you cannot explain what your automation did, you do not have automation. You have a liability."

**Beyond Traditional Logging:** Automation observability must capture:
- Unique IDs tracing every event
- Inputs and outputs at each step
- AI specifics (prompt, model version, temperature)
- Logic/validation results
- HITL decisions with reviewer context
- Execution timing and duration

**Audit Trails** must distinguish between three actor types — code, model, or human — with each audit event including `actor_type`, `decision`, `reason`, and `policy_version`.

**Replayability** enables testing past cases through current or previous logic to validate changes, build regression tests, and recover from failures. This is essential for debugging, compliance, and continuous improvement.

> **The Operator's Rule:** If you cannot answer the five questions (input, rules, model output, threshold, reviewer) and replay the event, the workflow is not ready for consequential work.

---

## Part 8: Agents Inside Bounded Workflows

**Core Thesis:** The practical use of AI agents is as **constrained operators** within defined workflows — not as autonomous digital employees.

**The Bounded Agent Mental Model:** An agent is like a junior employee with strict supervision. It has:
- A defined job (narrow mission)
- Scoped tools (subset of available tools)
- Clear permissions (what it can and cannot do)
- Success criteria (Definition of Done)
- Logging (every action recorded)
- Stop conditions (failure modes that halt execution)

**Tool-Permission Framework:** Before deployment, ask: "If you wouldn't give this tool to an unsupervised junior employee, don't give it to an agent without controls."

**Stop Conditions:** Max tool calls exceeded, missing required data, restricted category detected, injection attempt detected, timeout reached.

> **Summary Checklist:** Is the mission narrow? Are tools scoped? Are stop conditions defined? Is success defined by structured output? Is there a clear handoff?

---

## Part 9: Failure Modes, Security, and Blast Radius

**Core Thesis:** The useful question is not how to prevent every failure, but how much damage a failure can do, how quickly you can detect it, and how cleanly you can recover.

**Failure Taxonomy (10 types):**
| # | Failure Mode |
|---|---|
| 1 | Misclassification |
| 2 | Bad Extraction |
| 3 | Hallucinated Draft |
| 4 | Duplicate Side Effect |
| 5 | Unauthorized Action |
| 6 | Prompt Injection |
| 7 | Data Exfiltration |
| 8 | Irreversible Write |
| 9 | Silent Queue Backlog |
| 10 | Policy/Model Drift, API Change |

**Principle of Least Privilege:** Automation should operate with the absolute minimum permissions. Key practices: read only what's needed, separate drafting from sending, use scoped tokens, never give delete access by default.

**Stages of Autonomy Launch Strategy:**
1. **Shadow Mode** — AI recommends, humans act
2. **Draft Mode** — AI creates drafts, humans send
3. **Assisted Mode** — AI acts on low-risk items, humans review the rest
4. **Full Automation** — Low-risk, reversible, well-observed work only

> **The Operator's Rule:** "Build automation with failure containment from the start."

---

## Part 10: The Automation Architecture Worksheet

**Core Thesis:** The point of automation architecture is to make better decisions before the workflow is in production.

**8-Step Architecture Worksheet:**
1. **Workflow Definition** — Name, outcome, trigger, out-of-scope
2. **Boundary Mapping** — Code vs Model vs Human per step
3. **Risk & Reversibility** — Score each action
4. **Narrow Model Jobs** — Strict contracts with output schemas
5. **Decision Gates & State** — Idempotency keys, state machine
6. **Observability & Evaluation** — Gold sets, review cadence
7. **Security & Ownership** — Named owner, least privilege
8. **Launch Strategy** — Earn autonomy through stages

**Final Operator Checklist:**
- [ ] Deterministic parts handled by code?
- [ ] AI steps bounded by schemas?
- [ ] All side effects idempotent?
- [ ] Confidence gates change behavior?
- [ ] Named human owner assigned?
- [ ] Failure containment in place?
- [ ] Observable and replayable?
- [ ] Launch strategy defined?

---

## Related Pages

- [Concepts Index](/concepts/_index)
