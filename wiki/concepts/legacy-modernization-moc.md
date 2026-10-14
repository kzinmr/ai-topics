---
title: "Legacy Modernization — Map of Concepts"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, knowledge-management, software-engineering, architecture, testing, reliability]
sources:
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch13.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_018.html
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch03.html
  - https://learning.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch02.html
  - raw/papers/2018_google_sre-workbook/canarying-releases.md
related: [concepts/characterization-testing, concepts/legacy-code-seams, concepts/specification-by-example, concepts/property-based-testing, concepts/incremental-legacy-migration, concepts/architectural-fitness-functions, concepts/canary-release-acceptance, concepts/legacy-behavioral-parity, concepts/modernization-traceability]
---

# Legacy Modernization — Map of Concepts

Navigate the foundations behind [[concepts/enterprise-legacy-modernization]]. The order follows the initial reading path in [[queries/modernization-inner-loop-reading]]: observe, agree, replace incrementally, verify, constrain and release.

## Establish evidence and intended behavior

| Concept | Use |
|---|---|
| [[concepts/characterization-testing]] | Capture actual behavior without treating it as business authority |
| [[concepts/legacy-code-seams]] | Identify substitutions and the enabling points that select them |
| [[concepts/specification-by-example]] | Agree intended outcomes using realistic, readable examples |
| [[concepts/modernization-traceability]] | Connect observations, decisions, rules and acceptance evidence |

## Change and verify

| Concept | Use |
|---|---|
| [[concepts/incremental-legacy-migration]] | Choose an interception or internal boundary and manage coexistence |
| [[concepts/legacy-behavioral-parity]] | Compare outputs, state and effects with approved exceptions |
| [[concepts/property-based-testing]] | Explore agreed properties over generated inputs |
| [[concepts/architectural-fitness-functions]] | Preserve explicit architectural characteristics during change |

## Accept production operation

| Route | Use |
|---|---|
| [[concepts/canary-release-acceptance]] | Evaluate limited real exposure with attributable signals and recovery |
| [[queries/modernization-java-logging]] | Define the target system's diagnostic, business and audit observations |
| [[queries/modernization-inner-loop-study-notes]] | Inspect the reading scope and the resulting application rules |
| [[queries/modernization-inner-loop-sources]] | Find originals, PDFs, licenses and unresolved acquisition items |

These concepts organize an evidence-based delivery method. They do not report an implemented modernization or prove that a coding agent can execute it without domain and operational judgment.
