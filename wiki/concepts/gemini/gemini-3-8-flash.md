---
title: "Gemini 3.8 Flash & Gemini 3.8 Flash Cyber"
created: 2026-09-03
updated: 2026-09-03
type: concept
tags: [model, multimodal, frontier-models, code-model, ai-safety, text-generation, ai-agents, inference]
aliases: ["Gemini 3.8 Flash", "Gemini 3.8 Flash Cyber", "Gemini Nano"]
sources:
  - raw/articles/blog.google--innovation-and-ai-models-and-research-gemini-models-3-8-flash-and-3-8-flash-cyber.md
related:
  - concepts/gemini/gemini-3-7-flash
  - entities/deepmind
  - entities/google
  - concepts/coding-agents/agentic-coding
confidence: medium
---

# Gemini 3.8 Flash & Gemini 3.8 Flash Cyber

Announced on the Google blog on 2026-09-01, this "Gemini Drops" release ships three models: **Gemini 3.8 Flash** (the general fast-tier model), **Gemini 3.8 Flash Cyber** (a cyber-specialized variant for defensive vulnerability finding/patching), and **Gemini Nano** (on-device, Android/Chrome). Sundar Pichai's framing: *"AI has evolved from simply reading text and images to reading the room."*

## Gemini 3.8 Flash

- **Availability:** globally in the Gemini app and as a preview endpoint in Google AI Studio / Gemini API (`gemini-flash-latest`) — the fallback endpoint for developers not pinned to dated versions.
- **Positioning:** *"our best model for coding and real-world agentic tasks, particularly for finance and security"*; *"further blurs the line between Flash and Pro-class models."*
- **Benchmark:** 2x faster to first intelligent token than Claude Opus 4.7 on agentic search (LMArena Search, Aug 2026), with comparable performance.
- **Ecosystem:** rolling out as the default model across the Google Cloud suite (per Ashok Bhat's launch post).

^[[raw/articles/blog.google--innovation-and-ai-models-and-research-gemini-models-3-8-flash-and-3-8-flash-cyber.md]]

## Gemini 3.8 Flash Cyber

The release's most notable structural move: **a task- (and audience-) specialized frontier model**, not just a speed/cost tier.

- Purpose: finding and patching software vulnerabilities; defensive security work.
- **Trusted Access Program (TAP):** preview access is gated through Google's TAP program — available to a limited set of verified security researchers and participating organizations. This mirrors the "capability-gated rollout" pattern (compare OpenAI's limited-release security models) rather than the standard GA path.
- No public eval numbers were given in the launch post.

## Gemini Nano (on-device)

- Runs locally on Android/Chrome — no cloud round trip.
- Claimed ~**5x faster** than the previous Nano generation for on-device summarization, transcription, and writing assistance.
- Reinforces the industry-wide on-device/small-model trend alongside [[entities/mistral-ai|Mistral]]-class edge models.

## Assessment

Three signals worth tracking:
1. **Flash/Pro convergence** — if agentic-benchmark parity holds, the Flash tier absorbs most production workloads, compressing the pricing ladder (see [[concepts/token-economics]]).
2. **Specialized variants** — "Flash Cyber" suggests Google is bifurcating the family by *task domain*, not just by size; expect specialized siblings (finance, legal, bio) if TAP-style gating works.
3. **Gated security access** — TAP is a distribution decision as much as a safety one; it creates a two-tier developer ecosystem for defensive cyber capabilities.

Pricing and exact GA dates were not disclosed in the launch post; benchmark claims beyond the LMArena comparison are pending third-party evaluation (treat as vendor claims).

## See Also

- [[concepts/gemini/gemini-3-7-flash]] — previous Flash generation (Aug 2026)
- [[concepts/gemini/index]] — the Gemini family hub
- [[entities/deepmind]] — the lab behind it
- [[concepts/coding-agents/agentic-coding]] — the workload class Flash targets

## Sources

- raw/articles/blog.google--innovation-and-ai-models-and-research-gemini-models-3-8-flash-and-3-8-flash-cyber.md
