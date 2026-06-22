---
title: "Apple Foundation Models (AFM 3)"
type: concept
created: 2026-06-09
updated: 2026-06-15
tags:
  - concept
  - model
  - apple
  - foundation-models
  - on-device
  - claude-code
  - agent-sdk
  - multimodal
  - hardware
  - inference
  - quantization
sources:
  - raw/articles/2026-06-08_apple-third-generation-foundation-models.md
  - raw/articles/2026-06-15_apple-foundation-models-claude-sdk.md
  - https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models
  - https://developer.apple.com/documentation/foundationmodels/
  - https://www.anthropic.com/news/apple-foundation-models
related:
  - concepts/apple
  - entities/gemma-4
  - concepts/local-llm
  - concepts/on-device-rag
---

# Apple Foundation Models (AFM 3)

Third generation of Apple's foundation models announced at WWDC 2026 (June 8, 2026). A family of five models custom-built in collaboration with Google, spanning on-device to server-based inference, all designed for Apple Intelligence experiences with privacy at their core.

## Model Family

### On-Device Models

| Model | Params | Architecture | Active Params | Modalities | Hardware |
|-------|--------|-------------|---------------|------------|----------|
| AFM 3 Core | 3B | Dense | 3B | Text | Apple Silicon |
| AFM 3 Core Advanced | 20B | Sparse (IFP) | 1-4B | Text, Audio, Image | Apple Silicon (high-end) |

### Server Models (Private Cloud Compute)

| Model | Role | Hardware |
|-------|------|----------|
| AFM 3 Cloud | General server workhorse | Apple Silicon (PCC) |
| ADM 3 Cloud | Image generation/editing | Apple Silicon (PCC) |
| AFM 3 Cloud Pro | Agentic tool use, complex reasoning | NVIDIA GPUs on Google Cloud (PCC) |

## Architecture Innovations

### Instruction-Following Pruning (IFP) — AFM 3 Core Advanced

A novel sparse activation architecture distinct from standard MoE:

- **Full model in NAND flash**, not DRAM — breaks the DRAM wall for on-device models
- **Per-prompt routing** (not per-token): lightweight dense block selects a fixed set of experts during initial processing, periodically reselects during generation
- **Shared experts** (always active) + **routed experts** (swapped from NAND to DRAM when needed)
- **Inference-time elasticity**: active parameter count scales per use case difficulty
- Enables 20B-parameter model on devices with limited DRAM

> Unlike standard MoE models that swap experts per-token (requiring high NAND-to-DRAM bandwidth), IFP makes routing decisions per-prompt because NAND bandwidth is too slow for token-level swapping.

### Parallel-Track MoE (PT-MoE) — AFM 3 Cloud

Server-side architecture building on 2025 foundation. Key upgrades stabilize training and improve reasoning within context windows.

### ADM 3 Cloud (Image)

- Native image creation, editing, Genmoji
- Generalizes across aspect ratios and resolutions
- Specialized adapters for Spatial Reframing, Image Playground, touch-based modifications

## Training Approach

- **Data**: Public, licensed, open-sourced, dedicated studies, synthetic — no private user data
- **Pre-training**: Scaled on cloud TPU accelerators, common foundation → per-model specialization
- **Multimodal**: Audio, image understanding, long-context reasoning, visual generation
- **Post-training**: Supervised fine-tuning + multi-stage reinforcement learning
- **Compression**: Quantization Aware Training (QAT) for hardware-specific optimization

## Evaluation Results

### Human Evaluation — Text

| Comparison | AFM 3 | Baseline |
|------------|-------|----------|
| AFM 3 Core vs 2025 | **45.6%** preferred | 23.3% |
| AFM 3 Cloud vs 2025 Server | **64.7%** preferred | 8.7% |
| AFM 3 Cloud Pro vs AFM 3 Cloud | ~10% relative improvement | — |

### Human Evaluation — Image Understanding

| Comparison | AFM 3 | Baseline |
|------------|-------|----------|
| AFM 3 Core vs 2025 | **>61%** preferred | — |
| AFM 3 Cloud vs 2025 Server | **37.8%** preferred | 9.6% |
| AFM 3 Cloud Pro vs AFM 3 Cloud | ~14% relative improvement | — |

### TTS (AFM 3 Core Advanced at 1B active)

