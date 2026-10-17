---
title: "Code Modernization Foundations Reading Guide"
created: 2026-10-17
updated: 2026-10-18
type: query
tags: [query, curated-list, education, software-engineering, architecture, testing, verification, methodology, performance]
sources:
  - https://www.oscar.nierstrasz.org/oorp/
  - https://web.stanford.edu/~ouster/cgi-bin/book.php
  - https://www.informit.com/store/software-architecture-in-practice-9780136886099
  - https://www.brendangregg.com/systems-performance-2nd-edition-book.html
  - https://www.fceia.unr.edu.ar/asist/zave00.pdf
  - https://discovery.ucl.ac.uk/id/eprint/1471263/
  - https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055
  - https://www.manning.com/books/specification-by-example
  - https://www.manning.com/books/effective-software-testing
confidence: medium
---

# Code Modernization Foundations Reading Guide

Code modernization requires judgments about an existing system: what it does, what it should continue to do, which assumptions make that possible, how its structure should change, and what evidence would reveal a mistake. This guide selects seven books and two papers to develop those judgments through a small, inspectable migration exercise.

Foundation means durable reasoning that supports the choice and use of modernization techniques. General programming knowledge is assumed. Read selected sections alongside practical investigation; choose deeper coverage according to the change and the reader's responsibility. The chapter scopes and learning route below are recommendations based on the linked contents and public material.

Use [[queries/modernization-inner-loop-reading]] to apply these foundations to project execution and [[queries/modernization-outer-loop-reading]] to turn project learning into reusable methods. This guide supplies their shared conceptual preparation, including the evidence needed to evaluate changes proposed by coding agents.

## The selected resources

