---
title: "Spike (Mike Doan)"
tags: [training, ai-agents, llm, entity, rag, inference]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Spike (Mike Doan)

**URL:** https://supaiku.com
**Blog:** supaiku.com
**Twitter/X:** @spikedoanz
**GitHub:** spikedoanz
**Role:** Independent ML researcher; formerly at a math/ASI lab
**Projects:** BrainChop (tinygrad-based brain segmentation), from-bits-to-intelligence, weenygrad, tensor-tic-tac-toe

## Overview

Spike (real name: Mike Doan) is an independent machine learning researcher and systems programmer with a distinctive perspective on the foundations of AI computation. He previously worked at a math/ASI (Artificial Superintelligence) lab and now conducts independent research spanning mathematics, programming language theory, and machine learning systems.

Spike's work is characterized by a relentless focus on minimalism and understanding from first principles. His most prominent project, "from bits to intelligence," asks a provocative question: could we build the entire ML stack in 100,000 lines of code? The project maps out a complete stack from Verilog hardware design through C compiler, Python runtime, OS, tensor library, autograd, and a GPT-2 implementation — all in ~65K lines of code. This is not a toy exercise but a serious intellectual project about the relationship between code volume, interpretability, and understanding.

His other notable projects include BrainChop (a portable, lightweight brain segmentation tool built on tinygrad with 865+ GitHub stars on his dingllm.nvim project), weenygrad (a minimalist vector autograd implementation), and tensor-tic-tac-toe (parallelized hyperdimensional tic-tac-toe).

Spike's blog at supaiku.com publishes provocative, philosophically-rich technical essays that blend systems thinking with abstract reasoning. His recent posts include "attention is logarithmic" (a work-depth analysis challenging conventional time complexity thinking for parallel ML systems), "Towards a Time Theory of Money" (an economic framework), and "on llm agents" (a perspective on the trajectory of AI agent development).

His intellectual style is distinctive: concise, often aphoristic ("spikisms"), with a willingness to challenge conventional wisdom about what's important in ML systems design. He has a strong bias toward pragmatism and understanding over abstraction and tooling.

## Timeline

| Date | Event |
|------|-------|
| ~2022 | Joined GitHub (@spikedoanz); begins publishing code and essays |
| 2023 (Oct) | Released "talk" — a TypeScript project for making sand talk (588 GitHub stars) |
| 2024 (Feb) | Released weenygrad — minimalist vector autograd in Python (11 stars) |
| 2024 (May) | Published "taking back the web" — essay on web autonomy and self-hosting |
| 2024 (Jun) | Released brainchop — portable brain segmentation using tinygrad (PyPI package) |
| 2024 (Jun) | Released llm.nvim — no-frills LLM-assisted programming in Neovim (24 stars) |
| 2024 (Jul) | Published "from bits to intelligence" — the 100K line ML stack proposal (46 stars) |
| 2024 (Aug) | Released brainchop 0.1.24 on PyPI with WebGPU model export support |
| 2024 (Aug) | Published "spikisms" — collection of aphoristic technical insights |
| 2025 (Mar) | Published "attention is logarithmic" — work-depth analysis of transformer attention |
| 2025 (Aug) | Published "on becoming a computer" — philosophical essay on computational identity |
| 2025 (Oct) | Published "on llm agents" — perspective on the trajectory of AI agent development |
| 2025 (Dec) | Published "what does a lean proof prove" — mathematics and formal verification |
| 2026 (Jan) | Published "Towards a Time Theory of Money" — economic framework essay |
| 2026 (Feb) | Published "how i self hosted zulip and escaped the permanent underclass" — practical self-hosting guide |
| 2026 (Feb) | Last blog update: 2026-02-25 |

## Core Ideas

### The 100K Line ML Stack

Spike's most influential intellectual project is "from bits to intelligence" — a proposal to build the entire machine learning stack in approximately 65,000–100,000 lines of code, from hardware to trained model. The mapping:

| Layer | Component | Lines | Language |
|---|---|---|---|
| Hardware | GPU/DSP chip | ~1,000 | Verilog |
| Hardware | CPU chip | ~1,500 | Verilog |
| Hardware | MMU | ~1,000 | Verilog |
| Hardware | SD card driver | ~150 | Verilog |
| Software | C compiler | ~2,000 | Python |
| Software | Python runtime | ~50,000 | C |
| Software | OS | ~2,500 | C |
| Software | File system (FAT) | ~300 | C |
| Software | User space tools | ~500 | C |
| ML | Tensor library | ~500 | Python |
| ML | Autograd | ~5,000 | Python |
| ML | Data processing | ~500 | Python |
| ML | GPT-2 | ~500 | Python |

The default stack for training GPT-2 runs on PyTorch (2.3M lines) → Python (1.7M lines) → GCC (10M lines) → Linux (28.8M lines) → CUDA kernels → proprietary GPU drivers. Spike's proposal reduces this to a factor of ~100 fewer lines of code. The goal is not raw performance but interpretability — a stack that a single person could understand, modify, and verify.

### Attention Is Logarithmic

In "attention is logarithmic" (March 2025), Spike challenges the conventional wisdom that transformer attention has O(n²) complexity. Using work-depth analysis (a model better suited for parallel computation than traditional time complexity), he argues that vanilla attention should be considered O(log n + log d) in computational depth, where n is sequence length and d is embedding dimension.

