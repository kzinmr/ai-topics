---
title: "Modernization — Account-free Reading Review"
created: 2026-10-14
updated: 2026-10-14
type: query
tags: [query, review, documentation, education, software-engineering, testing, verification, methodology]
sources:
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_017.html
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch05.xhtml
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/03.htm
  - https://learning.oreilly.com/library/view/ai-engineering/9781098166298/ch04.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch05.html
  - raw/papers/2020-04-08_google_building-secure-reliable/ch13.md
---

# Modernization — Account-free Reading Review

**Finding:** the first-pass pages supplied definitions, useful distinctions and source links, but often left readers to construct their own worked case, failure test and decision procedure. They were a concept map with uneven teaching depth. After the continuation, **16 concept pages** provide worked mechanisms and answered comprehension questions; [the study guide](modernization-independent-study-guide.md) and [integrated exercise](modernization-batch-example.md) let a reader follow both loops without an O'Reilly account.

Scope is the **14 unique priority works** confirmed by the user. The review covers their selected modernization learning purposes, not independent access to every book's entire contents. [The reading ledger](modernization-reading-continuation.md) records actual new inspection and limits; earlier passes remain preserved. Baseline for this review is repository revision `8508dd20563387e667f73ce13132d81a74ea7491`.

## Review criteria

The following desk-review criteria are local editorial choices, informed by readable specification, living curation and effective testing. They are not a published book's scoring rubric:

1. Define the concept and essential terms in the page or in an accessible repository dependency.
2. Explain the problem, applicability and necessary assumptions.
3. Include a concrete input/condition and its output, effects or decision.
4. Give a repeatable procedure and a falsifiable pass/fail distinction.
5. State limits, failure modes and which authority resolves a tradeoff.
6. Provide a comprehension question with an answer supported by the page, without a required subscription link.

Repository links are legitimate learning dependencies. A paywalled source may document provenance or optional depth, but must not supply an essential missing definition or exercise answer. Basic programming, testing and data-processing familiarity is assumed. This is an author desk review, **not an independent human usability study** or evidence that every reader will understand the pages.

## Findings and corrections

Each result below was checked against the six criteria by reading the explanation and tracing the example/answer. A linked source or the mere presence of a heading was not treated as sufficient.

| Concept | First-pass gap / new foundation | Standalone mechanism added | Result within this review scope |
|---|---|---|---|
| [Characterization testing](../concepts/characterization-testing.md) | No populated numeric observation/decision case | 0/20/40/1999 rounding observations and separate target decision | Criteria met; sampled behavior remains narrower than intent |
| [Legacy code seams](../concepts/legacy-code-seams.md) | Enabling point described without an executable demonstration | Original injected recorder, argument/count assertions and real-integration limit | Criteria met; recorder is not delivery evidence |
| [Specification by Example](../concepts/specification-by-example.md) | Collaboration and automation separation lacked a full small workshop | Goal, owner/roles, approved examples, exclusions and expectation-consuming adapter | Criteria met; agreement and continued review remain necessary |
| [Incremental migration](../concepts/incremental-legacy-migration.md) | State-preserving recovery lacked a numbered transition | Five coexistence stages and sequences 100–104 | Criteria met; synchronization protocol is project-specific |
| [Property-based testing](../concepts/property-based-testing.md) | Generator/oracle cautions lacked a falsifiable small property | Domain, false-additivity counterexample and always-zero mutant | Criteria met; properties are not exhaustive correctness |
| [Architectural fitness functions](../concepts/architectural-fitness-functions.md) | No explicit workload/threshold versus business-result contrast | Dependency/latency obligations, known violations and retirement test | Criteria met; architectural success does not imply fee correctness |
| [Canary acceptance](../concepts/canary-release-acceptance.md) | No computed candidate/control decision | SLI/SLO definitions, 99.5% versus 98% and state-aware recovery | Criteria met; illustrative counts do not establish statistical certainty |
| [Behavioral parity](../concepts/legacy-behavioral-parity.md) | Comparator itself was not demonstrated against known faults | Original required-field comparator with fee/count/account mismatches | Criteria met; real state/payload/delivery require additional checks |
| [Traceability](../concepts/modernization-traceability.md) | Generic fields lacked one populated end-to-end chain | OBS-17 → FEE-01/DEC-03 → EX-04 → A1/RUN-08 → REL-02 | Criteria met; connected records alone do not establish semantics |
| [Living documentation](../concepts/living-documentation.md) | Reconciliation failure was described without a reproducible fixture challenge | Changed-expectation check, superseding decision and reader-specific views | Criteria met; regeneration is not accuracy |
| [Semantic recipes](../concepts/semantic-transformation-recipes.md) | No concrete positive/negative type/context cases | Fictional target API versus AuditLog, unknown types, composition and repeat-application checks | Criteria met; illustrative matching logic is not an implemented recipe |
| [Workflow recovery](../concepts/modernization-workflow-recovery.md) | No concrete lost-reply/retry timeline or version transition | Stable operation key, receiver enforcement, effect units and approval/version scope | Criteria met under explicit receiver assumptions |
| [Evaluation corpus](../concepts/modernization-evaluation-corpus.md) | No worked judge-error calculation or populated failure set | Five cases, split/label criteria and original 36/4/12/48 judge matrix | Criteria met; correction requires transferable error rates and uncertainty review |
| [Artifact gates](../concepts/artifact-provenance-gates.md) | No explicit substituted-artifact decision | Digest/signature distinction, H1/H2 gate, scoped authority and negative checks | Criteria met; no production gate is implemented here |
| [Specification-based test design](../concepts/specification-based-test-design.md) | New foundation central to Effective Software Testing | Preconditions/postconditions/invariants, partitions, boundaries and mutation limits | Criteria met; business agreement remains a separate responsibility |
| [Resilience acceptance testing](../concepts/resilience-acceptance-testing.md) | New foundation central to Release It! | Timeout/breaker/bulkhead definitions, injected-failure matrix and recovery procedure | Criteria met; times/capacity/fallback need actual owner agreement |

