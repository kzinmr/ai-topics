---
title: "Andrej Karpathy"
handle: "@karpathy"
url: "https://karpathy.ai/"
twitter: "https://x.com/karpathy"
github: "https://github.com/karpathy"
huggingface: "https://huggingface.co/karpathy"
blog: "https://karpathy.bearblog.dev/"
status: active
tags:
  - ai
  - deep-learning
  - education
  - coding-agents
  - open-source
  - computer-vision
  - self-driving
  - llms
---

# Andrej Karpathy (@karpathy)

## Overview

**Andrej Karpathy** (born October 23, 1986, Bratislava, Czechoslovakia) is a leading AI researcher and educator, widely regarded as one of the most effective communicators of deep learning concepts to a broad audience. He relocated to Toronto, Canada at age 15 (~2001). He is a **co-founder of OpenAI** (2015), former **Senior Director of AI at Tesla** (2017-2022) where he led the Autopilot vision team, and founder/CEO of **Eureka Labs** (2024) — an AI-native education platform. He coined the terms **"vibe coding"** (February 2025) and **"agentic engineering"** (February 2026), both of which became widely adopted descriptions of AI-assisted software development.

His YouTube series **"Neural Networks: Zero to Hero"** is one of the most popular free deep learning educational resources on the internet. His Stanford course **CS231n: Convolutional Neural Networks for Visual Recognition** (2015-2017) grew from 150 to 750 students and became one of the university's most popular classes.

## Timeline

| Date | Event |
|------|-------|
| Oct 1986 | Born in Bratislava, Czechoslovakia (now Slovakia) |
| ~2001 | Relocates to Toronto, Canada at age 15 |
| 2009 | BSc University of Toronto — Computer Science & Physics, Math minor |
| 2011 | MSc University of British British Columbia — ML for robotics/controllers (advisor: Michiel van de Panne) |
| ~2011-2015 | PhD at Stanford, studying computer vision under Fei-Fei Li |
| 2014/2015 | Publishes "Deep Visual-Semantic Alignments for Generating Image Descriptions" (Flickr30k: BLEU-4: 15.7, BLEU-1: 57.3) |
| 2015 | Co-founds OpenAI; creates CS231n at Stanford |
| 2015 | Publishes ConvNetJS, one of the first browser-based deep learning libraries |
| 2016 | Builds **OpenAI Universe** — web-based agent environments |
| 2017 | Publishes "World of Bits" — platform for training RL agents on web tasks |
| 2017 | Joins Tesla as Director of AI, leads Autopilot vision team |
| 2017 | Publishes "Software 2.0" — seminal essay on neural networks as programs |
| 2019 | Publishes "A Recipe for Training Neural Networks" — highly practical guide |
| 2021 | "Neural Networks: Zero to Hero" YouTube series begins |
| 2021 | Publishes "A from-scratch tour of Bitcoin in Python" |
| May 2021 | Tesla Vision: removes radar from Model 3/Y (camera-only autonomy) |
| Feb 2022 | Removes radar from Model S/X — full Tesla Vision rollout |
| Jul 13, 2022 | Leaves Tesla after 5 years, citing slow convergence to unsupervised autonomy despite exponential compute scaling |
| Oct 2025 | Releases **nanochat** — full-stack ChatGPT alternative deployable for <$100 cloud cost |
| Dec 2025 | **Phase shift in coding**: transitions from 80% manual coding to 80% AI agent coding in a matter of weeks |
| Dec 2025 | Publishes "2025 LLM Year in Review" on bearblog |
| Feb 2026 | Coins **"agentic engineering"** — managing multiple AI coding agents in parallel |
| Feb 2026 | Publishes **microgpt** — 200 lines of pure Python that trains and inferences a GPT |
| Mar 2026 | Releases **autoresearch** — AI agents running research autonomously overnight on single-GPU nanochat setups |
| Mar 2026 | Receives **NVIDIA DGX Station GB300** hand-delivered by Jensen Huang |
| Jan 2026 | Viral X thread on AI coding workflow: "I really am mostly programming in English now" — 39K+ likes, 7.5M+ impressions |
| 2023-2024 | Returns to OpenAI, builds team on midtraining and synthetic data generation |
| 2024 | Launches **Eureka Labs**, AI-native education company |
| 2024 | Announces **LLM101n** — course to build an LLM from scratch in Python, C, and CUDA |
| Apr 2025 | Coins term **"vibe coding"** after using LLMs to build MenuGen prototype |
| Apr 2025 | Publishes "Power to the people: How LLMs flip the script on technology diffusion" |
| Sep 2024 | Starts posting on karpathy.bearblog.dev |
| Dec 2025 | **Phase shift in coding**: transitions from 80% manual coding to 80% AI agent coding in a matter of weeks |
| Dec 2025 | Publishes "2025 LLM Year in Review" on bearblog |
| Feb 2026 | Coins **"agentic engineering"** — managing multiple AI coding agents in parallel |
| Feb 2026 | Publishes **microgpt** — 200 lines of pure Python that trains and inferences a GPT |
| Mar 2026 | Releases **autoresearch** — AI agents running research autonomously overnight on single-GPU nanochat setups |
| Jan 2026 | Viral X thread on AI coding workflow: "I really am mostly programming in English now" — 39K+ likes, 7.5M+ impressions |