The key insight: through sequential composition of matrix multiplications, contractions, and elementwise operations, attention has asymptotic depth complexity of just O(log n + log d). The practical limitation isn't the computation but memory — materializing the QK^T matrix overflows L2 cache, forcing memory-bound computation at O(n log n).

This has implications for future chip design: if training paradigms remain largely non-concurrent, the bottleneck is memory bandwidth, not compute. Spike speculates that moving weights onto faster memory (L2 cache) could unlock the theoretical logarithmic scaling.

### From Bits to Intelligence: Co-Recursion and Self-Hosting

Spike's projects demonstrate a fascination with bootstrapping — building systems that can build themselves. His C compiler in Python can host the C runtime that compiled it. His tensor library in Python can be lazily compiled down to RISC-V assembly that the hardware can execute. This recursive self-reference isn't just clever — it's a statement about the nature of computation and intelligence.

The "from bits to intelligence" repository asks: at what point does a collection of transistors become capable of learning? The answer isn't in any single layer but in the composition — each layer is simple enough to understand, but together they produce something that can model language, recognize images, and generate text.

### Minimalism as Epistemology

Spike's work is driven by a philosophical commitment to minimalism. His projects are deliberately small and hackable:

- **dingllm.nvim** (865 stars): A lightweight Neovim config for LLM-assisted programming. "I will be pushing breaking changes. I recommend reading the code and copying it over."
- **weenygrad** (11 stars): A minimalist vector autograd implementation — not a full ML framework, just the core computation engine.
- **tensor-tic-tac-toe** (127 stars): Parallelized hyperdimensional tic-tac-toe — a toy that demonstrates serious computational concepts.
- **just-large-models** (44 stars): "Just large language models. Hackable, with as little abstraction as possible. Done for my own purposes, feel free to rip."

The ethos is clear: code should be small enough to fit in your head. Abstraction is a tool, not a goal. If you can't understand it, you don't control it.

### AI Engineering as Stochastic Software Development

Spike has written about the nature of AI engineering as distinct from traditional software development. In a world where models produce non-deterministic outputs and their internal representations are opaque, the engineering challenge shifts from writing correct code to managing uncertainty and building systems that can tolerate and exploit stochastic behavior.

This connects to his broader philosophy: the best systems are those where you understand every layer, from the transistor to the output. When you're working with stochastic models, that understanding becomes even more critical — you need to know where the randomness comes from and how it propagates through your system.

### The "Spikisms" Tradition

Spike's "spikisms" are aphoristic technical insights that blend computational thinking with philosophical observation. They represent a tradition of concise, memorable technical wisdom — similar in spirit to the Zen of Python or Dijkstra's observations, but grounded in the practical realities of modern ML systems.

## Key Quotes

> "I will be pushing breaking changes. I recommend reading the code and copying it over."

> "Just large language models. Hackable, with as little abstraction as possible. Done for my own purposes, feel free to rip."

> "Time complexity is a very bad model when working with parallelism."

> "Instead of letting RAM fill until the process crashes, each thread return is a natural opportunity to decide what gets retained, what gets compressed, and what gets discarded."

> "The best systems are those where you understand every layer, from the transistor to the output."

## Related Wikilinks

- [[concepts/ml-systems]] — Spike's domain of expertise: building minimal, interpretable ML stacks
- [[concepts/transformer-architecture]] — The "attention is logarithmic" analysis of attention complexity
- [[concepts/tinygrad]] — The ML inference engine used in BrainChop
- [[concepts/brainchop]] — His portable brain segmentation tool
- [[concepts/work-depth-analysis]] — The computational complexity model Spike advocates for parallel systems
- [[concepts/software-minimalism]] — The philosophical commitment to small, readable code
-  — His llm.nvim project and views on AI in programming
-  — The instruction set architecture used in the 100K line ML stack proposal
-  — The concept of systems that can build themselves
## Influence Metrics

- BrainChop (dingllm.nvim): 865+ GitHub stars, active PyPI package with WebGPU export
- "from bits to intelligence": 46 stars, widely referenced in ML minimalism discussions
- "talk" project: 588 stars, creative intersection of code and art
- Regular contributor to tinygrad ecosystem and neuroneural/brainchop projects
- Active presence on X (@spikedoanz) with philosophical technical commentary
- His "attention is logarithmic" essay has been cited in discussions about efficient attention mechanisms
- Weenygrad: minimalist autograd implementation (11 stars)

## Sources

- [supaiku.com](https://supaiku.com/) — Personal blog
- [spikedoanz GitHub](https://github.com/spikedoanz) — Code and projects (117 followers, 93 public repos)
- [from-bits-to-intelligence](https://github.com/spikedoanz/from-bits-to-intelligence) — The 100K line ML stack proposal
- [BrainChop PyPI](https://pypi.org/project/brainchop/0.1.24/) — Package details and author attribution (Mike Doan)
- [dingllm.nvim](https://github.com/yacineMTB/dingllm.nvim) — Forked from llm.nvim, 865 stars
- [attention is logarithmic](https://supaiku.com/attention-is-logarithmic) — Technical essay on work-depth analysis
- [weenygrad](https://github.com/spikedoanz/weenygrad) — Minimalist vector autograd
- [tensor-tic-tac-toe](https://github.com/spikedoanz/tensor-tic-tac-toe) — Parallelized hyperdimensional tic-tac-toe
