---
title: "How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind"
url: "https://www.youtube.com/watch?v=7gujZrJ9L5I"
fetched_at: 2026-05-25T07:01:33+00:00
source: "AI Engineer (YouTube)"
tags: [youtube, raw, talk]
---

# How Google DeepMind Runs Agents at Scale

**Panelists:** Ian Ballantyne (Developer Relations Engineer) & KP Sawhney (Software Engineer), Google DeepMind
**Source:** AI Engineer Conference (2026-05-24), 25-minute panel
**Key Themes:** Agent architecture, scaling, quota management, skills libraries, deep research pipeline evolution, internal tooling.

## Key Excerpts

### On Token Quotas and Resource Management

> "Google DeepMind employees have worse token quotas than paying customers. That is not a mistake. KP Sawhney explains: customers get priority, and if an internal team spikes usage on a cluster someone monitoring 24/7 will just call and ask them to stop."

> "Honestly right now it's kind of brute force with the quota. So we have some real power users at DeepMind and ultimately it gets to a point where it's like, okay, you've got to just stop right now."

### On Skills Libraries

> "There's a huge amount of focus on building up a huge library of skills that enable folks to do their job better. … making sure that only the best ones survive, really, almost Darwinian nature."

### On the Future of Deep Research

> "My focus has turned now to making best use of this anti-gravity harness internally … starting to think about how we generalize this to a variety of other use cases. So, potentially deep research itself rather than passing around huge huge blobs of text from the searches that have been done, why not have the different parts of that pipeline collaborate in a shared file system?"

### On Model Mixing & Efficiency

> "What's going to be really interesting for folks like yourselves is mixing and matching between models like Gemma 4 which are effectively free from a quota perspective just using your whatever GPUs or TPUs you have, and then using the more advanced models for specific components of the agentic system."

## Summary

### Antigravity IDE & Agent Manager
- Antigravity is an internal IDE (Visual Studio–like) with a built-in agent manager
- You can spawn multiple agents working on different projects, each with their own planning system, to-do lists, and browser interaction capability
- The scratch pad reveals the agent's reasoning trace, enabling debugging and intervention

### How DeepMind Thinks About Agents at Scale
1. **Quota & Resource Control**: Token quotas strictly managed; internal employees have lower quotas than customers. SRE teams monitor 24/7.
2. **Skills Libraries**: Large, shared library of skills built by domain experts. Darwinian process ensures only the best survive.
3. **Deep Research Pipeline Evolution**: Moving from passing massive context blobs to shared file system collaboration between pipeline components.
4. **Model Mixing**: Combining cheap models (Gemma 4) for bulk work with advanced models for critical components.
5. **Code Review Automation**: Per-language auto-review models fine-tuned on style guides and good code examples.
