---
title: "[AINews] GLM-5.2: the top Frontend Coding model in the world, IndexShare for Speculative Decoding"
source: "AINews (swyx) / Latent Space"
date: 2026-06-17
url: "https://open.substack.com/pub/swyx/p/ainews-glm-52-the-top-frontend-coding"
---

Z.ai released GLM-5.2 as an MIT-licensed open-weight frontier model aimed at coding and long-horizon agentic work.

Key details:
- 744B parameter MoE, 40B active params/token
- 1M-token context window
- Two reasoning-effort modes: high and max
- Same API pricing as GLM-5.1 ($1.4/$4.4 per input/output MTokens)
- Architecture built on DeepSeek Sparse Attention extended with IndexShare
- Improved MTP (multi-token prediction) for speculative decoding

Benchmark results:
- FrontierSWE: #3 overall (behind Fable 5 and Opus 4.8, ahead of GPT-5.5)
- Design Arena: #1, Elo 1360 (+27 Elo, passing Fable 5)
- Agent Arena: #10 overall, #1 open model by wide margin
- Code Arena: Frontend: #2 overall (behind Fable 5), #2 React, #4 HTML
- Terminal-Bench 2.1: 81.0 (vs 62.0 for GLM-5.1)
- Text Arena: #25 overall
- 74.4 on long-horizon coding (ahead of GPT-5.5's 72.6)
- First open-weight model to cross 80% on Terminal-Bench

Ecosystem support: Day-zero on Transformers, vLLM, SGLang, Cloudflare Workers AI, OpenRouter, Ollama Cloud, Baseten, DeepInfra, Fireworks, Notion.

IndexShare: A novel technique extending DeepSeek Sparse Attention that reuses one indexer across every four sparse layers, improving efficiency at ultra-long contexts.
