---
title: "Max Woolf"
tags: [- person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Max Woolf

## Overview

**Max Woolf** (@minimaxir) is a data scientist, open-source developer, and technical blogger based in San Francisco. He is a Senior Data Scientist at [[concepts/buzzfeed]], where he has applied machine learning to creative projects including StyleGAN-generated "fake boyfriends" and AI-powered art quizzes. He is also a prolific open-source contributor and the author of several widely-used Python and R libraries, most notably **textgenrnn** (neural text generation) and **big-list-of-naughty-strings** (edge-case testing data).

Woolf's blog at minimaxir.com is characterized by **data-driven skepticism, empirical benchmarking, and a willingness to challenge industry narratives with hard numbers**. He approaches every claim — whether about AI capabilities, library performance, or platform policies — with the same methodology: build a test, measure the results, publish the data, and let the numbers speak. His tone is often described as "snarky" (his own characterization), but this masks a rigorous commitment to evidence-based technical analysis.

His projects are funded through , and he is notable for being one of the few independent technical bloggers who has built a sustainable, audience-supported model for data journalism.

---

## Timeline

| Period | Key Events |
|--------|-----------|
| ~2015 | Begins publishing open-source Python/R projects; starts minimaxir.com blog |
| 2017 | Releases **textgenrnn** — neural text generation on Keras/TensorFlow; goes viral with NYT, CNN, and Lifehacker coverage |
| 2018 | Publishes "big-list-of-naughty-strings" — becomes a widely-used edge-case testing resource |
| 2019–2020 | textgenrnn reaches ~5,000 GitHub stars; used for generating recipes, board game titles, metal band names, and more |
| 2020–2022 | Shifts focus to data journalism and AI/LLM benchmarking at BuzzFeed |
| 2021 | Publishes YouTube video metadata scraping script; benchmarks AI image generation tools |
| 2023–2024 | Establishes himself as a leading independent voice in LLM benchmarking and data journalism |
| 2025 | Writes "As an Experienced LLM User, I Actually Don't Use Generative LLMs Often" — influential skeptical take; publishes benchmark analyses of AI coding tools |
| 2026 | Publishes *"An AI agent coding skeptic tries AI agent coding, in excessive detail"* — comprehensive, data-backed analysis of agentic coding workflows with Claude Opus 4.5 and GPT models |

---

## Core Ideas

### The Empirical Imperative

Woolf's defining characteristic is his **insistence on measuring everything**. Where others speculate about AI capabilities, he runs benchmarks. Where others claim productivity gains, he measures execution times. Where others trust marketing, he audits the output.

His 2026 post *"An AI agent coding skeptic tries AI agent coding, in excessive detail"* is a masterclass in this approach. Rather than accepting or rejecting AI coding tools on principle, he:

1. Set up a systematic testing framework with explicit `AGENTS.md` configuration files
2. Tested multiple projects across Python, Rust, and WASM
3. Measured actual performance improvements against established libraries
4. Published the complete methodology and results

His findings were surprising even to himself: AI-optimized implementations of UMAP, HDBSCAN, and GBDT algorithms showed **2–100x speedups** over existing Python libraries, and **2–10x improvements** over existing Rust implementations. The data forced him to revise his skepticism.

### From Skeptic to Pragmatist

Woolf's journey with AI tools is notable for its **honesty about changing his mind**. In May 2025, he wrote *"As an Experienced LLM User, I Actually Don't Use Generative LLMs Often"* — a post expressing measured skepticism about LLM utility. By February 2026, after systematically testing agentic coding with Claude Opus 4.5 and GPT-5.2 Codex, he published results showing significant, reproducible performance gains.

> "It's Not AI Psychosis If It Works"

This willingness to follow the data wherever it leads — even when it contradicts prior beliefs — is central to Woolf's intellectual approach. He doesn't perform skepticism for its own sake; he performs it until the evidence demands revision.

### The Optimization Pipeline

Woolf developed an **8-step repeatable sequence** for algorithmic development using AI agents:

1. Implement core logic + representative benchmarks (`criterion`)
2. Clean code/comments, apply initial optimizations
3. Scan crate for algorithmic weaknesses in edge cases
4. Optimize until ALL benchmarks run ≤60% of original runtime
5. Create custom tuning profiles (CPU threading, `flamegraph` profiling)
6. Add Python bindings (`pyo3` + `maturin`)
7. Benchmark against existing Python packages
8. **Anti-Cheat:** Verify output similarity against known-good implementations

This pipeline is notable because it treats AI not as a magic code generator but as a **systematic optimization tool** within a human-directed workflow. The human remains the architect — the AI is the laborer.

### The Configuration File as System Prompt

Woolf popularized the use of **`AGENTS.md`** as a persistent, project-level configuration file that dictates *how* code is written:

```markdown
**NEVER** use emoji, or unicode that emulates emoji (e.g. ✓, ✗).
**MUST** avoid including redundant comments which are tautological or self-demonstrating.
**MUST** use `uv` + `.venv` for Python projects.
**MUST** use `polars` over `pandas`.
**NEVER** include API keys or secrets in code or logs.
```

This is a significant methodological contribution to the agentic coding discourse. Rather than relying on in-context prompting for every interaction, Woolf externalizes project standards into version-controlled files that persist across sessions. This addresses the "anterograde amnesia" problem that others (like [[miguel-grinberg]]) have identified with AI tools.

### The "Literal Genie" Problem

Woolf identifies a fundamental limitation of AI coding agents: **they are literalists who cannot infer unstated requirements**.

> "You, the user, are likely subconsciously picky, and there are always functional requirements that the agent won't magically apply because it cannot read minds and behaves as a literal genie."

His solution is a **human QA loop**: agents generate code → humans test → humans screenshot bugs → humans prompt fixes → repeat. This iterative process, while labor-intensive, consistently produces high-quality results because it leverages human judgment for the tasks humans are good at (evaluating "does this feel right?") and machine capability for the tasks machines excel at (generating and optimizing code).

### The Toxic Discourse Problem

One of Woolf's most important observations about the current AI coding landscape is the **toxicity of public discourse**. He notes that empirical results showing massive, verifiable performance gains are routinely dismissed as "vibecoded slop" or "AI slop" without examination:

> "Public AI coding discourse is toxic ('vibecoded slop'), but empirical results show massive, verifiable performance gains."

> "Is there a point to me writing this blog post and working on these libraries if people will likely just reply 'tl;dr AI slop'?"

This is a genuine concern for independent researchers and developers who invest significant effort into systematic analysis, only to have their work dismissed on ideological grounds. Woolf's response is to **publish even more detail** — his subtitle "in excessive detail" is both a joke and a serious methodological commitment to making his work irrefutable through transparency.

### Niche Expertise and the Gap in Resources

Woolf identifies a persistent gap in technical education: **there are few resources for intermediate practitioners**. Using Rust as an example, he notes that the ecosystem offers excellent beginner tutorials and expert-level documentation, but "there's little between the tutorial and 'write an operating system from scratch.'" His AI-augmented approach helps bridge this gap by allowing practitioners to work in domains where they lack deep expertise while maintaining quality through systematic review.

---

## Key Quotes

> "It's Not AI Psychosis If It Works"

> "You, the user, are likely subconsciously picky, and there are always functional requirements that the agent won't magically apply because it cannot read minds and behaves as a literal genie."

> "Is there a point to me writing this blog post and working on these libraries if people will likely just reply 'tl;dr AI slop'?"

> "In software engineering, one of the greatest sins is premature optimization... But with agentic coding, we implicitly accept that our interpretation of the code is fuzzy."

> "Public AI coding discourse is toxic ('vibecoded slop'), but empirical results show massive, verifiable performance gains."

> "Agents don't cause programming atrophy; they enable tackling complex, unfamiliar domains (Rust, WASM, terminal UIs) by bridging implementation gaps."

---

## Recent Themes (2024–2026)

**2024:** Continued LLM benchmarking work. Published analyses of AI image generation tools and model performance comparisons. Maintained open-source Python and R projects.

**2025:** Wrote *"As an Experienced LLM User, I Actually Don't Use Generative LLMs Often"* — influential skeptical analysis. Began systematic testing of agentic coding workflows. Published benchmark data on Nano Banana and other image generation models. Continued data journalism work at BuzzFeed.

**2026:** Published *"An AI agent coding skeptic tries AI agent coding, in excessive detail"* — comprehensive analysis of agentic coding with Claude Opus 4.5, documenting 2–100x algorithmic speedups. Developed the `AGENTS.md` configuration pattern for project-level AI guidance. Began work on **rustlearn** — a comprehensive Rust ML library with Python/JS bindings. Explored model chaining techniques (Codex optimizes → Opus re-optimizes → Opus verifies). Published analysis of LLM context window utilization (32,768 input tokens for Nano Banana Pro).

---

## Related

[[concepts/textgenrnn]] — Neural text generation library (Keras/TensorFlow), ~5,000 GitHub stars
[[concepts/buzzfeed]] — Woolf's employer; Senior Data Scientist working on AI initiatives
[[concepts/polars]] — Python data processing library Woolf advocates over pandas
 — Language Woolf has been exploring with AI-assisted development
[[miguel-grinberg]] — Fellow blogger with contrasting views on AI coding tools
 — Python implementation; Woolf's benchmarks compare against C/C++ implementations
CUDA — NVIDIA GPU computing platform; Woolf explores agent-driven algorithm porting
 — Funding platform supporting Woolf's independent research
big-list-of-naughty-strings — Woolf's widely-used edge-case testing data repository

---

## Sources

- [minimaxir.com](https://minimaxir.com) — Primary blog
- *An AI agent coding skeptic tries AI agent coding, in excessive detail* (February 2026)
- *As an Experienced LLM User, I Actually Don't Use Generative LLMs Often* (May 2025)
- *Can LLMs write better code if you keep asking them to "write better code"?* (earlier experimental post)
- [textgenrnn on GitHub](https://github.com/minimaxir/textgenrnn) — Neural text generation library
- [big-list-of-naughty-strings on GitHub](https://github.com/minimaxir/big-list-of-naughty-strings)
- GitHub: [@minimaxir](https://github.com/minimaxir)
- [Patreon: minimaxir](https://patreon.com/minimaxir) — Project funding
- BuzzFeed AI initiatives — StyleGAN-generated fake boyfriends, AI art quizzes
