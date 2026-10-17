---
title: Rain (sunshowers.io)
created: 2026-10-17
updated: 2026-10-17
type: entity
confidence: medium
tags: [person, open-source, agent-infrastructure]
sources:
  - raw/articles/anthropic-scion-mononoke-derived-data-rain-2026-10-14.md
related:
  - scion-anthropic-version-control
  - agent-native-cloud
  - anthropic
aliases:
  - sunshowers
  - John Rain
---

# Rain (sunshowers.io)

**Rain** (blog: sunshowers.io) is a systems engineer and a former Meta engineer who helped design
**Mononoke**, Meta's Rust-based source-control server (designed 2017-18, deliberately open source).
He writes about source control, systems programming, and the intersection of AI and software
engineering.

## Key contribution: the Scion / Mononoke attribution analysis (2026-10)

In October 2026 Rain published a widely-discussed comparison ([HN 425pts](https://news.ycombinator.com/item?id=50094694))
arguing that [Anthropic's Scion](scion-anthropic-version-control.md) — announced as a new agent-first
version control system — closely mirrors Mononoke's "derived data" design, which Rain had described
in his 2022 Oxide candidate materials. Scion credited Meta's Sapling for "hard-won lessons" but never
mentioned Mononoke. Rain called the omission "border[ing] on plagiarism" and observed the write-up
reads as if Claude designed everything.

His follow-up ([HN 253pts](https://news.ycombinator.com/item?id=50106738)) framed the deeper point:
LLMs **index heavily on designs in their training set**, and because Mononoke is open source it sits
in every major model's training data. His thesis — *"Giving credit to those that came before us is
now easier — and more important — than ever. There is no longer an excuse."* — is a touchstone for
the LLM-era attribution / training-set lineage debate.

Notably Rain holds **no grudge about the copying itself**: Mononoke is open source "to benefit
humanity through the spread of good ideas." His complaint is about *credit*, not licensing.

## Sources

- [Anthropic's Scion is heavily inspired by Mononoke](https://sunshowers.io/posts/anthropic-mononoke/)
- [More on Anthropic's Scion ripping off Mononoke](https://sunshowers.io/posts/anthropic-mononoke-2/)
- Raw: `raw/articles/anthropic-scion-mononoke-derived-data-rain-2026-10-14.md`
