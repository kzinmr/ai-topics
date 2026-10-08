---
title: "Crash-Consistent Agent: the effect-integrity gap measured for the first time"
created: 2026-10-09
updated: 2026-10-09
type: query
tags: [durable-execution, agent-evaluation, agent-memory, agent-runtime, verification, state-management]
sources:
  - raw/articles/arxiv-2610.05622-undobench-recovery-capability-tool-agents.md
  - raw/articles/arxiv-2610.05241-statewise-persistent-operational-state-repair.md
  - raw/articles/arxiv-2610.01160-retire-versioned-execution-interruptible-agents.md
  - raw/articles/earendil.com--pi-durable.md
  - raw/articles/2026-05-07_keeping-postgres-queue-healthy-planetscale.md
confidence: medium
related:
  - concepts/undobench-agent-recovery-capability
  - concepts/statewise-persistent-operational-state-repair
  - concepts/retire-versioned-execution
  - concepts/durable-execution
  - concepts/absurd-durable-execution
  - events/pi-durable-1-0
  - queries/2026-10-05-authority-converges-on-tool-call
---

# Crash-Consistent Agent: the effect-integrity gap measured for the first time

**One-liner**: UndoBench measured 83.54% nominal competence against 46.72% recovery — agent execution stacks still are not crash-consistent. In the first week of October 2026, five independent layers dug into the same hole at once.

## 1. The 83.54% / 46.72% split

[[concepts/undobench-agent-recovery-capability]] (arXiv:2610.05622) contributed, first of all, a **separated measurement of task competence vs. recovery capability**.

| Metric | Value |
|:---|:---:|
| Nominal task competence | **83.54%** |
| Conditional Recovery Success Rate (CRSR) | **46.72%** |
| Duplicate external effects fired by naive retry | **53.33%** |

36 base workflows + 36 fault scenarios across 8 enterprise domains, counterfactual paired trials under identical seeds, with wire-level effect-history oracles. 12 held-out workflows: 2 open-weight models × 2 frameworks × 3 recovery paradigms = 5,760 executions. **Commercial API models reproduced the same separation**, so it is not a weak-model artifact.

What matters is that recovery is **phase-dependent**:

| Fault point | Behaviour of recovery strategies |
|:---|:---|
| Before mutation | Strategies perform similarly; capable trials avoid duplicate effects |
| During partial mutation | Naive retry, per-call idempotency, and zero-privilege journaling **all collapse on composite workflows** |
| After commit, before acknowledgment | Verification and server-side idempotency substantially improve safety |

Prior benchmarks only ever measured the top row. Where [[concepts/agent-slop]] handles the gap between marketing and capability, UndoBench exposes a defect in the *instrument*: **no fault input was ever supplied**.

## 2. Four other lines digging the same hole at other layers

Between 2026-10-01 and 10-06, five non-overlapping layers addressed the same problem.

| Layer | Mechanism | What it protects | Numbers |
|:---|:---|:---|:---|
| Inference serving | [[concepts/retire-versioned-execution]] (arXiv:2610.01160, vLLM) | Which execution may publish output — execution *versions* own authority | Revision→successor TTFT **−17.1%** median; zero obsolete output emitted |
| Execution substrate | [[concepts/absurd-durable-execution]] (Postgres stored procedures) | Checkpoint-resume; `ctx.step()` persists each loop iteration | SDK **~1,400–1,900 lines vs Temporal ~170,000** |
| Harness | [[events/pi-durable-1-0]] (Earendil, 2026-10-01) | The conversation transcript itself is the durable object; runs anywhere a JS runtime exists (Bun, Cloudflare Durable Objects, a phone) | **~15,000 lines** — sized so the agent can read it |
| Premises (memory) | [[concepts/statewise-persistent-operational-state-repair]] (arXiv:2610.05241) | Repairs corrupted persistent records **before** an action runs | **93.3% vs 38.7%** correctness, zero unsafe actions |
| Measurement | [[concepts/undobench-agent-recovery-capability]] | Whether recovery actually works, via effect oracles | The only instrument that can prove the three above work |

Retire's abstraction is the sharpest of the set. **Requests own scheduling and memory resources; execution versions own authority** — the permission to publish output or install state. A revision becomes one atomic transition that ① **revokes** obsolete work (authority withdrawn, so it can no longer publish or install), ② **bounds** its remaining execution, and ③ **certifies the completed prefix** its successor may inherit. What "abort + resubmit" previously handled as two separate obligations — **leaking obsolete effects** and **rebuilding valid state** — collapses into one transition.

