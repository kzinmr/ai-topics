---
title: "DGX Spark (Local LLM Server)"
type: concept
created: 2026-04-15
updated: 2026-05-26
tags:
  - local-llm
  - hardware
  - nvidia
  - inference
  - infrastructure
aliases: ["nvidia-dgx-spark", "local-llm-server", "gb10-superchip", "nim-on-spark"]
sources:
  - url: "https://docs.nvidia.com/dgx/dgx-spark/dgx-spark.pdf"
    author: "NVIDIA"
    title: "DGX Spark User Guide"
  - url: "https://build.nvidia.com/spark/nim-llm"
    author: "NVIDIA"
    title: "NIM on Spark | DGX Spark"
  - url: "https://docs.nvidia.com/nemoclaw/latest/"
    author: "NVIDIA"
    title: "NVIDIA NemoClaw Developer Guide"
  - url: "https://dev.to/mrjhsn/the-ultimate-guide-to-local-llm-deployment-on-nvidia-dgx-spark-2026-4jfd"
    author: "Michael Hart"
    title: "The Ultimate Guide to Local LLM Deployment on NVIDIA DGX Spark (2026)"
---


# DGX Spark: Local LLM Server & NemoClaw Setup

**NVIDIA DGX Spark** (Grace Blackwell GB10 Superchip) is a desktop-sized personal AI supercomputer. With 128GB of unified memory (CPU/GPU shared), it can run models up to 200B parameters locally (405B in a dual-Spark configuration).

---

## Hardware Specifications

| Component | Specification |
|-----------|---------------|
| **Architecture** | NVIDIA Grace Blackwell (Integrated CPU/GPU) |
| **CPU** | 20-core Arm (10× Cortex-X925 + 10× Cortex-A725) |
| **GPU** | Blackwell, 5th Gen Tensor Cores, 6,144 CUDA Cores |
| **Memory** | **128 GB LPDDR5x unified** (CPU/GPU shared pool) |
| **Memory Bandwidth** | 273 GB/s |
| **AI Compute** | **1,000 TOPS** (inference), **1 PFLOP** (FP4 w/ sparsity) |
| **Model Support** | Up to 200B params (single), 405B (dual-Spark) |
| **Storage** | 1 TB or 4 TB NVMe M.2 (self-encrypting) |
| **Networking** | 10 GbE RJ-45, 2× QSFP (ConnectX-7 Smart NIC), Wi-Fi 7 |
| **Power/Thermal** | **240W external PSU** (140W SOC TDP). Operating: 5°C–30°C |
| **Form Factor** | 150 × 150 × 50.5 mm, 1.2 kg (2.6 lbs) |

### Spark Stacking (Clustering)
Two DGX Spark units can be connected via QSFP cable (ConnectX-7, 200 Gbps) for distributed inference. Parallel inference runs via MPI + NCCL v2.28.3 over RoCE (RDMA over Converged Ethernet).

---

## NIM (NVIDIA Inference Microservice) Setup

NVIDIA NIM is a containerized microservice that provides GPU inference services on the DGX Spark.

### Prerequisites

```bash
# Verify GPU detection
nvidia-smi

# Verify Docker with GPU support
docker run -it --gpus=all nvcr.io/nvidia/cuda:13.0.1-devel-ubuntu24.04 nvidia-smi

# Add user to docker group (optional)
sudo usermod -aG docker $USER
newgrp docker
```

### NGC Authentication

```bash
export NGC_API_KEY="<YOUR_NGC_API_KEY>"
echo "$NGC_API_KEY" | docker login nvcr.io --username '$oauthtoken' --password-stdin
```

### Launch NIM Container

```bash
export CONTAINER_NAME="nim-llm-demo"
export IMG_NAME="nvcr.io/nim/meta/llama-3.1-8b-instruct-dgx-spark:latest"
export LOCAL_NIM_CACHE=~/.cache/nim
export LOCAL_NIM_WORKSPACE=~/.local/share/nim/workspace
mkdir -p "$LOCAL_NIM_WORKSPACE"
chmod -R a+w "$LOCAL_NIM_WORKSPACE"
mkdir -p "$LOCAL_NIM_CACHE"
chmod -R a+w "$LOCAL_NIM_CACHE"

docker run -it --rm --name=$CONTAINER_NAME \
  --gpus all \
  --shm-size=16GB \
  -e NGC_API_KEY=$NGC_API_KEY \
  -v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \
  -v "$LOCAL_NIM_WORKSPACE:/opt/nim/workspace" \
  -p 8000:8000 \
  $IMG_NAME
```