| Metric | Production TTS | AFM 3 Core Advanced |
|--------|---------------|-------------------|
| General Voice MOS | 3.87 | **4.15** |
| Conversational Voice MOS | 3.82 | **4.24** |

### Dictation (AFM 3 Core Advanced at 1B active)

- Overall Quality preferred: **44.7%** vs 17.6%
- Consistent wins across all 7 dimensions

## Privacy Architecture

- On-device models: all inference local
- Server models: Private Cloud Compute (PCC)
  - Dedicated process per request in own namespace
  - Shared inference software recycled with short TTL
  - Attested keys in separate confidential VM
  - All binaries published for public inspection
- **PCC extended to Google Cloud** with NVIDIA GPUs for AFM 3 Cloud Pro — same security guarantees
- No private user data used in training

## Comparison with Gemma 4 (On-Device)

| Dimension | AFM 3 Core Advanced | Gemma 4 26B A4B |
|-----------|-------------------|-----------------|
| Total Params | 20B | 25.2B |
| Active Params | 1-4B (adaptive) | 3.8B (fixed) |
| Architecture | IFP sparse (per-prompt routing) | MoE (per-token routing) |
| Storage | NAND flash + DRAM | Full DRAM |
| Context | — | 256K |
| Modalities | Text, Audio, Image | Text, Image |
| License | Proprietary | Apache 2.0 |
| Hardware Target | Apple Silicon only | Any (Apple, NVIDIA, CPU) |
| Deployment | iOS/macOS only | LM Studio, Ollama, vLLM, etc. |
| Availability | Apple devices only | Open download (HuggingFace) |

### Key Architectural Difference

**Gemma 4 26B A4B** uses standard MoE with per-token routing — all 26B weights must reside in DRAM for fast expert switching. Active params are 3.8B but VRAM requirement is ~18GB (Q4_K_M).

**AFM 3 Core Advanced** uses IFP with per-prompt routing — the full 20B model lives in NAND flash, with only selected experts loaded into DRAM. This enables a larger effective model on memory-constrained devices, but sacrifices the per-token flexibility of MoE.

### Trade-off Summary

| Aspect | Gemma 4 26B A4B | AFM 3 Core Advanced |
|--------|-----------------|-------------------|
| **Accessibility** | Open, cross-platform | Apple ecosystem only |
| **Customizability** | Fine-tune, quantize, deploy anywhere | No customization |
| **Memory efficiency** | All weights in DRAM | NAND flash + selective DRAM loading |
| **Routing granularity** | Per-token (fine-grained) | Per-prompt (coarser) |
| **Community** | HuggingFace, LM Studio, Ollama ecosystem | Apple-only |
| **Benchmark data** | Public benchmarks available | Human eval only (no public benchmarks) |

## Strategic Significance

- **Google collaboration**: Custom model built with Google, not off-the-shelf Gemini
- **NVIDIA in PCC**: First time Apple's privacy infrastructure extends beyond Apple Silicon hardware
- **IFP innovation**: Novel architecture that could influence on-device AI beyond Apple
- **No public benchmarks**: Apple uses human evaluation only — no MMLU, HumanEval, or standard benchmarks published
- **Technical report**: Coming later summer 2026 with updated evaluations

## See Also

- [[concepts/apple]] — Apple's AI philosophy and strategy (overview)
- [[entities/gemma-4]] — Google's open-weight competitor for on-device use
- [[concepts/local-llm/_index]] — Local LLM deployment patterns and ecosystem
- [[concepts/on-device-rag]] — On-device AI concepts and trade-offs
- [[entities/anthropic]] — Anthropic, creator of Claude models
- [[concepts/claude-code/claude-code]] — Claude development ecosystem
- [[concepts/on-device-rag]] — On-device AI and retrieval patterns

## Sources

- Apple ML Research, "Introducing the Third Generation of Apple's Foundation Models" (June 8, 2026)
- raw/articles/2026-06-08_apple-third-generation-foundation-models.md

## Foundation Models API & SDK

In 2026, Apple released its Foundation Models API and SDK, giving developers programmatic access to Apple's on-device and cloud-based models for the first time. This represents a significant shift from Apple's previously closed model ecosystem.

### API Architecture

The Foundation Models API provides two deployment paths:

| Path | Description | Use Case |
|------|-------------|----------|
| **On-Device API** | Direct access to AFM 3 Core / Core Advanced on Apple Silicon | Privacy-sensitive tasks, offline capability, low-latency inference |
| **Cloud API** | Access to AFM 3 Cloud / Cloud Pro via Private Cloud Compute | Heavy workloads, complex reasoning, multi-modal tasks |