The two new pages are distinct from existing concepts: Specification by Example establishes shared intent, while test design selects cases from that contract; workflow recovery handles effect/state continuation, while resilience acceptance tests whether failure handling meets the service obligation.

## Verification evidence

- Executed the two original published Python examples, including their assertions. Independently specified seven valid fee inputs and seven invalid representations/domain cases passed; invalid inputs caused no recorder effects.
- Challenged the comparator with wrong fee, extra notice, wrong account and each missing required field. Missing a field on both sides still failed; an explicitly incidental extra field did not affect the compared contract.
- Checked the false-additivity example and a zero-output mutant: the mutant passes the two weak properties but fails approved examples. Nearest-rounding yields 50 rather than 49 for 1999.
- Recomputed the judge matrix, sensitivity 0.9, false-positive rate 0.2, raw pass 48% and corrected example 40%; recomputed the canary's 99.5%/98% against its illustrative 99% target.
- Traced the written ownership/recovery, recipe, reconciliation and artifact decisions through the integrated case. These are explanatory walk-throughs and proposed tests, not executed production systems or statistical experiments.

Structural metadata, source references, links, page lengths, index counts, prior-content preservation and repository hooks are checked as publication gates and recorded in `wiki/log.md`. Existing raw/transcripts remain unchanged. The larger guide tables, selections and order are preserved; their new links lead to the continuation and standalone route. Existing unrelated duplicate index entries are inherited; this change adds no duplicate. The oversized prior operation log was rotated by indexing its already-published immutable Git snapshot in the annual archive; the complete original history was verified byte-for-byte. Inlining historical Japanese entries into the English annual file triggered the language hook, so that uncommitted attempt was replaced with an English archive reference without bypassing the hook.

## Remaining limits

The selected concepts are understandable without full book text, within the declared audience and desk-review criteria. A production implementation still needs the actual business owner, environment, schema, service contracts, privileges, risk thresholds and integration/recovery runs. No measured modernization saving, mainframe retirement, rollout or security guarantee is claimed.

The commercial books' complete public text remains unverified; focused subscription reading does not close that acquisition gap. This task preserves permitted public originals/PDFs and original explanations rather than reproducing commercial chapters. Entire-book arguments and specialist topics outside the selected learning purposes remain optional source reading under the guides' conditional criteria.

## Related

- [[queries/modernization-independent-study-guide]] — account-free route through the 14 priorities
- [[queries/modernization-batch-example]] — integrated comprehension exercise
- [[queries/modernization-reading-continuation]] — inspected sections and coverage boundary
- [[concepts/legacy-modernization-moc]] — wider concept map
