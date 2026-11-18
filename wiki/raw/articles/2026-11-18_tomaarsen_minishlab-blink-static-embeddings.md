---
title: "MinishLab blink — small CPU-runnable static embedding models (X thread by Tom Aarsen)"
url: "https://x.com/tomaarsen/status/2123061190209491152"
fetched_at: 2026-11-18T22:45:00+00:00
source: "x.com/tomaarsen (5-tweet thread, 2026-11-18 14:30 UTC)"
tags: [blog, raw]
scrape_status: "tweet-text capture — HF collection/GitHub pages not scraped (linked only)"
---

# MinishLab blink — small CPU-runnable static embedding models

Source thread: https://x.com/tomaarsen/status/2123061190209491152 (reply thread by @tomaarsen praising @tulkenss and @thomas_v_dongen of the @minishlab team)

## Tweets (verbatim, newest-first in thread order as posted)

1. "Very nice work by @tulkenss and @thomas_v_dongen from the @minishlab team! 👏 Small, accessible embedding models that you can run on CPU are always welcome. Both models and their evaluation details: https://huggingface.co/collections/minishlab/blink"
2. "Both models look up token vectors, average them, and normalize the result, so you can run them on CPU without a transformer forward pass. About 31MB / 256MB of float32 weights, both MIT licensed: https://huggingface.co/collections/minishlab/blink"
3. "For English, Minish reports 55.35 on MTEB(eng, v2) and 46.70 nDCG@10 on decontaminated BEIR. blink-8M leads the seven static models in this comparison, all evaluated at 256d: https://huggingface.co/minishlab/blink-8M"
4. "The 64M model lets you search across 100+ languages with the same API. Here an English query matches Dutch and Spanish password-reset instructions above an unrelated English sentence: https://huggingface.co/minishlab/blink-multilingual-64M"
5. "For lightweight deployments, model2vec runs the same models with NumPy, without PyTorch. Here's the first example again. Since Blink normalizes its embeddings, a dot product gives you cosine similarity: https://github.com/MinishLab/model2vec"

## Linked resources

- HF collection: https://huggingface.co/collections/minishlab/blink — "Our best-in-class blink models. Load and use them with model2vec, model2vec-rs, or sentence-transformers."
- https://huggingface.co/minishlab/blink-8M — Feature Extraction model, 7.68M parameters
- https://huggingface.co/minishlab/blink-multilingual-64M — Feature Extraction model, 64M parameters
- https://github.com/MinishLab/model2vec — "Fast State-of-the-Art Static Embeddings" (NumPy-only inference, no PyTorch)

## Key facts

- Architecture: static (lexical) embeddings — token vector lookup + mean pooling + normalization; no transformer forward pass at inference → CPU-only, PyTorch-free deployment possible via model2vec.
- Sizes: ~31MB (blink-8M) / ~256MB (blink-multilingual-64M) float32 weights; both MIT licensed; 256-dim in the cited comparison.
- Reported English quality: **55.35 MTEB(eng, v2)**, **46.70 nDCG@10 on decontaminated BEIR**; blink-8M leads a seven-static-model comparison at 256d.
- Multilingual: blink-multilingual-64M searches 100+ languages with the same API (cross-lingual retrieval demo: English query → Dutch/SSpanish docs).
- Dot product == cosine similarity because embeddings are normalized.
- Team: Tom Lulens(? @tulkenss) and Thomas van Dongen (@thomas_v_dongen) at MinishLab (Minish = the company; MinishLab is known for docling / marker-style PDF extraction and model2vec).
