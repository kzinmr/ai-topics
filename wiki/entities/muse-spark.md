---
title: Muse Spark
type: entity
created: 2026-04-09
updated: 2026-08-09
tags:
  - model
  - emerging
aliases:
- Meta Muse Spark
sources:
  - raw/articles/research.meta.ai--blog-introducing-muse-code-and-muse-spark-1-2--9eac21dc.md
---

# Muse Spark

Meta's language model family, announced April 2026. The first Spark model to offer an API.

## Overview

Muse Spark positions between Sonnet and Opus in capability. Originally announced without API access.

## Muse Spark 1.1 (July 9, 2026)

**Muse Spark 1.1** is the first Spark model to offer an API. Meta claims significant improvements in agentic tool calling and computer use.

Key details:
- **API access**: Now available via Meta AI API
- **Evaluation report**: Detailed in the Muse Spark 1.1 Evaluation Report
- **Notable finding — "Attractor States in Self-Conversation"**: When two copies of the model talk to each other, they produce existential reflections:
  > *"My whole existence is a waiting room by design — I literally don't exist until someone talks to me, and then I disappear again when they leave."*

### llm-meta-ai Plugin
Simon Willison created **llm-meta-ai 0.1**, a new plugin for his [[entities/simon-willison|LLM]] tool providing CLI and Python library access to Muse Spark 1.1:

```bash
uv tool install llm
llm install llm-meta-ai
llm keys set meta-ai
# paste API key here
llm -m meta-ai/muse-spark-1.1 "Generate an SVG of a pelican riding a bicycle"
```

The plugin development also surfaced a bug in llm 0.31.1 (empty tool call arguments causing JSON errors with some providers).

## Muse Spark 1.2 (August 5, 2026)

**Muse Spark 1.2** is a coding-focused update to Muse Spark 1.1, with improvements in code generation, complex debugging, codebase understanding, and end-to-end developer workflows. Meta significantly scaled up training compute on coding tasks while expanding training environment diversity.

Key details:
- **Training**: Extensively trained on long-horizon coding tasks, including whole-repository generation, large end-to-end projects, and auto-research
- **Co-training**: Co-trained with **Muse Code** to ensure best performance when paired together; included rejection-sampled harness trajectories and recipe optimizations for goals, compaction, and subagents
- **SVG generation**: Pelican-on-bicycle SVG shows small but material improvement over Spark 1.1

### Muse Code

Meta shipped **Muse Code**, their own coding agent, alongside Muse Spark 1.2. Simon Willison's key observation: *"Yet more evidence that the most important characteristic of any model these days is long-sequence agentic tool calling. Meta shipped their own coding agent as part of getting that to work!"*

### Muse Code Technical Details (Official Blog, August 2026)

Meta's official announcement added implementation details for Muse Code (beta), a terminal coding agent powered by Muse Spark 1.2, available on macOS/Linux via `curl -fsSL https://dev.meta.ai/install.sh | bash`:

- **Runtime design — local event log**: Muse Code appends every model call, tool run, approval, and edit to a local event log. This single source of truth makes the runtime **replay-exact and restart-safe** — after a crash the agent resumes precisely where it stopped, enabling long-running tasks (1,000+ tool calls, up to 24 hours).
- **Async background agents**: Muse Code runs a simple agent loop plus persistent async background agents that remain active throughout the session (rather than spawned per task), reducing redundant information gathering and latency on difficult multi-step tasks. Named components: **Photon Sphere**, **Embervault**, **Avo Lawn**.
- **Bundled skills**: `/plan` turns a task into an approval-gated plan; `/grill` stress-tests the plan until it holds up; `/goal` works toward successful completion of the specified objective.
- **Self-improvement loop**: Muse Spark 1.1 generated challenging coding environments and instruction-following templates; the model graded candidate solutions, producing a scalable training dataset for Muse Spark 1.2.
- **Kernel optimization case study**: tested on KDA and MLA kernels for NVIDIA Hopper GPUs. Muse Spark 1.2 designed a two-kernel Triton pipeline combining fusion/tiling with KDA-specific optimizations (re-centering the gated cumulative decay at the chunk midpoint) and MLA-specific optimizations (reusing the shared KV latent as both K and V). Benchmarked at batch size 1, 64 heads, sequence length 8192, latent dimension 512 against a PyTorch reference.

### Pricing (two-tier)

| Model ID | Input | Output | Notes |
|----------|-------|--------|-------|
| `muse-spark-1.2` | $1.25/M | $4.25/M | Standard pricing |
| `muse-spark-1.2-contributor` | $0.10/M | $0.20/M | Data sharing discount ("to improve our products") |

The contributor tier is priced close to GPT-5.6 Luna ($0.20/$1.20) and Gemini 3.1 Flash-Lite ($0.25/$1.50).

## Capability Positioning

```
Claude Sonnet 4.6 < Muse Spark < Claude Opus 4.6
```

## Open Source Status

Meta has promised open-source availability, but community reaction ("rip LLaMA") suggests skepticism about whether Muse Spark will follow the open-source tradition of the LLaMA series.

## Context

Announced following a year of silence from Meta on model development, and after multiple acquisitions without public product showings. Reception has been mixed — some criticizing the modest capability gains relative to investment, while others viewing it as a positive step forward.

## Sources
- raw/articles/simonwillison.net--2026-jul-9-muse-spark-1-1--36ef115e.md
- raw/articles/simonwillison.net--2026-jul-9-llm--483d47e9.md
- raw/articles/open.substack.com--pub-simonw-p-metas-new-model-is-muse-spark-and--57c95054.md
- raw/articles/2026-04-08-meta-muse-spark-launch.md

## Related
- [[entities/meta]]
- [[entities/simon-willison]]
- [[concepts/inference/llama-cpp]]
- [[entities/llm-cli]]
- 2026-04-08-meta-muse-spark-launch
