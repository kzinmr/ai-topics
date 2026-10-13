---
title: "Specification by Example"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, software-engineering, testing, documentation, business-process, verification]
sources:
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_016.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_017.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_018.html
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/02.htm
confidence: high
---

# Specification by Example

Specification by Example develops a shared understanding of desired behavior through concrete examples agreed by business participants, developers and testers. The examples are refined into readable specifications and, where valuable, connected to executable validation. Gojko Adzic's book explains these activities as a collaboration practice, rather than merely a test format.

In modernization, it supplies the intended-outcome side of [[concepts/modernization-traceability]]. [[concepts/characterization-testing]] supplies observations of the old implementation; neither artifact silently becomes the other.

## Make examples reveal uncertainty

Chapter 7 emphasizes precise, realistic and understandable examples. A simple yes/no outcome can conceal missing details: a notification may be sent, yet contain the wrong information. Ask what else happens and how a business participant could verify the result through another system. This is particularly important during legacy coexistence.

An example should identify relevant context, concrete input and observable outcome. Include exceptions and boundaries that improve understanding. Do not enumerate every combination in a workshop: a large table can hide several separate concepts. Name those concepts and specify them independently.

Actual legacy data can expose inconsistencies that invented examples omit. Anonymization and authorization remain necessary when using it.

## Refine before automating

Chapter 8 separates raw discussion examples from a durable specification. Keep the purpose, relevant conditions and domain vocabulary; remove incidental implementation steps. A specification should make sense to someone who missed the workshop.

Chapter 9 separates three responsibilities:

| Layer | Contains | Changes when |
|---|---|---|
| Business specification | Rule, relevant context, examples and expected outcomes | Intended behavior changes |
| Validation workflow | How to exercise the business operation | The application's interaction path changes |
| Technical automation | API, UI or database operations | Technical interfaces change |

The automation depends on the specification. Altering business meaning to make automation easier reverses that relationship. Copying production business logic into a fixture can also make tests agree with the same mistake.

This separation does not require a particular language or tool. Automating below the UI can reduce maintenance cost when it exercises the relevant behavior; UI-specific requirements still need UI checks. Automation cost and human judgment can justify retaining some examples as manual checks.

## Modernization application

The following is a proposed evidence record, not a format quoted from the book:

| Field | Purpose |
|---|---|
| Rule ID and owner | Identify who decides the intended behavior |
| Legacy evidence | Locate observations and recovered rules |
| Context and representative example | Make assumptions and irregular data visible |
| Expected outcome and its basis | Avoid expectations inferred from generated target code |
| Retain/change/retire/unresolved | Preserve explicit decisions about old behavior |
| Executable check or manual acceptance | Connect the decision to evidence |

Maurício Aniche's *Effective Software Testing*, Chapter 2, complements this practice by deriving test partitions and boundaries from requirements. Use [[concepts/property-based-testing]] to explore broader properties after agreeing their meaning.

## Limits

Clear examples can still reflect a wrong rule, omit a rare business case, or execute an incomplete integration. Human-readable documentation becomes trustworthy through review and continued validation. Passing examples do not establish every input's correctness or acceptable production operation.

## Related

- [[concepts/modernization-traceability]] — decisions and evidence lineage
- [[concepts/legacy-behavioral-parity]] — observed versus intended behavior
- [[concepts/property-based-testing]] — broader input exploration
- [[queries/modernization-inner-loop-study-notes]] — book sections actually inspected
