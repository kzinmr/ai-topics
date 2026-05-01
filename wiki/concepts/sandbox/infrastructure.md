---
title: "Infrastructure-Level Sandbox"
type: concept
created: 2026-04-10
updated: 2026-04-16
tags: [concept, ai-agents, security, sandboxing, isolation, coding-agents, infrastructure]
aliases: ["agent-isolation", "ai-sandbox-technologies", "infrastructure-sandbox"]
related: [[concepts/sandbox/in-process]], [[concepts/anthropic-managed-agents]], [[concepts/ai-coding-reliability]], 
depth: L2
status: complete
sources: []
---

# Infrastructure-Level Sandbox

Infrastructure-level sandboxing refers to OS/hypervisor-level isolation technologies used to safely execute AI agent code — particularly LLM-generated or user-supplied code — without compromising the host system, other agents, or sensitive data. As AI agents gain the ability to execute arbitrary commands, access filesystems, and make network requests, sandboxing has become the critical security boundary between useful automation and catastrophic failure.

A Reddit discussion in early 2026 — *"A fair comparison of sandboxing options"* — crystallized the community's understanding that **the "Containers vs. VMs" debate has evolved into a much richer landscape** of isolation strategies, each suited to different threat models and operational constraints.

> **Note**: This page covers infrastructure-level isolation (containers, microVMs, gVisor). For in-process sandboxing, see [[concepts/sandbox/in-process]].

## Why Sandboxing Matters for AI Agents

Unlike traditional software, AI agents present unique security challenges:

1. **Untrusted code generation**: LLMs can (and do) generate code that inadvertently or maliciously performs harmful operations
2. **Ambient authority**: Agents operate with all permissions granted to them regardless of the current task context
3. **Dynamic tool use**: Agents discover and use tools at runtime, making static permission models insufficient
4. **Indirect prompt injection**: Attackers can embed malicious instructions in web content that agents process
5. **Speed of execution**: Agents can perform thousands of operations per second, amplifying the damage of any vulnerability

Simon Willison's **"Lethal Trifecta"** frames the risk: any agent with **access to private data + exposure to untrusted content + an exfiltration vector** is exploitable. Sandboxing addresses the exfiltration vector by containing what the agent can do.

## The Isolation Spectrum

In 2026, five levels of sandbox security have emerged, each trading performance overhead for stronger security boundaries:

### Level 1: Containers (Docker, Podman)

Processes share the host kernel, separated by Linux namespaces and cgroups.

- **Startup**: Fastest (~sub-90ms for Daytona)
- **Overhead**: Lowest — near-native performance
- **Isolation**: Moderate — a kernel vulnerability in one container can compromise all others
- **GPU Support**: Full native support
- **Best for**: Trusted code, single-tenant deployments, SMBs

**Security flags required for production use** (as used by OpenClaw):
- Non-root user — agent processes can't escalate to root inside the container
- Read-only filesystem — prevents modification of agent tools/scripts
- No privileged mode — removes container escape vectors
- Resource limits — prevents CPU/memory exhaustion attacks
- Network restrictions (UFW rules) — limits outbound connections

### Level 2: User-Space Kernels (gVisor)

A user-space application intercepts and re-implements syscalls, so the sandboxed program never talks to the real kernel.

- **Startup**: Slightly slower than native containers
- **Overhead**: 10-30% I/O overhead
- **Isolation**: Strong — syscalls are filtered before reaching the host kernel
- **GPU Support**: Supported via platform mode (Modal)
- **Best for**: Cloud-native deployments, moderate-risk workloads, compute-heavy agents with limited I/O

Used by Google Cloud Run, GKE Sandbox, and Modal for AI workloads. gVisor's Sentry intercepts ~200+ Linux syscalls in user space, providing defense-in-depth without full VM overhead.

### Level 3: Micro-VMs (Firecracker, Kata Containers, libkrun)

Each workload gets its own kernel running on hardware virtualization (KVM).

- **Startup**: ~125ms (Firecracker) to ~500ms (Kata Containers)
- **Overhead**: <5MB memory per VM (Firecracker)
- **Isolation**: Strongest — hardware-level boundary, kernel exploit in one VM cannot reach host
- **GPU Support**: Limited — requires passthrough configuration
- **Best for**: Multi-tenant environments, regulated industries, high-risk workloads

**Firecracker** (AWS, open source) is the reference implementation:
- Powers AWS Lambda and Fargate at scale
- Boots in under 125-200ms
- ~30 emulated devices vs. hundreds in QEMU (minimal attack surface)
- Snapshot/restore capability for fast warm starts
- Used by E2B (200M+ sandboxes), Sprites.dev, and other AI sandbox platforms

