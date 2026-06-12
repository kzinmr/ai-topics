---
title: "Nathan Lambert"
tags: [person]
created: 2026-04-24
updated: 2026-06-03
type: entity
aliases:
  - natolambert
  - nathan-lambert
sources:
  - https://www.interconnects.ai/p/the-distillation-panic
  - https://www.natolambert.com/
  - https://www.interconnects.ai/
  - https://www.interconnects.ai/p/some-ideas-for-what-comes-next-may
  - raw/newsletters/2026-06-01-open-and-closed-models-are-on-different-exponentials.md
---


# Nathan Lambert (@natolambert)

## Overview

Nathan Lambert is a Senior Research Scientist and **Post-Training Lead** at the **Allen Institute for AI (AI2)**. He previously worked at **HuggingFace** as a Research Scientist and RLHF Team Lead (2022–2023). He earned his Ph.D. at UC Berkeley in model-based reinforcement learning. He is one of the most prominent open voices on **RLHF**, post-training techniques, and the open-source AI movement.

He writes the newsletter **Interconnects** (~32K+ subscribers), hosts **Interconnects Interviews** podcast, and is authoring **"The RLHF Book"** (published via Manning, also freely available online at rlhfbook.com with 1,764+ GitHub stars).

## Background

- **Ph.D.**, UC Berkeley (2017–2022) — Model-based reinforcement learning, robotics, microrobotics
- **Internship**, Tesla — Battery engineering
- **Research Scientist Intern**, DeepMind (2021)
- **Student Researcher**, Facebook/Meta (2019–2020)
- **Research Scientist & RLHF Team Lead**, HuggingFace (May 2022 – Oct 2023)
- **Senior Research Scientist**, Allen Institute for AI (Oct 2023 – Present)
- **Founder**, Interconnects AI (Jan 2022 – Present)

His unconventional path — starting his Ph.D. in MEMS/physics, being rejected by top RL groups (Levine, Abbeel), finishing with no NeurIPS/ICML/IRCL papers, and then landing at HuggingFace — is one he shares openly to demystify AI research careers.

## Key Contributions

### OLMo & OLMo 3
- Core contributor to the **OLMo** (Open Language Model) family — Ai2's fully open LLM project releasing model weights, training data, and code
- **OLMo 3** (Dec 2025): Post-training lead for the 7B and 32B model family, including the first fully open 32B reasoning model (OLMo 3 Think 32B)
- Pioneered the "Model Flow" concept — releasing every stage, checkpoint, and data artifact to enable reproducibility

### Tülu 3
- Lead author on **Tülu 3** (Nov 2024) — a family of fully open state-of-the-art post-trained models (8B, 70B, 405B)
- Introduced **RLVR** (Reinforcement Learning with Verifiable Rewards) — training on math problems with verifiable outcomes instead of reward models
- Beat Llama 3.1 Instruct at 8B and 70B on focused tasks

### RewardBench
- Co-created **RewardBench** — the first comprehensive benchmark for evaluating reward models
- Evaluated RMs trained with PPO, DPO, and other methods across chat, reasoning, and safety tasks

### Zephyr (HuggingFace)
- Key contributor to **Zephyr-β** — a small, powerful chat model trained with Direct Preference Optimization (DPO)
- Demonstrated that effective alignment can be achieved without massive compute budgets

