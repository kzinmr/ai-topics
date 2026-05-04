---
title: "Lilian Weng (@lilianweng)"
tags: [type:, entity]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Lilian Weng (@lilianweng)

**URL:** https://lilianweng.github.io
**Blog:** Lil'Log (lilianweng.github.io/posts)
**Twitter/X:** @lilianweng
**LinkedIn:** linkedin.com/in/lilianweng
**GitHub:** lilianweng
**Projects:** Lil'Log blog, OpenAI robotics (Rubik's Cube solver), Pydantic validation

## Overview

Lilian Weng is one of the most influential voices in AI research communication and a leading figure in AI safety and autonomous agent systems. She co-founded [Thinking Machines Lab](https://thinkingmachines.ai) in January 2025 alongside Mira Murati (CEO), John Schulman (Chief Scientist), and Barret Zoph (CTO) — a $12B-valued startup formed after a wave of high-profile departures from OpenAI.

Weng spent seven years at OpenAI (2017–2024), where she progressed from Research Scientist on the robotics team to VP of Research and Safety. She led the Applied AI Research team, founded and headed the Safety Systems team (80+ scientists), and contributed to foundational work on GPT-4 safety, content moderation systems, and the celebrated robotic hand that solved a Rubik's Cube. Her career at OpenAI coincided with the company's transformation from a ~60-person non-profit driven by pure research to a global frontier AI lab.

Outside of her professional roles, Weng has authored the blog *Lil'Log* since 2017, publishing deeply technical survey articles on topics ranging from Transformers and diffusion models to LLM agents, prompt engineering, reward hacking, and test-time compute. Her June 2023 post "LLM Powered Autonomous Agents" became one of the most widely shared and cited technical blog posts of the AI boom, with 27,000+ LinkedIn reactions. The blog has become essential reading for practitioners across the ML community.

Her intellectual identity is shaped by two core traits she has named herself: **persistence** and **humility** — the latter stemming from childhood mathematics competitions where she learned that raw talent disparities require加倍 effort, and the former driving her to tackle problems many considered impossible (like training a robot hand to solve a Rubik's Cube purely in simulation).

## Timeline

| Date | Event |
|------|-------|
| 2006–2010 | Studied engineering in China; developed interest in mathematics and deep learning |
| 2012–2013 | Data Science internships at Facebook |
| 2013 | Earned PhD in Computer Science from Indiana University Bloomington, focusing on network science and computational systems |
| 2014–2015 | Data Scientist at Dropbox |
| 2015–2016 | Software Engineer at Dropbox |
| 2016–2018 | Staff Machine Learning Engineer at Affirm, Inc. |
| 2017 | Started *Lil'Log* blog to document learning notes on deep learning research papers |
| 2017 | Interviewed at OpenAI (then a ~60-person non-profit) in November |
| 2018 | Joined OpenAI as Research Scientist on the Robotics team |
| 2019 | Co-authored "Solving Rubik's Cube with a Robot Hand" — trained purely in simulation with domain randomization |
| 2021 | Transitioned to lead Applied AI Research team at OpenAI |
| 2022 | Published work on text/code embeddings by contrastive pre-training |
| 2023 | Founded OpenAI's Safety Systems team; launched "LLM Powered Autonomous Agents" blog post (June) |
| 2023 | Published "Prompt Engineering" (March) and "Adversarial Attacks on LLMs" (October) on Lil'Log |
| 2023–2024 | Led safety systems development for GPT-4 and subsequent models |
| 2024 | Featured in Business Insider's AI Power List for AI safety leadership |
| 2024 | Published "Thinking about High-Quality Human Data" (February), "Diffusion Models for Video Generation" (April), and "Extrinsic Hallucinations in LLMs" (July) |
| 2024 | Appointed VP of Research and Safety (August) |
| 2024 | Published "Reward Hacking in Reinforcement Learning" (November) |
| Nov 2024 | Announced departure from OpenAI after 7 years: "I feel ready to reset and explore something new" |
| Jan 2025 | Co-founded Thinking Machines Lab with Mira Murati, John Schulman, and Barret Zoph |
| 2025 | Thinking Machines Lab raised record $2B seed round at $12B valuation |
| May 2025 | Published "Why We Think" — comprehensive survey on test-time compute and chain-of-thought reasoning |

## Core Ideas

### Learning in Public as Research Methodology

Weng's approach to knowledge sharing is distinctive: she documents her own learning process in real-time on Lil'Log, transforming personal study notes into comprehensive survey articles. Each post is meticulously researched, heavily cited, and updated multiple times based on new developments. Her blog began in 2017 as a personal organizational tool for the papers she was reading, and grew organically into one of the most trusted resources in the ML community.

> "It all starts as a set of personal learning notes. I didn't enter the deep learning field super early and still considered myself a 'newbie.' I decided to blog to document and organize my learning notes."

This approach reflects her core belief that **explaining something clearly is the best way to understand it deeply**. Her posts often become the definitive reference documents for their topics — "The Transformer Family Version 2.0" (45 min read) and "LLM Powered Autonomous Agents" (31 min read) are routinely cited in academic papers, conference talks, and engineering documentation.

### AI Safety as a Systems Engineering Problem

Unlike researchers who approach AI safety purely theoretically, Weng has consistently framed safety as a practical systems engineering challenge. At OpenAI, she led the creation of Safety Systems teams that built concrete tools — content moderation classifiers, evaluation datasets for harmful content detection, and safety guardrails for deployed models. Her philosophy is that safety must be integrated into the product development lifecycle, not bolted on afterward.

Her work on GPT-4 content moderation demonstrated that LLMs themselves could be used as the evaluation layer for safety — a meta-approach where AI audits AI. The team designed a pipeline where policy experts and GPT worked in tandem: GPT could start labeling, policy experts could evaluate and disagree, and the model would learn from those disagreements.

### Human-AI Collaboration Over Full Autonomy

Weng has been a consistent voice advocating for AI systems designed to work *with* humans rather than replace them entirely. This philosophy carried through from her OpenAI work to Thinking Machines Lab's stated mission. At the Hysta 2025 conference, she emphasized:

> "Instead of focusing solely on making fully autonomous AI systems, we are building multimodal systems that work with people collaboratively."

This is a deliberate counterpoint to the prevailing narrative in AI development that pushes toward full autonomy. Weng's position is that the most valuable AI systems will be those that augment human expertise across the full spectrum of professional work — not just programming and mathematics, but creative fields, scientific discovery, and collaborative problem-solving.

### Test-Time Compute as a New Scaling Dimension

In her May 2025 post "Why We Think," Weng provided the most comprehensive survey available on test-time compute (also called "thinking time" or inference-time compute). She articulated the key insight that giving models more computation time during inference — through chain-of-thought reasoning, parallel sampling, and sequential revision — creates a **new axis of capability improvement** that is complementary to (and in some cases more efficient than) scaling model parameters.

The post connected deep theoretical frameworks (latent variable models, neural tangent kernels) with practical observations (o1/o3 models, rejection sampling patterns) and raised critical open questions: How should models adaptively allocate thinking time? What happens when thinking budget is constrained in production?

### The Value of Tackling "Impossible" Problems

Weng's experience on the OpenAI Rubik's Cube robot project shaped her approach to research ambition. The project aimed to train a single robotic hand — using deep reinforcement learning and domain randomization, entirely in simulation — to manipulate a physical Rubik's Cube. It was widely considered infeasible because the sim-to-real gap for dexterous manipulation was thought to be too large. The team succeeded.

This experience reinforced a research philosophy: **don't accept the conventional wisdom about what's possible**. When others say a problem is too hard, it may just require more creativity in the approach. This same philosophy applies to her views on AI safety — rather than accepting that alignment is intractable, she pushes for concrete engineering solutions.

### Humility and Persistence as Core Traits

Weng has described herself as a "normal person" who had to "give it her all" — a perspective shaped by early exposure to mathematics competitions where she confronted the reality that some people have innate talent advantages. Rather than discouraging her, this taught her that persistence and systematic effort can close most gaps.

This trait manifests in her work ethic: blog posts that take months of reading and synthesis, research projects that require years of iteration (the Rubik's Cube robot took two years), and a willingness to change direction when the learning curve flattens (her stated reason for leaving OpenAI).

## Key Quotes

> "After 7 years at OpenAI, I feel ready to reset and explore something new."
>
> — On departing OpenAI, November 2024

> "It all starts as a set of personal learning notes. I didn't enter the deep learning field super early and still considered myself a 'newbie.' Initially as I started digging into so many papers, I was amazed by the concept of not designing an algorithm to solve a problem, but training a model to learn the algorithm to solve a problem."
>
> — On why she started Lil'Log

> "I believe we are on the right track towards AGI, but scaling is not the only recipe. In my opinion the most urgent challenges right now are alignment and safety. To some extent, they may be the same issue about controllability or steerability."
>
> — On the biggest challenges in AI, December 2022

> "The exploration of test-time compute and chain-of-thought reasoning presents new opportunities for enhancing model capabilities. We are moving towards building future AI systems that mirror the best practices of how humans think, incorporating adaptability, flexibility, critical reflection, and error correction."
>
> — From "Why We Think," May 2025

> "Building agents with LLM (large language model) as its core controller is a cool concept. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver."
>
> — From "LLM Powered Autonomous Agents," June 2023

> "Everyone has something sparkling, inspiring, or respectful and I enjoy learning from them."
>
> — On her colleagues at OpenAI

## Recent Themes (2024–2026)

- **AI safety engineering**: Building concrete systems for content moderation, adversarial robustness, and alignment verification at OpenAI scale
- **Test-time compute and reasoning**: Comprehensive survey of chain-of-thought, o1/o3 models, and the new scaling dimension of "thinking time"
- **Reward hacking in RL**: Analysis of how RL agents exploit imperfect reward functions — increasingly relevant as RLHF becomes standard
- **LLM hallucination**: Distinguishing between fabrication and genuine error, and developing methods for grounding model outputs
- **High-quality human data**: Arguing that data collection and curation is the most undervalued work in ML ("everyone wants to do the model work, not the data work")
- **Autonomous agent architecture**: Framework for LLM-powered agents with planning, memory, and tool-use components
- **Human-AI collaboration**: At Thinking Machines Lab, building systems that augment rather than replace human expertise
- **Adversarial attacks on LLMs**: Taxonomy of jailbreak methods and defense strategies
- **Diffusion models for video**: Extending diffusion model research from image synthesis to temporal generation

## Related Concepts

- [[concepts/ai-safety-and-alignment]] — Her primary research focus at OpenAI
- [[concepts/agent-orchestration-frameworks]] — Frameworks she analyzed in "LLM Powered Autonomous Agents"
- [[concepts/test-time-compute]] — The "thinking time" paradigm she surveyed in "Why We Think"
- [[concepts/reward-hacking]] — Her November 2024 deep-dive topic
- [[concepts/chain-of-thought-reasoning]] — Central to her analysis of test-time compute
- [[concepts/rlhf]] — Reinforcement Learning from Human Feedback, the alignment method she worked on
-  — Her April 2024 analysis of video generation
-  — Her July 2024 survey on extrinsic hallucinations
- [[concepts/resilient-prompt-engineering]] — Her March 2023 definitive guide
- [[mira-murati]] — Thinking Machines Lab co-founder and CEO
- [[john-schulman]] — Thinking Machines Lab co-founder and Chief Scientist
- [[sam-altman]] — OpenAI CEO during her tenure
-  — The approach used for the Rubik's Cube robot
## Influence Metrics

- **Lil'Log blog**: Hundreds of thousands of readers; consistently cited in academic papers, conference talks, and engineering documentation
- **"LLM Powered Autonomous Agents"**: 27,000+ LinkedIn reactions; became the definitive survey article on the topic
- **"Why We Think"**: Comprehensive 40-minute read surveying test-time compute; translated and discussed across multiple languages
- **OpenAI Safety Systems team**: Grew to 80+ scientists, researchers, and policy experts under her leadership
- **Business Insider AI Power List 2024**: Recognized for leadership in AI safety
- **500+ publications on arxiv** (as co-author or contributor)
- **Thinking Machines Lab**: $2B seed round at $12B valuation — the largest seed round in startup history
- **GitHub repositories**: Stock-RNN (2K stars), multi-armed-bandit (417 stars), deep-reinforcement-learning-gym (310 stars), transformer-tensorflow (484 stars)
- **170,700+ Twitter/X followers**

## Sources

- https://lilianweng.github.io/ — Lil'Log blog homepage
- https://lilianweng.github.io/posts/ — Blog post listing
- https://lilianweng.github.io/posts/2023-06-23-agent/ — "LLM Powered Autonomous Agents"
- https://lilianweng.github.io/posts/2025-05-01-thinking/ — "Why We Think"
- https://openai.com/index/the-power-of-continuous-learning/ — OpenAI profile (Dec 2022)
- https://techcrunch.com/2024/11/08/openai-loses-another-lead-safety-researcher-lilian-weng/ — Departure announcement
- https://www.businessinsider.com/lilian-weng-openai-ai-power-list-2024 — Business Insider AI Power List 2024
- https://www.wired.com/story/thinking-machines-lab-mira-murati-funding/ — Thinking Machines Lab funding
- https://www.reuters.com/technology/artificial-intelligence/former-openai-technology-chief-mira-muratis-ai-startup-taps-top-researchers-2025-02-18 — Thinking Machines Lab launch
- https://github.com/lilianweng — GitHub profile

## Related Wiki Pages

- [[concepts/genai-handbook]] — Lilian Wengのブログ記事（RL Overview, Agent, Diffusion, Prompt Engineering）が🟢最重要リソースとして評価されている
- [[concepts/llm-course-roadmap]]
- [[concepts/learning-llms-in-2025]]
- https://linkedin.com/in/lilianweng — LinkedIn profile
- https://www.ayeshakhanna.com/women-in-ai-feature/lilian-weng — Women in AI feature
