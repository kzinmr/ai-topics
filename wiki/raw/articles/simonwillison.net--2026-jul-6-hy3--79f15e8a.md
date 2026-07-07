---
title: "tencent/Hy3"
url: "https://simonwillison.net/2026/Jul/6/hy3/#atom-everything"
fetched_at: 2026-07-07T07:01:41.294122+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# tencent/Hy3

Source: https://simonwillison.net/2026/Jul/6/hy3/#atom-everything

6th July 2026 - Link Blog
tencent/Hy3
. New Apache 2.0 licensed model from Tencent in China:
Hy3 is a 295B-parameter Mixture-of-Experts (MoE) model with 21B active parameters and 3.8B MTP layer parameters, developed by the Tencent Hy Team. Following the Hy3 Preview launch in late April, we gathered feedback from 50+ products and scaled up post-training with higher quality data. Today, we introduce Hy3, which outperforms similar-size models and rivals flagship open-source models with 2-5x parameters. It also shows significant gains in utility across various products and productivity tasks.
The full-sized model is 598GB on Hugging Face, and the FP8 quantized one
is 300GB
. The context length is 256K.
It's available for free
on OpenRouter until July 21st
. I had it "Generate an SVG of a pelican riding a bicycle" there and got this:
