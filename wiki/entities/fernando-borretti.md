# Fernando Borretti

**URL:** https://borretti.me
**Blog:** borretti.me
**Identity:** Software engineer, compiler author, and writer
**GitHub:** eudoxia0
**Twitter/X:** @zetalyrae
**Bluesky:** @eudoxia.bsky.social
**Goodreads:** zetalyrae
**Hacker News:** Active commenter and submitter
**Email:** fernando@borretti.me
**LinkedIn:** fborretti
**Themes:** Programming languages, compilers, type systems, AI/LLMs, data modeling, self-improvement, fiction, information management
**Tech Stack:** Emacs, Jekyll, Sass, GitHub Pages
**Notable Project:** Austral — a systems programming language with linear types and capabilities

## Overview

Fernando Borretti is a **software engineer, compiler author, and prolific technical writer** who builds programming languages and writes deeply about software engineering practice, AI systems, and data modeling. His most significant technical project is **Austral**, a new systems programming language featuring linear types for compile-time memory and resource management, capability-based security, and strong modularity — all designed with "fits-in-head simplicity" as the guiding principle.

Borretti's intellectual project spans four domains simultaneously:
1. **The future**: "What does life look like after biology, and what does the universe look like after intelligence?"
2. **Self-improvement**: Autodidactism, lifting, productivity, time-tracking
3. **Data modeling**: Ontologies, logic, information management — "choosing the right formalisms to model the world"
4. **Software engineering**: Compilers, programming languages, type systems, parsers — "not abstractly but with the goal of improving engineering practices"

This combination is rare. Most technical writers specialize in one area; Borretti writes at the intersection of **programming language theory, AI systems analysis, personal productivity, and practical software engineering**. His writing is characterized by **deep technical rigor combined with genuine curiosity** — he'll write a 3,000-word post on the mathematical properties of linear type checkers, then publish a personal essay on using Claude as a thinking partner, then write fiction.

His blog is built with **Emacs, Jekyll, and Sass** on GitHub Pages — a classic indie web stack that reflects his preference for tools he can understand and control completely. He publishes RSS feeds, maintains a comprehensive about page, and curates a "Best Posts" list that serves as an onboarding guide for new readers.

## Timeline

| Date | Event |
|------|-------|
| Pre-2021 | Builds personal projects in C, C++, Common Lisp, Standard ML, Java, Haskell, and OCaml |
| 2021 | Publishes "Parsing with Menhir, Part I: Forth" — tutorial series on OCaml parser generation |
| 2021 | Publishes "Introducing Austral" — the language's public debut |
| 2021 | Publishes "Language Pragmatics Engineering" — on practical language design |
| 2021 | Publishes "How Austral's Linear Type Checker Works" — 600 lines of OCaml, complete algorithm walkthrough |
| 2021 | Publishes "Unbundling Tools for Thought" — data modeling and personal knowledge management |
| 2021 | Publishes "Effective Spaced Repetition" — self-improvement and learning methodology |
| 2021 | Publishes "Signed Integers are Asymmetrical" — mathematical analysis of integer representation |
| 2023 | Publishes "Lessons from Writing a Compiler" — practical compiler construction wisdom |
| 2024 | Publishes "Design of the Austral Compiler" — detailed walkthrough of the bootstrapping compiler |
| 2025 | Publishes "How I Use Claude" — quantitative analysis of AI-assisted thinking |
| 2025 | Publishes "Implementing SM-2 in Rust" — spaced repetition algorithm implementation |
| 2026 | Publishes "Letting Claude Play Text Adventures" — LLM agent architecture experimentation |
| 2026 | Publishes "Some Data Should Be Code" — critique of DSL-in-data-format anti-pattern |
| 2026 | Publishes "There Is No New Aesthetics" — cultural/philosophical essay |

## Core Ideas

### Austral: A Systems Language with Linear Types and Capabilities

Borretti's magnum opus is **Austral**, a systems programming language designed to solve a specific set of problems:
- **No memory or resource leaks** — enforced at compile time via linear types
- **Memory safety without runtime checks or garbage collection** — through ownership and borrowing
- **Resource safety** — file handles, sockets, database handles guaranteed to be closed
- **Safe concurrency** — linear types prevent data races
- **Capability-based security** — constrain what side effects a program can perform
- **Simplicity** — rules that "fit on a page of text"

The implementation is remarkable for its pragmatism:

> "OCaml sits at a comfortable point in language space for building compilers. It has all the functional programming features you want: algebraic data types and pattern matching... Like Haskell, you can write functional code; unlike Haskell, you can mutate and perform side effects pervasively."

> "The compiler is just 12,000 lines of straightforward grugbrained OCaml. Readable: the compiler is written in the least fanciful style of OCaml imaginable. There's no transdimensional optical trickery."

The linearity checking algorithm is **600 lines of OCaml** — deliberately simple, with extensive error reporting. The compiler targets C as a backend, making it portable and debuggable.

### Lessons from Writing a Compiler

