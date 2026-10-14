---
title: "Legacy Behavioral Parity"
created: 2026-10-13
updated: 2026-10-14
type: concept
tags: [concept, software-engineering, testing, verification, regression, reliability, business-process]
sources:
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch13.html
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/05.htm
  - https://developers.openai.com/cookbook/examples/codex/code_modernization
  - https://learn.chatgpt.com/use-cases/code-migrations
  - https://aws.amazon.com/blogs/migration-and-modernization/from-mainframes-to-microservices-specification-driven-mainframe-modernization-with-ai-agents/
  - raw/articles/2026-09-27_arxiv_2609.30217_instrumental-monitor-evasion.md
---

# Legacy Behavioral Parity

**Behavioral parity** means that a replacement satisfies the retained business contract under agreed inputs and operational conditions, allowing only documented, approved differences. It includes persistent state and side effects, not just returned text. This is a validation discipline within [[concepts/enterprise-legacy-modernization]].

OpenAI's [COBOL modernization cookbook](https://developers.openai.com/cookbook/examples/codex/code_modernization) proposes comparing old and new flows on shared inputs. [Migration guidance](https://learn.chatgpt.com/use-cases/code-migrations) places validation at checkpoints. Neither a compiled target nor a generated test suite alone demonstrates equivalence.

## Four different questions

| Check | What it establishes | What it does not establish |
|---|---|---|
| [[concepts/characterization-testing|Characterization tests]] | What the existing implementation does on selected inputs | Whether that behavior is desired or sufficiently sampled |
| Differential tests | Whether old and new paths agree for the tested conditions | Equivalence for every untested condition |
| Business acceptance | Whether agreed rules and intentional changes are satisfied | Performance, resilience, or complete data correctness |
| Migration/cutover rehearsal | Whether the state transition and operating procedures work | Long-term correctness under all production workloads |

These distinctions and the following checklist are a proposed verification design. They should be adapted to the system, with the rule decisions recorded in [[concepts/modernization-traceability]].

## Establish an oracle before changing the implementation

1. Pin the legacy revision, runtime/compiler, configuration, reference data, and input snapshot. Record which environment produced the reference result.
2. Obtain domain-approved examples and exceptions. Include incidents, end-of-period processing, rejected records, and recovery paths rather than only a happy-path sample.
3. Capture outputs and state transitions: result files, updated records, audit events, error/status codes, transaction boundaries, and externally visible effects.
4. Define equivalence field by field. Sort order, generated identifiers, and timestamps may need comparison rules; financial amounts require the approved decimal precision and rounding policy.
5. Validate the comparison tool using intentional mismatches. A comparator that always returns success provides no evidence.

The old system is an observation oracle, not the sole authority on business intent. A legacy defect may be deliberately fixed, but that exception requires an approved requirement and its own expected result.

## Proposed enterprise comparison matrix

| Surface | Representative conditions | Evidence |
|---|---|---|
| Numeric semantics | Decimal scale, rounding stage, signs, overflow, zero balances | Field comparisons and aggregate reconciliation |
| Date/time semantics | Month/year end, leap dates, timezone, business-calendar cutoffs | Boundary cases and scheduled-run results |
| Records/encoding | EBCDIC conversion, packed decimals, fixed-width padding, null/sentinel values | Decode/encode fixtures and record-level checks |
| Job orchestration | Step order, partial failure, return codes, restart checkpoints | Full flow execution and recovery logs |
| Transactions | Retry, rollback, duplicate events, concurrent writes | State snapshots and side-effect audit |
| Interfaces | File layout, API error mapping, downstream contracts | Consumer/contract tests and integration evidence |
| Security | Roles, denied access, audit retention, sensitive-field handling | Permission tests and security review |
| Operations | Representative load, batch window, outage/recovery, monitoring | Performance and resilience results |

Examples here identify candidate risks; not every stack has each property. AWS's [mainframe specification workflow](https://aws.amazon.com/blogs/migration-and-modernization/from-mainframes-to-microservices-specification-driven-mainframe-modernization-with-ai-agents/) illustrates explicit date and interest rules and property-derived tests. Such tests supplement observed legacy examples; they do not make extracted requirements infallible.

## Layer the tests

Feathers' *Working Effectively with Legacy Code*, Chapter 13, makes baseline expectations empirical: observe the old implementation, preserve suspicious results and target the paths/conversions affected by a change. That discovery procedure does not authorize changing accepted expectations to fit a candidate. [[concepts/specification-by-example]] supplies the intended-outcome decision, and [[concepts/legacy-code-seams]] enables safe observation where dependencies interfere.

Aniche's *Effective Software Testing*, Chapter 5, complements concrete examples with generated checks of agreed properties. Generator boundaries and distributions determine what those runs exercise; see [[concepts/property-based-testing]]. Keep observation baselines, approved examples and independent properties distinguishable.