[[concepts/statewise-persistent-operational-state-repair]] moves that one level up. Reviewing the *action* is useless when the *premise* is corrupt, because a corrupted premise turns an otherwise-correct action into a wrong one. Record-level counterfactual replanning identifies which stored facts actually drive the action; current validity is established via reliability checks, read-only verification of machine-observable facts, and targeted clarification of developer-owned intent; typed evidence grounding then binds evidence to records, enabling persistent corrections with **repair lineage**. Before StateWise, action review, provenance tracking, and clarification all left **the persistent state itself uncorrected**.

The three are orthogonal, not competing:
- Retire = **which execution may publish** (inference-server layer)
- Durable Execution = **which effect may fire again** (application / DB layer)
- StateWise = **which memory may be trusted as a premise** (harness layer)
- UndoBench = **whether any of the above actually works** (evaluation layer)

## 3. Counter-evidence — swapping the substrate does not dissolve the problem

- **Moving state into Postgres does not remove the operational problem.** In Absurd's production evaluation, one task writes to up to 6 tables (Tasks / Runs / Checkpoints / Events / Wait Registrations / Idempotency Keys); a 20-step loop with 3 retries produces **26 dead tuples**. Sharing an instance with analytical queries pins the MVCC horizon — PlanetScale's benchmark reached **155,000 jobs backlog** and **300ms+** lock time in a death spiral. The default hourly cleanup cron cannot keep up at 800 jobs/sec, and the cleanup DELETE itself creates new dead tuples. "Just Postgres" delegates a deeper trade-off than SDK thinness to the operator.
- **Retire's certification is doing too much of the safety work.** The 17.1% is a median on controlled paired experiments; real-world gains depend on how often a revision inherits a valid prefix vs. needing rebuild. Certification cost on very long contexts is unverified, as is the isolation proof surface for obsolete-but-still-scheduled kernels.
- **StateWise is 150 cases** — validated across diverse runtimes, but small, and single-source (`confidence: medium`).
- **Idempotency keys are not universal.** Per-call idempotency *itself* collapsed during partial mutation in UndoBench. When the unit of the effect and the unit of the commit diverge, a key may suppress the duplicate while causing the drop instead.
- All three arXiv-backed pages are **single-source, `confidence: medium`** — independent verification pending.

## 4. Late-night verdict — "crash-consistent agent" is still an unfinished term

[[queries/2026-10-05-authority-converges-on-tool-call]] established that enforceable authority lives at the tool call. These five papers extend the same question onto the **time axis of execution**: not only which call may be issued, but **which effect may fire a second time, which prefix may be inherited, and which memory may be trusted**. All four are variants of one abstraction — an **effect-integrity ledger**. Retire's execution version, UndoBench's wire-level effect history, StateWise's repair lineage, and Absurd/Pi Durable's checkpoints name different things but point at the same missing object.

And 46.72% says that **nobody has put that ledger in production yet**. Temporal's 170k lines push the ledger into the SDK; Absurd's 1.4k lines push it into the database; Pi Durable compresses it to 15k lines so the agent itself can read it. Where the ledger belongs is still contested — but post-UndoBench, **any execution stack calling itself "durable" without empirically tested recovery is now falsifiably suspect**. This was the rare week where a benchmark measured the hole before the mechanisms filled it.

Still unresolved: which layer should own the effect ledger — inference server (Retire), database (Absurd), or harness (Pi Durable)? UndoBench's phase-dependence hints that **no single layer is sufficient**, but that decomposition has not been proposed yet.

## Related

- [[concepts/durable-execution]] — the underlying concept: checkpoint-resume and deterministic replay
- [[concepts/undobench-agent-recovery-capability]] — the instrument for recovery capability
- [[concepts/statewise-persistent-operational-state-repair]] — integrity of premises (memory)
- [[concepts/retire-versioned-execution]] — execution version as publish-authority
- [[concepts/absurd-durable-execution]] — Postgres-resident checkpointing and its MVCC limits
- [[events/pi-durable-1-0]] — durability with the harness as a library
- [[queries/2026-10-05-authority-converges-on-tool-call]] — the preceding authority-convergence analysis
- [[queries/2026-10-08-human-gate-retirement-synthesis]] — the same failure family from the human-governance side
