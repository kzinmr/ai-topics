---
title: "Cognitive load is what matters"
url: https://minds.md/zakirullin/cognitive#long
github: https://github.com/zakirullin/cognitive-load
author: Artem Zakirullin (@zakirullin)
date: 2025-10 (last update)
scraped: 2026-04-16
stars: 12000+
---

# Cognitive Load is What Matters — Artem Zakirullin

Full article source: https://minds.md/zakirullin/cognitive#long

## Author
Artem Zakirullin — Software Architect/Staff Engineer, 15+ years experience.
Based in Limassol, Cyprus. On sabbatical.
GitHub: https://github.com/zakirullin (18 repos, cognitive-load has 12k+ stars)
Twitter: @zakirullin

## Core Thesis
- **Cognitive load** = mental effort required to complete a task
- Working memory holds roughly **4 chunks** of information
- **Intrinsic load** (inherent to task) cannot be reduced
- **Extraneous load** (caused by presentation, abstractions, quirks) must be minimized
- Developers spend far more time reading code than writing it
- Code should be optimized for the reader's working memory

## Load Notation
- 🧠 = fresh working memory, zero cognitive load
- 🧠++ = two facts held, load increased
- 🤯 = cognitive overload, more than 4 facts

## Code-Level Patterns
- Complex conditionals → introduce intermediate descriptive variables
- Nested ifs → use early returns / guard clauses
- Deep inheritance → prefer composition over inheritance

## Architecture Patterns
- Deep modules (simple interface, complex internals) > shallow modules
- Unix I/O example: 5 simple calls hiding hundreds of thousands of lines
- SRP reinterpreted: responsible to one stakeholder, not "one thing"
- Microservices: delay splitting, avoid distributed monoliths
- Layered architectures: add indirection, rarely save migration time
- DDD: problem-space tool, not solution-space folder structure

## Language & Dependencies
- Feature-rich languages cause choice overload (C++: 21 init methods)
- HTTP status codes → self-describing response strings
- DRY abuse → premature abstraction, tight coupling
- Framework coupling → keep business logic framework-agnostic

## Mental Models & Onboarding
- Familiar projects: internalized models = low load
- New projects: ~40 min confusion threshold before intervention needed
- Measure onboarding friction to assess extraneous load
- "Boring" systems (Unix, Kubernetes, Chrome, Redis) succeed by minimizing cognitive load

See the full article at https://minds.md/zakirullin/cognitive#long