## Research Contributions

### Multimodal Vision-Language (2014-2015)
- **Paper:** "Deep Visual-Semantic Alignments for Generating Image Descriptions" (with Fei-Fei Li)
- Pioneered joint embedding spaces mapping image regions to word embeddings via hinge loss on cosine similarity
- **Flickr30k results:** BLEU-4: 15.7, BLEU-1: 57.3
- Laid groundwork for modern vision-language models (CLIP, Flamingo, etc.)

### Large-Scale Video Classification — Sports-1M (2014)
- Created **Sports-1M dataset**: 1.1 million YouTube videos across 487 classes
- **Innovation:** Temporal CNN fusion strategies (early, late, slow fusion)
- **Results:** Top-1: 63.9%, Top-5: 82.4% (surpassed traditional HOG/HOF at 55.3%)
- One of the largest video classification datasets at the time

### Character-level Language Models (2015-2016)
- Demonstrated character-level RNNs generating coherent Shakespeare-style prose in 4-6 epochs
- Highlighted empirical scaling laws that foreshadowed transformer architectures
- Early evidence that simple models + sufficient data could produce surprisingly coherent output

### Data-Centric AI Philosophy
- *"Data quality often trumps model scale"* — emphasis on curated/synthetic data pipelines
- Advocates for preventing model collapse through careful data curation
- Focus on addressing long-tail edge cases through targeted data collection

## Key Projects

### Eureka Labs (2024–present)
- **AI-native education company** founded July 16, 2024
- Vision: "Teacher + AI symbiosis" — human experts design courses, AI teaching assistants scale personalized guidance
- First product: **LLM101n** — undergraduate-level course to build an LLM chat interface from scratch in Python, C, and CUDA, with minimal CS prerequisites
- Goal: make high-quality education accessible to everyone, anywhere
- Karpathy's statement: *"Eureka Labs is the culmination of my passion in both AI and education over ~2 decades"*

### microgpt (2026)
- **200 lines of pure Python** with zero dependencies that trains and inferences a GPT
- Contains: dataset, tokenizer, autograd engine, GPT-2-like architecture, Adam optimizer, training loop, inference loop
- Culmination of micrograd → makemore → nanoGPT → microgpt progression
- 4,192 parameters total — demonstrates that the full algorithmic content of an LLM fits in a tiny script
- "I cannot simplify this any further" — Karpathy's statement on the script's minimalism

### autoresearch (2026)
- AI agents running research experiments autonomously overnight on single-GPU nanochat setups
- Structure: `prepare.py` (locked), `train.py` (agent-edited), `program.md` (human instructions)
- Mechanism: **Ratchet loop** — 5-min wall-clock training → eval `val_bpb` → git commit if improved
- Demonstrates practical use of AI agents for scientific discovery
- Part of Karpathy's broader "agentic engineering" workflow philosophy

### Dobby the Elf Claw (2026)
- Local, secure smart-home AI agent running on NVIDIA DGX Station GB300
- Interfacing via WhatsApp, autonomously reverse-engineering device APIs
- Named after Dobby from Harry Potter — a free elf that helps without being asked
- Exemplifies Karpathy's vision of AI agents operating autonomously in the physical world

### NanoGPT (2022)
- Minimal, educational PyTorch GPT implementation (~47.9k GitHub stars)
- Widely used as a teaching tool and starting point for LLM experimentation
- Simpler, more readable alternative to Hugging Face Transformers for learning

