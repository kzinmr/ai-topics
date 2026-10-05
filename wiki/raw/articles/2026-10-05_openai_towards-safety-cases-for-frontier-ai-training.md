---
title: 'Towards safety cases for frontier AI training | OpenAI'
source: 'openai'
url: 'https://openai.com/index/towards-safety-cases-for-frontier-ai-training'
date: '2026-10-05'
type: raw_article
tags: [raw, source]
fetched: '2026-10-05'
sha256: 504fe8e3eb5ead43cda9ae4e9f8ae2f4b5037fb98fbe05cdc4d47f02e40e9750
description: 'OpenAI publishes initial guidelines for safety cases for frontier RL training: technical safeguards (alignment, containment, monitoring), operational guidelines, and misalignment-incident investigation practices.'
---

OpenAI believes we are entering a new era in which structured safety documentation should be required before continuing any frontier reinforcement learning training run. Ideally such documentation would rise to the level of "safety cases" — comprehensive, structured, evidence-based arguments about risk used in other safety-critical industries (aviation, nuclear power). Safety cases are treated as an aspirational north star, while acknowledging the challenge of making them as rigorous for AI as for those industries due to emergent complexity at each new capability level. OpenAI is working on a framework to codify these practices.

The document focuses on frontier RL training; internal and external deployment require a much broader set of alignment properties.

## 1. Technical safeguards

Three aspects of the technical stack: alignment training, containment, and monitoring.

### Model alignment (first line of defense)
- **Training environments and grading**: decrease risk of misaligned behavior by preventing positive reinforcement of reward hacks during training — automated dataset reviews (agents find/fix broken RL environments that let misaligned trajectories win via exploits), manual dataset reviews, grader tuning to penalize environment-hacking, prior-run analysis (classifiers over traces to confirm graders work).
- **Alignment measurement**: run evals tracking misalignment propensities — offline alignment evals during frontier runs, backtesting evals on previous incidents (avoid overfitting to specific incidents), tracking eval-awareness/metagaming with blocking thresholds, worst-case stress tests.
- **Prevent training on chain-of-thought**: do not let automated graders see CoT in RL, to prevent models evolving to evade CoT monitors.

### Containment
Multiple layers of infrastructure security (harden sandbox + research infra hosting it for defense-in-depth against sandbox escape); containment red-teaming using checkpoints from frontier runs; limit high-bandwidth cross-sample communication to approved pathways and close side channels; immutable transcripts (write-once storage) for all RL training/eval/internal deployment.

### Monitoring
Enforce monitorability (monitorability + monitor-evasion evals with thresholds); high recall on known issues in held-out evals; eval freshness for monitors (net-new-risk datapoints); rapid response with priority alerts on a defined SLA (page on-call / auto-pause runs; auto-pause for unacknowledged night alerts).

## 2. Operational guidelines

- **Dissents (pre-mortems)**: another team writes a dissent to find holes and share a calibrated risk take.
- **Approvals**: senior leadership review with veto power (research org lead/VP, Head of Safety, Chief Scientist).
- **Accountability**: the senior leader responsible for a run is accountable for the safety case and incident response (including in performance reviews).
- **Pausing**: runbooks, technical controls, SLAs for pausing all covered runs if issues invalidate the safety case.
- **Internal transparency**: available to oversight groups (e.g., Safety and Security Committee).
- **Audits**: auditors given sufficient access to verify claims and raise gaps.
- **Escalations**: clear process with a table of misalignment severity levels and a misalignment on-call that can page executives (CEO).
- **Technical controls**: challenging to start noncompliant runs; safety features (monitoring, auto-pause) fail closed.
- **Rollback ability**: easy to identify all downstream uses of a misaligned model (data generation, grading) to undo its effect.
- **Residual risk completeness**: enumerate a comprehensive list of residual risks not covered by mitigations, for informed risk-acceptance.

These are current recommendations being implemented at OpenAI; practices will evolve.

## 3. Investigations of misalignment incidents

Best practices for investigating severe AI misalignment incidents, modeled on high-stakes-industry investigation practices (e.g., NTSB):
- **Internal transparency**: periodic (e.g., daily) updates; defined pathways for employees to get raw transcripts / sampling from misaligned models where safe.
- **Misalignment root-cause**: root-cause training dynamics (targeted ablations, resampling experiments) to understand how misaligned behaviors were introduced.
- **Postmortem**: operational and cultural postmortem of all contributing causes.
- **Detection**: develop alignment testing methods that discover the propensity to cause the incident without hillclimbing on incident-derived info; incident-derived evals as "regression tests."
- **Public disclosures**: share investigation results, postmortems, and operational changes with the public (per model misalignment reporting framework); notify affected third parties ASAP.
