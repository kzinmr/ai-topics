---
title: NVIDIA NemoClaw
aliases: [nemoclaw, nemo-claw]
created: 2026-04-15
updated: 2026-04-15
status: L2
sources:
  - https://github.com/NVIDIA/NemoClaw
  - https://nemoclawai.io/blog/getting-started-nemoclaw-dgx-spark/
  - https://build.nvidia.com/spark/nemoclaw/instructions
tags: [entity, ai-agents, local-llm, nvidia, security, dgx-spark]
---

# NVIDIA NemoClaw

NVIDIA NemoClaw is a secure AI agent development framework designed for running AI agents with enterprise-grade isolation. It bundles **OpenShell** (sandbox runtime), **OpenClaw** (agent framework), a **Privacy Router** (data routing control), and a **Network Policy Engine** (deny-by-default networking). The stack is designed to run locally on hardware like the DGX Spark, with full support for local inference via Ollama.

Official GitHub: https://github.com/NVIDIA/NemoClaw (19K+ stars)

## Architecture

```
DGX Spark (Ubuntu 24.04, aarch64, cgroup v2, 128 GB unified memory)
  └── Docker (28.x/29.x)
       └── OpenShell gateway container
            └── k3s (embedded)
                 └── nemoclaw sandbox pod
                      └── OpenClaw agent + NemoClaw plugin
```

### Core Components

| Component | Purpose |
|-----------|---------|
| **OpenShell** | Sandbox runtime with Landlock + seccomp + netns isolation. Embeds k3s inside Docker. |
| **OpenClaw** | Agent framework for building and running AI agents. Supports CLI, TUI, and web UI. |
| **Privacy Router** | Controls data routing between local and cloud endpoints. Default route: local. |
| **Network Policy Engine** | Deny-by-default networking with explicit allowlists for specific domains. |
| **Nemotron Policy Engine** | Nemotron 120B MoE (INT4, ~35GB) used for policy evaluation, intent classification, and PII detection. |

## Key Features

### Security Model
- **Sandbox isolation**: Each agent runs in an isolated OpenShell sandbox
- **Landlock + seccomp + netns**: Multi-layer security confinement
- **Deny-by-default network policy**: Explicit allowlists required for outbound connections
- **PII redaction**: Automatic detection and redaction of sensitive data in logs
- **Audit logging**: Immutable audit logs for all agent actions

### Local Inference Support
- **Ollama integration**: Run models locally on DGX Spark's GPU
- **Supported models**: Nemotron 3 Super 120B, Nemotron 120B MoE (INT4 quantized)
- **No API key required**: Fully local operation with proper hardware
- **Model size**: ~87 GB for 120B parameter GGUF models

### Agent Framework
- **Blueprint system**: Pre-built agent configurations (customer-support, sales-ops, security-ops, infra-management, code-review, data-pipeline)
- **Concurrent tasks**: Support for up to 8 concurrent agent tasks
- **Human approval workflows**: Operator approval for high-risk actions
- **Web dashboard**: Real-time monitoring at `http://127.0.0.1:18789`

## Installation on DGX Spark

### Prerequisites
- DGX Spark (Ubuntu 24.04, cgroup v2)
- Docker 24.0+ with NVIDIA Container Toolkit
- 50GB+ free disk space
- Node.js 22 (auto-installed)

### Quick Install
```bash
# One-line installation
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash

# Or clone and install manually
git clone https://github.com/NVIDIA/NemoClaw.git
cd NemoClaw
./install.sh
```

### Onboarding Wizard
The installer prompts for:
1. Sandbox name (lowercase alphanumeric + hyphens)
2. Inference provider (Local Ollama, NVIDIA NIM, etc.)
3. Model selection
4. Policy presets

### Verification
```bash
# Check sandbox is running
nemoclaw my-assistant connect

# Test agent interaction
openclaw agent --agent main --local -m "hello" --session-id test

# Verify local inference
curl -sf https://inference.local/v1/models
```

## Configuration

### Basic Config (`nemoclaw.yaml`)
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
    isolationLevel: standard
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
        methods: [GET]
```

## Telegram Integration

```bash
# Add network policy for Telegram
nemoclaw my-assistant policy-add  # Select telegram, confirm Y

# Set bot token and start
export TELEGRAM_BOT_TOKEN=<your-bot-token>
nemoclaw start

# Verify
nemoclaw status
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **cgroup v2 kills k3s** | Resolved in current OpenShell (`cgroupns=host` auto-set) |
| **Docker permission denied** | `sudo usermod -aG docker $USER && newgrp docker` |
| **CoreDNS CrashLoop** | Fixed in `fix-coredns.sh` (uses gateway IP) |
| **Image pull failure** | `openshell gateway destroy && openshell gateway start` |
| **Port 3000 conflict** | AI Workbench Traefik uses 3000; use alternate ports |
| **Gateway not auto-starting after reboot** | Run `nemoclaw start` manually or enable systemd service |

## Uninstall

```bash
cd ~/.nemoclaw/source
./uninstall.sh

# Full wipe (removes models too)
./uninstall.sh --yes --delete-models
```

**Note:** Uninstaller removes sandboxes, gateway, npm package, Docker artifacts, and state dirs. Preserves Docker, Node.js, npm, Ollama binaries.

## Related

- [[entities/nvidia-dgx-spark]] — DGX Spark hardware platform
- [[entities/peter-steinberger]] — OpenClaw creator, OpenAI
- [[concepts/local-llm-server-dgx-spark]] — Complete DGX Spark setup guide
- [[concepts/local-llm]] — Local LLM inference overview
- [[concepts/capabilities-based-security]] — Security philosophy matching NemoClaw's approach
