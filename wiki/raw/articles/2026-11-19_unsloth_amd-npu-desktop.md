---
title: "AMD NPU: Run Models Locally Guide"
url: "https://unsloth.ai/docs/get-started/install/amd/amd-npu"
source: "Unsloth Documentation"
date: 2026-11-19
type: raw-article
collected: 2026-11-19
tags:
  - raw
  - unsloth
  - amd
  - npu
---

# AMD NPU: Run Models Locally Guide | Unsloth Documentation

Announced by Daniel Han (@danielhanchen) on X, 2026-11-19 14:48 UTC:
*"Unsloth Desktop now supports NPUs! NPUs use 2-4x less energy per token for local models vs GPUs! We collabed with AMD to support the current Strix, Krackan and Gorgon devices, and future AMD devices with NPUs will also be supported out of the box!"*

Scraped from https://unsloth.ai/docs/get-started/install/amd/amd-npu (Last updated 2 hours before tweet).

---

You can now run local models on AMD Ryzen AI PCs with XDNA 2 NPUs by using the open-source package Unsloth. NPUs deliver powerful compute performance while using **2–4× less energy per token generation than traditional GPUs**. Enable the NPU runtime, download a supported model, and start chatting on Windows or Linux.

AMD Ryzen AI 300 (Strix Point, Krackan Point), Ryzen AI Max (Strix Halo) or Ryzen AI 400 (Gorgon Point), and future AMD devices with integrated NPUs are all supported! Read also their official AMD NPU blog.

On supported PCs with an XDNA 2 NPU, compatible **Q4NX** models appear in the model picker under NPU.

## Features

- Run LLMs on the NPU, with streaming responses and support for reasoning, vision and tools, skills, MCP servers, web search, chatting with local documents, and coding with local files.
- Connect compatible apps and scripts to your NPU models with Unsloth's API endpoint.
- Offload — Local inference to the NPU and free up memory on your other processors.

## Supported PCs

- **Processor**: AMD Ryzen AI 300 (Strix Point, Krackan Point), Ryzen AI Max (Strix Halo) or Ryzen AI 400 (Gorgon Point), with an XDNA 2 (or newer) NPU.
- **OS**: Windows 11 or Linux, x64.
- **Linux requirements**: kernel 7.0 or newer with the `amdxdna` driver, or an older kernel with `amdxdna-dkms`. Also needs updated NPU firmware and an unlimited memlock setting.

## Getting Started

1. **Install Unsloth** — Unsloth Desktop (native app) or Unsloth Web UI (browser). On a supported Ryzen AI PC, the model picker automatically shows an NPU section.
2. **Enable the NPU** — model picker → filter All → NPU → Enable NPU. One-time setup: Unsloth downloads **FastFlowLM** and checks your NPU driver version. If something's missing, Unsloth tells you exactly what to fix: an old driver or firmware, a kernel without NPU support, or a memlock limit that's too low.
3. **Pick a model** — NPU models are listed; filter by NPU, click to download and load.
4. **Start chatting** — set up with browser canvas, design skills; view speed in tokens/sec.

## Which models can I run?

Browse NPU models in the Model Hub by setting the format filter to NPU. The NPU runs **Q4NX (4-bit) models built for AMD's FastFlowLM runtime**. Measured speeds (tokens/sec, TTFT):

| Model | Size | Capabilities | Recommended RAM | tok/s | TTFT |
|---|---|---|---|---|---|
| Qwen3.6-35B-A3B-NPU2 | 20.6 GB | Vision, reasoning, tools | 64 GB | 17.2 | 3.13 s |
| Qwen3.8-27B-NPU2 (MTP) | 18.1 GB | Vision, reasoning, tools | 48 GB | 2.0 | 3.80 s |
| Gemma4-12B-IT-NPU2 | 8.7 GB | Vision, audio, reasoning, tools | 32 GB | 6.8 | 1.70 s |
| Qwen3.5-9B-NPU2 | 7.6 GB | Vision, reasoning, tools | 32 GB | 9.5 | 1.11 s |
| Qwen3-VL-4B-Instruct-NPU2 | 3.9 GB | Vision, tools | 16 GB | 20.5 | 1.05 s |
| LFM3-1.7B-NPU2 | 1.5 GB | Reasoning, tools | 16 GB | 40.7 | 0.12 s |

FastFlowLM and the Q4NX converter are progressively adding new models; Unsloth tracks the latest versions of these repositories.

## Why use the NPU?

Run a local chat model while keeping your GPU available for gaming, rendering or other GPU workloads. The NPU is a dedicated AI engine built into the Ryzen AI processor — another way to run models on hardware you already own. E.g. chat with a local model on the NPU while your Radeon GPU renders a video.

## Settings

- **Power Mode**: Power saver / Balanced / Performance / Turbo (FastFlowLM default: Performance). Power saver or Balanced for battery setups, Turbo when plugged in.
- **Prefill Chunk Length**: tokens of prompt read in one pass before answering (not a context limit). Bigger chunks reach the first token faster on long prompts. FastFlowLM default 4096; Unsloth keeps the chunk at or below context length.
- **Image Pre-resize** (vision models): Original / 480p / 720p / 1080p / 1440p. Smaller images process faster.
- Settings apply on next model load (Reload model to apply immediately). Save/load/reset per-model runtime settings.

## Terminal and API

`unsloth run --model Qwen3.6-35B-A3B-NPU2 --context-length 16384` starts a local server on the NPU. Connect OpenAI-compatible apps via the printed base URL + API key. `unsloth chat Qwen3.6-35B-A3B-NPU2` for interactive chat. Flags: `--model`, `--context-length`, `--max-new-tokens`, `--system-prompt`. NPU models serve through the OpenAI-compatible `/v1/chat/completions` endpoint; embeddings via the Anthropic-compatible `/v1/messages` endpoint.

## Bring your own model

The NPU uses its own model format, **Q4NX**. On the Export page you convert GGUF models to Q4NX. The conversion runs on the CPU, so you can train on any GPU, export the GGUF, and convert it on your Ryzen AI PC. Load the converted Q4NX model from the model picker under *Trained*.

## Use the rest of your Ryzen AI PC

Radeon GPU handles supported training, image and video generation workloads. On Ryzen AI Max (Strix Halo), it can use a large share of system memory, allowing larger models to fit than on GPUs with less dedicated VRAM.

## Secure by design

Unsloth manages its own copies of **Lemonade** and **FastFlowLM**, with separate runtime, configuration and model folders. Runtime downloads are pinned to specific versions and verified with SHA-256 checksums. The managed Lemonade server accepts connections only from your PC and uses a new authentication key each start. Unloading a model releases it from the NPU; quitting Unsloth stops the managed runtime. Set `UNSLOTH_STUDIO_ENABLE_NPU=0` to hide NPU features.

## FAQ

- **Does the NPU replace my GPU?** No — it's a dedicated AI engine; running a model on the NPU keeps GPU compute available for other workloads.
- **Can I run any GGUF on the NPU?** Not directly — this integration uses FastFlowLM's Q4NX models. You can convert supported GGUFs to Q4NX, but loading your own conversions directly from the NPU model list is not yet supported.
- **My NPU isn't showing up** — need a supported AMD XDNA 2 NPU on Windows or Linux x64; Unsloth checks system and gives guidance for driver/firmware issues.

Thanks to AMD and the Lemonade, FastFlowLM and Q4NX converter contributors. AMD also wrote about this on their blog: *Unlocking the AMD Ryzen AI NPU for Unsloth Desktop*.
