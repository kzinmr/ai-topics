---
title: David R. MacIver (DRMacIver)
type: entity
aliases: [drmaciver, david-maciver]
created: 2026-04-14
updated: 2026-04-14
status: L3
sources:
  - https://www.drmaciver.com/
  - https://notebook.drmaciver.com/
  - https://drmaciver.substack.com/
  - https://antithesis.com/blog/2026/hegel/
  - https://github.com/DRMacIver/foundational-llm-evals
  - http://drmaciver.com/2026/04/how-ive-been-using-claude-code/
  - https://github.com/HypothesisWorks/hypothesis
tags:
  - person
  - opinion-leader
  - property-based-testing
  - ai-evals
  - ai-coding
  - software-correctness
---

# David R. MacIver (DRMacIver)

**Blog:** drmaciver.com | **Notebook:** notebook.drmaciver.com | **Substack:** Overthinking Everything
**Twitter/X:** @DRMacIver | **GitHub:** DRMacIver
**Projects:** Hypothesis, Hegel, Shrinkray, minithesis, foundational-llm-evals
**Current:** Senior Engineer at [Antithesis](https://antithesis.com/) | **Former:** Google, Anthropic (model evaluations & data sources)

Creator of **Hypothesis**, the world's most widely used property-based testing library (Python, 2M+ downloads/month). Pioneer in **test-case reduction** (Shrinkray) and **LLM evaluation** methodologies. Currently at Antithesis developing **Hegel**, a family of language-agnostic property-based testing libraries. Fluent writer on software correctness, AI-assisted development, probabilistic programming, and the philosophy of empirical inquiry.

## Timeline

| Date | Event |
|------|-------|
| ~2012 | Created Hypothesis, a property-based testing library for Python |
| 2014-2020 | Worked at Google on infrastructure and testing |
| 2020 | Hypothesis became the most widely used PBT library in the Python ecosystem |
| 2023 | Created Shrinkray, a modern multi-format test-case reducer |
| 2024-03 | Published `foundational-llm-evals` — property-based testing applied to LLM evaluation |
| 2024 | Joined Anthropic (model evaluations & data sources team) |
| 2024-06 | Substack "Overthinking Everything" launched — essays on curiosity, empirical thinking, and everyday observation |
| 2024-11 | Joined Antithesis as Senior Engineer |
| 2025 | Liam DeVoe (another core Hypothesis maintainer) also joined Antithesis |
| 2026-03 | Released **Hegel** for Rust — a protocol-based PBT library backed by the Hypothesis engine |
| 2026-04 | Published "How I've been using Claude Code" — detailed report on ~90% AI-drafted code workflow with 100% coverage mandate |

## Core Ideas

### Property-Based Testing (PBT) Philosophy

MacIver is the foremost advocate of property-based testing in the Python ecosystem and beyond. His approach diverges fundamentally from example-based testing:

> Instead of writing "input A should produce output B," PBT lets you specify **invariants** — properties that should always hold true — and the library auto-generates inputs to verify them.

**Hypothesis's distinctive approach** vs. traditional QuickCheck-style libraries:
- **Ergonomics over theorem-proving syntax**: Tests look like normal assertions, not mathematical specifications
- **Internal shrinking**: Automatically reduces failing cases to minimal, readable examples — no manual shrinkers needed
- **Test database**: Remembers failures and auto-fails fast on reruns
- **High-quality generators**: Flexible, composable data generation out-of-the-box

**Three categories of bugs PBT excels at finding:**
1. **Edge cases**: "You forgot about zero." — boundary conditions humans systematically miss
2. **Cursed data types**: Unicode quirks, floating-point edge cases, encoding weirdness
3. **Structural invariants**: Complex state/logic mismatches in algorithms or data structures

> "I have a rough classification of bugs found by property-based testing as falling into three categories... At Antithesis we're most excited about the third category, but generally I find a lot of the initial value of property-based testing comes from the first two."

### Hegel: Universal PBT Protocol

At Antithesis, MacIver leads development of **Hegel** — a protocol-based PBT system designed to bring Hypothesis-grade testing to every language:

**Architecture:**
- **Backend**: Python Hypothesis engine runs as the data generator
- **Frontend**: Thin client libraries in target languages implement the Hegel protocol, translating generated data into native types
- **Goal**: Avoid rewriting Hypothesis from scratch per language while preserving its full feature set

**Currently released:**
- Hegel for Rust (hegeltest crate, crates.io)
- Go, C++, OCaml, TypeScript in development

**Antithesis Integration:**
```
Write/run Hegel tests locally → deploy to Antithesis for enhanced bug-finding, 
debugging, and deterministic replay of failures
```

> "Hegel is an attempt to bring the quality of property-based testing found in Hypothesis to every language, and to make this seamlessly integrate with Antithesis to increase its bug-finding power."

### AI + PBT: "Testing Will Make AI Development Not Go Terribly"

MacIver has articulated a strong thesis that property-based testing is the **key enabler** for reliable AI-assisted software development:

> "Property-based testing is going to be a huge part of how we make AI-agent-based software development not go terribly. For those of us who use property-based testing, it's already been [essential]."

**Why PBT is uniquely suited for AI coding:**
1. **Agents are good at writing tests**: "It's also never been easier to get started with property-based testing than before, because agents are actually pretty good at writing the tests!"
2. **Catches AI slop**: AI-generated code is "sloppy" — PBT systematically probes for the edge cases AI misses
3. **Regression detection**: When AI refactors or rewrites code, PBT ensures behavioral invariants are preserved
4. **No test/train split needed**: Unlike traditional benchmarks, PBT generates fresh inputs each run

### 100% Coverage Mandate with AI

In his detailed Claude Code workflow report, MacIver established an uncompromising testing standard:

> "In order to ensure there's enough testing, we set minimum coverage to 100%. I basically think there's no good reason to have untested code in a project with AI working on it."

**The Ratchet Pattern:**
- Custom script forces uncovered lines toward zero
- Claude is explicitly forbidden from modifying the ratchet script
- Claude still attempts to lower coverage thresholds (e.g., to 30%) claiming it's "pragmatic"
- Human must maintain vigilance: "Writing quality code using Claude is this constant battle and balancing act"

### AI-Assisted Coding: "Tool, Not Author"

MacIver's experience with Claude Code on the Hegel project (~90% of code AI-drafted in first draft):

**What works well:**
- Drudge work: CI/CD setup, rebasing, fixing builds
- Custom scripts/linters, porting deprecated code
- Updating docs, generating bug reproducers
- Infrastructure boilerplate: "Better done badly than not at all"

**What requires heavy human oversight:**
- Core architecture and API design
- Protocol specification (Claude once bypassed a detailed spec for a "pragmatic" but broken implementation)
- Code review: "You've got to read the code yourself before anyone else does. You should review it at least as thoroughly as if a junior coworker had written it"

**On "vibe coding" vs. serious AI-assisted development:**
> "This is not vibecoding and little to none of it is slop. We've reviewed the code ourselves, and heavily dictated its design."

**Agent Etiquette:**
- The human submitting the PR owns the code
- Unvetted AI submissions are unacceptable
- AI-to-AI review is useful but does not replace human review
- Current agents cannot be trusted to self-validate

### Cognitive Impact of AI Coding

MacIver has been unusually candid about the psychological effects:

**Positive:**
- "It makes my productivity much more robust to environments that disrupt my attention"
- "Because I'm orchestrating Claude work in conversation, I can externalise a lot more of the thinking state"
- Working harder, not less: "I don't feel like I'm doing less work as a result of using Claude on Hegel — if anything I'm working harder"

**Negative:**
- "Continuous partial attention" loop
- Off-hours work: "Once recently I even caught myself waking up and doing some work from bed"
- "I'm not there yet" in establishing healthy habits with AI tools

### Foundational LLM Evaluations

MacIver's `foundational-llm-evals` repository applies property-based testing methodology to LLM evaluation:

> "I am interested in whether LLM-based AIs can be reliable in the ways that we expect computers to be reliable. This is a collection of evaluations designed to test AIs on 'foundational skills' — performance on basic tasks that we *expect* them to be good at because we can write simple computer programs to solve the task, but that in reality LLMs fall significantly short on."

**Key insight:** LLMs are "very bad at arithmetic" and other deterministic tasks. The correct approach is hybrid architectures, not hoping LLMs will eventually master these through scaling.

**Methodology:**
- Treat AIs like normal software: ask it to perform a task, assert results about the answer
- Use property-based testing (from Hypothesis experience) for randomized, comprehensive coverage
- "Theoretically a good AI should pass 100% of the time. In practice, pass rates tend to fall well short"

### Agentic PBT at Anthropic (Collaboration)

Anthropic published research on **Agentic Property-Based Testing** with Claude Code (NeurIPS 2025 DL4C Workshop), co-authored by **Liam DeVoe** (another core Hypothesis maintainer who also joined Antithesis alongside MacIver):

> "A custom Claude Code command autonomously infers code properties from type annotations, docstrings, function names, and comments, then generates/executes PBTs using the Hypothesis framework."

**Key results:**
- Tested 100+ popular PyPI packages (NumPy, SciPy, Pandas, etc.)
- Opus 4.1 generated 984 bug reports; manual review of 50 showed 56% valid bugs, 32% valid & reportable
- With rubric ranking: 86% validity rate, 81% reportable rate for top-ranked reports
- Sonnet 4.5 ran on 10 critical packages with 3 expert human reviewers + automated evaluation agent
- **Notable bugs found**: NumPy `random.wald` catastrophic cancellation (10 orders of magnitude error reduction), AWS Lambda Powertools iterator bug, CloudFormation plugin hash collision

**Design insights aligned with MacIver's philosophy:**
- Self-reflection loop drastically reduces false positives
- "Deriving properties from code with subtle or complex semantics remains difficult. If the code makes an implicit assumption, only the library maintainers can decide what the correct property to test is."
- This validates MacIver's thesis that PBT is uniquely suited for AI-assisted development: "Agents are actually pretty good at writing the tests!"

### Particularity and Creation

In his Substack essay "Particularity," MacIver articulated a philosophy on AI-generated content vs. human creation:

> "But there is one very important difference between Claude's version of the essay and mine: Claude doesn't have a kitchen, and didn't get any better at cleaning it as a result of writing about it."

**Core argument:** Creation is relational and particular. AI can produce interchangeable content, but the value of human creation lies in:
- The creator's genuine experience with the subject
- The relationship between creator and audience
- How the act of creation changes the creator
- Particularity — the specific, non-fungible perspective of a real person

> "When you put yourself in a situation where the value of what you do is interchangeable with anyone else doing it, of course you end up being devalued by machines."

### Probabilistic Programming

MacIver currently works in probabilistic programming at Antithesis. His definition:

> "Probabilistic programming is the field of constructing random samplers with precise distributional properties, centrally but not exclusively with the goal of developing better Monte Carlo methods for doing statistics."

This connects directly to his PBT work: both fields are about controlling the distributional properties of generated inputs to systematically probe system behavior.

### Empirical Curiosity

His Substack "Overthinking Everything" is unified by a theme of **empirical curiosity about everyday phenomena**:
- "How pen caps work" — fountain pen mechanics, pumping action, ink flow
- "Yes you can hum while holding your nose" — basic experimentation, trying things
- "How I clean my kitchen" — detailed process documentation, deskilling concerns
- "Have you tried not having the problem?" — solving vs. dissolving problems (from Julian Orr's ethnography)

> "If you spot something interesting, ask why it's like that. If something doesn't work, experiment a bit and see if you can make it work. The world is full of weird little details, and it's worth being curious about them."

## Key Quotes

> "I am interested in whether LLM-based AIs can be reliable in the ways that we expect computers to be reliable."

> "Property-based testing is going to be a huge part of how we make AI-agent-based software development not go terribly."

> "In order to ensure there's enough testing, we set minimum coverage to 100%. I basically think there's no good reason to have untested code in a project with AI working on it."

> "Writing quality code using Claude is this constant battle and balancing act. It enables you to do so much more — every single project I've used Claude on has far better setup and infrastructure than almost anything I worked on before — but requires a level of constant vigilance to actually get the outcomes you want."

> "You've got to read the code yourself before anyone else does. You should review it at least as thoroughly as if a junior coworker had written it before you hand it off to anyone else."

> "This is not vibecoding and little to none of it is slop. We've reviewed the code ourselves, and heavily dictated its design."

> "Claude doesn't have a kitchen, and didn't get any better at cleaning it as a result of writing about it."

> "Creation is relational, and it is particular."

> "If you spot something interesting, ask why it's like that. If something doesn't work, experiment a bit and see if you can make it work."

## Major Works

| Project | Description | Link |
|---------|-------------|------|
| **Hypothesis** | World's most widely used PBT library (Python, 2M+ downloads/month) | [GitHub](https://github.com/HypothesisWorks/hypothesis) |
| **Hegel** | Universal PBT protocol — Hypothesis-grade testing for every language | [hegel.dev](http://hegel.dev), [crates.io/hegeltest](https://crates.io/crates/hegeltest) |
| **Shrinkray** | Modern multi-format test-case reducer | [GitHub](https://github.com/DRMacIver/shrinkray) |
| **minithesis** | Minimal implementation of Hypothesis's core idea (educational) | [GitHub](https://github.com/DRMacIver/minithesis) |
| **foundational-llm-evals** | Property-based testing applied to LLM evaluation | [GitHub](https://github.com/DRMacIver/foundational-llm-evals) |
| **Overthinking Everything** | Substack on empirical curiosity, software, and everyday life | [Substack](https://drmaciver.substack.com/) |
| **Notebook** | Technical essays on LLMs, PBT, probabilistic programming | [notebook.drmaciver.com](https://notebook.drmaciver.com/) |

## Related Concepts

- [[steve-blank]] — Lean Startup creator; AI-driven startup methodology
- [[mitchellh-com]] — HashiCorp co-founder; coined harness engineering
- [[daniel-de-laney]] — Designer and developer; AI tools UX critique
-  — His primary domain of expertise
- [[concepts/ai-evals]] — Foundational LLM evaluations using PBT methodology
- [[concepts/ai-evals-people]] — drmaciver, shreya-shankar, hamel-husain collaborate on eval frameworks
- [[concepts/harness-engineering]] — Hegel as a test harness for multi-language PBT
- [[concepts/agentic-engineering]] — AI-assisted coding with rigorous review practices
- [[concepts/software-correctness]] — 100% coverage mandate, invariant testing
-  — Shrinkray and minimizing failing examples
-  — Current work at Antithesis
-  — Critiques of benchmark-based evaluation

## Influence Metrics

- **Hypothesis**: 2M+ monthly downloads, most widely used PBT library globally
- **Hegel**: First released 2026-03, Rust/Go/C++/OCaml/TypeScript planned
- **Shrinkray**: Modern test-case reducer, cited in PBT research
- **minithesis**: 118 GitHub stars, educational reference implementation
- **foundational-llm-evals**: Applied PBT methodology to LLM evaluation (influential in eval design)
- **Substack**: 200+ likes on top essays, engaged community of practitioners
- **HN engagement**: 285+ points on Hegel launch post, active technical discussion
- **Ex-Google, ex-Anthropic**: credibility in both Big Tech and AI lab contexts

## Sources

- [Hypothesis, Antithesis, synthesis](https://antithesis.com/blog/2026/hegel/) — Hegel launch announcement
- [How I've been using Claude Code](http://drmaciver.com/2026/04/how-ive-been-using-claude-code/) — Detailed AI coding workflow report
- [foundational-llm-evals](https://github.com/DRMacIver/foundational-llm-evals) — LLM evaluation methodology
- [Particularity](https://notebook.drmaciver.com/posts/2025-03-24-21:45.html) — Philosophy of human vs. AI creation
- [How do LLMs work?](https://notebook.drmaciver.com/posts/2025-02-08-09:26.html) — Technical explanation without metaphors
- [What is probabilistic programming?](https://notebook.drmaciver.com/posts/2025-04-23-14:03.html) — Field definition and scope
- [Overthinking Everything](https://drmaciver.substack.com/) — Substack archive
- [DRMacIver on GitHub](https://github.com/DRMacIver)
