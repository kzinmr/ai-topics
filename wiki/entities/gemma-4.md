---
title: Google Gemma 4
type: entity
created: 2026-04-10
updated: 2026-06-09
tags:
  - entity
  - model
  - google
  - open-weight
  - inference
  - mtp
- entity
- model
- google
- open-weight
- gemma
- speculative-decoding
- mtp
related:
- google-deepmind
- open-models
- on-device-ai
- speculative-decoding
sources:
- raw/articles/2026-05-05_google-gemma-4-multi-token-prediction-drafters.md
- raw/articles/2026-06-07_xeophon_gemma-4-e4b-daily-local-model.md
- https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/
- https://huggingface.co/google/gemma-4-E4B-it
- https://huggingface.co/lmstudio-community/gemma-4-E4B-it-GGUF
- https://huggingface.co/google/gemma-4-12B-it
- https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf
- https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12B/
---

# Google Gemma 4

Family of open-weight models (Apache 2.0) from Google DeepMind designed for on-device frontier intelligence.

## Model Specifications

| Model | Architecture | Parameters | Context | Modalities | Use Case |
|-------|-------------|------------|---------|------------|----------|
| Gemma 4 E2B | Dense + PLE | 2.3B effective (5.1B w/ embeddings) | 128K | Text, Image, Audio | On-device / mobile |
| Gemma 4 E4B | Dense + PLE | 4.5B effective (8B w/ embeddings) | 128K | Text, Image, Audio | On-device / laptop daily driver |
| Gemma 4 12B Unified | Dense (encoder-free) | 11.95B | 256K | Text, Image, Audio | Consumer GPU / local multimodal |
| Gemma 4 26B A4B | MoE | 25.2B total (3.8B active) | 256K | Text, Image | Local coding / agentic workflows |
| Gemma 4 31B | Dense | 30.7B | 256K | Text, Image | Workstation-grade reasoning |

The "E" in E2B/E4B stands for "effective" parameters — Per-Layer Embeddings (PLE) give each decoder layer its own small embedding table, maximizing parameter efficiency for on-device deployment. The "A" in 26B A4B stands for "active" parameters (8 active / 128 total experts + 1 shared). The "Unified" in 12B refers to its **encoder-free architecture** — no separate vision/audio encoders; raw image patches and audio waveforms are projected directly into the LLM's embedding space via lightweight linear layers.

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

## Gemma 4 E4B: The On-Device Sweet Spot

The E4B variant has emerged as a practical daily-driver model for on-device use, particularly on Apple Silicon via LM Studio.

### Benchmark Performance (E4B)

| Benchmark | E4B | E2B | Gemma 3 27B (no think) |
|-----------|-----|-----|------------------------|
| MMLU Pro | 69.4% | 60.0% | 67.6% |
| AIME 2026 (no tools) | 42.5% | 37.5% | 20.8% |
| LiveCodeBench v6 | 52.0% | 44.0% | 29.1% |
| GPQA Diamond | 58.6% | 43.4% | 42.4% |
| MMMLU | 76.6% | 67.4% | 70.7% |
| MATH-Vision | 59.5% | 52.4% | 46.0% |

Notably, E4B outperforms the previous-generation Gemma 3 27B across all benchmarks despite having ~6× fewer effective parameters.

### GGUF Quantization (lmstudio-community)

