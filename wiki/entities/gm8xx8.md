---
title: "gm8xx8"
handle: "@gm8xx8"
created: 2026-04-10
updated: 2026-04-10
tags: [person, ml-infrastructure, llm-serving, cuda, systems-research]
aliases: ["gm8xx8"]
---

# gm8xx8 (@gm8xx8)

| | |
|---|---|
| **X** | [@gm8xx8](https://x.com/gm8xx8) |
| **GitHub** | [gm8xx8](https://github.com/gm8xx8) |
| **HuggingFace** | [gm8xx8](https://huggingface.co/gm8xx8) |
| **Role** | AI Infrastructure Researcher / Contributor |
| **Known for** | FFT-based attention alternatives, HCache (LLM state restoration), active contributor to cuLA, MiroEval, and multiple ML infrastructure projects |
| **Bio** | AI infrastructure researcher and prolific open-source contributor with ~7K followers on X. Works on efficient LLM serving, alternative attention mechanisms, and GPU-accelerated ML kernels. Known for surfacing cutting-edge systems research papers and providing technical analysis to the AI community. |

## Overview

**gm8xx8** is a prominent voice in the AI infrastructure and systems research community on X (formerly Twitter), with approximately 7,000 followers. While relatively anonymous — operating under a handle with no public personal website or detailed biographical information — gm8xx8 has established themselves as a key connector and analyst in the fast-moving world of ML systems optimization.

Their activity pattern reveals a deep engagement with the intersection of theoretical computer science and practical ML engineering. They regularly surface and analyze papers on topics ranging from attention mechanism alternatives to LLM serving optimization, often providing context and technical breakdowns that help the broader community understand emerging research directions.

gm8xx8's GitHub account shows contributions across a diverse set of ML infrastructure projects, including [inclusionAI/cuLA](https://github.com/InclusionAI/cuLA) (CUDA kernels for linear attention), [MiroMindAI/MiroEval](https://github.com/MiroMindAI/MiroEval), [MiroMindAI/trace-blame](https://github.com/MiroMindAI/trace-blame), and [capgym/cap-x](https://github.com/capgym/cap-x). This breadth of contribution suggests a generalist systems engineer comfortable working across CUDA kernels, evaluation frameworks, and infrastructure tooling.

## Core Ideas

### FFT-Based Attention Alternatives

In February 2025, gm8xx8 drew significant community attention by sharing and analyzing the paper ["The FFT Strikes Back: An Efficient Alternative to Self-Attention"](https://arxiv.org/abs/2502.18394). The tweet received 52K views, 676 likes, and 72 reposts, sparking a vigorous technical discussion.

The paper explores using Fast Fourier Transforms to replace the quadratic-complexity self-attention mechanism in transformers. The core insight: instead of computing correlations in the time domain, transform inputs to the frequency domain, multiply there, and transform back — reducing complexity from O(n²) to O(n log n).

gm8xx8's analysis prompted debate in the replies:

- **@MrCatid** questioned reproducibility, noting this echoes the earlier FNet (2021) approach
- Community members discussed the mechanics: *"Instead of convolution or correlation of x and y in time domain, first Fourier transform x and y into X and Y, then multiply X and Y in Fourier domain, then [inverse transform]."*
- **@SergioGaitanC** drew parallels to Stable Diffusion's breakthrough: *"Physics strikes back, same as it did with stable diffusion."*

### LLM State Restoration via HCache

gm8xx8 also amplified research on [HCache](https://arxiv.org/abs/2410.05004) — Fast State Restoration in LLM Serving by Shiwei Gao, Youmin Chen, and Jiwu Shu from Tsinghua University. The paper proposes using intermediate activations to restore LLM contextual states (KV cache) rather than recomputing from tokens or offloading to host storage.

Key results from the paper that gm8xx8's community discussed:
- **1.93× reduction in Time To First Token (TTFT)** compared to KV offloading
- **5.73× speedup** compared to token recomputation
- **1.92-2.40× less storage space** than conventional KV cache offload

### Linear Attention and CUDA Kernel Optimization

Through their contributions to [cuLA](https://github.com/InclusionAI/cuLA), gm8xx8 engages with the frontier of linear-time attention implementations. This project targets NVIDIA Blackwell (SM10X) and Hopper (SM90) GPUs with hand-tuned CUDA kernels for linear attention variants, including KDA (Kernelized Delta Attention) and Lightning attention patterns.

## Key Work

### GitHub Contributions

gm8xx8 has been an active contributor to the following projects (as of early 2026):

| Project | Organization | Description |
|---|---|---|
| [cuLA](https://github.com/InclusionAI/cuLA) | InclusionAI | CUDA kernels for linear attention (CuTe DSL, CUTLASS C++); targeting Blackwell/Hopper GPUs |
| [MiroEval](https://github.com/MiroMindAI/MiroEval) | MiroMind AI | Evaluation framework for AI models |
| [trace-blame](https://github.com/MiroMindAI/trace-blame) | MiroMind AI | Tracing and debugging tooling for ML pipelines |
| [MyPhoneBench](https://github.com/FreedomIntelligence/MyPhoneBench) | FreedomIntelligence | Mobile device AI benchmarking |
| [cap-x](https://github.com/capgym/cap-x) | CapGym | Gym/capacity testing for AI systems |
| [GLM-skills](https://github.com/zai-org/GLM-skills) | ZAI Organization | Skills framework for GLM models |
| [DIAL](https://github.com/xpeng-robotics/DIAL) | XPeng Robotics | Dialogue and interaction learning for robotics |
| [Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | PrismML Engineering | Demo infrastructure |

### Research Amplification

gm8xx8 serves as a critical node in the ML research information network:

1. **FFT Attention paper** (arXiv:2502.18394) — Sparked discussion on frequency-domain computation for transformers
2. **HCache paper** (arXiv:2410.05004) — Highlighted novel approaches to KV cache management
3. **FNet follow-up** — Contextualized new FFT work within the broader attention optimization landscape

## Blog / Recent Posts

gm8xx8 does not maintain a personal blog, but their X posts serve as a de facto research digest for the ML systems community. Notable recent posts include:

| Approx. Date | Topic | Engagement |
|---|---|---|
| Feb 2025 | "The FFT Strikes Back: An Efficient Alternative to Self-Attention" — sharing arXiv:2502.18394 | 52K views, 676 likes |
| Sep 2025 | HCache paper discussion — arXiv:2410.05004 on fast state restoration for LLM serving | 553 likes |
| Ongoing | Technical breakdowns of CUDA kernel optimization, attention variants, and LLM serving systems | Consistent high engagement |
| Various | CXL (Compute Express Link) and memory system innovations | Active discussion participant |

## Related People

- **[xjdr](./xjdr.md)** — Also works on inference optimization; gm8xx8's interest in attention efficiency complements xjdr's Entropix work
- **[Grad](./grad.md)** — Both contribute to the broader ML efficiency/speedrun community
- **[Shiwei Gao, Youmin Chen, Jiwu Shu](https://arxiv.org/abs/2410.05004)** — Tsinghua HCache authors whose work gm8xx8 amplified
- **[@karpathy](https://x.com/karpathy)** — gm8xx8 engages with the llm.c / modded-nanogpt ecosystem
- **[@MrCatid](https://x.com/MrCatid)** — Frequent interlocutor on technical analysis of attention papers
- **Keller Jordan** — Modded-nanogpt speedrun; shares the ML efficiency community
- **@fernbear.bsky.social** — Contributor to the NanoGPT speedrun; related optimization community

## X Activity Themes

- **Attention mechanism research** — FFT-based alternatives, linear attention, kernelized attention
- **LLM serving optimization** — KV cache management, state restoration, inference efficiency
- **CUDA/GPU programming** — Kernel optimization, Blackwell/Hopper architectures, CuTe DSL
- **Paper amplification and analysis** — Surfacing arXiv papers with technical context and discussion prompts
- **Memory systems and interconnects** — CXL, storage I/O, computational vs. I/O bottlenecks
- **ML infrastructure projects** — Active contributions to open-source tooling for model serving and evaluation
- **Community technical discussion** — Engages in detailed debates about reproducibility, novelty, and practical impact of research
