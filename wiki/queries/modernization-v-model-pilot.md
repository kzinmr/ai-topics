---
title: "AI Modernization Pilot for Requirements and Acceptance Capacity"
created: 2026-10-15
updated: 2026-10-15
type: query
tags: [query, coding-agents, software-engineering, testing, verification, workflow, productivity, methodology]
confidence: medium
sources:
  - queries/modernization-v-model-strategy.md
  - queries/modernization-batch-example.md
  - queries/modernization-reading-continuation.md
  - concepts/modernization-traceability.md
  - concepts/legacy-behavioral-parity.md
  - concepts/living-documentation.md
  - concepts/modernization-evaluation-corpus.md
  - concepts/modernization-workflow-recovery.md
  - concepts/artifact-provenance-gates.md
  - raw/papers/2025_google_dora-gen-ai/impact-of-generative-ai.md
  - raw/papers/2020-04-08_google_building-secure-reliable/ch13.md
  - raw/papers/2018_google_sre-workbook/canarying-releases.md
---

# AI Modernization Pilot for Requirements and Acceptance Capacity

This playbook applies [[queries/modernization-v-model-strategy]] to one bounded legacy business flow and then tests transfer to another. Its operating rules, lanes and 90-day schedule are proposed starting choices. The learning objective is to establish whether reusable decisions and acceptance reduce total effort at an unchanged quality bar. Completing a production migration within 90 days is not a condition assumed here.

## Start with a flow whose acceptance can be established

Select a flow with business value, an accountable owner, observable inputs/state/effects and a controlled way to exercise the legacy behavior. Include representative exception handling and the dependencies needed for meaningful comparison. Inventory period-end behavior, reference-data changes, concurrency and recovery before calling a daily batch simple. If a legacy runtime or authoritative intent is unavailable, first fund a bounded discovery outcome and revise the acceptance strategy explicitly.

Write the objective and exclusions in a short charter. For example: "Retire runtime X for the approved fee batch while preserving the agreed fee, account, notification and cutoff obligations; refunds and a new service decomposition are outside this wave." Identify consumers, writer ownership, retained data, coexistence cost and the evidence needed to decommission the old path. Do not silently turn an upgrade into a feature program.

| Responsibility | Owns the decision | Work an agent can prepare |
|---|---|---|
| Business/domain owner | Intended behavior, exceptions, changed or retired rules | Source-linked observations, conflicting examples, options and impact |
| Technical/data owner | Boundary, contracts, design characteristics and writer transfer | Dependency map, candidate designs, migration/reconciliation plan |
| Verification owner | Oracle provenance, representative cases, checker adequacy | Cases, adapters, fault candidates, failure clustering and evidence navigation |
| Delivery/platform owner | Reproducible execution, maintained recipes, workflow recovery | Environment definitions, recipe drafts, reproducible run instructions |
| Release/operations owner | Exposure, stop conditions, recovery and residual operational risk | Rehearsal evidence, signals, artifact identity and unresolved differences |

One person can hold several roles. Preserve an independent basis for acceptance and review changes to that basis separately from the candidate that failed it. Budget protected domain and verification time; an unstaffed responsibility is a delivery dependency, not an invitation for the agent to invent approval.

## Use one decision record to feed both shoulders

Use [[concepts/modernization-traceability|the existing ledger]] rather than creating separate competing requirements and test-plan databases. The following populated record extends the repository's fictional teaching case; its rule and identifiers are not production requirements.

| Field | Example |
|---|---|
| Objective and scope | Retire the old runtime for the fee batch; valid integer-cent amounts 0–1,000,000 |
| Observation | `OBS-17`: legacy revision L1 returns 49 for amount 1999 on fixture F1 |
| Evidence status | Observed legacy result; confirm intended rule separately |
| Decision | `DEC-03`, business owner: retain 2.5% rounded down; refunds unresolved and excluded |
| Acceptance | `EX-04`: 1999 → 49, correct work/account, one durable notice intent; invalid input has no effects |
| Applicability and review trigger | This approved product/period/input domain; review after rule, schema or reference-data changes |
| Independent checks | Approved boundary cases; wrong-account/rounding/duplicate-effect faults; separate integration evidence |
| Implementation and release | Candidate C2, artifact H1, fixture/environment E1, run R8, scoped release decision |

The owner reviews the smallest useful decision packet: disputed fact, evidence locations, concrete examples, viable choices and their consequences. Record unknowns explicitly. Group questions sharing one business rule and resolve them together. Do not require a review of every generated line of documentation.

Publish role-specific views from the record. The SME sees meaning and exceptions; the engineer sees contracts and affected code; the verifier sees expected results and fault cases; operations sees ownership and recovery. After a change to an example, check that the adapter consumes the changed expectation. A green test that uses an old hardcoded value is not reconciled documentation. See [[concepts/living-documentation]].

## Route work according to uncertainty and consequence

Use the strictest applicable lane. File count, model confidence and a green build are insufficient routing criteria. Changes can move to a more restrictive lane when discovery reveals new dependencies.

