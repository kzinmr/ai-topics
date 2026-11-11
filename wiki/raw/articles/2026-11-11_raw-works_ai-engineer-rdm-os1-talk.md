---
title: "Your Agent Doesn't Need an LLM for Every Decision — Raymond Weitekamp (aiDotEngineer talk)"
type: raw
source_url: https://www.youtube.com/watch?v=hFNbPmzzcEs
author: Raymond Weitekamp (@raw_works, OpenProse)
published: 2026-11-11
captured: 2026-11-11
origin: x-accounts-scan (tweet 2120533459227562414, 2026-11-11T15:05:48Z)
status: complete (full transcript in transcripts/hFNbPmzzcEs_ai-engineer-raymond-weitekamp-operating-system-one.md)
---

# Your Agent Doesn't Need an LLM for Every Decision — Raymond Weitekamp, OpenProse

> The original yt-dlp caption pull hit repeated HTTP 429s; the full transcript was
> subsequently retrieved the same day via the `youtube-content` skill's
> `fetch_transcript.py` helper and saved to
> `transcripts/hFNbPmzzcEs_ai-engineer-raymond-weitekamp-operating-system-one.md`
> (~7,900 words). Key points below are drawn from the transcript.

## Official video description (verbatim, from yt-dlp)

> Recursive language models have become a powerful harness pattern for LLMs. Raymond
> Weitekamp shows how the same idea applies to decision models, the fast classifiers
> also called System One models, to build far more efficient workflows for coding
> agents, information retrieval and computer use. He introduces Recursive Decision
> Models, shares a vision for real-time interfaces he calls Operating System One, and
> previews oSo, a new computer use decision agent.
>
> Raymond Weitekamp, OpenProse: https://x.com/raw_works | https://openprose.ai
> More: https://recursivedecisionmodels.com | https://github.com/rawwerks/rdm | https://oSo.computer

## Tweet announcing the talk

> "hey apparently my talk on \"operating system one\" is now live on the @aiDotEngineer yt!"
> — @raw_works, 2026-11-11T15:05:48Z
> https://x.com/raw_works/status/2120533459227562414

## Key points (from the full transcript)

- **Reframing**: Weitekamp submitted the talk under the title "Recursive Decision Models" but
  realized it is really about **"Operating System One"** — the talk's true subject.
- **Naming**: "System One" comes from Kahneman (*Thinking, Fast and Slow*) via TypeSafe's Jev
  launch (~2 months prior). Community consensus is "decision models"; the holdout camp insists on
  "zero-shot classifiers". He notes Almeida's argument that *Jev makes judgments, your code makes
  the decision* — "absolutely correct."
- **Core question of the talk**: *"What if reasoning was actually many small decisions?"* — tasks
  naively assumed to require deliberate reasoning may instead be solved by architecting many tiny,
  very fast decisions.
- **RDM = RLM applied to decision models**: direct analogy to MIT's RLM (Alex Zhang / Omar Khattab,
  ~1 year old) — root decision model calls sub-decision-models up to a max depth. Three rules:
  (1) context stays outside the model, code slices it; (2) a decision can choose to call another
  decision; (3) must work with **no generative model at all** ("decisions all the way down" — this
  is what proves the architecture is correct) *and* must compose with LLMs/agents.
- **Contrast framing**: generative models diverge, decision models converge — "yin and yang"; Jev as
  a counterbalancing force to the generation-first AI market.
- **Underappreciated prior art**: TypeSafe's launch demos — **Jev Plays Doom** (two coupled decision
  harnesses: first-person shooter + map-exploration, pure Jev calls), hierarchical Shopify
  category search (beam search "without the beam"), Lily/Nathan multimodal hit-zoom / recursive
  image halving.
- **His demos**: Factorio played by a pure-RDM agent (no LLM anywhere); **Earshot** — a precursor to
  oSo where a tiny Chai (successor to Wekinator, real-time ML) model supervised-learns voice commands to ~45 ms
  latency, with an upper RDM layer deciding *when to trust* the small model; roots in Princeton
  Laptop Orchestra / Wekinator real-time ML (~18 years ago).
- **The Map**: shared interface between decision model (can only point/judge) and LLM (unstructured
  output) — a set of named pointers with descriptions + underlying functions; the LLM can add/edit
  the map (learning e.g. "movie time" = TV on + lights off); the map can be multi-dimensional
  (embeddings — cites Kieran Clausen's semantic low-dim embeddings idea).
- **The Arbiter** (4th primitive): decision models are fast/cheap enough to run *many speculatively
  in parallel*; like CPU read/write locks, an arbiter gates which speculative decision is allowed to
  mutate shared state. Informed by Alex Zhang's speculative programmatic tool calling.
- **Implementations**: original as a **DSPy module** (thanks to cmpnd.ai adding System One API
  support to DSPy), plus a standalone **Rust package `rdm`** (github.com/rawwerks/rdm) for fast,
  portable deployment.
- **oSo** (oSo.computer, "Operating System 1", waitlist): a **computer-use agent built on RDMs —
  "decision first"**. Voice is the first input modality; goal is working on a computer without
  touching keyboard/mouse ("radical human-computer interfacing"; cites tech-neck/RSI suffering from
  QWERTY+mouse coupling, and Matt Mastracci's Hunch Pictionary doodle classifier at ~150 ms on
  WebGPU). It can farm jobs to normal coding agents (Claude Code, Codex) but routes decisions to
  the fastest/smallest trusted model over time (arbiter idea). His take on the terminal-ification of
  coding: the terminal isn't special — it was a flight from the limitations of default GUIs.
- Also references his earlier aiDotEngineer talk "Recursive Coding Agents" (AI Engineer World's Fair,
  summer 2026).

Canonical resources: https://recursivedecisionmodels.com · https://github.com/rawwerks/rdm · https://openprose.ai

## Relation to existing wiki

- `wiki/entities/raw-works.md` — author entity page (updated 2026-11-11 with this talk).
- `wiki/concepts/recursive-decision-models.md` — the concept page this talk presents.
- `wiki/concepts/system-one-models`, `wiki/concepts/rlm-recursive-language-models`,
  `wiki/entities/typesafe-ai`, `wiki/concepts/dspy` — lineage.
