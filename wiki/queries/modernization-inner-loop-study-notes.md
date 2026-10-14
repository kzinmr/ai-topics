---
title: "Modernization Inner-loop — Study Notes and Reading Evidence"
created: 2026-10-14
updated: 2026-10-14
type: query
tags: [query, software-engineering, architecture, testing, reliability, verification, documentation]
sources:
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch04.html
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch13.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_016.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_018.html
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch03.html
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/05.htm
  - https://learning.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch02.html
  - https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch10.xhtml
  - https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0047.xhtml
  - raw/papers/2018_google_sre-workbook/canarying-releases.md
  - raw/papers/2020-04-08_google_building-secure-reliable/ch14.md
  - raw/papers/2026-10-14_unknown_google-art-of-slos/participant-handbook.md
---

# Modernization Inner-loop — Study Notes and Reading Evidence

This is a focused reading of the initial path in [[queries/modernization-inner-loop-reading]]. It uses authenticated O'Reilly text and licensed public originals. [[queries/modernization-inner-loop-sources]] records acquisition status for all 42 books. This page records the narrower sections actually inspected; it does not claim full-book or all-42-book completion.

## Reading selection

**Continuation, 2026-10-14:** The table below preserves the first-pass snapshot. [[queries/modernization-reading-continuation]] records deeper sections subsequently read across the 14 unique priority works; [[queries/modernization-independent-study-guide]] provides account-free concept learning. Further-reading suggestions below describe the first pass, not the final continuation's unread list.

Follow the guide's purpose order: capture existing behavior, agree business intent, choose incremental boundaries, design independent checks, protect architecture and accept production operation. The final guide step contains two books, giving seven initial titles.

Use the catalogs to choose a section, then read its relevant text. Additional JVM, integration, domain-discovery and security references remain conditional on the target system's risks. No target application or JDK migration was implemented in this reading task.

## Inspected text

