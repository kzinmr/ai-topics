# Max Bernstein

**URL:** https://bernsteinbear.com
**Blog:** bernsteinbear.com
**Mastodon:** @maxbernstein@bernsteinbear.com
**Current:** Software Engineer (Compilers) @ **Shopify** | Hacker in Residence @ **Dartmouth College** CS Department
**Role:** Ruby committer
**Recurse Center:** Fall 2 2024

## Overview

Max Bernstein is a compiler engineer and prolific technical writer whose work spans runtime optimization, type systems, and programming language implementation. He is a core developer of **ZJIT**, Ruby's new method-level JIT compiler, and has contributed to five different Python runtimes (Skybison, Cinder, CPython, PyPy, and Pyjion).

Beyond production work at Shopify, Bernstein is deeply committed to education — teaching compilers at Dartmouth (COSC 294: Compilers for Functional Languages, Winter 2026) and sharing his learning process through an exceptionally active technical blog at bernsteinbear.com. His writing covers everything from SSA generation and register allocation to e-graphs, type inference, and systems-level debugging.

## Core Ideas

### ZJIT: A Textbook JIT for Ruby

Bernstein is one of the primary authors of **ZJIT**, Ruby's new just-in-time compiler. Unlike YJIT (which compiles YARV bytecode directly to low-level IR), ZJIT uses a **high-level SSA-based intermediate representation** and compiles entire methods rather than single basic blocks.

The design philosophy is intentionally traditional and accessible:

> "The team is making the intentional choice to build a more traditional 'textbook' compiler so it is easy for the community to contribute to."

This represents a deliberate tradeoff — ZJIT sacrifices some of YJIT's easy interprocedural type-based optimizations in exchange for a cleaner, more modular architecture that invites outside contributors. Bernstein has been transparent about ZJIT's early state, openly sharing performance numbers, design decisions, and unresolved challenges.

### Writing That Changed How He Thinks About PL

In "Writing that changed how I think about PL," Bernstein explored how the act of writing about programming languages reshaped his own understanding. This reflects a broader pattern in his work: **teaching as thinking**. His multi-part series "Compiling a Lisp" and "Writing a Lisp" (18+ parts each) demonstrate this philosophy — he doesn't just build compilers, he documents the process of understanding them.

### Scrapscript: Language Design as a Learning Vehicle

**Scrapscript** is a small programming language Bernstein has been implementing as a vehicle for exploring language design concepts. His blog chronicles building a compiler IR for Scrapscript, adding garbage collection, implementing the baseline compiler, and exploring type information for performance. The project serves as both a practical tool and a pedagogical artifact — a sandbox for trying out ideas about representation, optimization, and evaluation.

### IR Design and Intermediate Representations

