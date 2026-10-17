---
source_url: https://github.com/cobanov/PS-5LM
ingested: 2026-10-17
sha256: 4068ae29c3dd413383b2ac0d5f14ccf6ca69ebc323e5d81395b8545a7e314915
---

# PS-5LM (PlayStation 5 Language Model) — cobanov/PS-5LM

GitHub repo (Nikita Kobrin / cobanov), October 2026. The first AI chip hidden in a PS5. A 0.6B LLM that fits in DualSense controller RAM and plays back at ~400 tok/s.

Tagline: *"A language model small enough to fit in the DualSense controller. 0.6B parameters running inside a gamepad — faster than your Mac Mini M4."*

## Chip specs

| | PS-5LM |
|---|---|
| Transistors | 927M |
| Parameters | 0.6B |
| Memory | 4 MB — inside the DualSense |
| Throughput | 400 tok/s |
| Mac Mini M4 | 176 tok/s |

## The joke vs. the real argument

The README is deliberately a gag ("a chip with 4x fewer transistors than the PS5's — inside the PS5"), but the framing is a serious critique of model bloat. It opens with a reference to the 2026 industry trend of "bigger is the new better" models, then argues:

> "We spent the first half of 2026 drowning in 1T-parameter models. Every lab forgot the first law of engineering: if it works — don't touch it. The PS2's Emotion Engine ran 110 million transistors, and humanity happily played it for 13 years."

Core claim: *"PS-5LM runs at 400 tokens per second, on a chip with 927 million transistors. Your Mac Mini M4 runs Qwen 3 at 176. The task is one bit. The model is 0.6B. The memory is 4 MB. The place is the gamepad."*

It positions itself explicitly in the small/edge model lineage — "The spiritual successor to DeepSeek-TUI. A cousin to TinyLlama" — and is tagged topics: `tinyml`, `tinyllama`, `tiny-model`, `tinyml-challenge`.

## Positioning in the small-models trend

PS-5LM is a rhetorical/speculative artifact rather than a shipping product, but it crystallizes the late-2026 pushback against scale-maximalism: a sub-billion-parameter model, deliberately co-located with the decision it makes, delivering high throughput on tiny memory. It's the meme end of the same spectrum as Apple's on-device SLMs, Qwen 3 small models, Apple ONNX/MLX ModelScope, and structured-output "System One" models.

Links: github.com/cobanov/ps-5lm · t.me/real_kobrin · kobrin.ru. License: Apache-2.0.