### SDK Features

- **Native Swift/Obj-C bindings**: First-class integration with iOS/macOS development
- **Privacy-preserving by design**: On-device inference keeps data local; cloud calls go through attested PCC infrastructure
- **Model routing abstraction**: SDK handles automatic fallback from on-device to cloud when tasks exceed local capacity
- **Task-specific APIs**: Pre-built interfaces for text generation, image understanding, speech-to-text, and translation

### Developer Implications

This API/SDK release enables third-party apps to leverage Apple's foundation models without building custom ML pipelines. Key use cases include:
- **On-device summarization** via AFM 3 Core Advanced
- **Visual search** using AFM 3 Core Advanced's multimodal capabilities
- **Agentic workflows** leveraging AFM 3 Cloud Pro's tool-use abilities

## Claude SDK Integration

Anthropic's Claude SDK now includes direct support for Apple Foundation Models, creating a **hybrid inference pathway** that lets developers route requests between Apple's on-device models and Claude's cloud models based on task complexity, privacy requirements, and latency needs.

### Integration Architecture

```
Developer App
    │
    ├── Apple Foundation Models SDK (on-device)
    │       ├── AFM 3 Core (text, low-latency)
    │       └── AFM 3 Core Advanced (multimodal, moderate latency)
    │
    └── Claude SDK (cloud fallback)
            └── Claude models (complex reasoning, extended context)
```

### Key Features

- **Seamless model routing**: SDK automatically selects Apple on-device or Claude cloud based on task type
- **Privacy-preserving fallback**: Sensitive data processed locally; only anonymized summaries sent to cloud when needed
- **Unified API surface**: Single developer interface abstracts away the underlying model selection
- **Cost optimization**: On-device inference reduces cloud API costs for routine tasks

### Strategic Significance

This integration represents a notable departure from Apple's traditionally closed ecosystem. By partnering with [[entities/anthropic]], Apple gains access to frontier reasoning capabilities while Anthropic gains distribution through Apple's massive device install base.

- **For Apple**: Extends [[concepts/on-device-rag]] capabilities beyond what's feasible locally, maintaining privacy-first positioning
- **For Anthropic**: Reaches billions of iOS/macOS users without building on-device infrastructure
- **For developers**: Single SDK provides access to both edge and cloud models with intelligent routing

## Apple's AI Strategy

Apple's approach to AI is characterized by several distinctive pillars:

### Privacy-First Architecture

Unlike competitors who default to cloud-based inference, Apple's strategy prioritizes **on-device processing** as the primary pathway, with cloud fallback only for tasks exceeding local capacity. The [[concepts/apple]] Foundation Models API enforces this through:
- Data never leaves the device unless explicitly requested by the user
- Cloud inference runs through **Private Cloud Compute** with attested security guarantees
- All model binaries are published for independent security audit

### Vertical Integration

Apple's custom silicon (A-series, M-series) enables tight optimization between hardware and models:
- **NAND-based model storage**: IFP architecture allows larger models than DRAM constraints would suggest
- **Neural Engine acceleration**: Dedicated silicon for ML inference reduces power consumption
- **End-to-end optimization**: Model training, quantization, and deployment all tuned for Apple hardware

### Ecosystem Lock-in vs. Developer Enablement

The Foundation Models SDK creates a **dual dynamic**:
- **Lock-in**: Models optimized for Apple Silicon don't run efficiently elsewhere
- **Enablement**: First-party API lowers the barrier for developers to build AI features

This mirrors Apple's historical strategy with [[concepts/on-device-rag]] — provide powerful tools, but keep them within the ecosystem.

### Competitive Positioning

| Dimension | Apple AFM 3 + Claude SDK | Google Gemini | OpenAI GPT + Apple |
|-----------|--------------------------|---------------|-------------------|
| **Default inference** | On-device (Apple Silicon) | Cloud-first | Cloud-first |
| **Privacy** | Attested PCC, local-first | Varies | Varies |
| **Developer API** | Native SDK + Claude integration | Vertex AI | API only |
| **Hardware coupling** | Tight (Apple Silicon only) | Loose (any cloud) | None |
| **Open weights** | No | Yes (Gemma) | No |
| **Ecosystem reach** | iOS/macOS only | Multi-platform | Multi-platform |
