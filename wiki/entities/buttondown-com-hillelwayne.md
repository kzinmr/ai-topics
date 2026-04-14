---
title: Hillel Wayne (Buttondown Newsletter)
created: 2026-04-10
updated: 2026-04-10
tags:
- person
- blogger
- newsletter
- formal-methods
- tla+
- software-engineering
- empirical-research
aliases:
- buttondown.com/hillelwayne
- hillel-wayne-buttondown
- computer-things
---

# Hillel Wayne's Buttondown Newsletter

| | |
|---|---|
| **Newsletter** | [Computer Things](https://buttondown.com/hillelwayne) |
| **Blog** | [hillelwayne.com](https://hillelwayne.com) |
| **TLA+ Guide** | [learntla.com](https://www.learntla.com/) |
| **Role** | Formal methods consultant, researcher, and educator |
| **Known for** | Computer Things newsletter, Practical TLA+, The Crossover Project, formal methods advocacy |
| **Bio** | Hillel Wayne's Buttondown newsletter, *Computer Things*, is a long-running publication that bridges formal methods research with practical software engineering. While his main blog covers similar ground, the newsletter format allows for essay-length explorations of formal verification, testing methodology, software history, and developer productivity — published on a regular cadence to a dedicated subscriber base. For a comprehensive treatment of Hillel's work, see [[entities/hillel-wayne]]. |

## Core Ideas

The **Computer Things** newsletter (hosted on Buttondown) is Hillel Wayne's primary vehicle for **disseminating formal methods thinking to a practitioner audience**. It extends beyond his main blog by providing:

### Regular Deep-Dive Essays on Formal Verification

The newsletter serves as a **serial publication of formal methods tutorials and case studies**, covering:

- **TLA+ specifications for real-world systems**: Each issue often includes a worked example — modeling a database migration, a message queue, or a concurrent data structure in TLA+. The newsletter's format allows Hillel to build complexity incrementally, something that blog posts can't always accommodate.
- **Alloy modeling workshops**: Hillel uses the newsletter to teach Alloy through progressive examples, from simple data structure invariants to complex temporal properties.
- **SMT solver practical guides**: Tutorials on using Z3 and other solvers for everyday verification tasks.

### The Testing Methodology Thread

A significant portion of the newsletter is devoted to **advancing testing beyond example-based approaches**:

- **Property-based testing**: The newsletter regularly features essays on discovering meaningful properties for specific domains, not just generic "test with random inputs" advice.
- **Metamorphic testing**: Hillel has published multiple newsletter issues on this underused technique — testing that if you transform the input in a known way, the output should transform predictably.
- **Contract programming and design by contract**: Using preconditions, postconditions, and invariants as executable specifications that complement formal models.

### Software History as Engineering Practice

The newsletter frequently explores **the history of computing to inform modern engineering practice**. Unlike typical tech history writing, Hillel's approach is prescriptive — each historical essay connects past decisions to present-day engineering challenges:

- The evolution of type systems and what they teach us about modern language design
- How early operating system kernels handled concurrency, and lessons for distributed systems today
- The history of formal methods in aerospace and what commercial software can learn from it

### Developer Productivity and Tooling

Hillel uses the newsletter to share **practical tooling experiments and workflow improvements**:

- AutoHotKey scripting for developer productivity
- Neovim customization and Lua scripting
- Decision tables for managing complex conditional logic
- The "Hierarchy of Controls" framework adapted from industrial safety to software engineering

## Newsletter Format & Approach

The Computer Things newsletter is notable for its **essay-length depth** — most issues are significantly longer than typical newsletter content, more closely resembling short blog posts or academic essays written in an accessible style. This reflects Hillel's broader philosophy that **formal methods concepts deserve the time and space to be properly explained**, not reduced to soundbites.

The newsletter is **free and publicly accessible**, consistent with Hillel's commitment to making formal methods available to all developers regardless of their organization's budget for training.

## Relationship to Other Work

The newsletter complements Hillel's other outputs:

- **Main blog** ([hillelwayne.com](https://hillelwayne.com)): More polished, permanent essays and project announcements
- **Learn TLA+** ([learntla.com](https://www.learntla.com/)): Structured, interactive curriculum
- **Practical TLA+** (book): Comprehensive reference
- **Computer Things newsletter** (Buttondown): Regular, exploratory essays and ongoing experiments

The newsletter often serves as a **testing ground for ideas** that later appear in more formal publications. Its serial nature allows Hillel to build arguments across multiple issues and respond to reader feedback in real time.

## Related

- [[entities/hillel-wayne]] — Main entity page with comprehensive treatment of Hillel's work
- [[concepts/formal-methods]] — Mathematical techniques for verifying software correctness
- [[concepts/tla-plus]] — Temporal Logic of Actions, formal specification language
- [[concepts/property-based-testing]] — Testing general properties rather than specific examples
- [[concepts/software-friction]] — Cognitive and operational costs in software development
- [[concepts/hierarchy-of-controls]] — Framework for preventing production incidents

## Sources

- [Computer Things Newsletter](https://buttondown.com/hillelwayne)
- [Hillel Wayne's Blog](https://hillelwayne.com)
- [Practical TLA+](https://www.hillelwayne.com/post/practical-tla/)
- [Learn TLA+](https://www.learntla.com/)
