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
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch09.html
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

A rubric is the explicit rule for assigning a verdict or score, with examples that clarify what passes and fails. The evaluator applies that rubric; independently reviewed labels let you check whether it does so correctly.

Huyen's Chapter 3 discusses judge inconsistency, ambiguous criteria and bias. Shankar and Husain's Chapter 5 separates judge-prompt examples, development data and a final held-out test set. Development/test examples reused inside the prompt leak evaluation data.

Version the case set, rubric, expected labels, evaluator/model configuration and evaluated system. Group related cases when splitting to reduce leakage from near-duplicates. Evaluate judge agreement against independently reviewed labels, including passes and failures. Distinguish a raw judge pass rate from an estimated true success rate; uncertainty and class prevalence affect that inference.

The recipe author or coding agent must not silently redefine the expected outcome to fit a candidate change. An unresolved expectation belongs in [[concepts/modernization-traceability]], not in an automatically generated gold label.

## Worked example: preserve distinct failures

This original corpus starts with five fee-batch obligations, not a prescribed sample size:

| Case | Independent expectation | A failure that an aggregate can hide |
|---|---|---|
| Ordinary amount 1999 | Fee 49 to the intended account | Correct-looking output with fee 50 |
| Boundary amounts 39/40/41 | Fees 0/1/1 | A boundary conversion error |
| Invalid amount -1 | Rejection without record or notice intent | Rejection returned after an effect |
| Notice reply lost after acceptance | Reconciled result, no second accepted effect | Retry duplicates a notice |
| Candidate changed during approval waiting | Revalidate the decision's scope | Old approval promotes a new artifact |

For each execution, record separate results for expectation interpretation, transformation, tool arguments, observed effects and final reconciliation. If the fee rule was misread first, record that as the first observed failure; do not automatically count the resulting wrong notice as a separate root cause. A first failing stage helps diagnosis but is not proof of the underlying cause.

Keep prompt examples, judge-development cases and final held-out cases separate. A **held-out** set is reserved for evaluation after the relevant choices are fixed. Related versions of one work unit should not be scattered across these sets as apparently independent examples. Maintain a curated regression set and a separately sampled production set: passing the former protects known cases, while only appropriate sampling supports a production-rate estimate.

## Worked example: an imperfect judge inflates the pass rate

In this original hypothetical set, independent human review labels 40 cases as passing and 60 as failing. The judge makes these decisions:

| Human label | Judge says pass | Judge says fail |
|---|---:|---:|
| Pass | 36 | 4 |
| Fail | 12 | 48 |

The raw judge pass rate is `(36 + 12) / 100 = 48%`; the reviewed pass rate is 40%. **Sensitivity** is the fraction of actual passes the judge recognizes, `36/40 = 0.9`. The **false-positive rate** is the fraction of actual failures it incorrectly passes, `12/60 = 0.2`. If these rates transfer to a new population, its observed pass fraction satisfies `observed = sensitivity × true + false-positive-rate × (1 − true)`.

Rearranging gives `true = (observed − false-positive-rate) / (sensitivity − false-positive-rate)`. Here `(0.48 − 0.2)/(0.9 − 0.2) = 0.4`. This checks the arithmetic; it is not a measurement of a deployed system. If the denominator is near zero, the judge cannot support this correction reliably. Sampling uncertainty and changed cases/criteria/model behavior can invalidate the transferred rates. Report uncertainty and revalidate against fresh human labels rather than presenting this point estimate as a guarantee.

Huyen's Chapter 4 also asks whether the rubric gives better outcomes higher scores and whether improved metrics track the business goal. Shankar and Husain's Chapter 9 separates regression CI from production monitoring and describes judge drift. Pin configurations where supported, record changes and repeat alignment checks after a relevant change; a fixed model identifier or temperature alone does not prove repeatability.

**Check your understanding:** The stress set has a 100% judge pass rate. Can it authorize deployment or establish production success? No. Its sampling purpose, independent obligations, judge validity and release policy must still be considered.

## Related

- [[concepts/semantic-transformation-recipes]] — reusable changes to assess
- [[concepts/modernization-workflow-recovery]] — adverse execution and handoff cases
- [[queries/modernization-outer-loop-study-notes]] — book scope and proposed applications