Borretti's "Lessons from Writing a Compiler" is one of the most practical guides to compiler construction ever published. Key insights:

1. **Academic literature ignores the middle-end**: "The standard academic literature is most useful for the extreme frontend (parsing) and the extreme backend (SSA, instruction selection), but the middle-end is ignored. This is fine if you want to learn how to build the next LLVM. But what if you're building a compiler on top of LLVM?"

2. **OCaml is the right tool**: "OCaml sits at a comfortable point in language space for building compilers... short time to MVP."

3. **Waterfall is fine for compilers**: "Austral's compiler was written with a very unprincipled, waterfall-ish strategy: I went stage by stage, but omitting features as needed to get to 'Hello, world!' as early as possible."

4. **Environment data structures matter**: "Each compiler needs an environment data structure that works for one may be lacking for another."

5. **Error messages are a language feature**: "Writing a correct, production-quality compiler with useful diagnostics is difficult and time consuming work. However, it can be some of the most rewarding work in software engineering, because compilers communicate with the messy real world through a very narrow interface at the beginning: the parser."

### How I Use Claude: Quantitative Analysis of AI-Assisted Thinking

This post is unique in the AI writing landscape because it combines **quantitative measurement with qualitative reflection**:

> "Claude is Anthropic's AI, like ChatGPT but more capable. I was a casual user until the 23 October release (informally 'Claude 3.6'), when it crossed a quality threshold I didn't even know was there."

Borretti exports his Claude conversation history (a "massive JSON blob") and analyzes it with matplotlib (mostly generated by Claude itself). The analysis reveals:

1. **Massive increase in cumulative words written to Claude** after the 3.6 threshold
2. **Qualitative shift in usage patterns**: from occasional tool to daily collaborator
3. **Classification of conversation types**:
   - **Advice**: "Overcome anxiety, aversion, decision paralysis. Claude is really good at helping here, mostly because thinking quickly saturates: when you've thought about a problem for five minutes, you've thought about it as much as you're going to."
   - **Exploration**: "Exploring ideas together, including both vague open-ended conversations, and more concretely trying to learn something."
   - **Code**: "50% asking Claude to write something for me, and 50% using Claude as a rubber ducky: talking possibilities, tradeoffs, etc."
   - **Writing**: "Asking Claude to critique something I wrote."
   - **Lifting**: "Lifting-specific questions."

His most profound insight about AI:

> "If phones are the library of Alexandria in our pocket, Claude is like having Aristarchos of Samos on retainer."

> "Talking to Claude feels like using the Primer. And though there is no Miranda on the other side, it is no less magical."

