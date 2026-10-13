---
title: "Living Documentation"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, documentation, knowledge-management, software-engineering, verification, business-process]
sources:
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch01.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch02.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch03.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch04.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch05.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch12.xhtml
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_020.html
---

# Living Documentation

Living documentation is knowledge kept useful as a system changes, through an explicit relationship to authoritative artifacts, continued checking and shared maintenance. Cyrille Martraire extends the executable-specification practice in [[concepts/specification-by-example]] to rationale, architecture, domain vocabulary and other project knowledge.

Producing documents automatically is only one mechanism. A generated document can repeat an incorrect inference; a recent timestamp can conceal an obsolete decision. The relevant question is how a reader can establish the knowledge's authority and continuing applicability.

## Choose the accuracy mechanism

Martraire's Chapters 1 and 3 prefer using existing authoritative knowledge and publishing views from it. When redundancy is unavoidable, a reconciliation mechanism detects disagreement.

| Situation | Mechanism | Remaining responsibility |
|---|---|---|
| A fact is directly represented in code or configuration | Publish a versioned view from that source | Identify what the artifact actually establishes |
| Intended behavior is expressed in business examples and implementation | Execute the examples against the system | Decide which side should change after disagreement |
| A historical decision explains why a design exists | Keep context, alternatives and consequences with the decision | Reconsider it when assumptions change |
| Facts are dispersed across artifacts | Consolidate with inspectable source references | Expose omissions and conflicting meanings |

Chapter 3 gives a particularly useful failure case: a scenario can change while its adapter still checks a hardcoded expected value. A passing run then fails to reconcile the actual specification. Extract expectations from the specification and verify the adapter's relationship to it.

Code is authority for implemented behavior, not automatically for current business intent. Keep those authorities distinct in [[concepts/modernization-traceability]].

## Preserve why and when

Chapters 4 and 12 treat a decision's context and rejected alternatives as knowledge that the resulting code often cannot express. A versioned decision log should retain earlier decisions and add an explicitly superseding entry when the decision changes.

For modernization reuse, the following record is a proposed application of those principles:

| Field | Purpose |
|---|---|
| Rule/decision identifier and evidence location | Make the statement inspectable |
| Authority and accountable owner | Identify who can resolve disagreement |
| Applicable business context and assumptions | Prevent silent transfer to another flow |
| Approved examples and check revision | Reconcile intent with execution |
| Review trigger and superseding decision | Expose expiry and changed meaning |

A failed check or changed assumption should mark a decision for review. Rewriting the historical rationale to match today's code hides the reason the earlier choice was made.

## Curate for continued use

Adzic's Chapter 11 adds organization, consistent domain language and accessibility. Merge fragmented descriptions of one feature; split specifications that conceal several concepts; keep technical fixture operations outside business explanations. Martraire's Chapter 12 adds an architecture reality check: compare implemented structure with intended design, alongside explicit quality attributes.

Measure whether maintainers and domain participants can find, understand and update the relevant knowledge. The number of generated pages does not measure its usefulness. [[concepts/architectural-fitness-functions]] can check selected design characteristics, but does not settle a business disagreement.

## Worked example: keep one fee decision understandable

In this original fictional example, decision `DEC-03` approves integer-cent amounts from 0 to 1,000,000 and a fee of 2.5% rounded down. Example `EX-04` says that 1999 cents produces a 49-cent fee. The record also identifies the decision owner, applicable pilot, rationale and review trigger. A readable rule page and an executable example refer to this versioned record.

1. Publish the rule, its example and the reason for rounding down where maintainers and domain participants can find them.
2. Make the test adapter read the example's input and expectation, invoke the implementation and compare the actual result with 49.
3. Deliberately change the expectation to 50 in a temporary fixture. The unchanged implementation must now fail the check. If it remains green, the adapter may have ignored the specification.
4. Restore the fixture. If the owner later approves rounding to nearest, add a superseding decision with its scope and consequences; update examples and implementation together. Preserve the earlier decision as history.

The temporary fixture change tests reconciliation; it does not authorize a new business rule. Copying an expected value into an unrelated test and maintaining two copies manually creates a synchronization obligation. Generating both implementation and expected answer from the same mistaken rule can also hide a defect: shared storage does not replace independent review of intent.

Chapter 2's discussion of behavior-driven development puts collaboration before automation. Chapter 5's curation discussion adds a reader's route through relevant knowledge. For this case, a maintainer needs the rule and failing check; a decision owner needs the rationale and alternatives; an operator needs the pending-work/recovery policy. Link these views instead of making every reader inspect every artifact. Curation means selecting, organizing and explaining knowledge for a reader's purpose.

**Check your understanding:** The page was regenerated today, but its adapter always compares with a hardcoded 49 after the published example changes to 50. Is the documentation reconciled? No. Fresh publication and a green test have concealed disagreement between the two versions.

## Related

- [[concepts/specification-by-example]] — agreed examples and executable validation
- [[concepts/modernization-traceability]] — authority, dispositions and evidence lineage
- [[queries/modernization-outer-loop-study-notes]] — actual book-reading scope