| Resource | Foundational question | First reading scope |
|---|---|---|
| [Four Dark Corners of Requirements Engineering](https://www.fceia.unr.edu.ar/asist/zave00.pdf) | How do desired outcomes, environment knowledge and software obligations differ? | Sections 3 and 5, with the introduction for context |
| [Object-Oriented Reengineering Patterns](https://www.oscar.nierstrasz.org/oorp/) | How can an unfamiliar system be understood through evidence? | Chapters 3-5: First Contact, Initial Understanding, Detailed Model Capture |
| [Working Effectively with Legacy Code](https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055) | How can a change be protected before the code is substantially restructured? | Chapters 2 and 4 for change preparation and seams; 11 and 13 for effects and characterization |
| [Specification by Example](https://www.manning.com/books/specification-by-example) | How do domain experts and developers agree meaningful, executable expectations? | Chapters 5-9: scope, collaboration, examples, refinement and automation |
| [The Oracle Problem in Software Testing: A Survey](https://discovery.ucl.ac.uk/id/eprint/1471263/) | What makes an expected answer credible? | Problem statement and overview of sources of oracle information |
| [Effective Software Testing](https://www.manning.com/books/effective-software-testing) | Which cases and properties can expose a wrong change? | Chapters 2-5: specification, structure, contracts and properties |
| [A Philosophy of Software Design, 2nd Edition](https://web.stanford.edu/~ouster/cgi-bin/book.php) | What makes the revised code easier to understand and change? | Complexity, module depth, information hiding and deciding what matters |
| [Software Architecture in Practice, 4th Edition](https://www.informit.com/store/software-architecture-in-practice-9780136886099) | How do quality requirements guide structural choices and tradeoffs? | Chapters 1-3; then 19-22 for design and evaluation responsibilities |
| [Systems Performance: Enterprise and the Cloud, 2nd Edition](https://www.brendangregg.com/systems-performance-2nd-edition-book.html) | How can performance differences be investigated and compared fairly? | Chapters 2 and 12; consult 3-5 for system and observation context |

## Requirements and environment reasoning

**Pamela Zave and Michael Jackson, Four Dark Corners of Requirements Engineering.** The paper distinguishes requirements expressing desired outcomes, domain knowledge describing the environment, and specifications stating implementable obligations. Its refinement argument connects the software specification and relevant domain knowledge to satisfaction of the requirement. [Paper](https://www.fceia.unr.edu.ar/asist/zave00.pdf).

For modernization, separate an observed old behavior from an approved target rule and from an assumption about another system. For example, preventing duplicate business effects may depend on a stable operation identifier and a receiver that enforces uniqueness. Record who controls each relevant action and how the environmental assumptions are supported.

**Produce:** a rule and assumption ledger with source, owner, scope and unresolved questions. **Limit:** a precise model still needs validation against the actual environment. The paper supplies a reasoning framework; investigation and accountable business decisions supply its project-specific premises.

## Recovering an existing system's structure

**Serge Demeyer, Stéphane Ducasse and Oscar Nierstrasz, Object-Oriented Reengineering Patterns.** Early reconnaissance, design hypotheses, persistent-data analysis and runtime investigation form a repeatable approach to understanding a large existing system. Chapters 3-5 progress from first contact to targeted model recovery. The [author site](https://www.oscar.nierstrasz.org/oorp/) provides the full book as a free PDF.

Investigate one business flow through code, data, execution and discussion with maintainers. Keep hypotheses separate from observations and seek evidence that could disprove the current explanation. Investigate callers, batch consumers and shared storage as well as the apparent application boundary.

**Produce:** an evidence-backed system/data map and an investigation backlog. **Limit:** older object-oriented examples require adaptation. Experimental refactoring for understanding belongs in a controlled environment; it does not automatically justify a production change. Implementation evidence establishes actual behavior rather than business authority.

## Preparing a safe change

**Michael Feathers, Working Effectively with Legacy Code.** Change preparation, seams and characterization provide a way to protect behavior when tests and documentation are weak. A seam is a point at which behavior can be substituted without editing the code at that point; the enabling point selects the behavior. Read the relevant change scenarios and dependency-breaking techniques as the investigation exposes obstacles. [Publisher contents](https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055).

Capture affected behavior at a reachable boundary before substantial restructuring. Include initial state, returned values, persistent changes and important outgoing effects. Introduce the smallest necessary seam when a dependency prevents observation or controlled execution.

**Produce:** a reproducible baseline and a bounded change that can be checked against it. **Limit:** characterization records selected old behavior, including defects. Resolve desired changes separately and retain the observation as evidence. See [[concepts/characterization-testing]] and [[concepts/legacy-code-seams]].

## Agreeing intended behavior through examples

**Gojko Adzic, Specification by Example.** Collaborative examples connect scope and business goals to shared expectations and automated acceptance. Chapters 5-9 cover the progression from choosing what matters to expressing and automating useful examples. [Publisher overview](https://www.manning.com/books/specification-by-example).

Bring domain experts, developers and testers together around realistic normal cases, boundaries and exceptions. Distinguish a required business sequence from incidental interaction steps. For a disputed legacy behavior, document whether it will be retained, changed, retired or left unresolved, together with the responsible decision maker.

**Produce:** readable acceptance examples linked to decisions and an automation adapter that consumes them. **Limit:** agreement can still be incomplete or factually mistaken. Check examples against system evidence and real data characteristics; keep expectation ownership explicit through [[concepts/modernization-traceability]].

## Establishing the source of expected answers

**Earl T. Barr, Mark Harman, Phil McMinn, Muzammil Shahbaz and Shin Yoo, The Oracle Problem in Software Testing: A Survey.** A test oracle determines whether observed behavior is correct. The survey frames this problem and discusses sources of oracle information including specifications, models, metamorphic relations and human knowledge. [Institutional record and abstract](https://discovery.ucl.ac.uk/id/eprint/1471263/).

Identify the basis for each important expectation: an approved rule, an observed old execution, an independent model, a justified property or a verified external contract. Record its assumptions and the cases it cannot judge. Agreement between a candidate and tests derived from that same candidate is weak evidence of independent correctness.

**Produce:** an expectation record with provenance, authority, applicability and uncertainty. **Limit:** an old-system oracle can preserve a defect, a model can be wrong, and a property can be too weak. The survey supplies a map of the problem, rather than a project-specific decision about the right behavior.

## Designing checks that distinguish faults

**Maurício Aniche, Effective Software Testing.** Specification-based cases, boundaries, structural knowledge, explicit contracts and property-based testing complement one another. Chapters 2-5 supply a systematic route from the intended behavior to checks capable of exposing errors. [Publisher overview](https://www.manning.com/books/effective-software-testing).

Partition the relevant input space, test meaningful boundaries and specify state changes and external effects. Use code inspection to find overlooked paths while preserving independently justified expectations. Challenge important checks with plausible faults, such as a wrong identifier, an omitted rejection or an extra notification.

**Produce:** a test portfolio tied to risks and contracts, including evidence that selected faults are detected. **Limit:** line coverage and mutation scores describe particular observations rather than complete correctness. Property generators and distributions constrain the cases explored. See [[concepts/specification-based-test-design]] and [[concepts/legacy-behavioral-parity]].

## Judging module design

**John Ousterhout, A Philosophy of Software Design, 2nd Edition.** Complexity, module depth and information hiding offer criteria for judging the direction of a structural change. The second edition emphasizes general-purpose modules and deciding what matters. [Author's edition notes](https://web.stanford.edu/~ouster/cgi-bin/book.php).

Compare alternative interfaces for the same behavioral obligation. Ask what callers must know, which decisions stay inside the component, and how much neighboring implementation must be read to make a change. Evaluate whether an extraction reduces the knowledge a maintainer must hold at once.

**Produce:** a comparison of two candidate module designs and the reason for choosing one. **Limit:** module depth is a heuristic rather than a universal class-size rule. Assess the interface and its responsibilities in context, preserving the accepted behavioral contract during refactoring.

## Choosing and evaluating architecture

**Len Bass, Paul Clements and Rick Kazman, Software Architecture in Practice, 4th Edition.** Quality-attribute scenarios and tactics connect requirements to structure. Architecturally significant requirements, attribute-driven design, evaluation and documentation help make tradeoffs inspectable. [Publisher contents](https://www.informit.com/store/software-architecture-in-practice-9780136886099).

State important scenarios in terms of a stimulus, operating conditions and a measurable response. Compare candidate structures against several scenarios, including modifiability, availability and performance where relevant. Use a lightweight evaluation for a small change and deeper analysis for consequential structural decisions.

**Produce:** quality scenarios and an architecture decision record containing alternatives, assumptions, risks and rationale. **Limit:** the depth of evaluation should match the decision. Convert suitable accepted constraints into [[concepts/architectural-fitness-functions]]; automation depends on selecting the right constraints first.

## Investigating and accepting performance

**Brendan Gregg, Systems Performance: Enterprise and the Cloud, 2nd Edition.** Methodology and benchmarking connect application behavior to operating-system, kernel and hardware performance. Read Chapter 2 for investigation methods and Chapter 12 for benchmarking; use the remaining chapters to follow the evidence across layers. [Author's book page](https://www.brendangregg.com/systems-performance-2nd-edition-book.html).

Define representative work, data volume, concurrency and measurement conditions. Distinguish CPU work, waiting and resource saturation before tuning. Compare old and new systems under controlled conditions and verify that completed work, rejected work and business effects retain their intended meaning.

**Produce:** a repeatable workload, measurement procedure, performance comparison and supported bottleneck hypothesis. **Limit:** Linux is the main concrete platform, and tooling depends on access and privileges. Faster execution caused by missing work is a correctness failure. Use agreed quality scenarios to set the actual acceptance thresholds.

## Reading route through one small change

1. **Establish the boundary and premises.** Read the requirements paper with the early reengineering chapters. Map one business flow and separate desired outcomes, observations and assumptions.
2. **Observe and agree.** Use Feathers to capture behavior safely and Specification by Example to resolve intended outcomes. Use the oracle paper to scrutinize the sources of expected answers.
3. **Compare designs.** Apply Ousterhout's criteria to candidate modules and the relevant architecture scenarios to larger structural choices. Preserve the baseline while experimenting.
4. **Make checks discriminating.** Use Aniche to derive cases, boundaries and properties. Include state, external effects and the failure paths affected by the proposed change.
5. **Compare operational behavior.** Use Gregg's methodology to investigate representative load and performance. Revisit architectural assumptions when measurements or failure tests contradict them.

Reading and investigation should inform each other. Unknown behavior can require more observation; a disputed rule needs a decision; a failing check can expose an incorrect assumption. Select deeper architecture and performance chapters as those responsibilities enter the change. The learning outcome is the ability to explain and challenge a decision with evidence.

## Integrated learning exercise

Use a fictional nightly inventory export. The old job reads 10,000 records, exports 9,980 and rejects 20. A replacement must preserve the approved business contract while removing a legacy runtime dependency. The observations alone do not establish which rejection rules should remain.

- Trace one normal record and the rejected cases through input decoding, storage and downstream consumption. Record the dependency map and unknowns.
- Establish which outcomes are required, which behaviors are incidental and which environmental assumptions support delivery. Obtain an explicit decision on the rejection policy.
- Capture the old revision, input snapshot, initial state, outputs, rejection evidence and outgoing effects. Assign a source and owner to each target expectation.
- Compare two component boundaries and the relevant quality scenarios before choosing a structure.
- Check identity, values, accepted/rejected outcomes and duplicate delivery during retry. Introduce a wrong identifier, missing rejection and extra outgoing effect to challenge the checks.
- Compare performance under the same representative workload. A faster run that silently drops the 20 rejected records fails an approved requirement to retain rejection evidence.
- Verify removal of the old runtime dependency separately from behavioral comparison, and document the remaining integration and recovery evidence needed for release.

**Completion evidence:** an evidence-backed system map, a rule/assumption ledger, approved examples, a design rationale, discriminating checks and a reproducible performance comparison. These exercise artifacts prepare the reader for project acceptance; production work also needs actual environment access, accountable owners and cutover/recovery validation.

## Related

- [[queries/modernization-reading-guide]] — navigation across foundations, project execution and reusable methods
- [[concepts/legacy-modernization-moc]] — concept map and supporting explanations
- [[concepts/modernization-traceability]] — connect evidence, decisions, rules and runs
- [[queries/modernization-integration-testing]] — contracts and real integration evidence under access constraints
- [[concepts/modernization-workflow-recovery]] — retries, uncertain effects and recovery responsibilities