**Kata Containers** combines container UX with VM security:
- Kubernetes-native (K8s runtime class)
- Full Linux compatibility
- ~500ms boot time
- Used by Northflank for enterprise deployments

### Level 4: WebAssembly (WASM)

Applications compile to WASM bytecode and run in a sandboxed runtime.

- **Startup**: Near-instant (~1ms)
- **Overhead**: Lowest — near-native performance
- **Isolation**: Strong — sandboxed at the bytecode level
- **GPU Support**: Emerging — limited
- **Best for**: Compute-intensive tasks, specific workloads with predictable behavior

### Level 5: Copy-on-Write Micro-VMs (Zeroboot)

The newest entrant — achieves sub-millisecond spawns (0.79ms) via copy-on-write forking of Firecracker snapshots.

- **Startup**: 190x faster than E2B
- **Memory**: ~265KB per sandbox vs. ~128MB for E2B (~480x density)
- **Isolation**: Hardware-level (Firecracker-based)
- **Best for**: High-throughput ephemeral execution

## Platform Landscape (2026)

The market has split into three layers:

### Layer 1: Primitives (The Raw Materials)

Open-source virtualization technologies you run on your own infrastructure:

| Technology | Stars | Language | License | Approach |
|-----------|-------|----------|---------|----------|
| Firecracker | 33K | Rust | Apache-2.0 | MicroVM VMM |
| gVisor | 18K | Go | Apache-2.0 | Userspace kernel |
| Kata Containers | 7.6K | Rust | Apache-2.0 | OCI runtime + VM |
| Cloud Hypervisor | - | Rust | Apache-2.0 | Minimal VMM |

### Layer 2: Runtimes (Managed Isolation)

Platforms that wrap primitives with developer-friendly APIs:

- **E2B**: Market leader for ephemeral AI sandboxes. Open-source, Firecracker VMs, used by 88% of Fortune 100. ~150ms cold start, 24-hour session limit. Integrates with LangChain, LlamaIndex, and Claude APIs natively.
- **Sprites.dev**: Firecracker-based with checkpoint/rollback capability. Launched January 2026. ~150ms cold start, unlimited sessions.
- **Daytona**: Docker containers by default with optional Kata Containers. Fastest cold starts (<90ms), native Docker compatibility, stateful sandboxes with LSP support, desktop environments for computer-use agents.
- **Microsandbox**: Local-first approach using libkrun microVMs. ~187ms cold start, persistent state, checkpoints.
- **Zeroboot**: Copy-on-write Firecracker forking. 0.79ms p50 spawn latency, ~265KB memory per sandbox.

### Layer 3: Managed Platforms (End-to-End Solutions)

- **Modal**: gVisor isolation optimized for Python ML workloads. Native GPU support. ~2s cold start.
- **Northflank**: Enterprise-grade microVMs with VPC deployment and GPU support. Sub-second cold starts, BYOC deployment.
- **AIO Sandbox** (ByteDance-affiliated): All-in-one approach — browser, shell, IDE, Jupyter, and MCP in a single sandbox. Docker-based.
- **CodeSandbox**: MicroVMs for browser-based development environments.
- **GKE Agent Sandbox**: Native Kubernetes integration with gVisor by default for AI workloads.

## Comparison Matrix

| Platform | Isolation | Cold Start | Persist | GPU | Isolation Level |
|----------|-----------|------------|---------|-----|----------------|
| AIO Sandbox | Docker | ~seconds | — | — | ⭐ Container |
| CodeSandbox | microVMs | ~1s | ✅ | — | ⭐⭐⭐ VM |
| Daytona | Docker | <90ms | ✅ | — | ⭐ Container |
| E2B | Firecracker | ~150ms | — | — | ⭐⭐⭐ VM |
| Microsandbox | libkrun | ~187ms | ✅ | — | ⭐⭐⭐ VM |
| Modal | gVisor | ~2s | — | ✅ | ⭐⭐ Syscall |
| Northflank | Kata/gVisor | ~1s | ✅ | ✅ | ⭐⭐⭐ VM |
| OpenSandbox | Docker/K8s | ~seconds | — | — | ⭐ Container |
| Quilt | Namespaces | ~200ms | — | — | ⭐⭐ Kernel |
| Runloop | Custom hypervisor | ~2s | ✅ | — | ⭐⭐⭐ VM |
| Sprites | Firecracker | ~150ms | ✅ | — | ⭐⭐⭐ VM |
| Zeroboot | Firecracker CoW | 0.79ms | — | — | ⭐⭐⭐ VM |

## Security vs. Performance Tradeoffs

| Dimension | Containers | gVisor | Micro-VMs | WASM |
|-----------|-----------|--------|-----------|------|
| Isolation | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Performance | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| GPU Support | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐ |
| Startup Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Complexity | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |

