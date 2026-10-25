---
title: "Isuru Maduranga"
type: entity
created: 2026-10-24
updated: 2026-10-24
tags:
  - developer
  - author
  - harness-engineering
  - coding-agents
  - open-source
  - educator
sources:
  - https://github.com/IsuruMaduranga/harness-engineering-101
  - https://github.com/IsuruMaduranga/one-code
  - raw/articles/2026-10-22_harness-engineering-101-readme.md
related_concepts:
  - harness-engineering
  - harness-engineering-101
---

# Isuru Maduranga

Isuru Maduranga (publishing as **Isuru Wijesiri**) is an engineer and author best known in this wiki for **Harness Engineering 101**, a 16-chapter open-source book that derives the whole agent stack from the statelessness of the LLM API — "the LLM is the brain, the harness is the body" (v1.1, October 2026). See [[concepts/harness-engineering/harness-engineering-101]] for the book's structure and claims.

**▶ Summary**: Author of Harness Engineering 101 and builder of One Code; teaches the agent stack as 16 minimal patches to one stateless JSON-array loop.

## Work

- **Harness Engineering 101** (2026) — 16 chapters + appendices, built with mdBook, shipping a runnable ~300-line toy harness (`src/harness/`, one file per stage) so the progression from raw JSON array to real harness is reproducible. Each chapter has the same shape: the failure, the minimal patch, what the patch costs.
- **One Code** — his open-source coding agent, built on [[entities/pi]] (Earendil's `pi`). The book's ideas are the ones used in One Code; he also used Claude Code and One Code to restructure chapters into answer-first (Minto pyramid) form, polish English, and generate diagrams and charts — disclosed up front in the book.
- **WSO2 Copilots** — the production grounding for the book's claims: built **WSO2 MI Copilot** (WSO2 Micro Integrator for VS Code) and **WSO2 BI Copilot** (integration platform SaaS editor copilot).

## Why he matters here

Most harness writing is vendor architecture posts or coined terminology. Maduranga's contribution is a **curriculum** — the failure/patch/cost discipline gives [[concepts/harness-engineering]] a teachable spine, and his chapters 7 (subagents as context forks) and 15 ("RAG was a harness pattern all along") reframe two subsystems as array-management decisions rather than architectural tiers.

## Related

- [[concepts/harness-engineering/harness-engineering-101]] — the book
- [[concepts/harness-engineering]] — the discipline it teaches
- [[entities/pi]] — the coding-agent base One Code is built on

## Sources

- [Harness Engineering 101](https://github.com/IsuruMaduranga/harness-engineering-101) · [One Code](https://github.com/IsuruMaduranga/one-code) · [isuruwijesiri.com](https://isuruwijesiri.com/harness-engineering-101/)
