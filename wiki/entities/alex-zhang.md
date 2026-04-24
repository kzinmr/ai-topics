---
title: "Alex L. Zhang"
tags: [[person]]
created: 2026-04-13
updated: 2026-04-24
---


# Alex L. Zhang

## Profile

- **Name:** Alex L. Zhang
- **X/Twitter:** [@a1zhang](https://x.com/a1zhang), [@lateinteraction](https://x.com/lateinteraction) (sub-account)
- **Homepage:** [alexzhang13.github.io](https://alexzhang13.github.io/)
- **Current:** PhD Student at MIT CSAIL (advisors: Omar Khattab & Tim Kraska)
- **Previous:** VantAI (AI-based drug discovery, NYC), Sakana AI (Tokyo, summer 2024)
- **Undergrad:** Princeton University, summa cum laude (highest honors), Computer Science
- **Awards:** 
  - Phillip Goldman '86 Senior Prize in Computer Science (Princeton CS department's highest academic honor, 1/216)
  - Outstanding Senior Thesis Prize ("Leveraging language for decision-making AI")
  - Outstanding Computer Science Service Award (co-founded AI@Princeton, organized first AI Tiger Trek)
  - ISEF 2019 — 2nd Place (device-independent tremor suppression orthoses)
  - KernelBench — ICML 2025 Best Paper

Alex Zhang is a PhD student at MIT CSAIL working on areas where language models are underutilized or inefficient. He is the primary author of **Recursive Language Models (RLMs)**, a paradigm that treats context as a programmable environment variable rather than a static prompt. His work sits at the intersection of ML systems, efficient inference, and agentic architectures.

## Core Ideas

### 1. Recursive Language Models (RLMs)

RLMs represent Zhang's most influential contribution — a **task-agnostic inference paradigm** that allows language models to handle near-infinite length contexts by programmatically examining, decomposing, and recursively calling themselves over input snippets.

> "RLMs offload the context as a variable in a REPL environment that the LM can interact with and launch sub-LM calls inside of."
> — Alex Zhang, RLM blog post (Oct 2025)

**Key insight:** Traditional LLMs are bottlenecked by context windows. RLMs solve this by treating the **entire prompt as an environment variable** in a Python REPL. The root model never sees the full context at once — instead, it writes code to peek into, slice, and recursively query parts of it.

**Why it matters:**
- Handles inputs up to **100x beyond model context windows**
- Zero information loss (no summarization)
- **2-3x reduction** in main model token consumption
- GPT-5 baseline: 24% on CodeQA → RLM (GPT-5-mini): 62%
- OOLONG tasks: base GPT-5 collapses at 1M+ tokens, RLM maintains accuracy

**The paradigm shift:**
> "Rather than directly ingesting its (potentially large) input data, the RLM allows an LLM to use a persistent Python REPL to load the full input as a string variable, then reason over its context in code and recursive LM calls, rather than purely in token space."
> — RLM paper (arXiv:2512.24601)

### 2. Scaffold vs. RL: The "Next Milestone" Thesis

Zhang articulates a clear progression:

> "We think that RLMs trained explicitly to recursively reason are likely to represent the next milestone in general-purpose LLM inference."
> — Alex Zhang, RLM blog post (Oct 2025)

This positions **trained scaffolds** as the future — not just inference-time tricks, but models specifically trained to operate within recursive environments. The scaffold becomes the environment for reinforcement learning.

### 3. Software 1.0→2.0→3.0 Paradigm

Zhang extends Karpathy's famous taxonomy:
- **Software 1.0:** Hand-written code (C++, Python)
- **Software 2.0:** Neural network weights (trained)
- **Software 3.0:** Trained scaffolds + LLMs (RLM, agent environments)

In this framework, the scaffold itself becomes a **trainable component** — not just a prompt engineering trick, but an environment that can be optimized through RL.

### 4. Karpathy Comparison: Training vs. Inference Optimization

Zhang draws a parallel to Karpathy's insight about training-time vs. inference-time computation:
- Karpathy: "Training is the bottleneck, not inference"
- Zhang: "Context management is the bottleneck, not model size"

Both recognize that the **structure of computation** matters more than raw parameters. RLMs externalize context management into an environment that can be optimized, just as Karpathy argued for optimizing training rather than inference.

### 5. The Mismanaged Geniuses Hypothesis (MGH) — April 2026

Co-authored with Zhening (Zed) Li and Omar Khattab, MGH posits that **frontier language models are severely underutilized due to sub-optimal scaffolding**, not inherent model limitations.

> *"AI models are already good enough for the next leap in capabilities. The bottleneck is no longer scaling model size or training data. It is how we manage, decompose, and compose existing frontier LMs."*

**Key claims:**
- Current agent scaffolds (ReAct, tool-use APIs) are brittle and force narrow reasoning patterns
- Models can already decompose tasks correctly but lack the environment to execute decompositions
- Learning the **composition operator** (chaining in-distribution LM calls into OOD solutions) is more efficient than scaling parameters
- **Proof:** Qwen3-4B-Instruct + RL bootstrapping on simple tasks → 100% success on 1M context/8 needles (was ~0%)

MGH extends the RLM framework into a broader industry thesis: **stop building bigger models, start building better scaffolds.**

See: [[mismanaged-geniuses-hypothesis]]

## GPU MODE & Benchmarking

Zhang is part of the core team running the **GPU MODE leaderboard**, which has hosted:
- NVFP4 Blackwell competition with NVIDIA
- Three $100k-$1M competitions with AMD
- Model optimization competition with Jane Street

### KernelBench (ICML 2025 Best Paper)

A benchmark for evaluating LLMs on GPU kernel generation. This work demonstrates Zhang's focus on **practical ML systems evaluation** — not just language benchmarks, but actual performance on hardware-level tasks.

### VideoGameBench (2025)

Evaluates LLMs on video game understanding and interaction — part of Zhang's broader interest in **evaluation-driven development**.

## Key Publications

| Year | Title | Venue | Notes |
|------|-------|-------|-------|
| 2025 | Recursive Language Models (RLMs) | arXiv:2512.24601 | Task-agnostic inference paradigm, 10M+ token context |
| 2025 | KernelBench | ICML 2025 | Best Paper — GPU kernel generation benchmark |
| 2026 | The Mismanaged Geniuses Hypothesis | Blog | Frontier models are underutilized; composition > scaling |
| 2026 | Language Models will be Scaffolds | Blog | Scaffold-first philosophy for next-gen AI |
| 2025 | VideoGameBench | — | LLM evaluation on video game tasks |
| 2025 | Neo-1 Model | — | New model architecture |
| 2025 | Project Popcorn | — | ML systems efficiency |
| 2025 | KernelLLM-8B | — | Language model for kernel tasks |
| 2024 | Triton kernels for OSS AlphaFold3 | — | 1k+ GitHub stars |
| 2024 | Language-guided World Models | ACL 2024 (SpLU-RoboNLP) | Robotics + language |

## Career Timeline

1. **Pre-college:** Built and sold PC games (one ~100k+ sales)
2. **High school:** Valedictorian (~1/400), ISEF 2nd Place (tremor suppression device)
3. **2020–2024:** Princeton University, summa cum laude
   - Founded AI@Princeton (largest AI student org)
   - Organized first AI Tiger Trek
   - Advisors: Karthik Narasimhan, Khanh Nguyen, Ofir Press, Kai Li
   - Thesis: "Leveraging language for decision-making AI"
   - Top CS student (Phillip Goldman '86 Prize)
4. **Summer 2021– Spring 2022:** TA for COS226 (Algorithms & Data Structures)
5. **Fall 2022:** TA for COS240 (Reasoning About Computation)
6. **Fall 2022:** Grader & TA for COS326 (Functional Programming)
7. **Spring 2023:** Grader for COS445 (Economics in Computing)
8. **Internships:** Apple (AI/ML), Snap Research, Claryo
9. **2024–2025:** VantAI (NYC) — AI-based drug discovery
10. **Summer 2024:** Sakana AI (Tokyo, Japan)
11. **2025–present:** MIT CSAIL PhD (advisors: Omar Khattab & Tim Kraska)
12. **2025:** RLM blog post (Oct), paper release (Dec), Prime Intellect adoption (Jan 2026)

## Connection to Shunyu Yao's "The Second Half"

Zhang and Yao converge on the insight that **the environment is the bottleneck**:

| Zhang's RLM | Yao's "Second Half" | Convergence |
|-------------|---------------------|-------------|
| Context → REPL variable | Environment is key RL component | Both treat context as environment |
| Recursive sub-calls | Reasoning is an action | Both externalize computation |
| Trainable scaffolds | RL finally generalizes | Both see trained scaffolds as future |
| RLMs > summarization | Evaluation > training | Both prefer active management over passive compression |

Prime Intellect synthesizes both:
> "Teaching models to manage their own context end-to-end through reinforcement learning will be the next major breakthrough."

## Blog Posts & Public Commentary

| Date | Title | Key Insight |
|------|-------|-------------|
| Oct 2025 | "Recursive Language Models" | RLMs treat context as an environment variable, not a static prompt |
| 2024 | "A Meticulous Guide to Advances in Deep Learning Efficiency" | Comprehensive survey from pre-AlexNet to foundation models |

## Quotes

> "RLMs offload the context as a variable in a REPL environment that the LM can interact with and launch sub-LM calls inside of."
> — Alex Zhang, RLM blog post (Oct 2025)

> "We think that RLMs trained explicitly to recursively reason are likely to represent the next milestone in general-purpose LLM inference."
> — Alex Zhang, RLM blog post (Oct 2025)

> "Language models will be scaffolds."
> — Alex Zhang (paraphrased in community discussions)

## Open Source Contributions

- **`alexzhang13/rlm`** — 3,296 GitHub stars, 20+ contributors, v0.1.1a (Feb 2026)
- **`alexzhang13/rlm-minimal`** — 749 GitHub stars, minimal implementation
- **`rlms` PyPI package** — 6,034 downloads/month
- **Triton kernels for AlphaFold3** — 1k+ GitHub stars
- **AI@Princeton** — Founded and led largest AI student organization at Princeton

## Related Concepts

- **[[RLM (Recursive Language Models)]]** — Zhang's primary contribution
- **[[Context Folding]]** — Parallel approach (Sun et al., 2025)
- **[[Shunyu Yao]]** — "The Second Half" framework; RL generalization thesis
- **[[Omar Khattab]]** — PhD advisor, ColBERT/DSPy creator
- **[[Tim Kraska]]** — PhD co-advisor, MIT DSG, ML systems
- **[[GPU MODE]]** — Benchmarking leadership
- **[[KernelBench]]** — ICML 2025 Best Paper
- **[[Scaffold vs RL Debate]]** — Both Zhang and Yao argue for trained scaffolds
- **** — RLM as a new ACI paradigm
- **** — RLM scales computation, not parameters
- **** — Trained scaffolds + LLMs

## Status

- **Entity status:** Full (L1+L2+L3 complete)
- **Quality target:** ~12KB, high quote rate (>30%), conceptual connections mapped
- **Cross-connections:** Omar Khattab (advisor), Tim Kraska (co-advisor), Shunyu Yao (parallel work), Karthik Narasimhan (Princeton advisor), Prime Intellect (RLM adoption)
- **Next enrichment:** Monitor RLM training results, Neo-1 developments, GPU MODE competition outcomes
- **Last updated:** 2026-04-13
