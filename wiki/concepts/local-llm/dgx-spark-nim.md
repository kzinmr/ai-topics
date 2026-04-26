---
title: "DGX Spark (Local LLM Server)"
type: concept
created: 2026-04-15
updated: 2026-04-15
tags: [local-llm, dgx-spark, nvidia, inference, nemo-claw, openshell, hardware, self-hosting]
aliases: ["nvidia-dgx-spark", "local-llm-server", "gb10-superchip", "nim-on-spark"]
related: [[self-hosting-ai-development]], [[ollama]], [[llama-cpp]], [[inference/vllm]], [[openclaw]]
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

**NVIDIA DGX Spark** (Grace Blackwell GB10 Superchip) は、デスクトップサイズのパーソナルAIスーパーコンピュータ。128GBの統一メモリ（CPU/GPU共有）を持ち、最大200Bパラメータのモデル（405Bは2台構成）をローカルで実行可能。

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
2台のDGX SparkをQSFPケーブル（ConnectX-7, 200 Gbps）で接続し、分散推論が可能。RoCE（RDMA over Converged Ethernet）経由でMPI + NCCL v2.28.3による並列推論を実行。

---

## NIM (NVIDIA Inference Microservice) Setup

NVIDIA NIMは、DGX Spark上でGPU推論サービスを提供するコンテナ型マイクロサービス。

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

**NemoClaw**は、OpenClawエージェントをNVIDIA OpenShellランタイム内でセキュアに実行するためのオープンソースリファレンススタック。Landlock + seccomp + netnsによるサンドボックス化、ネットワークポリシー制御、ルーティング済み推論を提供。

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

インストーラーはガイド付きウィザードを実行し、OpenShellゲートウェイの作成、推論プロバイダーの登録、サンドボックスイメージのビルド、セキュリティポリシーの適用を自動的に行う。

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

NemoClawのonboardウィザードでは、推論プロバイダーとして **NVIDIA Endpoints**（クラウドAPI）、**OpenAI**、**Anthropic**、**Google Gemini**、および互換OpenAI/Anthropicエンドポイントを選択可能。

DGX Spark上のローカルNIMをNemoClawの推論バックエンドとして使用する場合、カスタムOpenAI互換エンドポイントとしてローカルの`http://localhost:8000/v1/`を指定できる。

---

## Distributed Agent Architecture: exe.dev + DGX Spark

Hermes Agentをexe.dev（クラウドVM）で実行し、DGX Sparkを**推論エンジン兼セキュア実行環境**として利用する分散アーキテクチャ。

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
| **Security** | NemoClawサンドボックス内でエージェントが実行。ファイルシステムは`/sandbox`と`/tmp`に制限。ネットワークアクセスはポリシー制御 |
| **Privacy** | 推論データが外部クラウドに流出しない。ローカルNIMで完結 |
| **Performance** | 273 GB/sメモリーバンド幅による低レイテンシー推論（Llama 3.1 8B: ~45 tok/s） |
| **Cost** | 初期投資 ~$8,000。月間電気代 ~$50。6-12ヶ月でクラウドAPI利用と比較してブレークイーブン |
| **Flexibility** | Hermes Agentはクラウド側でオーケストレーション・メモリ管理・マルチプラットフォーム連携を担当 |

### Setup Flow

1. **DGX Spark側**: NIMをDockerで起動（`docker run -p 8000:8000 ...`）
2. **DGX Spark側**: NemoClawをインストール（`curl ... nemoclaw.sh | bash`）
3. **exe.dev側**: Hermes Agentのconfig.yamlで推論プロバイダーをDGX Sparkのエンドポイントに設定
4. **exe.dev側**: NemoClawサンドボックス内のOpenClawとHermes Agentを連携（ネットワークポリシーで相互アクセスを許可）
5. **両側**: SSHトンネルまたはTailscaleでセキュア接続を確立

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

DGX Spark上のNemoClawサンドボックスから外部（exe.dev）へのアクセスを許可するため、ネットワークポリシーにエンドポイントを追加:

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
