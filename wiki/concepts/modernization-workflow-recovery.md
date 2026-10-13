---
title: "Modernization Workflow Recovery"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, workflow, orchestration, durable-execution, distributed-systems, state-management, reliability, human-in-the-loop]
sources:
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch03.html
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch04.html
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch07.html
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch09.html
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch11.html
  - raw/articles/2026-10-14_unknown_temporal-workflow-docs/retry-policies.md
  - raw/articles/2026-10-14_unknown_temporal-workflow-docs/saga-pattern.md
---

# Modernization Workflow Recovery

Workflow recovery is the design of how a modernization job continues, waits, reconciles or stops after interruption. It extends [[concepts/durable-execution]] with business-effect handling and accountable handoffs. Persisting a progress flag alone does not establish that a remote operation happened exactly once.

## Handle the ambiguous outcome

Ruecker's Chapter 9 explains that retries and message redelivery create repeated calls. A service can finish an operation while the caller loses the response. Retrying from the last checkpoint can then repeat an effect the caller did not record.

For each effectful operation, decide how it will be deduplicated or reconciled. A stable operation identifier must represent the intended operation across retries. A new identifier for each attempt defeats deduplication; comparing similar business payloads can incorrectly merge two legitimate operations. The receiver must participate in enforcing the contract.

## Separate recovery decisions

This is a proposed state vocabulary for modernization jobs:

| State / condition | Next action | Evidence needed |
|---|---|---|
| Transient technical failure | Retry within explicit limits | Attempt record, stable operation identity and retry policy |
| Remote outcome unknown | Reconcile before repeating an effect | Receiver status or deduplication record |
| Verification failed | Preserve evidence; repair or stop | Failing obligation and artifact/run identity |
| Business intent unresolved | Wait for the accountable decision owner | Question, source conflict and relevant examples |
| Approval pending | Persist a human task and resume after a valid decision | Approver, approved scope and evidence version |
| Compensation required | Run the accepted recovery procedure | Completed effects and remaining obligations |

Temporal's archived retry documentation distinguishes transient/intermittent failures from permanent failures that need changed input or logic. An unlimited retry of an invalid rule is not progress. Waiting for a human decision is likewise a workflow state, not a technical error to suppress.

## Compensation has business meaning

Chapter 9's Saga discussion separates compensation from full rollback: an already delivered physical item cannot simply be made undelivered. A compensating operation can restore an acceptable business condition while leaving observable consequences.

Specify which actions can be undone, which need a replacement action, and which require manual reconciliation. Compensation can fail or be retried, so its own effect handling matters. The archived Temporal Saga example registers a compensation before an operation that can fail mid-flight and explicitly requires that compensation to tolerate repeated execution.

The outbox pattern can atomically record business state and an event-to-be-sent in one local database transaction. It does not remove the need to handle repeated delivery downstream.

## Preserve human and operational visibility

Chapter 4 treats assignment, human tasks and exceptional cases as part of process execution. Chapter 11 separates an end-to-end business process view from fine-grained distributed tracing. Sampling, missing correlation and a technical trace's granularity can leave the business outcome unclear.

Record job/flow identity, significant state transitions, attempts, effects, decisions and accepted outcomes. Tool inputs/outputs and exposed decision records can support diagnosis; full hidden model reasoning is not a prerequisite or an assumed available artifact. Coordinate evidence retention and access with [[concepts/artifact-provenance-gates]].

## Worked example: a notice committed before the timeout

The following original timeline assumes a receiver that atomically records a stable operation key and its result with the accepted effect, keeps that record for the retry horizon and rejects conflicting reuse of a key. Without those conditions, the caller cannot claim deduplication merely by attaching an ID.

| Event | Caller knowledge | Required action |
|---|---|---|
| Job `W1` sends notice operation `W1/notice` | Intent is durably recorded | Track the operation independently of attempt number |
| Receiver accepts it; its reply is lost | Outcome is unknown to the caller | Persist the ambiguous state |
| Attempt 2 uses the same key and same payload | A repeated request is possible | Receiver returns the stored result without a second effect |
| Receiver evidence confirms acceptance | Outcome can be reconciled | Mark the operation complete with that evidence |

An attempt ID such as `W1/notice/attempt-2` is useful for diagnostics but must not replace the stable operation key. A second legitimate notice needs its own operation identity. If the receiver has no suitable deduplication/status mechanism, wait for reconciliation or follow an approved manual procedure; a blind retry can duplicate the effect.

Test both the successful retry and a deliberately faulty receiver that accepts twice. The latter must fail the no-duplicate obligation. A timeout alone proves only that waiting ended. A compensating correction notice may be acceptable after an erroneous delivery, but cannot erase the fact that the first notice was seen.

## Resume under the right responsibilities and version

Chapter 3 contrasts workflow steps with local function calls: a workflow can persist a wait, but the boundary of each recorded unit of work determines what repeats. Two remote effects hidden inside one step can leave the first effect committed when the second fails. Separate responsibilities and give each effect its recovery contract.

Chapter 7 assigns services explicit business outputs and communication boundaries. In this example, the batch owns the fee decision and notification intent; the receiver owns acceptance of the notice. Do not infer delivery from a checkpoint in the batch alone.

Chapter 3's versioning discussion allows existing instances to finish on an older version or explicitly migrate them. A waiting job created under `W1` must not silently resume under incompatible `W2` code/data rules. An approval must identify the candidate, rule/evidence version and allowed action; changing these can require a new decision. Persisting the human task makes waiting possible, but does not make an old answer applicable to new evidence.

**Check your understanding:** A retry gets a new request ID, succeeds and the job completes. Is that enough to establish one notice? No. Inspect the stable operation contract and receiver evidence for both attempts.

## Related

- [[concepts/durable-execution]] — persistence and replay mechanisms
- [[concepts/modernization-traceability]] — obligations and accountable decisions
- [[concepts/modernization-evaluation-corpus]] — interruption, retry and handoff test cases
