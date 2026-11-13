---
title: "GAIA Benchmark (redirect)"
type: concept
created: 2026-04-25
updated: 2026-11-13
tags:
  - redirect
  - benchmark
  - evaluation
  - ai-agents
sources:
  - https://arxiv.org/abs/2311.12983
aliases:
  - gaia
  - GAIA
---

# GAIA (General AI Assistants benchmark)

> **Canonical page**: [[concepts/ai-benchmarks/gaia-benchmark]]. This page exists because the top-level `gaia` slug was created in the 2026-04-25 bulk import; benchmark pages belong under `concepts/ai-benchmarks/`.

**GAIA** — "A Benchmark for General AI Assistants" (Mialon, Fourrier, Craig, Bosschat, LeCun, Artzi; Meta AI + Hugging Face + AutoGPT; arXiv:2311.12983, ICLR 2024) — is a benchmark of **466 real-world assistant questions** that are conceptually simple for humans (~92% accuracy) but extremely hard for frontier AI (GPT-4 with plugins scored ~15% at publication). Questions require multi-step reasoning, tool use, web browsing, and multimodal handling, and are designed to be *unambiguous* with a single verifiable answer so they resist "answer-anyway" behavior.

Key design properties:

- **Three difficulty levels** (Level 1: no tools / few steps; Level 2: several tool calls; Level 3: long multi-tool chains) — Level 1 can be attempted without any tools, isolating reasoning from tool-use.
- **Humans vs. AI gap** as the headline metric — the benchmark deliberately targets the human-machine competence gap rather than expert trivia.
- Co-created by [[entities/clefourrier|Céline Fourrier]]'s Hugging Face evaluation team with Meta; the motivation behind GAIA is documented in her entity page.

## Successors

- [[concepts/ai-benchmarks/gaia2-are]] — Gaia2 (250+ procedural, agentic tasks with execution-based scoring) and ARE (Agent Runtime Environment), arXiv:2509.17158.

## Related

- [[concepts/ai-benchmarks/gaia-benchmark]] — canonical benchmark page
- [[concepts/ai-benchmarks/gaia2-are]] — successor benchmark + runtime
- [[concepts/evaluation/ai-benchmarks-and-evals]] — evaluation landscape overview
- [[entities/clefourrier]] — GAIA co-creator
- [[concepts/agent-harnesses]] — tool-use scaffolding GAIA implicitly measures
