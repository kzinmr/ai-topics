---
title: "Semantic Transformation Recipes"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, software-engineering, compiler, developer-tooling, code-quality, testing, verification]
sources:
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_2.xhtml
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_5.xhtml
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_6.xhtml
  - https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/ch02.html
  - raw/articles/2026-10-14_unknown_openrewrite-docs/lst-examples.md
  - raw/articles/2026-10-14_unknown_openrewrite-docs/recipe-testing.md
  - https://docs.openrewrite.org/licensing/openrewrite-licensing
---

# Semantic Transformation Recipes

A semantic transformation recipe is a reusable operation over a structured representation of code, with explicit matching and change logic. OpenRewrite's semantic recipes use lossless semantic trees (LSTs), visitors and composition. [[concepts/living-documentation]] and [[concepts/modernization-traceability]] supply the intended rule and its evidence; the recipe supplies a repeatable implementation mechanism.

## What the representation contributes

Schulte's Chapter 2 explains that LSTs retain syntax, type attribution and formatting information. Type-aware matching can distinguish identically named methods from different libraries. Preserving formatting and comments helps constrain unrelated diff noise. Visitors traverse and transform nodes; cursors provide parent/context information needed for local decisions.

This representation does not prove that a transformation is safe. The official Java LST examples explicitly allow syntactically valid transformations that do not compile, such as using a variable before its definition. Complete dependencies, appropriate attribution and language semantics remain relevant; business equivalence needs additional evidence.

Not every OpenRewrite operation uses an LST. Chapter 5's shared H2 schema-fix example uses text replacement and is explicitly conditional on the database version. Do not transfer semantic-matching assumptions to text recipes or unsupported file formats.

## Choose the smallest adequate recipe

| Form | Useful for | Review focus |
|---|---|---|
| Declarative composition | Combining existing operations | Order, options, dependencies and interactions |
| Refaster template | Bounded before/after expressions or statements | Type-aware matching and semantic preconditions |
| Imperative recipe | Changes needing richer traversal or context | Visitor behavior, cursor state, attribution and unintended matches |

Chapters 5 and 6 explain these forms and custom-recipe development. Configuration validation checks required options and invalid combinations before execution; it is separate from validating the generated program or accepting its business behavior.

## Make reuse reviewable

The following asset contract is a modernization proposal, not an OpenRewrite-mandated schema:

- Pin recipe artifact/version, configuration and composition order.
- Identify supported source/runtime/dependency conditions and excluded cases.
- Keep reviewed before/after examples plus cases that must remain unchanged.
- Record known limitations, the owner and the checks required after application.
- Bind each execution to a source revision, environment and produced diff/artifact.

The book's Chapter 6 and official testing guide establish recipe tests for expected changes and absence of unwanted changes. Extend that with repeat-application/convergence tests where relevant, compilation, independent behavior checks and [[concepts/architectural-fitness-functions]]. A correct small fixture is evidence about that case, not a proof covering an entire estate.

## AI's contribution and boundary

Gehring, Kundzich and Johnson's Chapter 2 describes using recipes to retrieve targeted LST information, invoke AI for bounded work and insert results into the tree. Their Chapter 3 distinguishes classification, embedding and generation tasks. These are a vendor-authored design perspective, not an independent guarantee of accuracy or savings.

Use AI to discover candidates, explain failures and draft recipes; review and test the resulting transformation asset. A deterministic traversal containing an LLM call still has a probabilistic component. A recipe-generated diff still needs the acceptance contract in [[concepts/legacy-behavioral-parity]].

Documentation and individual recipe distributions can have different licenses. The archived OpenRewrite documentation is Apache-2.0; that does not establish the license of every recipe or supported language module.

## Related

- [[concepts/modernization-evaluation-corpus]] — representative and adverse cases for recipe changes
- [[concepts/artifact-provenance-gates]] — bind checks to produced artifacts
- [[queries/modernization-outer-loop-sources]] — licensed documentation snapshots and book availability
