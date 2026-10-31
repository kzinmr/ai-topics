---
title: "dbreunig/nesformer"
url: "https://simonwillison.net/2026/Oct/30/nesformer/"
fetched_at: 2026-10-31T10:00:57.327004+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# dbreunig/nesformer

Source: https://simonwillison.net/2026/Oct/30/nesformer/

30th October 2026 - Link Blog
dbreunig/nesformer
(
via
) Inspired by
qwenputer
by Divyansh Agrawal, Drew Breunig baked a working emulator for a Nintendo Entertainment System 6502 CPU into the weights of Qwen3.5-4B. You can now play NES ROMs such as Super Mario Bros (very slowly) running inside Qwen!
In
a comment on Hacker News
Drew reveals the Opus 5.5 prompts he used to build this system:
Read this article and any relevant source code: https://divagr.com/blog/qwenputer. Then explore if you could emulate the chip and ram in a Nintendo Entertainment System (as people do today with FPGAs in MISTRs) using this technique. If so, what size model would you have to build and if you could use smaller faster ones, could you get it to be at the standard clockspeed.
Followed by:
I think we should build it! Just for fun. It's okay if it's not fast. We want to be able to have the weights, and a cli to run them that we can point at a ROM.
Apparently Opus found and then used
this collection of conformance tests
for the NES CPU released 15 years ago by Christopher Pow.