| Lane | Conditions | Permitted execution and acceptance |
|---|---|---|
| Bounded repeatable change | Known scope, validated recipe, strong independent checks, controlled effects and tested reversibility | Agent executes in isolation under an approved policy; deterministic gates and the existing merge/release policy apply; audit samples examine misses |
| Judgment required | Intent/design alternatives or unexpected differences need resolution, but experiments can be contained | Agent investigates and proposes; named owner decides the affected contract; verifier reviews evidence before broader execution |
| Consequential state or business change | High-impact rules, writer ownership, irreversible effects or weak recovery | Explicit domain/data decisions, independent operational evidence, staged cutover and rehearsed recovery; no unattended promotion |

Automatic admission stops when a critical rule has no disposition, a material difference is unexplained, an execution environment cannot reproduce evidence, or a check/policy/fixture is changed without its required review. Confine the stop to dependent work when possible. A new model, recipe or environment version invalidates only evidence whose assumptions it changes, but that applicability must be assessed.

Implementers may propose test corrections; they cannot self-authorize changing approved expectations. Keep comparison fixtures and promotion credentials outside the worker's unrestricted write scope. Record what the policy permits and enforce it at execution. A second agent checking the same generated story does not turn it into independent evidence.

## Run the smallest complete acceptance loop

1. **Observe and prepare.** Pin legacy inputs/environment, capture outputs/state/effects and expose uncertainty. Preserve suspicious old behavior without automatically endorsing it.
2. **Agree and challenge.** Approve the target obligations and critical examples. Challenge the comparator and adapter with known faults before trusting their green results.
3. **Implement one coherent change.** Use a supported recipe when applicable; otherwise give the agent bounded scope, allowed files/actions, non-goals, acceptance commands and stop conditions.
4. **Run checks and classify failures.** Separate candidate defects, contract disagreements, fixture faults and environment instability. Preserve the first failing evidence and send it to the appropriate owner.
5. **Reconcile and rehearse.** Check real integrations, state transfer, partial failure and recovery under the relevant workload. Distinguish a recorded notification intent from receiver acceptance or delivery.
6. **Accept the exact artifact and monitor.** Bind applicable approvals and runs to the promoted digest. Expand exposure only under the agreed operational policy; retain evidence for the next flow.

An illustrative agent brief is: "For approved rule DEC-03 and fixture F1, map affected code and dependencies, propose one bounded change, execute the listed checks, and report artifact/run IDs plus unexplained differences. Preserve approved expectations. Stop dependent execution if intent, external effects or required evidence exceed this scope." Supply actual paths, tools and policy in the project; this wording alone enforces no boundary.

| Acceptance layer | Evidence it contributes | Challenge that should expose a gap |
|---|---|---|
| Structural traceability | Every in-scope rule has a disposition and applicable implementation/check references | Delete a required mapping and require the structural gate to fail |
| Business intent and boundaries | Approved examples, partitions and explicitly scoped properties | Replace down-rounding with nearest-rounding at 1999; an always-zero implementation must fail examples |
| State and external effects | Matched snapshots, record identities/totals, allowed side effects and receiver evidence | Wrong account or repeated notice despite a correct numeric result |
| Architecture and retirement | Dependency constraints and execution without the retired runtime | A parity-passing wrapper still calling the old engine |
| Resilience and coexistence | Timeouts, capacity isolation, catch-up and one writer per unit | Receiver accepts before reply is lost; retry must reconcile under its stable-key contract |
| Release integrity and operations | Checked artifact identity, representative canary signals and recovery drill | Substitute H2 for approved H1; recover after a new committed write without losing it |

Use selected fault injection to assess detection, then restore clean fixtures. Passing these examples establishes their tested obligations, not exhaustive correctness. Google distinguishes unit-test doubles from integration evidence and recommends challenging assertion strength. The existing [[queries/modernization-batch-example|batch exercise]] supplies worked answers. ^[raw/papers/2020-04-08_google_building-secure-reliable/ch13.md]

A shadow execution must contain side effects; a canary executes real work for a limited population. Choose observations representative of the business cycle, including rare critical cases through targeted tests. A small sample with no failures cannot prove a rare failure rate acceptable. Stop and recovery criteria must name material business differences and state/effect handling as well as service availability. ^[raw/papers/2018_google_sre-workbook/canarying-releases.md]

## Limit work in progress and measure the complete flow

Draw a visible queue for clarification, implementation, verification and release. Set initial limits from staffed capacity and observed work size. As an illustrative start, a team might allow one candidate awaiting a particular SME decision and two awaiting a particular verifier, then adjust after observing queue age and urgent work. These values are not general staffing ratios. When a queue is full, direct effort to resolving or verifying existing work and reusable checks.

Define the work unit before collecting metrics and retain failed/abandoned attempts in the cost numerator. Record active human effort once, even when several agents run concurrently; elapsed agent time, human labor, queue time and monetary tool/environment costs are different measures. Use consistent scope/risk strata and acceptance standards. DORA's archived measurement guidance supports baselines, multiple levels and distinguishing usage from impact. ^[raw/papers/2025_google_dora-gen-ai/impact-of-generative-ai.md]

