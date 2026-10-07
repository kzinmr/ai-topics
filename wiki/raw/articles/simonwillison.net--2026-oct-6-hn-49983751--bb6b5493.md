---
title: "EmbeddingGemma 2"
url: "https://simonwillison.net/2026/Oct/6/hn-49983751/"
fetched_at: 2026-10-07T10:01:26.851315+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# EmbeddingGemma 2

Source: https://simonwillison.net/2026/Oct/6/hn-49983751/

I really appreciate that
EmbeddingGemma 2
is under the Apache 2.0 license.
For embedding models in particular, I don't think it makes sense to use a closed, proprietary, hosted-only model.
Most applications of embedding models involve calculating thousands or even millions of embedding vectors and storing them for later comparison.
If your model is proprietary, the vendor is likely someday going to decide to stop offering that model. They'll have a better model to replace it, but you still need to pay to re-calculate those millions of stored existing vectors.
(In April 2024 OpenAI offered to "cover the financial cost of users re-embedding content with these new models" -
https://openai.com/index/gpt-4-api-general-availability/
- but I don't think that's something we can rely on from every provider.)
Notably, I
don't want to host the model myself
. I'd much rather pay a provider for a hosted model while knowing that if they ever stop hosting it I can run the open weights version myself - or find another vendor who can do that for me.