The [lmstudio-community GGUF](https://huggingface.co/lmstudio-community/gemma-4-E4B-it-GGUF) package provides three quantization levels:

| Quantization | Use Case | Downloads |
|---|---|---|
| Q4_K_M | Minimum VRAM | — |
| Q6_K | Quality/speed sweet spot | — |
| Q8_0 | Maximum fidelity | — |

Total downloads: 1M+ (as of June 2026). Also includes `mmproj-gemma-4-E4B-it-BF16.gguf` for vision support.

### Daily Driver Adoption (June 2026)

Florian Brand (@xeophon, Research Engineer at Prime Intellect, Interconnects editor) publicly switched to Gemma 4 E4B 6-bit as his always-loaded local model on Mac via LM Studio, replacing Qwen3 and 3.5 4B after ~9 months of usage:

> *"Gemma 4 E4B 6bit is now the local model of my choice and loaded 24/7 on my Mac (using @lmstudio), replacing Qwen3, 3.5 4B after ~9 months of usage"*

The killer use case for local models was identified as latency-sensitive text transformation tasks: **rewrite, summarize, translate** — where local models "win in latency" over cloud alternatives.

This represents a notable endorsement: an ML practitioner with deep benchmark expertise choosing a model not for benchmark scores but for practical daily utility on consumer hardware.

**Source**: [raw/articles/2026-06-07_xeophon_gemma-4-e4b-daily-local-model.md](raw/articles/2026-06-07_xeophon_gemma-4-e4b-daily-local-model.md), [@xeophon on X](https://x.com/xeophon/status/2063581687590649888) (691 likes, 423 bookmarks)

## Gemma 4 12B Unified: Encoder-Free Multimodal (May 2026)

Released on 2026-05-23, the 12B Unified model fills the gap between E4B and 26B A4B with a novel **encoder-free architecture**.

### Key Differentiator: Unified Architecture

Unlike other Gemma 4 models that use dedicated vision (~550M) and audio (~300M) encoders, 12B Unified **eliminates all separate encoders**. Raw image patches and audio waveforms are projected directly into the LLM's embedding space via lightweight linear layers. All modalities flow through a single decoder-only transformer.

**Benefits**:
- Reduced multimodal latency (no encoder pre-processing bottleneck)
- Entire model fine-tunable in one pass (no encoder/LLM alignment issues)
- Smaller deployment footprint despite 11.95B parameters (no encoder weight overhead)

### Specifications

| Property | Value |
|----------|-------|
| Parameters | 11.95B |
| Layers | 48 |
| Sliding Window | 1024 tokens |
| Context Length | 256K tokens |
| Modalities | Text, Image, Audio, Video |
| Vocab Size | 262K |
| License | Apache 2.0 |

### Benchmark Performance (12B Unified)

| Benchmark | 12B Unified | E4B | 26B A4B | 31B | Gemma 3 27B |
|-----------|-------------|-----|---------|-----|-------------|
| MMLU Pro | 77.2% | 69.4% | 82.6% | 85.2% | 67.6% |
| AIME 2026 (no tools) | 77.5% | 42.5% | 88.3% | 89.2% | 20.8% |
| LiveCodeBench v6 | 72.0% | 52.0% | 77.1% | 80.0% | 29.1% |
| Codeforces ELO | 1659 | 940 | 1718 | 2150 | 110 |
| GPQA Diamond | 78.8% | 58.6% | 82.3% | 84.3% | 42.4% |
| Tau2 (avg) | 69.0% | 42.2% | 68.2% | 76.9% | 16.2% |
| MMMLU | 83.4% | 76.6% | 86.3% | 88.4% | 70.7% |
| MMMU Pro (vision) | 69.1% | 52.6% | 73.8% | 76.9% | 49.7% |
| CoVoST (audio) | 38.5* | 35.54 | — | — | — |
| MRCR 128K (8-needle) | 43.4% | 25.4% | 44.1% | 66.4% | 13.5% |

*Excluding Chinese language.

**Notable**: 12B Unified achieves **near-26B A4B performance** on Tau2 (69.0% vs 68.2%) and MRCR long-context (43.4% vs 44.1%) — competitive with the MoE model despite being a dense architecture.

### Ecosystem (as of June 2026)

- [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it) — 434K+ downloads, 691 likes
- [unsloth/gemma-4-12B-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF) — 568K+ downloads (community GGUF)
- [google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf) — Official QAT quantization (June 5), 25K+ downloads
- [unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF) — Community QAT GGUF, 85K+ downloads
- Launch blog: [Google Blog: Introducing Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12B/)

**Source**: [HuggingFace google/gemma-4-12B-it model card](https://huggingface.co/google/gemma-4-12B-it)

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

## Multi-Token Prediction (MTP) Drafters (May 2026)

Google released specialized **MTP drafters** for the entire Gemma 4 family, achieving up to **3× faster inference** through speculative decoding:

### How MTP Works
1. **Drafting**: A lightweight MTP model suggests multiple future tokens simultaneously
2. **Verification**: The target Gemma 4 model checks the entire sequence in a **single forward pass**
3. **Bonus Token**: If the target agrees, it accepts the draft sequence AND generates one additional token

### Technical Enhancements
- **Shared KV Cache**: Drafters reuse the target model's activations, avoiding redundant computation
- **Clustering for Edge**: E2B/E4B models use a clustering technique in the embedder to bypass logit bottlenecks
- **Batch Optimization**: On Apple Silicon, batch sizes of 4–8 unlock ~2.2× speedup for 26B MoE
- **Cross-platform**: Supported on LiteRT-LM (edge), MLX (Apple), Ollama, vLLM, SGLang, and Hugging Face Transformers

### Performance Impact
| Model Tier | Use Case | MTP Speedup |
|------------|----------|-------------|
| E2B/E4B (Edge) | Mobile/IoT, battery-preserved | Significant latency reduction |
| 26B MoE | Offline coding, agentic workflows | Up to 3× (batch-optimized) |
| 31B Dense | Workstation-grade tasks | Up to 3× |

The MTP drafters are released under **Apache 2.0** and are available in the [Gemma 4 HuggingFace Collection](https://huggingface.co/collections/google/gemma-4).

See also: [[concepts/speculative-decoding]], [Google Blog: Accelerating Gemma 4 with MTP](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

## Gemma 4 26B A4B vs Apple AFM 3 Core Advanced (June 2026)

Apple announced its third-generation foundation models at WWDC 2026 (June 8). The on-device flagship **AFM 3 Core Advanced** (20B sparse, 1-4B active) directly competes with Gemma 4 26B A4B for on-device AI supremacy.

### Architecture Comparison

| Dimension | Gemma 4 26B A4B | AFM 3 Core Advanced |
|-----------|-----------------|-------------------|
| Total Params | 25.2B | 20B |
| Active Params | 3.8B (fixed) | 1-4B (adaptive per use case) |
| Architecture | Standard MoE (per-token routing) | IFP sparse (per-prompt routing) |
| Weight Storage | All in DRAM | NAND flash + selective DRAM loading |
| Context | 256K tokens | Not disclosed |
| Modalities | Text, Image | Text, Audio, Image |
| License | Apache 2.0 | Proprietary |
| Hardware | Any (Apple, NVIDIA, CPU) | Apple Silicon only |
| Deployment | LM Studio, Ollama, vLLM, etc. | iOS/macOS system integration |

### Key Architectural Difference

Gemma 4 uses standard MoE with **per-token routing** — all 26B weights must reside in DRAM for fast expert switching (~18GB VRAM for Q4_K_M). AFM 3 Core Advanced uses **Instruction-Following Pruning (IFP)** with **per-prompt routing** — the full 20B model lives in NAND flash, with only selected experts loaded into DRAM. This enables a larger effective model on memory-constrained devices but sacrifices per-token routing granularity.

### Practical Trade-offs for Mac Users

- **Gemma 4 26B A4B**: Open, customizable, runs via LM Studio/Ollama, fine-tunable, community GGUF quantizations available. Requires ~18GB VRAM. Best for users who want control and cross-platform flexibility.
- **AFM 3 Core Advanced**: Integrated into iOS/macOS, no setup required, adaptive activation, NAND-based loading enables larger model on same hardware. Locked to Apple ecosystem, no customization. Best for users who want seamless system-level AI without configuration.

Apple's evaluation uses human graders only (no public benchmarks like MMLU or HumanEval), making direct benchmark comparison impossible. A summer 2026 technical report may provide more data.

See also: [[concepts/apple-foundation-models]]

## Sources
|- raw/articles/2026-05-05_google-gemma-4-multi-token-prediction-drafters.md
|- raw/articles/2026-06-07_xeophon_gemma-4-e4b-daily-local-model.md
|- 
|- Google DeepMind announcement
|- Google Gemma 4 E4B model card: huggingface.co/google/gemma-4-E4B-it
|- lmstudio-community GGUF: huggingface.co/lmstudio-community/gemma-4-E4B-it-GGUF
|- Google Gemma 4 12B Unified model card: huggingface.co/google/gemma-4-12B-it
|- Google Blog: Introducing Gemma 4 12B (May 2026)
|- Martin Alderson, "A little tool to visualise MoE expert routing," martinalderson.com (April 13, 2026)
|- Patrick Loeber, "How to run a local coding agent with Gemma 4 and Pi," patloeber.com (Apr 2026)
|- Florian Brand (@xeophon), X post on Gemma 4 E4B daily driver (June 7, 2026)

## See Also

- [[florian-brand]] — Research Engineer who endorsed Gemma 4 E4B as daily local model.
- [[pi-coding-agent]] — Minimal coding agent by Mario Zechner that runs with Gemma 4 via LM Studio.
- [[mistral-ai]] — Competing open-weight model provider with Mistral Medium 3.5.
- [[open-models]] — Open-weight model ecosystem and licensing landscape.
- [[concepts/coding-agents]] — AI agents for software engineering tasks.
- [[concepts/local-llm]] — Local LLM deployment patterns and use cases.
- [[lmstudio]] — Local model serving tool for running Gemma 4 on consumer hardware.
