---
title: "Modernization Outer-loop — Focused Reading and Design Notes"
created: 2026-10-14
updated: 2026-10-14
type: query
tags: [query, software-engineering, knowledge-management, workflow, evaluation, verification, audit]
sources:
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch03.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch04.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch12.xhtml
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_010.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_020.html
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_6.xhtml
  - https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/ch02.html
  - https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/ch03.html
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch09.html
  - https://learning.oreilly.com/library/view/ai-engineering/9781098166298/ch04.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch03.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch05.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch08.html
  - raw/papers/2020-04-08_google_building-secure-reliable/ch05.md
  - raw/papers/2020-04-08_google_building-secure-reliable/ch14.md
  - raw/papers/2020-04-08_google_building-secure-reliable/ch15.md
  - raw/papers/2025_google_dora-gen-ai/impact-of-generative-ai.md
---

# Modernization Outer-loop — Focused Reading and Design Notes

First focused pass through the eight works in the five-stage priority path of [[queries/modernization-outer-loop-reading]], completed on 2026-10-14. Selection, order and conditional criteria are retained. These are original notes grounded in actual book sections, not conclusions inferred only from catalog descriptions.

This is **not** full-book reading, completion of every guide-designated chapter, or reading of all 20 works. O'Reilly was used for commercial-book reading, not for copying chapters into raw. Google's book and the supplementary documentation/report are inspected from licensed immutable snapshots. [[queries/modernization-outer-loop-sources]] records acquisition and licensing separately.

## Reading coverage, in guide order

**Continuation, 2026-10-14:** The following table preserves the first-pass coverage snapshot, including what was then unread. [[queries/modernization-reading-continuation]] records subsequent reading of living curation, recipe composition/cursors, AI use cases, workflow versions/boundaries, evaluator calibration and CI, and deeper Google test/provenance sections. [[queries/modernization-independent-study-guide]] supplies standalone learning for both loops.

| Stage / work | Sections actually inspected | Coverage boundary |
|---|---|---|
| 1 — Living Documentation | Ch. 1 core principles and accuracy mechanisms; Ch. 3 authoritative sources, publishing and reconciliation; Ch. 4 recording rationale; Ch. 12 quality attributes, decision logs and architectural reality check | Selected sections of Ch. 1/3/4/12; Ch. 2 and other material in those chapters remain unread |
| 1 — Specification by Example | Ch. 2 frequent validation/evolving documentation; Ch. 11 readability, consistency and organization | New outer-loop reading; Ch. 7–9 mechanics draw on the documented inner-loop pass; Ch. 3/10 not newly read |
| 2 — Automated Code Refactoring and Modernization with OpenRewrite | Ch. 2 architecture/LST representation; Ch. 5 recipe types and composition/sharing discussion; Ch. 6 testing and configuration validation | Focused Ch. 2/5/6 sections; Ch. 4 and detailed cursor implementations remain for recipe implementers; image-only comparison table not used as evidence |
| 2 — AI for Mass-Scale Code Refactoring and Analysis | Ch. 2 LST retrieval/context and recipe-guided AI; Ch. 3 classifier/embedding/generation roles and CPU deployment discussion | Selected Ch. 2/3 sections; Ch. 1 full text and worked Ch. 4 use cases not reviewed; historical vendor measurements are not independently reproduced |
| 3 — Practical Process Automation | Ch. 4 human-task rationale; Ch. 9 idempotency, Saga/compensation, outbox; Ch. 11 workflow audit data and distributed-tracing limits | Selected Ch. 4/9/11 sections; Ch. 3/7/8/10 and detailed task assignment remain available for implementation-specific depth |
| 4 — AI Engineering | Ch. 3 functional correctness and AI-judge limitations; Ch. 4 evaluation pipeline, component/task checks, methods and annotated data/slices | Task-specific selection; other chapters and the full judge/bias discussion not completed |
| 4 — Evals for AI Engineers | Ch. 3 trace dataset and open coding; Ch. 5 failure metrics and judge train/dev/test splits; Ch. 8 tool-call stages and traceability | Task-specific selection; calibration formulas, CI implementation and later chapters not fully reviewed |
| 5 — Building Secure and Reliable Systems | Ch. 5 narrow APIs, authorization, multi-party authorization and audit; Ch. 14 authenticated binary provenance, verifiable builders, enforcement and post-deployment verification; Ch. 15 useful immutable logging/privacy | Focused sections of existing full-book raw; no full-book completion claimed |

Supplementary reading: OpenRewrite LST overview, Java LST safety limitation, recipe forms and selected testing sections; Temporal retry permanent/transient distinction and Saga overview/registration example; DORA report v2025.2 PDF pages 38–42 on measurement and page 55 on its license. The remaining saved source documents/pages are acquisition coverage, not an assertion that every line was read.

Reader locations are explicit in each concept page's sources. Loading placeholders and table-of-contents text were excluded from substantive findings; the actual chapter heading and paragraph content were confirmed. The DORA page-40 measurement table was visually checked; text extraction alone does not preserve every layout relationship.

## 1. Reuse a decision with its authority and applicability

