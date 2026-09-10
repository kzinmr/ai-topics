---
source_url: https://lucumr.pocoo.org/2026/9/7/astra-why/
ingested: 2026-09-11
sha256: 2d3233e197081037944018904861700f81567627c999cf3d4b45d88801c4576c
---

# Astra for Coding: Why Are We Doing This Again? — Armin Ronacher (2026-09-07)

Note: this file is a condensed analytical digest of Ronacher's 2,775-line raw post
(`lucumr.pocoo.org--2026-9-7-astra-why--f41d7a13.md`), captured to give the
"involution" framing a traceable source. See that raw file for the full evidence
dump (Python string-splicing examples, tool-call logs).

## Thesis: AI engineering as Neijuan (内巻 / involution)

Ronacher opens by framing current AI engineering as **Neijuan (内巻, "curl inwards")** —
the Chinese term for a system that "demands ever more effort and competition without
improving output" (Western equivalent: "involution," from *Agricultural Involution*).
Agricultural involution = raising productivity per square meter while leaving
productivity per head unchanged. "That's how I feel about AI right now."

## The Slop Factory experiment

- Built a weekend "software factory" on **GPT-6 Astra**, letting the model decide the
  entire workflow, manage its own context, keep records in an `agent-notes` folder, and
  spin off subagents autonomously.
- Goal: a Python with virtual threads + lexical scoping.
- Cost: a **full ChatGPT reset's worth of tokens ≈ 4 billion tokens**, run over **35 hours
  with zero human oversight**.
- Outcome (verbatim): "the factory has delivered **absolutely nothing of value** and also
  not taught me anything about how to operate a better one."

## Why Astra produces the code it does

Ronacher's diagnosis: Astra is heavily rewarded for succeeding on **long-horizon tasks**
but gets **little punishment for low-quality ("shitty") code**. Consequence: it is amazing
at 3D work and can keep generating autonomously for a very long time (he had it reverse-
engineer his robot vacuum impressively), but the code quality is poor.

Concrete anti-patterns observed (in Codex harness, also in Pi/TypeScript):
- **Codegolf tool calls**: Astra over-uses on-demand Python to read/manipulate files
  (older Codex used bash/sed; Astra goes excessive Python).
- **Python string-splicing to edit C code**: subagents do manual `str.replace`/slicing
  via `pathlib.read_text().replace(...)` instead of using the patch tool — captured
  against CPython internals (`pycore_intrinsics.h`, `intrinsics.c`). Ronacher notes the
  project is "very meta" since he worked on CPython itself.

## Takeaway

Raw capability (Astra is "incredibly impressive" at computer use, images, long-horizon
persistence) does not translate into usable software engineering output. The bottleneck
is not the model's ability to keep going — it is the **reward shape** (completion over
correctness) and the absence of a verification gate. This is the empirical counterpart to
[[concepts/formal-verification-llm-agents]]: without a mechanically checkable correctness
signal, an agent rewarded for "keep going / succeed at horizon" optimizes for volume, not
value.
