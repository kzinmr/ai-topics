---
title: "Modernization — Account-free Concept Study Guide"
created: 2026-10-14
updated: 2026-10-14
type: query
tags: [query, education, documentation, software-engineering, testing, verification, workflow]
sources:
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch02.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_014.html
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch04.html
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/02.htm
  - https://learning.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch03.html
  - https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch05.xhtml
  - https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0048.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch05.xhtml
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_4.xhtml
  - https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/ch04.html
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch03.html
  - https://learning.oreilly.com/library/view/ai-engineering/9781098166298/ch04.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch05.html
  - raw/papers/2020-04-08_google_building-secure-reliable/ch14.md
---

# Modernization — Account-free Concept Study Guide

Start here to understand and use the selected inner-loop and outer-loop concepts without an O'Reilly account. All learning links below open repository pages. Source-book links in their metadata are optional deeper reading; no exercise requires subscription access. This is an original modernization curriculum grounded in the **14 priority works**, not a replacement for their full contents. Exact source-reading coverage is in [the continuation record](modernization-reading-continuation.md).

An **inner loop** delivers an accepted change for one business flow. An **outer loop** improves the reusable way to discover, transform, verify and release such changes. A business flow is an outcome-oriented sequence such as calculating a fee, recording it and notifying the correct account. An **oracle** is the independently justified basis for an expected result; an old program, generated test or model answer does not automatically supply business authority.

## Learn in the original guide order

Read each page's definition, example, procedure and limits, then answer its understanding question before checking the printed answer. The book column explains why the source matters; the learning task can be completed from the linked repository pages.

| Step / priority work | Account-free reading | Ability to demonstrate |
|---|---|---|
| I-1 — Working Effectively with Legacy Code | [Characterization](../concepts/characterization-testing.md), [seams](../concepts/legacy-code-seams.md) | Record old behavior, select a substitute and state what the recorder cannot prove |
| I-2 — Specification by Example | [Shared examples](../concepts/specification-by-example.md), [traceability](../concepts/modernization-traceability.md) | Separate observation from approved intent and identify who decides a difference |
| I-3 — Monolith to Microservices | [Incremental migration](../concepts/incremental-legacy-migration.md) | Choose a replacement boundary, a single writer and a state-aware recovery plan |
| I-4 — Effective Software Testing | [Test design](../concepts/specification-based-test-design.md), [properties](../concepts/property-based-testing.md), [parity](../concepts/legacy-behavioral-parity.md) | Select boundary cases, reject a false property and detect a material old/new difference |
| I-5 — Building Evolutionary Architectures, 2nd Edition | [Fitness functions](../concepts/architectural-fitness-functions.md) | Turn a required design characteristic into a falsifiable assessment |
| I-6a — Continuous Delivery | [Artifact gates](../concepts/artifact-provenance-gates.md), [canary acceptance](../concepts/canary-release-acceptance.md) | Promote the checked artifact and preserve post-cutover writes during recovery |
| I-6b — Release It!, 2nd Edition | [Resilience tests](../concepts/resilience-acceptance-testing.md) | Distinguish timeout, breaker and bulkhead; test degraded operation and recovery |
| O-1a — Living Documentation | [Living documentation](../concepts/living-documentation.md) | Explain authority, verify reconciliation and curate a useful reader route |
| O-1b — Specification by Example, shared with I-2 | Revisit [shared examples](../concepts/specification-by-example.md) and their maintenance | Keep examples readable and applicable as implementation details change |
| O-2a — Automated Code Refactoring and Modernization with OpenRewrite | [Semantic recipes](../concepts/semantic-transformation-recipes.md), matching/composition example | Distinguish same-spelled APIs and require evidence for changed and unchanged cases |
| O-2b — AI for Mass-Scale Code Refactoring and Analysis | [Semantic recipes](../concepts/semantic-transformation-recipes.md), AI contribution/acceptance sections | Distinguish discovery, proposed edits and reusable assets from accepted outcomes |
| O-3 — Practical Process Automation | [Workflow recovery](../concepts/modernization-workflow-recovery.md) | Reconcile a lost reply, preserve an operation key and scope a resumed approval |
| O-4a — AI Engineering | [Evaluation corpus](../concepts/modernization-evaluation-corpus.md), criteria and levels | Connect observable checks to business obligations and inspect the evaluator |
| O-4b — Evals for AI Engineers | [Evaluation corpus](../concepts/modernization-evaluation-corpus.md), judge matrix and data splits | Calculate a judge's error rates and explain why regression results are not production rates |
| O-5 — Building Secure and Reliable Systems | [Artifact gates](../concepts/artifact-provenance-gates.md) | Separate identity, authenticated origin, functional evidence and action authority |

This is seven inner-loop works plus eight outer-loop entries with one shared work: **14 unique titles**. Cross-links such as artifact identity are deliberate dependencies; revisit them when the outer loop adds reusable policy and evidence management. The guides' larger 42/20 selections and conditional specialties are preserved.

## Put the concepts together

Use [the fictional fee-batch exercise](modernization-batch-example.md) after the inner path, then repeat its later steps after the outer path. Its approved rule is integer cents from 0 to 1,000,000, with a 2.5% fee rounded down. The values and identifiers are invented for learning. No bank/customer data or production result is implied.

The essential decisions are:

1. Observe what the old system did, then identify whether the owner intends to retain it.
2. Define accepted inputs, outputs, state/effects and unresolved questions before changing code.
3. Verify a candidate at a controlled boundary; compare material outcomes and test the checks with known faults.
4. Move responsibility incrementally with explicit state ownership and preservation of new writes.
5. Keep rules, examples, recipes and recovery evidence versioned and applicable to their context.
6. Evaluate the reusable method with distinct correctness/recovery/architecture results and inspect judge validity.
7. Authorize only the identified artifact and scoped action for which applicable evidence exists.

## Check comprehension without the books

Try these before opening the answers in the linked pages:

- Both implementations return fee 49, but the candidate records account B instead of A. Explain why output equality is insufficient. [Answer and comparator](../concepts/legacy-behavioral-parity.md).
- A notification timed out, and a retry succeeds. State what evidence would establish whether one or two notices were accepted. [Answer and timeline](../concepts/modernization-workflow-recovery.md).
- A generated document and test both look current, but the test ignores the example's expectation. Design a check that exposes it. [Answer and fixture change](../concepts/living-documentation.md).
- A judge says 48 of 100 cases passed; human review says 40. Calculate sensitivity/false-positive rate from the provided matrix and state the limits of transferring them. [Answer and arithmetic](../concepts/modernization-evaluation-corpus.md).
- Release label R is unchanged but the artifact digest changed. Explain why the earlier test/approval cannot silently transfer. [Answer and gate table](../concepts/artifact-provenance-gates.md).

Basic programming, tests and data-processing concepts are assumed. Specialized tool syntax is optional: the examples explain their mechanism, and illustrative recipe logic is explicitly not a ready-to-run OpenRewrite implementation. Project-specific thresholds, schemas, privileges and business decisions need their own evidence.

## Public originals and audit trail

Google's complete licensed original is also available without an account: [source archive/license](../raw/papers/2020-04-08_google_building-secure-reliable/) and [publisher reading site](https://google.github.io/building-secure-and-reliable-systems/raw/toc.html). The [inner source register](modernization-inner-loop-sources.md) and [outer source register](modernization-outer-loop-sources.md) distinguish complete public text, samples, companion resources and unresolved availability. Do not treat a sample or subscription page as a complete public book.

[[concepts/legacy-modernization-moc]] retains the wider map. [[queries/modernization-independent-reading-review]] records the account-free review criteria and remaining limits.