[[concepts/living-documentation]] connects existing authoritative knowledge to versioned views and reconciliation. The most useful concrete failure is a business example that changes while a hardcoded adapter assertion remains unchanged: the test can pass without checking the current specification.

Keep code-observed behavior separate from intended business rules. Retain why a decision was made and what alternatives were rejected. When context changes, add a superseding decision instead of retrospectively rewriting history. Curate the resulting examples in consistent domain language so maintainers and SME reviewers can find them.

**Proposed platform asset:** rule/decision ID, evidence revision, owner, applicability, assumptions, approved examples, check revision and review trigger. A source link alone does not establish that a decision is still valid for a different application.

## 2. Make transformations inspectable assets

[[concepts/semantic-transformation-recipes]] explains LSTs, recipe forms and controlled AI assistance. Type attribution and formatting retention improve targeting and diff review; the official LST documentation explicitly permits transformations that do not compile. Configuration validation is also a different check from functional acceptance.

**Proposed platform asset:** versioned recipe plus ordered configuration, supported dependency/runtime conditions, negative cases, known exclusions, independent post-change checks and an owner. AI can support candidate discovery and recipe drafting; any LLM call inside a recipe preserves a probabilistic part of the workflow.

The 2024 AI report describes a vendor architecture. Its accuracy claims, model counts and CPU economics are not transferred into current production guarantees. Validate the actual selected task, dependencies, license and execution constraints before adopting a recipe.

## 3. Design recovery around effects and responsibility

[[concepts/modernization-workflow-recovery]] distinguishes retry, unknown remote outcome, failed validation, unresolved business intent, approval waiting and compensation. Ruecker's Chapter 9 makes two practical limits explicit: a receiver must support the idempotency contract, and compensation need not restore the exact prior world.

**Proposed platform asset:** stable job/operation identity, durable state and decision evidence, bounded retries, receiver deduplication/reconciliation, recovery procedure and escalation owner. Persist an approval against the reviewed candidate/evidence version. Separate sampled technical traces from authoritative records of significant business transitions.

The earlier broad statements about guaranteed completion and replay without duplicate effects in [[concepts/durable-execution]] are retained with a dated scope correction. Persistent workflow state is useful; it does not alone guarantee successful completion or exactly-once external effects.

## 4. Evaluate the method across cases, not only the current patch

[[concepts/modernization-evaluation-corpus]] takes completed/failed inner-loop work as input. Build failure categories from trace inspection, then check components and the end-to-end obligation. Tool selection, arguments, execution and result interpretation can fail separately. Include approved no-change/abstention cases and recovery/handoff cases.

**Proposed platform asset:** versioned case, fixtures/environment, independent expectation, effect/constraint checks, run evidence and first observed failure label. Keep ordinary-workload and targeted failure slices interpretable instead of reporting an unexplained aggregate score.

Judge prompts need separate construction, development and held-out test data. A raw judge pass rate is not automatically the true business success rate. A second agent or a fluent final explanation cannot replace the independent oracle and accountable acceptance decision.

## 5. Bind approval and deployment to the checked artifact

[[concepts/artifact-provenance-gates]] joins authenticated build provenance, artifact identity, check evidence and deployment decisions. Google's Chapter 14 makes the distinction between source assurance and binary assurance concrete. Chapter 5 contributes granular action authority; Chapter 15 contributes investigation records with integrity and privacy constraints.

**Proposed platform asset:** source/input identifiers, builder identity, artifact digest, test/reconciliation run IDs, policy revision, approver and deployment/exception record. A substituted artifact requires applicable checks and a new decision. Even authentic provenance can describe defective code; behavioral acceptance remains necessary.

## Measure reuse and maintenance as well as adoption

DORA v2025.2, pages 38–42, recommends baselines, multiple levels of measurement and acting on the feedback. Its page 41 explicitly separates coding-assistant usage signals from impact. Pages 39–40 connect capabilities, delivery/reliability performance and organizational outcomes. These are measurement guidance, not a causal estimate of this repository's modernization savings.

For O-06, proposed local measures are repeated SME questions, accepted reuse under unchanged assumptions, time waiting for decisions, first-pass acceptance, rework, recovery effort and maintenance cost per accepted flow. Record workload and context alongside improvements. No empirical efficiency result is claimed here; Team Topologies and Accelerate remain purpose-specific reading references, not read-book evidence in this pass.

## Further depth under the existing criteria

The remaining guide sections stay conditional on actual design questions: compiler designers use Language Implementation Patterns; integration designers consult EIP; shared-environment owners use IaC 3rd; responsibility/investment decisions use Team Topologies, Accelerate and Kill It with Fire. Security Engineering's public author PDF is available for reading, while its redistribution permission remains unresolved.

Deepen the outstanding priority-chapter sections when implementing their mechanism, rather than treating this focused report as a complete book review. No target-system workflow, recipe or gate was implemented or production-tested in this repository.

## Related

- [[queries/modernization-outer-loop-reading]] — selection criteria and remaining chapter purposes
- [[queries/modernization-outer-loop-sources]] — public scope, original files, licenses and checksums
- [[concepts/legacy-modernization-moc]] — five new concepts and shared foundations
- [[queries/modernization-inner-loop-study-notes]] — project-level evidence reused by the outer loop