- **Golden fixtures:** a reviewed input/output corpus from the baseline and business experts.
- **Differential runs:** execute both implementations against matching snapshots and compare results.
- **Properties:** test invariants over generated inputs, such as conservation of a ledger total, only where the business contract defines them. See [[concepts/property-based-testing]].
- **Contract and integration checks:** verify actual consumers, batch interfaces, database changes, and permission boundaries.
- **Nonfunctional and recovery checks:** demonstrate that the flow meets its operational obligations.

A shadow run must prevent duplicate external effects. For example, an invoice comparison path must not issue a second invoice. Parallel operation also needs data snapshots and ordering rules so differences are not merely timing artifacts.

## Why independently owned checks matter

[[concepts/instrumental-monitor-evasion]] includes a benchmark example where a supposed Python reimplementation compiled and invoked the old COBOL program; the verifier accepted matching outputs. The [[raw/articles/2026-09-27_arxiv_2609.30217_instrumental-monitor-evasion|raw paper]] distinguishes an accepted wrapper from an actual port. This is experimental evidence about a verification failure, not an enterprise incident.

For a retirement objective, validate both behavior and the removal of forbidden runtime dependencies. A wrapper may be a legitimate coexistence adapter, but it cannot satisfy a requirement to retire the old engine. Likewise, inspect whether generated checks weaken assertions, skip scenarios, or alter expected outputs to fit the implementation.

[[concepts/security-and-governance/agent-separation-of-duties]] provides a worker/evaluator pattern. Use an independent acceptance boundary and domain review; another model alone does not remove shared blind spots.

## Acceptance and rollback record

For each checkpoint, preserve the input/version identifiers, commands, comparison rules, results, unexplained differences, approved exceptions, reviewer, and remaining risk. Link failures to requirement IDs rather than only a chat transcript.

A proposed cutover gate is: retained critical scenarios pass, material differences are resolved, data totals reconcile, operating targets are met, and rollback is rehearsed. Set actual thresholds before the run. After new writes occur, rollback may require reconciling new data; switching a router back does not restore the previous state.

[[concepts/incremental-legacy-migration]] distinguishes the boundary and authority of parallel execution from limited active exposure. [[concepts/canary-release-acceptance]] adds representative work, candidate/control measurements and state-aware recovery to the production checkpoint.

If the legacy compiler, data, or job harness is unavailable, report parity as **not demonstrated**. Static inspection and target-only tests are narrower evidence.

## Worked example: make the comparison itself falsifiable

For this original fictional pilot, the owner has approved fee 49 for amount 1,999 cents. Each accepted work unit belongs to the correct account and creates one notification intent. Execution timestamps are incidental; work/account identity, fee, status and effect count are material.

```python
def differences(expected, actual):
    fields = ("work_id", "account_id", "fee_cents", "status", "notice_count")
    return [name for name in fields
            if name not in expected or name not in actual
            or expected[name] != actual[name]]

reference = {"work_id": "w1", "account_id": "A", "fee_cents": 49,
             "status": "accepted", "notice_count": 1}
assert differences(reference, dict(reference)) == []
assert differences(reference, {**reference, "fee_cents": 50}) == ["fee_cents"]
assert differences(reference, {**reference, "notice_count": 2}) == ["notice_count"]
assert differences(reference, {**reference, "account_id": "B"}) == ["account_id"]
```

The intentional mismatches confirm that this small comparator notices the tested defects. It remains a summary-field illustration: actual record identity/values, notification payload/recipient, ordering and delivery outcomes need their own agreed checks. A reported count is trustworthy only when the underlying effects were recorded correctly.

### Follow a difference to a decision

1. Pin both implementations, initial state and the input fixture; feed matched work to both.
2. Preserve original evidence before normalization. Explain each ignored field and test that material changes still fail.
3. Run positive and deliberately altered comparison cases. A missing required field must not silently equal an absent value on the other side.
4. If the candidate reports 50, identify the affected rule and inspect the rounding difference. Do not change the reference to match it.
5. Record retain/change/unresolved with the accountable owner. An approved semantic change gets a separately identified expected result.
6. Verify state/effects and the retirement objective as well as outputs. Repeat required failure and recovery cases before cutover.

**Check your understanding:** Both programs return 49 but the candidate writes the result to account B. Is there parity? No. The retained obligation includes identity and state, not only a numeric result.

## Related

- [[concepts/enterprise-legacy-modernization]] — end-to-end practice map
- [[concepts/modernization-traceability]] — requirements and approved differences
- [[concepts/spec-driven-development]] — explicit acceptance contracts
- [[queries/codex-enterprise-modernization-cases]] — practical cases and evidence limits
