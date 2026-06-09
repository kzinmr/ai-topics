---
title: "Apple Foundation Models (AFM 3)"
type: concept
created: 2026-06-09
updated: 2026-06-09
tags:
  - concept
  - model
  - apple
  - foundation-models
  - on-device
  - mixture-of-experts
  - multimodal
  - apple-silicon
  - inference
  - quantization
sources:
  - raw/articles/2026-06-08_apple-third-generation-foundation-models.md
  - https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models
related:
  - concepts/apple
  - entities/gemma-4
  - concepts/local-llm
  - concepts/on-device-ai
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

- [[concepts/apple]] — Apple's AI philosophy and strategy
- [[entities/gemma-4]] — Google's open-weight competitor for on-device use
- [[concepts/local-llm]] — Local LLM deployment patterns
- [[concepts/on-device-ai]] — On-device AI concepts and trade-offs

## Sources

- Apple ML Research, "Introducing the Third Generation of Apple's Foundation Models" (June 8, 2026)
- raw/articles/2026-06-08_apple-third-generation-foundation-models.md
