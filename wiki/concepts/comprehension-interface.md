---
title: "Comprehension Interface"
type: concept
created: 2026-10-02
updated: 2026-10-02
tags:
  - concept
  - human-in-the-loop
  - agent-communication
  - html
  - cognitive-science
  - ai-assistance
  - methodology
sources:
  - "raw/articles/2026-10-02_karpathy_understanding-llm-outputs-formats.md"
  - "raw/articles/2026-05-11_karpathy_html-and-vision-progression.md"
aliases:
  - comprehension-interface
  - understanding-llm-outputs
related:
  - "[[concepts/ai-output-format-progression]]"
  - "[[concepts/cognitive-load-theory]]"
  - "[[concepts/cognitive-debt]]"
---

# Comprehension Interface

> "We'll be spending a lot more time trying to understand the outputs of language models." — Andrej Karpathy, Oct 2, 2026

The **comprehension interface** is the layer of output formats and prompting techniques a human uses to *understand* what an LLM produced or explains — as opposed to techniques for getting the model to *generate* better content. Karpathy's Oct 2026 Note Tweet (30.9K likes, 40.1K bookmarks) frames it as the emerging bottleneck of AI-assisted work: as models do more legwork autonomously, human work "rises up the abstractions into oversight and understanding," and the rate-limiting factor becomes how fast a human can parse what the model knows and did.

## Karpathy's Escalating Format Ladder

Karpathy presents four output formats, each introduced with "But even better," ordered by increasing human comprehension efficiency:

| # | Format | Technique | Why |
|---|--------|-----------|-----|
| 1 | **Writing** | Ask the LLM to explain in **ASD-STE100** (Simplified Technical English) | Controlled-language spec from aerospace maintenance docs; heavy constraints on sentence style strip filler. Softening tip: "80% of the way to ASD-STE100" |
| 2 | **Diagrams / images** | Ask for a diagram instead of prose | Easier to process, parse, and understand than sequential text |
| 3 | **Web pages** | Ask for output "in HTML" | LLM frontend skills now yield beautiful, interactive, animated explainers |
| 4 | **Explainer videos** | "Create a 3b1b style video explainer on X. Use my ElevenLabs API key for audio narration" | The format Karpathy is "most bullish on": fully bespoke videos on any topic — "This is actually starting to work!" |

Fallback for the video tier: ask the LLM itself to find free TTS alternatives that use local compute.

## The Two Theses

1. **Work rises into oversight and understanding.** As LLMs automate the legwork, the human's remaining job is comprehension — reviewing, verifying, and understanding model output. This is the same shift described in [[concepts/agentic-engineering]] and Simon Willison's "AI doesn't reduce work; it intensifies it" ([[concepts/cognitive-cost-of-agents]]).
2. **Discardable software artifacts.** Because intelligence and code are now abundant, it makes economic sense to request large, custom, one-off artifacts (a web app to explain this concept, a video for this paper) that would never have been worth building before. This extends Thariq Shihipar's "disposable micro-apps" and "compute allocator" framing ([[concepts/ai-output-format-progression]]).

## Why Formats Matter: the Cognitive-Load View

Cognitive load theory (Zakirullin, via Sweller) says working memory holds ~4 chunks, and confusion is caused by exceeding that limit ([[concepts/cognitive-load-theory]]). Each rung of Karpathy's ladder is a direct attack on working-memory limits:

- **ASD-STE100** reduces *extraneous* load — no filler, unambiguous sentences, restricted vocabulary. (Ben Tossell's two-line custom-instruction variant predates Karpathy's endorsement; see [[concepts/prompt-engineering]] §ASD-STE100.)
- **Diagrams** exploit spatial processing — a structure map fits in working memory where a 2,000-word explanation does not.
- **HTML pages** add *interactivity*: progressive disclosure (collapsible sections, sliders) lets the reader control what enters working memory — the inverse of drowning in a wall of text ([[concepts/drowning-in-documents-paradox]]).
- **Videos** offload parsing entirely to narration + animation.

## The Other Side of the Coin

A comprehension interface optimizes the *reading* side of cognitive load; it does not resolve the deeper risks documented elsewhere in this wiki:

- **[[concepts/cognitive-debt]]** — understanding *at the interface* may still be shallow. MIT's "Your Brain on ChatGPT" found 83% of LLM users couldn't quote what they had just read/watched; Anthropic's trial found posture (asking conceptual questions vs. copy-pasting) determined learning, not the tool. A gorgeous HTML explainer can produce the *feeling* of understanding without retention.
- **[[concepts/cognitive-surrender]]** — frictionless formats lower the motivation to critically engage.
- **[[concepts/simulacrum-of-knowledge-work]]** — beautiful generated outputs are also perfect proxies, making it harder to tell polished explanation from correct explanation.
- **[[concepts/agent-human-oversight-failure]]** — faster comprehension of agent output doesn't shrink the gap between what the agent *says* it did and what it did; oversight fails for reasons format polish can't fix.

Karpathy himself pairs the format ladder with his standing "understanding is the bottleneck" thesis (see [[entities/andrej-karpathy]] §Core Ideas) — the format tricks buy throughput on comprehension, on top of which genuine oversight still must be exercised.

## Relationship to AI Output Format Progression

Karpathy's May 2026 framework ([[concepts/ai-output-format-progression]]) is the *production-side* view: text → Markdown → HTML → interactive neural simulations, driven by "audio in, vision out" (vision is the 10-lane superhighway into the brain). The Oct 2026 post is the *consumption-side* complement: given any topic or model output, pick the format that maximizes your own comprehension speed. Together they form the comprehension interface thesis end-to-end: output modalities should be chosen by the bandwidth of human vision and the limits of working memory, not by what's cheapest for the model to emit.

## Practical Recipe

From the post and adjacent practice:

1. Default reading format: append "explain in ASD-STE100" (or "80% of the way") to explanation prompts.
2. For anything structural: "make me a diagram" (SVG inside Markdown/HTML).
3. For anything you'll actually read: "output as a single self-contained HTML file" with collapsible sections.
4. For deep dives: request a 3Blue1Brown-style narrated video; wire narration via ElevenLabs API key or local TTS.
5. Treat each artifact as discardable — generate a fresh custom one per question instead of reusing a static doc.

## Related Pages

- [[concepts/ai-output-format-progression]] — Karpathy's May 2026 production-side framework (HTML as new default)
- [[concepts/cognitive-load-theory]] — working-memory limits the ladder exploits
- [[concepts/cognitive-debt]] — the risk the ladder does not remove
- [[concepts/cognitive-cost-of-agents]] — Willison: load shifts, not disappears
- [[concepts/prompt-engineering]] — ASD-STE100 as persistent custom instruction
- [[concepts/agent-communication]] — how agents communicate with humans
- [[concepts/agentic-engineering]] — oversight as the human role
- [[concepts/drowning-in-documents-paradox]] — why walls of text fail
- [[entities/andrej-karpathy]] — author
- [[entities/grant-sanderson-3blue1brown]] — the "3b1b style" reference
- [[entities/thariq-shihipar]] — HTML effectiveness case
- [[entities/artem-zakirullin]] — cognitive load framework

## References

- [[raw/articles/2026-10-02_karpathy_understanding-llm-outputs-formats]] — full Note Tweet text (this page's primary source)
- [[raw/articles/2026-05-11_karpathy_html-and-vision-progression]] — companion May 2026 Note Tweet
- Post: https://x.com/karpathy/status/2105819303471976479
