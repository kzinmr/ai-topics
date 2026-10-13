---
title: "Semantic Transformation Recipes"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, software-engineering, compiler, developer-tooling, code-quality, testing, verification]
sources:
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_2.xhtml
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_4.xhtml
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_5.xhtml
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_6.xhtml
  - https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/ch02.html
  - https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/ch04.html
  - https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/ch05.html
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

## Worked example: rename only the intended call

Suppose a fictional library version offers `example.notice.Notifier.deliver` with the previously reviewed `dispatch` contract. A call-site recipe should migrate only that API. This example assumes the new dependency supplies `deliver`; it does not describe a real library or provide executable OpenRewrite API code.

| Source situation | Intended result | Reason |
|---|---|---|
| A call resolved to `example.notice.Notifier.dispatch` | Change the call to `deliver` | Target owner/type and method match |
| A call to `example.audit.AuditLog.dispatch` | Leave unchanged | Same spelling, different API |
| A call already using `Notifier.deliver` | Leave unchanged | No remaining migration obligation |
| Receiver type cannot be resolved | Report an unresolved case for review | Missing attribution is not permission to guess |
| Target call inside a field initializer | Transform only if that context is supported and tested | There may be no enclosing method node |

A tree node represents a piece of program syntax. **Type attribution** records the resolved types and API identities; a **visitor** inspects/changes nodes; a **cursor** exposes the surrounding tree path. Illustrative matching logic is: resolve the call, check the target API and supported context, then replace the selected invocation while preserving unrelated syntax. A text-wide replacement of `dispatch` fails the AuditLog case.

Pin the dependency/classpath, recipe and options; test every row, compile the result and independently check the notification contract. Deliberately remove the type guard: the AuditLog fixture should detect the unwanted change. Apply the recipe again: this example expects no further diff. If the API's behavior also changed, renaming a compiling call is insufficient evidence for acceptance.

Chapter 4 warns that a text recipe can turn a file into plain text during a run, leaving later semantic recipes unable to process its LST. Order and representation therefore matter: test the composed recipe, including cases that must change, rather than assuming a successful process exit means all operations ran. Chapter 6 also warns about missing parent contexts and nullable type information. Unsupported contexts need an explicit disposition, not disabled validation to force a green result.

## Distinguish AI assistance from acceptance

The mass-scale report's Chapter 4 separates finding information, assisting a bounded edit, diagnosing a modernization need and building a reusable solution. In the fictional fee batch, these could mean finding notice call sites, drafting the bounded rename, explaining a failed test and proposing a recipe. Each produces a different artifact to inspect. A plausible explanation or proposed diff establishes none of the required business outcomes by itself.

Chapter 5 discusses trust, intellectual-property concerns and task-dependent cost. Treat its examples as the report's historical vendor perspective. Review what code/context a chosen deployment sends, what the model may produce and who checks it; private hosting alone does not establish correctness or safe handling. Repeatable execution still needs [[concepts/modernization-evaluation-corpus]] and an accountable release decision.

**Check your understanding:** Both calls compile after a global rename. Has the recipe met its contract? No. The unrelated AuditLog call must remain unchanged, and the intended call must retain its approved effects.

## Related

- [[concepts/modernization-evaluation-corpus]] — representative and adverse cases for recipe changes
- [[concepts/artifact-provenance-gates]] — bind checks to produced artifacts
- [[queries/modernization-outer-loop-sources]] — licensed documentation snapshots and book availability
