---
title: "Sakana AI"
created: 2026-05-28
updated: 2026-05-28
type: entity
tags:
  - company
  - lab
  - sakana-ai
  - japan
  - tokyo
  - evolutionary-algorithms
  - model-merging
  - open-source
  - nature-inspired
  - collective-intelligence
  - foundation-models
  - model
  - vlm
sources:
  - https://sakana.ai/
  - https://sacra.com/c/sakana-ai/
  - https://www.cnbc.com/2023/08/17/transformer-co-author-llion-jones-leaves-google-for-startup-sakana-ai.html
  - https://www.japantimes.co.jp/business/2025/11/17/companies/sakana-ai-valuation/
  - https://www.asahi.com/ajw/articles/15434714
  - https://github.com/SakanaAI
  - wiki/raw/papers/2025-06-17_2506.14202_diffusionblocks-block-wise-training.md
aliases:
  - Sakana AI
  - SakanaAI
---

# Sakana AI

> **Nature-inspired AI research lab based in Tokyo.** Founded July 2023 by David Ha, Llion Jones, and Ren Ito. Japan's most valuable AI unicorn (~$2.65B, Nov 2025). Pioneering evolutionary model merging, automated scientific discovery, and collective intelligence approaches that break from the brute-force scaling paradigm.

## Quick Facts

