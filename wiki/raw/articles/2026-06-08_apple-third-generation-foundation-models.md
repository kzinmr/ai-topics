# Introducing the Third Generation of Apple's Foundation Models

**Source**: https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models
**Date**: June 8, 2026
**Fetched**: 2026-06-09

---

Apple's next generation of Apple Intelligence is centered around users, integrated deeply into operating systems, and powered by a bold new architecture with privacy at its core.

## The AFM 3 Model Family

Five foundation models custom-built in collaboration with Google:

### On-Device Models

**AFM 3 Core**
- Next generation 3-billion-parameter dense model
- Step up in quality over previous generation

**AFM 3 Core Advanced**
- Most powerful on-device model
- Natively multimodal (expressive voices, higher-accuracy dictation)
- 20-billion-parameter sparse architecture
- Activates just 1 to 4 billion parameters at a time depending on request
- Unlocked by and optimized for most capable Apple Silicon systems

### Server-Based Models (Private Cloud Compute)

**AFM 3 Cloud**
- Server-side workhorse, optimized for speed, efficiency, and performance

**ADM 3 Cloud (Image)**
- Image generation and editing
- Powers advanced photo-editing, Image Playground, Genmoji

**AFM 3 Cloud Pro**
- Most capable server-based model
- Powers agentic tool use and complex reasoning
- Runs on NVIDIA GPUs in Google Cloud (PCC extended)

## Architecture: Instruction-Following Pruning (IFP)

AFM 3 Core Advanced introduces a novel sparsely activated architecture:

- Full model stored in flash memory (NAND), not DRAM
- Lightweight dense block selects a fixed set of experts during initial processing
- Periodically reselects experts during generation
- High percentage of always-active "shared experts" + input-dependent "routed experts"
- Inference-time elasticity: predetermined number of active parameters per use case
- Scales model size far beyond traditional DRAM limits while minimizing latency

This is distinct from standard MoE — routing decisions are per-prompt, not per-token, because NAND-to-DRAM bandwidth is too slow for token-level swapping.

## Server Architecture: PT-MoE

AFM 3 Cloud uses Parallel-Track Mixture-of-Experts (PT-MoE), building on architecture introduced in 2025. Key upgrades stabilize training and improve reasoning over context windows.

## ADM 3 Cloud (Image)

- Native image creation, editing, and Genmoji
- Generalizes across different aspect ratios and resolutions
- Specialized adapters for downstream editing (Spatial Reframing, Image Playground)

## Training

- Publicly available data, licensed/purchased data, open-sourced data, dedicated studies, synthetic data
- Does NOT use private personal data or user interactions
- Respects web publisher opt-out rights
- Scaled pre-training on cloud TPU accelerators
- Common initial foundation → specialization per architecture
- Multimodal capabilities: audio, image understanding, long-context reasoning, visual generation
- Post-training: supervised fine-tuning + multi-stage reinforcement learning
- Quantization Aware Training for hardware optimization

## Evaluations

### Model-Level (Human Evaluation)

**AFM 3 Core vs 2025 baseline:**
- General text: preferred on 45.6% of prompts vs 23.3% for baseline
- Image understanding: preferred over previous generation >61% of the time

**AFM 3 Cloud vs 2025 AFM Server:**
- General text: preferred on 64.7% of prompts vs 8.7% for baseline
- ~36% relative improvement in overall response satisfaction
- ~21% relative improvement in instruction following
- Image understanding: preferred on 37.8% vs 9.6% for baseline

**AFM 3 Cloud Pro vs AFM 3 Cloud:**
- ~10% relative improvement in overall text satisfaction
- ~14% relative improvement in image understanding
- Math: ~14% relative improvement

### Feature-Level

**TTS (AFM 3 Core Advanced at 1B active params):**
- General Voice MOS: 4.15 vs 3.87 (production baseline)
- Conversational Voice MOS: 4.24 vs 3.82

**Dictation (AFM 3 Core Advanced at 1B active params):**
- Overall Quality: preferred 44.7% vs 17.6%
- Consistent preference across all 7 dimensions (Punctuation, Casing, Layout, Meaning Capture, Disfluency Handling, Style)

## Key Takeaways

- **Collaboration with Google**: Custom models built in partnership
- **NVIDIA GPUs in PCC**: AFM 3 Cloud Pro runs on NVIDIA hardware in Google Cloud — first time PCC extends beyond Apple Silicon
- **IFP architecture**: Novel approach to on-device sparse activation, distinct from standard MoE
- **No user data in training**: Privacy-first stance maintained
- **Technical report**: Coming later in summer 2026

## Related Apple Research

- [Updates to Apple's On-Device and Server Foundation Language Models](https://machinelearning.apple.com/research) (June 9, 2025)
- [Introducing Apple's On-Device and Server Foundation Models](https://machinelearning.apple.com/research) (June 10, 2024)
