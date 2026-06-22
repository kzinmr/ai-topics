---
title: "GLM-5.2"
created: 2026-06-18
updated: 2026-06-18
type: concept
tags:
  - model
  - open-weight
  - text-generation
  - benchmark
  - deepseek
  - coding-agents
  - context-management
  - inference
  - china
sources:
  - raw/articles/simonwillison.net--2026-jun-17-glm-52--41b7cb7d.md
  - raw/articles/2026-06-17_fireworks-ai_glm-5p2.md
  - raw/articles/2026-06-17_ainews_glm-52-indexshare.md
  - raw/articles/glm-5-1-zhipu-2026.md
---

# GLM-5.2

**GLM-5.2** is a frontier open-weights large language model released by [[entities/glm-5-zai|Z.AI (Zhipu AI)]] in June 2026. It is the successor to [[concepts/glm-5-1|GLM-5.1]] and a text-only Mixture-of-Experts (MoE) model optimized for **coding** and **long-horizon agentic work**. GLM-5.2 is the highest-ranked open-weights model on the Artificial Analysis Intelligence Index v4.1 as of June 2026.

## Release History

GLM-5.2 was released in two phases:

| Date | Milestone |
|------|-----------|
| **June 13, 2026** | Released to Z.AI coding plan subscribers |
| **June 16, 2026** | Full open weights released under **MIT license** |

The MIT license permits commercial use, modification, and redistribution with no copyleft strings or regional restrictions.

## Architecture

| Detail | Value |
|--------|-------|
| **Total Parameters** | 744B |
| **Active Parameters** | 40B (Mixture-of-Experts) |
| **Model Size** | 1.51TB |
| **Context Window** | 1,000,000 tokens (1M) |
| **Attention Mechanism** | DeepSeek Sparse Attention (DSA) + [[concepts/index-share|IndexShare]] |
| **Modality** | Text-only (no vision input) |
| **Speculative Decoding** | Improved Multi-Token Prediction (MTP) |
| **License** | MIT |
| **Reasoning Modes** | Two effort levels: high and max |

### IndexShare

GLM-5.2 introduces **IndexShare**, a novel technique extending [[concepts/deepseek-v4|DeepSeek]] Sparse Attention that reuses one indexer across every four sparse layers. This improves efficiency at ultra-long contexts without sacrificing attention quality. See [[concepts/index-share]] for full details.

### Context Window

The 1M-token context window is a 5× increase over GLM-5.1's 200K window. According to Z.AI's technical blog, making a 1M context *reliable* under real engineering pressure — holding a repository, tests, and long tool-call traces without degrading — is a significant infrastructure challenge involving KV-cache capacity, kernel overhead, and CPU-side scheduling.

## Separation from Vision Models

GLM-5.2 is strictly **text-only**. Z.AI maintains a separate vision model family, most recently represented by [[entities/glm-5v-turbo|GLM-5V-Turbo]], which is not open weights. This architectural separation allows GLM-5.2 to optimize entirely for text-based coding and reasoning tasks.

## Benchmarks

### Artificial Analysis Intelligence Index v4.1

GLM-5.2 achieved a score of **51**, making it the leading open-weights model as of June 2026:

| Model | Score |
|-------|-------|
| **GLM-5.2** | **51** |
| MiniMax-M3 | 44 |
| DeepSeek V4 Pro (max) | 44 |
| Kimi K2.6 | 43 |

### Arena Leaderboards

| Arena | Rank | Notes |
|-------|------|-------|
| **Design Arena** | #1 | Elo 1360, +27 Elo over Claude Fable 5 |
| **Code Arena WebDev** | #2 | Behind only Claude Fable 5 |
| **Code Arena React** | #2 | — |
| **Code Arena HTML** | #4 | — |
| **Agent Arena** | #10 | #1 open model by wide margin |
| **Text Arena** | #25 | General text, not GLM-5.2's strength |
| **FrontierSWE** | #3 | Behind Fable 5 and Opus 4.8; ahead of GPT-5.5 |

### Terminal-Bench 2.1

GLM-5.2 scored **81.0** on Terminal-Bench 2.1, making it the **first open-weights model to cross 80%** on this benchmark. This represents a significant leap from GLM-5.1's score of 62.0.

### Long-Horizon Coding

GLM-5.2 scored **74.4** on long-horizon coding evaluations, ahead of GPT-5.5's 72.6.

## Token-Hungry Behavior

