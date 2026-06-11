---
source_url: "https://simonwillison.net/2026/Jun/10/diffusiongemma/"
title: "DiffusionGemma"
author: "Simon Willison"
blog: "simonwillison.net"
date: "2026-06-10"
fetched_at: "2026-06-11T07:00:00Z"
type: raw_article
---

# DiffusionGemma

**[DiffusionGemma](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)** ([via](https://news.ycombinator.com/item?id=48478471)) Last May Google briefly released an experimental Gemini Diffusion model. I [tried the preview at the time](https://simonwillison.net/2025/May/21/gemini-diffusion/) and recorded it running at 857 tokens/second. It was an exciting model, but Google made no further announcements about it.

That research has returned in the best possible way: as a new open weight (Apache 2 licensed) Gemma model, [google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it).

NVIDIA are currently [hosting the model for free](https://build.nvidia.com/google/diffusiongemma-26b-a4b-it) on their NIM cloud API. I used that API to [generate this pelican](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fe5e234a6dc6eef61e209ce1629620042), which took 4.4s (according to `time uv run generate.py`) to return 2,409 tokens - so at least 500 tokens/second.

![Flat minimalist illustration of a white pelican with a large orange beak riding a red bicycle with black wheels, against a pale blue background with a green line representing the ground](https://static.simonwillison.net/static/2026/diffusiongemma-pelican.png)

---

Posted 10th June 2026 at 8 pm

Tags: google, ai, generative-ai, llms, nvidia, pelican-riding-a-bicycle, gemma, llm-release, llm-performance
