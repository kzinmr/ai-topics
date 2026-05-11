---
title: "HTML as Default Agent Output & The Vision Progression"
source: "@karpathy / Andrej Karpathy (Note Tweet)"
date: 2026-05-11
scraped: 2026-05-11
type: x_note_tweet
url: https://x.com/karpathy/status/2053872850101285137
quoted_tweet: https://x.com/trq212/status/2052809885763747935
author: Andrej Karpathy
tags:
  - html
  - agent-output
  - ai-ux
  - vision
  - human-ai-interaction
  - markdown
  - audio
  - diffusion
  - neural-video
  - brain-computer-interface
metrics:
  likes: 3350
  bookmarks: 3339
  retweets: 317
  replies: 273
  quotes: 80
  impressions: 252234
---

# HTML as Default Agent Output & The Vision Progression

**Author**: Andrej Karpathy (@karpathy)
**Date**: 2026-05-11
**Metrics**: 3,350 likes · 3,339 bookmarks · 252K impressions
**In reply to**: [Thariq Shihipar's "The Unreasonable Effectiveness of HTML"](https://x.com/trq212/status/2052809885763747935)

## Full Note Tweet Content

This works really well btw, at the end of your query ask your LLM to "structure your response as HTML", then view the generated file in your browser. I've also had some success asking the LLM to present its output as slideshows, etc.

More generally, imo audio is the human-preferred input to AIs but vision (images/animations/video) is the preferred output from them. Around a ~third of our brains are a massively parallel processor dedicated to vision, it is the 10-lane superhighway of information into brain. As AI improves, I think we'll see a progression that takes advantage:

1. raw text (hard/effortful to read)
2. markdown (bold, italic, headings, tables, a bit easier on the eyes) ← current default
3. HTML (still procedural with underlying code, but a lot more flexibility on the graphics, layout, even interactivity) ← early but forming new good default
...4,5,6,...
n. interactive neural videos/simulations

Imo the extrapolation (though the technology doesn't exist just yet) ends in some kind of interactive videos generated directly by a diffusion neural net. Many open questions as to how exact/procedural "Software 1.0" artifacts (e.g. interactive simulations) may be woven together with neural artifacts (diffusion grids), but generally something in the direction of the recently viral https://x.com/zan2434/status/2046982383430496444

There are also improvements necessary and pending at the input. Audio nor text nor video alone are not enough, e.g. I feel a need to point/gesture to things on the screen, similar to all the things you would do with a person physically next to you and your computer screen.

TLDR The input/output mind meld between humans and AIs is ongoing and there is a lot of work to do and significant progress to be made, way before jumping all the way into neuralink-esque BCIs and all that. For what's worth exploring at the current stage, hot tip try ask for HTML.

## Key Insights

### 1. HTML is the Practical Next Step

Karpathy endorses Shihipar's approach: simply add "structure your response as HTML" to prompts. He's also had success asking LLMs to produce slideshows.

### 2. Audio In → Vision Out

A key framing: **audio is the preferred human input to AIs** (speaking is faster than typing), but **vision is the preferred output** (~1/3 of the brain is dedicated to visual processing — the "10-lane superhighway" for information).

### 3. The Output Progression

Karpathy outlines a ladder of AI output modalities:

| Stage | Format | Characteristics |
|-------|--------|----------------|
| 1 | Raw text | Hard/effortful to read |
| 2 | Markdown | Bold, italic, headings, tables — **current default** |
| 3 | HTML | Procedural code, but rich graphics, layout, interactivity — **emerging new default** |
| ... | — | Intermediate stages |
| n | Interactive neural videos/simulations | Generated directly by diffusion neural nets — **extrapolated endpoint** |

### 4. "Software 1.0" + Neural Artifacts

The endpoint involves blending procedural "Software 1.0" artifacts (interactive simulations) with neural artifacts (diffusion grids). References [@zan2434's viral post](https://x.com/zan2434/status/2046982383430496444) as an early directional signal.

### 5. Input Gaps Remain

Current input modalities (audio, text, video) aren't sufficient — Karpathy wants to **point/gesture at things on screen**, mimicking the in-person collaboration experience. This gap needs to be addressed before reaching the full input/output "mind meld."

### 6. No Need for BCIs Yet

Significant progress in human-AI I/O is achievable **well before** neuralink-style brain-computer interfaces. The current focus should be on practical improvements like HTML output and richer interaction modalities.

## Related

- Shihipar's original article: [[raw/articles/2026-05-08_trq212_unreasonable-effectiveness-html]]
- Simon Willison's take: [[raw/articles/2026-05-08_simonwillison_unreasonable-effectiveness-html]]
- zan2434's viral neural video post referenced as directional signal
- [[entities/andrej-karpathy]] — Entity page
- [[entities/thariq-shihipar]] — Entity page
