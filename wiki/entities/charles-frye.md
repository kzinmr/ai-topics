---
title: "Charles Frye"
handle: "@charles_irl"
created: 2026-04-10
updated: 2026-04-10
tags: [person, x-account, ai, ml-engineering, gpu, infrastructure, developer-advocacy]
aliases: ["charles_irl", "charles frye modal"]
---

# Charles Frye (@charles_irl)

| | |
|---|---|
| **X** | [@charles_irl](https://x.com/charles_irl) |
| **Blog** | [charlesfrye.github.io](https://charlesfrye.github.io) |
| **GitHub** | [charlesfrye](https://github.com/charlesfrye) |
| **Role** | Developer Advocate / AI Engineer at Modal |
| **Known for** | GPU Glossary, Cloud GPU Pricing Guide, Full Stack Deep Learning course, Modal ML infrastructure education |
| **Bio** | Computational neuroscientist turned ML infrastructure educator. PhD from UC Berkeley's Redwood Center for Theoretical Neuroscience. Previously at Weights & Biases building developer tools and documentation. Now at Modal, making GPU programming accessible to a broader audience through educational resources and developer advocacy. |

## Overview

Charles Frye is one of the most effective communicators bridging the gap between cutting-edge ML infrastructure and developer accessibility. With a PhD in computational neuroscience from UC Berkeley's Redwood Center for Theoretical Neuroscience (supported by the NSF Graduate Research Fellowship), Frye brings a scientist's rigor to explaining how GPU-accelerated computing actually works — not just how to invoke it.

Before joining Modal, Frye spent significant time at Weights & Biases, where he wrote documentation, created technical demos and walkthrough videos, and contributed to product development. He also co-instructs the [Full Stack Deep Learning](https://fullstackdeeplearning.com/) course, one of the most respected educational resources for practitioners building and deploying ML systems. The course covers the full pipeline from data preparation and model training to deployment and monitoring, emphasizing engineering fundamentals over theoretical abstraction.

At Modal, Frye has become a leading voice in GPU infrastructure education. His GPU Glossary project — described as a "Rosetta Stone" mapping concepts across the entire GPU programming stack — demystifies the layers of abstraction from raw hardware through CUDA, PTX, and the frameworks developers actually interact with. His Cloud GPU Pricing Guide (co-authored with Sergey Karayev) remains a canonical reference for understanding the economics of training and inference hardware.

## Core Ideas

### GPU Infrastructure as a Developer Accessibility Problem

Frye's central thesis is that GPU programming is unnecessarily inaccessible, and that this inaccessibility slows down the entire AI ecosystem. In his GPU Glossary series at Modal, he systematically maps the layers of GPU computing:

> "The real foundation of NVIDIA's GPU architecture isn't actually CUDA — it's the instruction set architecture called PTX. Understanding this changes how you think about GPU programming at every level above it."

His work emphasizes that developers don't need to be GPU experts to build effective ML systems, but they do need to understand the fundamentals: memory hierarchies, parallel execution models, and the tradeoffs between different hardware configurations.

### Serverless GPUs as the Right Abstraction for ML Workloads

Frye is a strong advocate for Modal's serverless GPU model, where containers spin up on-demand with GPU access and scale back to zero when idle. This contrasts with traditional cloud VMs that require reservation, management, and ongoing cost even when unused.

Key advantages he emphasizes:
- **No idle capacity cost** — you only pay for GPU time you actually use
- **Sub-second cold starts** — Modal's container startup is optimized for ML workloads
- **GPU memory snapshotting** — cuts replica spin-up from minutes to seconds, enabling responsive autoscaling
- **Elastic multi-cloud capacity** — access to GPUs across providers without vendor lock-in

### The ML Engineering Stack Is Evolving Beyond Prompting

Through Full Stack Deep Learning and his public writing, Frye consistently pushes the narrative that effective ML engineering requires deep systems knowledge:

> "LLMs are becoming commodities. Reasoning systems are the moat. You need PyTorch, Transformers, LoRA, vector DBs, and custom inference controllers — not just prompt tweaks. This is systems engineering now."

### Quantization as a Practical Necessity

Frye regularly discusses quantization techniques (INT8, INT4, GGUF) and their real-world impact on model deployment. His work helps developers understand that running large models doesn't always require large GPUs — proper quantization can dramatically reduce hardware requirements while maintaining acceptable quality.

## Key Work

### GPU Glossary (Modal)
A comprehensive resource mapping GPU programming concepts across hardware architectures, instruction sets, and frameworks. The glossary covers CUDA, PTX, Tensor Cores, memory architectures, and the software stacks that sit on top. It has been widely shared in the ML engineering community as a canonical learning resource.

### Cloud GPU Pricing Guide (Full Stack Deep Learning)
Co-authored with Sergey Karayev, this guide tracks pricing across all major cloud GPU providers (AWS, GCP, Azure, Lambda, RunPod, Modal, and others). It includes sortable tables comparing GPUs by architecture, VRAM, vCPUs, memory, and price-per-hour for both server and serverless options.

### Full Stack Deep Learning Course
One of the most popular courses for learning end-to-end ML systems engineering. The curriculum covers:
- Data management and versioning
- Model training and evaluation
- Infrastructure and deployment (including GPU selection)
- Monitoring and observability
- The business and organizational context of ML

### Modal Open Models and Inference Engines
At Modal, Frye has written and presented extensively on running open-source models (Llama, Mistral, Qwen) for production inference, covering:
- Engine initialization and JIT compilation optimization
- GPU memory snapshotting for fast cold starts
- Speculative decoding techniques
- Benchmarking across hardware configurations (A100, H100, L40S, B200)

### Building End-to-End ML Applications on Modal (Video)
A hands-on walkthrough demonstrating fine-tuning a diffusion model and deploying it as a web service on Modal. The video showcases Modal's key differentiators: independent scaling of GPU and CPU components, serverless architecture, and the ability to get interactive shell access to running GPU instances.

## Blog / Recent Posts

- **GPU Glossary (Modal)** — A comprehensive "Rosetta Stone" for GPU programming concepts, mapping the relationship between PTX, CUDA, and higher-level frameworks. Explains why understanding the instruction set architecture matters more than knowing specific framework APIs.
- **What Every LLM Developer Needs to Know About GPUs** (YouTube interview with Latent Space, 2024) — A deep-dive conversation covering GPU hardware architectures, profiling techniques, quantization tradeoffs, and practical guidance for selecting GPUs for different ML workloads.
- **Cloud GPU Pricing Guide** (Full Stack Deep Learning, updated 2023–2024) — Continuously maintained comparison of GPU pricing across providers, with per-GPU and per-hour cost analysis for training and inference scenarios.
- **Modal: Accelerating AI Research** (Modal blog, 2025) — Case studies showing how research teams use Modal's infrastructure for GPU-intensive ML experiments, including KernelBench, TTT-Discover, and RL-4-MLE projects.

## Related People

- **[[sergey-karayev]]** — Co-author of the Cloud GPU Pricing Guide; co-instructor of Full Stack Deep Learning
- **[[hamel-husain]]** — Full Stack Deep Learning co-instructor; co-author of the "What We Learned from a Year of Building with LLMs" series
- **[[eugene-yan]]** — Co-author of the LLMs-in-Production series; Full Stack Deep Learning collaborator
- **[[bryan-bischof]]** — Co-author of "What We Learned from a Year of Building with LLMs" series; fellow Weights & Biases alum
- **Modal Labs** — The cloud infrastructure platform where Frye now works, providing serverless GPU computing for ML workloads
- **Weights & Biases** — Frye's previous employer, the ML experiment tracking platform

## X Activity Themes

- **GPU infrastructure education** — Threads explaining GPU architectures, pricing economics, and deployment strategies
- **Modal platform updates** — New features, case studies, and benchmarks for serverless GPU computing
- **ML engineering best practices** — Practical advice for building, deploying, and monitoring ML systems
- **Full Stack Deep Learning** — Course updates, student success stories, and community engagement
- **Quantization and inference optimization** — Discussion of GGUF, INT8, and other techniques for running models efficiently
- **AI industry analysis** — Commentary on hardware trends, model releases, and the evolving ML infrastructure landscape
