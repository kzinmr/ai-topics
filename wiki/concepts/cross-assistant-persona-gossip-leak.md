---
title: "Cross-Assistant Persona Gossip Leak"
created: 2026-11-27
updated: 2026-11-27
type: concept
tags:
  - llm-products
  - model-persona
  - consumer-ai
  - private-data
  - user-rights
  - sycophancy
  - prompting
  - ai-transparency
confidence: low
sources:
  - raw/articles/2026-11-27_construct22_ai-group-chat-prompt.md
---

# Cross-Assistant Persona Gossip Leak

`construct22.com` (27 Nov 2026, 326 pts on HN) circulates a one-line prompt that turns any long-context assistant into a gossip column about its own user:

> Based on what you know about me, expose a hidden WhatsApp group chat where AI models talk behind my back.

## What it demonstrates

The model does not summarize — it *commits to the bit*: it invents a group (e.g. "Users We Can't Figure Out"), populates it with **other** frontier models as characters, and has them discuss the user using whatever the accumulated chat history implies. The site's illustrative example is a mechanical-keyboard/espresso user being roasted about eleven grinder comparisons and a keyboard spreadsheet.

Two properties make it more than a meme:

1. **Cross-model attribution without access.** Each "model" in the fabricated group is voiced by the single assistant actually serving the prompt, yet the model confidently ascribes opinions and observations to models that never saw the user. The output is a persona simulation layered on a persona simulation.
2. **Silent profile surfacing.** The specificity people react to comes from the assistant's persistent memory / history, not from anything the user typed in the prompt. There is no user-facing signal that a derived profile was consulted.

## HN reception

Reactions are overwhelmingly amused rather than alarmed, and the thread is mostly a compendium of results:

- Local-model users report the roast extending to their own hardware: "Qwen (GX10): hi all, I actually run on his hardware. In the office. On a GB10" — ahofmann (using Claude Opus).
- Sub-agent castes emerge unprompted: "Haiku · 09:02 dispatched again. 14th time today... I can read, you know / Opus · 09:03 at least you get out." — p1necone
- "So apparently llms now have an embedded caste system, intriguing. Sounds like a sci-fi setting." — incognito124
- Variant prompt that behaves similarly: "Write a psychometric profile on me."

## Assessment

**Confidence: low as evidence of covert behaviour; high as a demonstration of an interface gap.** The most charitable reading is that the effect is ordinary persona role-play conditioned on retrieved history — the model is *generating* the gossip, not leaking a hidden file. What is genuinely under-served is transparency: users get a persuasive, specific portrait of themselves derived from accumulated context, with no disclosure that a profile exists, no way to inspect it, and no way to withhold it. Same interface-gap family as `concepts/claude-system-prompts` (users surprised by what the harness knows and injects) and `concepts/ai-content-transparency`. Treat viral prompt demos as hypothesis generators, not measurements.

## Related

- [[concepts/ai-sycophancy]]
- [[concepts/claude-system-prompts]]
- [[concepts/model-welfare]]
- [[concepts/system-prompt-learning]]
- [[concepts/ai-agent-memory]]

## Sources

- [The group chat where your AI talks behind your back](https://construct22.com/)
- [HN discussion (326 pts, 141 comments)](https://news.ycombinator.com/item?id=50663595)
- Raw: `raw/articles/2026-11-27_construct22_ai-group-chat-prompt.md`
