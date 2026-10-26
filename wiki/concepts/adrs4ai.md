---
title: "ADRs4AI (Deliberative Programming)"
created: 2026-10-26
updated: 2026-10-26
type: concept
tags: [concept, agent-workflows, human-in-the-loop, agent-documentation, software-engineering, knowledge-management]
sources:
  - raw/articles/2026-10-26_adrs_adr-deliberation-records.md
confidence: high
---

# ADRs4AI (Deliberative Programming)

**ADRs4AI** is an open methodology and tooling ecosystem by Jérémie Lumbroso that turns human–AI collaboration sessions into **versioned deliberation records** (Architecture/Decision Records adapted for human–AI work), stored in Git alongside the code. Thesis: *the most valuable byproduct of human–AI collaboration is the thinking — and by default all of it evaporates.* The record keeps the **why** so decisions compound for "every mind that comes later" (including future agents). Show HN 2026-10-25 (45 pts).

## The mechanic

One loop: **seed → stake → rule.**

1. **Seed** — the human dumps thinking (dictation fine); the AI chunks it into ADRs preserving the human's actual words, options, reasoning, and open questions (`### QST:` blocks grep-findable in `docs/adr/`).
2. **Stake** — the AI stakes a question with options, a **recommendation, rationale, stated confidence, and a falsifier** ("what would prove it wrong"), each attributed to the model that produced it (e.g. "by GPT 5.6 Sol at Perplexity Computer").
3. **Rule** — the human spends one judgment (accept / override / any answer), possibly from a phone; the ruling is committed verbatim with attribution.

Example record shape (from a live public project): a bitemporal-truth question with options A/B/C, a model recommendation with confidence calibration and falsifier, then the founder's one-line `ANS:` — "The AI carries the reasoning, the human spends one judgment, and the record keeps the why."

Explicit non-goals: not transcript archival, not vector-DB "memory," not an orchestration platform, no claim of persistent AI identity. Called **deliberative programming** — cognitive load down, "bandwidth freed for the deliberations that matter."

## Ecosystem

- GitHub template repo (`ADRs4AI/human-ai-collaboration-template-A`) — ADR & seed templates, directives, inbox protocol, task-runner recipes
- VS Code extension (tree views of open questions, malformed-record diagnostics, **MCP server so agents can query the record**)
- iOS client (review + one-tap Accept landing real commits)
- `awesome-adrs4ai` curated map

## Academic grounding

- *"Cybernetic and Epistemic: A Missing Vocabulary for Trustworthy Agentic Delegation"* — accepted at **AAAI 2026 Fall Symposium on Trustworthy Agentic Systems (TAS 2026)**, arXiv:2610.00961
- *"Deliberative Programming: A Versioned Deliberation Protocol for Human–AI Collectives"* — DOI 10.5281/zenodo.23300579; the template itself is citable (concept DOI 10.5281/zenodo.23303469)

## Why it matters

It attacks the **reasoning-amnesia** failure mode of agentic development: sessions produce reusable judgment that is discarded, and agents re-litigate settled questions. Contrast with memory-system approaches (vector memory, [[concepts/cross-agent-memory-sharing]]) — ADRs4AI is structured, versioned, attributable, and human-legible rather than embedding-based. Its attribution discipline (which model recommended what, with what confidence and falsifier) also makes it a lightweight audit surface, adjacent to [[concepts/evaluation/agent-observability]] and [[concepts/epistemic-transparency]]. The "AI stakes, human rules" pattern is a formalized [[concepts/human-in-the-loop]] for the judgment layer rather than the action layer.

## Related

- [[concepts/human-in-the-loop]]
- [[concepts/agent-documentation]]
- [[concepts/skill-graph]] — the "procedures as markdown in git" cousin; ADRs4AI does "decisions as markdown in git"
- [[concepts/epistemic-transparency]]

## Sources

- [ADRs4AI — adrs.systems](https://adrs.systems) — raw: `raw/articles/2026-10-26_adrs_adr-deliberation-records.md` (Show HN 45 pts, 2026-10-25)
