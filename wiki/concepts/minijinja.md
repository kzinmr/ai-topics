---
title: "MiniJinja"
type: concept
aliases:
  - minijinja
  - MiniJinja
created: 2026-04-25
updated: 2026-11-26
tags:
  - concept
  - rust
  - python
  - open-source
  - developer-tooling
related:
  - "[[entities/armin-ronacher]]"
  - "[[concepts/agentic-engineering]]"
sources:
  - https://github.com/mitsuhiko/minijinja
  - raw/articles/lucumr.pocoo.org--2026-6-23-the-coming-loop--5fc36909.md
  - raw/articles/minimaxir.com--2026-09-agentic-iteration--961851b8.md
---

# MiniJinja

**MiniJinja** is a **Rust re-implementation of the Jinja2 template engine** created by [[entities/armin-ronacher|Armin Ronacher]] (2021; ~2.5k GitHub stars). It extends Ronacher's Jinja2 lineage (Flask, Jinja2, Werkzeug, Click) into Rust, and has since grown into a case study in **AI-agent-driven code porting**.

## Why It Matters

### 1. Rust as the substrate for developer tooling
MiniJinja is part of Ronacher's post-2017 Rust bet (with Insta and Rye): performance, safety, and expressiveness for developer infrastructure, language-agnostic via bindings.

### 2. The landmark AI porting case (January 2026)
Ronacher **ported MiniJinja from Rust to Go using AI agents** (Opus 4.5 + GPT-5.2 Codex):

| Metric | Value |
|---|---|
| Active human time | ~45 minutes |
| Agent runtime | 10 hours |
| Messages | 2,698 |
| Tool calls | 1,386 |
| API cost | ~$60 |

Widely cited as a landmark demonstration of agent-driven **mechanically verifiable translation** — the class of task where "agentic loops" genuinely work (see [[concepts/agentic-engineering]] and Ronacher's own *The Coming Loop* critique). Ronacher's conclusion: loops excel at code porting, performance exploration, security scanning, and research — *not* at writing lasting code.

### 3. Language-agnostic templating
MiniJinja now spans Rust (native), **Go (native, AI-ported)**, and **WASM for JavaScript** — Ronacher's vision of one template semantics, many runtimes.

## Related

- [[entities/armin-ronacher]] — creator; Earendil founder; Pi owner
- [[concepts/agentic-engineering]] — MiniJinja→Go as the canonical loop-succeeds example
- Bun's Zig→Rust rewrite is the other frequently paired porting case

## Sources

- [mitsuhiko/minijinja (GitHub)](https://github.com/minijinja/minijinja)
- Ronacher, *Porting MiniJinja to Go With an Agent* (Jan 2026)
- Ronacher, *The Coming Loop* (Jun 2026) — raw article in this wiki