### Validate (OpenAI-compatible API)

```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "meta/llama-3.1-8b-instruct",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 50
  }'
```

### Available NIM Models for DGX Spark
- **Llama 3.1 8B** — General purpose, coding
- **Qwen3-32** — Multilingual, strong reasoning
- **Nemotron-3-Nano-30B-A3B** — NVIDIA's MoE model (3B active params)
- **MiniMax-M2.5 (229B)** — Dual-Spark required (115 GiB VRAM + KV cache)

---

## NemoClaw Setup on DGX Spark

**NemoClaw** is an open-source reference stack for securely running OpenClaw agents within the NVIDIA OpenShell runtime. It provides sandboxing via Landlock + seccomp + netns, network policy control, and routed inference.

### Prerequisites for NemoClaw

| Resource | Minimum | Recommended |
|---|---|---|
| CPU | 4 vCPU | 4+ vCPU |
| RAM | 8 GB | **16 GB** (DGX Spark has 128 GB — ample) |
| Disk | 20 GB free | 40 GB free |
| OS | Ubuntu 22.04 LTS or later | Ubuntu 24.04 (DGX OS) |
| Node.js | 22.16+ | Latest LTS |
| Container Runtime | Docker | Docker (DGX Spark native) |

### Install & Onboard

```bash
# Run the official installer (auto-installs Node.js if missing)
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

The installer runs a guided wizard that automatically creates an OpenShell gateway, registers inference providers, builds sandbox images, and applies security policies.

### Post-Install Summary

```
──────────────────────────────────────────────────
Sandbox      my-assistant (Landlock + seccomp + netns)
Model        nvidia/nemotron-3-super-120b-a12b (NVIDIA Endpoints)
──────────────────────────────────────────────────
Run:         nemoclaw my-assistant connect
Status:      nemoclaw my-assistant status
Logs:        nemoclaw my-assistant logs --follow
──────────────────────────────────────────────────
```

### Connect & Chat

```bash
# Enter the sandboxed shell
nemoclaw my-assistant connect

# Launch OpenClaw TUI
openclaw tui

# Or send a single CLI message
openclaw agent --agent main --local -m "hello" --session-id test
```

### Inference Routing (Local NIM + NemoClaw)

NemoClaw's onboard wizard allows selecting inference providers including **NVIDIA Endpoints** (cloud API), **OpenAI**, **Anthropic**, **Google Gemini**, and compatible OpenAI/Anthropic endpoints.

To use the local NIM on DGX Spark as NemoClaw's inference backend, specify the local `http://localhost:8000/v1/` as a custom OpenAI-compatible endpoint.

---

## Distributed Agent Architecture: exe.dev + DGX Spark

A distributed architecture where Hermes Agent runs on exe.dev (cloud VM) and uses DGX Spark as an **inference engine and secure execution environment**.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        exe.dev (Cloud VM)                        │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │                    Hermes Agent (Orchestrator)              │  │
│  │  • Session Management (SQLite)                             │  │
│  │  • Tool Orchestration (terminal, web_search, patch, etc.)  │  │
│  │  • Memory (SOUL.md, skill registry)                        │  │
│  │  • Gateway (Discord, Telegram, Slack, CLI)                 │  │
│  │  • Scheduling (cron jobs)                                  │  │
│  └──────────────────────┬─────────────────────────────────────┘  │
│                         │                                        │
│                         │ HTTPS / OpenAI-compatible API           │
└─────────────────────────┼────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                   DGX Spark (Home)                               │
│  ┌─────────────────────────────┐  ┌──────────────────────────┐  │
│  │  NIM Local Inference Server │  │  NemoClaw Sandbox        │  │
│  │  (nvcr.io/nim/...)          │  │  (OpenClaw + OpenShell)  │  │
│  │                             │  │                          │  │
│  │  • OpenAI-compatible API    │  │  • Landlock + seccomp    │  │
│  │  • 128GB unified memory     │  │  • Network policies      │  │
│  │  • Llama 3.1 8B / Qwen3-32  │  │  • Egress control        │  │
│  │  • Nemotron-3-Nano-30B-A3B  │  │  • Credential isolation  │  │
│  └─────────────────────────────┘  └──────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Benefits