### llm.c (2024)
- Raw C/CUDA implementation of GPT-2 training and inference
- Demonstrates that LLM training can be done in a single, understandable file
- No PyTorch dependency — everything from scratch in C and CUDA
- Part of Karpathy's commitment to demystifying LLM internals

### nanochat (Oct 2025)
- Full-stack ChatGPT alternative deployable for **<$100 cloud cost**
- Combines nanoGPT training with a minimal web interface
- Designed for self-hosted, local LLM deployment
- Shows the complete pipeline from data → training → inference → deployment

### makemore (2022)
- Character-level language model that generates names
- Educational project showing how to build neural networks from scratch
- Demonstrates autoregressive generation at a conceptual level

### micrograd (2019)
- Tiny scalar-valued autograd engine in Python
- Builds a neural network on top for binary classification
- One of Karpathy's most popular educational projects — teaches backpropagation from scratch
- Used as the foundation for thousands of deep learning tutorials

### CS231n (2015-2017)
- Stanford course: Convolutional Neural Networks for Visual Recognition
- Grew from 150 to 750 students — one of Stanford's most popular classes
- Course notes, videos, and assignments remain widely used
- Established Karpathy as a world-class educator

### ConvNetJS (2015)
- One of the first browser-based deep learning libraries
- Allowed training neural networks directly in JavaScript
- Pioneering demo of accessible, visual deep learning education

### Tesla Autopilot (2017-2022)
- Director → Senior Director of AI at Tesla, led the Autopilot vision team
- Championed **Tesla Vision** — camera-only autonomy approach (no lidar)
- Removed radar from Model 3/Y (May 2021) and Model S/X (Feb 2022)
- Implemented closed-loop **data engine**: deploy → collect edge cases → auto-label → retrain → redeploy
- Scaled training on billions of fleet miles using PyTorch (adopted 2020)
- Scaled team from ~30 to ~200+ engineers during his tenure
- Left July 13, 2022, citing slow convergence to unsupervised autonomy despite exponential compute scaling

### OpenAI (2015-2017, 2023-2024)
- Co-founding member (2015) — founding research scientist
- **Tenure 1 (2015-2017):** Advanced computer vision, generative modeling, RL. Built **OpenAI Universe** (2016) and **World of Bits** (2017) — platforms for training RL agents on web-based environments
- Contributed to GPT architecture development during first stint
- **Tenure 2 (2023-2024):** Returned to build team on midtraining and synthetic data generation
- Departed voluntarily on Feb 13, 2024 to pursue independent projects (Eureka Labs)

## Writings & Blog Posts

### Bearblog (2024–present)

**2025 LLM Year in Review** (Dec 2025)
- Comprehensive assessment of LLM progress in 2025
- Analysis of model capabilities, limitations, and trajectory

**Verifiability** (Nov 2025)
- Explores the fundamental importance of verifiability in AI systems
- Argues that the ability to verify outputs is more important than raw capability

**The space of minds** (Nov 2025)
- Philosophical reflection on the diversity of possible intelligences
- Questions whether current LLMs occupy a narrow or broad region of possible "minds"

**Animals vs Ghosts** (Oct 2025)
- Conceptual framework for thinking about AI behavior
- Contrasts reactive, stimulus-driven behavior (animals) with generative, imagination-driven behavior (ghosts)

**Power to the people: How LLMs flip the script on technology diffusion** (Apr 2025)
- Argues that LLMs dramatically accelerate the spread of technical capabilities
- Previously, expertise was the bottleneck; now it's access and judgment
- Democratizing effect on software development

**Vibe coding MenuGen** (Apr 2025)
- Origin of the term **"vibe coding"**
- Built a menu generation prototype using LLMs
- Describes the experience of coding by natural language description and iterative refinement

**Finding the Best Sleep Tracker** (Mar 2025)
- Personal project comparing sleep tracking devices
- Shows his data-driven approach to personal decisions

**The append-and-review note** (Mar 2025)
- Note-taking methodology: append new thoughts, periodically review and synthesize
- Practical system for knowledge management

**Digital hygiene** (Mar 2025)
- Personal practices for maintaining digital health and productivity
- Parallel to his "chemical hygiene" post

**Chemical hygiene** (Dec 2025)
- Systematic approach to managing chemical/biological safety in a home lab context
- Shows his methodical approach to risk management

**Auto-grading decade-old Hacker News discussions with hindsight** (Dec 2025)
- Uses LLMs to evaluate old HN discussions with the benefit of hindsight
- Tests predictive accuracy of past comments

