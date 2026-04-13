---
title: "Google Gemma 4"
created: 2026-04-10
updated: 2026-04-13
tags: [entity, model, google, open-weight, gemma]
related: [google-deepmind, open-models, on-device-ai]
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

## MoE Expert Routing Visualization

Martin Alderson (martinalderson.com) built an interactive visualization tool for MoE expert routing patterns using Gemma 4 26B: [moe-viz.martinalderson.com](https://moe-viz.martinalderson.com)

Key findings:
- **~25% of experts never activate** for any given short prompt
- The dormant 25% **varies by prompt** — different prompts activate different expert subsets
- Built by modifying llama.cpp to output profiling data, with Claude Code assistance
- Demonstrates the **dynamic and unpredictable** nature of MoE routing

Inference insight: Gemma 4 26B's small parameter count makes it practical for "CPU MoE" inference — loading certain experts on CPU while keeping KV cache on GPU. This suggests a path toward more efficient local MoE deployments where expert caching strategies could optimize the ~25% dormancy rate.

## Sources
- [[raw/articles/blog.google--innovation-and-ai-technology-developers-tools-gemma-4--9648c97b.md]]
- [[raw/articles/huggingface.co--google-gemma-4-e4b--b37a0ece.md]]
- Google DeepMind announcement
- Martin Alderson, "A little tool to visualise MoE expert routing," martinalderson.com (April 13, 2026)
