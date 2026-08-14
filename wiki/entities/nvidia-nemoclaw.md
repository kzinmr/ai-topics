---
title: NVIDIA NemoClaw
type: entity
aliases: [nemoclaw, nemo-claw]
created: 2026-04-15
updated: 2026-08-14
sources:
  - https://github.com/NVIDIA/NemoClaw
  - https://docs.nvidia.com/nemoclaw/latest/
  - https://docs.nvidia.com/nemoclaw/latest/about/ecosystem.html
  - https://nemoclawai.io/blog/getting-started-nemoclaw-dgx-spark/
  - https://build.nvidia.com/spark/nemoclaw/instructions
tags: [entity, ai-agents, local-llm, nvidia, security, hardware, sandbox, agent-runtime, open-source]
related:
  - entities/nvidia-openshell
  - entities/nvidia-dgx-spark
  - entities/peter-steinberger
  - entities/openclaw
  - entities/hermes-agent
  - concepts/security-and-governance/agent-sandboxing
  - concepts/harness-engineering
---

# NVIDIA NemoClaw

NVIDIA NemoClaw is an open-source **reference stack for sandboxed AI agents** — an Apache-2.0 project that runs supported agents (OpenClaw by default, plus Hermes and LangChain Deep Agents Code) more safely inside **OpenShell** containers. It combines a host CLI, a versioned blueprint, an agent-specific integration layer, managed inference, network policy, MCP server management, snapshots, and lifecycle operations. The stack is designed to run locally on hardware like the DGX Spark, with full support for local inference via Ollama, vLLM, llama.cpp, and NVIDIA NIM.

Official GitHub: https://github.com/NVIDIA/NemoClaw (22K+ stars, 3K+ forks, active daily releases)

> **Positioning**: NemoClaw sits *above* OpenShell — it calls OpenShell APIs/CLI to create and configure the sandbox that runs the agent. OpenShell is the execution environment (sandbox lifecycle, network/filesystem/process policy, inference routing); NemoClaw is the NVIDIA reference stack on the host (`nemoclaw` CLI, versioned blueprint, managed inference, MCP servers, messaging channels, host readiness, lifecycle operations). If you want maximum flexibility with custom images, use OpenShell directly; if you want a tested, hardened OpenClaw/Hermes/Deep-Agents setup, use NemoClaw.

## Supported Agents

| Agent | Status | Guide |
|-------|--------|-------|
| **OpenClaw** | Default | [Quickstart with OpenClaw](https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html) |
| **Hermes** | Supported | [Quickstart with Hermes](https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart-hermes.html) |
| **LangChain Deep Agents Code** | Supported | [Quickstart with Deep Agents](https://docs.nvidia.com/nemoclaw/latest/user-guide/deepagents/get-started/quickstart.html) |

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
- **Credential custody**: Inference credentials and managed MCP bearer values live *outside* the sandbox — OpenShell replaces real credentials with placeholder tokens at egress via its L7 proxy; NemoClaw auto-creates providers during onboarding and filters sensitive host env vars (API keys, `DISCORD_BOT_TOKEN`, `SLACK_BOT_TOKEN`, `TELEGRAM_BOT_TOKEN`) from sandbox creation commands to prevent leakage through build args
- **Process limits**: Best-effort `ulimit -u 512` applied in the container entrypoint
- **Sandbox hardening**: Capability drops, `setpriv` privilege transitions (replacing legacy gosu), corporate CA trust staging, credential rotation, trusted computing base reviews (including OpenShell 0.0.71/0.0.72 security reviews)

### Local Inference Support
- **Ollama integration**: Run models locally on DGX Spark's GPU
- **vLLM, llama.cpp, NVIDIA NIM**: Supported local inference servers (incl. two-node DGX Spark / DGX Station setups)
- **Supported models**: Nemotron 3 Super 120B, Nemotron 120B MoE (INT4 quantized), Nemotron 3.5 Lightning
- **No API key required**: Fully local operation with proper hardware
- **Model size**: ~87 GB for 120B parameter GGUF models
- **Managed inference routing**: `inference.local` route with provider validation, model capability audit, timeouts, and shared gateway routes

### Agent Framework
- **Blueprint system**: Pre-built agent configurations (customer-support, sales-ops, security-ops, infra-management, code-review, data-pipeline)
- **Concurrent tasks**: Support for up to 8 concurrent agent tasks
- **Human approval workflows**: Operator approval for high-risk actions
- **Web dashboard**: Real-time monitoring at `http://127.0.0.1:18789`
- **MCP server management**: Authenticated HTTPS Streamable HTTP MCP servers for all supported agent runtimes, with credential placeholders replaced at approved egress boundaries
- **Snapshots & recovery**: Create/restore snapshots, rebuild/recover sandboxes, host readiness reporting
- **Messaging channels**: Telegram, Discord, Slack, WhatsApp (QR-paired sessions) with channel-specific policy

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

## Release Cadence

NemoClaw is an **alpha project** with near-daily release notes (v0.0.108 as of August 12, 2026). Recent highlights include: read-only host mounts (`--host-mount`), an Experimental **Muse Glimmer** managed vLLM profile for one DGX Spark, onboarding recovery improvements, messaging credential rotation, stricter inference validation, MCP registration into the OpenClaw workspace config, Hermes configuration validation, and hardened managed images (Node.js 22.23.2, `setpriv`, BuildKit attestation verification, Sigstore auditing).

## Related

- [[entities/nvidia-openshell]] — OpenShell sandbox runtime, the layer below NemoClaw
- [[entities/nvidia-dgx-spark]] — DGX Spark hardware platform
- [[entities/peter-steinberger]] — OpenClaw creator, OpenAI
- [[entities/hermes-agent]] — Hermes agent runtime, supported by NemoClaw
- [[concepts/local-llm/server-dgx-spark]] — Complete DGX Spark setup guide
- [[concepts/local-llm/_index]] — Local LLM inference overview
- [[concepts/capability-based-security]] — Security philosophy matching NemoClaw's approach
- [[concepts/security-and-governance/agent-sandboxing]] — Agent sandboxing patterns
- [[concepts/harness-engineering]] — Harness engineering umbrella

## References

- 2026-04-28_nvidia-nemotron-3-nano-omni

- crawl-2026-04-18-nvidia-speculative-decoding
- crawl-2026-04-23-speculative-decoding-nvidia
