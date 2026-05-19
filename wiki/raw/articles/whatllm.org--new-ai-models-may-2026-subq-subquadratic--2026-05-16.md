# SubQ: The First Commercial Subquadratic LLM

> Source: WhatLLM.org — "New AI Models May 2026: The Frontier Took a Breath, Architecture Took the Stage" by Dylan Bristot, May 13, 2026
> URL: https://whatllm.org/blog/new-ai-models-may-2026

The most interesting release in May 2026 isn't from a name on existing leaderboards. **SubQ** (the company is Subquadratic, the first model is SubQ 1M-Preview) launched on May 5 with $29M in seed funding and a single claim: their model is not a transformer.

Standard transformer attention is O(n²) in context length. Double the context, quadruple the cost. SubQ uses sparse, subquadratic attention end to end. The first release ships with a native 12 million token context window. Subquadratic claims roughly 1/5 the cost of frontier models on long-context tasks and up to 52x faster attention at scale.

Key details:
- **Architecture**: Subquadratic sparse attention, not a standard transformer. First commercially available LLM built this way.
- **Context**: Native 12 million tokens. Designed for repo-wide code, long document analysis, and multi-document research.
- **Cost claim**: ~1/5 of frontier model cost on long-context workloads.
- **Speed claim**: Up to 52x faster attention at scale (vendor figure, awaiting independent confirmation).
- **Funding**: $29M seed, May 2026.
- **Products**: API access plus SubQ Code, a repo-wide coding agent built to use the full context.

Caveats: Headline numbers are vendor numbers. No third party has yet posted SubQ against MRCR, RULER, or other long-context benchmarks. "Subquadratic attention" as a research area is not new — Mamba, RWKV, Hyena, BASED, and other efforts have shown promise and then plateaued when pushed against frontier scale.

## The broader May 2026 context

April 2026 was the loudest month in years: GPT-5.5 broke 60 on the Intelligence Index, Opus 4.7 landed, DeepSeek V4, Kimi K2.6, and MiMo V2.5 Pro all crossed 50. May opened with no new frontier LLM in the first week. The model layer went quiet while everything else got loud — distribution, infrastructure, architecture.

Notable May 1-13 releases:
- May 5: GPT-5.5 Instant (OpenAI) — ChatGPT default
- May 5: SubQ 1M-Preview (Subquadratic) — first commercial subquadratic LLM
- May 6: Grok 4.3 (xAI) — X / xAI API
- May 6: ZAYA1-8B (Zyphra) — MoE, Apache 2.0, trained on AMD
- May 8: Gemini 3.1 Flash Lite (Google) — gateways
