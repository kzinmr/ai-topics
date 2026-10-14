---
title: "Modernization — Priority Reading Continuation"
created: 2026-10-14
updated: 2026-10-14
type: query
tags: [query, documentation, software-engineering, testing, verification, methodology]
sources:
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch02.html
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch11.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_014.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_015.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_017.html
  - https://learning.oreilly.com/library/view/specification-by-example/9781617290084/kindle_split_019.html
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch02.html
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch04.html
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/02.htm
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/03.htm
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/04.htm
  - https://learning.oreilly.com/library/view/effective-software-testing/9781633439931/OEBPS/Text/05.htm
  - https://learning.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch03.html
  - https://learning.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch08.html
  - https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch05.xhtml
  - https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch12.xhtml
  - https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0048.xhtml
  - https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0049.xhtml
  - https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/f_0050.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch02.xhtml
  - https://learning.oreilly.com/library/view/living-documentation-continuous/9780134689418/ch05.xhtml
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_4.xhtml
  - https://learning.oreilly.com/library/view/automated-code-refactoring/9781808347832/Text/Chapter_6.xhtml
  - https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/ch04.html
  - https://learning.oreilly.com/library/view/ai-for-mass-scale/9781098175849/ch05.html
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch03.html
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch07.html
  - https://learning.oreilly.com/library/view/ai-engineering/9781098166298/ch04.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch05.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch09.html
  - raw/papers/2020-04-08_google_building-secure-reliable/ch13.md
  - raw/papers/2020-04-08_google_building-secure-reliable/ch14.md
---

# Modernization — Priority Reading Continuation

The user confirmed the **14 unique priority works** across the two guides on 2026-10-14. Specification by Example appears in both paths and is counted once. This continuation follows the existing purpose order: first the inner-loop foundations, then the outer-loop reusable delivery method. It adds reading beyond the first focused passes in [[queries/modernization-inner-loop-study-notes]] and [[queries/modernization-outer-loop-study-notes]].

The unit of completion here is independent comprehension of the selected modernization concepts and decision procedures. This is selected-section reading across all 14 works, **not cover-to-cover completion of 14 books**, completion of every chapter designated in the larger guides, or reproduction of their contents. Commercial text was read in the authenticated O'Reilly reader and used for original synthesis; it was not exported into raw. Google's licensed original was read from the existing archive.

## Additional reading actually performed

Each row describes new inspection in this continuation. Earlier reading remains documented in the two first-pass records; a chapter number alone does not mean its whole text was read.

