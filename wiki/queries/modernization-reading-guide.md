---
title: "Codex Enterprise Modernization Reading Guide"
created: 2026-10-13
updated: 2026-10-18
type: query
tags: [query, curated-list, codex, coding-agents, software-engineering, architecture, testing, reliability, security]
sources:
  - https://learning.oreilly.com/playlists/881eb67b-8276-489e-ad26-d009b8b2a34f/
  - https://learning.oreilly.com/playlists/f09ea227-8f41-450e-b79b-e9fbdbe4c597/
---

# Codex Enterprise Modernization Reading Guide

A reading guide for safely advancing code modernization of enterprise systems with Coding Agents such as Codex. The primary target language is Java; the focus is on language-independent design, verification, and operations principles, with Java/JVM- and Agent-specific knowledge covered alongside.

The goal is to decompose modernization into verifiable work and accumulate SME (business/systems expert) judgment in a reusable form, so that required interventions concentrate on unresolved items and critical exceptions while keeping the post-migration system running safely.

## Choose by reading purpose

People executing individual engagements open the **inner-loop** guide; people reusing, standardizing, and reducing the effort of *how* engagements are executed open the **outer-loop** guide. Each provides a reading order, per-book purpose, and required chapters.

| Reading situation | Markdown | O'Reilly | Scope |
|---|---|---|---|
| Learn the foundations of investigation, design and verification | [[queries/modernization-foundation-books-review]] | See author/publisher links for each item | 7 books, 2 papers |
| Investigate, change, verify and cut over an individual engagement | [[queries/modernization-inner-loop-reading]] | [inner-loop: engagement execution](https://learning.oreilly.com/playlists/881eb67b-8276-489e-ad26-d009b8b2a34f/) | 42 books, 7 categories |
| Systematize execution methods from lessons learned in engagements | [[queries/modernization-outer-loop-reading]] | [outer-loop: systematization](https://learning.oreilly.com/playlists/f09ea227-8f41-450e-b79b-e9fbdbe4c597/) | 20 items, 6 categories |

## How to use the two loops

**In the inner loop, you change and evaluate the system being migrated.** Confirm business specifications, change code and data, and accept behavior and production operation. Automated transformation and Agent use are included as practices for getting the engagement done.

**In the outer loop, you change and evaluate the *method* of executing modernization.** Design business-knowledge management, transformation recipes, Agent role division, resumable workflows, and evaluation infrastructure so they can be reused across many tasks and engagements.

Early in an engagement, read mainly the inner loop. Even mid-engagement, once you see repeated work, failures, or recurring SME questions, you can improve them with the relevant outer-loop knowledge. Limited permissions, source-backed acceptance evidence, reproducible environments, and stop conditions are required from the first engagement; consult the outer loop when you reach the stage of designing that shared foundation and operating conventions.

## Find by problem

I-xx are section numbers of the inner-loop guide/playlist, O-xx of the outer-loop guide/playlist.

| Problem | Knowledge applied within the engagement | Knowledge used for systematization |
|---|---|---|
| Decide migration targets, scope and completion criteria | I-01: value, boundaries, incremental change, decommission criteria for the legacy platform | O-06: investment, responsibility split, automation payoff |
| Foundations for understanding, design and verification | [[queries/modernization-foundation-books-review]]: seven books and two papers covering requirements/environment reasoning, evidence recovery, safe change, oracle provenance, test design, module/architecture judgment and performance | Reuse evidence maps, rule/assumption records, approved examples, design criteria and measurement procedures |
| Surface SME knowledge and the basis for "correct answers" | I-02: current-state survey, business interviews, fixing rules and expected values | O-01: managing provenance, rationale, applicability scope, freshness, and update ownership |
| Choose between automated transformation and Agents | I-01/I-03: decomposing changes, applying recipes, verifying results | O-02: recipe development and reuse, Agent roles and work contracts |
| Evaluate the correctness of changes | I-03: independent expected values, behavioral equivalence, property/contract verification | O-04: representative cases, failure analysis, regression evaluation, quality gates |
| Migrate data and external integrations safely | I-04: compatibility windows, data reconciliation, transactions, external contracts | O-03: cross-job correlation, deduplication, exception handling |
| Restricted intranet integration testing | [[queries/modernization-integration-testing]]: controllable dependencies, verified contracts, actual connectivity and business reconciliation | Reusable scenarios, dependency distribution, provider ownership and evidence from limited access windows |
| Reproduce environments and make cutover/recovery reliable | I-05: old/new environments, deployment, observability, production acceptance, recovery procedures | O-03: shared execution environment, state management, retries, approval waits, stop/resume |
| Define logging purpose, design and operation | I-03/I-05/I-06/I-07: business/diagnostic/audit logs of the target system, observability contracts, Java implementation. See [[queries/modernization-java-logging]] | O-05: execution audit trails recording Agent operations, approvals, run results, and artifact provenance |
| Check Java-specific risks | I-06: API contracts, modules, concurrency, JVM performance | O-02/O-04: turning repeated changes and checks into recipes and evaluations |
| Manage permissions and artifacts | I-07: trust boundaries, work permissions, dependencies, distribution checks | O-05: execution-infrastructure authorization, approval responsibility, audit, artifact provenance |

## How to read and how the list was selected

Reading every book cover to cover is not a prerequisite. Start from each guide's "read-first order" / "priority reading order" and consult the relevant sections according to your assigned phase and the target system's risks. When reading, convert knowledge into the artifacts the work needs: specifications, acceptance criteria, transformation recipes, recovery procedures.

Emphasize long-lived design, verification, and operations principles, supplementing with Coding Agent, structure-based automated transformation, and modern-Java material. Rework classic implementation examples and configuration values to fit the target environment. Use newer material to understand concrete tools and problems, and also check each technique's applicability conditions and verification methods.

Books listed in both loops are marked "shared", with the **reading purpose and required chapters** shown separately per loop. Even when citing the same chapters, distinguish knowledge applied to the engagement from knowledge used to design the execution method. For example, Specification by Example is read in the inner loop to agree on concrete business examples and acceptance conditions, and in the outer loop to build a system that continuously verifies and updates approved concrete examples.

Record SME judgment — specifications, concrete examples, invariants, approved exceptions — together with their provenance. As common principles for turning reading into practice: verify whether observed legacy behavior is actually business-correct, and return unresolved business decisions and critical exceptions to the people who own them.

## Related

- [[concepts/enterprise-legacy-modernization]] — overall practice and phases.
- [[concepts/legacy-behavioral-parity]] — comparing return values, state, side effects, and recovery.
- [[concepts/modernization-traceability]] — mapping provenance, decisions, specs, verification, and releases.
- [[queries/codex-enterprise-modernization-cases]] — public case studies and the limits of their evidence.
