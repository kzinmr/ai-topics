---
title: "SGNT — You Could Have Built Jev"
type: entity
created: 2026-09-19
updated: 2026-10-28
tags: [ai-company, small-models, sgnl, jev, sgnt, llm-internals, first-principles, model-optimization, inference-speed, tokenization]
sources:
  - https://sgnt.ai/p/jev/
  - https://x.com/dbreunig/status/2101154389574791210
---

# SGNT — You Could Have Built Jev

**SGNT** (sgnt.ai) is a small AI lab / publication that publishes short, illustrated, first-principles explainers of its own model optimizations, under the framing "you could have built [it]" — each article walks through a technique so thoroughly from first principles that the reader understands it as obvious. The inaugural piece, **"You could have built Jev"** (sgnt.ai/p/jev), explains **sgnl**'s Jev model and its predecessor sgnt-ai.

## How Jev was built

Jev is a **100M-parameter model initialized from the GPT2-small checkpoint** — not trained from scratch, but evolved from a 2019 model. The stated thesis: "the most popular model architecture of all time can be made 100x better and 100x faster with the right tweaks." The article enumerates the accumulated modifications:

- **Smaller tokenizer**: 50K tokens (vs GPT2's 50K+ over a larger vocab design), fewer embedding parameters
- **GQA + MLA + DeepSeek-style MoE**: attention and parameter-efficiency techniques borrowed from [[entities/deepseek|DeepSeek]]-lineage research, layered onto GPT2's skeleton
- **Sub-1-bit weights**: quantization below one bit per weight
- **1.6-bit Triton attention kernel**: custom kernel for fast low-precision attention
- **CUDA fused ops** and a **custom C inference backend** for latency
- **Domain-specific pretraining corpus**: ~22B tokens heavily weighted toward code, math, and reasoning tasks (10.9B The Stack v2 code, 4B StackEdu v2, 1.7B OpenWebMath, 2B NuminaMATH, 1B OpenThought3, etc.)

## Why it matters

Jev demonstrates that **architecture-level accumulated optimizations on tiny models** can punch far above their parameter count for narrow domains (code/math), and that the GPT2 skeleton remains a viable substrate a decade later. The sgnt.ai article doubles as both a technical explainer and a manifesto for "small, fast, transparent models you can reason about."

The article was personally endorsed by **Drew Breunig** (["No, but this is good"](https://x.com/dbreunig/status/2101154389574791210) — recommending it in reply to a question about Jev coverage, Sep 19, 2026). Related coverage: Samuel Colvin benchmarked Jev vs Claude Sonnet via [[concepts/pydantic-ai|Pydantic AI]].

## Related
- [[concepts/system-one-models|System One Models]] — the model class Jev belongs to (this article is its first-principles reproduction)
- [[entities/typesafe-ai|TypeSafe AI]] — the lab that originally launched Jev as a System One model
- [[entities/anthropic|Anthropic]] / [[entities/deepseek|DeepSeek]] — source of many borrowed techniques
- [[concepts/harness-engineering/agent-harness|Agent Harnesses]] — the deployment context where cheap fast models matter

## Competing approaches (2026-10-27)

**Voyage AI** published *"How to create your own JEV using Voyage models"* (blog.voyageai.com, Oct 27,
2026), an embedding-based challenger to Jev's direct-labeling approach on **personalized prediction over
MongoDB collections** (imputation / classification / regression on a partially-populated field, e.g.
predicting a movie's IMDb rating or a ticket's priority).

- **Method**: serialize each document to JSON (minus the target field) → embed the whole document with a
  Voyage model → fit a standard estimator (XGBoost / ridge regression) on documents where the field is
  set → predict the missing values. Free text, lists, and nested sub-docs are all used, unlike tabular
  flattening. Because Jev labels documents **directly** (a System-One style model), it doesn't learn from
  the already-labeled documents in the collection; the Voyage recipe explicitly fits on those.
- **Headline results vs Jev**: across 50 real-world tasks, adding free/open-source Voyage embeddings cuts
  errors **37%** (voyage-4-nano) to **44%** (voyage-json, an experimental JSON-post-trained model). On the
  29 classification tasks, **voyage-json makes 48% fewer errors than TypeSafe AI's Jev** (88.3 vs 77.6
  AUROC). voyage-4-nano runs locally (GPU optional) via sentence-transformers; the larger models are API.
- **Caveat**: this is Voyage's own benchmark (their models, their framing) — treat the margin as
  vendor-reported, not independent. It nonetheless signals an interesting axis: for structured-collection
  prediction, *embedding + a classical head* is competitive with a purpose-built small System-One model.

Source: raw/articles/2026-10-27_voyage-jev.md

- [[entities/voyage-ai|Voyage AI]] — embedding provider behind the challenger recipe
