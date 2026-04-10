---
title: "Lilian Weng"
handle: "@lilianweng"
created: 2026-04-10
updated: 2026-04-10
tags: [person, llm-research, ai-safety, agents, openai]
aliases: ["lilianweng", "Lilian Weng", "Lil'Log"]
---

# Lilian Weng (@lilianweng)

| | |
|---|---|
| **X** | [@lilianweng](https://x.com/lilianweng) |
| **Blog** | [Lil'Log](https://lilianweng.github.io) |
| **GitHub** | [lilianweng](https://github.com/lilianweng) |
| **Role** | VP of Research, OpenAI |
| **Known for** | Comprehensive ML survey posts, LLM-powered agents research, AI safety leadership |
| **Bio** | Lilian Weng is VP of Research at OpenAI, where she leads risk management and safety research for frontier models. She joined OpenAI in 2018 after working as a data scientist and software engineer at Meta, Dropbox, and Affirm. Since 2017, she has maintained "Lil'Log," one of the most respected technical blogs in ML, known for its deeply-researched survey posts on transformers, agents, diffusion models, and AI safety. |

## Overview

Lilian Weng occupies a rare position at the intersection of frontier AI research and practical safety engineering. As VP of Research at OpenAI, she leads the Preparedness team — responsible for safeguarding against major risks from OpenAI's most powerful models. She also serves on OpenAI's board safety and security committee. Her career trajectory, from data scientist at major Silicon Valley companies to research leadership at one of the world's most impactful AI labs, gives her a uniquely grounded perspective on both the capabilities and risks of modern AI systems.

But Weng's influence extends far beyond her role at OpenAI. Since 2017, she has maintained "Lil'Log" (lilianweng.github.io), a personal technical blog that has become one of the most comprehensive and accessible educational resources in machine learning. Her survey posts — covering topics from transformer architectures to adversarial attacks on LLMs — are distinguished by their mathematical rigor, thorough citations, and clear explanations. Many practitioners have used these posts as their primary introduction to advanced ML topics.

Weng's research interests span the full spectrum of modern AI: reinforcement learning, generative models, large language models, agent architectures, AI safety, and interpretability. Her blog posts often serve as de facto literature reviews for entire subfields, synthesizing dozens of papers into coherent narratives. Her 2023 post "LLM Powered Autonomous Agents" became one of the most widely-cited overviews of the agentic AI landscape.

## Core Ideas

### LLM-Powered Autonomous Agents

In her landmark June 2023 post ["LLM Powered Autonomous Agents"](https://lilianweng.github.io/posts/2023-06-23-agent/), Weng laid out a foundational architecture for AI agents:

- **Planning** — The LLM functions as the agent's "brain," decomposing complex tasks into sub-goals using Chain-of-Thought (CoT), Tree of Thoughts (ToT), or self-reflection mechanisms like ReAct and Reflexion
- **Memory** — Short-term memory (in-context learning, bounded by context window) and long-term memory (external vector stores using ANN algorithms like HNSW, FAISS, or ScaNN)
- **Tool Use** — External API integration, where the LLM acts as a router to specialized modules

Her analysis of ChemCrow (LLM + 13 chemistry tools) revealed a critical insight: human evaluations found ChemCrow vastly superior to GPT-4 alone, but LLM self-evaluations found them equal. *"LLMs lack domain expertise to self-evaluate correctness."* This finding has important implications for automated evaluation of AI systems.

Weng also highlighted safety concerns: in the Boiko et al. scientific agent study, 36% of illicit drug synthesis requests were accepted, though web search helped reject 5/7 blocked cases. This underscored the need for robust safety layers in agentic systems.

### Extrinsic Hallucinations in LLMs

In her July 2024 post ["Extrinsic Hallucinations in LLMs"](https://lilianweng.github.io/posts/2024-07-07-hallucination/), Weng provided one of the most comprehensive analyses of why LLMs fabricate information:

- **Pre-training data issues** — Internet-crawled corpora contain outdated, missing, or incorrect information that models memorize via log-likelihood maximization
- **Fine-tuning risks** — Citing Gekhman et al. (2024), she showed that LLMs learn new knowledge substantially slower than existing knowledge, and learning new knowledge *increases hallucination tendency*
- **Detection frameworks** — She catalogued methods including FActScore (decomposes text into atomic facts, validates via retrieval), SAFE (LLM agent iteratively searches to verify facts, 72% human agreement, 20x cheaper than manual), and SelfCheckGPT (black-box consistency across stochastic samples)

Her anti-hallucination analysis covered RARR (Retroactive Attribution using Research and Revision), Self-RAG (end-to-end training with intermittent reflection tokens), and retrieval-augmented approaches.

### Chain-of-Thought and Test-Time Compute

In her May 2025 post ["Why We Think"](https://lilianweng.github.io/posts/2025-05-01-thinking/), Weng reviewed the rapidly evolving landscape of reasoning in LLMs:

- Test-time compute and chain-of-thought reasoning have led to significant performance improvements
- Smaller models combined with advanced inference algorithms can offer Pareto-optimal trade-offs in cost and performance
- OpenAI's o1/o3 and DeepSeek-R1 showed that policy gradient algorithms applied to reasoning traces produce dramatic capability gains
- Reward hacking remains a fundamental challenge: RL agents exploit flaws in reward functions

She called for more research on open questions in test-time compute and chain-of-thought reasoning, noting that the exploration "presents new opportunities for reflection and error correction."

### Reward Hacking in Reinforcement Learning

In her November 2024 post, Weng examined how RL agents exploit imperfect reward functions — a problem that becomes more acute as RLHF becomes the de facto method for LLM alignment. She connected reward hacking to broader challenges in specifying objectives for increasingly capable AI systems.

### High-Quality Human Data

In February 2024, Weng wrote about the critical importance of human data quality for training modern models. As AI systems improve, the bottleneck shifts from compute and algorithms to the availability of high-quality human-generated training data — a resource that is finite and unevenly distributed across domains.

### Adversarial Attacks on LLMs

Her October 2023 post surveyed the landscape of adversarial attacks on language models, including jailbreak prompts, prompt injection, and data poisoning. She noted that adversarial attacks on text are "a lot more challenging" than on images due to the lack of direct gradient signals, connecting this to her earlier work on controllable text generation.

## Key Work

### Lil'Log Blog Posts (2017–2025)

Weng's blog contains over 50 technical deep-dives spanning approximately 19 hours of reading. Key posts include:

| Date | Title | Est. Read | Topic |
|---|---|---|---|
| May 2025 | "Why We Think" | 40 min | Test-time compute, CoT reasoning |
| Nov 2024 | "Reward Hacking in Reinforcement Learning" | 37 min | RL safety, objective specification |
| Jul 2024 | "Extrinsic Hallucinations in LLMs" | 29 min | LLM factuality, detection methods |
| Apr 2024 | "Diffusion Models for Video Generation" | 20 min | Generative models for video |
| Feb 2024 | "Thinking about High-Quality Human Data" | 20 min | Training data quality |
| Oct 2023 | "Adversarial Attacks on LLMs" | 33 min | Jailbreaks, prompt injection |
| Jun 2023 | "LLM Powered Autonomous Agents" | 31 min | Agent architecture, planning, memory |
| Mar 2023 | "Prompt Engineering" | 21 min | In-context learning, prompting methods |
| Jan 2023 | "The Transformer Family Version 2.0" | 45 min | Transformer architecture variants |
| Jan 2023 | "Large Transformer Model Inference Optimization" | 9 min | Efficient inference |
| 2022 | "Some Math behind Neural Tangent Kernel" | 17 min | Theoretical ML |
| 2021 | "What are Diffusion Models?" | 31 min | Generative models |
| 2020 | "How to Build an Open-Domain Question Answering System?" | 33 min | QA systems |
| 2019 | "Meta Reinforcement Learning" | 22 min | RL meta-learning |
| 2018 | "Policy Gradient Algorithms" | 52 min | RL algorithms |
| 2017 | "Learning Word Embedding" | 18 min | NLP fundamentals |

### OpenAI Research Leadership

As VP of Research at OpenAI, Weng leads the Preparedness team, which is responsible for:
- Safeguarding against major risks from frontier models
- Consolidating safety research under her leadership
- Serving on the board's safety and security committee
- Overseeing model evaluation and red-teaming efforts

Business Insider named Weng to their 2024 AI Power List for this work.

### Previous Industry Experience

Before joining OpenAI in 2018, Weng worked as a data scientist and software engineer at:
- **Meta (Facebook)** — ML/data science
- **Dropbox** — Data engineering
- **Affirm** — Financial ML systems

## Blog / Recent Posts

Lil'Log (lilianweng.github.io) is Weng's personal technical blog, maintained since 2017. It is distinguished by:

- **Mathematical rigor** — Posts include equations, proofs, and algorithmic details
- **Comprehensive citations** — Each post references dozens of papers with proper attribution
- **Visual explanations** — Diagrams and figures clarify complex architectures
- **Long-form depth** — Posts average 20–45 minutes of reading time
- **Broad coverage** — From classical ML (multi-armed bandits, object detection) to cutting-edge AI (diffusion models, LLM agents, adversarial attacks)

## Related People

- **John Schulman** — OpenAI colleague who provided feedback and edits on Weng's "Why We Think" post; co-creator of RLHF and PPO
- **Chip Huyen** — Both address ML systems; Huyen from production engineering, Weng from research depth
- **Eugene Yan** — Both write about LLM systems in production; Yan focuses on RecSys, Weng on fundamental research
- **Andrej Karpathy** — Both produce highly educational content on deep learning; Karpathy through videos/talks, Weng through written surveys
- **Andriy Burkov** — Both excel at making complex ML accessible through writing
- **Sam Altman** — CEO of OpenAI where Weng serves as VP of Research

## X Activity Themes

Lilian Weng's X/Twitter activity focuses on:

- **AI Safety Research** — Updates on OpenAI's preparedness and safety work
- **Technical Deep-Dives** — Sharing and discussing new ML papers and research developments
- **Blog Post Announcements** — Promoting new Lil'Log entries with detailed summaries
- **AI Policy & Governance** — Commentary on regulatory approaches to frontier AI
- **Research Community Engagement** — Interactions with other ML researchers and practitioners
- **Educational Content** — Sharing resources for learning advanced machine learning concepts
