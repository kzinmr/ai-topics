---
title: "AlphaEvolve on Google Cloud: AI for agentic discovery and optimization"
source: Google Cloud Blog
date: 2025-12-10
url: https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-on-google-cloud
scraped: 2026-05-09
---

# AlphaEvolve on Google Cloud: AI for agentic discovery and optimization

AlphaEvolve is a Gemini-powered coding agent for designing advanced algorithms, released to Google Cloud in private preview.

## How it works

- Input: Problem specification, evaluation logic, seed initialization program
- Mutation: Gemini models (Flash for speed, Pro for depth) generate mutated, optimized code versions
- Evolution: Evolution algorithms select which code mutations to combine and further mutate
- Loop: Evaluation scores used by LLM ensemble to generate next set of improved solutions

## Proven Impact at Google

- Data center efficiency: Recovering on average 0.7% of global compute resources
- Gemini training: Sped up a vital kernel by 23%, reducing Gemini's training time by 1%
- Hardware design: Accelerated next-generation TPU design by discovering more efficient arithmetic circuits
- FlashAttention: Up to 32.5% speedup for FlashAttention kernel in Transformer models
- Matrix multiplication: First improvement in 56 years over Strassen's algorithm for 4×4 complex-valued matrices

## Paper

arXiv: 2506.13131 — "AlphaEvolve: A coding agent for scientific and algorithmic discovery"
