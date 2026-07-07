---
title: Martin Alderson
type: entity
created: 2026-04-09
updated: 2026-07-07
tags:
  - person
  - blogger
  - hn-popular
  - model
  - product
  - developer-tooling
  - economics
  - quantization
  - company
sources:
  - raw/articles/martinalderson.com--posts-managed-agents-are-the-new-lambda--f9db9fb9.md
  - raw/articles/martinalderson.com--posts-built-for-turbulence-podcast--40b40da5.md
  - raw/articles/martinalderson.com--posts-is-datacentre-sovereignty-really-that-important--8195ad72.md
  - raw/articles/martinalderson.com--posts-xais-new-rental-business--bb5df5aa.md
  - raw/articles/martinalderson.com--posts-a-brief-history-of-kv-cache-compression-developments--c7414ee7.md
  - raw/articles/martinalderson.com--posts-expert-aware-quantisation--532b8e2a.md
  - raw/articles/martinalderson.com--posts-the-upcoming-ai-margin-collapse-part-1-glm-5-2--20d7e445.md
---


# Martin Alderson

| | |
|---|---|
| **Blog** | [martinalderson.com](https://martinalderson.com) |
| **RSS** | https://martinalderson.com/feed.xml |
| **Role** | Writer at the intersection of software engineering and economics; AI transformation analyst |
| **Bio** | Software engineer and blogger focused on the economics of AI, the future of SaaS, agentic coding tools, and supply chain security. Known for data-driven analysis that cuts through AI hype — particularly on SaaS disruption, compute economics, and the widening productivity gap between AI power users and casual users. |

## Core Ideas

### The "$285 Billion Markdown Files" Thesis (Feb 2026)

Martin's most viral essay documented how **13 markdown files (~156KB)** in Anthropic's `knowledge-work-plugin` repository on GitHub triggered a **$285 billion selloff** in SaaS stocks on February 3, 2026 — roughly **$1M in market cap erased per byte of markdown**. The analysis cuts through media panic to identify a genuine structural shift:

> *"Instead of SaaS being replaced by 'agentically-built' SaaS, what if people just don't need (as much) SaaS?"*

Key insight: AI agents operate at a **higher abstraction level** than traditional SaaS. Instead of navigating dashboards and clicking through UIs, users prompt agents that directly execute tasks using raw source material (markdown, text files, APIs). This means:
- Professional services firms face disruption — their expertise is being codified into structured markdown
- Legacy SaaS platforms with poor API support are vulnerable; "headless" API-first platforms will win
- The future belongs to **API-first infrastructure** that treats agents as first-class consumers

### Two Kinds of AI Users: The Bifurcation (Feb 2026)

Martin identified a dramatic productivity divide that is accelerating:

**Power Users** — Often surprisingly non-technical (finance directors, marketers, operations staff) who use Claude Code in the terminal, build custom Python scripts, chain MCPs together, and achieve **10x–100x productivity gains**. One non-technical executive converted a 30-sheet Excel financial model to Python in 2–3 prompts using Claude Code.

**Casual Users** — Stuck with M365 Copilot and web-based chatbots, generating meeting agendas and summaries. Martin's assessment: *"One extremely jarring realisation was just how poor Microsoft Copilot is."*

The structural driver: **enterprise IT lockdown** prevents agentic tooling (no local script execution, no terminal access, locked-down laptops), while smaller companies with fewer legacy constraints are "absolutely flying with AI."

> *"I don't think there's ever been a time in history where a tiny team can outcompete a company one thousand times its size so easily."*

### The Open Source Supply Chain Crisis (Mar 2026)

Martin documented the cascading **TeamPCP supply chain attack** that compromised Trivy → LiteLLM (~22M weekly downloads) → Telnyx → Axios (~100M weekly downloads) in under two weeks. Key contribution: identifying **LLMs as an accelerant** for supply chain attacks:

1. LLMs lower the barrier to finding vulnerabilities — even non-experts can discover zero-days in minutes
2. Attackers use AI to craft more sophisticated payloads
3. The cascading credential theft creates a "vicious cycle of compromises"

Proposed solutions include AI-powered pre-publish scanning by frontier labs and OS-level sandboxing for package managers (restricting `npm install` to designated directories, blocking unexpected network calls from CI/CD pipelines).

### AI Compute Economics

Martin consistently applies rigorous arithmetic to debunk AI hype and uncover genuine constraints:

- **"No, it doesn't cost Anthropic $5k per Claude Code user"** — demonstrated the viral claim doesn't survive basic math, analyzing token costs, caching, and amortization
- **"The Coming AI Compute Crunch"** — argued DRAM shortages (not capital expenditure) will define AI infrastructure growth through 2027
- **"Are we really repeating the telecoms crash with AI datacenters?"** — compared token demand growth and capacity utilization to the 2000s telecom bubble, finding the economics don't match
- **"Are OpenAI and Anthropic Really Losing Money on Inference?"** — deconstructed real costs, suggesting economics may be far more profitable than commonly claimed

#### Open-Weight Margin Collapse (July 2026)

Martin's July 2026 analysis of GLM 5.2 as the first open-weights model reaching Opus/GPT quality in practice, with significant implications for frontier lab inference margins:

- **GLM 5.2 breakthrough**: The first open-weights model that genuinely reaches Opus/GPT quality for everyday use, making it a credible drop-in replacement for frontier API inference
- **Frontier inference margins**: Analysis suggesting frontier labs operate at ~90% gross margin on API inference — the core business model is training once, then amortising over very profitable inference
- **Drop-in replacement viability**: Both Z.ai and Fireworks offer OpenAI/Anthropic compatible endpoints, making migration trivial — just change the base URL. Switching costs far lower than keeping up with frontier lab policy changes
- **Cost analysis**: GLM 5.2 at ~$4.40/MTok vs Opus at ~$25/MTok (~20% cost), potentially 50%+ cheaper after accounting for GLM's longer thinking token usage, for very similar quality
- **AMD inference efficiency**: Wafer/Zenith's analysis showing 2.75x cheaper per token on AMD vs Nvidia Blackwell for running GLM 5.2
- **Structural thesis**: Open weights fundamentally break the frontier inference margin moat — when a drop-in replacement exists at 20% of the cost, the ~90% gross margins on frontier API inference are unsustainable

Source: [[raw/articles/martinalderson.com--posts-the-upcoming-ai-margin-collapse-part-1-glm-5-2--20d7e445.md]]

### xAI as Datacentre REIT (June 2026)

Martin analyzed xAI's unexpected partnerships with **Anthropic** ($1.25bn/month for 300MW ~ 220K GPUs from Colossus 1, May 2026) and **Google** ($920mn/month for 110K GPUs, June 2026) — deals so lucrative that xAI would recoup its entire datacentre capex within **18 months** while retaining hundreds of MW of spare GPU capacity. Key structural points:

- **Anthropic's compute bind as catalyst**: Anthropic's peak-hour restrictions (5am–11am PT / 1pm–7pm GMT) and chronic capacity issues — especially during Europe/Americas overlapping work hours — created demand that xAI's underutilised Colossus 1 could absorb at enormous scale.
- **xAI's competitive moat in build speed**: The original Colossus 1 was built in **122 days** — a pace that hyperscalers cannot match (their projects take years). This construction speed advantage, inherited from SpaceX's infrastructure execution culture, is a structural edge in a world where every competitor is behind schedule on compute buildout. Even OpenAI's Stargate UAE faces disruption from the Iran conflict.
- **Grok de-prioritisation**: Most of xAI's GPU capacity is now leased to direct competitors, signalling a strategic retreat from Grok as a frontier-tier model — or that xAI over-specified capacity relative to Grok inference demand and is monetising the surplus.
- **Three-way thesis**: Martin argues all three explanations are simultaneously true to varying degrees — financial engineering (Musk/OpenAI legal battle, Google's SpaceX stake motivation), genuine compute shortage, and xAI/SpaceX's structural build-speed advantage. The magnitude of each will determine the success of the largest IPO in North American history.

> *"The more I look at it, the more xAI is starting to resemble a datacentre REIT with a frontier lab attached, rather than the other way around."*

Source: [[raw/articles/martinalderson.com--posts-xais-new-rental-business--bb5df5aa.md]]

### Agentic Coding Tool Analysis

- **"Which web frameworks are most token-efficient for AI agents?"** — benchmarked 19 frameworks; minimal frameworks cost up to 2.9x fewer tokens than full-featured ones
- **"Minification isn't obfuscation — Claude Code proves it"** — used ASTs and AI agents to reverse-engineer minified JavaScript
- **"How to generate good looking reports with Claude Code, Cowork or Codex"** — practical guide to brand extraction and report generation
- **"Using agents and Wine to move off Windows"** — documented using Claude Code to fix Linux desktop issues and get garbage-rated Windows apps working in Wine


### Managed Agents Analysis — "Managed agents are the new Lambda" (May 2026)

Martin analyzes managed agents (cloud-hosted agents) using an **AWS Lambda analogy**. Just as Lambda was a serverless revolution, managed agents are powerful but carry a "stickiness" that makes migration extremely difficult once deeply integrated.

#### Definition of Managed Agents
- **Agent harnesses (Claude Code / Codex / OpenCode equivalents) running in the cloud**
- Benefits: 24/7 operation, webhook/event-driven, sandboxing and patch management by cloud provider
- Essence: If you're already running agents in Docker, you can build this yourself

#### Vendor Lock-In Warning
- **Anthropic's pricing change (May 2026)**: Non-interactive Claude Code usage excluded from subscription token allocation → effectively a **5-20x price increase**
- **Agent interchangeability**: Migration between harnesses is relatively easy (shared basic structure of prompts, context, tools, and logs)
- **Managed agent lock-in**: When data and workflows are embedded in a provider's cloud, migration becomes a "multi-month" effort, just like Lambda function migration

#### Solutions
1. **Self-hosting**: Docker containers + OpenCode (switchable to any model provider in minutes) — Martin's current recommendation
2. **Multi-provider platforms**: Cloudflare Agents, Vercel, AWS AgentCore, Azure AI Foundry, GCP Vertex AI Agent Engine

#### Strategic Concern
> "I have a strong gut feeling the frontier labs are going to start introducing new models and capabilities that are ONLY available on their managed agent platforms."

If frontier labs begin offering new models and capabilities exclusively on their own managed agent platforms, the premise of the self-hosting strategy could collapse.


### AI-Discovered Zero-Days

Martin wrote about Anthropic's red team finding **500+ critical vulnerabilities** in abandoned software and asked: *"Who fixes the zero-days AI finds?"* This is a genuinely hard coordination problem — AI makes vulnerability discovery cheap and fast, but remediation still requires human effort on projects that may have no active maintainers.

### KV Cache Compression History

Martin documented the remarkable **100x compression** of KV cache memory per token since 2017 — from ~2.6MB/token with MHA to ~26KB/token with modern techniques. This compression matters because memory is one of the hardest physical constraints on AI infrastructure buildout.

#### The Scale of the Problem (2017)

In 2017, a 128K token context window for a 70B-parameter dense model with Multi-Head Attention (MHA) required ~340GB of GPU memory — about **2.6MB per token**. The state-of-the-art Tesla V100 shipped with 16GB HBM2, meaning ~20 GPUs were needed to hold a single conversation.

#### The Evolution: MHA → MQA → GQA → MLA

- **MQA (Multi-Query Attention, 2019)** — Noam Shazeer at Google shared a single KV head across all query heads, achieving ~64x reduction. But quality suffered significantly and long-recall degraded, limiting adoption to PaLM and Falcon.
- **GQA (Grouped Query Attention, 2023)** — Groups of query heads shared KV heads, offering an ~8x reduction with very little quality loss. Llama 2 70B and Mistral adopted it immediately, making it the default for open models. Sliding window attention emerged in parallel, where some layers only attend to a fixed window so their cache stops growing.
- **MLA (Multi-head Latent Attention, 2024)** — DeepSeek compressed keys and values into a much smaller latent vector, folding decompression into the surrounding projection matrices so full keys/values never need to be materialised. DeepSeek claimed **93% reduction** in KV cache size while *improving* quality benchmarks. This was a key enabler of DeepSeek's dramatically cheaper inference — and a decent chunk of how they wiped nearly $600bn off Nvidia's market cap in a single day in early 2025.

#### Linear-Attention Hybrids (2025)

Models like **Qwen3-Next** and **Kimi Linear** replaced most full attention layers with linear attention, keeping a small fixed-size state per layer rather than an ever-growing cache. Only a minority of layers retain a full KV cache. This unlocked **1M-token context windows** with minimal quality loss, and is presumably why Anthropic shipped a 1M context window for Claude without charging extra.

#### The Future

Research increasingly targets eliminating the quadratic attention bottleneck entirely — pure linear and recurrent approaches that maintain a fixed-size state regardless of context length. Whether they can fully match attention on quality remains an open question, but the hybrids have already proven that not every layer needs to pay full price.

#### The Economic Insight

Across nine years of ~100x compression, surprisingly little showed up as cheaper token prices. Most efficiency was spent on **longer context windows** — 4K became 128K became 1M. Much like video codecs were spent on higher resolutions rather than smaller files, KV cache compression keeps being spent on more capable agents. And with memory now one of the hardest constraints on AI buildout, this trend is expected to continue.

Source: [[raw/articles/martinalderson.com--posts-a-brief-history-of-kv-cache-compression-developments--c7414ee7.md]]

## Blog Themes

- **AI economics** — Cost analysis, compute constraints, market dynamics
- **SaaS disruption** — How agentic AI is reshaping enterprise software
- **Developer productivity** — Agentic coding tools, MCPs, token efficiency
- **Supply chain security** — Open source vulnerability cascades, LLM-accelerated attacks
- **Enterprise adoption** — The bifurcation between power users and casual users
- **AI cybersecurity discourse** — Fictional scenarios and real analysis on AI-discovered vulnerabilities

### AI-Cybersecurity Scenarios and AI-Discovered Zero-Days

Martin's August 2026 post "[29th August 2026: a scenario](https://martinalderson.com/posts/august-29-2026-a-scenario/)" uses fictional narrative to illustrate three critical theses about AI and cybersecurity:

1. **CopyFail (CVE-2026-31431)** — A real 9-year-old Linux kernel page-cache bug in crypto code, found by an AI tool in four months. Demonstrates that "the rate at which vulnerabilities get found from now on is bounded by GPU hours, not human ones."
2. **Cloud centralization risk** — Modern life depends on AWS and Azure; disaster recovery plans don't model "what happens if the fallback is also down, or if every other org on earth is failing over at the same minute."
3. **Democratization of sophisticated attacks** — "Everyone is worried about nation states. Most of the big incidents that have actually happened turned out to be a kid, a misconfiguration, or someone who didn't really understand what they were doing. The threat model in most boards' heads assumes a sophisticated adversary. The thing that's actually arriving is an unsophervised adversary holding tools that are now sophisticated for them."

This post extends his earlier writing on Anthropic's red team finding [500+ critical vulnerabilities](https://martinalderson.com/posts/anthropic-found-500-zero-days/) in abandoned software — the coordination problem of "who fixes the zero-days AI finds?"

### Datacentre Sovereignty Skepticism (June 2026)

Martin published a UK-centric analysis arguing that **data centre sovereignty is significantly overvalued** in political discourse. Key arguments:

- **Latency is negligible for most AI use**: Round-trip from UK to US East Coast is ~80ms vs 1.6-3.6s first-token latency for frontier models. European data centres already ensure <20ms for voice/video applications. Northern Scottish data centres would have *worse* latency for densely populated southern England than Paris or Amsterdam.
- **Tax revenue is a rounding error**: A 1GW data centre generates ~GBP 100M/yr in business rates — only 0.2% of UK government spending even if *all* 30GW of global data centre construction were moved to the UK. Jobs are equally minimal (~few dozen per 100MW site).
- **Actual control requires contracts, not geography**: Physical location of a data centre does not guarantee preferential compute access — hyperscalers serve global demand from any facility. Contractual compute lock-in is the real leverage, regardless of geography.
- **Seizure scenarios do not survive contact**: AI models decay rapidly in value (a seized 2025-era data centre would be outclassed by 2026 laptop models). Remote wiping by frontier labs would precede any physical seizure. The supporting operational infrastructure is not collocated with the models.

Martin's conclusion: the UK should focus on attracting frontier lab offices and talent rather than obsessing over physical data centre placement. The international AI infrastructure market already provides adequate latency, resilience, and access for nearly all use cases.

## Key Quotes

> *"Instead of SaaS being replaced by 'agentically-built' SaaS, what if people just don't need (as much) SaaS?"*

> *"I don't think there's ever been a time in history where a tiny team can outcompete a company one thousand times its size so easily."*

> *"The bifurcation is real and seems to be, if anything, speeding up dramatically."*

> *"While the world's been watching physical supply chains, a different kind of supply chain attack has been escalating in the open source ecosystem."*

## Related

- [[concepts/ai-economics]] — Martin's analysis of AI cost structures and compute constraints
-  — The "$285 billion markdown files" thesis
-  — Two kinds of AI users
-  — Open source vulnerability cascades- [[entities/anthropic]] — Claude Code, Cowork, and the knowledge-work-plugin

## Sources

- [Wall Street just lost $285 billion because of 13 markdown files](https://martinalderson.com/posts/wall-street-lost-285-billion-because-of-13-markdown-files/) (Feb 2026)
- [Two kinds of AI users are emerging. The gap between them is astonishing.](https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/) (Feb 2026)
- [Telnyx, LiteLLM and Axios: the supply chain crisis](https://martinalderson.com/posts/telnyx-litellm-axios-supply-chain-crisis/) (Mar 2026)
- [The Coming AI Compute Crunch](https://martinalderson.com/posts/the-coming-ai-compute-crunch/) (Jan 2026)
- [No, it doesn't cost Anthropic $5k per Claude Code user](https://martinalderson.com/posts/anthropic-5k-per-user/) (Mar 2026)
- [Which web frameworks are most token-efficient for AI agents?](https://martinalderson.com/posts/web-frameworks-token-efficiency/) (Feb 2026)
- [martinalderson.com/archive/](https://martinalderson.com/archive/)

### Podcast: Built for Turbulence (Jun 2026)

Martin appeared on Radical's **"Built for Turbulence"** podcast discussing AI agents' impact on software economics. Topics: 5 people with agents vs 500-person company, the **"Figma Trap"** (paying competitors through own customer usage), why AI-unaudited human-written code is becoming reckless, open weights closing up, and whether small-team-with-agents advantage is temporary. Source: [[raw/articles/martinalderson.com--posts-built-for-turbulence-podcast--40b40da5.md]]

## Machine Learning Research

### Expert-Aware Quantization for MoE Models (Jun 2026)

Martin explored selective per-expert quantization for Mixture-of-Experts models, demonstrating that profiling which experts are 'hot' (heavily used) vs 'cold' (rarely used) for specific tasks enables near-Q4 quality at near-Q2 size. Using Qwen3.6 35B-A3B profiled on C++ code generation:

| Method | Size | Perplexity (reading) | Perplexity (writing) |
|--------|------|---------------------|---------------------|
| Q8 (baseline) | 35GB | 1.568 | — |
| Uniform Q4 | 20GB | 1.582 | 1.449 |
| Q8-hot/Q2-cold (profiled) | 18GB | 1.620 | 1.456 |
| Q4-hot/Q2-cold (profiled) | 14GB | 1.635 | 1.477 |
| Uniform Q2 | 13GB | 2.103 | 1.977 |

Key findings:
- C++ code generation shows heavy expert concentration: per-layer Gini coefficient of 0.61, with top 32/256 experts handling ~50% of routing
- Profiled expert selection beats random selection across all metrics
- Q4-hot/Q2-cold (14GB) recovers ~90% of the quality gap between uniform Q2 and Q4 for just 1GB more
- The approach is not production-ready but could enable domain-specific model variants (one per task domain)
- The llama.cpp modification was implemented autonomously by Claude Code running for ~90 minutes

**Prior art reviewed**: DynaExq (dynamic runtime precision control from router traces), Mixture-Compressor (activation-frequency per-expert bit allocation), MoPEQ (sensitivity-based per-expert bits without activation frequency), foundational quantization methods (AWQ, GPTQ, SmoothQuant, SpQR), llama.cpp imatrix/k-quants, Apple's mixed 2/4-bit on-device scheme.

Source: [[raw/articles/martinalderson.com--posts-expert-aware-quantisation--532b8e2a.md]]

## References

- martinalderson.com--posts-ai-agents-are-starting-to-eat-saas--37d8652e
- martinalderson.com--posts-anthropic-found-500-zero-days--e16d62a3
- martinalderson.com--posts-are-we-dismissing-ai-spend-before-the-6x-lands--0aadfca9
- martinalderson.com--posts-are-we-in-a-gpt4-style-leap-that-evals-cant-see--7696618b
- martinalderson.com--posts-are-we-really-repeating-the-telecoms-crash-with-ai-dat--e40dbebb
- martinalderson.com--posts-attack-of-the-clones--1a69c778
- martinalderson.com--posts-building-a-tax-agent-with-claude-code--72e6cc36
- martinalderson.com--posts-claude-code-static-analysis--2a4b4efb
- martinalderson.com--posts-excel-agents-could-unlock-1t-in-economic-value--2fb910d0
- martinalderson.com--posts-figmas-woes-compound-with-claude-design--f8915a52
- martinalderson.com--posts-google-ai-studio-api-unreliable-for-two-weeks--8a7a82ba
- martinalderson.com--posts-has-mythos-just-broken-the-deal-that-kept-the-internet--290ac35f
- martinalderson.com--posts-has-the-cost-of-software-just-dropped-90-percent--d6e9e325
- martinalderson.com--posts-how-i-make-cicd-much-faster-and-cheaper--006d75ad
- martinalderson.com--posts-how-i-use-claude-code-to-manage-sysadmin-tasks--82cdaf85
- martinalderson.com--posts-how-to-make-great-looking-consistent-reports-with-clau--3d6f1578
- martinalderson.com--posts-how-to-use-qwen-3-5-to-ocr-documents--f3719003
- martinalderson.com--posts-i-finally-found-a-use-for-ipv6--d17a28d3
- martinalderson.com--posts-is-the-ai-compute-crunch-here--3df57c24
- martinalderson.com--posts-mcp-support-across-ai-apis--c5e1cf4b
- martinalderson.com--posts-minification-isnt-obfuscation-claude-code-proves-it--89931401
- martinalderson.com--posts-moe-expert-routing-visualization--a70dde30
- martinalderson.com--posts-no-it-doesnt-cost-anthropic-5k-per-claude-code-user--77319d6f
- martinalderson.com--posts-non-technical-cfo-shipping-better-code-than-agencies--35095076
- martinalderson.com--posts-notes-from-mcp-europe--22c3c8bd
- martinalderson.com--posts-ported-photoshop-1-to-csharp-in-30-minutes--e5438a32
- martinalderson.com--posts-self-improving-claude-md-files--ac9dfa7e
- martinalderson.com--posts-telnyx-litellm-axios-supply-chain-crisis--1cf34d19
- martinalderson.com--posts-the-coming-ai-compute-crunch--de305311
- martinalderson.com--posts-tracking-mcp-server-growth--d7da3712
- martinalderson.com--posts-travel-agents-developers--03e9ba7f
- martinalderson.com--posts-turns-out-i-was-wrong-about-tdd--df116d72
- martinalderson.com--posts-two-kinds-of-ai-users-are-emerging--409d6535
- martinalderson.com--posts-using-agents-and-wine-to-move-off-windows--85a78b28
- martinalderson.com--posts-using-opencode-in-cicd-for-ai-pull-request-reviews--1b4f7bf3
- martinalderson.com--posts-wall-street-lost-285-billion-because-of-13-markdown-fi--69ec5d77
- martinalderson.com--posts-welcome--6aca66b2
- martinalderson.com--posts-what-happens-when-coding-agents-stop-feeling-like-dial--d2aad4ef
- martinalderson.com--posts-what-next-for-the-compute-crunch--d8f87332
- martinalderson.com--posts-which-programming-languages-are-most-token-efficient--9c9c84db
- martinalderson.com--posts-which-web-frameworks-are-most-token-efficient-for-ai-a--a83d9cfe
- martinalderson.com--posts-why-claudes-new-1m-context-length-is-a-big-deal--294e4983
- martinalderson.com--posts-why-im-building-my-own-clis-for-agents--08080178
- martinalderson.com--posts-why-on-device-agentic-ai-cant-keep-up--5a080ee7
- martinalderson.com--posts-why-sandboxing-coding-agents-is-harder-than-you-think--4d65588c