(The "Primer" and "Miranda" references are to Neal Stephenson's *The Diamond Age* — a book about a personalized educational AI.)

### Letting Claude Play Text Adventures: Agent Architecture Experimentation

In this post, Borretti builds a system where **Claude plays text adventure games** via the Frotz interpreter. The technical architecture is elegant:

1. **Python wrapper around dfrotz** (dumb Frotz interpreter) — `stdin`/`stdout` interface
2. **Claude as the player** — reads game output, sends commands
3. **Harness design** — treating the LLM/game interaction like a chat history

The motivation is research-driven:

> "Something I think about a lot is cognitive architectures (like Soar and ACT-R). This is like a continuation of GOFAI research, inspired by cognitive science. And like GOFAI it's never yielded anything useful. But I often think: can we scaffold LLMs with cog arch-inspired harnesses to overcome their limitations?"

> "LLM agents like Claude Code are basically 'accidental' cognitive architectures: they are designed and built from the bottom up through trial and error, not from top-down cognitive science principles."

This connects to his broader interest in **building principled agent architectures** — not just prompting an LLM, but designing the scaffolding that makes LLM capabilities reliable and composable.

### Some Data Should Be Code

A critique of a common anti-pattern in infrastructure tooling:

> "A lot of things are like Makefiles: data that should be lifted one level up to become code."

> "Consider CloudFormation. Nobody likes writing those massive YAML files by hand, so AWS introduced CDK, which is literally just a library of classes that represent AWS resources. Running a CDK program emits CloudFormation YAML as though it were an assembly language for infrastructure."

> "Some people think it's cute and clever to build tiny DSLs in a data format. They're proud that they can get away with a 'simple', static solution rather than a dynamic one."

The core argument: **static data formats that grow into DSLs are a design mistake**. The right approach is to use a real programming language to generate the data format, getting type safety, modularity, abstraction, conditionals, and loops "for free."

### Signed Integers Are Asymmetrical

A mathematical analysis of integer representation that reveals a subtle but important property: **signed integers have one more negative value than positive value** (e.g., int8 ranges from -128 to +127, not -127 to +127). This asymmetry causes bugs in absolute value calculations, negation operations, and hash functions.

### Effective Spaced Repetition

Borretti implements the **SM-2 algorithm in Rust** and writes about spaced repetition as a learning methodology. This connects to his interest in **autodidacticism** — the practice of self-directed learning, which he considers essential for a career in technology.

## Key Quotes

> "OCaml is the right tool for building compilers. Like Haskell, you can write functional code; unlike Haskell, you can mutate and perform side effects pervasively."

> "The compiler is just 12,000 lines of straightforward grugbrained OCaml."

> "If phones are the library of Alexandria in our pocket, Claude is like having Aristarchos of Samos on retainer."

> "LLM agents like Claude Code are basically 'accidental' cognitive architectures.'"

> "A lot of things are like Makefiles: data that should be lifted one level up to become code."

> "Writing a correct, production-quality compiler with useful diagnostics is difficult and time consuming work. However, it can be some of the most rewarding work in software engineering."

> "I approach things as a quant, systems thinker, and anarchist. I mean that I'm strongly in favour of direct democracy, liberty, non-violence, and solidarity."

> "The future: what does life look like after biology, and what does the universe look like after intelligence?"

## Writing Style & Philosophy

Borretti writes with **intellectual depth and technical precision**. Characteristics:

- **Rigorous analysis** — mathematical derivations, algorithm walkthroughs, quantitative measurement
- **Honest self-assessment** — "I've a whole graveyard of half-finished compiler projects"
- **Practical orientation** — "not abstractly but with the goal of improving engineering practices"
- **Cross-disciplinary thinking** — connects cognitive science to AI agents, integer math to compiler design
- **Literary references** — Stephenson, Waterhouse paintings, classical philosophy
- **Willingness to be wrong** — publishes failed projects and dead ends alongside successes

His blog is structured around **projects, articles, and fiction** — reflecting his belief that technical writing, creative writing, and software building are complementary activities, not competing ones.

## Technical Breadth

- **Programming Languages**: Austral (OCaml compiler), type systems, linear types, capability-based security
- **Compilers**: Parsing (Menhir), lexing (ocamllex), semantic analysis, code generation, bootstrapping
- **AI/LLMs**: Claude usage patterns, agent architectures, cognitive scaffolding, quantitative analysis
- **Systems Programming**: OCaml, Rust, C, memory management, resource safety
- **Data Modeling**: Ontologies, logic, information management, formalisms
- **Self-Improvement**: Spaced repetition (SM-2), time-tracking, productivity, autodidacticism
- **Infrastructure**: Makefiles, build systems, CI/CD, CloudFormation, GitHub Actions
- **Web Publishing**: Emacs, Jekyll, Sass, GitHub Pages, RSS feeds

## Recent Themes (2024–2026)

- **Compiler construction**: Austral compiler design, OCaml best practices, bootstrapping
- **AI-assisted development**: Quantitative analysis of Claude usage, agent architecture experiments
- **Cognitive scaffolding**: Building principled agent architectures inspired by cognitive science
- **Data-as-code**: Critiquing DSL-in-data-format anti-patterns across infrastructure tooling
- **Spaced repetition**: SM-2 implementation in Rust, learning methodology
- **Text adventures as AI eval**: Using interactive fiction to test LLM agent capabilities
- **Fiction writing**: Creative work alongside technical writing

## Related

- [[Austral]] — Systems programming language with linear types and capabilities
- [[Programming Languages]] — Type systems, compilers, parsers, semantic analysis
- [[AI Agents]] — Cognitive architectures, LLM scaffolding, agent evaluation
- [[Compiler Construction]] — OCaml, Menhir, bootstrapping, middle-end design
- [[Spaced Repetition]] — SM-2 algorithm, learning science, productivity
- [[Data Modeling]] — Ontologies, logic, information management
- [[Systems Programming]] — Memory safety, resource management, capability-based security

## Podcasts & Media

- **Func Prog Podcast #6** — Discussing Austral and functional programming
- **Glasp Talk #12** — Technical writing and knowledge management
- **The Stewart Mackenzie Indaba #31** — Software engineering and programming languages

## Influence

- Austral is cited as one of the more interesting new systems languages, particularly for its linear type system and capability-based security
- "Lessons from Writing a Compiler" and "Design of the Austral Compiler" are frequently referenced by language implementers
- His quantitative analysis of Claude usage is one of the most data-driven pieces of AI writing available
- The blog's cross-disciplinary approach (compilers + AI + self-improvement + fiction) is unusual and valuable
- Active on Hacker News, Bluesky, and Mastodon, contributing to technical discussions across platforms

## Sources

- borretti.me — Primary blog and project repository
- borretti.me/about/ — Author biography, interests, and contact information
- "Lessons from Writing a Compiler"
- "Design of the Austral Compiler"
- "How Austral's Linear Type Checker Works"
- "Introducing Austral: A Systems Language with Linear Types and Capabilities"
- "How I Use Claude"
- "Letting Claude Play Text Adventures"
- "Some Data Should Be Code"
- "Signed Integers are Asymmetrical"
- "Effective Spaced Repetition"
- "Implementing SM-2 in Rust"
- "Unbundling Tools for Thought"
- "Language Pragmatics Engineering"
- "There Is No New Aesthetics"
- Func Prog Podcast #6, Glasp Talk #12, The Stewart Mackenzie Indaba #31
