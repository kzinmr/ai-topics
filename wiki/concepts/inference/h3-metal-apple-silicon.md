---
title: "H3-metal — Native MiniMax-H3 Inference for Apple Silicon"
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [inference, apple-silicon, local-llm, open-source]
sources: [raw/articles/2026-08-11_h3-metal.md]
---

# H3-metal — Native MiniMax-H3 Inference for Apple Silicon

**Repository:** [antirez/h3.c](https://github.com/antirez/h3.c) (GitHub)
**Author:** [[entities/antirez-com|Salvatore Sanfilippo (antirez)]]
**License:** MIT
**Language:** C (with Metal Shading Language for GPU kernels)

## Overview

H3-metal is a native inference engine for the MiniMax-H3 model family running on Apple Silicon (M-series Macs). It is written entirely in C, using Apple's Metal GPU API for hardware acceleration, and targets video generation, multimodal understanding, and interactive prompt-to-video workflows. The project is a continuation of antirez's tradition of bare-metal, dependency-free implementations of complex AI systems — following the lineage of [[concepts/voxtral-c]] (Mistral Pixtral 12B on CPU) and [[concepts/ds4-dwarfstar-4]] (DeepSeek V4 Flash local inference).

Unlike [[concepts/local-llm/llama-cpp]], which focuses on text-based LLM inference across diverse hardware, H3-metal is purpose-built for the MiniMax-H3 video/multimodal generation model family and is optimized exclusively for Apple Silicon via the Metal API.

## How It Works

### Architecture

H3-metal is structured as a collection of vertical slices — independent subsystems that are built, validated, and integrated incrementally:

| Subsystem | Source File | Purpose |
|-----------|------------|---------|
| **Host/model metadata** | `h3_host.c/h`, `h3_weights.c/h` | Deterministic model loading, weight mapping, device detection |
| **Metal GPU backend** | `h3_metal.m/h`, `h3_shaders.metal`, `h3_gpu.m/h` | Metal kernel dispatch, tensor operations, attention, convolution |
| **DiT (Diffusion Transformer)** | `h3_dit.c/h`, `h3_dit_schedule.c/h` | Denoising diffusion transformer with configurable steps, reuse, and layers |
| **Video VAE** | `h3_video_vae.c/h` | Video encoding/decoding in latent space |
| **Audio VAE** | `h3_audio_vae.c/h` | Audio generation pipeline |
| **Vision encoder** | `h3_vision_encoder.c/h` | Image/video conditioning for Ref2VA and first/last-frame anchors |
| **Text encoder** | `h3_text_encoder.c/h` | Prompt encoding into conditioning vectors |
| **Multimodal integration** | `h3_multimodal.c/h` | Combined text + vision + audio pipeline |
| **Tokenizer** | `h3_tokenizer.m/h` | Text tokenization compatible with MiniMax-H3 vocabulary |
| **SafeTensors loader** | `h3_safetensors.c/h` | Hugging Face SafeTensors weight format parsing |
| **FFmpeg bridge** | `h3_ffmpeg.c/h` | Video/audio encoding via FFmpeg |
| **CLI/Terminal** | `h3_cli.c/h`, `main.c` | Interactive session with Iris-style REPL, command history (linenoise) |

### Metal GPU API Integration

H3-metal uses Apple's Metal API directly — no PyTorch, no MLX, no TensorFlow, no C++ bindings. The Metal shading language kernels are written in `h3_shaders.metal` and dispatched from C via the Objective-C bridge (`h3_metal.m`). This provides:

- **Zero Python dependency**: The entire engine compiles with a single `make -j8`
- **Direct GPU control**: Memory allocation, kernel dispatch, and synchronization are managed explicitly
- **Apple Silicon optimization**: Apple-specific memory model (unified memory), AMX coprocessor, and M-series GPU features

### MiniMax-H3 Model Family

H3-metal targets the **H3-Base** 768p model from [[entities/minimax|MiniMax]]. Key characteristics:

- **Video generation**: Prompt-to-video with configurable resolution, duration, and framerate (24 fps)
- **Multimodal conditioning**: Text prompts, first/last-frame anchors, and Ref2VA image/video/audio references
- **Spatial tokens**: 8x8 effective grid at 256px, scaling up for larger canvases
- **Temporal structure**: Frames aligned to 5 + 17*n formula; duration controlled via `--frames` or `--seconds`

## Performance Characteristics

H3-metal exposes five independent speed/quality controls that can be combined (within limits):

| Control | Slow Reference | Default | Aggressive | Effect |
|---------|---------------|---------|------------|--------|
| **Denoising passes** (`--steps`) | 50 | 20 | 4–7 | More passes = better detail, smoother motion |
| **Denoiser reuse** (`--reuse`) | 1 | 2 | 3 | Reuses denoiser velocities; 20 steps with reuse 2 = 11 fresh evaluations |
| **Active DiT blocks** (`--layers`) | 50 | 45 | 40 | Fewer blocks = less compute, lower memory |
| **Core residual reuse** (`--core-reuse`) | 1 | — | 4–6 | Refreshes patch/head work every step, reuses expensive core |
| **Token reduction** (`--token-reduction`) | off | off | on (optional) | Pairs horizontal tokens inside middle blocks; faster but may change composition |

Additional optimizations:

- **Internal canvas rendering** (`--render-width/--render-height`): Run DiT/VAE at lower resolution (e.g., 320x320), upscale to output (e.g., 512x512) using vImage
- **INT8 row-wise FC2** (`--use-int8-row-fc2`): Uses one activation scale per FC2 row with TensorOps; ~2.6% faster with minimal quality impact
- **Automatic low-res RoPE**: At 256x256, spatial RoPE coordinates are halved to prevent lattice artifacts

### Performance Benchmarks (M5 Max, 512x512, 22 frames)

| Configuration | Steps | Layers | Reuse | Time | Notes |
|--------------|-------|--------|-------|------|-------|
| Reference quality | 50 | 50 | 1 | ~26.4s | Full 50-pass denoise |
| Default (balanced) | 20 | 45 | 2 | ~16.7s | Standard preset |
| Fast (token reduction) | 20 | 45 | 2 | ~12.6s | With `--token-reduction` |
| Aggressive (4-step) | 4 | 50 | 1 | ~3.5s | SSIM 0.556 vs 29-pass reference |

The four-pass schedule uses a linear base grid with one terminal point — evaluated as the best low-budget configuration after comparing several tail-heavy schedules that produced woven texture, weak motion, or clipped colors.

## Interactive Session

H3-metal includes an Iris-style interactive REPL (reminiscent of Redis's `redis-cli`):

```
./h3 -d ./MiniMax-H3 --width 512 --height 512 --steps 6
h3> A red fox walks through fresh snow in a pine forest.
h3> !status
h3> !seed random
h3> !first opening.png
h3> !last ending.png
h3> !save output.mp4
```

The session keeps the BF16 prompt conditioning, prepared DiT, and video decoder resident in memory, so repeating a prompt avoids reloading and encoding. Key commands:

- `!status` — Show current configuration
- `!seed random` — Randomize the seed
- `!first PATH` / `!last PATH` — Set first/last-frame conditioning anchors
- `!ref-image PATH` — Add Ref2VA conditioning image (exposed as `<Picture N>`)
- `!refs` / `!ref-remove N` — Manage reference list
- `!save output.mp4` — Write generated video
- `!show` — Display frames in terminal (Kitty/Ghostty or iTerm2/WezTerm/Konsole graphical protocols)
- `!int8-row-fc2 on` — Toggle INT8 row-wise optimization

First/last-frame conditioning and Ref2VA references are mutually exclusive within a single session.

## Why It Matters

### 1. Native Apple Silicon Inference Without Framework Overhead

H3-metal demonstrates that complex AI inference — including video generation — can be implemented in pure C with direct Metal API calls, with no Python, no PyTorch, and no MLX. This is philosophically aligned with antirez's broader project of democratizing access to AI: if the code is readable C that compiles with `make`, anyone can understand, modify, and run it on consumer hardware.

### 2. antirez's Engineering Philosophy Applied to AI

H3-metal extends antirez's lifelong approach to systems programming into the AI domain:

- **Radical simplicity**: The entire engine fits in ~20 source files, is MIT-licensed, and has no external dependencies beyond macOS system libraries and FFmpeg
- **Vertical slices**: Each subsystem is independently verifiable before integration, following the same pattern as Redis's incremental development
- **Optimize for joy**: The interactive session, debug-friendly code, and clear CLI reflect the belief that tools should be pleasurable to use and understand
- **Ideas over code**: Following antirez's \"Control the Ideas, Not the Code\" July 2026 essay, H3-metal prioritizes architectural clarity and design documentation over line-by-line implementation details

### 3. The Apple Silicon AI Ecosystem

H3-metal joins a growing ecosystem of native Apple Silicon inference projects:

- [[concepts/local-llm/llama-cpp]] — Text LLM inference on CPU/GPU (GGUF format)
- [[concepts/ds4-dwarfstar-4]] — antirez's DeepSeek V4 Flash inference with asymmetric quantization
- [[concepts/ds4-deepseek-flash-metal]] — Armin Ronacher's Metal optimization fork of ds4.c
- MLX — Apple's own machine learning framework for Apple Silicon
- H3-metal — The first native C+Metal engine for video/multimodal generation

### 4. Video Generation at the Edge

Unlike cloud-based video generation services (Runway, Pika, Sora), H3-metal runs entirely on-device. This matters for:

- **Privacy**: Prompts, conditioning images, and generated videos never leave the machine
- **Iteration speed**: The interactive session with persistent model state enables rapid prompt experimentation
- **Cost**: No API fees; compute is bounded by local hardware
- **Offline capability**: No network dependency after model download

## Comparison to llama.cpp

| Dimension | H3-metal | [[concepts/local-llm/llama-cpp]] |
|-----------|---------|-----------------------------------|
| **Target models** | MiniMax-H3 (video/multimodal) | Text LLMs (LLaMA, Mistral, DeepSeek, etc.) |
| **Hardware** | Apple Silicon only (Metal) | Cross-platform (CPU, CUDA, Metal, Vulkan, SYCL) |
| **Model format** | SafeTensors (Hugging Face) | GGUF (custom quantized format) |
| **Primary workload** | Video generation, multimodal | Text generation, chat, code |
| **Language** | C + Metal Shading Language | C++ |
| **Quantization** | BF16, optional INT8 row-wise FC2 | Extensive (Q2_K through Q8_0, IQ quants) |
| **Interactive mode** | Iris-style REPL with persistent state | CLI chat, server mode with OpenAI-compatible API |
| **Dependencies** | macOS, FFmpeg | Cross-platform, minimal system deps |
| **Philosophy** | Minimal C, educational, anti-framework | Practical ecosystem, broad hardware support |

H3-metal and llama.cpp serve complementary roles in the local inference ecosystem. llama.cpp provides broad text-based LLM access; H3-metal provides focused, high-performance video generation on Apple Silicon. Both share the conviction that frontier AI should run on consumer hardware without cloud dependency.

## Limitations and Tradeoffs

- **Apple Silicon only**: No support for NVIDIA, AMD, or Intel GPUs — by design, as the Metal API is Apple-exclusive
- **Model-specific**: Only supports MiniMax-H3; not a general-purpose inference framework
- **Resolution limits**: Canvas dimensions constrained to multiples of 32 with a maximum product of 768 x 1344 pixels
- **Native 128x128 unsupported**: The 4x4 token grid at that resolution cannot recover a recognizable subject
- **Thermal throttling sensitive**: M-series Macs throttle under sustained GPU load; repeated runs should be compared under similar thermal conditions
- **Early stage**: As of August 2026, the project is actively developed with ongoing Metal performance optimization on M3 Max and M5 Max

## Related Pages

- [[entities/antirez-com]] — Salvatore Sanfilippo, creator of H3-metal and Redis
- [[concepts/local-llm/llama-cpp]] — Cross-platform local LLM inference (comparison above)
- [[concepts/inference/_index]] — LLM inference optimization techniques and engines
- [[concepts/ds4-dwarfstar-4]] — antirez's DeepSeek V4 Flash local inference project
- [[concepts/ds4-deepseek-flash-metal]] — Armin Ronacher's Metal optimization of ds4.c
- [[entities/minimax]] — MiniMax, the company behind the H3 model family
- [[entities/mistral-voxtral-tts]] — antirez's earlier bare-metal C implementation of multimodal inference on CPU
