---
title: "LLM Landscape: November 2025 – May 2026"
created: 2026-05-19
updated: 2026-05-19
type: concept
tags:
  - model
  - timeline
  - reasoning
  - coding-agents
  - openclaw
  - local-llm
  - open-source
  - rlvr
  - comparison
sources:
  - raw/articles/simonwillison.net--2026-may-19-5-minute-llms--498c7192.md
---

# LLM Landscape: November 2025 – May 2026

Simon Willison's lightning talk at PyCon US 2026, summarizing six months of LLM developments in five minutes.

## The November 2025 Inflection Point

November 2025 was a critical month for LLMs, especially for coding. Two major themes emerged:

1. **The frontier model crown changed hands five times** between three providers
2. **Coding agents crossed a quality barrier** — going from "often-works" to "mostly-works"

### Model Race Timeline

| Date | Model | Provider | Notes |
|------|-------|----------|-------|
| Sep 29, 2025 | Claude Sonnet 4.5 | Anthropic | Pre-November "best" model |
| Nov 2025 | GPT-5.1 | OpenAI | First to dethrone Sonnet 4.5 |
| Nov 2025 | Gemini 3 | Google | Briefly held the crown |
| Nov 2025 | GPT-5.1 Codex Max | OpenAI | Coding-specialized variant |
| Nov 2025 | Claude Opus 4.5 | Anthropic | Held crown for following months |
| Feb 2026 | Gemini 3.1 Pro | Google | Significant vision/image generation improvements |
| Apr 2026 | Gemma 4 series | Google | Most capable open-weight models from a US company |
| Apr 2026 | GLM-5.1 | GLM (China) | Open-weight 1.5TB monster model |

## Coding Agents Cross the Quality Barrier

OpenAI and Anthropic spent most of 2025 running **Reinforcement Learning from Verifiable Rewards (RLVR)** to increase code generation quality. By November, the results became apparent:

> "Coding agents went from often-work to mostly-work, crossing a quality barrier where you could use them as a daily-driver to get real work done, without needing to spend most of your time fixing their stupid mistakes."

This enabled a wave of experimentation during the December–January holiday period, including Willison's own exploration of ambitious agent-driven projects (some of which were "quietly retired").

## The Rise of Claws: OpenClaw Ecosystem

- **November 2025**: First commit to "Warelay" repo by Pete (Peter Steinberger)
- **December–January**: Multiple name changes
- **February 2026**: Launched as **[[entities/openclaw|OpenClaw]]** — took the world by storm

The term **"Claws"** became a generic category for personal AI assistants (OpenClaw, NanoClaw, ZeroClaw, etc.). Mac Minis sold out around Silicon Valley as people bought them to run Claws — described as "digital pets" with a Mac Mini as "the perfect aquarium."

### Doc Ock Metaphor

Willison's favorite metaphor: Alfred Molina's Doc Ock in Spider-Man 2 — AI-powered claws that are perfectly safe until the inhibitor chip is damaged, after which they turn evil and take over.

## Open-Weight Models Exceed Expectations

While frontier models dominated the headline race, **laptop-available open-weight models began wildly outperforming expectations**:

| Model | Provider | Key Features |
|-------|----------|-------------|
| **Gemma 4 series** | Google | Most capable open-weight from US company |
| **GLM-5.1** | GLM (China) | 1.5TB parameters, open-weight, strong vision generation |

Willison notes that Gemma 4 and GLM-5.1 represent a significant shift — open-weight models reaching frontier-competitive quality, even if still behind the absolute best.

## The Pelican-on-Bicycle Benchmark

Willison's signature evaluation: "Generate an SVG of a pelican riding a bicycle." Pelicans are hard to draw, bicycles are hard to draw, and pelicans can't ride bicycles — making it an impossible-to-game creativity test.

| Model | Pelican Quality | Notes |
|-------|----------------|-------|
| Claude Sonnet 4.5 | Basic | September 2025 baseline |
| Gemini 3 | Best still frame | Fish in basket detail |
| Gemini 3.1 Pro | Excellent | Animated capabilities (pelican, frog, giraffe, ostrich, turtle, dachshund) |
| GLM-5.1 | Very competent | Animation had warping issues |
| GLM-5.1 + custom prompt | Best overall | "North Virginia Opossum on an E-scooter" — "Cruising the commonwealth since dusk" |

> Jeff Dean tweeted a video of animated pelicans from Gemini 3.1 Pro, suggesting AI labs may be watching Willison's benchmark.

## Key Takeaways

1. **RLVR works**: Post-training with verifiable rewards was the key enabler for coding agent quality improvement
2. **Claws are a new category**: Always-on personal AI assistants running on local hardware
3. **Open-weight models are closing the gap**: US and Chinese labs both releasing competitive open models
4. **The frontier moves fast**: Five model changes at the top in a single month

## Related Pages

- [[entities/simon-willison|Simon Willison]] — author, Django co-creator
- [[entities/openclaw|OpenClaw]] — always-on personal AI assistant
- [[concepts/post-training/rlvr|RLVR]] — Reinforcement Learning from Verifiable Rewards
- [[entities/openai-codex|OpenAI Codex]]
- [[concepts/agentic-engineering|Agentic Engineering]]
