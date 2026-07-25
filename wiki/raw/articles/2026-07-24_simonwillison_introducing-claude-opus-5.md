---
title: Introducing Claude Opus 5
source: Simon Willison's Weblog
source_url: https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/
date: 2026-07-24
author: Simon Willison
type: link_blog
tags: [claude, anthropic, model-release, llm]
---

# Introducing Claude Opus 5

Simon Willison covers Anthropic's release of Claude Opus 5 (July 24, 2026).

Anthropic describes it as a "thoughtful and proactive model that comes close to the frontier intelligence of Claude Fable 5 at half the price."

It's currently leading the Artificial Analysis leaderboard, in front of even Fable 5.

Priced the same as Opus 4.8. Continues to offer a "fast mode" at twice the cost of the base model.

## Key Highlights

**Relentlessly proactive**: On a Frontier-Bench task, Opus 5 was given a drawing of a machine part and asked to write code to rebuild it as a 3D FreeCAD model. The model was intentionally given no way to directly view the drawing. Opus 5 responded by writing its own computer vision pipeline to pull the geometry from the raw pixels, then reconstructed the full machine part.

**Cyber capabilities**: Better at finding vulnerabilities but deliberately not trained on how to exploit them. Comes close to Mythos 5 at finding cybersecurity vulnerabilities but remains substantially behind Mythos 5 on exploitation.

## References

- Anthropic prompting guide for Claude Opus 5
- Thariq Shihipar: "The new rules of context engineering for Claude 5 generation models"
- Anthropic's official Opus 5 announcement
