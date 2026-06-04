---
name: dgx-spark-nemoclaw-setup
description: Guide for setting up DGX Spark local LLM server with NemoClaw sandbox and distributed agent architecture (exe.dev orchestration + remote inference).
category: mlops
---

# DGX Spark + NemoClaw Setup Guide

## Hardware Overview
- **DGX Spark**: NVIDIA Grace Blackwell GB10 Superchip
- **Memory**: 128GB unified memory (CPU+GPU), 273 GB/s bandwidth
- **Compute**: 1 PFLOP (FP4), up to 200B parameter models locally
- **Multi-GPU**: 2 units stackable for 405B models via ConnectX-7 RoCE
- **Network**: 2x 400GbE, Wi-Fi 7, 2.5GbE, Thunderbolt 4
- **Cost**: ~$8,000 USD, ~$50/month electricity

## Quick Setup

### 1. NIM Inference Server
```bash
docker run --rm -it --gpus all -e NIM_MODEL=nvidia/nemotron-3-nano-30b-a3b \
  -p 8000:8000 nvcr.io/nim/nvidia/nemotron-3-nano-30b-a3b:latest
```
- OpenAI-compatible API on port 8000
- Models: Llama 3.1 8B (~45 tok/s), Qwen3-32, Nemotron-3-Nano-30B-A3B

### 2. NemoClaw Setup
```bash
curl -fsSL https://nemo.nvidia.com/nemoclaw.sh | bash
```
- Installs: OpenShell + OpenClaw + sandbox environment
- Security: Landlock + seccomp + netns isolation
- Default: Nemotron-3-Super-120B-A12B (NVIDIA endpoints)

## Distributed Agent Architecture

### exe.dev (Orchestration) → DGX Spark (Inference + Sandbox)
```
┌──────────────┐           HTTPS / OpenAI API          ┌──────────────────┐
│  exe.dev     │ ───────────────────────────────────►  │  DGX Spark (家)  │
│ Hermes Agent │                                     │ ┌──────────────┐ │
│ (orchestrate)│                                     │ │  NIM Server  │ │
│              │                                     │ │ (inference)  │ │
│ Discord/     │                                     │ └──────────────┘ │
│ Telegram/CLI │                                     │ ┌──────────────┐ │
│              │                                     │ │ NemoClaw     │ │
└──────────────┘                                     │ │ (sandbox)    │ │
                                                     │ └──────────────┘ │
                                                     └──────────────────┘
```

### Connection Options
1. **Tailscale**: Zero-config VPN, recommended for home server access
2. **Cloudflare Tunnel**: `cloudflared tunnel --url http://localhost:8000`
3. **SSH Tunnel**: `ssh -L 8000:localhost:8000 user@home-server`

### Hermes Agent Configuration
```yaml
# ~/.hermes/config.yaml
model: "custom/dgx-spark"
provider:
  base_url: "https://home-server.local:8000/v1"
  api_key: "your-api-key"
```

## NemoClaw Custom Provider
Point to local NIM instead of NVIDIA endpoints:
```bash
export NIM_MODEL_ENDPOINT="http://localhost:8000/v1"
nemoclaw run --provider openai-compat
```

## Cost Analysis
- **Break-even**: 6-12 months vs cloud API ($500-2,000/month)
- **Savings**: ~$6,000/year after break-even
- **Privacy**: All data stays local, no API rate limits

## Wiki Page
- Location: `wiki/concepts/dgx-spark-local-llm-server.md`
- Related: `wiki/concepts/nemoclaw.md` (if exists)

## Pitfalls
- DGX Spark requires Linux kernel 6.8+ for GB10 support
- NemoClaw sandbox needs root for Landlock setup
- Network latency matters — keep orchestration and inference close
- Firewall rules must allow port 8000 for NIM API
- Model download requires NVIDIA NGC account