## Which Sandbox for Which Use Case?

### Coding Agents (Claude Code, Cursor, Gemini CLI)

**Needs**: Filesystem access, network access, package installation, terminal execution

**Recommendation**: 
- **Trusted code** (your own codebase): Hardened Docker with all 5 security flags
- **Untrusted code** (LLM-generated, community plugins): Firecracker micro-VMs or gVisor
- **GPU-intensive tasks**: Modal (gVisor with GPU support) or Northflank (Kata with GPU)

### Browser Agents (Claude Computer Use, ChatGPT Atlas, OpenAI Operator)

**Needs**: Full browser environment, network access, cookie/session isolation

**Recommendation**: 
- Firecracker micro-VMs with network restrictions
- GKE Agent Sandbox (gVisor) for Kubernetes deployments
- Trail of Bits recommends extending Same-Origin Policy to AI agents as a minimum

### Data Analysis Agents

**Needs**: Access to datasets, compute resources, output generation

**Recommendation**:
- E2B for ephemeral execution (Firecracker)
- Sprites for persistent sessions with checkpoint/rollback
- Docker with resource limits for trusted workloads

### Multi-Agent Swarms

**Needs**: Inter-agent communication, shared state, coordinated execution

**Recommendation**:
- Northflank (VPC deployment with microVMs)
- Modal (serverless with GPU support)
- E2B + custom orchestration layer

## Defense-in-Depth Architecture

The 2026 consensus is that **no single sandbox is sufficient**. Production systems need layered defense:

1. **Compute isolation**: MicroVM or gVisor sandbox for untrusted code
2. **Filesystem restrictions**: Read-only mounts, no sensitive file access
3. **Network controls**: Domain allowlisting, egress monitoring, no unrestricted outbound
4. **Resource limits**: CPU/memory caps to prevent exhaustion attacks
5. **Input sanitization**: Strip HTML metadata before injecting fetched content (defends against silent egress attacks)
6. **Audit logging**: Every request and response logged for post-session forensics
7. **Policy enforcement**: YAML-based deny-by-default policies for tool access

As Blake Crosley's analysis notes: *"The minimum viable defense is a URL allowlist and an egress log. Start there."*

## Key Takeaways

1. **For LLM-generated code execution, microVMs (Firecracker, Kata) are the only production-safe isolation layer.** Containers are insufficient for truly hostile code.
2. **The market has converged on specialized AI sandbox platforms** (E2B, Daytona, Sprites) rather than general container orchestrators.
3. **Cold start latency (90ms-200ms) is now acceptable** for most agent use cases.
4. **Defense in depth is non-negotiable**: compute isolation + filesystem restrictions + network controls + resource limits.
5. **Sandboxed agents reduce security incidents by ~90%** compared to agents with unrestricted host access.

## Related Concepts

- [[concepts/anthropic-managed-agents]] — Managed agent services and their sandboxing approaches
- [[concepts/ai-coding-reliability]] — Ensuring AI-generated code is correct and safe
-  — The practice of directing AI agents in software development- [[concepts/claude-mythos-glasswing]] — Anthropic's internal agent architecture
- [[concepts/ai-agent-traps]] — Common pitfalls in agent deployment

## Sources

- [Manveer Chawla: "How to sandbox AI agents in 2026"](https://manveerc.substack.com/p/ai-agent-sandboxing-guide) (February 2026)
- [ManageMyClaw: "AI Agent Sandboxing 2026: MicroVM vs Docker"](https://managemyclaw.com/blog/ai-agent-sandboxing-2026/) (March 2026)
- [Ry Walker Research: "AI Agent Sandboxes Compared"](http://rywalker.com/research/ai-agent-sandboxes) (2026)
- [Ry Walker Research: "Container-to-VM Runtimes Compared"](http://rywalker.com/research/container-vm-runtimes) (2026)
- [Zylos Research: "AI Agent Sandbox & Code Execution Isolation"](https://zylos.ai/research/2026-02-21-ai-agent-sandbox-execution-isolation) (February 2026)
- [Reddit: "A fair comparison of sandboxing options"](https://www.reddit.com/r/LocalLLM/comments/1ly245x/a_fair_comparison_of_sandboxing_options/) (2026)
- [Blake Crosley: "Silent Egress: The Attack Surface You Didn't Build"](https://blakecrosley.com/blog/silent-egress-attack-surface) (2026)
- [Trail of Bits: "Lack of isolation in agentic browsers resurfaces old vulnerabilities"](https://blog.trailofbits.com/2026/01/13/lack-of-isolation-in-agentic-browsers-resurfaces-old-vulnerabilities/) (January 2026)
