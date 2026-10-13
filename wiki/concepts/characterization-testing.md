---
title: "Characterization Testing"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, testing, regression, verification, software-engineering]
sources:
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch02.html
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch11.html
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

## Worked example: discover a rounding boundary

This is an original, fictional example. A batch calculates a fee in integer cents. Its current code multiplies the amount by 25 and divides by 1,000, discarding the fractional part. For nonnegative amounts this means rounding down. The old program is the object of observation; this formula is not yet an approved target rule.

| Input amount, cents | Observed fee, cents | What the case reveals |
|---|---|---|
| 0 | 0 | Zero input |
| 20 | 0 | A fractional fee is discarded |
| 40 | 1 | The first full-cent boundary |
| 1999 | 49 | A result close to the next cent is still rounded down |

A candidate that rounds to the nearest cent returns 50 for 1,999. That is a real behavioral difference, even if the candidate looks more reasonable. Record it as unresolved until the domain owner decides whether to retain the old rounding or approve a change. Keep the old observation after that decision; put an approved new expectation in a separately identified acceptance case.

### Repeatable capture procedure

1. Freeze the old revision, amount fixtures, rounding-related configuration and initial database state.
2. Run each case safely and capture the fee, records changed and notification intent. An output-only assertion misses a second notification.
3. Save the observations before changing the calculation. Remove only agreed incidental fields, such as an execution timestamp; retain the original record too.
4. Change one implementation boundary, rerun the same cases and investigate differences. Do not turn 49 into 50 in the baseline simply to make the candidate pass.
5. Exercise the real notification integration separately: a recorder establishes an attempted call, not successful delivery.

Feathers' Chapter 2 places test preparation before the substantive change; Chapter 11 follows the effects of a change outward to observable results. For this example, inspect both the fee calculation and the batch code that persists and sends it. A passing calculation test does not cover a later conversion that changes the fee.

**Check your understanding:** If the test observes 49 but the business wants 50, which record changes? Add the approved target acceptance expectation and its decision reference; preserve the old observation as historical evidence.

## Limits

A snapshot covers the cases observed. It is not exhaustive equivalence, a specification of intent, or evidence that a substituted collaborator behaves like the real dependency. Broad output snapshots can also become brittle when incidental formatting is included. Choose the observable contract deliberately and supplement it with integration checks and [[concepts/property-based-testing]].

## Related

- [[concepts/legacy-code-seams]] — isolate dependencies and sense effects
- [[concepts/specification-by-example]] — make intended outcomes explicit
- [[concepts/legacy-behavioral-parity]] — compare state, contracts and approved differences
- [[queries/modernization-inner-loop-study-notes]] — reading scope and applications
