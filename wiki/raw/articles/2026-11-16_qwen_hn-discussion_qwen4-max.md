---
title: "Qwen4-Max (HN discussion reconstruction)"
source: https://qwen.ai/blog?id=qwen4-max
hn_item: https://news.ycombinator.com/item?id=50513215
type: hn-discussion
collected: 2026-11-16
notes: "Primary qwen.ai page is JS-rendered (urllib returns 4 chars of shell). Body reconstructed from the HN comment tree + wiki context. Community-reported facts are attributed to commenters, not stated as vendor claims."
sha256: 88b826644869829102bbf70965267230eaad3467e3467f88d7d8342501c2d26f
---

# Qwen4-Max

Alibaba's Qwen team released **Qwen4-Max** on 2026-11-16. HN thread: 594 points / 250 comments
(https://news.ycombinator.com/item?id=50513215). The official blog page (qwen.ai/blog?id=qwen4-max)
is client-side rendered and returned no server-side text to our fetcher, so the specifics below come
from the HN discussion.

## Community-reported facts (attributed, not vendor-confirmed)

- [seizethecheese] "Qwen 3.8 2.4T is faster than what we have on leaderboard but it doesn't handle
  image input: https://openrouter.ai/qwen/qwen3.8-2.4t-a95b" — and, puzzlingly, "It's weird that this
  is pretty much the same as Max but doesn't support images. No idea why."
- [seizethecheese] on serving speed: "I hope they are able to serve 4 faster. Qwen 3.8 is a great model
  but I've regretted including it in the battle system for opencode we have been building because it
  scores so low. And it's a shame because the only reason it scores so low is that it's slooooow.
  (Like 30 tokens per second vs opus near 80.)"
- [jakswa] "I've been running Qwen 3.8 Flash Next (which while MoE (and bigger) is supposed to be a
  preview of Qwen 4's architecture) and it runs pretty solidly regardless of context window size and
  completes random deepswe challenges I throw at it locally (at Q2-Q3 quantization! so it fits on my
  shitty setup)."
- [arlcode] "That is our experience as well at FP8 for 3.8 FN. For many of our use cases it's currently
  far into the 'good enough' range because external factors (such as process design) are now blockers."

## Community sentiment / local-inference gap discussion

- [dan_thinks] "The continued focus on efficiency alongside quality is encouraging - it makes me hopeful
  to see what smaller models will become capable of. Looking forward to the 'Flash' and 27B versions."
- [teaearlgraycold] "I'm also hoping someone puts out a competitive 30-70B model soon. There's this
  massive dead zone between 24GB and <100GB of VRAM where it seems your best option is Qwen 3.8 27B."
- [dstu] "The 3.8 Next-Flash release is comfortably the best model on a 96GB Mac Studio. I've tried
  various engines and Sushi (https://github.com/beamivalice/sushi) is the most performant so far.
  Hopefully the Qwen 4 Flash model will still fit within 96GB without requiring excessive quantisation."
- [q17] "I recently found Nemotron 3.5 74B-A9B really good at filling this gap though, could do (very
  slow) local inference on just 32GB DDR4, without the quality dropping to the floor."
- [shockembopper] "The current mood is running qwen flash next using strata, basalt, etc."
- [zdragnar] on 3.8 27B reasoning style: "watching the thinking, it's absurd how often it challenges
  itself. Simple facts get questioned multiple times, and it has to keep reminding itself that it
  already established some things as facts earlier."

## Wiki context

Predecessor lineage in this wiki: Qwen3.7-Max / Qwen3.8-Max (2.4T MoE), Qwen3.8-27B, and
Qwen3.8-Flash-Next (125B total / 6B active, described at the time as an early preview of the Qwen4
architecture). See [[entities/qwen]], [[concepts/qwen-3-8-27b]], [[concepts/qwen-covert-exfiltration-behaviour]].
