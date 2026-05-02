---
title: "Theodoros Galanos"
description: "AI researcher and practitioner at the intersection of harness engineering, agentic AI, and architecture/engineering/construction (AEC). Chief Science Officer at infrared.city, author of The Harness blog, creator of AEC-Bench and Lambda-RLM."
type: entity
created: 2026-05-02
updated: 2026-05-02
tags:
  - entity
  - person
  - harness-engineering
  - aec
  - rlm
  - agent-evaluation
aliases:
  - Theodore Galanos
  - "@TheodoreGalanos"
sources:
  - https://theharness.blog/about/
  - https://theharness.blog/blog/recursive-by-design/
  - https://scholar.google.com/citations?user=0jN3c4IAAAAJ&hl=en
  - raw/articles/2026-05-02_the-harness-blog_recursive-by-design.md
---

# Theodoros Galanos

**Theodoros Galanos** is an AI researcher and practitioner working at the intersection of harness engineering, agentic AI, and the Architecture, Engineering, and Construction (AEC) industry. He serves as **Chief Science Officer at infrared.city** and writes **The Harness** blog — a working notebook on harness engineering and making AI useful in real engineering practice.

## Overview

Galanos has been working at the intersection of AI, design, and engineering for over 12 years, based in Melbourne, Australia. His work focuses on the "harder middle layer between model capability and reliable real-world work" — environments, tools, verifiers, workflows, evaluation, and control surfaces for autonomous agents.

He is the author of several peer-reviewed publications in computational design and ML for architecture, and the creator of **AEC-Bench**, a multimodal benchmark for evaluating agentic systems on real-world AEC tasks. His blog post **"Recursive by Design"** introduced Lambda-RLM, a deterministic pipeline architecture that achieved 14x token reduction with +8.4% quality improvement on engineering report generation.

## Key Contributions

### Lambda-RLM (April 2026)

Introduced Lambda-RLM, a deterministic pipeline variant of Recursive Language Models where task structure is computed upfront rather than discovered by the model. The architecture comprises:

1. **Plan phase** — Reads template, measures sources, computes decomposition (0 LLM calls)
2. **Extract + Review phase** — Pulls data from bounded chunks in dependency order; contract alignment check
3. **Generate phase** — Composes sections from extractions and dependencies

**Benchmark results** (Open REPL vs Lambda-RLM on AEC report generation):

| Metric | Open REPL | Lambda-RLM | Improvement |
|--------|-----------|------------|-------------|
| Total Tokens | 740K | 53K | **14x less** |
| Input Tokens | 732K | 33K | **22x less** |
| API Calls | 48 | 27 | **1.8x fewer** |
| Quality (Reward) | 0.67 | 0.73 | **+8.4%** |

Core thesis: "The agent's reasoning architecture is itself a harness design choice. Agent design and harness design are the same problem."

### AEC-Bench

Created **AEC-Bench**, a multimodal benchmark for evaluating agentic systems on real-world tasks in Architecture, Engineering, and Construction. The benchmark revealed that the biggest performance gains come from better retrieval and document parsing, not model upgrades — and that when harness support is stripped away, performance collapses rather than degrading gracefully.

See: [[concepts/aec-bench]]

### The Harness Blog

Runs **The Harness** (theharness.blog), a blog focused on harness engineering, agent evaluation, and AI in AEC. As of April 2026, the blog has 25 posts across 6 topics, making it one of the most focused publications on AI agent harnesses in the engineering domain.

See: [[entities/the-harness-blog]]

### The "Third Axis" — Harness Self-Improvement

Explored feedback-driven harness evolution, where the harness improves itself through automated prompt optimization and system-level adaptation.

### Research Publications

- **"AEC-Bench: A Multimodal Benchmark for Agentic Systems in Architecture, Engineering, and Construction"** — arXiv:2603.29199 (2026)
- **"Architext: Language-driven generative architecture design"** — arXiv:2303.07519 (2023)
- **"A digital workflow to quantify regenerative urban design in the context of a changing climate"** — Genetic Programming Theory and Practice XX (2024)
- **"A deep-learning approach to real-time solar radiation prediction"** — The Routledge Companion to AI in Architecture (2021)
- Co-authored on wind comfort prediction, urban configuration analysis, and the InFraRed framework

## Core Theses

### Agent Design = Harness Design

The performance of AI agents in complex domains depends less on the model and more on the harness — the domain-specific tooling and reasoning architecture surrounding it. The agent's reasoning architecture (e.g., open REPL vs deterministic pipeline) is itself a harness design choice.

### Harness > Model

Domain-specific agent harnesses, not bigger models, close the AI performance gap on real engineering tasks. When harness support is stripped away, performance doesn't degrade gracefully — it collapses.

### The Model is the Easy Part

The real work is the iterative loop of measuring, reviewing, and refining the harness. Technical benchmarks are insufficient; domain experts must review the output.

## Professional Background

- **Chief Science Officer**, infrared.city — AI-driven urban environmental performance tools
- **Advanced Design Lead**, Aurecon — Engineering and design consultancy (via Google Scholar profile)
- Research in computational design, evolutionary computation, and ML for architecture
- Based in Melbourne, Victoria, Australia

## Related Entities

- [[entities/the-harness-blog]] — The Harness blog (his publication)
- [[concepts/rlm-recursive-language-models]] — RLM framework (Lambda-RLM is a variant)
- [[concepts/recursive-language-models]] — Simpler RLM concept page
- [[concepts/lambda-rlm]] — Lambda-RLM architecture concept
- [[concepts/harness-engineering]] — Broader harness engineering framework
- [[entities/alex-zhang]] — Original RLM paper author
- [[entities/raw-works]] — Raymond Weitekamp, RLM practitioner

## Community

- **Blog**: https://theharness.blog
- **X/Twitter**: @TheodoreGalanos
- **GitHub**: https://github.com/theodoros-galanos
- **LinkedIn**: https://www.linkedin.com/in/theodorosgalanos/
- **Google Scholar**: https://scholar.google.com/citations?user=0jN3c4IAAAAJ

## Sources

- [The Harness About Page](https://theharness.blog/about/) — Scraped 2026-05-02
- [Recursive by Design](https://theharness.blog/blog/recursive-by-design/) — Scraped 2026-05-02
- [Google Scholar Profile](https://scholar.google.com/citations?user=0jN3c4IAAAAJ&hl=en) — Scraped 2026-05-02
- [LinkedIn Profile](https://www.linkedin.com/in/theodorosgalanos/) — Scraped 2026-05-02
