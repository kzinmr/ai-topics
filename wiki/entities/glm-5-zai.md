---
title: GLM-5 (Z.ai)
type: entity
created: 2026-04-10
updated: 2026-06-18
tags:
- entity
- model
- open-weight
- mixture-of-experts
- benchmark
- long-context
- sparse-attention
- speculative-decoding
related:
- chinese-ai
- open-weights
- llm-benchmarks
sources:
- raw/articles/2026-06-17_ainews_glm-52-indexshare.md
- raw/articles/simonwillison.net--2026-jun-17-glm-52--41b7cb7d.md
---

# GLM-5 (Z.ai)

New state-of-the-art open weights LLM from Z.ai (智谱AI).

> **Latest variant: GLM-5.2**, released June 17, 2026 — an MIT-licensed open-weight frontier model focused on coding and long-horizon agentic work.

## Key Details

### GLM-5.2 Model Architecture (June 2026)
- **Parameters:** 744B total, 40B active per token (Mixture-of-Experts)
- **License:** MIT
- **Context window:** 1M tokens
- **Two reasoning effort modes:** high and max
- **API pricing:** $1.4 / $4.4 per input/output MTokens (same as GLM-5.1)
- **Architecture:** Built on DeepSeek Sparse Attention, extended with [[concepts/index-share|IndexShare]]
- **Speculative decoding:** Improved MTP (multi-token prediction) for faster inference

### IndexShare
A novel technique extending DeepSeek Sparse Attention that reuses one indexer across every four sparse layers, improving efficiency at ultra-long contexts. See [[concepts/index-share]] for details.

### GLM-5.2 Benchmark Performance
- **FrontierSWE:** #3 overall (behind Fable 5, Opus 4.8; ahead of GPT-5.5)
- **Design Arena:** #1, Elo 1360 (+27 Elo, surpassing Fable 5)
- **Agent Arena:** #10 overall, #1 open model by wide margin
- **Code Arena Frontend:** #2 overall, #2 React, #4 HTML
- **Terminal-Bench 2.1:** 81.0 (vs 62.0 for GLM-5.1 — first open-weight model to cross 80%)
- **Text Arena:** #25 overall
- **Long-horizon coding:** 74.4 (ahead of GPT-5.5's 72.6)

### Ecosystem Support (Day 0)
Transformers, vLLM, SGLang, Cloudflare Workers AI, OpenRouter, Ollama Cloud, Baseten, DeepInfra, Fireworks, Notion.

### General Performance
- Competitive with frontier proprietary models
- Strong benchmark performance across coding, agentic, and design tasks

### Developer
- Z.ai (智谱AI) — Chinese AI company
- Part of China's push in open AI
- Follows GLM-4, GLM-5V-Turbo, and GLM-5.1 releases

### Strategic Context
- Demonstrates China's advancing AI capabilities
- Open weights strategy (MIT license) vs proprietary models
- Competition with Western labs (OpenAI, Anthropic, Google)
- Part of broader Chinese AI ecosystem growth

## Sources
- raw/articles/2026-06-17_ainews_glm-52-indexshare.md
- raw/articles/simonwillison.net--2026-jun-17-glm-52--41b7cb7d.md

## Independent Review: Simon Willison (June 17, 2026)

Simon Willison reviewed GLM-5.2 and highlighted several key findings:

- **Artificial Analysis Intelligence Index**: GLM-5.2 ranked #1 open weights model at 51 points, ahead of MiniMax-M3 (44), DeepSeek V4 Pro (max, 44), and Kimi K2.6 (43)
- **Code Arena WebDev**: #2 overall, behind only Claude Fable 5 — impressive given the model lacks image input
- **Token hunger**: Uses 43k output tokens per Intelligence Index task (vs GLM-5.1 26k, MiniMax-M3 24k, Kimi K2.6 35k, DeepSeek V4 Pro 37k)
- **Pricing via OpenRouter**: ~$1.40/M input, ~$4.40/M output from 9 providers. For comparison: GPT-5.5 is $5/$30, Claude Opus 4.5-4.8 is $5/$25
- **SVG generation**: Strong pelican on bicycle (self-contained animated SVG), but disappointing opossum on e-scooter (step down from GLM-5.1)