### The RLHF Book
- Open-source textbook at [rlhfbook.com](https://rlhfbook.com) (1,764+ GitHub stars)
- Covers RLHF from fundamentals through advanced topics: Constitutional AI, synthetic data, over-optimization, character training
- Also available as a Manning MEAP (print publication estimated Summer 2026)

### ATOM Project (American Truly Open Models)
- Launched in 2025 as a community movement to reinvigorate U.S. investment in open AI models
- Argues that America is losing open-model leadership to China (which has 5+ labs producing leading open models)
- Recommends at least one U.S. lab focused on training open models with 10,000+ leading-edge GPUs

## Interconnects Newsletter & Media

- **Newsletter**: Weekly analysis of AI trends, model releases, and research papers (~32K+ subscribers)
- **Podcast**: "Interconnects Interviews" featuring conversations with leading AI researchers
- **Top podcast appearances**: Lex Fridman (2x), Latent Space (2x), ChinaTalk (5x), The MAD Podcast, Lawfare's "Scaling Laws", AI Summer
- **2025 highlights**: Covered DeepSeek V3/V4, OLMo 3 launch, RLVR revolution, sycophancy in LLMs
- **2026 highlights**: ATOM Report release, RAM metric development, Gemma 4 analysis, RLHF Book publication

### May 2026: The Distillation Panic

**"The Distillation Panic" (May 4, 2026)**: Published a major policy intervention arguing that the term "distillation attacks" is a dangerous misnomer. Key arguments:
- The real problematic behavior is **API abuse** (jailbreaking, identity spoofing, extracting reasoning traces), not distillation itself
- Anti-distillation rhetoric risks criminalizing a fundamental technique used by Anthropic, OpenAI, xAI, Nvidia, and Ai2
- Proposed alternative terminology: call it "API abuse," "jailbreaking," or "hacking" instead of "distillation attacks"
- Warned of regulatory overreach: H.B. 8283, NSTM-4 Executive Order, and Congressional probes could create a de facto ban on open-weight models
- Cited Kevin Xu's "crutch" theory — Chinese reliance on distillation may prevent original research development
- **Created concept**: [[concepts/ai-api-abuse]] — distinguishing illegitimate API access from legitimate model distillation

See [[raw/articles/2026-05-04_interconnects_distillation-panic]] and [[concepts/model-distillation]].

### April 2026 Developments

**ATOM Report & RAM Metric**: Released "The ATOM Report" with updated Relative Adoption Metric (RAM) showing:
- GPT-OSS's exceptional per-model performance despite only 2 releases
- Chinese models dominating top 10 LMArena positions
- Meta's Llama derivative share dropping from 50% to 15%
- RAM Score methodology: time+size normalized adoption trajectory prediction

**Gemma 4 Analysis**: Published insights on open model success factors, noting:
- 2026 open model landscape is crowded (Qwen 3.5, Kimi K2.5, GLM 5, MiniMax M2.5, GPT-OSS, Arcee Large, Nemotron 3, OLMo 3)
- Open models feel like "dark matter" — huge potential but few clear recipes
- Agentic AI and OpenClaw will spur mass experimentation with open models
- Key success factors: licensing simplicity, ecosystem support, release cadence

**RLHF Book Completed**: The RLHF Book is done and ready for pre-order via Manning (also available free at rlhfbook.com with 1,764+ GitHub stars).

**Post-Training Course**: Announced development of a comprehensive post-training course covering SFT, DPO, RLVR, and synthetic data pipelines.

**"My bets on open models, mid-2026" Newsletter (Apr 15, 2026)**: Comprehensive analysis covering:
- **Capability Gap Persists**: Open models will not fully catch up to closed models; the gap is sustained by compute advantages, research depth, and real-world usage data
- **Chinese Open-Weight Labs**: Heavily benchmark-focused, effective distillation users, but expected to face funding constraints by late 2026
- **RL & Real-World Data Advantage**: Shift to RL-dominated training makes user interaction data critical; closed labs can leverage online RL from direct user feedback (e.g., Claude Code, Codex) to accelerate beyond open models
- **Open Model Market Fit**: Will dominate repetitive automation tasks (API market share), driving investment into domain-specific efficient open models
- **U.S. Adoption Shift**: U.S. will regain open-model adoption leadership starting early 2027; key catalysts: Google Gemma 4, Nvidia Nemotron, Arcee AI
|- **Local Agents as "Dark Matter"**: "Local agents, OpenClaw, and other personal agents represent a large, to date, mostly ignored market for open model usage. It is a sort of dark matter, with pervasive, massive potential for influence on the balance of open-to-closed models"
|- **Regulatory Reality**: Bans on frontier models are unenforceable; another sovereign will always train and release them
|- **Funding Evolution**: New funding structures will emerge as enterprises and sovereigns recognize that dependencies on single, for-profit companies for AI access are unreliable

### Interconnects Podcast — Arcee AI Interview (May 2026)

Lambert hosted **Mark McQuade** (CEO) and **Lucas Atkins** (CTO) of [[entities/arcee-ai|Arcee AI]] on the Interconnects Interviews podcast. The conversation covered:
- Arcee's pivot from post-training services to **pretraining from scratch** with Trinity Large (400B/13B MoE)
- The **Muon optimizer** — Adam alternative that achieved better results with less compute on Trinity Large
- **DeepSeek-style auxiliary-loss-free load balancing** for MoE routing
- Training on **22,048 NVIDIA B300 GPUs** via TorchTitan — the largest known non-hyperscaler training cluster
- The **$20M training cost** and business model of selling post-trained open models to enterprises
- Lambert's assessment that Arcee is "taking the most real approach to monetizing open models"


### June 2026: Open and closed models are on different exponentials

**"Open and closed models are on different exponentials" (Jun 1, 2026)**: Published a provocative economic analysis arguing that open and closed models follow fundamentally different growth curves:

- **Coding agents create premium market**: Past the Opus 4.5 and Codex 5.2 thresholds, coding agents created the first large market willing to pay dramatically more for top intelligence. Users who rely on coding agents will always pay more for the best (Lambert: "I would pay $2000/month for the tools today")
- **Closed labs as Apple+Microsoft hybrid**: Frontier labs will look like a mix of Apple (integrated, hard-to-replicate technology) and Microsoft (high-leverage subscriptions). Expects Anthropic and OpenAI to reach $2-10T valuations in 5-10 years, forming an oligopoly like today's cloud market
- **Open model economics on a different curve**: Open models optimize for cost efficiency, accessibility, and democratization — a fundamentally different exponential from the premium-intelligence curve
- **Integration benefits favor closed labs**: The integration of model weights, harnesses, tools, and serving infrastructure has massive returns that open models (designed for diverse serving situations) cannot capture
- **No walls in progress**: Every direction of model improvement (speed, intelligence, specialization) remains open; there have been no walls in progress
- **Short-term vs long-term**: Near-term markets will be dictated by compute buildout and token subsidization; the true economic divergence between open and closed is a 5-10 year timeline

Added source: `raw/newsletters/2026-06-01-open-and-closed-models-are-on-different-exponentials.md`

### May 2026: Some ideas for what comes next

Published a comprehensive AI landscape analysis covering the state of the industry in May 2026. Key arguments:

- **Open models lack an "agent moment"**: Unlike Claude Code + Opus 4.5 driving Anthropic's surge, open models have no equivalent killer application — 5-6 months behind and counting
- **Gemini gap**: Google's Gemini lacks competitors for Claude Code and Codex in the coding agent space, leaving a two-horse race between Anthropic and OpenAI
- **No open-weights Mythos this year**: Despite progress, a truly frontier open model comparable to Anthropic's Mythos is unlikely in 2026
- **American open models gaining momentum**: Nvidia Nemotron and Google Gemma 4 under Apache 2.0 are outperforming Qwen in key benchmarks, shifting the open-model center of gravity
- **Anthropic vs OpenAI intensifies**: Both companies are just hitting their stride; competition is accelerating rather than consolidating
- **Power structures asserting control**: Existing institutions (governments, large corporations) are increasingly shaping AI development through regulation, compute allocation, and partnership strategies

### Departure from Ai2 (June 2026)

Nathan Lambert **departed the Allen Institute for AI (Ai2)** in June 2026, marking a significant transition in his career. Key details:

- His **last day** was in June 2026
- He joined Ai2 as "an accident" — meeting Luca at **ICML 2023** led to his role
- Proudest achievement: the **OLMo work** — leading post-training for the fully open LLM family
- Will **continue in this space**, focusing on making the open ecosystem better coordinated
- Reflects on the various paths to AI impact **beyond frontier performance**
- His departure marks the end of a ~3-year tenure at Ai2 (Oct 2023 – June 2026)

## Core Ideas

### Post-Training Is the New Bottleneck
> "Pretraining scaling as we know it is ending. Post-training is where the action is."

Lambert argues that the frontier of AI capability has shifted from pretraining scale to post-training quality. Mastering SFT, DPO, RLVR, and synthetic data pipelines is now the primary differentiator between models.

### Open Models Are Essential for Research
The OLMo project embodies his belief that truly open models — with full transparency into data, code, architecture, and training — are necessary for scientific progress. Closed models prevent reproducibility and independent verification.

### RLHF Is Underexplored and Misunderstood
Most people think RLHF is "solved." Lambert argues it's barely scratched the surface. His book and newsletter consistently push the narrative that RLHF, DPO, and related techniques are still evolving rapidly, especially with the shift to AI-generated feedback and verifiable rewards.

### AI Feedback Is Democratizing Post-Training
With GPT-4-tier models available as evaluators, the cost of preference data has dropped from ~$5–20/sample (human) to <$0.01/sample (AI). This makes high-quality post-training accessible to smaller labs.

### The "American DeepSeek" Problem
China is producing leading open models (Qwen, DeepSeek, Kimi) while the U.S. is closing off its best models. Lambert's ATOM Project is a call to action to maintain U.S. leadership in open AI research.

## Writing Style

Lambert writes with a distinctive mix of technical rigor and personal candor. He shares his career struggles openly (no top-tier papers during Ph.D., rejected by major labs) and uses his newsletter as both a research outlet and a personal journal. His posts often combine:
- Deep technical analysis of model releases
- Interviews with researchers at frontier labs
- Personal reflections on AI's trajectory
- Policy commentary on open vs. closed AI

## Related

- [[concepts/allen-institute-ai]] — Current employer, OLMo project
-  — Previous employer, Zephyr and TRL work
- [[concepts/post-training/rlhf]] — Core research area, book author
- [[concepts/post-training/rlhf-dpo-preference]] — Direct Preference Optimization, Zephyr
- [[concepts/post-training]] — His primary research focus
- [[entities/teknium]] — Fellow post-training researcher, Nous Research co-founder
-  — Co-created reward model evaluation benchmark-  — Advocate for fully open AI development- [[concepts/model-distillation]] — Fundamental ML technique; Lambert's "Distillation Panic" defends it from criminalization
- [[concepts/ai-api-abuse]] — Term Lambert coined to replace the misleading "distillation attacks" framing
- [[events/distillation-attacks-2026]] — Anthropic's accusations that prompted Lambert's response
-  — His newsletter and podcast-  — Open post-training model family he leads
## Key Links

- **Website**: [natolambert.com](https://www.natolambert.com/)
- **Newsletter**: [interconnects.ai](https://www.interconnects.ai/)
- **RLHF Book**: [rlhfbook.com](https://rlhfbook.com/)
- **GitHub**: [github.com/natolambert](https://github.com/natolambert)
- **LinkedIn**: [linkedin.com/in/natolambert](https://linkedin.com/in/natolambert)
- **X/Twitter**: [@natolambert](https://x.com/natolambert)
- **Google Scholar**: Available on his website

## References

- 2026-04-12-nathan-lambert-open-model-consortium
