---
title: Antoine Buteau
type: entity
created: 2026-05-02
updated: 2026-05-02
status: L2
tags:
  - person
  - bizops
  - automation-architecture
  - strategy-execution
  - technical-literacy
aliases:
  - anbuteau
  - Antoine Buteau
sources:
  - https://www.antoinebuteau.com/
  - https://x.com/anbuteau
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

# Antoine Buteau

**Antoine Buteau** (@anbuteau) is a BizOps leader and writer whose work sits at the intersection of automation architecture, organizational power dynamics, individual agency, and technical leadership. He is currently **Head of BizOps at Shakepay** (Canada's leading Bitcoin rewards platform) and was previously **Head of BizOps at Replit**. Before moving into tech leadership, he spent five years building a boutique consulting firm specialized in strategy execution, and began his career in professional services implementing enterprise search engines.

His writing — published at [antoinebuteau.com](https://www.antoinebuteau.com/) — spans hundreds of articles across multiple series, most notably a 10-part **Automation Series** that has become a reference framework for building safe, scalable AI-augmented workflows. He lives in Quebec with his wife, two kids, and a dog.

## Career

| Period | Role |
|--------|------|
| Early Career | Professional services — implemented enterprise search engines |
| ~5 years | Founder, boutique consulting firm specializing in strategy execution |
| Past | Head of BizOps at **Replit** |
| Current | Head of BizOps at **Shakepay** (Canada) |

## Writing Series

### Automation Series (10 Parts)

Buteau's flagship series — the key work documented in this wiki — delivers a complete automation architecture framework. The series treats automation not as a single category but as a deliberate design practice requiring boundary maps, risk analysis, and human-centered governance.

| # | Title | Core Thesis |
|---|-------|-------------|
| 1 | Automation Is Not One Thing | Three kinds of work: deterministic, probabilistic, and accountable. The right question is not "Can we automate this?" but "Which parts should be deterministic, which probabilistic, and where do we need human judgment?" |
| 2 | Deterministic Workflows: When Reliability Matters More Than Intelligence | "AI is expensive ambiguity machinery. Do not spend it on work that needs exactness." Use deterministic logic as a dispatcher that calls AI only when ambiguity is the primary task. |
| 3 | AI Automation: When Judgment, Language, or Ambiguity Matters | AI as a narrow, bounded step within larger workflows. Confidence scores must drive specific actions or they are "decorative." Gold sets (50–200 examples), sampled review, drift checks. |
| 4 | The Automation Boundary: Code vs Model vs Human | Without an intentional boundary map, responsibilities are assigned by accident. Code owns exactness, models own ambiguity, humans own accountability. |
| 5 | Human-in-the-Loop Is a Design Pattern, Not a Failure | Human review enables automation to handle consequential work safely. Good HITL is selective, explainable, and has a feedback loop. Every intervention is operational training data. |
| 6 | State, Idempotency, Retries, and Queues | While AI handles "intelligence," unglamorous backend components prevent failures, duplicates, and data corruption. Durable state, idempotency keys, and dead-letter queues are essential. |
| 7 | Observability, Auditability, and Replay | "If you cannot explain what your automation did, you do not have automation. You have a liability." Must capture actor_type, decision, reason, and policy_version for every event. |
| 8 | Agents Inside Bounded Workflows | Agents as constrained operators within defined workflows — not autonomous digital employees. Like a junior employee with strict supervision: defined job, tools, permissions, and stop conditions. |
| 9 | Failure Modes, Security, and Blast Radius | The useful question is how much damage a failure can do, how quickly you can detect it, and how cleanly you can recover. Four-stage launch strategy: Shadow → Draft → Assisted → Full Automation. |
| 10 | The Automation Architecture Worksheet | An 8-step design worksheet: workflow definition, boundary mapping, risk & reversibility, model jobs, decision gates, observability, security & ownership, and launch strategy. |

### Other Series

- **Agency Series** — Individual agency within organizations; how to operate effectively regardless of formal authority
- **Power Series** — Organizational power dynamics, influence, and navigating corporate structures
- **Technical Literacy Series** — Making technical concepts accessible to non-engineers in business roles
- **Live Player Series** — Patterns for being an effective, engaged professional ("live player" vs "dead player")
- **"Lessons From" Profiles** — Hundreds of profiles distilling lessons from industry leaders across tech, finance, and other domains

## Key Ideas

### The Three Kinds of Work

Buteau's foundational framework classifies work into three categories, each with distinct tooling and governance:

1. **Deterministic Work** — Same input always produces same output. Tools: Code, rules, schemas, APIs, tests.
2. **Probabilistic Work** — Messy inputs with ambiguity. Tools: AI/LLMs with strict contracts.
3. **Accountable Work** — High-consequence decisions requiring ownership. Tools: Human gates or strict control models.

### The Automation Boundary (Code vs Model vs Human)

Every automation workflow must explicitly map which decisions belong to which actor:

- **Code** owns exactness: required fields, permission checks, policy thresholds, idempotency, retries.
- **Models** own ambiguity: classification, extraction, sentiment — with fixed contracts and output schemas.
- **Humans** own accountability: low-confidence outputs, irreversible actions, sensitive communications.

> "If you cannot say which decisions belong to code, model, and human, you are not designing automation. You are distributing risk randomly."

### Human-in-the-Loop as Design Pattern

Buteau reframes human review not as a failure mode but as a deliberate architectural choice:

- **Bad HITL:** Every item requires approval. Reviewers lack context. No feedback loop.
- **Good HITL:** Selective (high-risk/low-confidence only). Explainable. Operationally owned with feedback loop.

> "A human approval queue is not a failure of automation. It is often the part that makes automation safe enough to use."

### Bounded Agents

Buteau's practical model for AI agents: constrained operators within defined workflows. Before giving an agent a tool, ask: "Would I give this tool to an unsupervised junior employee?" If not, it needs controls.

### Four-Stage Launch Strategy

1. **Shadow Mode** — AI recommends, humans act
2. **Draft Mode** — AI creates, humans send
3. **Assisted Mode** — AI acts on low-risk, humans review rest
4. **Full Automation** — Low-risk, reversible, well-observed work only

## Key Quotes

> "The fastest way to build bad automation is to treat it as a single category."

> "AI is expensive ambiguity machinery. Do not spend it on work that needs exactness."

> "Use AI where ambiguity is the job. Do not use AI to replace state management, permissions, retries, audit logs, policy enforcement, or ownership."

> "If you cannot explain what your automation did, you do not have automation. You have a liability."

> "If you cannot answer 'What happens if this runs twice?' you are not ready to launch. If you cannot answer 'Where is this item in the workflow?' you are not ready to scale."

> "Build automation with failure containment from the start."

> "If 95% of reviewed items are approved unchanged, raise the threshold carefully or narrow the review trigger."

## Related Concepts

- Automation architecture
- Human-in-the-loop design patterns
- Operationalizing AI confidence scores
- Bounded agent workflows
- Workflow boundary mapping (code vs model vs human)

## Links

- [antoinebuteau.com](https://www.antoinebuteau.com/) — Personal site and writing
- [X/Twitter: @anbuteau](https://x.com/anbuteau)

## Sources

- [antoinebuteau.com](https://www.antoinebuteau.com/)
- Automation Series raw articles in `wiki/raw/articles/`
