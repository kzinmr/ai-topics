---
title: "doubleAI"
type: entity
created: 2026-10-24
updated: 2026-10-24
tags:
  - company
  - model
  - formal-verification
  - program-synthesis
  - performance
  - startup
sources:
  - https://heymaxwell.ai/
  - https://doubleai.com
  - raw/articles/2026-10-22_doubleai-maxwell-code-execution-model.md
related_concepts:
  - code-execution-model
---

# doubleAI

doubleAI is a startup that coined the **Code Execution Model (CEM)** category — AI models that sit between code and silicon, rewriting a running program's binary for the exact machine and data it sees, with every rewrite formally proven equivalent to the original. Its first product, **Maxwell** ("Maxwell's Daemon"), opened for early access in October 2026.

**▶ Summary**: Startup behind Maxwell, the self-described first Code Execution Model — formally-proven, in-process binary rewriting with up to 38× pipeline / 4.25× kernel speedups claimed.

## Product: Maxwell

Maxwell watches a program execute, then swaps in formally-proven optimizations tailored to that machine while the program keeps running — on both CPUs and GPUs. Reported results (all self-published): 38× faster data-processing pipelines, 4.25× faster AI inference kernels, 1.87× faster LTX-2.5 4K video generation (134s vs 250s per clip on two B200s), 90% of SOL-ExecBench Blackwell kernels beating NVIDIA's PyTorch baselines after one day of search, and a verified drop-in cuGraph reimplementation 3.6× faster on average. See [[concepts/code-execution-model]] for the category framing, the formal-verification correctness gate, and the credibility caveats.

## Positioning

The company's public materials frame CEMs as a distinct model class from code-writing LLMs: a CEM's output is a binary, not source; its constraint set is "the model must never err," since no human reviews the swaps; and its enabling tool is formal verification — the same technique doubleAI credits with recent AI-driven advances in mathematics.

## Caveats

Coverage of doubleAI consists almost entirely of its own product site (`heymaxwell.ai`, `doubleai.com`). There is no third-party benchmark reproduction, no published paper, and no independent reporting in this wiki's corpus as of 2026-10-24. Treat it as an early-stage, unverified vendor.

## Related

- [[concepts/code-execution-model]] — the category it proposes; full results and analysis
- [[concepts/formal-verification-llm-agents]] — proof-based correctness gating (Anthropic × Theorem, Verus)
- [[concepts/inference]] — the layer Maxwell claims to automate
- [[concepts/ai-supply-chain-security]] — trust surface of a live binary rewriter

## Sources

- [Maxwell — The first Code Execution Model](https://heymaxwell.ai/) (raw: `raw/articles/2026-10-22_doubleai-maxwell-code-execution-model.md`)
