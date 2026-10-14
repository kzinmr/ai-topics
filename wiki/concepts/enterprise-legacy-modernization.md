---
title: "Enterprise Legacy Modernization with Coding Agents"
created: 2026-10-13
updated: 2026-10-14
type: concept
tags: [concept, coding-agents, codex, enterprise-ai, software-engineering, architecture, business-process, verification, case-study]
sources:
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch03.html
  - raw/papers/2018_google_sre-workbook/canarying-releases.md
  - raw/papers/2020-04-08_google_building-secure-reliable/ch14.md
  - https://developers.openai.com/cookbook/examples/codex/code_modernization
  - https://learn.chatgpt.com/use-cases/code-migrations
  - https://aws.amazon.com/blogs/migration-and-modernization/forward-engineering-aws-transform-generated-business-requirements-with-openai-codex/
  - https://martinfowler.com/bliki/StranglerFigApplication.html
  - raw/articles/openai.com--index-virgin-atlantic--7b2d9e41.md
  - raw/articles/2025-08-29_humanlayer-advanced-context-engineering-coding-agents.md
  - raw/articles/2026-03-31_hugobowne_top-questions-about-ai-assisted-software.md
---

# Enterprise Legacy Modernization with Coding Agents

Modernization changes an established system's implementation or operating model while retaining the business obligations that still matter. Coding agents such as [[entities/codex|Codex]] can support discovery, candidate changes, testing, and documentation. The reusable unit is a **business flow with an observable contract**, including its jobs, data, integrations, and recovery behavior.

This hub connects existing engineering knowledge to enterprise modernization. Dated examples, tool attribution, reported measurements, and evidence limitations live in [[queries/codex-enterprise-modernization-cases]]. The practices below are a research synthesis, not results from an implementation performed in this repository.

## What the evidence currently supports

Public Codex examples include legacy refactoring and database migration at Virgin Atlantic, framework migration and cross-repository maintenance at Cisco/Splunk, and production engineering workflows at Rakuten and Instacart. Their detailed scope differs; an airline app, a UI framework upgrade, and a core banking migration require different evidence. See the [[queries/codex-enterprise-modernization-cases|case review]] for primary sources.

For mainframes, AWS and OpenAI published a CardDemo demonstration connecting extracted requirements to Codex-generated target services. The OpenAI COBOL cookbook provides a planning and parity workflow. Neither establishes a named customer's complete production mainframe retirement. Within the sources reviewed on 2026-10-13, that outcome remains unverified.

## Concept map

[[concepts/legacy-modernization-moc]] maps the engineering foundations from focused inner-loop reading. [[queries/modernization-inner-loop-study-notes]] records actual inspected sections; [[queries/modernization-inner-loop-sources]] separates public readability, reuse permission and archived source coverage.

| Question | Practice | Wiki route |
|---|---|---|
| What does the system actually do? | Recover entry points, dependencies, business rules, and operational exceptions | [[concepts/harness-engineering/context-engineering]] |
| Which behavior must survive? | Classify retention, intentional change, retirement, and unresolved decisions | [[concepts/modernization-traceability]] |
| How do people control the work? | Reviewable specifications and execution plans | [[concepts/spec-driven-development]] |
| How do we know the replacement is correct? | Characterization, differential testing, reconciliation, and approved exceptions | [[concepts/legacy-behavioral-parity]] |
| Can the agent execute and repair changes? | Reproducible tools, fixtures, build commands, and feedback | [[concepts/agent-harness-primitives]] |
| Who checks the implementation? | Independent checks plus accountable domain and architecture review | [[concepts/code-review]], [[concepts/security-and-governance/agent-separation-of-duties]] |
| How is execution contained? | Scoped workspaces, credentials, network access, and audit | [[concepts/security-and-governance/agent-sandboxing-patterns]] |
| How does this scale economically? | Shared workflow assets and accepted-outcome cost measurement | [[concepts/dark-factory-software-factory]], [[concepts/enterprise-ai-cost-management]] |

## Choose the modernization motion before the tool

The following selection table is a proposed decision aid, not a vendor capability matrix.

| Motion | Suitable starting condition | Useful Codex work | Main acceptance concern |
|---|---|---|---|
| Improve in place | Runtime and architecture remain viable | Tests, dead-code removal, build fixes, bounded refactors | Regression and maintainability |
| Upgrade dependencies or frameworks | Target remains structurally similar | Map API changes, update callers, repair builds | Contracts, authentication, configuration, runtime differences |
| Replatform with limited behavior change | Deployment constraints dominate | Build packaging, adapters, deployment definitions | Performance, operations, state, and licensing |
| Replace one business flow | A boundary and test oracle can be established | Recover rules, implement a module/service, compare outputs | [[concepts/legacy-behavioral-parity|Business parity]] and ownership |
| Redesign selected capabilities | Business approves changed rules or timing | Draft target specifications, data models, APIs, and migration scripts | Explicit exceptions and [[concepts/modernization-traceability|traceability]] |

Microservices are a design choice. A modular monolith or modern batch module may meet the objective with fewer distributed consistency problems. Retaining or retiring an application is also a valid portfolio decision.

## A practical delivery sequence

