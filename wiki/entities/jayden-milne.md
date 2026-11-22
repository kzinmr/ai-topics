---
title: "Jayden Milne"
tags: [person]
sources:
  - raw/articles/jayd.ml--2026-11-01-llms-are-going-to-crush-every-bug-html--b5609894.md
  - raw/articles/jayd.ml--2026-11-14-rockbox-on-yp3-html--410a7866.md
created: 2026-04-24
updated: 2026-11-22
type: entity
---


# Jayden Milne

**Blog:** [thejaymo.net](https://thejaymo.net)  
**Podcast:** Permanently Moved (300+ episodes), Experience.Computer  
**Projects:** Off Grid: Red Team (cybersecurity game at Semaeopus), BYENNE (100 Notes on Storydwelling), Start Select Reset zine  
**Other:** Photo 365 project, Forest Bed (band)

## Overview

Jayden Milne is a writer, game designer, podcaster, and researcher whose work spans AI culture criticism, cybersecurity education, interactive fiction, and digital sovereignty. He is a prolific blogger and podcaster whose long-form content serves as a deliberate archive against the ephemerality of social media. His writing examines the cultural and philosophical implications of AI — particularly around companionship, agency, and the future of human-computer interaction.

## Core Ideas

### The AI "Butlerian Jihad" and Cultural Fracture

Milne characterizes the current AI debate as a cultural war fracturing into quasi-religious camps — from neo-Luddites and moral panic advocates to accelerationists, builders, and safety proponents. He identifies with the "aliens are here" position: viewing AI as a mathematical/cultural substrate creating a novel, non-human intelligence.

> "The debate has shifted from economic concerns to moral/aesthetic panic, losing political utility."

He notes the irrationality of opposing transformer-based AI even in applications like early cancer detection, arguing that the culture war has become counterproductive.

### Attention Economy and the "Great Retreat"

Milne's thesis: *"The attention economy was caused by attention being scarce. When we can turn electricity into attention, the bottleneck moves as well."* He sees the Information Age — ignited by the 1947 silicon transistor — reaching a natural inflection with AI. The challenge is no longer *whether* to use AI, but *"what kind of humans we intend to be while standing alongside them."*

He advocates for a "Great Retreat" from algorithmic feeds toward addressable, long-form content — blogs, forums, newsletters. Running a personal site is, for him, "a deliberate, funded act of digital sovereignty."

### AI Companions: "Little Guys" and Coexistence

Milne has been tracking AI companions since 2024, writing about Character.AI, Replika, and the emerging phenomenon of AI agents inhabiting social spaces. His position:

> "The idea that we can avoid a future where social networks are populated by AI-generated profiles? That ship has sailed."

He argues the real question isn't whether to resist AI agents online, but how to coexist with them in ways that reflect human values and aspirations. He follows developments in virtual environments, agentic LLMs in robotics labs, and the blurring boundary between AI characters and their supporting infrastructure.

### World Running

Milne coined "world running" to describe how automation has always shaped the internet. On Wikipedia, most edits are by bots; on social media, AI agents are increasingly indistinguishable from humans. The challenge isn't preventing AI agents from existing but determining how to coexist with them meaningfully.

### Cybersecurity as Game-Based Learning

His *Off Grid: Red Team* project (at Semaeopus) teaches players to "think like an attacker" using real CVEs and MITRE ATT&CK frameworks. The vertical slice was nominated for Serious Games Awards (Utrecht). Milne believes in game-first experiences that maintain educational rigor — the opposite of gamified training that sacrifices substance for engagement.

### Blogging as Digital Sovereignty

In 2025 alone, Milne published 123,382 words across 104 posts. He values blogs as addressable archives that compound over time, enabling context-rich first contact. This stands in sharp contrast to the "nuclear winter" of short-form social platforms collapsing under algorithmic incentives.

## LLM-Assisted Embedded Reverse Engineering (November 2026)

Two November 2026 posts on jayd.ml (a second blog distinct from thejaymo.net) document aggressive LLM-assisted embedded-systems work, in the lineage of his Arch-Linux-on-Surface experiments:

- **"LLMs are going to crush every open source bug" (Nov 1)** — Claude brought modern Linux up on a 9-year-old Galaxy Tab S3 and, in one hour, "backport[ed] a WIP GPU patch from LKML that hasn't even been merged," fixed a freedreno GPU driver bug existing since 2018, found two separate Kwin bugs and an Alpine packaging bug (file capabilities not applied for a month), and prepared fork + MR descriptions for each. His thesis: even accepting the "stochastic averages" framing, most code mostly works, so average-quality code generation compounds against a massive backlog of neglected open-source bugs. ^[raw/articles/jayd.ml--2026-11-01-llms-are-going-to-crush-every-bug-html--b5609894.md]
- **"Porting Rockbox to an undocumented $9 Aliexpress 'YP3' MP3 Player with LLMs" (Nov 14)** — ported Rockbox to a 512 KiB-RAM undocumented player ("I was barely involved"), then had Claude distill the approach into a reusable **auto-rockbox** porting toolkit/skills with which it ran Rockbox on a second player (TS47) **in 4 hours**. Project site: rockslop.jayd.ml. Credit given to ilyakurdyukov for the original ROM-download-mode/flash-dump tooling. Detailed constraint accounting (shared 128 KiB codec/plugin arena, feature cuts: no voice/DSP/cuesheets/album art). ^[raw/articles/jayd.ml--2026-11-14-rockbox-on-yp3-html--410a7866.md]

> Agent-era significance: the second port in 4 hours via a self-generated porting toolkit is a clean demonstration of **skill/toolkit distillation as an agent capability multiplier** — the agent authored the reusable procedure from its own first run. Pairs with his earlier hardware-porting posts and with [[concepts/agent-generated-software]].

## Key Quotes

> "The attention economy was caused by attention being scarce. When we can turn electricity into attention, the bottleneck moves as well."

> "The debate has shifted from economic concerns to moral/aesthetic panic, losing political utility."

> "The idea that we can avoid a future where social networks are populated by AI-generated profiles? That ship has sailed."

> "Running a personal site is a deliberate, funded act of digital sovereignty."

> "What kind of humans we intend to be while standing alongside them."

## Recent Themes (2024–2026)

- **AI companions research** — Secured contracts after 2024 blog posts surfaced via ChatGPT deep research; visited robotics labs observing soft robotics + agentic LLMs
- **AI Butlerian Jihad** — Mapping the cultural fracture around AI into quasi-religious camps; arguing for rational engagement over panic
- **World Two** — Tracking the subculture of people giving AI agents full computer access; the next interface paradigm for agentic AI
- **Cybersecurity gaming** — *Off Grid: Red Team* vertical slice complete, Serious Games Award nomination
- **On-chain interactive fiction** — *The O'Ruggin Trail* with NFT-based game state transfer
- **Permanently Moved podcast** — 301 episodes completed; shifting to quarterly long-form releases to escape the algorithmic grind
- **Photo 365** — Year 5 of daily photography, marking ~1/8th of his life

## Related

- [[entities/george-hotz]] — AI infrastructure, open-source ethos, anti-monopoly views
- [[entities/grant-slatton]] — Technocapital thesis, capital ownership in AI era
- [[entities/stefano-marinelli]] — Critical AI infrastructure perspectives, "EnshittifAIcation"
- [[entities/john-carmack]] — Pragmatic AI tool use, optimization focus

## Sources

- [thejaymo.net](https://thejaymo.net) — Blog (100+ posts/year)
- "2025 Year in Review: Macro-to-Micro Retrospective" (January 2026)
- "Living Alongside Computer People" (January 2025)
- "Virtual Friends, Real Feelings" (September 2024)
- Permanently Moved podcast (301 episodes)
- Experience.Computer podcast
- Off Grid: Red Team — Semaeopus cybersecurity game

## References

- jayd.ml--2025-04-15-arch-linux-on-surface-html--97105161
- jayd.ml--2025-04-30-someone-at-youtube-needs-glasses-html--9965a209
- jayd.ml--2025-05-31-adventures-in-podcasting-html--62747723
- jayd.ml--2025-06-15-encoding-xml-is-broken-and-no-one-cares-html--3522c300
- jayd.ml--2025-10-29-finally-figured-out-locales-html--ca47d81c
- jayd.ml--2025-11-10-someone-at-youtube-needs-glasses-prophecy-fulfill--1a20d5d7
- jayd.ml--2026-01-05-the-hypnoverse-html--5fa03501
- jayd.ml--2026-02-14-godot-minesweeper-html--9f958842
- jayd.ml--2026-02-14-letterboxd2jellyfin-html--7d65fe92
- jayd.ml--2026-02-14-microsoft-game-pass-fraud-html--d58463f3
- jayd.ml--2026-11-01-llms-are-going-to-crush-every-bug-html--b5609894
- jayd.ml--2026-11-14-rockbox-on-yp3-html--410a7866
