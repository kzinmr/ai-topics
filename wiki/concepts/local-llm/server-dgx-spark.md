---
title: Local LLM Server Setup on DGX Spark
aliases: [dgx-spark-setup, local-llm-server, nemoclaw-setup-guide]
created: 2026-04-15
updated: 2026-04-15
status: L2
sources:
  - https://docs.nvidia.com/dgx/dgx-spark
  - https://build.nvidia.com/spark
  - https://github.com/NVIDIA/NemoClaw/blob/main/spark-install.md
  - https://nemoclawai.io/blog/getting-started-nemoclaw-dgx-spark/
  - https://build.nvidia.com/spark/nemoclaw/instructions
tags: [concept, setup-guide, local-llm, dgx-spark, nemoclaw, nvidia]
---

# Local LLM Server Setup on DGX Spark

Complete setup guide for running a local LLM server on NVIDIA DGX Spark, with focus on NemoClaw integration for secure AI agent development.

## Hardware Overview

The DGX Spark is NVIDIA's personal AI supercomputer powered by the GB10 Grace Blackwell Superchip:
- **CPU**: 20-core Arm (10× Cortex-X925 + 10× Cortex-A725)
- **GPU**: Blackwell architecture, 5th Gen Tensor Cores
- **Memory**: 128 GB LPDDR5x Coherent Unified System Memory (273 GB/s)
- **Storage**: 4 TB NVMe M.2 (self-encrypting)
- **OS**: Ubuntu 24.04 Noble (aarch64)
- **Power**: 240W PSU, 140W TDP
- **Form Factor**: 150mm × 150mm × 50.5mm, 1.2 kg

The coherent unified memory eliminates the VRAM bottleneck, enabling local inference of models up to 200B parameters (405B with dual-Spark configuration).

## Setup Overview

```
DGX Spark → Docker → OpenShell (k3s) → Sandbox → OpenClaw Agent
           ↓
      Ollama (Local Inference)
           ↓
   Nemotron 120B MoE (INT4, ~87GB)
```

## Phase 1: Initial Setup & Prerequisites

### 1.1 Unboxing & First Boot
1. Connect power (240W adapter), Ethernet, and display (HDMI)
2. Power on — DGX OS (Ubuntu 24.04) boots automatically
3. Complete initial setup via DGX Dashboard or SSH

### 1.2 Configure Docker & NVIDIA Container Runtime
OpenShell's gateway embeds k3s inside Docker and requires host cgroup namespace access:

```bash
# Set NVIDIA runtime
sudo nvidia-ctk runtime configure --runtime=docker

# Configure cgroup v2 host mode
sudo python3 -c "
import json, os
path = '/etc/docker/daemon.json'
d = json.load(open(path)) if os.path.exists(path) else {}
d['default-cgroupns-mode'] = 'host'
json.dump(d, open(path, 'w'), indent=2)
"

# Restart & verify
sudo systemctl restart docker
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

**Permission Fix:** If `docker` commands fail with permission errors:
```bash
sudo usermod -aG docker $USER
newgrp docker
```

### 1.3 Install Ollama for Local Inference
```bash
curl -fsSL https://ollama.com/install.sh | sh

# Bind to all interfaces (required for sandbox access)
sudo mkdir -p /etc/systemd/system/ollama.service.d
printf '[Service]\nEnvironment="OLLAMA_HOST=0.0.0.0"\n' | sudo tee /etc/systemd/system/ollama.service.d/override.conf
sudo systemctl daemon-reload
sudo systemctl restart ollama

# Verify
curl http://0.0.0.0:11434  # Expected: "Ollama is running"
```

### 1.4 Pull & Pre-load Model
```bash
# Pull Nemotron 3 Super 120B (~87 GB, 15-30 min download)
ollama pull nemotron-3-super:120b

# Pre-load weights to unified memory
ollama run nemotron-3-super:120b
# Type /bye to exit after model loads

# Verify
ollama list
```

## Phase 2: NemoClaw Installation

### 2.1 Quick Install
```bash
# One-line installation
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash

# Or clone and install manually
git clone https://github.com/NVIDIA/NemoClaw.git
cd NemoClaw
./install.sh
```

### 2.2 Onboarding Wizard
The installer prompts for:
1. **Sandbox name**: lowercase alphanumeric + hyphens (e.g., `my-assistant`)
2. **Inference provider**: Select `Local Ollama` (option 7)
3. **Model**: Select `nemotron-3-super:120b` (option 1)
4. **Policy presets**: Accept defaults (Y)

**IMPORTANT**: Save the tokenized Web UI URL printed at completion:
`http://127.0.0.1:18789/#token=<long-token>`

If `nemoclaw` command not found after install:
```bash
source ~/.bashrc
```

### 2.3 Verify Installation
```bash
# Check sandbox is running
nemoclaw my-assistant connect

# Inside sandbox, test agent
openclaw agent --agent main --local -m "hello" --session-id test

# Verify local inference from sandbox
curl -sf https://inference.local/v1/models
```

## Phase 3: Access & Monitoring

### 3.1 Web Dashboard
Access at `http://127.0.0.1:18789/#token=<your-gateway-token>`