| Field | Detail |
|---|---|
| **Founded** | July 2023, Tokyo, Japan |
| **CEO & Co-Founder** | David Ha (ex-Google Brain Tokyo lead, ex-Stability AI Head of Research) |
| **CTO & Co-Founder** | Llion Jones (co-author of "Attention Is All You Need," 12 years at Google) |
| **COO & Co-Founder** | Ren Ito (ex-Japanese Foreign Ministry, ex-Mercari, ex-Stability AI COO) |
| **Employees** | ~131 (2025), research-heavy: 45 in research, 36 technical |
| **Headquarters** | Toranomon Hills Business Tower, Minato-ku, Tokyo (3 offices total) |
| **Valuation** | ~¥400B / $2.65B (Nov 2025 Series B) — Japan's highest-valued startup |
| **Total Funding** | ~$379M across 10 rounds (as of Mar 2026) |
| **GitHub** | [@SakanaAI](https://github.com/SakanaAI) — 46 public repos, 3,000+ followers |
| **Website** | [sakana.ai](https://sakana.ai/) |
| **Twitter/X** | [@SakanaAILabs](https://twitter.com/SakanaAILabs) |

## Name & Philosophy

The name "sakana" means "fish" in Japanese — chosen to evoke schools of fish forming coherent, intelligent entities from simple local rules. This metaphor captures Sakana AI's founding thesis: that intelligence can emerge from simpler components interacting collectively, rather than from scaling a single monolithic system.

Sakana AI explicitly positions itself against the **brute-force scaling paradigm** that dominates Western (OpenAI, Anthropic) and Chinese AI labs. Instead, it pursues:

- **Nature-inspired intelligence**: Evolutionary algorithms, collective behavior, and emergence as core design principles
- **Model merging over training from scratch**: Combining existing open-source models via evolutionary optimization to create new capabilities without massive GPU clusters
- **Architectural sovereignty**: Building an AI ecosystem outside US/China influence, with Japanese enterprise and government partnerships
- **Ingenuity over data scale**: Competing on algorithmic creativity rather than parameter count or dataset size

> *"We can compete based on people's ingenuity rather than the amount of data we put in."* — Takuya Akiba, Staff Research Scientist

## Funding History

| Round | Date | Amount | Key Investors | Valuation |
|---|---|---|---|---|
| **Seed** | Jan 2024 | $30M | Lux Capital (lead), Khosla Ventures | — |
| **Series A** | Sep 2024 | $214M | Miyako Capital, NEA, NTT, KDDI, Mitsubishi, NEC, Fujitsu, ITOCHU, SBI | — |
| **Series B** | Nov 2025 | ¥20B (~$135M) | MUFG (lead), Khosla, NEA, Lux Capital, In-Q-Tel, Nvidia, Geodesic, Macquarie, Factorial, Ora Global, MPower, Shikoku Electric | ~$2.65B |
| **Post-B rounds** | Feb–Mar 2026 | Undisclosed | Citi, Salesforce Ventures, Mitsubishi Electric (Corporate Minority) | — |

### Notable Investor Profile
- **MUFG, Nomura, SMBC**: Japan's megabanks, signaling enterprise AI demand in financial services
- **NTT, KDDI**: Telecom giants partnering on Japanese-optimized LLMs
- **Nvidia**: Hardware partner; strategic alignment with efficient training methods
- **In-Q-Tel (IQT)**: CIA-linked venture arm, signaling defense/intelligence applications
- **NEC, Fujitsu, ITOCHU**: Distribution into manufacturing, supply chain, and enterprise IT

## Key Research & Projects

### 1. Evolutionary Model Merging (~1.4K GitHub stars)
Sakana AI's flagship technique. Uses evolutionary algorithms to automatically discover optimal combinations of diverse open-source models, operating in both parameter space and data flow space. Published in **Nature Machine Intelligence** (Jan 2025).

- **EvoLLM-JP**: 7B-parameter Japanese Math LLM that surpassed 70B-parameter models
- **EvoVLM-JP**: Culturally-aware Japanese Vision-Language Model
- **EvoSDXL-JP**: Japanese image generation via merged diffusion models
- **CycleQD** (ICLR 2025) and **Natural Niches**: Follow-up work extending the paradigm
- Integrated into `mergekit` and Optuna Hub

### 2. AI Scientist (~13K+ GitHub stars)
The first comprehensive system for fully automatic scientific discovery. LLMs perform end-to-end research: idea generation, experiment execution, paper writing, and peer review. Published Aug 2024.

### 3. AI Scientist v2 (~5.5K+ GitHub stars)
Substantially improved successor. Removes reliance on human-coded templates, generalizes across ML domains, and introduces **agentic tree search** managed by an experiment manager agent. Generated the first entirely AI-written workshop paper accepted through peer review (ICLR 2025 workshop). Integrates VLM feedback loops.

### 4. DiffusionBlocks (ICLR 2026)
Block-wise neural network training via diffusion interpretation. Co-authored by [[entities/takuya-akiba]], Makoto Shing, and Masanori Koyama. Reinterprets residual connections as Euler discretization of a diffusion process, enabling genuinely independent block training with memory reduction proportional to the number of blocks. See [[concepts/diffusionblocks]].

### 5. Continuous Thought Machines (~1.8K stars)
Explores reasoning as a continuous process rather than discrete chain-of-thought steps, treating neural computation as flowing through time.

### 6. Self-Adaptive LLMs (~1.2K stars)
LLMs that adapt to unseen tasks in real-time without fine-tuning, using test-time learning strategies.

### 7. Text-to-LoRA (~1.2K stars)
Hypernetworks that generate LoRA adapters from text descriptions, enabling benchmark-specific model adaptation on demand.

### 8. Japanese-Optimized LLMs
Enterprise partnerships with NTT, KDDI, and Japan's megabanks to build Japanese language and culturally-aware foundation models for domestic deployment.

### 9. ShinkaEvolve
Generalized evolutionary code-search engine for discovering algorithms and agent architectures. Couples novelty-weighted sampling with AI-ensemble mutation for optimization across domains.

### 10. AB-MCTS
Monte Carlo Tree Search-based inference orchestration that routes between different AI providers at inference time, selecting the best model for each sub-problem.

### 11. RSI Lab Tokyo (June 2026)
Sakana AI launched a dedicated **Recursive Self-Improvement (RSI) Lab** in Tokyo, formalizing their research into self-improving AI systems. The lab ties together prior projects — [[concepts/ai-scientist]] (fully automatic scientific discovery), the Darwin Gödel Machine, and ShinkaEvolve (evolutionary code-search engine) — under an explicit claim that self-improving systems can be built under compute constraints by prioritizing **sample efficiency** over raw scale. This positions Sakana AI as the first major lab with an org-level RSI commitment, in contrast to Western labs' more cautious RSI timelines.

## Competitive Position

### Differentiation
Sakana AI competes on **efficiency and specialization**, not raw parameter count. Evolutionary model merging can produce competitive models in days/weeks at a fraction of traditional training costs — models run on consumer-grade hardware, targeting Japan's 3.5M small businesses.

### In Japan
- **Rakuten**: AI 2.0 models for e-commerce/fintech
- **CyberAgent**: CALM3-22B for ad-tech
- **SoftBank (Sarashina)**: 390B-parameter model with ¥421B government subsidies
- **Preferred Networks**: PLaMo for on-premises enterprise deployment

### Globally
Positioned as a **third-pole AI player** alongside US (OpenAI, Anthropic) and Chinese (DeepSeek, Alibaba) labs. Sakana AI's architectural sovereignty thesis resonates with Japanese government priorities (GENIAC supercomputing grant, Ministry of Defense contracts).

## Business Model

- **Type**: B2B AI research lab monetizing through enterprise licensing and strategic partnerships
- **MUFG deal**: Flagship multi-year partnership for banking automation — establishes credibility for regional banks, insurers, and securities firms
- **Revenue**: Hybrid model combining software licensing (custom AI solutions) + implementation and support services
- **Cost advantage**: Evolutionary merging avoids massive GPU training clusters; models producible at a fraction of traditional cost

## Research Team

Key researchers include:
- **David Ha** (CEO) — Generative AI, evolutionary computing, world models
- **Llion Jones** (CTO) — Transformer architecture, attention mechanisms, language models
- **[[entities/takuya-akiba]]** (Staff Research Scientist) — Optuna creator, distributed training, evolutionary model merging, DiffusionBlocks
- **Makoto Shing** — Evolutionary model merging, DiffusionBlocks
- **Yujin Tang** — Evolutionary model merging, reinforcement learning
- **Qi Sun** — Evolutionary model merging, computer vision

## Government & Defense

- **GENIAC grant**: Japanese government supercomputing time for AI research
- **Ministry of Defense**: Defense-adjacent research contracts
- **In-Q-Tel investment**: Signals US intelligence community interest in Sakana AI's approach
- Part of Japan's broader push for **technological sovereignty** in AI

## Related Pages

- [[entities/takuya-akiba]] — Staff Research Scientist, Optuna creator, evolutionary model merge co-author
- [[concepts/diffusionblocks]] — Block-wise training method (ICLR 2026)
- [[concepts/evolutionary-algorithms]] — Evolutionary algorithms in AI
- [[concepts/model-merging]] — Model merging techniques and approaches
- [[concepts/training-efficiency]] — Memory-efficient and compute-efficient training
- [[concepts/collective-intelligence]] — Collective and swarm intelligence in AI systems
- [[concepts/nature-inspired-ai]] — Nature-inspired approaches to AI

## External Links

- Official website: https://sakana.ai/
- GitHub: https://github.com/SakanaAI
- Twitter/X: https://twitter.com/SakanaAILabs
- AI Scientist: https://github.com/SakanaAI/AI-Scientist
- AI Scientist v2: https://github.com/SakanaAI/AI-Scientist-v2
- Evolutionary Model Merge: https://github.com/SakanaAI/evolutionary-model-merge
- DiffusionBlocks: https://github.com/SakanaAI/DiffusionBlocks
- Blog: https://sakana.ai/blog/
- Careers: https://sakana.ai/careers/
