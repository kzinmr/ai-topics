---
title: "Granite 4.1 3B SVG Pelican Gallery"
url: "https://simonwillison.net/2026/May/4/granite-41-3b-svg-pelican-gallery/#atom-everything"
fetched_at: 2026-05-05T07:00:55.844442+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Granite 4.1 3B SVG Pelican Gallery

Source: https://simonwillison.net/2026/May/4/granite-41-3b-svg-pelican-gallery/#atom-everything

4th May 2026 - Link Blog
Granite 4.1 3B SVG Pelican Gallery
. IBM released their
Granite 4.1 family
of LLMs a few days ago. They're Apache 2.0 licensed and come in 3B, 8B and 30B sizes.
Granite 4.1 LLMs: How They’re Built
by Granite team member Yousaf Shah describes the training process in detail.
Unsloth released the
unsloth/granite-4.1-3b-GGUF
collection of GGUF encoded quantized variants of the 3B model - 21 different model files ranging in size from 1.2GB to 6.34GB.
All 21 of those Unsloth files add up to 51.3GB, which inspired me to finally try an experiment I've been wanting to run for ages: prompting "Generate an SVG of a pelican riding a bicycle" against different sized quantized variants of the same model to see what the results would look like.
Honestly,
the results
are less interesting than I expected. There's no distinguishable pattern relating quality to size - they're all pretty terrible!
I'll likely try this again in the future with a model that's better at drawing pelicans.
