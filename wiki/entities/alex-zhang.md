---
title: "Alex Zhang"
handle: "@a1zhang"
created: 2026-04-10
updated: 2026-04-10
tags: [person, ai, ml-systems, rlm, gpu-computing, benchmarking, open-source]
aliases: ["@a1zhang", "a1zhang", "Alex L. Zhang"]
---

# Alex Zhang (@a1zhang)

| | |
|---|---|
| **X** | [@a1zhang](https://x.com/a1zhang) |
| **Blog** | [alexzhang13.github.io](https://alexzhang13.github.io/) |
| **GitHub** | [alexzhang13](https://github.com/alexzhang13) |
| **Role** | PhD Student at MIT CSAIL |
| **Known for** | Recursive Language Models (RLMs), GPU MODE community, KernelBench |
| **Bio** | Alex L. Zhang is a PhD student at MIT CSAIL advised by Omar Khattab and Tim Kraska. His research focuses on areas where language models are underutilized or inefficient, from novel inference strategies to GPU kernel generation benchmarks. He is a core member of the GPU MODE community and has previously worked at Sakana AI in Tokyo and VantAI in NYC on AI-based drug discovery. |

## Overview

Alex Zhang is a rising figure at the intersection of ML systems research and practical GPU computing infrastructure. As a PhD student at MIT CSAIL under the joint supervision of Omar Khattab and Tim Kraska, he works in the OASYS (Optimized AI Systems) lab on making language models more efficient and capable through novel inference paradigms.

His most impactful contribution to date is **Recursive Language Models (RLMs)**, an inference strategy introduced in late 2025 that allows language models to decompose and recursively interact with input contexts of unbounded length through a REPL environment. Rather than attempting to process massive contexts in a single pass (the approach that hits the well-documented "context rot" problem), RLMs let the model programmatically examine, search, partition, and recurse over its input. In experiments, an RLM using GPT-5-mini outperformed GPT-5 on the OOLONG benchmark by more than double the number of correct answers at 132K tokens, and did so at a lower cost per query.

Beyond his research, Alex is a central figure in the **GPU MODE** community, which runs open GPU kernel programming competitions. He helped organize the NVFP4 Blackwell competition with NVIDIA, three $100K–$1M competitions with AMD, and a model optimization competition with Jane Street. Through projects like KernelBench, VideoGameBench, and SWE-bench Multimodal, he has established himself as a leader in building rigorous, real-world benchmarks for AI systems.

Before MIT, Alex graduated as the top student of the Princeton CS department, where he founded and ran the largest AI student organization. His mentors there included Professor Karthik Narasimhan, Dr. Khanh Nguyen, Dr. Ofir Press, and Professor Kai Li. He has also interned at Snapchat, Apple, and Claryo, and notably built and sold PC games early in his career (one reaching ~100K+ players). He spent a summer at Sakana AI in Tokyo and a year as a researcher at VantAI in NYC working on AI-based drug discovery.

## Core Ideas

### Recursive Language Models (RLMs)

Alex's signature research contribution is the concept of **Recursive Language Models** — an inference-time scaling approach that reframes how LLMs handle long contexts. Rather than treating context as something to be stuffed into a single forward pass, RLMs treat the context as a variable stored in a programmatic environment (a Python REPL) that the model can interact with recursively.

From the RLM blog post: *"We take a context-centric view rather than a problem-centric view of input decomposition. The LM autonomously decides how to chunk, search, and recurse over data."*

Key design principles from the RLM framework:

- **Root LM never sees the full context.** The root model (at depth 0) receives only the query and a pointer to the environment, preventing window clogging and the degradation that comes from processing massive contexts in a single pass.
- **Programmatic interaction via REPL.** The model writes code to `peek`, `grep`, `partition`, or `transform` the context, then spawns isolated sub-LM calls (at depth 1+) on specific subsets.
- **Emergent strategies.** The REPL environment reveals interpretable behavior: peeking (sampling first N characters to infer data structure), grepping (using regex to narrow search space), partition + map (chunking context for parallel recursive calls), and summarization (compressing subsets for the root LM to synthesize).
- **Not agents, but scaffolds.** Alex distinguishes RLMs from agentic approaches: *"Agents rely on human-defined task decomposition. RLMs let the LM autonomously decompose context."*

The RLM framework was formalized in the paper "Recursive Language Models" (Zhang, Kraska & Khattab, 2025, arXiv:2512.24601) and has an open-source implementation at github.com/alexzhang13/rlm with 3,200+ GitHub stars.

### Context Rot and Inference-Time Compute

A key motivation behind RLMs is the phenomenon Alex calls **"context rot"** — the degradation of model accuracy and recall as context length increases, even when the context fits within the model's advertised window. Current benchmarks (like RULER) do not capture real-world failure modes that emerge with bloated chat histories or massive documents.

RLMs bypass context rot by never feeding massive contexts to a single model call. Instead, they treat inference-time compute as a scalable axis — the same way chain-of-thought reasoning treats computation as something the model can spend more of. Alex's view is that *"fixed interaction formats (like CoT/ReAct) enable performance gains. RLM trajectories are fully RL-trainable, representing the next milestone in inference-time scaling."*

The RLM approach has shown remarkable results: on the BrowseComp-Plus benchmark (multi-hop QA over ~100K documents), RLM(GPT-5) maintained perfect accuracy at 1000 documents (10M+ tokens), while base GPT-5 and ReAct+BM25 degraded significantly as context scaled.

### GPU Kernel Generation and Benchmarking

Through the GPU MODE community, Alex has been instrumental in building benchmarks that test LLMs' ability to write efficient GPU kernels — a task that requires deep domain expertise and is crucial for performant ML architectures.

**KernelBench** (ICML 2025, DL4C Best Paper) evaluates LMs on 250 real-world PyTorch ML workloads that could be accelerated using performant GPU kernels. The results showed that frontier reasoning models struggle significantly, matching PyTorch's baseline performance in less than 20% of cases. The benchmark introduced a new `fast_p` metric measuring the percentage of generated kernels that are both functionally correct and offer a speedup greater than threshold `p`.

**KernelBot** (CODEML @ ICML 2025, Spotlight) is a competition platform for writing heterogeneous GPU code, running as part of the GPU MODE community with support from NVIDIA, AMD, and Modal.

### The Mismanaged Geniuses Hypothesis

In his blog post "The Mismanaged Geniuses Hypothesis," Alex explores the idea that modern AI systems have untapped capabilities that are not properly leveraged by current architectures and inference strategies. The hypothesis suggests that with better scaffolding, decomposition strategies, and inference-time compute allocation, we could extract significantly more capability from existing models — a theme that connects directly to his RLM work.

### Language Models as Scaffolds

In "Language Models will be Scaffolds," Alex argues that LLMs should be viewed as foundational infrastructure upon which more capable systems are built, rather than as end-user products themselves. This perspective underpins his work on RLMs (where the model is scaffolded by a REPL environment) and GPU MODE (where models are scaffolded by benchmark-driven evaluation and competition frameworks).

## Key Work

### Research Papers & Preprints

- **Recursive Language Models** (2025) — arXiv:2512.24601. Co-authored with Tim Kraska and Omar Khattab. Proposes RLMs as a task-agnostic inference paradigm for handling near-infinite length contexts through recursive decomposition.
- **KernelBench: Can LLMs Write Efficient GPU Kernels?** (ICML 2025, DL4C Best Paper) — Co-authored with Anne Ouyang, Simon Guo, Simran Arora, William Hu, Christopher Re, and Azalia Mirhoseini. A comprehensive benchmark of 250 ML workloads for evaluating GPU kernel generation by LLMs.
- **KernelBot: A Competition Platform for Writing Heterogeneous GPU Code** (CODEML @ ICML 2025, Spotlight) — Co-authored with Matej Sirovatka, Erik Schultheis, Benjamin Horowitz, and Mark Saroufim. An open-source platform for GPU kernel programming competitions.
- **VideoGameBench: Can Vision-Language Models Complete Popular Video Games?** (Under review) — Evaluates VLMs on real-world video game tasks, testing multimodal understanding and interaction capabilities.
- **SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?** (ICLR 2025) — Extends the SWE-bench framework to multimodal software engineering tasks.
- **Language-guided World Models: A Model-Based Approach to AI Control** (SpLU-RoboNLP Workshop @ ACL 2024, Oral) — Explores using language models for robotics control through world model approaches.
- **Neo-1** (2025) — A model developed through GPU MODE research.
- **KernelLLM-8B** (2025) — A specialized LLM for GPU kernel generation, available on Hugging Face.
- **Scalable Video Understanding Benchmarks through Sports** (DMLR Workshop @ ICLR 2024) — Using sports video as a domain for building scalable video understanding benchmarks.
- **Project Popcorn** (2025) — A GPU MODE project exploring GPU kernel generation and optimization, with 142+ stars on GitHub.
- **Triton kernels for OSS AlphaFold3** (2024) — Contributed Triton kernel implementations that gained 1K+ GitHub stars.

### Open Source Projects

- **[RLM](https://github.com/alexzhang13/rlm)** — General plug-and-play inference library for Recursive Language Models, supporting various sandboxes (3,200+ stars).
- **[RLM Minimal](https://github.com/alexzhang13/rlm-minimal)** — Minimal implementation for building on top of RLMs.
- **[Popcorn CLI](https://github.com/gpu-mode/popcorn-cli)** — Command-line tool for submitting GPU kernel solutions to the GPU MODE leaderboard (142 stars).
- **[KernelBot](https://github.com/gpu-mode/kernelbot)** — Backend service for the GPU MODE kernel competition platform (90 stars).
- **[KernelBench](https://github.com/ScalingIntelligence/KernelBench)** — Benchmark framework for GPU kernel generation evaluation.

### Blog Posts

- **"Recursive Language Models"** (October 2025) — The original blog post introducing the RLM concept with detailed explanations, motivation, and experimental results.
- **"The Mismanaged Geniuses Hypothesis"** — Explores untapped capabilities in current AI systems.
- **"Language Models will be Scaffolds"** — Proposes viewing LLMs as foundational infrastructure rather than end-user products.
- **"A Meticulous Guide to Advances in Deep Learning Efficiency over the Years"** — A comprehensive survey of efficiency improvements in deep learning.
- **"The Annotated Kolmogorov-Arnold Network (KAN)"** — An educational deep-dive into KANs.
- **"Highlights of NeurIPS 2023 from Reading All 3584 Abstracts"** — An AI-assisted analysis of the entire NeurIPS 2023 abstract corpus.

## Blog / Recent Posts

| Date | Title | Summary |
|------|-------|---------|
| Oct 2025 | Recursive Language Models | Introduces RLMs as an inference paradigm for unbounded context handling via REPL environments. Includes experimental results showing GPT-5-mini via RLM outperforming GPT-5 on OOLONG benchmark. |
| 2025 | The Mismanaged Geniuses Hypothesis | Argues that current AI systems have capabilities that are not being properly leveraged by existing architectures. |
| 2025 | Language Models will be Scaffolds | Proposes viewing LLMs as foundational infrastructure rather than end-user products. |
| 2024 | A Meticulous Guide to Advances in Deep Learning Efficiency | Comprehensive survey of efficiency improvements across the deep learning landscape. |
| 2024 | The Annotated Kolmogorov-Arnold Network (KAN) | Educational deep-dive into KAN architecture and its implications. |
| 2023 | Highlights of NeurIPS 2023 from Readinging All 3584 Abstracts | AI-assisted analysis of the full NeurIPS 2023 abstract corpus to identify key trends. |

## Related People

- **[[Omar Khattab]]** — PhD advisor at MIT CSAIL; co-author on RLM paper; creator of ColBERT, DSPy.
- **[[Tim Kraska]]** — PhD co-advisor at MIT CSAIL; co-author on RLM paper.
- **[[Mark Saroufim]]** — GPU MODE collaborator; co-author on KernelBot; PyTorch team at Meta.
- **[[Christopher Re]]** — Stanford professor; co-author on KernelBench; Hazy Research lab.
- **[[Simran Arora]]** — GPU MODE community member; KernelBench co-author.
- **[[Karthik Narasimhan]]** — Princeton professor; early mentor.
- **[[Ofir Press]]** — Princeton; early mentor; known for work on LLM inference optimization.

## X Activity Themes

Alex's X activity (@a1zhang) centers on:

1. **ML Systems Research** — Sharing new papers, benchmarks, and open-source tools related to efficient inference, GPU computing, and language model capabilities.
2. **GPU MODE Community** — Announcing competitions (NVIDIA Blackwell, AMD, Jane Street), sharing benchmark results, and engaging with the GPU kernel programming community.
3. **AI Benchmarking** — Discussing the methodology, results, and implications of benchmarks like KernelBench, VideoGameBench, and SWE-bench Multimodal.
4. **Open Source & Reproducibility** — Advocating for open-source research, sharing code repositories, and building transparent evaluation frameworks.
5. **Inference-Time Compute** — Exploring how spending more compute at inference time (through recursion, search, and decomposition) can dramatically improve model capabilities.
6. **AI Education** — Writing annotated guides and surveys to help the broader ML community understand emerging techniques.
