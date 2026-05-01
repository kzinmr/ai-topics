---
title: Google Gemma 4
type: entity
created: 2026-04-10
updated: 2026-04-13
tags:
- entity
- model
- google
- open-weight
- gemma
related:
- google-deepmind
- open-models
- on-device-ai
sources: []
---

# Google Gemma 4

Family of open-weight models (Apache 2.0) from Google DeepMind designed for on-device frontier intelligence.

## Model Specifications

| Model | Type | Parameters | Use Case |
|-------|------|------------|----------|
| Gemma 4 26B | MoE | 26 billion | Advanced reasoning, agentic workflows |
| Gemma 4 31B | Dense | 31 billion | High-performance local deployment |

## Key Capabilities

### On-Device Frontier Intelligence
- Optimized for phones, laptops, desktops
- Matches/exceeds larger cloud models
- Reduces latency, enables private offline deployments

### Agentic Workflow Support
- Multi-step tool use
- Function calling
- Structured output generation
- Reliable local execution for agent pipelines

### Licensing & Availability
- Apache 2.0 license (no usage restrictions)
- Commercial deployment enabled
- Fine-tuning permitted
- Available on Kaggle, Hugging Face, Google AI Studio

## Strategic Importance
- Democratizes frontier AI capabilities
- Enables local agent deployments without cloud dependency
- Competitive response to proprietary models
- Part of Google's open model strategy
- Apache 2.0 licensing removes barriers compared to Meta's restrictive Llama license

## What Makes an Open Model Succeed

Analysis by Nathan Lambert (Interconnects.ai, April 2026) identifies key success factors:

### The Crowded Open Model Landscape (2026)
Gemma 4 competes with: Qwen 3.5, Kimi K2.5, GLM 5, MiniMax M2.5, GPT-OSS, Arcee Large, Nemotron 3, OLMo 3, and more. The space is "populated but full of hidden opportunity."

### Key Success Factors
1. **Licensing simplicity** — Apache 2.0 (Gemma) removes barriers vs. restrictive licenses (Llama)
2. **Ecosystem support** — Models need community, tooling, and documentation
3. **Release cadence** — Regular updates maintain mindshare
4. **Per-model impact** — GPT-OSS shows that 2 exceptional models can outsell 20 mediocre ones

### The "Dark Matter" Potential
> *"The potential of open models feels like a dark matter, a potential we know is huge, but few clear recipes and examples for how to unlock it are out there."*
> — Nathan Lambert, April 2026

Agentic AI, OpenClaw, and similar tools will "spur mass experimentation in open models to complement the likes of Claude and Codex, not replace them."

### Benchmarks Are Incomplete
For open models especially, benchmarks at release tell an incomplete story. New open models have "much higher variance and ability to surprise" — spending a few hours in agentic workflows reveals more than benchmark scores.

### Gemma 4's Position
- Apache 2.0 license positions it well against Llama's restrictions
- MoE architecture (26B) enables efficient local deployment
- Strong tool use and structured output support makes it agent-ready
- Small enough for CPU inference with strategic expert loading

## MoE Expert Routing Visualization

Martin Alderson (martinalderson.com) built an interactive visualization tool for MoE expert routing patterns using Gemma 4 26B A4B: [moe-viz.martinalderson.com](https://moe-viz.martinalderson.com)

Key findings:
- **~25% of experts never activate** for any given short prompt
- The dormant 25% **varies by prompt** — different prompts activate different expert subsets
- Built by modifying llama.cpp to output profiling data, with Claude Code assistance
- Demonstrates the **dynamic and unpredictable** nature of MoE routing

Inference insight: Gemma 4 26B's small parameter count makes it practical for "CPU MoE" inference — loading certain experts on CPU while keeping KV cache on GPU. This suggests a path toward more efficient local MoE deployments where expert caching strategies could optimize the ~25% dormancy rate.

## Local Coding Agent Integration (pi, 2026-04)

The article at patloeber.com documents a practical setup for running **pi** (Mario Zechner's minimal coding agent) with Gemma 4 26B A4B via LM Studio:

- **Model:** Gemma 4 26B A4B (MoE) — 26B total params, only 4B activate per token
- **Provider:** LM Studio at `http://localhost:1234/v1`
- **VRAM:** ~18GB for Q4_K_M (all 26B must be loaded despite MoE routing)
- **Context:** Up to 256K tokens; recommended 128K if VRAM allows
- **Install:** `npm install -g @mariozechner/pi-coding-agent`
- **Config:** Point `~/.pi/agent/models.json` to LM Studio's base URL

**Key architectural note:** *"Even though the model only activates 4B parameters per token, all 26B parameters must be loaded into memory for fast routing. That's why VRAM requirements are closer to a dense 26B model."*

## Context vs. VRAM Tradeoff

| Use Case | Context | Additional VRAM |
|----------|---------|-----------------|
| Small edits | 16K | ~1 GB |
| Standard coding | 64K | ~4 GB |
| Multi-file refactors | 128K | ~8 GB |
| Full repo context | 256K | ~16 GB |

|The article emphasizes the tradeoff between context size and VRAM overhead. Coding agents accumulate heavy session context, making larger contexts highly beneficial for multi-file refactors and full repo understanding.

## Sources
|- 
|- 
|- Google DeepMind announcement
|- Martin Alderson, "A little tool to visualise MoE expert routing," martinalderson.com (April 13, 2026)
|- Patrick Loeber, "How to run a local coding agent with Gemma 4 and Pi," patloeber.com (Apr 2026)

## See Also

- [[pi-coding-agent]] — Minimal coding agent by Mario Zechner that runs with Gemma 4 via LM Studio.
- [[mistral-ai]] — Competing open-weight model provider with Mistral Medium 3.5.
- [[open-models]] — Open-weight model ecosystem and licensing landscape.
- [[coding-agents]] — AI agents for software engineering tasks.
- [[lmstudio]] — Local model serving tool for running Gemma 4 on consumer hardware.
