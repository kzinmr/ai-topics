---
title: NVIDIA DGX Spark
aliases: [dgx-spark, project-digits, gb10-spark, nvidia-dgx-spark]
created: 2026-04-15
updated: 2026-04-15
status: L2
sources:
  - https://www.nvidia.com/en-us/products/workstations/dgx-spark
  - https://docs.nvidia.com/dgx/dgx-spark
  - https://build.nvidia.com/spark
  - https://github.com/NVIDIA/dgx-spark-playbooks
tags: [entity, hardware, local-llm, nvidia, inference]
---

# NVIDIA DGX Spark

Personal AI supercomputer powered by the NVIDIA GB10 Grace Blackwell Superchip. Designed for developers, data scientists, and researchers to prototype, fine-tune, and deploy AI models locally. Officially began shipping October 2025. Previously codenamed "Project DIGITS."

> *"For 128GB of unified memory dedicated to inference, that changed the calculation."* — Mirek Fokt, March 2026

## Hardware Specifications

| Component | Specification |
|-----------|---------------|
| **SoC** | NVIDIA GB10 Grace Blackwell Superchip |
| **CPU** | 20-core Arm (10× Cortex-X925 + 10× Cortex-A725) |
| **GPU** | Blackwell Architecture, 5th Gen Tensor Cores, 4th Gen RT Cores |
| **Memory** | 128 GB LPDDR5x Coherent Unified System Memory (256-bit, 273 GB/s) |
| **Storage** | 4 TB NVMe M.2 (self-encrypting) |
| **Networking** | ConnectX-7 NIC @ 200 Gbps, 10 GbE Ethernet, Wi-Fi 7, BT 5.4 |
| **I/O** | 4× USB-C, 1× HDMI 2.1a, NVENC/NVDEC |
| **Power** | 240W PSU, 140W TDP (GB10) |
| **Dimensions** | 150mm × 150mm × 50.5mm, 1.2 kg |
| **OS** | NVIDIA DGX OS (Ubuntu 24.04 Noble, aarch64) |
| **Noise** | 35 dB operating (max GPU stress), 19 dB idle |
| **Product ID** | 940-54242-0000-000 |

## Key Architectural Advantage: Coherent Unified Memory

DGX Spark's 128 GB is **coherent unified system memory** — shared between CPU and GPU without PCIe transfer overhead. This eliminates the VRAM bottleneck that limits consumer GPUs (24GB on RTX 4090) and enables running models up to 200B parameters locally (405B with dual-Spark configuration).

## AI Performance Benchmarks

### Inference (ISL|OSL = 2048|128, BS=1)

| Model | Precision | Backend | Prompt Tok/s | Gen Tok/s |
|-------|-----------|---------|-------------|-----------|
| Qwen3 14B | NVFP4 | TRT-LLM | 5,928.95 | 522.71 |
| GPT-OSS-20B | MXFP4 | llama.cpp | 3,670.42 | 282.74 |
| GPT-OSS-120B | MXFP4 | llama.cpp | 1,725.47 | 55.37 |
| Llama 3.1 8B | NVFP4 | TRT-LLM | 10,256.9 | 38.65 |
| Qwen2.5-VL-7B-Instruct | NVFP4 | TRT-LLM | 65,831.7 | 741.71 |
| Qwen3 235B (dual Spark) | NVFP4 | TRT-LLM | 23,477.0 | 11.73 |

### Fine-Tuning (Seq len: 2048, Epoch: 1, Steps: 64)

| Model | Method | Throughput |
|-------|--------|------------|
| Llama 3.2 3B | Full fine-tuning | 82,739.2 tok/s |
| Llama 3.1 8B | LoRA | 53,657.6 tok/s |
| Llama 3.3 70B | QLoRA | 5,079.4 tok/s |

### Image Generation

| Model | Precision | Backend | Config | Performance |
|-------|-----------|---------|--------|-------------|
| Flux.1 12B Schnell | FP4 | TensorRT | 1024×1024, 4 steps, BS=1 | 1 image / 2.6 sec |
| SDXL 1.0 | BF16 | TensorRT | 1024×1024, 50 steps, BS=2 | 7 images / min |

### Dual-System Scaling

Two DGX Sparks linked via ConnectX-7 can run **Qwen3 235B (NVFP4)**, demonstrating horizontal scaling capability for models exceeding single-unit memory.

## Software Ecosystem

### Preinstalled Stack
- CUDA-X (cuML, cuDF, etc.) — zero-code-change acceleration for scikit-learn/pandas workflows
- TRT-LLM — optimized inference engine
- NVIDIA NIM — containerized microservices for model serving
- DGX Dashboard — system monitoring, updates, and management

### Supported Local LLM Frameworks
- **Ollama** — simplest path for local inference (GGUF models)
- **vLLM** — production-grade serving with PagedAttention
- **llama.cpp** — CPU/GPU hybrid inference, GGUF support
- **SGLang** — high-performance inference engine
- **Unsloth** — fast fine-tuning
- **LM Studio** — GUI-based model management
- **NVIDIA NIM** — containerized microservice deployment

### AI Workflow Playbooks (40+ available)
- **Data Science:** CUDA-X acceleration, UMAP, HDBSCAN (zero code changes)
- **Fine-Tuning:** NeMo, Unsloth, LLaMA Factory, PyTorch
- **Inference:** vLLM, TRT-LLM, SGLang, NVFP4 quantization
- **Agents:** NemoClaw + Telegram, OpenClaw, Multi-Agent Chatbot, VSS Agent
- **Vision:** Live VLM WebUI, Isaac Sim & Isaac Lab
- **DevOps:** VS Code remote, NCCL for multi-Spark

## NemoClaw Integration

DGX Spark is the **reference platform** for NemoClaw — NVIDIA's secure agent development stack. The combination enables:

- Running Nemotron 3 Super 120B locally (~87 GB for Ollama GGUF)
- OpenShell sandbox with Landlock + seccomp + netns isolation
- Telegram bot integration for always-on agent access
- Web dashboard at `http://127.0.0.1:18789`

See [[concepts/local-llm-server-dgx-spark]] for the complete setup guide.

## Market Positioning

| Aspect | DGX Spark | Consumer GPU (RTX 4090) | Cloud API |
|--------|-----------|------------------------|-----------|
| **Unified Memory** | 128 GB | 24 GB | N/A |
| **Peak AI Compute** | 1 PFLOP (FP4) | ~660 TFLOP (FP4) | Unlimited |
| **Form Factor** | Desktop (1.2 kg) | Full-size GPU | Remote |
| **Price** | ~$4,000–$4,700 | ~$1,600–$2,000 | Pay-per-token |
| **Data Privacy** | Complete | Complete | Limited |
| **Max Local Model** | ~200B params | ~14B–30B (quantized) | N/A |
| **Monthly Running Cost** | ~$50 (electricity) | ~$30–$50 | $500–$2,000+ |

## Timeline

| Date | Milestone |
|------|-----------|
| Oct 2025 | Official shipping begins |
| Jan 2026 | Software update delivers 2x performance + open AI model support |
| Feb 2026 | AI Photo Booth demo at CES (Reachy Mini + Hugging Face) |
| Mar 2026 | NemoClaw alpha released with DGX Spark support |
| Apr 2026 | DGX Spark Playbooks repo reaches 40+ recipes |

## Related

- [[entities/nvidia-nemoclaw]] — NemoClaw secure agent framework
- [[concepts/local-llm-server-dgx-spark]] — Setup guide for local LLM server
- [[concepts/local-llm]] — Local LLM inference overview
- [[entities/jensen-huang]] — NVIDIA CEO, physical AI advocate
