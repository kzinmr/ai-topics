---
title: "Artifact Provenance Gates"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, supply-chain, security, ci-cd, verification, audit, governance, software-engineering]
sources:
  - raw/papers/2020-04-08_google_building-secure-reliable/ch05.md
  - raw/papers/2020-04-08_google_building-secure-reliable/ch14.md
  - raw/papers/2020-04-08_google_building-secure-reliable/ch15.md
---

# Artifact Provenance Gates

An artifact provenance gate makes a promotion decision using trustworthy evidence about the particular artifact being promoted. It connects [[concepts/software-supply-chain-security]] to [[concepts/modernization-traceability]]: a tested source revision is insufficient if deployment substitutes a different binary or configuration.

Google's *Building Secure and Reliable Systems*, Chapter 14, describes binary provenance, trustworthy builders, deployment policy enforcement and later verification. This page applies those mechanisms to modernization; the local record and approval rules below are proposed design choices.

## Bind evidence to identity

Chapter 14 recommends authenticated provenance identifying output artifacts, typically by content hash, and useful inputs such as source revisions, dependencies, build commands and environments. A signature establishes who asserted the provenance and protects integrity; confidence in the assertion also depends on the builder and the threat model.

```mermaid
flowchart LR
    S[Source revision and build inputs] --> B[Identified builder]
    B --> A[Artifact digest and provenance]
    A --> V[Checks and reconciliation for that artifact]
    V --> D[Policy and accountable approval]
    D --> P[Promote the identified artifact]
```

The diagram is a modernization synthesis, not the book's exact pipeline. Connect check results to fixture/environment versions as well as artifact identity. Record the recipe/configuration and relevant rule dispositions when interpreting the evidence.

| Evidence | Question answered |
|---|---|
| Source and build-input identifiers | What inputs produced this candidate? |
| Builder identity and authenticated provenance | Why trust the asserted origin? |
| Artifact digest and check-run record | Which candidate was actually checked? |
| Policy revision, decision and approver | What allowed this promotion? |
| Deployment/exception record | What actually ran, including bypasses? |

Passing checks on one digest should not authorize another digest merely because both carry the same release name. Re-evaluate approvals when relevant artifacts, inputs, accepted exceptions or policy change; do not let an old human response authorize a substituted candidate.

## Constrain the execution boundary

Chapter 5 recommends narrow functional APIs, least privilege, multi-party authorization and granular audit records. For a modernization platform, assign distinct capabilities for proposing changes, executing transformations, validating evidence and promoting a release. Apply enforcement at the action boundary, alongside explicit responsibilities.

A second model agreeing with a proposal does not itself create an independent business oracle or a trustworthy authorization boundary. The gate needs the policy, evidence and authority defined outside the candidate's own self-assessment.

## Retain and recheck

Chapter 14 also explains why deployment-time checks need later verification: policies change, enforcement may fail open, and an operator may use emergency access. Record such exceptions and evaluate already deployed artifacts under applicable policy changes.

Chapter 15 recommends structured, timestamped investigation records and logs that resist alteration, with an audit trail for alterations. It also discusses privacy constraints, so immutable logging is not a rule to preserve all sensitive payloads forever. Keep enough identity and decision evidence to investigate a transition under an explicit retention/access policy.

## Limits

Trusted provenance can faithfully describe a build of defective code. Reproducibility, trustworthy provenance, functional acceptance and authorization answer different questions. Use [[concepts/modernization-evaluation-corpus]] and the agreed acceptance contract alongside origin verification.

## Related

- [[concepts/modernization-traceability]] — requirements and decision lineage
- [[concepts/modernization-workflow-recovery]] — durable approval and exception states
- [[concepts/software-supply-chain-security]] — toolchain and dependency trust
