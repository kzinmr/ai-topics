---
title: "Nathan Lambert"
tags: [person]
created: 2026-04-24
updated: 2026-04-15
type: entity
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
- **Local Agents as "Dark Matter"**: "Local agents, OpenClaw, and other personal agents represent a large, to date, mostly ignored market for open model usage. It is a sort of dark matter, with pervasive, massive potential for influence on the balance of open-to-closed models"
- **Regulatory Reality**: Bans on frontier models are unenforceable; another sovereign will always train and release them
- **Funding Evolution**: New funding structures will emerge as enterprises and sovereigns recognize that dependencies on single, for-profit companies for AI access are unreliable

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
- [[concepts/rlhf]] — Core research area, book author
- [[concepts/fine-tuning/rlhf-dpo-preference]] — Direct Preference Optimization, Zephyr
- [[concepts/post-training]] — His primary research focus
- [[teknium]] — Fellow post-training researcher, Nous Research co-founder
-  — Co-created reward model evaluation benchmark-  — Advocate for fully open AI development- [[concepts/fine-tuning/grpo-rl-training]] — Discussed extensively as part of the RLVR trend
- [[simon-willison]] — Fellow open-source AI advocate
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
