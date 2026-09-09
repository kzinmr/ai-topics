---
title: "Introducing ChatGPT Images 2.5"
url: "https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/"
fetched_at: 2026-09-09T10:00:59.771095+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Introducing ChatGPT Images 2.5

Source: https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/

8th September 2026 - Link Blog
Introducing ChatGPT Images 2.5
. OpenAI's image generation models are apparently used "more than 3 billion images across ChatGPT Images and the GPT‑Image models in the API". This latest release improves their instruction-following ability across multiple turns, responds faster, and "is better at preserving the subjects in your reference photos".
There are two new model IDs in the API:
gpt-image-2.5-sunburst
and
gpt-image-2.5-flare
. Based
on this
I think Sunburst is the stronger option:
Choose Sunburst for workflows where editing precision matters most, and Flare for fast, high-quality everyday image generation.
I
upgraded
my
openai_image.py
CLI tool to support passing in one or more reference images, so now this works:
uv run https://tools.simonwillison.net/python/openai_image.py \
'
add a raccoon scientist studying the chart thoughtfully
'
\
  -i https://static.simonwillison.net/static/2026/openai-agent-usage.webp \
  -m gpt-image-2.5-sunburst
This is the
original image
, and here's what I got back from that prompt to "add a raccoon scientist studying the chart thoughtfully":