1. **Select a bounded pilot.** Choose a valuable flow whose owner, input/output, dependencies, and rollback path can be identified. A read-oriented daily report can be easier to isolate than a transaction spanning several ledgers; confirm this against the actual system.
2. **Reconstruct the current flow.** Inspect source alongside schedulers/JCL, copybooks, stored procedures, interfaces, schemas, and production runbooks. Mark inferred behavior separately from observed execution and owner-confirmed rules.
3. **Agree the target contract.** Record retained behavior, approved changes, data ownership, nonfunctional requirements, and unresolved decisions. Use [[concepts/spec-driven-development]] and a requirement ledger.
4. **Establish the comparison environment.** Capture an approved baseline, representative fixtures, deterministic build/test commands, and a way to execute both paths. An agent lacking the legacy runtime can draft changes but cannot demonstrate parity.
5. **Implement in checkpoints.** Ask Codex for bounded changes and evidence after each checkpoint. Keep task scope aligned with what reviewers and test infrastructure can verify.
6. **Reconcile and rehearse cutover.** Review unexplained differences, load and recovery behavior, migration reconciliation, rollback, and business acceptance before expanding traffic or batch ownership.
7. **Standardize after a successful pilot.** Version reusable instructions, tools, acceptance criteria, and environment setup; record which assumptions remain application-specific.

OpenAI's [modernization cookbook](https://developers.openai.com/cookbook/examples/codex/code_modernization) makes the pilot plan, inventory, target design, and validation documents explicit. These are useful scaffolds; the cookbook's initial modules are not a completed runnable production system.

## Incremental coexistence and data ownership

The [Strangler Fig approach](https://martinfowler.com/bliki/StranglerFigApplication.html) replaces behavior gradually while the old system continues to serve the business. OpenAI's [migration guidance](https://learn.chatgpt.com/use-cases/code-migrations) similarly uses checkpoints, compatibility options, and rollback.

For an enterprise pilot, the proposed design must answer who owns reads and writes during coexistence. Routing requests is insufficient if both paths update shared state differently. Prefer a clear writer and explicit synchronization/reconciliation; if dual writes are necessary, define failure handling and replay before adoption. Batch replacement also needs scheduler ownership, completion signals, cutoff times, and restart semantics.

Use adapters or branch-by-abstraction where a stable boundary can be introduced. Remove the temporary layer only after the replacement and rollback conditions are accepted. These are architectural applications of incremental migration, not claims that a specific case used every pattern.

Newman's *Monolith to Microservices*, Chapter 3, distinguishes perimeter interception, an internal abstraction, and parallel execution with one authoritative result. [[concepts/incremental-legacy-migration]] explains those boundaries. [[concepts/canary-release-acceptance]] adds limited active production exposure and attributable evaluation; a shadow comparison is a different source of evidence. ^[raw/papers/2018_google_sre-workbook/canarying-releases.md]

## Make the environment an engineering asset

- Put repository navigation, conventions, verified commands, and scope restrictions in AGENTS.md; keep flow-specific evidence in versioned documents.
- Supply build/runtime dependencies and permitted package sources. For disconnected environments, validate dependency availability and the actual execution arrangement rather than assuming a coding assistant is an offline system.
- Use deterministic checks for enforceable constraints. [[concepts/coding-agents/lint-rules-as-agent-feedback-loop]] explains why instructions need execution feedback.
- Keep acceptance fixtures and their expected values under an independent review boundary. A worker's own tests and self-review can share its mistaken assumptions.
- Assign owners for business rules, architecture, legacy operations, data migration, verification, and release decisions. These roles may be shared by a small team, but the decisions must remain identifiable.

The existing [[raw/articles/2025-08-29_humanlayer-advanced-context-engineering-coding-agents|HumanLayer source]] reports both successful brownfield work and a failed attempt to remove Parquet Java's Hadoop dependency. Incorrect dependency assumptions survived the research stage. This is a transferable caution from Claude Code work, not a Codex migration result.

## Measure accepted outcomes

[[concepts/architectural-fitness-functions]] makes retained design characteristics explicit alongside business acceptance. Google's *Building Secure and Reliable Systems*, Chapter 14, adds a deployment integrity requirement: connect the tested artifact to the artifact actually promoted. Source-level evidence alone does not establish that connection. ^[raw/papers/2020-04-08_google_building-secure-reliable/ch14.md]

Recommended pilot measures: time from approved scope to accepted release; engineer hours including discovery and review; first-pass acceptance and rework; unresolved parity differences; requirement disposition completeness; reconciled record/value totals; incidents and recovery time; model plus environment and human cost per accepted flow.

Record workload and baseline alongside every number. Generated lines, PR count, unit-test coverage, and source-code shrinkage do not establish business equivalence or total programme ROI. [[concepts/ai-assisted-development]] provides the broader team-measurement framing.

## Open questions

- What named, independently inspectable Codex projects have retired a production mainframe application, including data migration and operational acceptance?
- How much SME discovery and review effort remains after generation becomes faster?
- Can parity tests exercise the undocumented exceptions that actually drive operational risk?
- Which parts of the modernization workflow transfer across organizations without importing assumptions about data ownership and business policy?

## Related

- [[queries/modernization-reading-guide]] — O’Reilly reading guide: durable engineering foundations, Java, and Coding Agent evaluation
- [[queries/codex-enterprise-modernization-cases]] — evidence inventory and case-to-practice mapping
- [[concepts/legacy-behavioral-parity]] — comparison strategy and cutover evidence
- [[concepts/modernization-traceability]] — source-to-rule-to-implementation lineage
- [[concepts/codex/_index]] — other Codex workflows
