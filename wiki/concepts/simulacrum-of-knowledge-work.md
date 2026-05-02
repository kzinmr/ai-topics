---
title: "Simulacrum of Knowledge Work"
created: 2026-05-02
updated: 2026-05-02
tags:
  - concept
  - ai-in-workplace
  - llm-evaluation
  - incentive-design
aliases:
  - simulacrum-of-knowledge-work
  - Goodhart's Law in AI
related:
  - [[entities/onehappyfellow]]
sources:
  - raw/articles/2026-04-25_onehappyfellow-simulacrum-of-knowledge-work.md
  - https://blog.happyfellow.dev/simulacrum-of-knowledge-work/
---

# Simulacrum of Knowledge Work

> "We have built a working simulacrum of knowledge work."

The **Simulacrum of Knowledge Work** is a critical concept describing how LLMs have broken the proxy measures that knowledge work relies on for quality assessment. Organizations use surface-level proxies (writing quality, formatting, presentation polish) because actual quality is expensive to evaluate — and LLMs are now exceptionally good at simulating those proxies without the underlying substance.

## Summary

Knowledge work has always faced a fundamental asymmetry: the quality of someone's work is hard to judge without redoing it yourself. Organizations rely on **proxy measures** — surface quality like clear writing, well-formatted reports, proper code presentation — as affordable stand-ins for actual quality assessment. These proxies historically correlated well enough.

LLMs broke this correlation. A ChatGPT-generated market analysis reads like a top-tier consulting deliverable. AI-generated code passes a quick skim. AI-conducted code reviews surface plausible issues. The entire ritual of producing, reviewing, and validating knowledge work can now be simulated end-to-end by LLMs, with humans serving only as a thin approval layer.

## Key Ideas

### Proxy Measures in Knowledge Work

Quality assessment in knowledge work is inherently expensive — evaluating a market analysis requires domain expertise, time, and effort comparable to producing the work itself. Therefore:

- Organizations default to **cheap proxies**: writing clarity, formatting consistency, presentation polish
- These proxies historically had **high enough correlation** with actual quality to be functional
- Workers optimize for the metrics they're measured on

### LLMs Broke the Proxies

LLMs are uniquely capable of simulating the **form** of knowledge work without its **substance**:

- **Market analysis**: Reads like a top-tier consulting deliverable, may be factually empty
- **Code**: Passes a 2-second skim, may be structurally unsound
- **Code review**: Produces plausible-sounding findings, may be hallucinated
- **Report generation**: Correct dates/formatting → false sense of reliability

### The Incentive Alignment Crisis

> "Many workers, quite rationally, want to do well on whatever dimension they are being measured on. If they are judged by the surface-level quality of their work, then it's no surprise most of 'their' output will be written by LLMs."

When the measurement system is broken, rational actors optimize for the broken metrics. This creates a self-reinforcing spiral:
1. Workers produce more LLM-generated output (optimizing surface quality)
2. Less time is spent examining output deeply
3. Even less substantive quality is expected or verified
4. More incentive to produce surface-level output

### The Problem Is Recursive

LLM training itself relies on proxy measures:
- **Next-token prediction**: Optimizes for "looks like the training data"
- **RLHF**: Optimizes for "satisfies the judge"
- **Benchmarks**: Optimize for "achieves high score"

The same Goodhart dynamic applies: we are optimizing LLMs to produce output which *looks like* high quality output, not to *be* high quality.

### The Tokens-Spent Leaderboard

> "Companies are racing to be the first on the tokens-spent leaderboard."

A meta-commentary on the industry-wide dynamic where LLM adoption metrics (tokens consumed, sessions opened, Claude Code instances running) become vanity metrics that obscure the underlying question: is all this LLM-driven work actually producing *better* outcomes?

## Graph Structure Query

```
[simulacrum-of-knowledge-work] ──author──→ [entity: onehappyfellow]
[simulacrum-of-knowledge-work] ──embodies──→ [concept: goodharts-law]
[simulacrum-of-knowledge-work] ──relates-to──→ [concept: llm-evaluation]
[simulacrum-of-knowledge-work] ──relates-to──→ [concept: vibe-coding]
[simulacrum-of-knowledge-work] ──contrasts──→ [concept: compound-engineering]
```

Authored by [[entities/onehappyfellow]]. Relates to the broader [[concepts/goodharts-law]] dynamic in AI systems, the challenges of [[concepts/llm-evaluation]], the surface-quality trap of [[concepts/vibe-coding]], and contrasts with the intentional, verification-heavy [[concepts/compound-engineering-loop]].

## Related Concepts

- **Goodhart's Law** — "When a measure becomes a target, it ceases to be a good measure." The Simulacrum of Knowledge Work is a direct application of Goodhart's Law to the LLM era.
- [[concepts/llm-evaluation]] — The challenge of evaluating LLM output quality, which mirrors the human-side quality assessment problem.
- [[concepts/vibe-coding]] — A style of AI-assisted development that prioritizes throughput over code quality, exemplifying the simulacrum pattern in software engineering.
- [[concepts/compound-engineering-loop]] — A contrasting paradigm that emphasizes careful verification and human oversight.
- [[concepts/cognitive-debt]] — The cognitive cost of not understanding AI-generated code, a direct consequence of the simulacrum dynamic.

## Sources

- [Simulacrum of Knowledge Work](https://blog.happyfellow.dev/simulacrum-of-knowledge-work/) by @onehappyfellow (April 25, 2026)
- Raw article: `raw/articles/2026-04-25_onehappyfellow-simulacrum-of-knowledge-work.md`
