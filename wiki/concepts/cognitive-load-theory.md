---
title: "Cognitive Load Theory — Core Concepts"
type: concept
aliases:
  - cognitive-load-core
created: 2026-04-16
updated: 2026-04-16
tags:
  - concept
  - methodology
  - software-engineering
  - cognitive-science
status: active
---

# Cognitive Load Theory — Core Concepts

Artem Zakirullin's framework centers on a fundamental human constraint: **working memory capacity**.

## Core Theorem

> "Confusion costs time and money. Confusion is caused by high cognitive load. It's not some fancy abstract concept, but rather **a fundamental human constraint.**"

- Developers spend far more time **reading** code than writing it
- Human working memory holds approximately only **4 chunks**
- Exceeding this threshold causes confusion (🤯), reducing productivity and quality

## Two Types of Cognitive Load

| Type | Description | Controllability |
|------|-------------|-----------------|
| **Intrinsic Load** | Task/domain-inherent difficulty | Cannot be reduced |
| **Extraneous Load** | Presentation method, unnecessary abstractions, author's quirks | **Reducible — this is where to focus** |

### Load Notation
- 🧠 = Fresh working memory, zero load
- 🧠++ = Holding 2 facts, load increasing
- 🤯 = Cognitive overload, 4+ facts

## Mental Models & Onboarding

### Familiar Projects
- Mental models internalized in long-term memory → low cognitive load
- The more unique mental models a project requires, the longer before new developers provide value

### The 40-Minute Rule
> "If they're confused for more than ~40 minutes in a row — you've got things to improve in your code."

- Low cognitive load enables new team members to contribute within hours
- "Boring" systems (Unix, Kubernetes, Chrome, Redis) succeed because they minimize cognitive load

### Mental Model Dependency
HN commenter *weiliddat* (2,334 chars) argues that cognitive load reduction doesn't happen in a vacuum — it depends on the reader's **existing mental models**. A framework familiar to one team may be heavier cognitive load for newcomers. The lesson: "simpler is always better" is a dangerous assumption — consider the target developer's (or agent's) training distribution.

### Programming as Theory-Building
*physidev* connects this to Peter Naur's "Programming as Theory-building" paper — code is not just instructions but **a formalization of domain understanding**. When that theory is lost, the code loses meaning. For harness design, this means agents should maintain domain theory, not just generate code.

## Related

- [[concepts/cognitive-load-software-development]] — Main concept page
- [[concepts/cognitive-load-patterns]] — Code and architecture anti-patterns
- [[concepts/cognitive-load-tool-support]] — Tooling and agentic engineering