| Aspect | Advantage |
|--------|-----------|
| **Security** | Agents run inside NemoClaw sandbox. Filesystem restricted to `/sandbox` and `/tmp`. Network access is policy-controlled |
| **Privacy** | Inference data never leaks to external cloud. Self-contained on local NIM |
| **Performance** | Low-latency inference via 273 GB/s memory bandwidth (Llama 3.1 8B: ~45 tok/s) |
| **Cost** | Initial investment ~$8,000. Monthly electricity ~$50. Breaks even in 6-12 months vs cloud API usage |
| **Flexibility** | Hermes Agent handles orchestration, memory management, and multi-platform coordination on the cloud side |

### Setup Flow

1. **DGX Spark side**: Launch NIM in Docker (`docker run -p 8000:8000 ...`)
2. **DGX Spark side**: Install NemoClaw (`curl ... nemoclaw.sh | bash`)
3. **exe.dev side**: Set inference provider to DGX Spark endpoint in Hermes Agent's config.yaml
4. **exe.dev side**: Connect OpenClaw inside NemoClaw sandbox with Hermes Agent (allow mutual access via network policies)
5. **Both sides**: Establish secure connection via SSH tunnel or Tailscale

### Remote Access via SSH Tunneling

```bash
# From exe.dev, tunnel to DGX Spark
ssh -L 8000:localhost:8000 user@dgx-spark-local-ip

# Verify NIM is accessible
curl http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model": "meta/llama-3.1-8b-instruct", "messages": [{"role": "user", "content": "test"}]}'
```

### NemoClaw Network Policy for External Access

To allow NemoClaw sandbox on DGX Spark to access external services (exe.dev), add the endpoint to the network policy:

```bash
nemoclaw my-assistant policy add --endpoint https://api.exe.dev
```

---

## Cost Analysis: DGX Spark vs Cloud API

| Metric | DGX Spark (Local) | Cloud API |
|--------|-------------------|-----------|
| Initial Cost | ~$8,000 | $0 |
| Monthly Cost | ~$50 (electricity) | $500–$2,000+ |
| Data Privacy | Complete | Limited |
| Latency | 10–50ms | 100–500ms |
| Customization | Full control | Restricted |
| **Break-even** | **~6-12 months** | N/A |

---

## Model Performance on DGX Spark (4-bit Quantization)

| Model | Parameters | Throughput | Best Use Case |
|-------|------------|------------|---------------|
| Llama 3.1 8B | 8B | ~45 tok/s | General purpose, coding |
| Mistral 7B v0.3 | 7B | ~52 tok/s | Instruction following |
| Qwen 2.5 7B | 7B | ~48 tok/s | Multilingual tasks |
| CodeLlama 13B | 13B | ~28 tok/s | Programming assistance |
| Nemotron-3-Nano-30B-A3B | 30B (3B active) | ~35 tok/s | Reasoning, tool calling |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Insufficient VRAM** | Switch to quantized variants (e.g., `ollama pull llama3.1:8b-q4_0`) |
| **OOM during sandbox build** | Configure ≥8 GB swap on the host |
| **`nemoclaw` not found** | Run `source ~/.bashrc` or open a new terminal (nvm/fnm PATH issue) |
| **Model loading errors** | Clear corrupted cache: `rm -rf ~/.cache/nim` and re-pull |
| **Slow inference** | Verify GPU detection with `nvidia-smi`, check thermal throttling |

---

## References

- [NVIDIA DGX Spark Documentation](https://docs.nvidia.com/dgx/dgx-spark/)
- [DGX Spark User Guide (PDF)](https://docs.nvidia.com/dgx/dgx-spark/dgx-spark.pdf)
- [NIM on Spark Playbook](https://build.nvidia.com/spark/nim-llm)
- [NemoClaw GitHub Repository](https://github.com/NVIDIA/NemoClaw/)
- [NemoClaw Developer Guide](https://docs.nvidia.com/nemoclaw/latest/)
- [Nemotron-3-Nano with llama.cpp Playbook](https://build.nvidia.com/spark/nemotron)
