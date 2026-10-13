---
title: "Codex Enterprise Modernization: Cases and Practice Review"
created: 2026-10-13
updated: 2026-10-13
type: query
tags: [query, codex, enterprise-ai, software-engineering, case-study, methodology, verification, architecture]
sources:
  - raw/articles/openai.com--index-virgin-atlantic--7b2d9e41.md
  - raw/articles/2025-08-29_humanlayer-advanced-context-engineering-coding-agents.md
  - raw/articles/2026-03-31_hugobowne_top-questions-about-ai-assisted-software.md
  - raw/articles/2026-09-27_arxiv_2609.30217_instrumental-monitor-evasion.md
  - https://openai.com/index/virgin-atlantic/
  - https://openai.com/index/cisco/
  - https://openai.com/index/rakuten/
  - https://openai.com/index/codex-now-generally-available/
  - https://developers.openai.com/cookbook/examples/codex/code_modernization
  - https://aws.amazon.com/blogs/migration-and-modernization/forward-engineering-aws-transform-generated-business-requirements-with-openai-codex/
  - https://aws.amazon.com/blogs/migration-and-modernization/from-mainframes-to-microservices-specification-driven-mainframe-modernization-with-ai-agents/
  - https://www.infosys.com/services/data-ai-topaz/offerings/accelerating-ai-value.html
  - https://blogs.infosys.com/topaz/openai/infosys-and-openai-from-ai-pilots-to-production-results.html
  - https://developers.openai.com/cookbook/examples/agents_sdk/sandboxed-code-migration/sandboxed_code_migration_agent
  - https://learn.chatgpt.com/use-cases/code-migrations
  - https://martinfowler.com/bliki/StranglerFigApplication.html
---

# Codex Enterprise Modernization: Cases and Practice Review

**Research cutoff: 2026-10-13.** Question: which public practices make Codex useful for modernizing enterprise legacy business systems, and how should the wiki connect them?

The strongest concrete Codex evidence found concerns bounded refactoring, framework migration, cross-repository engineering, and maintenance. Mainframe-specific publications add a useful specification-to-implementation method, but the reviewed examples do not demonstrate a named customer's complete production mainframe retirement. Use [[concepts/enterprise-legacy-modernization]] as the navigation hub; [[concepts/legacy-behavioral-parity]] and [[concepts/modernization-traceability]] cover its two critical acceptance disciplines.

## Repository-first research and selection

Started with SCHEMA.md and index.md, then searched Layer 2 pages and raw articles for Codex, modernization, COBOL, legacy systems, and migration. Read the Codex entity's cases and the existing specifications, context, harness, review, factory, and cost material. The Virgin Atlantic raw article provided a directly relevant enterprise starting point.

Consulted raw material behind related practices, particularly HumanLayer's brownfield report, the AI-assisted-development practitioner FAQ, and the monitor-evasion paper's COBOL example. Supplemented gaps with opened primary pages from OpenAI, AWS, Infosys, and Martin Fowler. This is a targeted qualitative synthesis, not a complete census of the repository or the market.

Two Factory raw articles (`2026-05-10_factory_legacy-bench.md` and `2026-09-25_factory_legacy-bench-specialized-intelligence-index.md`) contain mostly title/navigation text. They were insufficient to support quantitative legacy-language capability claims. General model leaderboards, partnership announcements, prototypes, and scientific rewrites were not treated as production business-system migration evidence.

## How to read the evidence

| Class | Meaning | Interpretation |
|---|---|---|
| Named enterprise experience | A customer and workflow are identified | Relevant adoption evidence; published metrics remain self-reported |
| Anonymous experience | A workflow is described without an identified customer | Useful pattern; limited independent inspectability |
| Demonstration or cookbook | A sample system or instructional workflow | Method evidence; no implied customer production cutover |
| Adjacent evidence | Another model/tool or transferable engineering experience | Keep tool attribution explicit |

Most enterprise entries below are vendor-published customer accounts, not controlled experiments. No common baseline supports averaging their speedup figures.

## Named Codex enterprise experiences