GLM-5.2 is notably **token-hungry** compared to other leading models:

| Model | Output Tokens per Intelligence Index Task |
|-------|-------------------------------------------|
| **GLM-5.2** | **43,000** |
| DeepSeek V4 Pro (max) | 37,000 |
| Kimi K2.6 | 35,000 |
| MiniMax-M3 | 24,000 |
| GLM-5.1 | 26,000 |

GLM-5.2 uses approximately **3.5× more output tokens** than the average model on equivalent tasks (43K vs ~12K average). This verbosity contributes to its high benchmark scores but increases inference cost in production.

## Comparison with Predecessor

| Feature | GLM-5.1 | GLM-5.2 |
|---------|---------|---------|
| **Total Parameters** | 744B | 744B |
| **Active Parameters** | 40B | 40B |
| **Context Window** | 200K | 1M |
| **License** | — | MIT |
| **Attention** | DeepSeek Sparse Attention | DSA + IndexShare |
| **Terminal-Bench 2.1** | 62.0 | 81.0 |
| **Output Tokens/Task** | 26K | 43K |
| **AA Intelligence Index** | — | 51 (#1 open) |

## Comparison with Competing Open-Weight Models

| Model | Params (Total/Active) | Context | AA Index v4.1 | License |
|-------|----------------------|---------|---------------|---------|
| **GLM-5.2** | 744B / 40B | 1M | **51** | MIT |
| [[concepts/deepseek-v4|DeepSeek V4 Pro]] | 1.6T / 284B | 1M | 44 | Custom |
| [[concepts/kimi-k2-6|Kimi K2.6]] | 1T / 32B | 256K | 43 | Custom |
| [[concepts/minimax-m3|MiniMax-M3]] | — | 1M | 44 | — |

GLM-5.2 achieves the highest intelligence score with significantly fewer total parameters than DeepSeek V4 Pro (744B vs 1.6T), demonstrating a more parameter-efficient architecture for open-weights models.

## Deployment and Access

### Pricing (via OpenRouter and Fireworks)

| Token Type | Price per 1M Tokens |
|------------|---------------------|
| Input | $1.40 |
| Output | $4.40 |
| Cache Hit (Fireworks) | $0.26 |

For comparison: GPT-5.5 costs $5/$30 per M input/output tokens; Claude Opus 4.5-4.8 costs $5/$25.

### Day-Zero Ecosystem Support

GLM-5.2 launched with immediate support from: Transformers, vLLM, SGLang, Cloudflare Workers AI, OpenRouter, Ollama Cloud, Baseten, DeepInfra, Fireworks AI, and Notion. OpenRouter lists 9 different providers.

### Agent Integration

GLM-5.2 can be used as a drop-in replacement in major coding agents including **Claude Code** (via FireConnect), **OpenCode**, and any tool supporting OpenAI or Anthropic-compatible APIs.

## US-China AI Bifurcation Context

GLM-5.2's release continues the rapid pace of Chinese open-weights model development documented in [[concepts/china-agentic-coding-sprint]]. With an MIT license and no regional restrictions, it represents a counterpoint to the tightening of open-weights licensing by Western labs (see [[concepts/open-weights-licensing-tightening]]).

The model arrives alongside competing releases from Kimi, Qwen, DeepSeek, and MiniMax — all within a single week in June 2026 — demonstrating the intensity of China's open-weights frontier competition.

## Independent Evaluation: Simon Willison

Simon Willison's testing (June 17, 2026) found:
- **SVG generation**: Excellent self-contained animated SVG of a pelican on a bicycle with non-broken animations
- **Opossum SVG**: Disappointing result — a step down from GLM-5.1's output on the same prompt
- **Code Arena WebDev #2 without vision**: Impressive ranking given GLM-5.2 has no image input capability

## Related Pages

- [[entities/glm-5-zai]] — Z.AI entity page with GLM-5 family overview
- [[concepts/glm-5-1]] — Predecessor model
- [[entities/glm-5v-turbo]] — Z.AI's vision model family (not open weights)
- [[concepts/index-share]] — IndexShare attention technique
- [[concepts/deepseek-v4]] — Competing open-weights MoE model
- [[concepts/kimi-k2-6]] — Competing open-weights model from Moonshot
- [[concepts/minimax-m3]] — Competing multimodal open-weights model
- [[concepts/china-agentic-coding-sprint]] — Chinese open model competition context
- [[concepts/open-weights-licensing-tightening]] — Licensing trend context
