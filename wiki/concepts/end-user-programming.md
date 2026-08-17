---
title: "End-User Programming"
type: concept
aliases:
  - end-user-programming
  - end user programming
created: 2026-04-25
updated: 2026-08-17
tags:
  - concept
  - personal-software
  - customization
  - gui
sources:
  - raw/articles/geoffreylitt.com--2023-03-25-llm-end-user-programming-html--17879d95.md
  - https://geoffreylitt.com/2023/03/25/llm-end-user-programming.html
---

# End-User Programming

## Summary

**End-user programming** is the vision that normal people — not just professional developers — should be able to harness the full, general power of computers. The field has a decades-long history (Alan Kay's 1984 "we want to edit our *tools* as we have previously edited our *documents*"), with practical successes such as spreadsheets, HyperCard, Smalltalk, Yahoo Pipes, Airtable, Glide, and iOS Shortcuts. Its central obstacle — the **programming bottleneck** of turning fuzzy informal intent into formal, executable code — is being pried open by LLMs, making end-user programming one of the most plausible near-term structural changes in software production and distribution.

## The Programming Bottleneck

System designers have tried super-high-level languages, visual editors, layered complexity, and programming-by-example, but all hit a ceiling: helping people turn rough ideas into executable code is genuinely hard. [[entities/geoffrey-litt|Geoffrey Litt]]'s **Wildcard** system (customize any website through a spreadsheet interface) illustrates the bottleneck: the spreadsheet formulas were a barrier to initial use, and behind the scenes each site needed hand-written scraping adapters. Both bottlenecks — formula synthesis and adapter generation — are exactly the code-synthesis tasks LLMs can now perform.

## LLMs as a Step Change (Litt, March 2023)

In "Malleable software in the age of LLMs," Litt argued LLMs would produce structural changes in who creates software, when, and for what purpose:

- **One-off scripts** — users have AI create and execute scripts dozens of times a day (data analysis, video editing, automation)
- **One-off GUIs** — AI builds a full application for a single task, containing just the needed features
- **Build don't buy** — businesses write more custom in-house software instead of buying SaaS, because tailoring is now cheap
- **Modding/extensions** — users demand the ability to extend the software they already use
- **Recombination** — compose the best parts of different applications into hybrids

## Local Developers: Betty and Buzz

Bonnie Nardi and James Miller's 1990 study of collaborative spreadsheet development found that real end-user development is a partnership: the domain expert ("Betty") builds most of the spreadsheet herself, while a local technical expert ("Buzz") adds small advanced pieces expressed in terms of her work — an adjunct consultant, not an architect. The LLM-era version of this pattern: the user drives creation and asks for technical help on demand; ideally the LLM *teaches* the user, so their dependence on the AI gently decreases over time rather than locking them into a black box.

## Interaction Models

A key open question is which interaction model suits which task: chatbot, one-off script, or custom throwaway GUI. Litt's position is that **chat is an essentially limited interaction mode** — direct manipulation UIs offer flow states, muscle memory, and fine control that natural-language back-and-forth cannot match. The promising design space is **open-ended computational media** (the spreadsheet as archetype): an inner loop of direct manipulation plus an outer loop of tool editing, with LLMs as collaborators inside the medium.

## Related Concepts

- [[concepts/malleable-software]] — The design agenda for end-user programming: software users can pull apart and re-combine
- [[concepts/ink-switch]] — Research lab where end-user programming and malleable software are actively developed
- [[entities/geoffrey-litt]] — Researcher whose LLM-era essays define the current debate
- [[concepts/ai-programming-as-theory-building]] — Adjacent perspective on what programming (and AI-assisted programming) is for

## Sources

- [Malleable software in the age of LLMs (Geoffrey Litt, Mar 2023)](https://geoffreylitt.com/2023/03/25/llm-end-user-programming.html)
- [The State of the Art in End-User Software Engineering (Ko et al., 2011)](https://faculty.washington.edu/ajko/papers/Ko2011EndUserSoftwareEngineering.pdf)
- [Spreadsheets in Cooperative Software Development (Nardi & Miller, 1990)](https://dl.acm.org/doi/10.1145/98188.98200)
