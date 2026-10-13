---
title: "Characterization Testing"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, testing, regression, verification, software-engineering]
sources:
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch13.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_016.html
confidence: high
---

# Characterization Testing

A characterization test records what an existing implementation does under a particular set of conditions. It protects those observations against unintended change. It supplies an observation baseline for [[concepts/legacy-behavioral-parity]], while [[concepts/specification-by-example]] establishes what the business wants the replacement to do.

## Observe before prescribing

In *Working Effectively with Legacy Code*, Chapter 13, Michael Feathers obtains expectations by exercising the legacy code and inspecting its results. A deliberately failing assertion can expose the actual result; the assertion is then changed to capture that observation. This is appropriate while establishing a baseline. It does not justify updating an accepted expectation to match a newly changed implementation.

Unexpected behavior remains evidence. Mark a suspected defect and investigate whether consumers depend on it; decide its disposition through [[concepts/modernization-traceability]]. The observation and the approved replacement rule can both be retained.

| Record | Question answered | Authority |
|---|---|---|
| Characterization case | What did this legacy revision do? | Recorded execution |
| Acceptance example | What should the target do? | Approved domain rule |
| Differential result | Did the implementations agree in this case? | Executions plus comparison rules |

Agreement with a defective baseline does not establish business correctness. A disagreement is a finding to explain, rather than automatic evidence that either implementation is right.

## Select cases for the intended change

Feathers combines exploration with targeted testing: inspect the code, understand its behavior, then exercise the paths and conversions affected by the proposed extraction or move. A test can run through a conversion without revealing truncation if its input happens to produce an integral value. Check both the presence of a behavior and its connection to the surrounding flow.

*Specification by Example*, Chapter 7, provides a complementary warning: fabricated data can miss irregularities in real legacy records even when all example tests pass. Use authorized, anonymized representative records where their structure matters.

The following capture checklist is a modernization application of those principles:

- Identify the revision, runtime, configuration, reference data and input fixture.
- Record return values, state changes and important external effects.
- Include affected branches, boundaries, conversions and failure paths.
- Define normalization explicitly; retain evidence before normalization.
- Introduce [[concepts/legacy-code-seams]] when dependencies prevent safe observation.
- Preserve suspicious cases alongside their owner decisions and approved exceptions.

## Limits

A snapshot covers the cases observed. It is not exhaustive equivalence, a specification of intent, or evidence that a substituted collaborator behaves like the real dependency. Broad output snapshots can also become brittle when incidental formatting is included. Choose the observable contract deliberately and supplement it with integration checks and [[concepts/property-based-testing]].

## Related

- [[concepts/legacy-code-seams]] — isolate dependencies and sense effects
- [[concepts/specification-by-example]] — make intended outcomes explicit
- [[concepts/legacy-behavioral-parity]] — compare state, contracts and approved differences
- [[queries/modernization-inner-loop-study-notes]] — reading scope and applications
