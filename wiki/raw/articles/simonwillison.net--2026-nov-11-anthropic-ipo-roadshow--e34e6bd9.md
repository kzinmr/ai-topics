---
title: "Anthropic's IPO roadshow video"
url: "https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/"
fetched_at: 2026-11-12T10:01:09.680595+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Anthropic's IPO roadshow video

Source: https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/

11th November 2026 - Link Blog
Anthropic's IPO roadshow video
. Anthropic kicked off their IPO roadshow yesterday, and their roadshow video has some previously unreleased information about how their business works.
The section on "Approach to compute" with co-founder Tom Brown is particularly interesting, describing how Anthropic train and serve Claude across AWS Trainium, Google TPUs, NVIDIA GPUs, and AMD GPUs.
I'm not sure why there's no official video transcript, but here's
one that I extracted
using MacWhisper. Highlights below:
We train and serve Claude now across all four major chip families. That's only possible because early on we made an unconventional bet on a multi-chip strategy. At the time, many people thought that running AI models on different chips wasn't worth the effort. Each chip needs its own tailored software stack and inference stack, which is expensive and difficult to build. We've now been doing it for years, and we've gotten incredibly good at it. [...]
As an example, this year, we started working with AMD GPUs for the first time. In the past, bringing on a new chip platform took dozens of engineers months of work
This time, we had Mythos try it out. It got Claude running on AMD in just three days, with basically no human intervention
. Claude ported or wrote almost 100% of the kernels. [...]
The second driver of our compute advantage is our rate of discovery of compute multipliers. We focus on total effective compute, which is the multiplicative product of physical capacity times the compute multipliers that we discover. Each one we discover makes our pool of total effective compute bigger. For example, say you need 100 units of compute to train a model of a certain intelligence. A 4x compute multiplier means you can use 25 units of compute to train the exact same model. Or you can use those hundred physical units to train an even more intelligent model that would have previously required 400 units.
Compute multipliers create a competitive advantage for us that's hard to replicate. They build on each other. Each new multiplier we discover has a positive effect on the multipliers before it. They stack.
We believe that this can accelerate even further as we approach recursive self-improvement. Claude will be able to discover compute multipliers entirely by itself
, allowing the number of compute multipliers to grow faster and faster.
We got a hint at Anthropic's multi-chip strategy last September in their
postmortem of three recent issues
, where they described bugs that affected just their TPU deployments.
