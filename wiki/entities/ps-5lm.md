---
title: "PS-5LM (Small-Model Provocation)"
type: entity
created: 2026-10-17
updated: 2026-10-17
tags:
  - small-models
  - model
  - ai-industry-economics
confidence: low
sources:
  - raw/articles/2026-10-17_github_ps-5lm-small-model.md
related:
  - concepts/domain-specialization-beats-general-scale
  - concepts/small-language-models
---

# PS-5LM (Small-Model Provocation)

**PS-5LM** ("PlayStation 5 Language Model") is a satirical GitHub project by Nikita Kobrin (cobanov), October 2026 — *"the first AI chip hidden in a PS5."* It is a **deliberate joke / rhetorical artifact**, not a shipping product, but it crystallizes the late-2026 pushback against scale-maximalism and is cataloged here as a meme-with-a-thesis. See [[concepts/domain-specialization-beats-general-scale]].

## The "specs" (satirical)

| | PS-5LM |
|---|---|
| Transistors | 927M |
| Parameters | 0.6B |
| Memory | 4 MB — "inside the DualSense" |
| Throughput | "400 tok/s" (vs "Mac Mini M4: 176 tok/s") |

The framing gag: "a chip with 4× fewer transistors than the PS5's — *inside* the PS5."

## The actual argument

Beyond the joke, the README makes a serious engineering critique:

> "We spent the first half of 2026 drowning in 1T-parameter models. Every lab forgot the first law of engineering: if it works — don't touch it. The PS2's Emotion Engine ran 110 million transistors, and humanity happily played it for 13 years. … The task is one bit. The model is 0.6B. The memory is 4 MB. The place is the gamepad."

Its thesis: **match the model to the task, co-locate it with the decision, don't reach for scale reflexively.** It self-positions in the tiny-model lineage — "spiritual successor to DeepSeek-TUI, a cousin to TinyLlama," tagged `tinyml`, `tinyllama`, `tiny-model`.

## Why it's in the wiki

Marked `confidence: low` because it is satire (the chip and throughput are fictional). It's kept not as a technical artifact but as a **mood indicator** of the October 2026 anti-bloat current — the same current that produces the benchmarked, serious version of the claim in [[entities/indra-ocr-agent|Indra]]. The pairing (a meme + a benchmark making the same argument the same week) is itself the signal.

## Related
- [[concepts/domain-specialization-beats-general-scale]]
- [[concepts/small-language-models]]
- [[entities/indra-ocr-agent]]

## Sources
- [cobanov/PS-5LM (GitHub)](https://github.com/cobanov/PS-5LM) (Oct 2026, Apache-2.0)
