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

## Related Pages

- [[concepts/specification-by-example]] — establish the rule being tested
- [[concepts/legacy-behavioral-parity]] — compare old/new behavior and state
- [[concepts/characterization-testing]] — preserve concrete observed cases
- [[queries/modernization-inner-loop-study-notes]] — inspected book sections
