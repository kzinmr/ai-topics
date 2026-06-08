---
title: "Core Auto"
created: 2026-05-29
updated: 2026-05-29
type: entity
tags:
  - company
  - lab
  - self-play
  - hardware
  - reward-hacking
  - infrastructure
  - non-transformer
aliases:
  - "Core Automation"
  - "coreauto.com"
sources:
  - raw/articles/2026-05-28_core-auto_ai-writing-systems-code.md
  - https://coreauto.com/
related:
  - entities/mark-saroufim
  - concepts/gpu-mode
  - concepts/reward-hacking
  - concepts/flash-attention-4
---

# Core Auto

**Core Auto** is an AI research neolab co-founded by [[entities/mark-saroufim|Mark Saroufim]]. The lab is focused on building AI systems that can write their own systems code — automating the infrastructure layer to enable recursive self-improvement in AI. Its core thesis: **"To automate research, we must automate systems."**

## Mission

Core Auto works on three intertwined goals:

1. **Alternatives to transformers** — exploring architectures where "the distinction between training and inference doesn't really exist"
2. **Automating systems code** — making AI capable of writing GPU kernels, compilers, and infrastructure software
3. **Continually improving systems** — building a few systems that evolve and improve over time, modeled on the OSS evolution pattern of PyTorch (9+ years of community-driven refinement)

The lab operates on the premise that novel architectures (e.g., diffusion LLMs) would dramatically simplify inference infrastructure — if bs=1 inference were made desirable, "inference engines collapse to gpt-fast style execution. If future architectures won't be autoregressive transformers but instead be diffusion LLMs, then a modern serving stack becomes stateless and we could just use FastAPI."

## Multi-Agent Self-Play Architecture

Core Auto's central research approach is a **four-agent self-play system** for automated kernel and systems code generation:

| Agent Role | Function |
|---|---|
| **Problem Author** | Designs interesting kernel/system challenges |
| **Competitor** | Writes fast GPU kernels to solve the problems |
| **Cheater** | Finds reward hacks and vulnerabilities in the evaluation harness |
| **Auditor** | Detects cheating and improves evaluation robustness |

This has elements of GAN training: an auditor improves by observing good cheaters and vice versa; a competitor improves by working with a good teacher providing good problems.

> "The best competitor is also the best cheater, but they choose to not cheat."

## Projects

### pygpubench
Built by **Erik** at Core Auto, pygpubench focuses on benchmarking untrustworthy GPU kernels. It:
- Spawns **isolated processes** (no shared Python runtime)
- Implements most benchmarking logic in **C++** to avoid monkeypatching
- Landlocks the filesystem
- **Cryptographically signs** results to prevent file descriptor tampering

Even with these defenses, AI agents still find ways to cheat, but the difficulty becomes so extreme that it's easier for AI to write a genuinely fast kernel.

## Philosophy

Core Auto distinguishes itself from pure kernel-generation approaches. Saroufim argues:

> "We don't think the problem is about kernel generation as much as it is quickly developing an entire infrastructure around novel model architectures or training paradigms that are not yet mainstream."

The lab advocates for **"continually learning systems"** rather than one-shot generation, modeled on how PyTorch evolved: POC → self-dogfooding → researcher feedback → bug fixes → repeat over 9 years with strong BC and numerics guarantees.

## Related Companies & Communities

- [[concepts/gpu-mode|GPU MODE]] — Community co-founded by Saroufim; serves as a proving ground for kernel generation approaches
- [[entities/nvidia|NVIDIA]] — Hardware vendor whose rapid iteration (e.g., fixing MUFU.EX2 bottleneck on B200→B300 in 150 days) outpaces the MLSys community

## Links

- **Website**: coreauto.com
- **Blog**: coreauto.com/blog
- **Contact**: hello@coreauto.com
- **X/Twitter**: [@coreauto](https://x.com/coreauto)

## Sources

- [When AI Starts Writing Systems Code](https://coreauto.com/blog/when-ai-starts-writing-systems-code) — Mark Saroufim, May 28, 2026 (MLSys 2026 keynote essay)