| Order / material | Actual reading scope | Evidence location |
|---|---|---|
| 1. Working Effectively with Legacy Code | Chapters 4 and 13: seams/enabling points; characterization, suspicious behavior and change-focused tests | [Ch. 4](https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch04.html), [Ch. 13](https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch13.html) |
| 2. Specification by Example | Chapters 7 and 9; introductory and concluding sections of Chapters 5, 6 and 8 | [5](https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_014.html), [6](https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_015.html), [7](https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_016.html), [8](https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_017.html), [9](https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_018.html) |
| 3. Monolith to Microservices | Chapter 3: Strangler Fig overview/applicability, branch by abstraction and parallel run, including side effects | [Ch. 3](https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch03.html) |
| 4. Effective Software Testing | Chapters 2 and 4 introductions/summaries; Chapter 5 introduction, section 5.6 and summary | [2](https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/02.htm), [4](https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/04.htm), [5](https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/05.htm) |
| 5. Building Evolutionary Architectures, 2nd Edition | Chapter 2: definition, categories and outcomes versus implementations | [Ch. 2](https://learning.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch02.html) |
| 6a. Continuous Delivery | Chapter 10 introduction, rollback constraints and summary | [Ch. 10](https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch10.xhtml) |
| 6b. Release It!, 2nd Edition | Chapter 5 introduction; Timeouts, Circuit Breaker and Bulkheads introductions and concluding guidance | [Intro](https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0047.xhtml), [Timeouts](https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0048.xhtml), [Circuit Breaker](https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0049.xhtml), [Bulkheads](https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0050.xhtml) |
| Operational supplement: The Site Reliability Workbook | Chapter 4 introduction/speed/calculations; Chapter 5 alerting considerations; Chapter 16 definitions, release principles, population/metrics, monitoring requirements and related deployment methods | [[raw/papers/2018_google_sre-workbook/monitoring]], [[raw/papers/2018_google_sre-workbook/alerting-on-slos]], [[raw/papers/2018_google_sre-workbook/canarying-releases]] |
| Security supplement: Building Secure and Reliable Systems | Introductions and conclusions of Chapters 5, 6, 13, 14 and 15 | [[raw/papers/2020-04-08_google_building-secure-reliable/ch05]], [[raw/papers/2020-04-08_google_building-secure-reliable/ch06]], [[raw/papers/2020-04-08_google_building-secure-reliable/ch13]], [[raw/papers/2020-04-08_google_building-secure-reliable/ch14]], [[raw/papers/2020-04-08_google_building-secure-reliable/ch15]] |
| PDF supplement: The Art of SLOs | Participant handbook printed pages 6 and 8; original PDFs and mechanical text extraction saved. These pages were also visually checked | [[raw/papers/2026-10-14_unknown_google-art-of-slos/participant-handbook]] |

The O'Reilly reader returned loading placeholders on initial navigation. Those responses were excluded from reading evidence; the sections above were subsequently inspected after actual text appeared. No O'Reilly book/chapter text was exported to raw.

## What changes in the delivery method

### 1. Establish observations without granting them business authority

[[concepts/characterization-testing]] and [[concepts/legacy-code-seams]] make evidence collection concrete. Capture the old revision's behavior, preserve suspicious cases and exercise the paths affected by the planned change. Selecting the substitute matters as much as locating an interface.

The application rule is to retain two distinguishable records: an observation of old behavior and an approved target expectation. Changing an observation baseline during initial discovery differs from changing an accepted expectation after a candidate fails.

### 2. Keep domain meaning separate from validation mechanics

[[concepts/specification-by-example]] makes SME discussion durable through realistic examples, explicit outcomes and refinement. An example that says only that a message is sent can conceal its contents or additional downstream effects.

Automated fixtures should exercise the agreed rule without duplicating its implementation. The way a check invokes an API or prepares data can evolve while the business specification remains stable. [[concepts/modernization-traceability]] records intentional rule changes and their owner.

### 3. Choose the replacement boundary before the rollout tool

[[concepts/incremental-legacy-migration]] separates external interception, internal abstraction, parallel comparison and canary exposure. A deep internal capability may require a seam rather than a perimeter proxy. A comparison path must contain external effects without hiding the real integration it aims to verify.

Preserve explicit writer ownership, state compatibility and recovery decisions. A router reversal does not roll back data. Removing obsolete paths and dependencies is part of a retirement objective.

### 4. Give tests an independent reason to pass

Aniche's requirements-first approach complements observed baseline cases. Derive partitions, boundaries, pre/postconditions and properties from the agreed contract. [[concepts/property-based-testing]] explores those properties but is constrained by generator quality and its oracle.

A large generated suite that shares the candidate's misunderstanding is weaker than a focused set with independent expectations and representative inputs.

### 5. Measure the architecture characteristics that matter

[[concepts/architectural-fitness-functions]] turns a dependency, performance or security obligation into an explicit assessment. Select scope and cadence from risk; test important interactions when isolated checks can both pass while the combined system fails.

Architectural assessment complements business acceptance. Neither should quietly replace the other or be weakened by the implementation agent.

### 6. Accept failure handling and production evidence

*Release It!* motivates recovery-oriented design: timeouts bound waiting, circuit breakers stop repeated calls to an unhealthy dependency, and bulkheads contain resource failure. For a migration, use these principles to derive partial-failure scenarios and observable recovery criteria; counting applied patterns is not an acceptance metric.

[[concepts/canary-release-acceptance]] connects limited exposure to representative work, attributable measurements and a rehearsed recovery decision. Google supplies concrete monitoring and artifact-provenance foundations. The recommendations here are a synthesis for a future project, rather than measured results of a modernization in this repository.

## Further reading by condition

The initial reading establishes the core concept map in [[concepts/legacy-modernization-moc]]. It does not replace the guide's remaining chapter scopes.

- Data ownership/schema change: Monolith to Microservices Chapter 4, Refactoring Databases and the selected integration/data books.
- Difficult rule discovery: the I-02 requirements, domain and history-analysis references.
- Logging design: follow the separate sequence in [[queries/modernization-java-logging]], including GOOS and SRE second edition. Workbook material is not a substitute for the second edition.
- Java concurrency, modules or performance: choose I-06 references against the actual JDK and workload.
- Security boundaries and supply chain: expand the I-07 reading against the project's privileges, data and deployment path.

## Related

- [[queries/modernization-inner-loop-sources]] — 42-book availability and immutable corpus
- [[queries/modernization-inner-loop-reading]] — purposes, chapter scopes and conditional priorities
- [[concepts/legacy-modernization-moc]] — concept navigation
