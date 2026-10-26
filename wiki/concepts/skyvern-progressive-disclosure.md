---
title: "Skyvern Progressive Disclosure (Deleting RAG from a Browser Agent)"
created: 2026-10-26
updated: 2026-10-26
type: concept
tags: [concept, browser-agent, agentic-engineering, context-engineering, prompt-caching, token-economics, retrieval, performance]
sources:
  - raw/articles/2026-10-26_skyvern_skyvern-progressive-disclosure.md
confidence: high
---

# Skyvern Progressive Disclosure (Deleting RAG from a Browser Agent)

**Progressive disclosure for browser agents**: an architecture pattern where, instead of pre-processing the page into a condensed "actionable elements" context (screenshot + annotation + element list, i.e. a RAG-style transformation) on every turn, the agent is given raw access and *pulls* only what each turn needs. Skyvern (YC S23, Ikonomos Inc.) rewrote Skyvern from scratch using Earendil's **Pi** as inspiration and A/B-tested the result in production (blog post 2026-10-01, updated 10-06; HN 21 pts 10-24).

## Headline numbers (Skyvern 2.0 → 3.0)

| Metric | Skyvern 2.0 | Skyvern 3.0 | Change |
|---|---|---|---|
| Mean run time | 593 s | 262 s | **2.3× faster** |
| Cost per run | $0.039 | $0.0302 | **−22.5%** |
| Screenshot usage in LLM calls | 27% | 2.7% | **−90%** |
| Tokens per run | 188K | 286K | **+52%** |
| Turns per run | 6.4 | 23 | **3.59×** |
| Tokens per turn | 29K | 12K | −59% |
| Prompt cache hit rate | 27% | 79.7% | **+195%** |

## Why faster-and-cheaper-despite-more-tokens works

1. **Vision encoders are the latency tax.** Image-bearing LLM calls route through a vision encoder ~1.7× slower than text-only encoders; cutting screenshot usage from 27% to 2.7% of calls removes most of that.
2. **Small, stable turns are cacheable.** Loading full screenshots/HTML every turn poisons the prompt prefix. Removing them let nearly 80% of prompt tokens hit cache — and cached tokens carry a ~70% discount, which more than pays for the 52% token increase.
3. **More, smaller turns beat fewer, fatter ones.** 23 turns × 12K tokens outperformed 6.4 turns × 29K tokens: the RAG condensation step was itself the error source ("worked great *if* you could identify every interactable element with 100% accuracy" — they couldn't).

This makes prompt caching ([[concepts/prompt-caching]]) — not retrieval quality — the dominant cost lever in agent harness design, and gives a concrete, measured version of the [[concepts/bitter-lesson-agent-harnesses]] "the less you build, the more it works" argument.

## Limits & roadmap

- Skyvern is explicit that browser agents are **not solved** — cost, speed, and accuracy all have headroom.
- Next exploration: **system-one models** (cf. [[concepts/system-one-models]], Jev-class) for browser-agent decision steps; today's generation is limited to 64K context and no image processing, causing unacceptable accuracy loss, but they expect viability within 6–12 months.
- Related Skyvern engineering line: Rustwright (Playwright reimplemented as in-process Rust CDP engine, −70% memory, 2.55× faster) and HTML-instead-of-JSON element representation (−11% tokens, +3.9% success).

## Related

- [[concepts/context-engineering/_index]] — the umbrella discipline; this is the "delete the retriever" branch
- [[concepts/context-engineering/context-compaction]] — opposite strategy: compress context rather than stop pre-loading it
- [[concepts/browser-agent/death-of-browser]]
- [[concepts/agent-sandbox-patterns]] — Browser Use production architecture (screenshot-annotate approach this replaced)
- [[concepts/retrieval-augmented-generation]]
- [[concepts/earendil]] — Pi, the reference minimal harness

## Sources

- [Deleting RAG from our web agent made it 2.3x faster — Suchintan Singh, Skyvern blog (2026-10-01/06)](https://www.skyvern.com/blog/deleting-rag-from-our-web-agent-made-it-2-3x-faster/) — raw: `raw/articles/2026-10-26_skyvern_skyvern-progressive-disclosure.md`
