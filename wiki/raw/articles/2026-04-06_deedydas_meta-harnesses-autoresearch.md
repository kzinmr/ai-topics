---
title: "Meta Harnesses — Autoresearch on Steroids"
type: x_article
created: 2026-05-25
source: https://x.com/deedydas/status/2041189706910875869
author: "@deedydas (Deedy Das)"
author_metrics: {followers: 242293, likes: 1277, bookmarks: 1742, retweets: 147, impressions: 133488}
tags: [meta-harness, autoresearch, hill-climbing, agentic-engineering, harness-engineering]
---

# Meta Harnesses — Autoresearch on Steroids

**Author:** Deedy Das (@deedydas) — Partner at Menlo Ventures, former Glean/Google Search
**Date:** 2026-04-06
**Engagement:** 1,277 likes · 1,742 bookmarks · 147 RTs · 133K impressions

## Full Text

> Meta Harnesses is Autoresearch on steroids.
>
> Something I've been exploring recently is to get long running agents to hill climb on a verifiable task to continuously improve without my intervention. Karpathy's Autoresearch did this pretty well on specific tasks, but this weekend I [built/tried something more ambitious]

## Context

This tweet introduces the concept of **Meta Harnesses** as an evolution beyond Andrej Karpathy's Autoresearch pattern. The core idea:

- **Long-running agents** that hill-climb on verifiable tasks
- **No human intervention** — agents continuously self-improve
- **Verifiable task** = objective metric the agent can optimize against
- **Hill climbing** = iterative improvement loop: try → measure → learn → try again

## Key Framing

- Meta Harness > Autoresearch: Autoresearch explores and reports; Meta Harness **optimizes**
- The harness (code around the model) becomes the optimization target, not the model weights
- This shifts the problem from "train a better model" to "build a better operating system for the model"

## Related

- [[concepts/meta-harness]]
- [[concepts/autoresearch]]
- [[entities/deedydas]]
- [[concepts/harness-engineering]]
