---
title: "Qwen3.8-Flash-Next"
url: "https://simonwillison.net/2026/Aug/26/qwen38-flash-next/"
fetched_at: 2026-08-27T10:01:12.121775+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Qwen3.8-Flash-Next

Source: https://simonwillison.net/2026/Aug/26/qwen38-flash-next/

26th August 2026 - Link Blog
Qwen3.8-Flash-Next
(
via
) Another open weights model from Qwen. This one is "a multimodal MoE model that also serves as an early preview of the architecture used in Qwen4".
It's pretty big: 125B tokens, but only 6B active which means it gets a significant performance boost.
I've been trying it out on a DGX Spark using
these Unsloth quantized models
. I'm still exploring the model - so far I've tried the 72.5GB UD-IQ1_S one (producing
these pelicans
) and the 78.9GB UD-Q2_K_XL (producing
these
).
My favorite so far was this xhigh reasoning effort one from UD-Q2_K_XL:
