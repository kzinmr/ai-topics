---
title: Matt Godbolt
type: entity
created: 2026-04-09
updated: 2026-04-10
tags:
- person
- blogger
- hn-popular
- c++
- compiler-explorer
- assembly
- open-source
- systems-programming
aliases:
- xania.org
- compiler-explorer
- godbolt
- mattgodbolt
sources: []
---

# Matt Godbolt

| | |
|---|---|
| **Blog** | [xania.org](https://xania.org) |
| **RSS** | https://xania.org/feed |
| **GitHub** | [github.com/mattgodbolt](https://github.com/mattgodbolt) |
| **Mastodon** | [@mattgodbolt](https://mastodon.social/@mattgodbolt) |
| **Bluesky** | [@xania.org](https://bsky.app/profile/xania.org) |
| **Podcast** | [Two's Complement](https://twoscomplement.org/) (Co-host) |
| **Role** | C++ Developer at Hudson River Trading; Creator & Maintainer of Compiler Explorer (godbolt.org) |
| **Location** | Chicago, IL |
| **Known for** | Compiler Explorer (godbolt.org), C++ conference keynotes, "Advent of Compiler Optimisations" series |
| **Bio** | Matt Godbolt is a C++ developer and the creator of Compiler Explorer, an interactive tool that visualizes how compilers translate source code into assembly. He works at Hudson River Trading on "super fun but secret things" and co-hosts the *Two's Complement* podcast. His blog has been running since 2007, covering compilers, systems programming, open-source stewardship, and more recently, AI-assisted development. |

## Core Ideas

Godbolt writes primarily about **compilers, systems programming, open-source project stewardship, and the intersection of AI with developer tools**. His blog is a rare window into the internals of how modern compilers optimize code, written by someone who has built the world's most popular tool for exploring exactly that.

### Compiler Explorer: 92 Million Compilations Per Year

Compiler Explorer (godbolt.org) began in 2012 as a hacky internal tool — a shell script running `watch "gcc -S example.cpp -O1 | c++filt"` — to justify enabling C++11 features to his boss. Today it supports **81 programming languages**, hosts **4,724 compiler versions**, and processes **92 million compilations per year** (1.8M/week).

**Key infrastructure details:**
- **3.9 TB** of compilers, libraries, and tools stored on AWS EFS
- **30+ EC2 instances** for compilation, with auto-scaling based on CPU load
- **nsjail** (Google's lightweight process isolation) for sandboxing — critical because "we let random people run arbitrary code on our machine"
- **1,982,662 short links saved** — preserving legacy goo.gl URLs manually after Google's shutdown
- **Zero tracking** by design: "we purposefully don't have the kind of tracking that could tell us [how many users]"
- **Cost transparency**: ~$3,000/month (~$37,000/year) funded by Patreon, GitHub Sponsors, and corporate sponsors (e.g., NVIDIA)

### The Philosophy of Permanent URLs

Godbolt treats **link rot as a civilizational problem** to be actively fought:

> *"One of our core principles is that we never retire compiler versions. Once a compiler goes up on Compiler Explorer, it stays there forever... It's our small contribution to fighting link rot."*

When Google shut down goo.gl (the URL shortener Compiler Explorer originally used), Godbolt manually migrated **12,000+ legacy links** rather than letting them break. This commitment to permanence reflects a broader philosophy: **developer tools should outlast their creators and the platforms they depend on**.

In 2024, he formed **Compiler Explorer, LLC** to formalize the project's governance and financial structure, ensuring its long-term sustainability beyond volunteer effort alone.

### The Advent of Compiler Optimisations (AoCO2025)

Godbolt's most ambitious writing project was a **25-day series of blog posts and videos** (December 2025), each detailing a specific compiler optimization. The series revealed surprising compiler behaviors:

- **Loop optimization**: Compilers apply unexpected mathematical shortcuts to simple iterative functions (e.g., summing 1..N becomes a closed-form formula)
- **Switch statements**: "The standard wisdom is that switch statements compile to jump tables. And they do — when the compiler can't find something cleverer to do instead."
- **Memory access patterns**: Clang replaces `memcmp` with inline bitwise ops and overlapping reads when comparing against compile-time constants
- **SIMD auto-vectorization**: Modern compilers automate SIMD processing (2, 4, 8, 16+ data units per instruction), originally requiring manual assembly
- **Floating-point non-associativity**: SIMD vectorization fails with floating-point math because `(a + b) + c ≠ a + (b + c)` — integers don't suffer this limitation
- **Recursive inlining**: Recursive routines (e.g., GCD) can be inlined/optimized, defying the assumption that self-calls prevent inlining

The series was **written by Godbolt, proof-read by an LLM** — a pattern he adopted for efficiency while maintaining intellectual ownership.

### AI and the Semiconductor Revolution Analogy

Godbolt draws a powerful parallel between **AI coding tools and the 1970s-80s semiconductor design revolution**:

| Era | Method | Scale |
|:---|:---|:---|
| **1970s** | Hand-drawn gates on acetate | ~3,500 transistors (MOS 6502) |
| **Modern** | Automated CAD & standard libraries | >134 billion transistors (Apple M2 Ultra) |

> *"The semiconductor design evolution didn't eliminate jobs — it enabled creations of previously impossible complexity."*

His argument: AI coding tools (particularly Claude Code) are **establishing a new layer of abstraction**, not replacing programmers. The MOS 6502 had 3,500 transistors; the Apple M2 Ultra has 134 billion — a 38-million-fold increase made possible by automation. Similarly, AI will enable programmers to build systems of previously impossible complexity.

### AI as Junior Developer

Godbolt works with Claude Code much as he would with a **junior programmer**:

> *"When I collaborate with Claude Code, I find myself working with it much as I would with a junior programmer. I provide context, direction, and quality control. The AI handles implementation details."*

This framing leads to his **Junior Developer Dilemma**: if AI handles entry-level tasks, how do newcomers gain experience? His solutions:
- **Revive apprenticeship**: Pair juniors with seniors to learn AI direction and architectural thinking
- **Evolve education**: Teach fundamentals alongside AI collaboration and quality control
- **New entry roles**: AI supervision, output validation, workflow orchestration

> *"Companies have a vested interest in continuing to hire and develop junior talent... Without this pipeline, who will guide the AIs in the future when us old-timers retire?"*

### On AI, Assembly, and Project Stewardship

Godbolt's most philosophically rich essay addresses the controversy of adding AI features to Compiler Explorer. He built an **"Explain with Claude" pane** that takes source code + compiled assembly + compilation options and generates beginner-friendly explanations. The architecture is "Claude all the way down" — a backend service (written with Claude Code) crafts prompts for a high-capability Claude model, which generates explanations delivered via a simpler, cost-effective model.

**Community reaction was polarized**:
- Some found it incredibly useful for learning assembly
- Others raised concerns about AI hallucinations, training data ethics, and environmental impact

Godbolt's stewardship philosophy:

> *"Compiler Explorer belongs to its community, and I genuinely want to consider everyone's perspectives. But as the project's maintainer, I sometimes face the uncomfortable reality of having to make decisions that not everyone will love."*

His guardrails for the feature:
- **Strictly opt-in** — no forced integration
- **Transparent disclaimers** — clear about data flow, processing methods, and experimental status
- **Focused scope** — specifically for assembly-intimidated users

On AI hallucinations vs. "lying":

> *"The 'AI lies' critique particularly puzzles me. Yes, AI can produce incorrect information, but calling it 'lying' implies intentionality. It doesn't seem right to simultaneously argue that AI can't think and that it deliberately deceives."*

And with characteristic self-deprecation:

> *"If a human assembly expert explained the same code, they'd also have a decent chance of making mistakes. I know I certainly do, especially early in the morning before coffee when I'm arguably just a biological token prediction machine myself."*

### Technical Deep Dives

Godbolt's blog posts are distinguished by their **granular technical depth**. The Advent of Compiler Optimisations series alone covered:

- **Inlining** — "the ultimate optimisation" — and when it causes code bloat
- **Loop-invariant code motion (LICM)** — and when aliasing prevents it
- **Partial inlining** — optimizing only the hot path of a function
- **Tail call optimization** — "chasing your tail" to eliminate stack frames
- **Unswitching loops** — duplicating loops around conditionals for performance
- **Population count** — replacing loops with single instructions
- **Induction variables** — rewriting loops to avoid expensive calculations
- **Division avoidance** — replacing division with multiplication tricks
- **ARM barrel shifter** — architectural features compilers exploit
- **Constant multiplication** — avoiding actual multiply instructions
- **XOR register zeroing** — why compilers love `xor eax, eax`
- **Address calculation** — why adding on x86 isn't as obvious as it seems
- **Pattern recognition** — compilers seeing through obfuscated code

### Blog Modernization with Claude

Godbolt used Claude AI to **rewrite his decade-old Python blog generator** into a modern system. He published the code unedited (except for British spellings and a couple of links) as a transparency experiment. The AI even generated a draft blog post, which he published as evidence of the tool's capability — and its limitations.

## Key Quotes

> *"One of our core principles is that we never retire compiler versions. Once a compiler goes up on Compiler Explorer, it stays there forever."*

> *"The semiconductor design evolution didn't eliminate jobs — it enabled creations of previously impossible complexity."*

> *"When I collaborate with Claude Code, I find myself working with it much as I would with a junior programmer."*

> *"Compiler Explorer belongs to its community, and I genuinely want to consider everyone's perspectives. But as the project's maintainer, I sometimes face the uncomfortable reality of having to make decisions that not everyone will love."*

> *"I'm arguably just a biological token prediction machine myself [before coffee]."*

> *"It's Claude all the way down."*

> *"The 'AI lies' critique particularly puzzles me. Yes, AI can produce incorrect information, but calling it 'lying' implies intentionality."*

> *"In the end, open source is about building things that help people learn and create."*

## Recent Themes (2024–2026)

| Theme | Posts | Key Argument |
|-------|-------|-------------|
| **Compiler Explorer at scale** | "How Compiler Explorer Works in 2025" (Jun 2025) | 92M compilations/year, 81 languages, 4,724 compiler versions, full infrastructure breakdown |
| **AI in developer tools** | "On AI, Assembly, and the Art of Project Stewardship" (May 2025) | Opt-in AI features with transparent guardrails; maintainer decision-making in open source |
| **AI coding parallels** | "AI coding: parallels with the Semiconductor Revolution" (Apr 2025) | AI as abstraction layer, not job replacement; junior developer pipeline concerns |
| **Blog modernization** | "Blog Modernisation with Claude" (Apr 2025) | Transparent AI-assisted code generation and publishing |
| **Compiler optimization education** | "Advent of Compiler Optimisations 2025" (Dec 2025) | 25-day deep dive into how compilers transform code |
| **Cost transparency** | "Compiler Explorer Cost Transparency" (Jun 2025) | $37K/year to serve 8M backend compilations/month |
| **URL permanence** | "Compiler Explorer and the Promise of URLs That Last Forever" (May 2025) | Manual migration of 12K+ legacy goo.gl links |
| **Project governance** | "Compiler Explorer, LLC" (Mar 2024) | Formalizing project structure for long-term sustainability |
| **Conference keynotes** | ACCU, C++ on Sea, CppCon, Jane Street talks | Teaching an Old Dog New Tricks; C++: Some Assembly Required; Microarchitecture |

## Style & Approach

Godbolt's writing is characterized by:
- **Deep technical authenticity** — writes from decades of hands-on compiler and systems programming experience
- **Infrastructure transparency** — publishes costs, architecture diagrams, and operational details
- **Historical perspective** — connects modern tools to computing history (BBC Micro, MOS 6502, GCC 1.27 from 1987)
- **Educational mission** — everything he writes is designed to help others learn
- **AI transparency** — discloses LLM assistance prominently ("Written with LLM assistance. Details at end.")
- **Humor and self-deprecation** — "biological token prediction machine," "Claude all the way down"
- **Commitment to permanence** — never retires compiler versions, fights link rot, preserves legacy URLs
- **Open-source stewardship** — treats Compiler Explorer as a community resource, not a personal project

## Related

- [[compiler-explorer]] — Interactive assembly visualization tool (godbolt.org)
- [[ai-as-abstraction-layer]] — Godbolt's semiconductor design analogy for AI coding
- [[open-source-stewardship]] — Project governance and community decision-making
-  — How modern compilers transform and optimize code
-  — Fighting link rot as a civilizational responsibility
-  — Formal entity for Compiler Explorer governance
- [[harness-engineering]] — Related to Mitchell Hashimoto's AGENTS.md approach

## Sources

- [How Compiler Explorer Works in 2025](https://xania.org/202506/how-compiler-explorer-works) (Jun 2025)
- [On AI, Assembly, and the Art of Project Stewardship](https://xania.org/202505/ai-and-compiler-explorer) (May 2025)
- [AI coding: parallels with the Semiconductor Revolution](https://xania.org/202504/ai-in-coding) (Apr 2025)
- [Blog Modernisation with Claude](https://xania.org/202504/blog-modernisation-with-claude) (Apr 2025)
- [Compiler Explorer Cost Transparency](https://xania.org/Compiler-Explorer) (Jun 2025)
- [Advent of Compiler Optimisations 2025](https://xania.org/AoCO2025) (Dec 2025)
- [2025 in Review](https://xania.org/) (Dec 2025)
- [Compiler Explorer, LLC](https://xania.org/Compiler-Explorer) (Mar 2024)
- [xania.org/about](https://xania.org/) (footer)
