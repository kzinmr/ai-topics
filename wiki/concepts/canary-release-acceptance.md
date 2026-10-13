---
title: "Canary Release Acceptance"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, reliability, monitoring, testing, verification, software-engineering]
sources:
  - raw/papers/2018_google_sre-workbook/canarying-releases.md
  - raw/papers/2018_google_sre-workbook/monitoring.md
  - raw/papers/2026-10-14_unknown_google-art-of-slos/participant-handbook.md
  - https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch10.xhtml
confidence: high
---

# Canary Release Acceptance

A canary release exposes a limited production population to a candidate for a bounded period and evaluates whether to expand, pause or recover. Chapter 16 of *The Site Reliability Workbook* distinguishes the candidate from a control population and integrates the assessment into the release process. ^[raw/papers/2018_google_sre-workbook/canarying-releases.md]

This provides production evidence for [[concepts/incremental-legacy-migration]]. It supplements prerelease testing and [[concepts/legacy-behavioral-parity]]; it does not establish every business rule's correctness.

## Define the decision before exposure

The following checkpoint record is a proposed modernization application:

| Decision input | Required definition |
|---|---|
| Candidate and control | Versions, configuration, dependencies and population labels |
| Exposure | Cohort/work partition, size, assignment and allowed growth |
| Observation | Minimum useful traffic/work, duration and relevant business cycle |
| Evaluation | User-facing SLIs, architectural constraints and reconciliation checks |
| Decision | Expand/pause/recover criteria, unresolved findings and accountable owner |
| Recovery | Traffic reversal plus persistent-state and external-effect handling |

There is no universal safe percentage or duration. A small cohort without sufficient representative work can supply almost no evidence. Batch canaries must span the processing of a work unit; multistage work needs assignment that keeps candidate and control signals distinguishable. ^[raw/papers/2018_google_sre-workbook/canarying-releases.md]

## Preserve the signal

- Break down measurements by candidate/control and version. Aggregate service health can conceal a candidate regression.
- Compare meaningful populations. Different infrastructure, request mix or load can confound attribution.
- Keep shared failure domains visible: a candidate can affect the control through a common backend.
- Use absolute service objectives as well as relative comparisons. Both populations can deteriorate together.
- Match measurement windows to the evaluation duration and account for telemetry arrival delay.

The Workbook warns that an hourly aggregate can include an earlier event and mislead a 30-minute canary. Monitoring needs the freshness and breakdowns required by the actual decision. ^[raw/papers/2018_google_sre-workbook/canarying-releases.md] ^[raw/papers/2018_google_sre-workbook/monitoring.md]

## Measure the user's outcome

Google's *The Art of SLOs* handbook, printed pages 6 and 8, expresses an SLI as the proportion of valid events classified as good. Agree the population and success definition before implementing counters. An HTTP status can be a useful proxy only if it represents the relevant outcome. ^[raw/papers/2026-10-14_unknown_google-art-of-slos/participant-handbook.md]

For modernization, a proposed batch example is “eligible work units that finish correctly before the agreed cutoff,” supplemented by reconciliation of values and records. A success log or queue acknowledgement alone does not demonstrate that result. [[queries/modernization-java-logging]] covers the target system's observation contract.

## Distinguish shadow execution and recovery

Shadow/parallel execution sends comparable work to both paths while keeping one authoritative result. Canarying sends some users or work to the candidate as the active path. Duplicated writes, billing calls or notifications require explicit containment in either design.

*Continuous Delivery*, Chapter 10, treats data and external integrations as rollback constraints. Reversing a route does not undo committed state or preserve writes lost by restoring a backup. Rehearse the actual state-aware recovery path before expanding exposure.

## Worked example: make a bounded production decision

This is an original simplified exercise; its thresholds are illustrative. Define a valid event as one eligible fee-batch work unit. Define a good event as a correct fee and reconciled state completed before the cutoff, with no duplicate notification. The **service-level indicator (SLI)** is `good events / valid events`; the **service-level objective (SLO)** is the agreed target for that indicator.

The example policy requires an SLI of at least 99%, representative work and no unresolved critical mismatch before expansion:

| Population | Valid events | Good events | SLI | Decision under this policy |
|---|---|---|---|---|
| Old-version control | 1000 | 995 | 99.5% | Meets the numerical target |
| Candidate | 1000 | 980 | 98% | Pause expansion and investigate |

The candidate fails the absolute target even if overall service health remains green. An HTTP 200 or "job complete" message does not count as good if its fee is wrong. A control/candidate comparison is also not meaningful if the control receives easy records and the candidate receives all month-end exceptions.

Before exposure, record the version/cohort, evaluation window, data-arrival delay, decision owner and recovery action. Keep routing stable for a multi-step work unit so its state and effects do not switch implementations halfway through.

If recovery redirects work to the old path after the candidate has accepted new writes, first apply the recorded reconciliation procedure. Preserve accepted writes and handle already emitted notifications. Routing reversal alone is not a database rollback.

**Check your understanding:** Would 10 successful candidate events justify expansion? This policy also requires adequate representative work. A 100% score on an insufficient sample is not enough; the example does not infer statistical certainty from a fixed count.

## Related

- [[concepts/incremental-legacy-migration]] — migration boundaries and activation
- [[concepts/legacy-behavioral-parity]] — semantic and state comparison
- [[concepts/architectural-fitness-functions]] — explicit design constraints
- [[queries/modernization-inner-loop-sources]] — archived originals and licensing