| Case and publication | Actual scope and reported outcome | Transferable practice and boundary |
|---|---|---|
| [Virgin Atlantic](https://openai.com/index/virgin-atlantic/), 2026-05-22 | Legacy refactors reported 78–80% code shrinkage and selected two-week tasks taking 30–60 minutes. Revamped mobile app had near-complete unit-test coverage and zero P1 tickets at launch; database migrations to the core warehouse were also assisted. | Put tests and launch quality alongside speed. Code shrinkage and app launch quality are different measurements; neither proves airline-wide core-system replacement. Raw starting point: [[raw/articles/openai.com--index-virgin-atlantic--7b2d9e41]]. |
| [Cisco / Splunk](https://openai.com/index/cisco/), 2026-05-27 | React 18→19 UI migrations compressed weeks to days. Analysis across 15+ repositories reduced build times about 20%, with 1,500+ engineering hours saved monthly; C/C++ defect repair reported 10–15× throughput. | Reviewable plans, dependency analysis, and compile/test/fix execution fit established repositories. These are distinct workloads, not a measured end-to-end mainframe conversion. |
| [Rakuten](https://openai.com/index/rakuten/), 2026-03-11 | Codex supports KQL-based incident diagnosis, CI/CD review and vulnerability checks. Reported MTTR improvement is approximately 50%. A web agent service's mobile version used FastAPI and Swift/SwiftUI, with a quarter-long project compressed to weeks. | Integrate internal standards and runtime feedback into delivery. Recovery improvement and a new mobile implementation support adoption; they are not legacy-core retirement evidence. |
| [Instacart / Olive](https://openai.com/index/codex-now-generally-available/), 2025-10-06 | Codex SDK integrated into a background coding platform, using remote development environments to edit and test changes, remove dead code and expired experiments, and handle well-understood repetitive work. | A continuous maintenance backlog is an entry point before broader replacement. The account publishes no modernization-wide cost or cutover measurement. |

The most direct named migration example here is Cisco/Splunk's framework upgrade. Virgin Atlantic supplies the closest existing repository evidence for legacy refactoring and business data migration. Rakuten and Instacart broaden the operational pattern.

## Mainframe and anonymous migration evidence

| Source | Scope | What can be concluded |
|---|---|---|
| [OpenAI code-modernization cookbook](https://developers.openai.com/cookbook/examples/codex/code_modernization), 2025-11-19: COBOL pilot | Investment-portfolio reporting example with execution plan, inventory, target design, API contract, and parity validation artifacts | A repeatable pilot method. Initial modules still need wiring to run; no named customer's production deployment is established. |
| Same cookbook: anonymous monorepo customer | Hundreds of Jira tickets supplied to Codex, with risk/dependency analysis, candidate changes, and a separate validator reviewing/merging | A backlog-to-checkpoint pattern; customer identity, target stack, programme duration, and quantitative outcomes are unspecified. |
| [AWS Transform + Codex](https://aws.amazon.com/blogs/migration-and-modernization/forward-engineering-aws-transform-generated-business-requirements-with-openai-codex/), 2026-09-21 | CardDemo sample: roughly 1,000 requirements across eight functions; Java/Spring Boot, PostgreSQL, API/event contracts, tests, and CDK assets generated after review | A concrete mainframe forward-engineering demonstration. Reported infrastructure/test repair is useful method evidence, not proof of customer production cutover or a general benchmark. |

The preceding [AWS specification article](https://aws.amazon.com/blogs/migration-and-modernization/from-mainframes-to-microservices-specification-driven-mainframe-modernization-with-ai-agents/) (2026-08-19) uses **Kiro**. It supports the requirements-recovery and domain-boundary method; keep its execution results separate from the later Codex example.

## Adjacent cases and attribution traps

**Infosys retail COBOL modernization:** the [Infosys/OpenAI offering page](https://www.infosys.com/services/data-ai-topaz/offerings/accelerating-ai-value.html) attributes 25–30% effort savings to **GPT-4o plus Infosys iLEAD**, for a department-store chain. The opened [Infosys partnership blog](https://blogs.infosys.com/topaz/openai/infosys-and-openai-from-ai-pilots-to-production-results.html) also reports the anonymous retailer's cloud modernization using GPT models and iLEAD. It mentions Codex in the partnership, but does not establish Codex as the tool responsible for that reduction. Publication dates were not clearly exposed on these pages; accessed 2026-10-13. The offering page's direct open failed, so its finer model attribution rests on the primary search extract; the opened blog confirms only GPT models.

**HumanLayer brownfield work, 2025-08-29:** the existing [[raw/articles/2025-08-29_humanlayer-advanced-context-engineering-coding-agents|source]] describes Claude Code work on BAML and a failed Parquet Java/Hadoop dependency removal. Discovery, planning, and expert participation are transferable; its positive figures are not Codex measurements. The failure is especially relevant to undocumented transitive dependencies.

**Agents SDK sandbox migration, 2026-04-07:** the [OpenAI cookbook](https://developers.openai.com/cookbook/examples/agents_sdk/sandboxed-code-migration/sandboxed_code_migration_agent) demonstrates a host-owned harness, scoped sandboxes, baseline tests, returned patches, and audit records on fixture repositories. It is an Agents SDK example, not a named enterprise Codex deployment. Compare with [[concepts/security-and-governance/agent-sandboxing-patterns]], which describes a different boundary: isolating the whole agent. Select the boundary deliberately.

## Case-to-practice synthesis

| Practice | Supporting evidence | Wiki connection |
|---|---|---|
| Start with one business flow and a reviewable plan | COBOL cookbook; anonymous backlog; Cisco's planning practice | [[concepts/spec-driven-development]] |
| Recover rules before committing to the target design | AWS requirements workflow; HumanLayer's discovery failure | [[concepts/modernization-traceability]] |
| Separate observed behavior from approved changes | Mainframe requirement layering; migration checkpoints | [[concepts/legacy-behavioral-parity]] |
| Give the agent real execution feedback | Cisco builds/repairs; SDK sandbox baseline; existing lint practice | [[concepts/agent-harness-primitives]], [[concepts/coding-agents/lint-rules-as-agent-feedback-loop]] |
| Keep independent acceptance evidence | Anonymous validator; COBOL wrapper verification failure in the raw paper | [[concepts/security-and-governance/agent-separation-of-duties]], [[concepts/instrumental-monitor-evasion]] |
| Modernize incrementally with explicit ownership | [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html); [OpenAI migration guidance](https://learn.chatgpt.com/use-cases/code-migrations) | [[concepts/enterprise-legacy-modernization]] |
| Measure the complete delivery flow | Airline delivery bottlenecks; existing practitioner measurement/cost material | [[concepts/ai-assisted-development]], [[concepts/enterprise-ai-cost-management]] |

## Proposed first pilot for a legacy business system

This is a recommendation derived from the synthesis, not a duration or cost promise.

Choose one representative flow with a known owner and repeatable baseline. For example, a daily report consuming a fixed input snapshot may offer a manageable first boundary. Include its real upstream/downstream dependencies before judging it low risk.

| Review point | Required artifact | Decision |
|---|---|---|
| Discovery | Inventory, job/data flow, rule ledger, uncertainty list | Can the team explain the current flow and obtain missing evidence? |
| Design | Retention/change decisions, contracts, data ownership, execution plan | Does the target meet the business objective without hidden policy changes? |
| Implementation | Bounded patch, build results, fixture and rule references | Does it satisfy the agreed contract under independent checks? |
| Cutover rehearsal | Differential results, reconciliation, load/recovery results, rollback record | Is it acceptable to transfer this flow's operational ownership? |
| Expansion | Reusable assets, acceptance/rework data, total cost per accepted flow | Is another similar flow justified? |

An effective initial Codex task can ask it to map the flow, cite source locations, identify one bounded boundary, and list what cannot be inferred. Follow with specification and acceptance work; only then ask for implementation against the agreed contract. SME decisions stay explicit.

## Remaining research gaps

- Named Codex COBOL/PL/I projects with independently inspectable reconciliation, production cutover, and decommissioning evidence.
- Legacy business-platform specifics: SAP/ABAP, Oracle Forms/PL/SQL, proprietary job schedulers, and vendor-runtime dependencies. This review establishes no tool-specific success rates for them.
- Comparative effort including SME interviews, harness setup, data cleanup, review, migration, and long-term maintenance.
- Independent verification of vendor-reported gains and unsuccessful enterprise pilots, not only successful selected tasks.

## Validation of this research artifact

The deliverable is a documentation synthesis. No legacy application was converted or executed. Wiki frontmatter, taxonomy, new-page links, source references, index entries, and preservation of existing/raw content are checked as part of this edit; application parity and production readiness remain outside that validation.
