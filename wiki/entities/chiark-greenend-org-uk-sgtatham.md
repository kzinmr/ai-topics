---
title: Simon Tatham
type: entity
created: 2026-04-09
updated: 2026-04-13
tags:
  - person
  - blogger
  - hn-popular
  - developer-tools
  - free-software
  - unix-philosophy
sources: []
---


# Simon Tatham

| | |
|---|---|
| **Born** | 3 May 1977, United Kingdom (via Grokipedia) |
| **Education** | Mathematics, Trinity College, University of Cambridge (via Grokipedia) |
| **Employer** | Arm Ltd., Development Solutions Group — compiler developer (via Grokipedia) |
| **Blog** | [chiark.greenend.org.uk/~sgtatham](https://www.chiark.greenend.org.uk/~sgtatham/) |
| **RSS** | https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/feed.xml |
| **Mastodon** | [@simontatham@hachyderm.io](https://hachyderm.io/@simontatham) |
| **Role** | Software engineer, free-software author |
| **Known for** | PuTTY SSH client (1999), NASM co-developer, Simon Tatham's Portable Puzzle Collection, spigot (exact real calculator), Halibut documentation system, agedu, xtruss |
| **Bio** | Software engineer based in Cambridge, UK. Maintains a diverse portfolio of free software projects spanning networking tools, mathematical puzzles, and utilities. Writes a "quasi-blog" of long-form technical essays. Notable for his deep dives into mathematical curiosities (aperiodic tilings, field extensions) alongside pragmatic Unix tooling. |

## Biography

Simon Tatham was born on 3 May 1977 in the United Kingdom (via Grokipedia). He attended primary school at Dolphin School and Hurst School — the latter twice, due to family relocations — and completed his secondary education at Leighton Park School in Reading (via Grokipedia). By age nine, Tatham had already begun writing complex programs on the ZX Spectrum, sparking an early and enduring fascination with computing (via Grokipedia).

He earned a degree in mathematics from the University of Cambridge, where he studied at Trinity College (via Grokipedia). During his university years, Tatham prioritized intensive personal programming projects over traditional coursework, and it was during this time that he co-developed the Netwide Assembler (NASM) with Julian Hall in 1996 — a portable x86 assembler that continues to be maintained by a team at Intel (via Grokipedia).

After graduation, Tatham joined Arm Ltd. in the early 2000s, where he works full-time in the company's Development Solutions Group as a compiler developer, focusing on tools like Arm Compiler for embedded systems and high-performance computing (via Grokipedia). His contributions have extended to formal verification techniques for numerical algorithms, such as verifying floating-point division routines using tools like Gappa to guarantee accuracy in compiler-generated code (via Grokipedia).

Tatham is best known as the primary author and maintainer of **PuTTY**, a free and open-source SSH/Telnet client first released in 1999. PuTTY has become one of the most widely used SSH clients globally, particularly on Windows systems, due to its lightweight design, portability, and support for both graphical and command-line interfaces (via Grokipedia). Key features include its built-in xterm-style terminal emulation (via Grokipedia).

Beyond PuTTY and NASM, Tatham created **Simon Tatham's Portable Puzzle Collection** — a suite of single-player logic puzzle games — and authored the widely-cited 1999 essay **"How to Report Bugs Effectively,"** a guide on submitting clear and actionable bug reports that remains a standard reference in the free-software community (via Grokipedia).

## Core Ideas

Simon Tatham is a **pragmatic craftsman** in the Unix tradition — someone who builds small, focused tools that do one thing well, then writes extensive, thoughtful documentation about both the tools and the deeper principles behind them. His writing spans from mathematical recreations to hard-nosed engineering philosophy.

### Code Review as Social Technology

Tatham's widely-cited essay ["Code review antipatterns"](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/code-review-antipatterns/) uses satire to illuminate real dysfunction in the code review process. By cataloguing dark-side reviewer behaviors — *The Death of a Thousand Round Trips*, *The Ransom Note*, *The Double Team*, *The Guessing Game*, *The Priority Inversion*, *The Catch-22*, *The Flip Flop*, and *The Late-Breaking Design Review* — he reveals how code review's social dynamics can be weaponized against contributors.

His underlying thesis: **code review is as much about people as it is about code**. Most antipatterns share a common root — the reviewer avoids stating clearly what they actually want, or exercises authority without responsibility. The fix is equally social: reviewers should commit to a single comprehensive pass, state their acceptance criteria upfront, and argue with each other rather than bouncing conflicting demands off the contributor.

### Stop Helping! — On User Experience Design

In ["Stop helping!"](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/stop-helping/), Tatham argues against the common CLI practice of dumping full help text after an error message. His reasoning is grounded in visual pattern recognition:

> *"At first glance, this display with an error message plus help text looks almost exactly the same as the display with just the help text. It is entirely possible to miss the error completely, simply because it was lost in the noise."*

The broader principle: **well-intentioned verbosity is a form of user hostility**. When users learn to ignore walls of text, you've trained them to miss the one thing that matters. Tell users how to get help — but wait until they ask.

### Git Without a Forge

Tatham's essay on using Git without GitHub/GitLab explores the philosophy of **distributed version control as originally intended**. He maintains his projects without relying on any forge, treating Git as a peer-to-peer system rather than a client-server architecture with a central authority. This reflects his broader skepticism about platform lock-in and the gradual centralization of tools that were designed to be decentralized.

### Policy of Transience

Tatham has written about maintaining a "policy of transience" — the deliberate choice not to accumulate digital baggage. This extends from his approach to email (not hoarding it) to his software maintenance philosophy. The principle: **systems that assume permanence become harder to maintain over time**. Designing for transience reduces the long-term cost of ownership.

### Separation of Concerns in Tooling

Across his projects, Tatham consistently applies Unix philosophy principles:
- **PuTTY** separates protocol implementation from terminal emulation from authentication
- **Halibut** separates content from formatting, supporting multiple output formats from a single source
- **spigot** separates mathematical computation from presentation, enabling exact real arithmetic

His bug tracker essay argues that **issue tracking should separate report, diagnosis, and fix** rather than conflating them into a single thread. Each concern has different participants, different lifecycles, and different resolution criteria.

### Mathematical Curiosities as Engineering Practice

Tatham's series on aperiodic tilings (five parts and counting) and his essay on brute-forcing Langley's geometry problem with field extensions demonstrate a rare blend: **treating mathematical recreation with the same engineering rigor as production software**. He builds finite-state transducers to generate tilings, implements exact arithmetic to avoid floating-point errors, and publishes the code alongside the mathematics.

## Key Quotes

> *"Code review can also be a powerful tool for totally different purposes. When a reviewer turns to the dark side, they have a huge choice of ways to obstruct or delay improvements to the code, to annoy patch authors or discourage them completely."*

> *"Trying harder to be helpful is often the problem. Wait for users to ask for help before volunteering the entire screenful of text."*

> *"If you have authority to make that decision, you can say so in words, so the submitter doesn't waste any more time on it!"*

## Related

- [[unix-philosophy]] — Small tools, clear interfaces, composability
- [[code-review]] — Social dynamics of reviewing code
-  — Using Git without GitHub/GitLab
-  — Distributed version control system
-  — Building tools for developers
- [[mitsuhiko]] — Another free-software author with similar philosophy

## Sources

- [Grokipedia: Simon Tatham](https://grokipedia.com/page/Simon_Tatham)
- [Code review antipatterns](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/code-review-antipatterns/) (Aug 2024)
- [Stop helping!](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/stop-helping/) (Sep 2023)
- [Git without a forge](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/git-without-a-forge/)
- [Policy of transience](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/policy-of-transience/)
- [Separation of concerns in a bug tracker](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/bug-tracker/)
- [Aperiodic Tilings series](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/) (Parts I-V, 2023-2024)
- [Brute-forcing Langley's geometry problem with field extensions](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/langley/)
- [Coroutines in C](https://www.chiark.greenend.org.uk/~sgtatham/coroutines.html)
- [Writing commit messages](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/commit-messages/)
- [Symbiosisware](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/symbiosisware/)
