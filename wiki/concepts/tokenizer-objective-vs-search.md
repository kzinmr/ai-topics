---
title: "Tokeniser Objective vs. Search — What Actually Makes a Good Tokenizer"
aliases: ["objective vs search tokenisation", "BPE vs UnigramLM", "what makes a good tokeniser"]
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [tokenization, pretraining, model-training, arxiv, methodology]
sources: [raw/articles/tokenizer-objective-vs-search-2026.md]
confidence: medium
---

# Tokeniser Objective vs. Search

A 2026 ablation study (Yavuz, Meister & Pimentel, arXiv 2609.19145) that cleanly separates two
properties that the two dominant tokenizers conflate, and finds one of them barely matters.

## The confound

Two algorithms dominate modern LMs: **BPE** and **UnigramLM**. Each differs on *two orthogonal axes*:

| Axis | BPE | UnigramLM |
|---|---|---|
| **Objective** | compression | log-likelihood |
| **Search procedure** | bottom-up merging | top-down pruning |

Because BPE and UnigramLM differ on *both* axes at once, prior head-to-head comparisons couldn't
tell whether observed quality differences came from **what is optimised** (the objective) or
**how it is searched** (the procedure).

## The experiment

Disentangle the axes by (a) running each objective *under the other's search procedure*, and
(b) measuring **downstream LM quality**, not just tokenizer-level proxy metrics.

## The finding

- **Search procedure is largely inconsequential** for downstream performance.
- **The objective is the dominant factor** — the **log-likelihood** objective yields consistent
  gains over the compression objective.

This reframes the perennial "BPE vs. SentencePiece/Unigram" debate: the folklore explanation
(merging vs. pruning) is mostly noise; the real lever is *which objective you optimise*. Practically,
it argues for log-likelihood-driven tokenizer training over compression-driven BPE when downstream
quality is the target.

## Why it matters

Tokenizer choice is an early, expensive-to-reverse decision in model pretraining — it fixes
vocabulary, token budgets, and cross-lingual/code behavior. Knowing the objective dominates lets
teams pick and tune tokenizers on the axis that actually moves model quality.

## Open questions

- Does the log-likelihood advantage hold at very large vocabularies / multilingual corpora?
- How does objective choice interact with byte-level vs. text-level tokenization?
- Does the result change for tokenizers used in multimodal or code-specialized models?

## Related
- [[concepts/tokenization]] — general tokenization concepts page
- [[concepts/semantic-ids]] — an alternative discrete-tokenization use case
- [[concepts/scaling-laws]] — tokenizer efficiency interacts with effective-token/compute budgets
