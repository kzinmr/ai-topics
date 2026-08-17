---
title: "Malleable Software"
type: concept
aliases:
  - malleable-software
  - malleable systems
created: 2026-04-25
updated: 2026-08-17
tags:
  - concept
  - personal-software
  - customization
  - extensibility
  - local-first
sources:
  - raw/articles/geoffreylitt.com--2023-03-25-llm-end-user-programming-html--17879d95.md
  - https://geoffreylitt.com/2023/03/25/llm-end-user-programming.html
---

# Malleable Software

## Summary

**Malleable software** is software that users can pull apart, recombine, and extend at the granularity of individual UI elements, rather than being locked into prefabricated applications shipped by distant developers. The term was coined by Philip Tchernavskij in his 2019 PhD thesis *Designing and Programming Malleable Software*; [[entities/geoffrey-litt|Geoffrey Litt]] and the [[concepts/ink-switch|Ink & Switch]] research lab made it a central research agenda. In the LLM era the concept gained new force: if users can describe changes in natural language, the cost of adapting tools collapses, and AI-generated tools can inherit platform capabilities (persistence, collaboration, composition) instead of living as throwaway chat artifacts.

## Key Ideas

- **Users edit their tools, not just their documents** — Alan Kay's 1984 framing ("We now want to edit our *tools* as we have previously edited our *documents*") is the canonical statement of the vision.
- **Pull-apart and re-combine** — Tchernavskij's definition: malleable software "aims to increase the power of existing adaptation behaviors by allowing users to pull apart and re-combine their interfaces at the granularity of individual UI elements."
- **Principles from the Ink & Switch essay (2025)** — universal version control for user artifacts, live collaboration across tools on shared data, gradual enrichment (text → structure → interactivity → automation), and AI-assisted development inside the malleable environment.
- **The programming bottleneck** — historically, end-user programming was blocked by the difficulty of turning fuzzy informal intent into formal, executable code. LLMs open this bottleneck by generating scraping code, spreadsheet formulas, and small tools from natural language.
- **Chat is an essentially limited interaction mode** — even a perfect chatbot cannot replace direct-manipulation UIs (Litt's video-trimming example; Winograd & Flores's "readiness-to-hand" steering-wheel argument). Malleable software preserves rich UIs while adding an outer loop for tool editing.
- **Double interaction loop** — the spreadsheet is the archetype: an inner loop of direct manipulation (edit a number, see the model update) plus an outer loop that edits the tool itself (edit the formulas). LLMs make the outer loop available to non-programmers.
- **LLM as local developer** — Bonnie Nardi and James Miller's 1990 study of collaborative spreadsheet development ("Betty and Buzz") showed domain experts and local technical experts co-develop tools. An LLM can play Buzz's role, but ideally it *teaches* the user so their reliance on the AI decreases over time.
- **On-the-fly UI** — one-off GUIs generated for a single task ("just the features you need, no bloat"), demonstrated by Litt's interactive-spreadsheet mockup and early demos by Sean Grove and Vasek Mlejnsky.

## LLMs and Malleability (Litt, March 2023)

Litt's essay "Malleable software in the age of LLMs" argued that LLMs represent a step change in tool support for end-user programming, predicting five structural shifts: one-off scripts created and executed dozens of times a day; one-off GUIs; "build don't buy" (in-house software over SaaS); modding/extensions of existing software; and recombination of the best parts of different applications. The essay motivated his later AI HUDs argument ("Enough AI copilots! We need AI HUDs") and the 2025 Ink & Switch malleable-software manifesto.

## Projects & Research

| Project | Org | Description |
|---------|-----|-------------|
| **Wildcard** | Ink & Switch (2020) | Customize any website through a spreadsheet interface; LLMs can now generate the site-specific scraping adapters that were the bottleneck |
| **Potluck** | Ink & Switch (2022) | Dynamic documents: text notes enriched with detectors and interactive behaviors (scaling, timers) |
| **Embark** | Ink & Switch (2023) | Dynamic documents for travel planning |
| **Patchwork** | Ink & Switch (2024-2026) | Version control for non-engineers; AI-generated tools gain persistence and multi-user collaboration inside the environment |
| **Ambsheets** | Ink & Switch (2025) | Spreadsheet-like interfaces augmented with AI capabilities |

## Related Concepts

- [[concepts/end-user-programming]] — The broader field: normal people harnessing the full power of computers; malleable software is its design agenda
- [[concepts/ink-switch]] — Research lab where the malleable-software agenda was developed
- [[concepts/local-first-software]] — Related architectural movement: user data control, offline capability, portability
- [[entities/geoffrey-litt]] — Leading researcher and essayist on malleable software in the LLM era

## Sources

- [Malleable software in the age of LLMs (Geoffrey Litt, Mar 2023)](https://geoffreylitt.com/2023/03/25/llm-end-user-programming.html)
- [Designing and Programming Malleable Software (Philip Tchernavskij, 2019 PhD thesis)](https://hal.inria.fr/tel-02440479)
- [Malleable Software: Restoring User Agency in a World of Locked-Down Apps (Ink & Switch, 2025)](https://www.inkandswitch.com/malleable-software/)