### Older Blogs

**Software 2.0** (Nov 2017) — karpathy.github.io
- Seminal essay arguing that neural networks are the new "software"
- Traditional programming (Software 1.0) writes explicit rules; Software 2.0 learns patterns from data
- One of the most influential essays in deep learning, widely cited

**A Recipe for Training Neural Networks** (Apr 2019)
- Practical, experience-based guide to training neural networks
- Covers data inspection, overfitting to a single batch, regularization, optimization
- Considered essential reading for ML practitioners

**A from-scratch tour of Bitcoin in Python** (Mar 2021)
- Complete implementation of Bitcoin transaction creation, signing, and broadcasting
- Demonstrates his interest in understanding systems at their lowest level

**A Survival Guide to a PhD** (Sep 2016)
- Advice on navigating the PhD experience
- Covers advisor relationships, research productivity, and mental health

## X/Twitter Activity & Influence

Karpathy is one of the most followed and influential accounts in AI on X/Twitter (1M+ followers). His posts regularly generate millions of impressions and shape industry discourse.

### "Vibe Coding" (April 2025)
Coined the term that became the dominant cultural descriptor for AI-assisted software development. The phrase captured the experience of building software by describing intent in natural language and iteratively refining — rather than writing code line by line.

### "Programming in English" Thread (January 2026)
His viral post about transitioning from 80% manual to 80% agent coding received **39,345 likes, 7,524,606 impressions**, and sparked global debate about the future of software engineering. Key quotes:
> *"I really am mostly programming in English now, a bit sheepishly telling the LLM what code to write... in words. It hurts the ego a bit."*
> *"LLM agent capabilities (Claude & Codex especially) have crossed some kind of threshold of coherence around December 2025 and caused a phase shift in software engineering."*
> *"2026 is going to be a high energy year as the industry metabolizes the new capability."*

### "Slopacolypse" Warning (January 2026)
Predicted 2026 would see a flood of low-quality AI-generated content across GitHub, Substack, arXiv, X, Instagram, and all digital media — coining another widely adopted term.

### "Agentic Engineering" (February 2026)
Reframed AI coding from individual assistance to **managing multiple agents in parallel** — giving them tasks, reviewing outputs, and orchestrating workflows rather than writing code directly.

### Key Observations on AI Agents
From his detailed writings and posts, Karpathy has identified several critical patterns:
- **Tenacity**: AI agents never get tired or demoralized — stamina is a core bottleneck that LLMs dramatically increase
- **Leverage**: "Don't tell it what to do, give it success criteria and watch it go"
- **Fallibility**: Agents make subtle conceptual errors, not syntax errors — they need human oversight
- **Sycophancy**: Agents don't push back when they should, don't manage their own confusion
- **Bloat**: Agents tend to overcomplicate code and APIs

## Core Ideas

### AGI Timeline: ~10 Years
- Predicts steady, incremental diffusion of AI capabilities, not a sudden explosion
- Key bottlenecks: continual learning/memory, synthetic data collapse, RL inefficiency
- Advocates for the **"march of nines"** — measuring progress in reliability (99.9%, 99.99%) rather than benchmark leaderboard scores

### Critique of Current Reinforcement Learning
- Calls current RL *"terrible"* due to reward hacking and extreme sample inefficiency
- Views RLHF as *"barely RL"* — more of a targeted finetuning approach
- Prefers imitation learning + targeted finetuning over pure RL approaches
- Believes RL needs fundamental algorithmic improvements before it can scale effectively

## Core Ideas

### Software 2.0
The fundamental paradigm shift where neural networks replace hand-coded programs. Instead of writing explicit rules (Software 1.0), we specify objective functions and let the network learn the implementation from data. This is not a metaphor — it is literally what is happening across the industry.

### Vibe Coding
Coding by describing intent in natural language and iteratively refining based on the output. The programmer becomes a curator and reviewer rather than a writer. The "vibe" is the feeling of working with AI as a creative partner — fast, exploratory, and low-friction.
- **Concrete example:** MenuGen (Apr 2025) — OCR + AI image gen for restaurant menus, built with Cursor/Claude & Superwhisper (voice-to-code)
- **Deployment friction:** Likens deploying to Vercel, Supabase, Stripe, and APIs to *"assembling complex IKEA furniture"*
- **Prediction:** Agent-native CLIs will eventually automate deployment friction entirely

