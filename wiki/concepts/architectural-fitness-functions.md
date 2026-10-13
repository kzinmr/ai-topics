---
title: "Architectural Fitness Functions"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, architecture, verification, testing, reliability, software-engineering]
sources:
  - https://learning.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch02.html
  - raw/papers/2020-04-08_google_building-secure-reliable/ch06.md
  - raw/papers/2020-04-08_google_building-secure-reliable/ch14.md
confidence: high
---

# Architectural Fitness Functions

An architectural fitness function objectively assesses a characteristic that the architecture must preserve. *Building Evolutionary Architectures*, second edition, Chapter 2, applies the idea to such concerns as dependency structure, performance and security. The result guides incremental change and reveals degradation.

The mechanism can be a code check, measurement or defined manual assessment. Using a monitoring product alone does not establish a fitness function: a relevant characteristic and interpretable evaluation criterion must exist.

## Choose scope and execution deliberately

| Dimension | Alternatives | Design implication |
|---|---|---|
| Scope | Atomic / holistic | A local constraint can pass while an interaction fails |
| Cadence | Triggered / continual / temporal | Choose feedback speed and cost for the risk |
| Result | Fixed / context-dependent | An objective threshold may vary with stated workload |
| Invocation | Automated / manual | Manual verification still needs a defined procedure |
| Discovery | Intentional / emergent | Add and revise checks as important characteristics emerge |

For example, caching may satisfy an isolated latency check while violating a freshness requirement. A holistic check evaluates the relevant combination. Continual verification reduces detection delay but can impose runtime cost; a triggered check on recorded evidence may be cheaper but too late for a critical violation.

The authors distinguish architectural characteristics from domain behavior. Keep business acceptance examples and architectural checks separately identifiable, even when the same test framework runs both. [[concepts/specification-by-example]] and [[concepts/legacy-behavioral-parity]] cover the domain obligation.

## Apply to a modernization checkpoint

The following are original candidate checks; choose them from the actual system's requirements:

| Required characteristic | Candidate evidence | Important limit |
|---|---|---|
| Dependency direction | Check prohibited package/module references | Static references miss some runtime interactions |
| Retired runtime independence | Inspect artifacts and execute without the old engine | Matching outputs alone can accept a wrapper |
| Latency at an agreed load | Measure a defined percentile on a pinned workload | A threshold without workload context is misleading |
| Recoverability | Exercise a documented failure and recovery path | A healthy-path check supplies no recovery evidence |
| Deployment integrity | Verify artifact provenance and authorized promotion | A tested source revision is not necessarily the deployed binary |

Google's *Building Secure and Reliable Systems*, Chapter 6, connects understandability to explicit invariants, narrow interfaces and clear responsibility. Chapter 14 connects approved source, build and test steps to the artifact actually deployed. These are complementary foundations for selecting inspectable constraints. ^[raw/papers/2020-04-08_google_building-secure-reliable/ch06.md] ^[raw/papers/2020-04-08_google_building-secure-reliable/ch14.md]

## Define the assessment record

State the characteristic, rationale, owner, input/workload, measurement, threshold, cadence and failure response. Version the assessment alongside the requirement and retain run evidence. This record is a proposed application of fitness functions, not a universal template from the book.

When legitimate requirements change, review the criterion and record the reason in [[concepts/modernization-traceability]]. An agent should not weaken it merely to make its change pass.

## Limits

The book emphasizes outcomes over tool choices. Objective measurements expose tradeoffs but do not choose every tradeoff for the organization. More checks do not automatically make a better architecture; poorly selected constraints can measure convenience rather than the characteristic that matters.

## Related

- [[concepts/incremental-legacy-migration]] — checkpoints and coexistence
- [[concepts/canary-release-acceptance]] — production evaluation of a candidate
- [[concepts/modernization-traceability]] — criterion ownership and approved changes
- [[queries/modernization-inner-loop-study-notes]] — inspected reading scope