**⚠️ CRITICAL**: Use `127.0.0.1`, NOT `localhost` — gateway origin check requires exact match.

### 3.2 Remote Access via SSH Tunnel
```bash
# On DGX Spark host
hostname -I | awk '{print $1}'  # Get IP (e.g., 192.168.1.42)
openshell forward start 18789 my-assistant --background

# On remote machine (Mac/Linux)
ssh -L 18789:127.0.0.1:18789 <user>@<spark-ip>
# Open: http://127.0.0.1:18789/#token=<long-token>
```

### 3.3 Interactive TUI
```bash
openclaw tui
# Exit: Ctrl+C
```

## Phase 4: Telegram Bot Integration

### 4.1 Create Bot
1. Open Telegram, find `@BotFather`
2. Send `/newbot` and follow prompts
3. Copy the bot token

### 4.2 Configure NemoClaw
```bash
# Add Telegram network policy
nemoclaw my-assistant policy-add  # Select telegram, confirm Y

# Start bridge
export TELEGRAM_BOT_TOKEN=<your-bot-token>
nemoclaw start

# Verify
nemoclaw status
```

### 4.3 Test
Message your bot on Telegram → agent replies (30-90s initial latency for local 120B model)

**Troubleshooting**: If bridge missing in status, ensure `TELEGRAM_BOT_TOKEN` is exported in the same shell session. Restart: `nemoclaw stop` → `export ...` → `nemoclaw start`

## Configuration Reference

### Basic `nemoclaw.yaml`
```yaml
apiVersion: nemoclaw.nvidia.com/v1
kind: NemoClawConfig
metadata:
  name: my-first-deployment
spec:
  model:
    provider: local
    name: nemotron-120b-moe
    quantization: int4
    gpuLayers: all
  openshell:
    enabled: true
    isolationLevel: standard  # standard | strict | paranoid
    auditLog: true
  privacyRouter:
    enabled: true
    defaultRoute: local
  networkPolicy:
    enabled: true
    defaultAction: deny
    allowlist:
      - "*.internal.company.com"
  agent:
    framework: openclaw
    version: "3.13"
    maxConcurrentTasks: 8
```

### Network Policy Example
```yaml
networkPolicy:
  egress:
    allow:
      - domain: "api.zendesk.com"
        methods: [GET, POST, PUT]
        headers:
          required: ["Authorization"]
      - domain: "api.stripe.com"
        methods: [GET]  # Read-only
```

## Performance Expectations

| Metric | Value |
|--------|-------|
| **First Response Latency** | 30-90 seconds (local 120B model) |
| **Memory Usage** | ~87 GB for 120B GGUF model |
| **Power Consumption** | ~140W under load |
| **Max Model Size** | ~200B parameters (single unit) |
| **Dual-Spark Scaling** | Up to 405B parameters |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **cgroup v2 kills k3s** | ✅ Resolved in current OpenShell (`cgroupns=host` auto-set) |
| **Docker permission denied** | `sudo usermod -aG docker $USER && newgrp docker` |
| **CoreDNS CrashLoop** | ✅ Fixed in `fix-coredns.sh` (uses gateway IP) |
| **Image pull failure** | `openshell gateway destroy && openshell gateway start` |
| **GPU passthrough** | ⚠️ Untested; should work with `--gpu` if NVIDIA Container Toolkit configured |
| **`pip install` fails** | Use `venv` (recommended) or `--break-system-packages` (last resort) |
| **Port 3000 conflict** | AI Workbench Traefik uses 3000/10000; use alternate ports |
| **Network blocks cloud API** | Ensure `integrate.api.nvidia.com` allowed in sandbox network policy |
| **Gateway not auto-starting after reboot** | Run `nemoclaw start` manually or enable systemd service |

## Uninstall

```bash
cd ~/.nemoclaw/source
./uninstall.sh

# Full wipe (removes models too)
./uninstall.sh --yes --delete-models
```

**Note:** Uninstaller removes sandboxes, gateway, npm package, Docker artifacts, and state dirs (`~/.nemoclaw`, `~/.config/openshell`, `~/.config/nemoclaw`). Preserves Docker, Node.js, npm, Ollama binaries.

## Essential Commands

| Command | Purpose |
|---------|---------|
| `nemoclaw <name> connect` | Enter sandbox shell |
| `nemoclaw <name> status` | Show sandbox status & inference config |
| `nemoclaw list` | List all registered sandboxes |
| `nemoclaw start` | Start auxiliary services (Telegram bridge, cloudflared) |
| `nemoclaw stop` | Stop all services |
| `nemoclaw uninstall` | Remove all NemoClaw components |
| `openclaw agent --agent main --local -m "message"` | Test agent interaction |
| `openclaw tui` | Interactive terminal UI |

## Related

- [[entities/nvidia-dgx-spark]] — DGX Spark hardware specifications
- [[entities/nvidia-nemoclaw]] — NemoClaw secure agent framework
- [[concepts/local-llm/_index]] — Local LLM Ecosystem Overview
- [[../../capabilities-based-security]] — Security philosophy matching NemoClaw's approach
