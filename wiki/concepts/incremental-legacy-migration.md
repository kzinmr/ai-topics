---
title: "Incremental Legacy Migration"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, software-engineering, architecture, design-patterns, testing, reliability]
sources:
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch02.html
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch04.html
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch03.html
  - https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch10.xhtml
  - https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch12.xhtml
  - raw/papers/2018_google_sre-workbook/canarying-releases.md
confidence: high
---

# Incremental Legacy Migration

Incremental migration replaces bounded capabilities while old and new implementations coexist. Each step has a defined observation, acceptance and recovery boundary. It can lead to another monolith, a module or services; the method does not require microservices as the destination.

Sam Newman's *Monolith to Microservices*, Chapter 3, distinguishes several mechanisms that solve different problems.

## Choose the mechanism by the boundary

| Mechanism | What changes or is observed | Appropriate condition |
|---|---|---|
| Strangler Fig | Redirect calls at an interceptable perimeter | Requests can be mapped to the capability being moved |
| Branch by abstraction | Select an implementation behind an internal boundary | The capability is buried inside the existing system |
| Parallel run | Execute both paths, compare results, retain one authority | Side effects can be isolated and inputs aligned |
| Canary release | Expose a limited population to the candidate and evaluate it | Production risk can be bounded and measured |

A perimeter router cannot isolate a capability invoked by many unrelated internal flows. In that case, introduce an internal seam; see [[concepts/legacy-code-seams]]. Branch by abstraction concerns coexisting implementations in the application, rather than a long-lived source-control branch.

## Separate deployment from activation

A replacement can be deployed and tested in its final environment before it serves users. First establish the interception or abstraction with the old implementation still active. Add the candidate, verify it, then change selection. This makes infrastructure setup, implementation and user exposure separately reviewable.

Newman's cleanup step removes the inactive implementation and obsolete toggles. A useful abstraction may remain, but an indefinite collection of temporary switches is not completion.

## Parallel execution needs a side-effect plan

Running both implementations is not safe by default. Newman's notification example substitutes a recorder at the actual sending boundary so that the comparison path does not send a second email. Replacing the whole service call would make verification easier while hiding network behavior that also needs evaluation.

Define one authoritative result, comparable input/state, the effects suppressed on the comparison path and the evidence recorded. Check latency, timeouts and failure rates as well as values. This is an application of [[concepts/legacy-behavioral-parity]].

Canarying is different: some real users receive the candidate's result. See [[concepts/canary-release-acceptance]] for population, duration, control and monitoring requirements. ^[raw/papers/2018_google_sre-workbook/canarying-releases.md]

## Recovery includes state and contracts

*Continuous Delivery*, Chapter 10, identifies persistent data and integrated systems as constraints on rollback. Restoring a pre-release database backup can discard writes made afterward. Moving traffic back does not reverse those writes.

The following is a proposed modernization record:

- Identify the writer and read path during each coexistence stage.
- Define schema and consumer compatibility across the transition.
- Record synchronization, reconciliation and restart/replay behavior.
- Decide how new writes are preserved or reconciled on recovery.
- Rehearse the recovery process and establish its stop conditions.
- Verify that retiring the old path removes the intended dependencies.

Newman also warns that adding business changes during a migration can weaken rollback: the old path may no longer provide the same features. Keep intentional differences explicit in [[concepts/modernization-traceability]] and reduce the size of the transition where possible.

## Worked example: replace a fee batch gradually

This original fictional plan aims to retire an unsupported runtime while preserving the approved fee calculation and notification behavior. A modular batch executable is an eligible destination; microservices are not an acceptance condition. Newman's Chapter 2 starts from the goal and evaluates progress against it.

| Stage | Active result / writer | Candidate's role | Advance only when |
|---|---|---|---|
| Establish boundary | Old batch | Deployed but inactive | The selection boundary leaves old behavior unchanged |
| Compare | Old batch | Calculate from matched fixtures; record notification intents | Fees, state effects and intents reconcile under reviewed comparison rules |
| Limited activation | Exactly one selected implementation per work unit | Process the selected cohort as the active path | Candidate/control outcomes and recovery conditions meet the agreed policy |
| Complete transition | New batch | Own all in-scope work | Data, consumers, schedules and operations are accepted |
| Retire | New batch | Operate without the old runtime | Old jobs, toggles and forbidden dependencies are removed and checked |

In the comparison stage, both paths receive amount 1,999 cents and should produce fee 49. Only the old path sends the real notification. The candidate records its intent, so a discrepancy can be inspected without sending two notices. In limited activation, some work receives the candidate's real result; that is no longer a shadow comparison.

### If data moves too

A **snapshot** is a copy at a known point in time. A **backfill** copies existing records into the new store. Changes after that snapshot must also be copied before the new store becomes authoritative.

Suppose the snapshot ends at change sequence 100. The old system then writes changes 101–103 while the copy runs. The new store must include and reconcile those changes, not merely the snapshot, before reads switch. Matching row counts alone can conceal different values. Chapter 4's application-synchronization pattern stages bulk copying, synchronized writes and a read switch, while preserving a fallback for a period.

For the actual project, choose one accountable writer or a rigorously specified synchronization protocol. Define handling of partial writes, duplicates, ordering and recovery. Two applications independently trying to keep two stores synchronized can create divergent state. This example does not mandate dual writing.

After the new writer accepts change 104, redirecting reads to an old store ending at 103 loses visibility of accepted work. Recovery must first retain or reconcile 104. An old database backup is not a sufficient recovery plan.

**Check your understanding:** Has a new executable that still invokes the old runtime completed retirement? No. It may be a useful coexistence adapter, but the retirement criterion needs execution without that dependency.

## Related

- [[concepts/enterprise-legacy-modernization]] — end-to-end delivery practice
- [[concepts/legacy-code-seams]] — internal substitution opportunities
- [[concepts/canary-release-acceptance]] — evaluate limited production exposure
- [[concepts/legacy-behavioral-parity]] — equivalence and approved differences
