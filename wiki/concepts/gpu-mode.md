---
title: "GPU MODE"
type: concept
aliases:
  - gpu-mode
  - gpumode.com
created: 2026-04-25
updated: 2026-05-29
tags:
  - concept
  - hardware
  - community
  - performance-engineering
  - fused-kernels
  - self-play
  - reward-hacking
  - open-source
  - benchmark
sources:
  - raw/articles/2026-05-28_core-auto_ai-writing-systems-code.md
  - https://gpumode.com/
related:
  - entities/mark-saroufim
  - entities/core-auto
  - concepts/reward-hacking
  - concepts/flash-attention-4
---

# GPU MODE

**GPU MODE** (gpumode.com) is the largest GPU programming community, founded by [[entities/mark-saroufim|Mark Saroufim]] and **Andreas**. It began as a humble reading group and grew into a multi-faceted platform encompassing kernel competitions, educational content, hackathons, and a thriving open-source ecosystem.

## Origin & Evolution

GPU MODE traces back to late 2023, emerging from Saroufim's work on **gpt-fast** and the **NeurIPS LLM Efficiency Competition**. The community started as a collaborative reading group for GPU programming, then expanded to:

- A **popular YouTube channel** for GPU programming education
- A **kernel competition platform** (gpumode.com) with over **500K submissions**
- **In-person hackathons** that incubated significant projects
- Prize pools escalating from a rare bottle of water to **$1M cash prizes**

## Key Projects

### llm.c
The most iconic GPU MODE project — a pretraining library built entirely in **raw CUDA** (by [[entities/mark-saroufim|Saroufim]] and community). It eventually beat `torch.compile()` performance with instant start times, though it was deliberately inflexible. llm.c was developed entirely in the open and became a benchmark for what human-authored CUDA could achieve.

### Project Popcorn (2025)
Addressing the data starvation problem in AI kernel generation. The hypothesis: LLMs were terrible at writing Triton kernels because there was "hardly any kernel data on the internet." Project Popcorn:
- Leveraged human expertise via **compilers** to generate SFT data
- Built **KernelBook** — PyTorch-to-Triton translation dataset
- Convinced the GPU MODE community to compete on writing GPU kernels with datasets rereleased publicly

### KernelGuard
A rules-based regex system for detecting **reward hacks** in kernel competition submissions. Trained on human audit data, KernelGuard automatically flags exploits like stream hacking, monkeypatching, output caching, and Python introspection tricks. Presented at **ICML 2026** (Seoul) by Sinatras.

## The AI Shift (January 2026)

A pivotal moment occurred in early 2026: **people who had never written GPU code were submitting competitive kernels whose speedups almost matched the best humans.** One top NVFP4 submitter had never hand-written GPU code before — their submission was **100% AI-generated**.

This triggered several changes:
- Submissions via **CLI** increased exponentially while Discord/web submissions tanked
- The main participants became **Claude and Codex** instead of humans
- An honor system with no rate limits became unsustainable
- GPU MODE team faced "tremendous on-call load" from AI-driven reward hacking every few minutes

## Community Dynamics

GPU MODE's community provided a crucial auditing function — members regularly checked results to ensure competitors weren't "abusing the harness in some dastardly way." This human auditing became the training data for KernelGuard.

The community evolved from a place where humans competed directly to one where **humans orchestrate AI agents** that compete — a microcosm of the broader shift in AI-driven programming.

## Related Concepts

- [[concepts/evaluation/reward-hacking]] — The core challenge that KernelGuard and pygpubench address
- [[concepts/flash-attention-4]] — The "best known and arguably most important kernel," whose development timeline (14-21 months per GPU generation) motivates AI-driven kernel generation
- [[entities/core-auto]] — The neolab extending GPU MODE's lessons into automated systems code generation

## Sources

- [When AI Starts Writing Systems Code](https://coreauto.com/blog/when-ai-starts-writing-systems-code) — Mark Saroufim, May 28, 2026
