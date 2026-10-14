---
title: "Modernization — A Fictional Fee-batch Exercise"
created: 2026-10-14
updated: 2026-10-14
type: query
tags: [query, tutorial, software-engineering, testing, verification, workflow, documentation]
sources:
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch04.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_016.html
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch04.html
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/02.htm
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch09.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch05.html
  - raw/papers/2020-04-08_google_building-secure-reliable/ch14.md
---

# Modernization — A Fictional Fee-batch Exercise

This original teaching case connects the inner and outer loops. All amounts, limits, measurements and identifiers are invented. It is not a financial recommendation, a book's case study or evidence of an implemented migration. Follow [the account-free study guide](modernization-independent-study-guide.md) for definitions and worked mechanisms.

## Case and approved contract

The goal is to retire an unsupported batch runtime while preserving approved business behavior. A work unit names an account and an integer amount in cents. For this pilot, the owner approves:

- Valid domain: integers from 0 to 1,000,000 inclusive. Boolean/text/fractional/missing values are invalid at the defined interface.
- Fee: 2.5% rounded down to whole cents, calculated as `amount_cents * 25 // 1000` in the Python illustrations.
- Accepted work: record the fee against the correct work/account and durably create one notification intent with the approved payload.
- Rejected work: no fee record or notification intent.
- Delivery: the receiver's deduplication/reconciliation contract governs retries; recording an intent is distinct from acceptance/delivery evidence.
- Refunds/credits: outside the pilot. Do not invent a rule for them.

The illustrative seam on the concept page checks the fee and collaborator request only. It is not a complete transactional batch implementation of this contract.

| Input amount, cents | Fee or rejection | Why selected |
|---|---|---|
| -1 | Reject with no effects | Just outside the nonnegative domain |
| 0 | 0 | Lowest valid amount |
| 20 | 0 | Fractional fee rounds down |
| 39 / 40 / 41 | 0 / 1 / 1 | Both sides of the first whole-cent fee |
| 1999 | 49 | Distinguishes down-rounding from nearest-rounding 50 |
| 1,000,000 | 25,000 | Highest valid amount |
| 1,000,001 | Reject with no effects | Just outside the upper limit |

## Inner loop: establish and accept one change

| Step | Concrete action | Evidence / decision |
|---|---|---|
| 1. Observe | Run controlled inputs against legacy revision `L1` with known initial state | Preserve actual outputs/effects as `OBS-17`; do not call an observation an approved rule |
| 2. Isolate | Select a notification recorder at the constructor seam | Check requested payload/call count without sending notices; retain a separate real integration check |
| 3. Agree | Owner records `DEC-03`, rule `FEE-01` and examples `EX-04` | The 1999 → 49 obligation comes from reviewed intent, not candidate output |
| 4. Derive cases | Select the table's partitions/boundaries and rejection cases | Check output, correct identity and absence/presence of effects |
| 5. Challenge tests | Inject nearest-rounding, wrong account and duplicate-notice faults | Each must fail its relevant assertion; line coverage alone is insufficient |
| 6. Compare | Run old and candidate on matched snapshots; preserve material differences | Normalization must not hide fee, account, status or effects; approved changes remain separately identified |
| 7. Protect design | Assess the agreed dependency direction, load/latency and old-runtime retirement | A wrapper using the old engine may match fees while failing the retirement goal |
| 8. Switch gradually | Start with effect-contained shadow comparison, then limited active work with one writer per unit | Reconcile copied state and later changes; stage/control population and recovery before expanding |

**Decision exercise:** Candidate `C2` produces 50 at 1999. Keep the reference 49 and record the failure. The owner can approve a separately scoped change, but the developer cannot relabel it a refactor. See [parity](../concepts/legacy-behavioral-parity.md) and [traceability](../concepts/modernization-traceability.md).

**State exercise:** Snapshot state is current through sequence 100. Apply changes 101–103 before routing ownership to the candidate. After cutover, write 104 occurs there. Recovery must retain/reconcile 104; restoring snapshot 100 or simply routing back loses the accepted transition. See [incremental migration](../concepts/incremental-legacy-migration.md).

**Canary exercise:** Under an invented target of at least 99% good work units, control is 995/1000 = 99.5% and candidate is 980/1000 = 98%. The candidate fails that target. A good unit must include correctness, state/effects and the agreed cutoff; these arithmetic counts do not establish representativeness or statistical certainty. See [canary acceptance](../concepts/canary-release-acceptance.md).

## Outer loop: make the method reusable and inspectable

| Step | Concrete action | Evidence / decision |
|---|---|---|
| 9. Maintain knowledge | Publish readable views of `DEC-03` and `EX-04`, and verify that the adapter consumes the current example | A deliberately changed fixture expectation must break the unchanged implementation's check |
| 10. Package a change | Version a bounded recipe, input conditions, positive/negative cases and composition order | Same-spelled unrelated methods remain unchanged; unresolved types/context need review |
| 11. Recover execution | Persist job `W1`, stable operation key `W1/notice`, attempts and receiver result | A lost reply is reconciled; a retry uses the same operation identity under receiver enforcement |
| 12. Evaluate the method | Preserve ordinary, boundary, invalid, lost-reply and changed-approval cases | Report distinct failure dimensions; curated regression pass rate is not a production-rate estimate |
| 13. Promote the artifact | Bind candidate artifact `A1`/digest `H1`, run `RUN-08`, fixture/environment `E1` and policy `P1` | Approval names the artifact, evidence and allowed action; a rebuilt `H2` needs applicable new evidence |

Recipe, recovery and provenance records are local proposals for this example. They are not mandatory schemas from the books. The reusable method must preserve applicable context and owner decisions; the same fee name in a different business flow does not justify transferring this contract.

## Fault scenarios and answers

| Scenario | Correct response | Where to learn why |
|---|---|---|
| Fee is 49, but account B receives account A's result | Reject parity; numeric equality missed identity/effects | [Parity comparator](../concepts/legacy-behavioral-parity.md) |
| A property suite checks only bounds/monotonicity and accepts an always-zero fee | Add independently approved concrete examples; weak properties missed the rule | [Properties](../concepts/property-based-testing.md) |
| Receiver accepts a notice, then reply is lost | Reconcile or retry under enforced stable-key semantics; do not infer no effect from timeout | [Recovery timeline](../concepts/modernization-workflow-recovery.md) |
| All notification workers stall | Test bounded waits, isolation, backlog policy and recovery of accepted work | [Resilience testing](../concepts/resilience-acceptance-testing.md) |
| Judge passes 48/100 while human review passes 40/100 | Inspect the 36/4/12/48 matrix, error rates and uncertainty | [Evaluation arithmetic](../concepts/modernization-evaluation-corpus.md) |
| Worker presents the `H1` approval for `H2` | Stop promotion; a release label does not bind the substituted artifact | [Artifact gate](../concepts/artifact-provenance-gates.md) |

Use these faults to challenge the relevant check as well as the candidate. Do not infer full system correctness from the simplified comparator or recorder. Real data storage, transactions, concurrency, authentication and delivery need the project's own integration and operational evidence.

## Explain the decisions back

Without opening the books, explain who owns `DEC-03`, what a recorder establishes, why restoring snapshot 100 is insufficient after write 104, why a new attempt ID cannot substitute for the operation key, and why `H1` evidence does not authorize `H2`. The answers are in the case and linked mechanisms; inability to answer identifies a specific explanation to revisit.

[[concepts/legacy-modernization-moc]] connects the wider concepts. [[queries/modernization-independent-reading-review]] records the review's criteria and limits.
