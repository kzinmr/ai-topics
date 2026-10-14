---
title: "Property-Based Testing"
type: concept
aliases:
  - property-based-testing
created: 2026-04-25
updated: 2026-10-14
tags:
  - concept
  - testing
  - property-based-testing
  - verification
  - software-engineering
sources:
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/02.htm
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/04.htm
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/05.htm
  - https://jqwik.net/docs/current/user-guide.html
confidence: high

---

# Property-Based Testing

## Overview

Property-based testing expresses a rule that should hold across a defined input domain, then generates inputs to search for counterexamples. The developer supplies both the property and its domain; a framework cannot decide the correct business rule.

In *Effective Software Testing*, Chapter 5, Maurício Aniche combines property-based tests with example-based specification and structural tests. The technique extends those checks rather than making carefully chosen examples obsolete.

## Design the property and generator together

An agreed property can concern an invariant, a relation between transformations, or a postcondition. For example, round-tripping a supported encoding should preserve the fields that its contract defines. Such relations require explicit preconditions: a lossy transformation need not satisfy a lossless round-trip rule.

Generators determine what is explored. Aniche's section 5.6 warns about impossible/expensive constraints, incorrectly expressed boundaries and distributions that underexercise important cases. Generate valid and invalid populations deliberately; verify that filtering does not discard almost everything.

The jqwik guide documents shrinking and replay of falsified properties. Retain the seed and failing case with the implementation, generator, framework and configuration versions. Shrinking helps expose a simpler counterexample; it does not guarantee a globally minimal example or reproduce a failure after the generator changes.

## Modernization application

- Start with domain-approved examples and [[concepts/specification-by-example]].
- Derive properties from the retained or deliberately changed contract.
- Exercise numeric/date boundaries and representative state transitions.
- Supplement differential checks with independent constraints where available.
- Preserve a discovered counterexample as a regression case.

These are proposed applications. Two implementations can agree on the same wrong result, and a property copied from the implementation can share its mistake. [[concepts/legacy-behavioral-parity]] therefore separates observation, comparison and business acceptance.

Passing finite generated runs provides evidence within the tested domain. It is not a proof over every input, a substitute for integration tests, or permission to alter expectations to fit new code.

## Worked example: properties need an approved domain

This original example uses a reviewed fee rule: valid inputs are integer cents from 0 to 1,000,000; the fee is 2.5% rounded down to whole cents. A **generator** produces values or value sequences in the domain. A **property** states the obligation checked for each generated input.

| Proposed property | Required scope | Why it matters |
|---|---|---|
| `0 <= fee(a) <= a` | Valid nonnegative amounts | Reject impossible negative/excessive fees |
| `fee(a) <= fee(b)` when `a <= b` | Same applicable rule/configuration | Increasing the amount must not reduce the fee |
| Negative input is rejected without records/notices | Rejected-input population | Rejection must prevent effects, not just return an error |

Draw ordinary values across the range and deliberately include 0, the maximum, values around fee boundaries such as 39/40/41, and rejected negative values. Generating only multiples of 40 hides fractional-rounding differences. Test valid and rejected populations separately instead of filtering away almost all generated values.

A plausible property, `fee(a + b) == fee(a) + fee(b)`, is **wrong for this rule**: `fee(20) + fee(20) = 0`, while `fee(40) = 1`. Rounding each fee destroys that additivity. A counterexample here exposes a bad proposed property, not necessarily bad application code.

The first two properties are also too weak to characterize the fee rule: a candidate returning zero for every valid input satisfies both. Keep independently approved examples such as `1999 -> 49` and `40 -> 1`, along with more specific reviewed obligations. This is why property tests and examples complement each other.

When a generated case fails, preserve the actual input/state sequence and execution versions. **Shrinking** searches for a simpler failing case, helping diagnosis; a smaller case is not guaranteed to be the unique minimum. For stateful operations, include operation order, starting state and effects, not only final amounts.

**Check your understanding:** Must an input found by a framework be a real defect? First verify that the input satisfies the property's preconditions and that the property reflects the approved rule. Then investigate the implementation and test machinery.

## Related Pages

- [[concepts/specification-by-example]] — establish the rule being tested
- [[concepts/legacy-behavioral-parity]] — compare old/new behavior and state
- [[concepts/characterization-testing]] — preserve concrete observed cases
- [[concepts/specification-based-test-design]] — derive independent expectations and boundary cases
- [[queries/modernization-inner-loop-study-notes]] — inspected book sections
