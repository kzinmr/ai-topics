---
title: "Incremental Legacy Migration"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, software-engineering, architecture, design-patterns, testing, reliability]
sources:
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch03.html
  - https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch10.xhtml
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

## Related

- [[concepts/enterprise-legacy-modernization]] — end-to-end delivery practice
- [[concepts/legacy-code-seams]] — internal substitution opportunities
- [[concepts/canary-release-acceptance]] — evaluate limited production exposure
- [[concepts/legacy-behavioral-parity]] — equivalence and approved differences