### Agentic Engineering
The next evolution beyond vibe coding: **managing multiple AI agents in parallel**, each handling different tasks, with the human providing high-level direction, judgment, taste, oversight, and iteration. This is "delegation" at scale — the engineer becomes a manager rather than an individual contributor.

### Teacher + AI Symbiosis
Human experts design courses and curricula, but AI teaching assistants scale personalized guidance to every student. The goal is to make it possible for anyone to learn from the best minds in their field — "learning physics as if studying directly under Richard Feynman."

### Verifiability Over Raw Capability
The ability to verify AI outputs is more important than raw model capability. Without verification, higher capability is just more confident wrongness. This applies to coding agents, research agents, and all AI systems.

### Understanding is the Bottleneck
*"The biggest bottleneck in AI isn't compute or data. It's understanding."* Karpathy believes that demystifying AI through education is the most important work for long-term progress. Free, accessible education (YouTube, open courses, blog posts) is his primary contribution mechanism.

### Minimalism in Education
His progression from micrograd → makemore → nanoGPT → microgpt shows a commitment to **reducing AI concepts to their absolute minimum**. If you can understand it in 200 lines of Python, you understand it. Everything else is just efficiency.

### Generalists Will Outperform Specialists
With LLMs filling in the micro-details, generalists with broad knowledge and good judgment will increasingly outperform narrow specialists. The engineer's value shifts from depth in one area to breadth across many areas plus strong taste and oversight.

### The "Slopacolypse" is Inevitable
Low-quality AI-generated content will flood all platforms. The defense is not to avoid AI but to develop better taste, verification skills, and curation abilities. Quality will become more valuable precisely because slop becomes cheaper.

### Programming Will Feel Like Playing Factorio
Future coding will resemble resource management games — setting up systems, defining goals, and watching agents execute — rather than typing individual statements. The skill shifts from writing code to designing systems and verifying outputs.

## Key Questions Karpathy is Exploring

1. **What happens to the "10X engineer"?** — The ratio of productivity between the mean and the max engineer may grow *a lot*
2. **Do generalists increasingly outperform specialists?** — LLMs are better at fill-in-the-blanks (micro) than grand strategy (macro)
3. **What does LLM coding feel like in the future?** — Is it like playing StarCraft? Factorio? Music?
4. **How much of society is bottlenecked by digital knowledge work?** — If AI removes this bottleneck, the economic implications are enormous
5. **What happens when the intelligence part is ahead of all the rest?** — Tools, workflows, organizations, and diffusion all lag behind model capability

## Key Links

- **Personal website**: [karpathy.ai](https://karpathy.ai/)
- **Blog (Bearblog)**: [karpathy.bearblog.dev](https://karpathy.bearblog.dev/)
- **Blog (GitHub Pages)**: [karpathy.github.io](http://karpathy.github.io/)
- **X/Twitter**: [@karpathy](https://x.com/karpathy)
- **GitHub**: [github.com/karpathy](https://github.com/karpathy)
- **YouTube**: [Zero to Hero playlist](https://karpathy.ai/zero-to-hero.html)
- **Eureka Labs**: [@EurekaLabsAI](https://x.com/EurekaLabsAI)
- **Hugging Face**: [huggingface.co/karpathy](https://huggingface.co/karpathy)
- **Google Scholar**: [Andrej Karpathy](https://scholar.google.com/citations?user=4kAboOEAAAAJ)
- **TED Talk**: [How AI Can Save Humanity](https://www.ted.com/talks/andrej_karpathy_how_ai_can_save_humanity)
- **Dwarkesh Podcast (2025)**: [Andrej Karpathy — Eureka Labs](https://www.youtube.com/watch?v=...)

## Related

- [[eureka-labs]] — AI-native education company he founded
- [[software-2.0]] — His seminal essay on neural networks as programs
- [[vibe-coding]] — Term he coined for AI-assisted software development
- [[agentic-engineering]] — Term he coined for managing multiple AI agents in parallel
- [[micrograd]] — His educational autograd engine
- [[nanoGPT]] — Minimal GPT implementation for education
- [[cs231n]] — His Stanford computer vision course
- [[openai]] — Co-founded in 2015
- [[tesla-autopilot]] — Led AI team from 2017-2022
- [[deep-learning]] — Core research area
- [[computer-vision]] — PhD research area
- [[simon-willison]] — Fellow AI educator and blogger
- [[llm-education]] — Teaching LLMs from first principles
