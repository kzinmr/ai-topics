---
title: "Specification by Example"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, software-engineering, testing, documentation, business-process, verification]
sources:
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_010.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_014.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_015.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_020.html
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch03.xhtml
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

## Maintain the documentation system

Chapters 2 and 11 extend individual examples into a frequently validated, accessible and consistently worded documentation system. Split specifications that mix several concepts; merge fragments that force readers to assemble one feature from many files. Update the domain language as understanding changes, while keeping technical automation details outside business explanations.

[[concepts/living-documentation]] adds an important reconciliation check from Martraire's Chapter 3: automation must actually consume the expectation in the specification. A fixed assertion in an adapter can keep passing after the displayed example changes. Continued checking therefore needs both the current example and the correct connection to execution.

For cross-project reuse, retain the decision owner, applicable context and evidence revision in [[concepts/modernization-traceability]]. A passing example for one context cannot silently authorize a different business rule elsewhere.

## Worked example: agree a fee rule before automation

This is an original fictional workshop, not a book case study. The business goal is to retire an unsupported batch runtime while retaining the approved fee and notification behavior. A request to build microservices is a suggested solution; first establish whether that architecture is necessary to achieve the goal. Chapters 5 and 6 connect this goal/scope discussion to collaborative specification.

Before the discussion, bring observed legacy cases and record open questions. Include a person who can decide the business rule, a developer who knows the relevant constraints and someone responsible for validation. They can be three people or roles shared by a smaller team.

The owner confirms this pilot's rule: valid amounts are integer cents from 0 to 1,000,000 inclusive, and the fee is 2.5% rounded down to whole cents. The approved examples are:

| Amount, cents | Intended fee, cents | Intended effect |
|---|---|---|
| 20 | 0 | One notification intent containing fee 0 |
| 40 | 1 | One notification intent containing fee 1 |
| 1999 | 49 | One notification intent containing fee 49 |
| -1 | Rejected | No fee record and no notification |

The negative-input behavior requires owner agreement too; it is not inferred from the positive examples. Credit/refund behavior is outside this pilot and remains an explicit open question.

Write the examples using the business meaning above, not clicks through a particular screen. A technical adapter can later submit an API request or launch a batch fixture. It must pass the amount from the example and check both its fee and specified effects. A fixture that always submits 40 and checks 1 is not checking the other rows, however green its report looks.

### A practical collaboration loop

1. State the goal, affected users and candidate scope; question any assumed solution.
2. Compare normal, boundary, rejected and suspicious legacy cases. Mark disagreements explicitly.
3. Agree the rule, examples, exclusions and decision owner; simplify incidental details without removing an important condition.
4. Have a participant who missed the discussion explain the examples back. Ambiguity discovered here is cheaper to resolve than ambiguous automation.
5. Automate the reviewed examples and preserve their identity when technical interaction details change.

Chapter 8 distinguishes a specification of behavior from an interaction script. If the workflow itself is the obligation, its ordering belongs in the specification; if login clicks merely reach the fee function, keep them in the adapter.

**Check your understanding:** Can a developer change 49 to 50 to improve rounding? Only after a separately recorded business decision changes the rule and acceptance examples. It is not an incidental refactor.

## Limits

Clear examples can still reflect a wrong rule, omit a rare business case, or execute an incomplete integration. Human-readable documentation becomes trustworthy through review and continued validation. Passing examples do not establish every input's correctness or acceptable production operation.

## Related

- [[concepts/modernization-traceability]] — decisions and evidence lineage
- [[concepts/legacy-behavioral-parity]] — observed versus intended behavior
- [[concepts/property-based-testing]] — broader input exploration
- [[concepts/specification-based-test-design]] — derive partitions, boundaries and explicit contracts
- [[queries/modernization-inner-loop-study-notes]] — book sections actually inspected