In "What I talk about when I talk about IRs," Bernstein explored the design space of intermediate representations — the core abstraction that makes compilers possible. His perspective is informed by hands-on experience across multiple IRs (YARV bytecode, ZJIT's HIR, SSA, e-graphs) and a deep skepticism toward premature abstraction:

> "An IR is not a data structure. It's a way of thinking about a program."

His catalog posts — "A catalog of ways to generate SSA," "A catalog of side effects," "Walking around the compiler" — demonstrate his preference for systematic exploration over dogmatic answers. He doesn't tell you the One True IR; he shows you the landscape and helps you navigate it.

### Optimization Through Transparency

Bernstein's approach to performance optimization is characterized by **visibility and measurement**. His post on using Perfetto in ZJIT demonstrates this: rather than guessing where slowdowns occur, he built detailed tracing infrastructure to visualize side-exits, deoptimizations, and guard failures. The same philosophy appears in his work on annotating JITed code for perf/samply and his binary search technique for finding compiler bugs.

> "Visualizations are awesome. Get your data in the right format so you can ask the right questions easily."

### Multi-Runtime Experience

Having contributed to five different Python runtimes, Bernstein has a rare cross-runtime perspective. He understands that each runtime makes different tradeoffs between performance, correctness, developer experience, and maintainability. This breadth informs his work on ZJIT — he doesn't just optimize Ruby; he compares Ruby's JIT landscape to Python's, learning from both.

### Teaching Compilers

Bernstein's commitment to education extends beyond his blog. At Dartmouth, he teaches COSC 294: Compilers for Functional Languages. His teaching style mirrors his writing: start from fundamentals, build understanding incrementally, and make the invisible visible. His "Compiling a Lisp" series (14 parts) and "Writing a Lisp" series (18 parts) are among the most comprehensive open-source compiler education materials available.

## Key Quotes

> "The team is making the intentional choice to build a more traditional 'textbook' compiler so it is easy for the community to contribute to." — on ZJIT's design philosophy

> "An IR is not a data structure. It's a way of thinking about a program."

> "Visualizations are awesome. Get your data in the right format so you can ask the right questions easily." — on using Perfetto in ZJIT

> "The first rule of just-in-time compilers is: you stay in JIT code. The second rule of JIT is: you STAY in JIT code!" — on minimizing side-exits

> "I adopted the Person Biking emoji 🚴."

> "I have now contributed to five different Python runtimes (Skybison, Cinder, CPython, PyPy, and Pyjion)."

## Recent Themes (2024–2026)

- **ZJIT development** — Core contributor to Ruby's new method-level JIT compiler; merged into Ruby (May 2025), shipped in Ruby 4.0 (December 2025)
- **Compiler education** — Teaching COSC 294 at Dartmouth; extensive "Compiling a Lisp" and "Writing a Lisp" series
- **Performance visualization** — Using Perfetto for tracing JIT side-exits and deoptimizations
- **Scrapscript implementation** — Building a compiler IR, garbage collector, and baseline compiler for a small language
- **SSA and IR design** — Systematic catalogs of SSA generation methods, side effects, and IR design patterns
- **Type propagation** — Interprocedural sparse conditional type propagation (with Maxime Chevalier-Boisvert)
- **Academic publication** — "Partial Evaluation, Whole-Program Compilation" at PLDI 2025 (with Chris Fallin)
- **Recurse Center** — Half-batch participant (Fall 2 2024); part of the broader RC community
- **Open-source Python runtimes** — Continued contributions across five different Python implementations
- **Systems-level tooling** — Binary search for compiler bugs, GDB JIT interface, perf annotation

## Related

- [[ZJIT]] — Ruby's new method-level JIT compiler; Bernstein's primary current project
- [[YJIT]] — Ruby's existing basic-block JIT compiler; predecessor to ZJIT
- [[Maxime Chevalier-Boisvert]] — Co-author on type propagation work; compiler researcher
- [[Shopify]] — Employer; sponsors Ruby and Rails development
- [[Recurse Center]] — Self-directed learning community; Bernstein attended Fall 2 2024
- [[Scrapscript]] — Small language Bernstein is implementing as a learning vehicle
- [[SSA]] — Static Single Assignment form; central to ZJIT's IR design
- [[Cinder]] — Instagram's performance-oriented CPython fork; one of five Python runtimes Bernstein has contributed to
- [[Dartmouth College]] — Where Bernstein is Hacker in Residence and teaches compilers
- [[Geoffrey Litt]] — Fellow programmer-researcher; complementary focus on end-user programming vs. systems-level compilation

## Sources

- "ZJIT has been merged into Ruby" (bernsteinbear.com, May 2025)
- "ZJIT is now available in Ruby 4.0" (bernsteinbear.com, December 2025)
- "Using Perfetto in ZJIT" (bernsteinbear.com, March 2026)
- "A fuzzer for the Toy Optimizer" (bernsteinbear.com, February 2026)
- "What I talk about when I talk about IRs" (bernsteinbear.com)
- "Writing that changed how I think about PL" (bernsteinbear.com)
- "Interprocedural sparse conditional type propagation" (with Maxime Chevalier-Boisvert, Rails At Scale, 2025)
- "A catalog of ways to generate SSA" (bernsteinbear.com)
- "A catalog of side effects" (bernsteinbear.com)
- "Partial Evaluation, Whole-Program Compilation" (with Chris Fallin, PLDI 2025)
- bernsteinbear.com/about/ — Personal bio and project list
- "Compiling a Lisp" series (14 parts, bernsteinbear.com)
- "Writing a Lisp" series (18 parts, bernsteinbear.com)
- Recurse Center directory — Fall 2 2024 batch