| Work, in purpose order | Newly inspected text | Resulting application |
|---|---|---|
| 1. Working Effectively with Legacy Code | Ch. 2 change algorithm; Ch. 11 reasoning-about-effects opening and mutable-alias example | Separate preparatory dependency changes; follow effects beyond the edited method |
| 2. Specification by Example | Ch. 5 goal/scope and why/who discussion; Ch. 6 workshop models/preparation opening; Ch. 8 refining precise examples; Ch. 10 unreliability and managing failing regression checks | Distinguish a requested solution from the goal; keep business meaning visible and known failures accountable |
| 3. Monolith to Microservices | Ch. 2 understanding the goal; Ch. 4 ownership transfer, application-synchronization stages and Saga-failure introduction | Control writer ownership, catch up state before switching and preserve committed effects during recovery |
| 4. Effective Software Testing | Ch. 2 partitions 2.1.3, boundaries 2.1.4 and combinations 2.4.6; Ch. 3 structural-only limits 3.9 and mutation testing 3.11; Ch. 4 pre/postconditions and input-validation opening; Ch. 5 property derivation/generation and stateful Basket opening | Derive cases from a contract; distinguish executed code from effective assertions; define property domains |
| 5. Building Evolutionary Architectures, 2nd Edition | Ch. 3 incremental-change opening and deployment pipelines; Ch. 8 inappropriate governance | Put selected fitness checks at useful pipeline stages; choose controls from outcomes and coupling risks |
| 6. Continuous Delivery | Ch. 5 pipeline definition/build binaries once; Ch. 12 incremental database changes and rollback without losing new transactions | Bind evidence to the promoted artifact and test data-preserving recovery |
| 7. Release It!, 2nd Edition | Complete Ch. 5 subsection pages: Timeouts, Circuit Breaker and Bulkheads | Explain states, bounded waiting, capacity isolation, remaining failure domains and recovery tests |
| 8. Living Documentation | Ch. 2 BDD collaboration/reconciliation discussion; Ch. 5 living/dynamic curation and guided-tour opening | Check the specification-to-test connection and organize views around readers' tasks |
| 9. Automated Code Refactoring and Modernization with OpenRewrite | Ch. 4 recipe composition and mixing text/typed-recipe pitfalls; Ch. 6 cursor-hierarchy opening and actual common-pitfalls discussion | Verify composition, positive/negative contexts, attribution and unsupported cases |
| 10. AI for Mass-Scale Code Refactoring and Analysis | Ch. 4 four-use-case introduction, ASSIST opening, DIAGNOSE solution and BUILD discussion; complete short Ch. 5 | Separate AI outputs by purpose and review their trust/cost assumptions; vendor examples remain historical claims |
| 11. Practical Process Automation | Ch. 3 model/code, persistent work units and process versioning; Ch. 7 responsibility boundaries, process-monolith warning and crossing-boundaries API discussion | Separate effects/checkpoints, receiver responsibility, instance versions and approval scope |
| 12. AI Engineering | Ch. 4 scoring rubrics/examples, business-metric relationship and evaluation-pipeline evaluation/iteration | Review the evaluator's signal, variability and context instead of treating its score as business success |
| 13. Evals for AI Engineers | Ch. 5 imperfect-judge correction, denominator limits, bootstrap explanation and common pitfalls; Ch. 9 CI/regression distinction, CI mistakes and judge drift | Separate curated regression from production sampling; make judge errors and transferred-rate assumptions explicit |
| 14. Building Secure and Reliable Systems | Ch. 13 unit-test effectiveness, mutation-testing discussion, test doubles, correctness validation and integration testing; Ch. 14 provenance fields and code-signing limits | Give tests independent obligations and bind origin/check/authorization evidence to the actual artifact |

OpenRewrite Ch. 6 initially returned a temporary not-found page; it was reloaded and actual chapter text was subsequently inspected. That failed response is not counted as reading. Chapter introductions that repeat a section heading were not substituted for the later section body. The imperfect-judge shipping sidebar was not reliably extracted and is not claimed as read.

## What the deeper reading changed

- Added [[concepts/specification-based-test-design]] and [[concepts/resilience-acceptance-testing]] as reusable foundations central to their sources, rather than hiding them inside a generic testing page.
- Expanded 14 core concept pages with original worked examples, explicit limits and comprehension questions with answers. The fee batch, recipe rename, judge matrix and artifact identifiers are invented teaching examples, not book case studies or production measurements.
- Added [an account-free study route](modernization-independent-study-guide.md), [an integrated exercise](modernization-batch-example.md) and [the review record](modernization-independent-reading-review.md).

## Coverage boundary

These pages explain how to apply the selected concepts without following an essential explanation through an O'Reilly link. They assume basic programming, test and data-processing familiarity. They do not teach an entire language/framework, establish a production design or replace the books' broader argument, exercises and specialist chapters.

Full public text remains unverified for the commercial priority works. The existing source registers and GitHub Wiki comments preserve those gaps; this reading does not reclassify a subscription page as a public original. Additional full books are conditional on the actual application, as the original guides specify. Implementing an OpenRewrite recipe, migrating a live schema or selecting operational thresholds still requires project-specific evidence and current tool documentation.

## Related

- [[queries/modernization-independent-study-guide]] — learn the selected concepts with repository content
- [[queries/modernization-independent-reading-review]] — criteria, findings and verification
- [[queries/modernization-inner-loop-reading]] — original selection and conditional chapter scopes
- [[queries/modernization-outer-loop-reading]] — original reusable-method sequence
