---
title: Hillel Wayne
aliases: [buttondown-com-hillelwayne, computer-things-newsletter]
created: 2026-04-10
updated: 2026-04-19
tags:
  - person
  - blogger
  - formal-methods
  - tla+
  - software-engineering
  - empirical-research
  - testing
---


# Hillel Wayne

| | |
|---|---|
| **Blog** | [hillelwayne.com](https://hillelwayne.com) |
| **Newsletter** | [Computer Things](https://buttondown.com/hillelwayne) |
| **TLA+ Guide** | [learntla.com](https://www.learntla.com/) |
| **Projects** | [hillelwayne.com/projects](https://hillelwayne.com/projects/) |
| **Role** | Formal methods consultant, researcher, and educator |
| **Known for** | Practical TLA+, Learn TLA+, The Crossover Project, formal methods advocacy |
| **Bio** | Software engineer and researcher specializing in formal methods for businesses. Based in Chicago. Author of *Practical TLA+*, *Logic for Programmers* (in progress), and *Computer Things* newsletter. Runs the free [Learn TLA+](https://www.learntla.com/) guide. |

## Core Ideas

Hillel is a **formal methods practitioner** who bridges the gap between academic formal verification and practical software engineering. Unlike most formal methods advocates who focus purely on theory, Hillel emphasizes **accessibility, empirical evidence, and real-world applicability**. His work consistently demonstrates that formal techniques can catch critical bugs before implementation, reduce software friction, and improve system design — without requiring a PhD in mathematics.

### Formal Methods as Practical Tooling

Hillel's core thesis is that formal methods should be **usable by working developers**, not just researchers. He approaches this through multiple vectors:

- **TLA+ (Temporal Logic of Actions)** — Developed by Leslie Lamport (Turing Award winner). Hillel uses TLA+ to model and verify concurrent and distributed systems before writing code. He has written extensively on applying TLA+ to real-world problems: database migrations, message queues, goroutine concurrency, adversarial systems, and state machine composition.
- **Alloy** — A structural modeling language for software design. Hillel advocates Alloy for specification refinement and has written about common pitfalls ("Don't let Alloy facts make your specs a fiction") and the evolution of Alloy 6's temporal logic.
- **Z3/SMT Solvers** — Uses Microsoft's Z3 theorem prover for constraint solving and verification. His recent work includes practical scripts for verifying system properties.
- **MiniZinc** — Constraint modeling language for optimization problems.
- **PRISM** — Probabilistic model checking for systems with uncertainty.

### The Learn TLA+ Initiative

Hillel maintains [learntla.com](https://www.learntla.com/), a **free, comprehensive online guide** to TLA+ designed to be accessible to developers without formal mathematics backgrounds. Key design principles:

- **Progressive disclosure**: Starts with basic operators and gradually advances to temporal logic, action properties, and module systems
- **Interactive exercises**: Each lesson includes problems to solve, with show/hide answers
- **Real-world examples**: Bank transfer systems, database migrations, message queues — not abstract mathematical puzzles
- **Community maintained**: Open to contributions and corrections from readers

The guide serves as the free companion to his book *Practical TLA+*, which he explicitly notes "costs $26" and that no matter how good he makes it, "it's never going to have the reach of a free resource."

### Books & Publications

- ***Logic for Programmers*** (2026, content-complete) — A book teaching the mathematics of boolean logic and its application to programming: refactoring code, property-based testing, contracts, subtyping, formal verification, database theory, decision tables, Alloy specification, TLA+ system design, SMT solving, and logic programming. Currently in copyediting, available as beta with 20% discount.
- ***Practical TLA+*** (2018) — Comprehensive resource on TLA+ programming with rich examples. Covers operators, logic, functions, PlusCal, models, concurrency, and real-world case studies. Spiritual successor to Learn TLA+.
- ***Computer Things, 2020*** — Compilation of newsletter essays (98,000 words, 330 pages) on the history and culture of software engineering. Topics include Donald Knuth's "Literate Programming," message passing, and how learning math helps with programming.
- ***Graveyard*** — Four abandoned essays, published as a test of self-publishing.

### The Crossover Project (2019–2021)

Hillel conducted an ambitious research project to answer: **Is software engineering really engineering?** He interviewed 17 "crossovers" — people who worked professionally as both traditional engineers and software developers. Key findings published in three essays:

1. **"Are We Really Engineers?"** — 15 of 17 crossovers said yes, software development is engineering. The gap between "software craft" and "software engineering" is smaller than between "electrician" and "electrical engineer" in other fields. We are separated from engineering by *circumstance, not by essence*.
2. **"We Are Not Special"** — Comparing constraints of software work to traditional engineering, finding they're actually not that different in the end.
3. **"What Engineering Can Teach (and Learn from) Us"** — Principles of engineering that software has yet to fully adopt, and innovations software has made that could revolutionize other fields.

This work was presented at multiple conferences including GOTO Chicago (2019), Deconstruct (2019), JAX (2022), DDD Europe (2024), and QCon (2026).

### Testing Philosophy: Beyond Examples

Hillel advocates moving beyond example-based testing to more rigorous approaches:

- **Property-based testing** — Testing general properties rather than specific inputs. His essay "Finding Property Tests" provides practical guidance on discovering useful properties.
- **Metamorphic testing** — Testing relationships between inputs and outputs rather than absolute correctness. His "Metamorphic Testing" essay explores this underused technique.
- **Contract programming** — Pre/post conditions and invariants as executable specifications.
- **Cross-branch testing** — Testing behavior across different code branches systematically.
- **"Software correctness is a lot like flossing"** — Nobody does it until something goes wrong, then everyone claims they've been doing it all along.

### Software Friction & Hierarchy of Controls

Recent work focuses on practical approaches to reducing software defects:

- **"Software Friction"** (May 2024) — On the cognitive and operational costs that slow down development.
- **"The Hierarchy of Controls"** (Mar 2025) — A framework for preventing production incidents, modeled after industrial safety hierarchies: elimination, substitution, engineering controls, administrative controls, and PPE. Argues for systematic, layered approaches to preventing developers from "dropping prod."
- **"Composing TLA+ Specifications with State Machines"** (Jun 2024) — Practical techniques for building complex specifications from simpler, composable state machines.
- **"Don't let Alloy facts make your specs a fiction"** (Apr 2024) — Warning about how over-constraining specs with facts can hide real bugs by eliminating the behaviors you're trying to test.

### Developer Tooling & Workflow Automation

Hillel is deeply invested in practical tooling that improves daily developer experience:

- **AutoHotKey** — Wrote extensive guides on learning AutoHotKey by stealing his scripts. Advocates for workflow automation as a force multiplier.
- **Neovim/Lua** — Published "A Neovim Task Runner in 30 lines of Lua," demonstrating that custom tooling doesn't require complex setup.
- **Vim tricks** — Regularly shares productivity techniques for Vim users.
- **Decision tables** — Advocates using decision tables to systematically enumerate and test complex conditional logic.

### Historical & Cultural Analysis

Hillel frequently explores the history of computing to inform modern practice:

- **"Alan Kay Did Not Invent Objects"** (May 2019) — Correcting the historical record on object-oriented programming.
- **"A Very Early History of Algebraic Data Types"** (Sep 2025) — Tracing the origins of ADTs through computing history.
- **"That Time Indiana Almost Made π 3.2"** (Mar 2023) — The famous (and apocryphal) π bill story.
- **"10 Most(ly Dead) Influential Programming Languages"** (Mar 2020) — Surveying languages that shaped modern computing.
- **"Software Mimicry"** (Jul 2022) — How software patterns evolve through imitation and adaptation.

### Open Invitation & Community Engagement

Hillel maintains an **open invite** for anyone to email him with questions about:
- Empirical data on software practices
- General software history
- TLA+ and Alloy questions
- How to start with formal methods
- Essay and conference proposal review

He explicitly states: *"Don't feel like you have to trade me something if you only have questions. I'm just happy to help!"*

## Key Quotes

> *"I deeply, deeply believe in the value of interdisciplinary dialogue. If software is like engineering, then we can learn from their mistakes — and they can learn from ours."* — on The Crossover Project

> *"Software correctness is a lot like flossing. Nobody does it until something goes wrong, then everyone claims they've been doing it all along."*

> *"Don't let Alloy facts make your specs a fiction"* — on the danger of over-constraining formal specifications

> *"We are separated from engineering by circumstance, not by essence, and we can choose to bridge that gap at will."* — Are We Really Engineers?

## Related

- [[formal-methods]] — Mathematical techniques for verifying software correctness
- [[tla-plus]] — Temporal Logic of Actions, formal specification language by Leslie Lamport
- [[property-based-testing]] — Testing general properties rather than specific examples
- [[software-friction]] — Cognitive and operational costs in software development
- [[hierarchy-of-controls]] — Framework for preventing production incidents

## Sources

- [Hillel Wayne's Blog](https://hillelwayne.com) (2017–present)
- [Computer Things Newsletter](https://buttondown.com/hillelwayne)
- [Learn TLA+](https://www.learntla.com/)
- [Practical TLA+](https://www.hillelwayne.com/post/practical-tla/)
- [The Crossover Project](https://www.hillelwayne.com/tags/crossover-project/)
- [Projects Page](https://hillelwayne.com/projects/)
- [Talks](https://www.hillelwayne.com/talks/)
- [Logic for Programmers](https://leanpub.com/logic/)
