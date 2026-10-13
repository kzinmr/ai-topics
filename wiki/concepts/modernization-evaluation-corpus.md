---
title: "Modernization Evaluation Corpus"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, evaluation, datasets, agent-evaluation, software-engineering, verification, regression, methodology]
sources:
  - https://learning.oreilly.com/library/view/ai-engineering/9781098166298/ch03.html
  - https://learning.oreilly.com/library/view/ai-engineering/9781098166298/ch04.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch03.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch05.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch08.html
---

# Modernization Evaluation Corpus

A modernization evaluation corpus is a versioned collection of representative jobs, agreed obligations, execution evidence and failure cases used to assess changes to the reusable delivery method. It applies the general [[concepts/evaluation/evaluation-flywheel]] to prompts, tools, recipes, environments and recovery procedures. Acceptance of one migrated flow remains an inner-loop decision in [[concepts/legacy-behavioral-parity]].

## Build the corpus from observed work

Shankar and Husain's Chapter 3 starts with execution traces, reads them with free-form observations, then organizes those observations into a failure taxonomy. Production traces and domain-expert hard cases provide valuable inputs; structured synthetic cases can bootstrap a system without production history.

Focus first on the earliest observed failure rather than labelling every downstream symptom as an independent cause. Continue inspection while new failure categories appear. The book's illustrative sample counts are starting heuristics, not a required statistical sample size or a guarantee of coverage.

## Case contract

The following is a proposed modernization record:

| Part | Record |
|---|---|
| Case identity and scope | Business flow, source revision and applicable rule IDs |
| Inputs and environment | Fixtures, dependencies, runtime and controlled external state |
| Independent expectation | Approved outcome, provenance, reviewer and unresolved ambiguity |
| Expected effects and constraints | Outputs, state changes, timing, authorization and architecture obligations |
| Execution evidence | Component results, tool arguments/results, effects and final reconciliation |
| Failure label | First observed failing stage, supporting evidence and uncertainty about cause |

Include cases that require no transformation or a justified abstention, unusual legacy data, loss of a remote response, repeated execution and approval waiting. Balance these with ordinary workload cases. A stress/failure set is useful for finding weaknesses, but its pass rate is not an estimate of normal production success without appropriate sampling.

## Evaluate several levels

Huyen's Chapter 4 combines component, intermediate, turn and end-to-end evaluation. Shankar and Husain's Chapter 8 decomposes tool use into selection, arguments, execution and output handling.

| Check | What it establishes | What it does not establish |
|---|---|---|
| Argument/schema validity | The request fits a structural contract | Correct recipient, flow, revision or business meaning |
| Tool execution result | A particular call's observed outcome | Completion of the intended business task |
| Recipe before/after test | Expected bounded transformation | Estate-wide semantic equivalence |
| Independent execution/reconciliation | The tested obligations and effects match | Coverage of untested inputs or acceptable rollout |
| Reviewed judgement | Agreement with specified qualitative criteria | An automatic grant of release authority |

Separate business correctness, recovery, architectural constraints, cost, latency and human effort. A single aggregate score can hide a serious regression in one slice.

## Keep the evaluator inspectable

Huyen's Chapter 3 discusses judge inconsistency, ambiguous criteria and bias. Shankar and Husain's Chapter 5 separates judge-prompt examples, development data and a final held-out test set. Development/test examples reused inside the prompt leak evaluation data.

Version the case set, rubric, expected labels, evaluator/model configuration and evaluated system. Group related cases when splitting to reduce leakage from near-duplicates. Evaluate judge agreement against independently reviewed labels, including passes and failures. Distinguish a raw judge pass rate from an estimated true success rate; uncertainty and class prevalence affect that inference.

The recipe author or coding agent must not silently redefine the expected outcome to fit a candidate change. An unresolved expectation belongs in [[concepts/modernization-traceability]], not in an automatically generated gold label.

## Related

- [[concepts/semantic-transformation-recipes]] — reusable changes to assess
- [[concepts/modernization-workflow-recovery]] — adverse execution and handoff cases
- [[queries/modernization-outer-loop-study-notes]] — book scope and proposed applications
