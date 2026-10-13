---
title: "Resilience Acceptance Testing"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, reliability, testing, verification, distributed-systems, monitoring, software-engineering]
sources:
  - https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0048.xhtml
  - https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0049.xhtml
  - https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0050.xhtml
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch09.html
---

# Resilience Acceptance Testing

Resilience acceptance testing checks whether a system preserves the required business service and recovers acceptably under specified failures. A healthy-path test cannot establish this. *Release It!*, second edition, explains timeout, circuit-breaker and bulkhead mechanisms; [[concepts/modernization-workflow-recovery]] supplies the complementary effect/reconciliation contract.

## Know what each mechanism does

| Mechanism | Plain meaning | Remaining obligation |
|---|---|---|
| Timeout | Stop waiting beyond a defined duration | The remote operation may still have completed |
| Circuit breaker | Temporarily avoid calls to a dependency judged unhealthy | Define permitted degraded behavior and a recovery/probe policy |
| Bulkhead | Reserve/isolate capacity so one failure does not consume all resources | Check shared lower-level dependencies and the remaining useful service |

A circuit breaker normally allows calls in its **closed** state. Its **open** state rejects or applies the agreed fallback without calling the dependency. A **half-open** state allows limited probes to decide whether ordinary calls may resume. Threshold, failure window and probe limits are design choices, not universal constants.

A fallback changes business behavior. A fee batch must not invent a successful delivery merely because its notice service is unavailable. An accepted outcome might instead be a durably recorded pending notification, if the owner approves that behavior.

## Worked example: protect a batch from a stalled receiver

This is an original simplified test plan. Four workers deliver notices. Two separate workers validate new work. The example policy bounds outbound waiting, limits retries and requires accepted work to remain recoverable; exact times and capacity must be chosen for the actual system.

| Injected condition | Observe | Acceptance requirement |
|---|---|---|
| Receiver never replies | Wait duration, occupied workers, cancellation/resource release | Waiting is bounded and capacity becomes available according to the tested contract |
| Receiver commits but reply is lost | Operation ID, receiver record and retry attempt | Reconciliation or deduplication prevents a second accepted effect |
| Dependency fails repeatedly | Breaker state, real call count and probe behavior | Policy limits further calls; state is observable; healthy recovery is tested |
| All notice workers are occupied | Validation throughput and its lower-level dependencies | The promised independent service continues within its defined limits |
| Backlog exceeds a limit | Queue state, admission decision and accepted-job identities | Apply explicit backpressure/rejection/persistence; do not silently lose accepted work |

**Backpressure** means slowing or limiting upstream admission when downstream capacity is insufficient. A bounded queue alone is not a policy: specify what happens to the work that cannot enter it.

When the receiver recovers, drain pending work using stable operation identities and reconcile outcomes. Restoring a connection is narrower than proving that every accepted work unit was processed correctly and only as intended.

## Make the test useful

1. Name the failure, affected boundary, business obligation and allowed degraded state.
2. Set explicit time/capacity/recovery criteria and record the workload and environment.
3. Inject one failure, then test relevant combinations such as overload during a dependency outage.
4. Capture returned outcomes, state, effects, resource usage and operator-visible transitions.
5. Remove the fault and demonstrate recovery, including reconciliation of pending/ambiguous work.

An isolation design may still share a database, network or CPU bottleneck. Check the actual failure domain; multiple instances do not automatically provide independent capacity. A timeout does not by itself cancel remote processing, and immediate repeated retries can amplify an outage.

**Check your understanding:** A request timed out, then the retry reported success. Was the first attempt harmless? Its outcome is unknown until receiver evidence or the operation's deduplication contract resolves it.

## Related

- [[concepts/modernization-workflow-recovery]] — persistent state, retries and compensation
- [[concepts/architectural-fitness-functions]] — objective recovery/capacity assessments
- [[concepts/canary-release-acceptance]] — limited production evidence and recovery decisions
