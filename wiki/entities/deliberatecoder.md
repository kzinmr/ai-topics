---
title: "Steve Shogren (Deliberate Software)"
tags: [[person]]
created: 2026-04-24
updated: 2026-04-24
---


# Steve Shogren (Deliberate Software)

**URL:** https://deliberate-software.com  
**Blog:** Deliberate Software  
**Identity:** Steve Shogren — software developer, manager, author, speaker  
**Active:** ~2017–present  
**Themes:** Deliberate coding practices, functional programming (F#, Haskell), vim/Emacs editor abstractions, team dynamics, domain-driven design, ethical software development  

## Overview

**Deliberate Software** is a technical blog by **Steve Shogren**, a software developer, manager, author, and speaker who writes about the craft of programming with a focus on **intentionality** — making conscious, well-reasoned decisions about code structure, tooling, team practices, and the ethical dimensions of software.

The blog's name is its thesis: **deliberate coding means doing things consciously and intentionally.** Shogren's work is characterized by a willingness to challenge conventional wisdom in software engineering, explore unconventional tools and languages, and examine the human factors that shape technical outcomes.

Unlike many technical blogs that focus on specific frameworks or languages, Deliberate Software takes a **meta-engineering approach**: it asks not just "how do I write this code?" but "how should I think about writing code?" and "what am I actually optimizing for?" This perspective draws on Shogren's experience as both an individual contributor and a team leader, giving his writing practical grounding alongside philosophical depth.

## Timeline

| Date | Event |
|------|-------|
| ~2017 | Blog becomes active with posts on design patterns, DSLs, and proofs |
| Aug 2017 | "DSLs Are Terrible" — critique of domain-specific languages |
| Aug 2017 | "Design Pattern Dangers" — examines the pitfalls of pattern-driven development |
| Aug 2017 | "Papers We Love: The Byzantine Generals Problem" — connects academic distributed systems research to practical software concerns |
| Apr 2017 | "Darkest Proof: Day 3" — exploration of formal verification using Coq |
| Dec 2017 | "MOBA Item Optimization In Haskell" — applies functional programming to game design problems |
| Jun 2018 | "Simple Haskell Automation in Emacs" — demonstrates practical Haskell tooling within Emacs |
| Dec 2018 | "F# Domain Design: Interdependent Enums and Booleans" — explores type system design for complex domain models |
| Feb 2018 | "Scientific Software Design: Human Working Memory" — argues that software design must account for human cognitive limitations |
| Aug 2022 | "Powerful Editor Abstractions" — deep dive into vim/Emacs customization as a force multiplier |
| 2022+ | Publishes "Books That Shape My Thinking" — curated reading list reflecting intellectual influences |
| 2023–2025 | Continues writing on deliberate coding, team dynamics, and editor productivity |
| 2025 | Explores "deliberation-first coding" methodology in the context of AI-assisted development |

## Core Ideas

### Deliberate Coding: Intentionality Over Habit

Shogren's central philosophy is that **most developers don't code deliberately**. They follow habits, copy patterns, and make decisions reactively rather than proactively. Deliberate coding requires:

> "Doing something consciously and intentionally. It turns out that not everyone writes code deliberately, and at the very least, not everyone does it consistently."

This manifests in several practices:
- **Questioning legacy code:** Don't assume every line exists for a good reason. The original author may not have known what they were doing.
- **Documenting intention:** Code should explain not just what it does, but why it does it that way.
- **Making small, focused changes:** Each change should have a clear purpose that can be articulated and reviewed.

### Scientific Software Design and Human Working Memory

One of Shogren's most interesting arguments is that **software design is fundamentally constrained by human cognitive architecture**:

> "Scientific Software Design: Human Working Memory" — software systems should be designed with an understanding of how many variables, relationships, and abstractions a human mind can simultaneously hold.

This insight has practical implications:
- **Limit abstraction depth:** Each additional layer of abstraction consumes working memory.
- **Design for the reader, not the writer:** Code is read far more often than it is written.
- **Prefer explicit over implicit:** Hidden behavior increases cognitive load.

This connects to the broader deliberate coding philosophy: if we design software with human cognitive limits in mind, we produce systems that are easier to maintain, review, and extend.

### Editor Abstractions as Force Multipliers

Shogren is a strong advocate for investing in editor proficiency as a form of leverage:

> "Powerful Editor Abstractions" — customizing your editor (vim, Emacs) to encode your workflow patterns is one of the highest-ROI activities a developer can undertake.

The argument is straightforward: if you perform a task hundreds of times per week, even a small efficiency improvement compounds dramatically. Shogren demonstrates this with vim and Emacs configurations that automate repetitive editing patterns, reduce keystrokes, and enforce consistent code style.

### Functional Programming for Domain Modeling

Shogren's exploration of F# and Haskell is driven by a practical concern: **how do we represent complex business domains in code without creating tangled, bug-prone systems?**

His F# posts focus on **interdependent enums and booleans** — cases where domain logic requires multiple related states that are difficult to model with traditional object-oriented approaches. By using discriminated unions, pattern matching, and type-level constraints, functional languages can make invalid states unrepresentable, eliminating entire categories of bugs.

His Haskell work is similarly pragmatic: using the type system to encode domain invariants, then letting the compiler enforce them.

### The Ethical Dimension of Code

Shogren identifies an often-overlooked aspect of deliberate coding:

> "There's an even higher level of coding deliberately that I think is worth considering: the ethical dimension of writing code. Every line of code represents an ethical and moral decision."

This isn't about grand philosophical statements — it's about the small choices: Do I handle this error case? Do I validate this input? Do I log this sensitive data? Do I ship this feature knowing it has known bugs? Each decision has downstream consequences for users, colleagues, and society.

### Team Dynamics and Self-Organization

Shogren writes about what keeps self-organizing teams functional:
- **Shared mental models:** Teams need common vocabulary and understanding of their domain.
- **Deliberate communication:** Not just more communication, but more intentional communication.
- **Ego management:** "Ego Driven Development" is a real anti-pattern that Shogren identifies and critiques.

His "Ten Years of Pair Programming" post reflects a long-term commitment to collaborative coding as a way to distribute knowledge, catch errors early, and maintain code quality.

## Key Influences and Reading

Shogren's "Books That Shape My Thinking" list includes works on:
- Software architecture and design
- Team dynamics and organizational behavior
- Functional programming and type theory
- Cognitive psychology and human factors
- Philosophy of technology

This intellectual breadth informs his writing, which consistently draws connections between technical problems and their human, organizational, and ethical contexts.

## Writing Style and Approach

- **Pragmatic idealism:** Advocates for best practices while acknowledging real-world constraints
- **Cross-paradigm:** Comfortable moving between object-oriented, functional, and procedural approaches
- **Tool-focused:** Believes that investing in your development environment pays compounding returns
- **Human-centered:** Always returns to how software affects the people who write, read, and use it
- **Evidence-based:** Draws on personal experience, academic research, and community wisdom

## Key Quotes

> "Every line of code represents an ethical and moral decision."

> "Doing something deliberately means doing it consciously and intentionally."

> "The people who wrote this code may or may not have known what they were doing. So don't worry too much about preserving old stuff."

## Contact

- **Blog:** https://deliberate-software.com
- **Identity:** Steve Shogren
- **Roles:** Software developer, manager, author, speaker

## See Also

- [[entities/_index.md]]
