---
title: "GLM-5.1-HighSpeed Launch Announcement"
url: https://x.com/zrdianjiao/status/2057662110516322360
author: zR (@zRdianjiao)
date: 2026-05-21
type: x-post
tags: [tilert, glm, inference, speed, zhipu]
---

# GLM-5.1-HighSpeed Launch Announcement

**Source:** https://x.com/zrdianjiao/status/2057662110516322360
**Author:** zR (@zRdianjiao) — Algorithm Engineer @Zai_org (Zhipu AI)
**Date:** 2026-05-21

## Post Content

> 🚀 GLM-5.1-HighSpeed is live: 400 tokens/s — a new speed ceiling for flagship-tier LLM APIs.
>
> Not a smaller model traded for speed. A flagship from @Zai_org that's also the fastest.
>
> 📖 Full technical deep-dive 👇
> https://www.tilert.ai/blog/speed-as-the-next-scaling-law.html

## Context
- zR is an Algorithm Engineer at Zai_org (Zhipu AI) working on GLM model research & OSS adaptation
- GLM-5.1-HighSpeed achieves 400 tokens/s on a flagship-tier model
- The backend is powered by TileRT inference engine
- Follow-up tweet (id: 2057662553703272778) explains TileRT's technical architecture:
  - Persistent Kernel — full graph compiled AOT into one GPU-resident Engine Kernel, launched once
  - Tile Pipeline — compute, async IO, comms as tile-level tasks; intermediates flow through registers & shared memory
- TileRT GitHub: https://github.com/tile-ai/TileRT
