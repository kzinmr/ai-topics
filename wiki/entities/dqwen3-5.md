---
title: dQwen3.5
created: 2026-09-20
updated: 2026-09-20
type: entity
tags: [model, diffusion, llm, open-weight, qwen, hybrid-architecture, training]
sources:
  - raw/articles/2026-09-20_arxiv-2609.20751_dqwen3-5-hybrid-attention-diffusion-language-models.md
related: [diffusion-language-models, qwen, ssm-mamba, transformer-architecture]
confidence: high
---

# dQwen3.5

**dQwen3.5** is a family of diffusion language models (DLMs) created by adapting the
autoregressive **Qwen3.5** checkpoints at **0.8B, 2B, 4B, and 9B** parameters. Introduced by
Xue, Rout, Akella, Klivans, Sanghavi & Shakkottai (University of Texas at Austin) in
*"dQwen3.5: Hybrid-Attention Diffusion Language Models"* (arXiv:2609.20751, Sept 2026), and
released openly on HuggingFace (`UT-IFML/dQwen3.5-9B-Base`).

## Why it matters

dQwen3.5 is the first demonstration that a **hybrid attention+RNN** backbone — not just a
full-attention transformer — can be cheaply adapted into a capable [[diffusion-language-models|diffusion
language model]]. Nearly every prior AR→DLM adaptation (e.g. from LLaMA-class models) started from a
full-attention transformer because **masked diffusion needs bidirectional context**, and causal
attention masks are trivially "bidirectionalized." But modern frontier AR models increasingly use
hybrid architectures that interleave attention with recurrent (RNN/linear-attention) layers to cut
inference cost — and RNN layers carry a **structural causal bias** that resists bidirectionalization.

The finding: that mismatch is **overstated**.

## Key results

- **~2× token efficiency**: the hybrid backbone reaches a given training loss in about **half the
  tokens** of a matched full-attention control during diffusion adaptation.
- **Any-order decoding works**: despite the RNN causal bias, dQwen3.5 reproduces full-attention DLM
  any-order generation behavior across all four scales.
- **Strong parallel decoding**: performs well under parallel (multi-token-per-step) generation.
- **Competitive family**: `dQwen3.5` is presented as a competitive model family against comparable
  diffusion and autoregressive baselines.

## Mechanism / intuition

The authors' argument (also supported by prior LM-probing results): the information most useful for
predicting a token is concentrated in the **tokens immediately preceding it**. So even though RNN
layers can only see left-context, the *few* bidirectional attention layers in a hybrid stack supply
enough future context for any-order unmasking — the strong causal bias is mostly harmless for
language.

## Significance for the field

- **Cheap DLMs from cheap AR models.** As production AR models move to hybrid designs for
  inference efficiency, dQwen3.5 shows those same efficient backbones are *good* (in fact more
  token-efficient) starting points for diffusion adaptation — aligning the two efficiency trends.
- **Decouples "diffusion needs full attention" as an assumption**, opening hybrid-attention diffusion
  as a research direction (cf. [[ssm-mamba]], [[transformer-architecture]]).

## Related

- [[diffusion-language-models]] — the paradigm dQwen3.5 belongs to
- [[qwen]] — upstream autoregressive backbone adapted here
- [[ssm-mamba]] — attention+RNN backbones (Qwen3.5, MiniMax) this work leverages
