---
title: zakirullin
description: "Artem Zakirullin — Software Architect and author of 'Cognitive load is what matters,' a widely-cited framework (12K+ GitHub stars) on minimizing cognitive complexity in software design"
url: https://minds.md/zakirullin
type: entity
created: 2026-04-25
updated: 2026-04-30
tags:
  - entity
  - person
  - software-engineering
  - methodology
  - cognitive-load
aliases:
  - Artem Zakirullin
  - zakirullin
  - @zakirullin
sources:
  - https://minds.md/zakirullin
  - https://github.com/zakirullin/cognitive-load
  - https://cy.linkedin.com/in/zakirullin
  - https://github.com/zakirullin
  - raw/articles/zakirullin-cognitive-load-2025.md
---

# Artem Zakirullin

**Artem Zakirullin** (handles: `zakirullin`, `@zakirullin`) is a Software Architect / Staff Engineer with 15+ years of experience, and the author of **"Cognitive load is what matters"** — one of the most widely-cited frameworks on cognitive complexity in software design. The GitHub repository has accumulated over 12,000 stars and been translated into Chinese, Japanese, Spanish, Korean, Turkish, Vietnamese, and Nepali.

## Overview

Based in Limassol, Cyprus (currently on sabbatical as of 2025–2026), Zakirullin has worked across multiple companies and roles including Senior Engineer at TheSoul Publishing (advancing to Architect role), where he was recognized for "handling complex projects with significant uncertainty" and a "product-oriented mindset." Beyond his cognitive load work, he has published a PDF on mobile coding journey in PagedOut magazine.

## Core Thesis: Cognitive Load is What Matters

### The Central Idea
> "Cognitive load is how much a developer needs to think in order to complete a task."

When reading code, developers hold variables, control flow, and call sequences in working memory. The average person holds only **four chunks** simultaneously. Once cognitive load reaches this threshold, understanding becomes dramatically harder.

### Two Types of Load
- **Intrinsic load** — Inherent to the task itself, cannot be reduced
- **Extraneous load** — Caused by presentation, abstractions, quirks — **must be minimized**

The framework uses a visual notation system:
- 🧠 = fresh working memory, zero load
- 🧠++ = two facts held
- 🤯 = cognitive overload (>4 facts)

### Key Code-Level Patterns

1. **Complex conditionals** → Introduce intermediate descriptive variables
2. **Nested ifs** → Use early returns / guard clauses
3. **Deep inheritance** → Prefer composition over inheritance
4. **DRY abuse** → Premature abstraction creates tight coupling

### Architecture Patterns

- **Deep modules** (simple interface, complex internals) > shallow modules
- **Layered architectures** add indirection but rarely save migration time
- **Microservices**: delay splitting, avoid distributed monoliths
- **DDD**: problem-space tool, not solution-space folder structure

### Language & Dependencies
- Feature-rich languages cause choice overload (C++ has 21 initialization methods)
- HTTP status codes → prefer self-describing response strings
- Framework coupling → keep business logic framework-agnostic

### Onboarding & Mental Models
- Familiar projects: internalized models = low cognitive load
- New projects: ~40 min confusion threshold before intervention needed
- "Boring" systems (Unix, Kubernetes, Chrome, Redis) succeed by minimizing cognitive load

## Impact
The cognitive load framework has become a standard reference in software engineering discussions, particularly in:
- Code review guidelines
- Architecture decision records
- Onboarding documentation design
- AI coding agent prompt engineering (reducing agent confusion)

## Related Concepts
- [[concepts/cognitive-load-software-development]] — Comprehensive concept page on the framework
- [[concepts/cognitive-cost-of-agents]] — Cognitive load applied to AI agent interactions

## References
- [Cognitive load is what matters (full article)](https://minds.md/zakirullin/cognitive#long)
- [GitHub Repository (12K+ stars)](https://github.com/zakirullin/cognitive-load)
- [LinkedIn](https://cy.linkedin.com/in/zakirullin)
- [X/Twitter](https://x.com/zakirullin)
