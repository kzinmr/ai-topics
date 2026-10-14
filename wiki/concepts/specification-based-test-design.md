---
title: "Specification-based Test Design"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, testing, verification, software-engineering, quality-assurance]
sources:
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/02.htm
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/03.htm
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/04.htm
---

# Specification-based Test Design

Specification-based test design derives cases from the required behavior, then uses implementation knowledge to find additional risks. It differs from [[concepts/specification-by-example]], which establishes shared business understanding: this page explains how a tester turns that agreed contract into a systematic set of cases.

Maurício Aniche's *Effective Software Testing*, Chapters 2–4, combines input/output analysis, partitions, boundaries, structural testing and explicit contracts. The explanation and example below stand alone; reading the book is optional for using this method.

## Define the contract first

A **precondition** states what must be true before an operation; a **postcondition** states what it promises afterward; an **invariant** states a condition maintained across relevant state changes. A contract's precondition does not automatically specify the public response to invalid data. Define rejection, validation and absence of effects explicitly at the boundary that receives it.

For an original fictional fee batch, the approved contract is:

- Accept integer amounts from 0 to 1,000,000 cents, inclusive.
- Calculate 2.5% rounded down to whole cents.
- Create the agreed record and one notification intent for an accepted work unit.
- Reject invalid amounts without creating either effect.

The upper limit and rejection policy are example requirements, not general financial recommendations.

## Divide the input space and inspect the borders

A **partition** is a group of inputs expected to exercise the same kind of behavior. That grouping is a testing assumption to refine, not proof that every member behaves identically. A **boundary** is a transition between such groups or between relevant outcomes.

| Concern | Candidate cases | Required expectation |
|---|---|---|
| Negative versus nonnegative | -1, 0 | Rejection without effects versus valid fee 0 |
| First full-cent fee | 39, 40, 41 | Fees 0, 1, 1 |
| Fractional rounding | 1999 | Fee 49, not nearest-rounded 50 |
| Maximum versus overflow of domain | 1,000,000; 1,000,001 | Fee 25,000 versus rejection without effects |
| Invalid representation | Null/text/fractional amount, if the interface accepts such representations | Defined parse/validation failure, not a guessed coercion |
| Failure after processing starts | Receiver commits a notice but reply is lost | Reconcile/retry under the operation contract; no duplicate accepted effect |

Include both sides of a meaningful boundary. A test of 1,000,000 alone would not catch an implementation that also accepts 1,000,001. Choose risk-relevant combinations such as a boundary amount during a retry; a Cartesian product of every incidental input can become unmanageable without improving understanding.

## Add code knowledge without letting it supply the oracle

Inspect branches, loops, conversions and state changes for behavior the original cases missed. **Coverage** records which implementation elements were executed; it does not establish that assertions are correct or sufficiently discriminating.

**Mutation testing** deliberately introduces a bounded set of small code faults and checks whether tests detect them. In this example, change the maximum-input comparison to accept one extra cent, change rounding down to nearest, or remove the no-effect guard on rejection. A surviving fault can reveal a weak test. Equivalent or irrelevant mutations need analysis; a score over a chosen mutation set is not proof of correctness.

The expected fee and valid domain must come from reviewed intent, not from executing the candidate and copying its answer. [[concepts/characterization-testing]] supplies observed old behavior; the two sources of expectation remain distinguishable.

## A repeatable design loop

1. Identify inputs, outputs, effects and the authority for each rule.
2. Select partitions and meaningful boundaries, then write explicit expected results.
3. Automate the cases at an appropriate boundary with controlled starting state.
4. Inspect the implementation and add missing risk cases without rewriting intent to match it.
5. Inject known faults into the candidate or comparator to test detection.
6. Add [[concepts/property-based-testing]] for broader reviewed properties, keeping important concrete examples.

**Check your understanding:** A suite covers every line, but never checks the fee value. Has it established the fee rule? No. It has execution evidence without the necessary outcome assertions.

## Related

- [[concepts/specification-by-example]] — collaborate on intended outcomes
- [[concepts/legacy-behavioral-parity]] — old/new comparison and approved exceptions
- [[concepts/property-based-testing]] — search for counterexamples in a defined domain