| Measure | Operational definition | Decision it informs |
|---|---|---|
| Total labor per accepted flow | Discovery + design + implementation + verification + operations/rework labor, including unsuccessful attempts; report setup separately and allocate shared upkeep transparently | Is recurring effort falling without hiding work in another team? |
| Lead time and queue age | Start from selection of the flow through agreed operational acceptance; show pre-implementation discovery and stage waiting separately | Which stage constrains delivery; where should admission stop? |
| First-pass acceptance | Candidates accepted without substantive repair / candidates first submitted, by risk class | Is the evidence or transformation improving? Report canceled work separately |
| Repeated SME work | Reopened previously answered questions under unchanged assumptions, and SME minutes per accepted flow | Are decisions findable and applicable; are ownership or views missing? |
| Meaningful reuse | Reuses accepted after applicability check / attempted reuses; include adaptation and upkeep effort | Does the second flow justify the shared asset? |
| Quality and operations | Escaped defects by severity/exposure, material reconciliation failures, recovery failures, service objectives and legacy dependencies retired | Is an apparent saving actually a transfer of risk? |
| Oracle/checker health | Detection of selected known faults, unexplained differences, flaky-check burden and disputes about labels | Can the reported pass rate support acceptance? |

Classify new issues as previously hidden obligations, deliberate scope additions, AI-introduced defects or environment/checker problems. Compare the same obligations across methods. Necessary discovery may improve outcomes while increasing initial cost; it should not be disguised as either pure AI waste or already-realized savings.

Where feasible, compare matched tasks or introduce the method across comparable flows in stages, recording tool/environment versions, experience and risk. Avoid learning leakage from repeating the identical task. Historical comparisons are weaker when scope, staff or quality standards change. With few heterogeneous pilots, report ranges and concrete mechanisms rather than a causal percentage. The setup amortization example in [[queries/modernization-v-model-strategy]] is a budget illustration, not an estimate from these measurements.

## Use the first 90 days to make expansion decisions

The timeboxes below organize learning. Approval depends on evidence, so a failed exit condition can extend discovery, narrow scope or stop a wave. Long business cycles may require observation beyond this window.

| Window | Work and accountable roles | Exit decision |
|---|---|---|
| Days 1–15 | Sponsor and flow owners set objective, baseline, risks, obligations, staffing and acceptance/stop criteria; platform owner verifies legacy execution | Is this a bounded executable pilot, or should the funded outcome be discovery only? |
| Days 16–30 | Domain and verification owners resolve critical examples, establish comparison fixtures and challenge checks; technical owner chooses the seam and state boundary | Is intent sufficiently resolved and acceptance credible for the next change? |
| Days 31–60 | Engineering delivers small candidates; verifier classifies failures; operations rehearses cutover/recovery; platform owner records reusable assets | Does the flow meet its agreed functional and operating obligations? Actual release follows the release policy |
| Days 61–90 | A second comparable flow tests reuse; owners review total effort, queues, quality and maintenance | Expand only supported change families, refine the method or stop investment that has no plausible recurring benefit |

Choose numerical thresholds with the owner before seeing the candidate results. Examples of categorical expansion conditions are: no unresolved critical obligation; no unexplained material discrepancy in the agreed corpus; selected known faults detected; state-preserving recovery demonstrated; unchanged quality requirements; and a plausible benefit after upkeep. A lower-cost recurring flow supports expansion but does not by itself establish statistical causality or full program payback.

Do not expand if repeated SME clarification is unchanged because records lack applicability, if accepted throughput is flat while queues grow, if failures cluster outside the tested workload, or if every recipe needs bespoke repair. Address the observed mechanism first. If a critical behavior cannot be independently evaluated, retain a contained/manual route or change the modernization scope instead of compensating with more generated tests.

## Common responses that make the shoulders heavier

| Tempting response | Why it fails | Better intervention |
|---|---|---|
| Generate a complete specification for the entire estate first | Unverified inferred rules create a large review backlog | Resolve the next valuable flow and shared high-impact dependencies |
| Generate code and its golden answers together | A common misunderstanding can pass every test | Independently approved intent, observations and checker challenges |
| Add more reviewers or agents to every task | Coordination grows while the scarce decision owner remains serialized | Reduce repeated decisions, constrain WIP and target demonstrated bottlenecks |
| Require a manual approval for every tool call | Attention becomes routine confirmation with weak context | Enforced scope policies, focused consequential decisions and evidence-based audits |
| Replace all review with an agent judge | Fluent agreement and an uncalibrated pass rate conceal errors | Deterministic checks plus calibrated assistance and accountable acceptance |
| Generalize the pilot into a platform immediately | Maintenance cost arrives before reusable demand is demonstrated | Test transfer to a second flow and retain only valuable shared assets |
| Count output parity as complete modernization | The old runtime, data risk or operational dependency can survive | Verify retirement, state, resilience and release obligations separately |

The reusable result is a narrower uncertainty set, an accepted flow and maintained evidence that makes the next decision cheaper. Preserve business decisions, test obligations and recovery responsibility as generation becomes faster; remove repeated translation, rediscovery and avoidable waiting.
